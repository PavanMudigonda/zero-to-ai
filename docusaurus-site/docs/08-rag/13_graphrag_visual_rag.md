---
title: "14. GraphRAG Visual RAG"
sidebar_label: "14. GraphRAG Visual RAG"
sidebar_position: 12
format: "md"
---
# GraphRAG and Visual RAG (Microsoft GraphRAG + ColPali)

This notebook covers two frontier RAG techniques that tackle the hardest failure modes of standard vector RAG:

**Section A — Microsoft GraphRAG**: For thematic, aggregate, and community-level queries that span entire document collections

**Section B — ColPali Visual Document RAG**: For PDFs with tables, charts, infographics, and complex layouts where OCR-based text extraction destroys meaning

---

> **Prerequisites**: OpenAI API key, Python 3.10+, sufficient disk space (~2GB for model downloads)

---

# Section A: Microsoft GraphRAG

## A.1 Why GraphRAG Exists: The Failure Mode of Vector RAG

Consider a corpus of 500 news articles about climate change. A user asks:

> *"What are the main themes and competing perspectives in these documents?"*

**Vector RAG fails here because**:
- No single chunk contains "all themes"
- Top-k retrieval finds the most similar chunks, but similarity ≠ thematic coverage
- The answer requires understanding relationships ACROSS the entire corpus

**GraphRAG's approach**: Extract a knowledge graph from all documents, then use community detection to find natural topic clusters, generate hierarchical summaries of each community, and answer queries using these summaries.

### Query Types

| Query Type | Example | Best Approach |
|-----------|---------|---------------|
| **Global / thematic** | "What are the main themes?" | GraphRAG Global Search |
| **Entity-specific** | "What do documents say about Elon Musk?" | GraphRAG Local Search |
| **Specific fact** | "What is Tesla's revenue?" | Vector RAG |
| **Multi-doc holistic** | "How has the narrative evolved over time?" | GraphRAG Global |
| **Abstract summary** | "What is the main argument?" | RAPTOR or GraphRAG |

## A.2 GraphRAG Architecture

```
Input Documents
     │
     ▼
┌─────────────────────────────────────┐
│  Phase 1: Graph Extraction          │
│  LLM extracts: entities + relations │
│  ("Google" --acquired--> "YouTube") │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│  Phase 2: Community Detection       │
│  Leiden algorithm finds clusters    │
│  Community 1: Cloud companies       │
│  Community 2: AI researchers        │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│  Phase 3: Community Summarization   │
│  LLM writes summaries per community │
│  at multiple granularity levels     │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│  Query Time                         │
│  Local: entity graph traversal      │
│  Global: summarize community sums   │
│  DRIFT: iterative query refinement  │
└─────────────────────────────────────┘
```

```python
# Install Microsoft GraphRAG
!pip install -q graphrag
!pip install -q python-dotenv openai
```

```python
import os
import json
import pathlib

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_KEY")
print("OpenAI key set:", bool(OPENAI_API_KEY and OPENAI_API_KEY != "YOUR_OPENAI_KEY"))
```

## A.3 Setting Up a GraphRAG Project

A GraphRAG project requires a specific directory structure: an `input/` folder for source documents, a `settings.yaml` configuration file that defines the LLM, embedding model, chunk sizes, and graph construction parameters, and an output directory where the knowledge graph and community reports will be stored. The cell below creates this structure programmatically. The `graphrag.index` CLI will later walk this directory, process every document in `input/`, and build the entity-relationship graph that powers global and local search.

```python
# Step 1: Create a working directory for the GraphRAG project
import os
import pathlib

PROJECT_ROOT = "/tmp/graphrag_project"
INPUT_DIR = os.path.join(PROJECT_ROOT, "input")

os.makedirs(INPUT_DIR, exist_ok=True)
print(f"Project directory: {PROJECT_ROOT}")
print(f"Input directory:   {INPUT_DIR}")
```

```python
# Step 2: Create sample documents for GraphRAG to process
# We'll use a fictional technology industry corpus

DOCUMENTS = {
    "cloud_wars.txt": """
The Cloud Computing Wars: Amazon, Microsoft, and Google

Amazon Web Services, founded by Andy Jassy and launched in 2006, pioneered the cloud computing
industry. AWS introduced the concept of renting computing infrastructure on demand, transforming
how companies build software. Amazon CEO Jeff Bezos championed the initiative despite initial
skepticism from the board.

Microsoft Azure, launched in 2010 under CEO Steve Ballmer, initially struggled to compete with AWS.
The transformation came when Satya Nadella became CEO in 2014. Nadella's "mobile-first, cloud-first"
strategy revitalized Microsoft. Azure grew to become the second-largest cloud provider by 2018,
capturing 20% market share.

Google Cloud Platform (GCP), led by Diane Greene and later Thomas Kurian, focused on data analytics
and machine learning capabilities. Google's expertise in distributed systems, built over decades
running Search and Gmail, gave GCP unique technical advantages. However, GCP struggled with
enterprise sales, a domain where AWS and Azure had stronger relationships.

The cloud market reached $500 billion in 2023. AWS holds 32% market share, Azure 22%, and GCP 11%.
The remaining 35% is fragmented among dozens of smaller providers including Alibaba Cloud,
Oracle Cloud, and IBM Cloud.
""",
    
    "ai_race.txt": """
The Artificial Intelligence Race: OpenAI, Google DeepMind, and Anthropic

OpenAI, founded in 2015 by Sam Altman, Elon Musk, Greg Brockman, and others, began as a
nonprofit focused on safe AI development. The release of GPT-3 in 2020 marked a turning point,
demonstrating unprecedented language capabilities. ChatGPT's launch in November 2022 became
the fastest product in history to reach 100 million users — achieving this in just 2 months.

Google DeepMind, formed from the 2023 merger of Google Brain and DeepMind, combined the
resources of two world-class AI labs. DeepMind, founded by Demis Hassabis in London in 2010,
was known for AlphaGo, AlphaFold, and Gemini. The merged entity, led by Hassabis, became
one of the most well-resourced AI labs globally.

Anthropic, founded by Dario Amodei, Daniela Amodei, and other OpenAI alumni in 2021, focused
on AI safety research. Their Constitutional AI approach aimed to create helpful, harmless, and
honest AI systems. Claude, Anthropic's AI assistant, was designed with safety guardrails from
the ground up. Amazon invested $4 billion in Anthropic in 2023.

The competition between these labs accelerated in 2024-2025, with each releasing increasingly
capable foundation models. The industry faced existential questions about compute resources,
energy consumption, and the path to AGI.
""",
    
    "semiconductor_supply.txt": """
The Semiconductor Supply Chain Crisis and AI Chip Dominance

NVIDIA, under CEO Jensen Huang, transformed from a gaming graphics company to the dominant
supplier of AI training chips. The H100 GPU, launched in 2022, became the gold standard for
training large language models. NVIDIA's CUDA software ecosystem, built over 15 years, created
a powerful moat. By 2024, NVIDIA's market cap exceeded $3 trillion.

The 2020-2022 global semiconductor shortage exposed critical vulnerabilities in the supply chain.
TSMC (Taiwan Semiconductor Manufacturing Company), founded by Morris Chang, manufactures over
90% of the world's most advanced chips. This concentration in Taiwan created geopolitical risk
as tensions between the US and China intensified.

The CHIPS and Science Act of 2022, signed by President Biden, allocated $52 billion to boost
US semiconductor manufacturing. Intel, AMD, and TSMC all announced new US-based fab investments.
Samsung invested $17 billion in a new Texas facility. These investments represented a fundamental
shift in semiconductor geopolitics.

AMD, under CEO Lisa Su, emerged as NVIDIA's primary competitor in AI chips. The MI300X accelerator
offered competitive performance at lower prices, attracting Microsoft, Meta, and Google as customers.
AMD's market cap grew from $2 billion in 2019 to over $200 billion by 2024.
"""
}

# Write documents to input directory
for filename, content in DOCUMENTS.items():
    filepath = os.path.join(INPUT_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(content.strip())

print(f"Created {len(DOCUMENTS)} documents in {INPUT_DIR}:")
for name in DOCUMENTS:
    print(f"  - {name}")
```

```python
# Step 3: Initialize GraphRAG project
# This creates the required directory structure and default configuration

import subprocess

result = subprocess.run(
    ["python", "-m", "graphrag", "init", "--root", PROJECT_ROOT],
    capture_output=True, text=True
)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr[:500] if result.stderr else "")
print("Return code:", result.returncode)

# List created files
print("\nCreated project structure:")
for root, dirs, files in os.walk(PROJECT_ROOT):
    # Skip deep cache dirs
    dirs[:] = [d for d in dirs if d not in ['cache', '__pycache__', 'output']]
    level = root.replace(PROJECT_ROOT, '').count(os.sep)
    indent = '  ' * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = '  ' * (level + 1)
    for file in files:
        print(f"{subindent}{file}")
```

## A.4 Configuring settings.yaml

The `settings.yaml` file controls:
- Which LLM to use for entity extraction and summarization
- Which embeddings model to use
- Storage backend (local files, Azure Blob, S3)
- Chunking parameters
- Community detection settings

```python
# Configure settings.yaml for OpenAI
# GraphRAG uses YAML configuration

settings_yaml = f"""encoding_model: cl100k_base
skip_workflows: []
llm:
  api_key: {OPENAI_API_KEY}
  type: openai_chat
  model: gpt-4o-mini
  model_supports_json: true
  max_tokens: 4000
  request_timeout: 180.0
  api_base: null
  api_version: null
  organization: null
  proxy: null
  cognitive_services_endpoint: null
  deployment_name: null
  tokens_per_minute: 150000
  requests_per_minute: 10000
  max_retries: 10
  max_retry_wait: 10.0
  sleep_on_rate_limit_recommendation: true
  concurrent_requests: 25

parallelization:
  stagger: 0.3
  num_threads: 50

async_mode: threaded

embeddings:
  async_mode: threaded
  llm:
    api_key: {OPENAI_API_KEY}
    type: openai_embedding
    model: text-embedding-3-small
    max_retries: 10

chunks:
  size: 1200
  overlap: 100
  group_by_columns: [id]

input:
  type: file
  file_type: text
  base_dir: "input"
  file_encoding: utf-8
  file_pattern: ".*\\.txt$"

cache:
  type: file
  base_dir: "cache"

storage:
  type: file
  base_dir: "output"

reporting:
  type: file
  base_dir: "output/reports"

entity_extraction:
  prompt: "prompts/entity_extraction.txt"
  entity_types: [organization, person, technology, event, location]
  max_gleanings: 1

summarize_descriptions:
  prompt: "prompts/summarize_descriptions.txt"
  max_length: 500

claim_extraction:
  enabled: false

community_reports:
  prompt: "prompts/community_report.txt"
  max_length: 2000
  max_input_length: 8000

cluster_graph:
  max_cluster_size: 10

embed_graph:
  enabled: false

umap:
  enabled: false

snapshots:
  graphml: false
  raw_entities: false
  top_level_nodes: false

local_search:
  text_unit_prop: 0.5
  community_prop: 0.1
  conversation_history_max_turns: 5
  top_k_mapped_entities: 10
  top_k_relationships: 10
  max_tokens: 12000

global_search:
  max_tokens: 12000
  data_max_tokens: 12000
  map_max_tokens: 1000
  reduce_max_tokens: 2000
  concurrency: 32
"""

settings_path = os.path.join(PROJECT_ROOT, "settings.yaml")
with open(settings_path, 'w') as f:
    f.write(settings_yaml)

print(f"settings.yaml written to: {settings_path}")
```

## A.5 Running the Indexing Pipeline

The indexing pipeline performs:
1. **Text Unit extraction**: Split documents into overlapping chunks
2. **Entity & Relationship extraction**: LLM identifies entities and their relationships
3. **Entity summarization**: Consolidate descriptions for entities appearing in multiple chunks
4. **Graph construction**: Build a NetworkX graph from entities and relationships
5. **Community detection**: Run Leiden algorithm to find entity communities
6. **Community summarization**: LLM writes reports for each community at each level
7. **Embedding**: Embed text units and entity descriptions

> **Cost Warning**: The indexing pipeline makes MANY LLM calls. For our 3-document corpus:
> - ~30-50 LLM calls for entity extraction
> - ~20-30 LLM calls for summarization
> - ~10-20 LLM calls for community reports
>
> Estimated cost: $0.05–$0.50 with gpt-4o-mini. For large corpora (1000+ docs), budget $10–$100+.

```python
# Run the GraphRAG indexing pipeline
# This can take 2-10 minutes depending on document size and API rate limits

print("Starting GraphRAG indexing pipeline...")
print("This will make multiple OpenAI API calls.")
print("Progress will be shown below:\n")

result = subprocess.run(
    ["python", "-m", "graphrag", "index", "--root", PROJECT_ROOT],
    capture_output=True, text=True,
    timeout=600  # 10 minute timeout
)

# Print last 100 lines of output
lines = result.stdout.split('\n')
print('\n'.join(lines[-50:]))

if result.returncode != 0:
    print("\nERROR OUTPUT:")
    print(result.stderr[-1000:])
else:
    print("\nIndexing completed successfully!")
```

```python
# Inspect the indexing output
output_dir = os.path.join(PROJECT_ROOT, "output")

print("Indexing outputs:")
for root, dirs, files in os.walk(output_dir):
    dirs[:] = sorted(dirs)
    level = root.replace(output_dir, '').count(os.sep)
    indent = '  ' * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = '  ' * (level + 1)
    for file in sorted(files):
        filepath = os.path.join(root, file)
        size = os.path.getsize(filepath)
        print(f"{subindent}{file} ({size:,} bytes)")
```

## A.6 Local Search vs Global Search

GraphRAG offers two distinct query modes:

**Local Search**: Entity-centric. Finds the most relevant entities, then traverses their relationships and associated text units. Best for questions about specific people, organizations, or events.

**Global Search**: Community-centric. Uses the hierarchical community summaries to answer broad, thematic questions. Best for "What are the main themes?" style questions.

**DRIFT Search** (2025): Dynamic Iterative Refinement via Follow-up Thought. Starts local, iteratively refines the query based on what it discovers. Best for complex exploratory questions.

```python
# GraphRAG Query via Python API
# Note: This requires the indexing pipeline to have completed successfully

import asyncio
import pandas as pd

# GraphRAG stores results as Parquet files
# We need to load these to build the search context

def find_output_folder(project_root: str) -> str:
    """Find the timestamped output folder created by GraphRAG."""
    output_base = os.path.join(project_root, "output")
    if not os.path.exists(output_base):
        raise FileNotFoundError(f"Output directory not found: {output_base}")
    
    # Find the artifacts directory
    for root, dirs, files in os.walk(output_base):
        for f in files:
            if f == "entities.parquet":
                return root
    raise FileNotFoundError("entities.parquet not found — indexing may not have completed")

try:
    artifacts_dir = find_output_folder(PROJECT_ROOT)
    print(f"Found artifacts at: {artifacts_dir}")
    
    # Load key data structures
    entities_df = pd.read_parquet(os.path.join(artifacts_dir, "entities.parquet"))
    relationships_df = pd.read_parquet(os.path.join(artifacts_dir, "relationships.parquet"))
    communities_df = pd.read_parquet(os.path.join(artifacts_dir, "communities.parquet"))
    community_reports_df = pd.read_parquet(os.path.join(artifacts_dir, "community_reports.parquet"))
    
    print(f"\nExtracted:")
    print(f"  Entities:            {len(entities_df)}")
    print(f"  Relationships:       {len(relationships_df)}")
    print(f"  Communities:         {len(communities_df)}")
    print(f"  Community Reports:   {len(community_reports_df)}")
    
    print(f"\nSample entities:")
    print(entities_df[['title', 'type', 'description']].head(10).to_string(index=False))

except FileNotFoundError as e:
    print(f"Indexing not yet complete or failed: {e}")
    print("Run the indexing cell above first.")
```

```python
# Inspect relationships extracted by GraphRAG
try:
    print("Sample relationships (entity graph edges):")
    print(relationships_df[['source', 'target', 'description', 'weight']].head(15).to_string(index=False))
    
    print("\nCommunity structure:")
    print(communities_df[['community', 'level', 'title', 'entity_ids']].head(10).to_string(index=False))

except NameError:
    print("DataFrames not loaded — run the indexing pipeline first.")
```

```python
# GraphRAG Local Search via Python API
# Local search: find specific entities and their neighborhood

try:
    from graphrag.query.api import local_search

    async def run_local_search(query: str):
        result = await local_search(
            config_filepath=os.path.join(PROJECT_ROOT, "settings.yaml"),
            data_dir=artifacts_dir,
            root_dir=PROJECT_ROOT,
            community_level=2,
            response_type="multiple paragraphs",
            query=query
        )
        return result

    # Run local search
    local_query = "What role did Satya Nadella play in Microsoft's cloud strategy?"
    print(f"LOCAL SEARCH QUERY: {local_query}")
    print("=" * 70)

    local_result = asyncio.run(run_local_search(local_query))
    print(local_result.response)

except ImportError:
    print("graphrag.query.api not available in this version.")
    print("Try CLI: python -m graphrag query --root ./graphrag_project --method local --query '...'")
except Exception as e:
    print(f"Error: {e}")
    print("Ensure indexing completed successfully before running queries.")
```

```python
# GraphRAG Global Search via Python API
# Global search: uses community summaries to answer thematic questions

try:
    from graphrag.query.api import global_search

    async def run_global_search(query: str):
        result = await global_search(
            config_filepath=os.path.join(PROJECT_ROOT, "settings.yaml"),
            data_dir=artifacts_dir,
            root_dir=PROJECT_ROOT,
            community_level=2,
            response_type="multiple paragraphs",
            query=query
        )
        return result

    # Global search: thematic question across the entire corpus
    global_query = "What are the main themes and competitive dynamics in the technology industry based on these documents?"
    print(f"GLOBAL SEARCH QUERY: {global_query}")
    print("=" * 70)

    global_result = asyncio.run(run_global_search(global_query))
    print(global_result.response)

except ImportError:
    print("Use CLI for global search:")
    print(f"python -m graphrag query --root {PROJECT_ROOT} --method global --query 'What are the main themes?'")
except Exception as e:
    print(f"Error: {e}")
```

```python
# GraphRAG via CLI (most reliable interface across versions)
# These are the exact commands to use in your terminal

cli_commands = {
    "Local search": (
        f"python -m graphrag query "
        f"--root {PROJECT_ROOT} "
        f"--method local "
        f"--query 'What role did Jensen Huang play in NVIDIA becoming an AI chip leader?'"
    ),
    "Global search": (
        f"python -m graphrag query "
        f"--root {PROJECT_ROOT} "
        f"--method global "
        f"--query 'What are the main themes across these technology documents?'"
    ),
    "DRIFT search": (
        f"python -m graphrag query "
        f"--root {PROJECT_ROOT} "
        f"--method drift "
        f"--query 'How are cloud computing, AI, and semiconductors interconnected?'"
    )
}

print("GraphRAG CLI commands:")
print("=" * 70)
for name, cmd in cli_commands.items():
    print(f"\n[{name}]")
    print(cmd)
```

## A.7 DRIFT Search (2025 Addition)

**DRIFT** (Dynamic Iterative Refinement via Follow-up Thought) was added to GraphRAG in 2025. It addresses a gap between local and global search:

- **Local search** is great for known entities but misses broader context
- **Global search** covers themes but lacks depth for specific questions
- **DRIFT** starts with a local query, identifies follow-up questions, answers them, and synthesizes everything

```
User query: "How does NVIDIA's dominance affect the AI lab competition?"

DRIFT Step 1: Local search for NVIDIA → finds GPU facts, H100, Jensen Huang
DRIFT Step 2: LLM generates follow-up: "Which AI labs use NVIDIA GPUs?"
DRIFT Step 3: Local search for OpenAI, DeepMind, Anthropic + GPU usage
DRIFT Step 4: Synthesize all findings into a comprehensive answer
```

DRIFT produces more complete answers for complex analytical questions that span multiple entity neighborhoods.

```python
# Comparing all three search modes

comparison_table = {
    "Feature": ["Primary data source", "Best for", "Answer style", "LLM calls", "Cost", "Speed"],
    "Local Search": [
        "Entity graph + text units",
        "Questions about specific entities",
        "Detailed, entity-focused",
        "~5-10",
        "$",
        "Fast"
    ],
    "Global Search": [
        "Community summaries",
        "Thematic/aggregate questions",
        "High-level, balanced",
        "~20-50 (map+reduce)",
        "$$$",
        "Slow"
    ],
    "DRIFT Search": [
        "Entity graph + iterative local",
        "Complex exploratory questions",
        "Comprehensive, multi-hop",
        "~15-30",
        "$$",
        "Medium"
    ]
}

import pandas as pd
df = pd.DataFrame(comparison_table).set_index("Feature")
print("GraphRAG Search Mode Comparison:")
print(df.to_string())
```

## A.8 When to Use GraphRAG vs Other Methods

| Scenario | Recommended Approach | Reason |
|----------|---------------------|--------|
| "What does the document say about X?" | Vector RAG | Fast, cheap, accurate for specific facts |
| "Summarize this 100-page report" | RAPTOR | Hierarchical summaries without graph overhead |
| "What are the main themes across 500 docs?" | **GraphRAG Global** | Only way to get thematic coverage |
| "How is entity X connected to entity Y?" | **GraphRAG Local** | Explicit graph traversal |
| "What caused the 2008 financial crisis?" (corpus of books) | **GraphRAG + DRIFT** | Complex causal chains spanning many sources |
| Low budget or time constraints | Vector RAG + Reranking | Good enough for most queries, much cheaper |

**Cost considerations**:
- GraphRAG indexing: **expensive** (many LLM calls per document)
- GraphRAG global search: **expensive** (map-reduce over all community summaries)
- Vector RAG: **cheap** (embeddings + 1 LLM call per query)
- Budget: GraphRAG indexing ~$1/100 docs with gpt-4o-mini; $10+/100 docs with gpt-4o

---

# Section B: ColPali Visual Document RAG

## B.1 Why OCR-Based RAG Fails on Visual Documents

Most RAG systems handle PDFs by:
1. Extract text with OCR or PDF parsers (PyMuPDF, pdfplumber)
2. Chunk the text
3. Embed and index

**This pipeline destroys information** in visually rich documents:

| Document Element | OCR Behavior | Information Lost |
|-----------------|--------------|------------------|
| Tables | Garbled text fragments | Row/column relationships |
| Charts/graphs | Ignored entirely | All quantitative information |
| Infographics | Partial text extraction | Visual hierarchy, arrows, layout |
| Multi-column PDFs | Mixed column order | Reading flow |
| Scanned PDFs | OCR errors | Accuracy of facts |
| Equations | Symbol substitution | Mathematical meaning |

**Example failure**: A financial report PDF has a bar chart showing quarterly revenue. OCR extracts the axis labels as scattered text fragments. A query "What was Q3 revenue?" fails because the data was never captured as text.

## B.2 The ColPali Architecture

ColPali (Column-wise Late Interaction for Page Images) treats each **PDF page as an image** and applies ColBERT-style late interaction retrieval:

```
PDF Document
     │
     ▼
Page Images (one per page)
     │
     ▼
PaliGemma Vision Encoder
(produces 1030 patch embeddings per page, each 128-dim)
     │
     ▼
Page Embeddings Matrix: (1030, 128)

Query Text
     │
     ▼
Language Encoder
(produces ~20 token embeddings)
     │
     ▼
Query Embeddings Matrix: (N_tokens, 128)

Similarity = MaxSim(Query_Embeddings, Page_Embeddings)
```

**ColQwen2.5** (2025) is the current state-of-the-art variant, replacing PaliGemma with Qwen2.5-VL as the vision encoder.

```python
# Install ColPali dependencies
!pip install -q colpali-engine
!pip install -q pdf2image pillow pymupdf
!pip install -q torch torchvision  # required for ColPali

# Note: ColQwen2.5 requires ~8GB GPU VRAM or will run slowly on CPU
# For CPU-only systems, use a smaller variant or use the quantized version
```

```python
import torch
import warnings
warnings.filterwarnings('ignore')

# Check available hardware
if torch.cuda.is_available():
    device = "cuda"
    print(f"GPU available: {torch.cuda.get_device_name(0)}")
    print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
    device = "mps"  # Apple Silicon
    print("Apple Silicon MPS available")
else:
    device = "cpu"
    print("Running on CPU — inference will be slow for ColPali")

print(f"\nUsing device: {device}")
print(f"Torch version: {torch.__version__}")
```

## B.3 Loading ColQwen2.5

**ColQwen2.5** is a state-of-the-art visual retrieval model from the ColPali family that generates multi-vector embeddings directly from page images, bypassing OCR and text extraction entirely. Built on the Qwen2-VL vision-language backbone, it encodes each page as a grid of patch-level embeddings that capture both textual and visual layout information. The model is loaded via the `colpali_engine` library using `ColQwen2_5` and its companion processor. At approximately 8 GB, the download is substantial but the resulting embeddings enable retrieval over visually rich documents -- charts, tables, infographics -- that traditional text-only RAG cannot handle.

```python
# Load ColQwen2.5 model
# ColQwen2.5 is the 2025 state-of-the-art visual retrieval model
# Model: vidore/colqwen2.5-v0.2 (~8GB download)

from colpali_engine.models import ColQwen2_5, ColQwen2_5_Processor

MODEL_NAME = "vidore/colqwen2.5-v0.2"

print(f"Loading ColQwen2.5 model: {MODEL_NAME}")
print("First load downloads ~8GB. Subsequent loads use cache.")
print("This may take 5-15 minutes on first run...")

# Load model
model = ColQwen2_5.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.bfloat16,  # use bfloat16 to reduce memory
    device_map=device
).eval()

# Load processor (handles image preprocessing and tokenization)
processor = ColQwen2_5_Processor.from_pretrained(MODEL_NAME)

print(f"\nModel loaded successfully!")
print(f"Parameters: {sum(p.numel() for p in model.parameters()) / 1e9:.2f}B")
```

## B.4 Indexing PDF Pages as Images

Visual RAG treats each PDF page as an image rather than extracting text. The page image is passed through the ColQwen2.5 model, which produces a sequence of patch embeddings (one per image region). These patch embeddings are stored as the document's representation in the index. At query time, the same model encodes the text query into a compatible embedding space, and **MaxSim scoring** (the maximum similarity between any query token and any page patch) determines relevance. This approach preserves spatial layout, font emphasis, and graphical elements that are lost by OCR.

```python
# Create a sample PDF with visual elements for demonstration
# In practice, you would load your own PDFs

from PIL import Image, ImageDraw, ImageFont
import io
import os

def create_sample_page_image(page_num: int, content: str, width: int = 800, height: int = 1100) -> Image.Image:
    """Create a simple page image simulating a document page."""
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw page border
    draw.rectangle([20, 20, width-20, height-20], outline='black', width=2)
    
    # Draw page number
    draw.text((width//2 - 30, height - 50), f"Page {page_num}", fill='gray')
    
    # Draw content (simplified - in real docs this comes from PDF rendering)
    lines = content.split('\n')
    y = 60
    for line in lines:
        if line.strip():
            # Title detection
            if line.startswith('##'):
                draw.text((40, y), line.replace('##', '').strip(), fill='darkblue')
                y += 35
            elif line.startswith('#'):
                draw.text((40, y), line.replace('#', '').strip(), fill='black')
                y += 40
            else:
                # Word wrap at 90 chars
                words = line.split()
                current_line = ""
                for word in words:
                    if len(current_line) + len(word) < 85:
                        current_line += word + " "
                    else:
                        if current_line:
                            draw.text((40, y), current_line.strip(), fill='black')
                            y += 22
                        current_line = word + " "
                if current_line:
                    draw.text((40, y), current_line.strip(), fill='black')
                    y += 22
        else:
            y += 15  # paragraph spacing
        
        if y > height - 80:
            break
    
    return img

# Sample multi-page document content
page_contents = [
    """# Annual Financial Report 2024
## Executive Summary

NexCloud Inc. achieved record revenue of $8.2 billion in fiscal year 2024,
representing 23% year-over-year growth. The AI division was the primary
growth driver, contributing $2.87 billion (35% of total revenue).

Key highlights:
- Total revenue: $8.2B (up 23% YoY)
- Net income: $1.4B (up 45% YoY)
- Employee count: 45,000 across 30 countries
- Market capitalization: $120B as of December 2024

The board approved a $500M share buyback program.""",
    
    """# Revenue Breakdown by Segment
## Quarterly Performance

Q1 2024: $1.8B total revenue
  Cloud Storage:  $980M
  AI Services:    $620M
  Enterprise:     $200M

Q2 2024: $2.0B total revenue
  Cloud Storage:  $1.05B
  AI Services:    $720M
  Enterprise:     $230M

Q3 2024: $2.1B total revenue (record quarter)
  Cloud Storage:  $1.10B
  AI Services:    $760M
  Enterprise:     $240M

Q4 2024: $2.3B total revenue
  Cloud Storage:  $1.15B
  AI Services:    $890M
  Enterprise:     $260M

Full year AI revenue: $2.87B representing 35% of total revenue""",
    
    """# Geographic Revenue Distribution
## Regional Performance 2024

North America: $4.1B (50% of total)
Europe: $2.05B (25% of total)
Asia Pacific: $1.64B (20% of total)
Rest of World: $0.41B (5% of total)

## Key Strategic Developments

The company opened three new data centers in Singapore, Frankfurt, and
Toronto during 2024. These expansions support AI workloads requiring
low-latency access for enterprise customers.

Dr. James Park, CEO, stated: "The AI transition is accelerating faster
than we projected. We are investing $2B in compute infrastructure for 2025."

The company also announced a partnership with NVIDIA for priority access
to H100 and B100 GPU clusters, securing $800M in hardware commitments."""
]

# Generate page images
sample_pages = []
for i, content in enumerate(page_contents):
    img = create_sample_page_image(i + 1, content)
    sample_pages.append(img)

print(f"Created {len(sample_pages)} sample document pages")
print(f"Page dimensions: {sample_pages[0].size}")
```

```python
# Index pages with ColPali
# This produces multi-vector embeddings for each page

from torch.utils.data import DataLoader
import numpy as np

def index_pages_with_colpali(
    pages: list,  # list of PIL Images
    model,
    processor,
    batch_size: int = 2
) -> list[torch.Tensor]:
    """
    Generate ColPali multi-vector embeddings for each page.
    
    Returns a list of tensors, one per page.
    Each tensor has shape (N_patches, embedding_dim).
    For ColQwen2.5: ~1030 patches, 128-dim each.
    """
    all_page_embeddings = []
    
    for i in range(0, len(pages), batch_size):
        batch = pages[i:i + batch_size]
        
        # Preprocess images
        batch_inputs = processor.process_images(batch)
        batch_inputs = {k: v.to(model.device) for k, v in batch_inputs.items()}
        
        # Generate embeddings
        with torch.no_grad():
            embeddings = model(**batch_inputs)  # (batch, n_patches, dim)
        
        # Store per-page embeddings
        for emb in embeddings:
            all_page_embeddings.append(emb.cpu().float())
        
        print(f"  Indexed pages {i+1} to {min(i+batch_size, len(pages))} of {len(pages)}")
    
    return all_page_embeddings

print("Indexing document pages with ColQwen2.5...")
print("Each page generates ~1030 patch embeddings (128-dim each)\n")

page_embeddings = index_pages_with_colpali(sample_pages, model, processor)

print(f"\nIndexing complete:")
print(f"  Pages indexed:              {len(page_embeddings)}")
print(f"  Patches per page (approx):  {page_embeddings[0].shape[0]}")
print(f"  Embedding dimension:        {page_embeddings[0].shape[1]}")
print(f"  Total vectors stored:       {sum(e.shape[0] for e in page_embeddings):,}")
print(f"  Memory per page:            {page_embeddings[0].numel() * 4 / 1024:.1f} KB")
```

## B.5 Querying: MaxSim Scoring Over Page Embeddings

**MaxSim** (Maximum Similarity) is the scoring function used by ColPali-family models. For each query token embedding, it finds the most similar patch embedding on the page, then sums these maximum similarities across all query tokens. Formally, for query tokens $\{q_1, \ldots, q_m\}$ and page patches $\{p_1, \ldots, p_n\}$:

$$\text{MaxSim}(Q, P) = \sum_{i=1}^{m} \max_{j=1}^{n} \, q_i \cdot p_j$$

This late-interaction scoring is more expressive than a single-vector dot product because it allows fine-grained token-to-patch matching, enabling the model to attend to specific regions of a page that are relevant to the query.

```python
# Encode a text query and compute MaxSim scores

def query_colpali(
    query: str,
    page_embeddings: list[torch.Tensor],
    model,
    processor,
    top_k: int = 3
) -> list[dict]:
    """
    Query ColPali with a text query.
    
    1. Encode query to multi-vector representation
    2. Compute MaxSim score against each page
    3. Return top-k pages sorted by score
    """
    # Encode query
    query_inputs = processor.process_queries([query])
    query_inputs = {k: v.to(model.device) for k, v in query_inputs.items()}
    
    with torch.no_grad():
        query_embeddings = model(**query_inputs)  # (1, n_query_tokens, dim)
    
    query_emb = query_embeddings[0].cpu().float()  # (n_query_tokens, dim)
    
    # Compute MaxSim scores against all pages
    # model.score_multi_vector handles the MaxSim computation
    scores = model.score_multi_vector(
        qs=[query_emb],          # list of query embeddings
        ps=page_embeddings       # list of page patch embeddings
    )
    
    scores_array = scores[0].numpy()  # (n_pages,)
    
    # Get top-k pages
    top_indices = np.argsort(scores_array)[::-1][:top_k]
    
    results = []
    for rank, idx in enumerate(top_indices):
        results.append({
            "rank": rank + 1,
            "page_number": idx + 1,
            "score": float(scores_array[idx]),
            "page_image": sample_pages[idx]
        })
    
    return results


# Test queries on our sample document
test_queries = [
    "What was the Q3 revenue?",
    "What is the revenue breakdown by region?",
    "What are the company's strategic investments?"
]

for query in test_queries:
    print(f"\nQUERY: '{query}'")
    print("-" * 60)
    results = query_colpali(query, page_embeddings, model, processor, top_k=3)
    for r in results:
        print(f"  Rank {r['rank']}: Page {r['page_number']} (MaxSim score: {r['score']:.4f})")
```

```python
# Visualize retrieval results
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

query = "What was the quarterly revenue performance?"
results = query_colpali(query, page_embeddings, model, processor, top_k=3)

fig, axes = plt.subplots(1, 3, figsize=(18, 10))
fig.suptitle(f'ColPali Retrieval Results\nQuery: "{query}"', fontsize=14, fontweight='bold')

for ax, result in zip(axes, results):
    ax.imshow(result['page_image'])
    ax.set_title(
        f"Rank {result['rank']}: Page {result['page_number']}\nMaxSim Score: {result['score']:.4f}",
        fontsize=12
    )
    ax.axis('off')
    # Highlight the top result
    if result['rank'] == 1:
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_edgecolor('green')
            spine.set_linewidth(4)

plt.tight_layout()
plt.savefig("/tmp/colpali_retrieval_results.png", dpi=100, bbox_inches='tight')
plt.show()
print("Results saved to /tmp/colpali_retrieval_results.png")
```

## B.6 End-to-End Visual RAG Pipeline: PDF to Answer

The complete Visual RAG pipeline chains four steps: **(1)** convert each PDF page to an image using PyMuPDF (`fitz`), **(2)** encode every page image with ColQwen2.5 to produce patch embeddings, **(3)** at query time, compute MaxSim scores between the query embedding and all page embeddings to find the most relevant pages, and **(4)** pass the top-scoring page images alongside the query to a vision-language model (e.g., Qwen2-VL or GPT-4V) for answer generation. This end-to-end approach works on any PDF, including those with complex layouts, scanned images, and mixed text-and-graphic content.

```python
# Function to load a real PDF and convert to page images
# Uses PyMuPDF (fitz) for high-quality rendering

def pdf_to_images(pdf_path: str, dpi: int = 150) -> list:
    """
    Convert each page of a PDF to a PIL Image.
    
    Args:
        pdf_path: Path to PDF file
        dpi: Rendering DPI (150 is good for retrieval, 200+ for OCR)
    
    Returns:
        List of PIL Images, one per page
    """
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(pdf_path)
        images = []
        zoom = dpi / 72  # PyMuPDF default is 72 DPI
        matrix = fitz.Matrix(zoom, zoom)
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            pixmap = page.get_pixmap(matrix=matrix)
            img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
            images.append(img)
        
        doc.close()
        print(f"Loaded {len(images)} pages from {pdf_path}")
        return images
    except ImportError:
        print("PyMuPDF not installed. Install with: pip install pymupdf")
        return []
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return []


# Full Visual RAG Pipeline
class VisualRAGPipeline:
    """
    End-to-end Visual RAG pipeline:
    PDF → Page Images → ColPali Embeddings → Retrieve Pages → VLM Answer
    """
    
    def __init__(self, colpali_model, colpali_processor, openai_api_key: str):
        self.model = colpali_model
        self.processor = colpali_processor
        self.openai_api_key = openai_api_key
        self.pages: list = []
        self.page_embeddings: list = []
    
    def ingest_pdf(self, pdf_path: str, dpi: int = 150):
        """Load a PDF and index all pages."""
        print(f"[1/2] Loading PDF: {pdf_path}")
        self.pages = pdf_to_images(pdf_path, dpi=dpi)
        
        if not self.pages:
            raise ValueError("Failed to load PDF pages")
        
        print(f"[2/2] Indexing {len(self.pages)} pages with ColPali...")
        self.page_embeddings = index_pages_with_colpali(
            self.pages, self.model, self.processor
        )
        print("Ingestion complete.")
        return self
    
    def ingest_images(self, images: list):
        """Index pre-loaded page images (for demo without real PDF)."""
        self.pages = images
        print(f"Indexing {len(images)} pages with ColPali...")
        self.page_embeddings = index_pages_with_colpali(
            images, self.model, self.processor
        )
        print("Indexing complete.")
        return self
    
    def retrieve_pages(self, query: str, top_k: int = 3) -> list:
        """Retrieve most relevant pages using ColPali MaxSim."""
        return query_colpali(query, self.page_embeddings, self.model, self.processor, top_k=top_k)
    
    def answer_with_gpt4o(self, query: str, top_k: int = 3) -> dict:
        """
        Full pipeline: retrieve relevant pages, then use GPT-4o Vision to answer.
        """
        import base64
        import openai
        
        # Step 1: Retrieve relevant pages
        print(f"[1/2] Retrieving top-{top_k} pages for: '{query}'")
        retrieved = self.retrieve_pages(query, top_k=top_k)
        
        # Step 2: Encode retrieved pages as base64 for GPT-4o
        print(f"[2/2] Generating answer with GPT-4o Vision...")
        
        messages = [
            {
                "role": "system",
                "content": "You are a document analysis assistant. Answer questions based ONLY on the provided document pages. Be precise and cite specific data points."
            }
        ]
        
        # Build user message with images
        user_content = []
        user_content.append({
            "type": "text",
            "text": f"Please answer the following question based on these {len(retrieved)} document pages:\n\nQuestion: {query}"
        })
        
        for result in retrieved:
            # Convert PIL image to base64
            buffer = io.BytesIO()
            result['page_image'].save(buffer, format='PNG')
            img_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            user_content.append({
                "type": "text",
                "text": f"Page {result['page_number']} (relevance score: {result['score']:.3f}):"
            })
            user_content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{img_b64}", "detail": "high"}
            })
        
        messages.append({"role": "user", "content": user_content})
        
        # Call GPT-4o Vision
        client = openai.OpenAI(api_key=self.openai_api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=1000
        )
        
        return {
            "query": query,
            "answer": response.content if hasattr(response, 'content') else response.choices[0].message.content,
            "retrieved_pages": [r['page_number'] for r in retrieved],
            "retrieval_scores": [r['score'] for r in retrieved]
        }

print("VisualRAGPipeline class defined")
```

```python
# Build and test the Visual RAG pipeline
visual_pipeline = VisualRAGPipeline(
    colpali_model=model,
    colpali_processor=processor,
    openai_api_key=OPENAI_API_KEY
)

# Ingest our sample pages (in real usage, call .ingest_pdf(path))
visual_pipeline.ingest_images(sample_pages)
```

```python
# Test visual queries
test_visual_queries = [
    "What was the total revenue in Q3 2024?",
    "Which region contributed the most revenue and what percentage?",
    "What infrastructure investments did the company make?"
]

for query in test_visual_queries:
    print(f"\nQUERY: {query}")
    print("=" * 60)
    
    # Retrieval only (no VLM call)
    results = visual_pipeline.retrieve_pages(query, top_k=2)
    print(f"Retrieved pages: {[(r['page_number'], f'{r[\"score\"]:.3f}') for r in results]}")
    
    # Full pipeline with GPT-4o Vision
    result = visual_pipeline.answer_with_gpt4o(query, top_k=2)
    print(f"\nAnswer: {result['answer']}")
```

## B.7 Loading ColPali with Real PDFs

Moving from synthetic examples to real documents is straightforward. The `pdf_to_images` utility renders each page at a configurable DPI using PyMuPDF, producing PIL Image objects that are fed directly into the ColPali processor. For large document corpora, you would batch the encoding step and store the resulting embeddings in a vector database (e.g., Qdrant or Milvus) with the page number and PDF path as metadata. The code below provides a production-ready recipe for ingesting, indexing, and querying your own PDF collections with Visual RAG.

```python
# Production recipe: real PDF ingestion

REAL_PDF_EXAMPLE = """
# How to use ColPali with your own PDFs

import fitz  # pip install pymupdf
from PIL import Image
from colpali_engine.models import ColQwen2_5, ColQwen2_5_Processor
import torch

# 1. Convert PDF to page images
def pdf_to_images(pdf_path, dpi=150):
    doc = fitz.open(pdf_path)
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    images = []
    for page in doc:
        pixmap = page.get_pixmap(matrix=matrix)
        img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        images.append(img)
    return images

# 2. Load ColQwen2.5
model = ColQwen2_5.from_pretrained(
    "vidore/colqwen2.5-v0.2",
    torch_dtype=torch.bfloat16,
    device_map="cuda"  # or "mps" for Apple Silicon
).eval()
processor = ColQwen2_5_Processor.from_pretrained("vidore/colqwen2.5-v0.2")

# 3. Index pages
pages = pdf_to_images("my_document.pdf")
page_inputs = processor.process_images(pages)
with torch.no_grad():
    page_embeddings = model(**{k: v.to(model.device) for k, v in page_inputs.items()})

# 4. Query
query = "What does the revenue chart show for Q3?"
query_inputs = processor.process_queries([query])
with torch.no_grad():
    query_embeddings = model(**{k: v.to(model.device) for k, v in query_inputs.items()})

# 5. Score and retrieve
scores = model.score_multi_vector(query_embeddings, page_embeddings)  # (1, n_pages)
best_page_idx = scores[0].argmax().item()
best_page = pages[best_page_idx]

# 6. Answer with GPT-4o or LLaVA
# Pass best_page as image to your VLM of choice
"""

print(REAL_PDF_EXAMPLE)
```

## B.8 ViDoRe Benchmark and Model Variants

**ViDoRe** (Visual Document Retrieval Benchmark) is the standard evaluation for visual document retrieval. It tests models on 10 diverse datasets including financial reports, medical records, and academic papers.

### 2025 ViDoRe Leaderboard (approximate)

| Model | ViDoRe NDCG@5 | Size | Speed |
|-------|--------------|------|-------|
| **ColQwen2.5-v0.2** | 88.4 | 3B | Fast on H100 |
| ColQwen2-v1.0 | 86.9 | 2B | Faster |
| ColPali-v1.3 | 81.3 | 3B (PaliGemma) | Baseline |
| BM25 (text only) | 36.2 | — | Very fast |
| GPT-4o w/ OCR | 71.1 | — | Slow + expensive |

ColQwen2.5 achieves **88.4 NDCG@5** vs **36.2 for BM25** — a massive gap driven by its ability to understand visual structure that text-based methods miss entirely.

```python
# Available ColPali model variants

colpali_variants = [
    {
        "model_id": "vidore/colqwen2.5-v0.2",
        "class": "ColQwen2_5",
        "processor": "ColQwen2_5_Processor",
        "base_model": "Qwen2.5-VL-3B",
        "vidor_score": 88.4,
        "released": "2025",
        "notes": "State-of-the-art, recommended"
    },
    {
        "model_id": "vidore/colqwen2-v1.0",
        "class": "ColQwen2",
        "processor": "ColQwen2Processor",
        "base_model": "Qwen2-VL-2B",
        "vidor_score": 86.9,
        "released": "2024",
        "notes": "Smaller, faster, still excellent"
    },
    {
        "model_id": "vidore/colpali-v1.3",
        "class": "ColPali",
        "processor": "ColPaliProcessor",
        "base_model": "PaliGemma-3B",
        "vidor_score": 81.3,
        "released": "2024",
        "notes": "Original ColPali, well-tested"
    },
]

import pandas as pd
df = pd.DataFrame(colpali_variants)
print("ColPali Model Variants:")
print(df[['model_id', 'base_model', 'vidor_score', 'released', 'notes']].to_string(index=False))

print("\nUsage example:")
print("""
from colpali_engine.models import ColQwen2_5, ColQwen2_5_Processor  # v0.2 (best)
from colpali_engine.models import ColQwen2, ColQwen2Processor       # v1.0 (faster)
from colpali_engine.models import ColPali, ColPaliProcessor         # v1.3 (original)
""")
```

## B.9 When to Use ColPali vs Text-Based RAG

| Scenario | Recommended | Reason |
|----------|-------------|--------|
| PDFs with tables and charts | **ColPali** | OCR destroys table/chart structure |
| Scanned documents | **ColPali** | Poor OCR accuracy on scans |
| Mixed text + infographics | **ColPali** | Can't extract visual context |
| Financial/scientific PDFs | **ColPali** | Equations, figures, formatted data |
| Plain text documents | Text RAG | Faster, cheaper, equally accurate |
| Code repositories | Text RAG | No visual content to preserve |
| Email archives | Text RAG | Text-only, ColPali overhead unnecessary |
| High-volume indexing (>10K pages) | Text RAG + selective ColPali | ColPali is GPU-intensive |

### Hybrid Approach (Best Practice)

For maximum coverage:
1. **Attempt text extraction** with PyMuPDF
2. **Check extraction quality** (word count, special character ratio)
3. **If text quality is poor** (scanned, complex layout): route to ColPali
4. **If text quality is good**: use text RAG (faster + cheaper)
5. **For tables/charts**: always use ColPali regardless of text quality

```python
# Hybrid routing: decide text vs visual RAG per page

def assess_page_quality(page_image: Image.Image) -> dict:
    """
    Heuristic: assess whether a page needs visual RAG.
    Checks text-to-image ratio, OCR confidence, etc.
    
    Returns a routing decision: 'text' or 'visual'
    """
    try:
        import fitz
        # PyMuPDF approach: render page then count text blocks
        # This is a simplified version; real impl would use fitz.Page.get_text()
    except ImportError:
        pass
    
    # Simple heuristic based on image characteristics
    img_array = np.array(page_image.convert('L'))  # grayscale
    
    # Images with lots of color variation → likely have charts/infographics
    color_img = np.array(page_image)
    color_std = color_img.std()
    
    # Very uniform pages are likely text-only
    # High color std suggests charts/images
    
    if color_std > 60:
        routing = 'visual'
        reason = 'High color variation suggests charts/images'
    else:
        routing = 'text'
        reason = 'Low color variation suggests mostly text'
    
    return {
        'routing': routing,
        'reason': reason,
        'color_std': float(color_std)
    }

print("Page routing assessment:")
for i, page in enumerate(sample_pages):
    assessment = assess_page_quality(page)
    print(f"  Page {i+1}: Route to {assessment['routing']:6s} | {assessment['reason']}")
```

---

## Summary: GraphRAG vs ColPali vs Vector RAG

```
┌─────────────────────────────────────────────────────────────────────┐
│                    RAG DECISION TREE                                 │
│                                                                       │
│  Q: What type of documents?                                          │
│  ├── PDFs with visual elements (charts, tables, scans)?              │
│  │   └── ✅ Use ColPali + VLM                                        │
│  └── Text-based documents?                                           │
│      │                                                               │
│      Q: What type of questions?                                      │
│      ├── Thematic / "main themes" / aggregate?                       │
│      │   └── ✅ Use GraphRAG (Global Search)                        │
│      ├── Entity-specific / "what does doc say about X"?              │
│      │   └── ✅ Use GraphRAG (Local Search) or Vector RAG           │
│      ├── Abstract / requires global understanding?                   │
│      │   └── ✅ Use RAPTOR                                          │
│      └── Specific facts / standard Q&A?                              │
│          └── ✅ Use Vector RAG + Semantic Chunking + Reranking      │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Takeaways

**GraphRAG**:
- Microsoft's answer to aggregate and thematic queries
- Expensive to build (many LLM calls), but powerful at query time
- Best for: research corpora, news archives, large document collections
- DRIFT search (2025) adds iterative refinement for complex queries

**ColPali**:
- Treats pages as images — no OCR, no text extraction
- ColQwen2.5-v0.2 achieves 88.4 NDCG@5 on ViDoRe benchmark
- Pairs best with GPT-4o Vision or LLaVA for answer generation
- Essential for financial reports, scientific papers, scanned documents

**The Meta-Lesson**: There is no single RAG architecture that wins on all query types. Production systems need a routing layer that selects the right retrieval strategy based on document type and query nature.
