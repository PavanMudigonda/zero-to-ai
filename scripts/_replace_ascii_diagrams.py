#!/usr/bin/env python3
"""Replace all remaining ASCII arrow diagrams with Mermaid diagrams."""
import json, re

def load(path):
    with open(path) as f:
        return json.load(f)

def save(path, nb):
    with open(path, 'w') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

def set_src(cell, text):
    cell['source'] = text.splitlines(keepends=True)

def code_to_md(cell, text):
    """Convert a code cell to markdown and set its source."""
    cell['cell_type'] = 'markdown'
    cell.pop('outputs', None)
    cell.pop('execution_count', None)
    set_src(cell, text)

def swap_block(src, old_block, new_block):
    if old_block in src:
        return src.replace(old_block, new_block), True
    return src, False

# ─── 1. 10-specializations/10-specializations.ipynb cells 3, 5, 7 ────────────
path = "jupyter-notebooks/10-specializations/10-specializations.ipynb"
nb = load(path)

paths_data = [
    (3,
     "1. Advanced NLP (2-3 months)\n   ↓\n2. AI Agents (2 months) - Leverage NLP skills\n   ↓\n3. Computer Vision (2-3 months) - Multimodal agents",
     "```mermaid\nflowchart TD\n    A[\"1. Advanced NLP\\n(2–3 months)\"] --> B[\"2. AI Agents\\n(2 months)\\nLeverage NLP skills\"]\n    B --> C[\"3. Computer Vision\\n(2–3 months)\\nMultimodal agents\"]\n```"),
    (5,
     "1. Computer Vision (2-3 months)\n   ↓\n2. Advanced NLP (2 months) - Multimodal understanding\n   ↓\n3. AI Agents (2-3 months) - Multimodal agents",
     "```mermaid\nflowchart TD\n    A[\"1. Computer Vision\\n(2–3 months)\"] --> B[\"2. Advanced NLP\\n(2 months)\\nMultimodal understanding\"]\n    B --> C[\"3. AI Agents\\n(2–3 months)\\nMultimodal agents\"]\n```"),
    (7,
     "1. AI Agents (2-3 months)\n   ↓\n2. Advanced NLP (2 months) - Better language agents\n   ↓\n3. Computer Vision (2-3 months) - Visual agents",
     "```mermaid\nflowchart TD\n    A[\"1. AI Agents\\n(2–3 months)\"] --> B[\"2. Advanced NLP\\n(2 months)\\nBetter language agents\"]\n    B --> C[\"3. Computer Vision\\n(2–3 months)\\nVisual agents\"]\n```"),
]
for ci, old_text, new_text in paths_data:
    cell = nb['cells'][ci]
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    if old_text in src:
        code_to_md(cell, src.replace(old_text, new_text))
        print(f"UPDATED 10-specializations.ipynb cell {ci}")
save(path, nb)

# ─── 2. 10-specializations/ai-agents/ai-agents.ipynb cells 7, 11 ─────────────
path = "jupyter-notebooks/10-specializations/ai-agents/ai-agents.ipynb"
nb = load(path)

OLD7 = "Chatbot:\nUser → LLM → Response\n\nAgent:\nUser → Agent\n       ↓\n    Reasoning (What do I need?)\n       ↓\n    Action (Use tools)\n       ↓\n    Observation (Results)\n       ↓\n    Repeat until done\n       ↓\n    Final Answer"
NEW7 = "**Chatbot:** `User → LLM → Response`\n\n**Agent:**\n\n```mermaid\nflowchart TD\n    U([User]) --> A[Agent]\n    A --> R[Reasoning]\n    R --> T[\"Action / Tool use\"]\n    T --> O[Observation]\n    O -->|repeat| R\n    O --> F([Final Answer])\n```"

OLD11 = "User Request\n    ↓\nSupervisor Agent (coordinates)\n    ↓\n├─ Researcher (gathers info)\n├─ Analyst (processes data)\n├─ Writer (creates content)\n└─ Critic (reviews)\n    ↓\nFinal Output"
NEW11 = "```mermaid\nflowchart TD\n    U([User Request]) --> S[Supervisor Agent]\n    S --> R[Researcher]\n    S --> A[Analyst]\n    S --> W[Writer]\n    S --> C[Critic]\n    R & A & W & C --> O([Final Output])\n```"

for ci, old_t, new_t in [(7, OLD7, NEW7), (11, OLD11, NEW11)]:
    cell = nb['cells'][ci]
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    if old_t in src:
        code_to_md(cell, src.replace(old_t, new_t))
        print(f"UPDATED ai-agents.ipynb cell {ci}")
save(path, nb)

# ─── 3. 10-specializations/ai-agents/00_START_HERE ───────────────────────────
path = "jupyter-notebooks/10-specializations/ai-agents/00_START_HERE/00_START_HERE.ipynb"
nb = load(path)
cell = nb['cells'][1]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']

# Extract the fenced block containing the box-drawing
old_block = re.search(r'```\n┌─+┐.*?└─+┘\n```', src, re.DOTALL)
if old_block:
    OLD = old_block.group()
    NEW = """```mermaid
flowchart TD
    A([User Input]) --> B["LLM Brain\\nPlanning & Reasoning"]
    B --> C[Tool Selection]
    C --> D["Tool Execution\\nWeb Search / DB / Code / API"]
    D --> E["Memory\\nShort & Long-term"]
    E --> F([Final Response])
```"""
    src2, changed = swap_block(src, OLD, NEW)
    if changed:
        set_src(cell, src2)
        print("UPDATED ai-agents/00_START_HERE cell 1")
save(path, nb)

# ─── 4. 10-specializations/computer-vision/00_START_HERE ─────────────────────
path = "jupyter-notebooks/10-specializations/computer-vision/00_START_HERE/00_START_HERE.ipynb"
nb = load(path)
cell = nb['cells'][8]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']

old_block = re.search(r'```\n┌─+┐[\s\S]*?└─+┘\n```', src, re.DOTALL)
if old_block:
    OLD = old_block.group()
    NEW = """```mermaid
flowchart TD
    A([Input Image]) --> B["Preprocessing\\nResize, normalize, augment"]
    B --> C["Feature Extraction\\nCNN or ViT backbone"]
    C --> D["Task-Specific Head\\nClassification / Detection / etc."]
    D --> E["Post-processing\\nNMS, thresholding"]
    E --> F(["Output\\nLabels, boxes, masks"])
```"""
    src2, changed = swap_block(src, OLD, NEW)
    if changed:
        set_src(cell, src2)
        print("UPDATED computer-vision/00_START_HERE cell 8")
save(path, nb)

# ─── 5. 15-ai-agents/02_intro_to_agents cell 1 ───────────────────────────────
path = "jupyter-notebooks/15-ai-agents/02_intro_to_agents/02_intro_to_agents.ipynb"
nb = load(path)
cell = nb['cells'][1]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']

OLD = "```\n┌─────────────────────────────────────────┐\n│           AI Agent                      │\n│                                         │\n│  ┌──────────┐  ┌──────────┐  ┌───────┐│\n│  │ Perceive │→ │ Reason   │→ │  Act  ││\n│  │(Inputs)  │  │(Planning)│  │(Tools)││\n│  └──────────┘  └──────────┘  └───────┘│\n│        ↑             ↓           │     │\n│        └──────[Memory]───────────┘     │\n└─────────────────────────────────────────┘\n```"
NEW = """```mermaid
flowchart LR
    P["Perceive\\n(Inputs)"] --> R["Reason\\n(Planning)"]
    R --> A["Act\\n(Tools)"]
    A -->|memory feedback| P
```"""
src2, changed = swap_block(src, OLD, NEW)
if changed:
    set_src(cell, src2)
    print("UPDATED 02_intro_to_agents cell 1")
save(path, nb)

# ─── 6. 15-ai-agents/13_agentic_coding_ides cell 1 ──────────────────────────
path = "jupyter-notebooks/15-ai-agents/13_agentic_coding_ides/13_agentic_coding_ides.ipynb"
nb = load(path)
cell = nb['cells'][1]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']

OLD = "```\nUser Prompt → [Plan] → [Tool Call] → [Observe Result] → [Decide Next Step] → ...\n → [Complete]\n                ↑                                              |\n                └──────────── Self-Correction Loop ────────────┘\n```"
NEW = """```mermaid
flowchart LR
    A([User Prompt]) --> B[Plan]
    B --> C[Tool Call]
    C --> D[Observe Result]
    D --> E[Decide Next Step]
    E --> F([Complete])
    E -->|self-correction| B
```"""
src2, changed = swap_block(src, OLD, NEW)
if changed:
    set_src(cell, src2)
    print("UPDATED 13_agentic_coding_ides cell 1")
save(path, nb)

# ─── 7. 08-rag/12_advanced_retrieval cells 19, 27, 31 ────────────────────────
path = "jupyter-notebooks/08-rag/12_advanced_retrieval/12_advanced_retrieval.ipynb"
nb = load(path)

# cell 19 — RAPTOR
cell = nb['cells'][19]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
OLD19 = "```\nLevel 0 (leaves): Original text chunks\n    ↓ embed + cluster (GMM)\nLevel 1: LLM summaries of each cluster\n    ↓ embed + cluster again\nLevel 2: Summaries of summaries\n    ↓ ... repeat ...\nLevel N (root): One global summary\n```"
NEW19 = """```mermaid
flowchart TD
    L0["Level 0: Original text chunks"] -->|"embed + cluster (GMM)"| L1
    L1["Level 1: LLM summaries of each cluster"] -->|embed + cluster again| L2
    L2["Level 2: Summaries of summaries"] -->|repeat| LN
    LN["Level N: One global summary"]
    Q([Query]) -->|search all levels| L0 & L1 & L2 & LN
```"""
src2, changed = swap_block(src, OLD19, NEW19)
if changed:
    set_src(cell, src2)
    print("UPDATED 12_advanced_retrieval cell 19")

# cell 27 — HyDE
cell = nb['cells'][27]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
OLD27 = '```\nQuery: "What year was NexCloud founded?"\n    ↓ LLM generates hypothetical answer\nHyDE doc: "NexCloud was founded in [year]. The company was established by..."\n    ↓ embed this hypothetical document\nSearch with hypothetical embedding → much better recall\n```'
NEW27 = """```mermaid
flowchart TD
    A([\"Query: 'What year was NexCloud founded?'\"]) --> B[LLM generates hypothetical answer]
    B --> C[\"HyDE doc: 'NexCloud was founded in...'\\n(plausible but may be hallucinated)\"]
    C --> D[Embed hypothetical document]
    D --> E([Search vector store → better recall])
```"""
src2, changed = swap_block(src, OLD27, NEW27)
if changed:
    set_src(cell, src2)
    print("UPDATED 12_advanced_retrieval cell 27")

# cell 31 — Complete pipeline
cell = nb['cells'][31]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
OLD31 = "```\nDocument\n    ↓ Semantic Chunking (LangChain SemanticChunker)\nSemantic Chunks\n    ↓ HyDE query expansion\nVector Store (ChromaDB)\n    ↓ Top-50 candidate retrieval\n    ↓ ColBERT re-retrieval (RAGatouille)\n    ↓ Cohere Rerank (top-5)\nFinal Context\n    ↓ LLM generation (GPT-4o-mini)\nAnswer\n```"
NEW31 = """```mermaid
flowchart TD
    D([Document]) --> SC["Semantic Chunking\\n(LangChain SemanticChunker)"]
    SC --> C[Semantic Chunks]
    C --> VS["Vector Store\\n(ChromaDB)"]
    Q([Query]) --> H[HyDE query expansion]
    H --> VS
    VS --> R50[Top-50 candidate retrieval]
    R50 --> CB["ColBERT re-retrieval\\n(RAGatouille)"]
    CB --> RE["Cohere Rerank\\n(top-5)"]
    RE --> FC[Final Context]
    FC --> G["LLM generation\\n(GPT-4o-mini)"]
    G --> A([Answer])
```"""
src2, changed = swap_block(src, OLD31, NEW31)
if changed:
    set_src(cell, src2)
    print("UPDATED 12_advanced_retrieval cell 31")

save(path, nb)

# ─── 8. 28-practical-data-science transformers_from_scratch cell 5 ────────────
path = "jupyter-notebooks/28-practical-data-science/deep-learning-nlp/01_transformers_from_scratch/01_transformers_from_scratch.ipynb"
nb = load(path)
cell = nb['cells'][5]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
OLD = "```\nInput (batch, seq, d_model)\n    ↓ split into h heads\nHead 1: Q1, K1, V1 → Attention1 → output1\nHead 2: Q2, K2, V2 → Attention2 → output2   (in parallel!)\n...\nHead h: Qh, Kh, Vh → Attentionh → outputh\n    ↓ concatenate\nConcat → Linear → final output (batch, seq, d_model)\n```"
NEW = """```mermaid
flowchart TD
    I["Input\\n(batch, seq, d_model)"] -->|split into h heads| H
    subgraph H["Parallel Heads"]
        H1["Head 1: Q1,K1,V1 → Attn1"]
        H2["Head 2: Q2,K2,V2 → Attn2"]
        Hh["Head h: Qh,Kh,Vh → Attnh"]
    end
    H -->|concatenate| O["Concat → Linear → Output\\n(batch, seq, d_model)"]
```"""
src2, changed = swap_block(src, OLD, NEW)
if changed:
    set_src(cell, src2)
    print("UPDATED transformers_from_scratch cell 5")
save(path, nb)

# ─── 9. 30-inference-optimization prefix_caching cell 0 ──────────────────────
path = "jupyter-notebooks/30-inference-optimization/07_prefix_caching_chunked_prefill/07_prefix_caching_chunked_prefill.ipynb"
nb = load(path)
cell = nb['cells'][0]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
OLD = '```\nRequest 1: [SYSTEM PROMPT (2048 tokens)] [User: "What is X?"]\n                ↓\n           KV blocks for system prompt cached with hash key\n\nRequest 2: [SYSTEM PROMPT (2048 tokens)] [User: "What is Y?"]\n                ↓\n           System prompt KV blocks reused → TTFT drops from ~500ms to ~50ms\n```'
NEW = """```mermaid
flowchart TD
    R1["Request 1:\\n[SYSTEM PROMPT 2048 tokens]\\n[User: 'What is X?']"] --> C[KV blocks for system prompt\\ncached with hash key]
    R2["Request 2:\\n[SYSTEM PROMPT 2048 tokens]\\n[User: 'What is Y?']"] --> HIT[System prompt KV blocks reused\\nTTFT drops ~500ms → ~50ms]
    C -.->|reuse| HIT
```"""
src2, changed = swap_block(src, OLD, NEW)
if changed:
    set_src(cell, src2)
    print("UPDATED prefix_caching cell 0")
save(path, nb)

# ─── 10. 12-llm-finetuning/05_qlora_efficient cell 0 ─────────────────────────
path = "jupyter-notebooks/12-llm-finetuning/05_qlora_efficient/05_qlora_efficient.ipynb"
nb = load(path)
cell = nb['cells'][0]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
old_block = re.search(r'```\nQLoRA[\s\S]*?└─+┘\n```', src, re.DOTALL)
if old_block:
    OLD = old_block.group()
    NEW = """```mermaid
flowchart LR
    I([Input]) --> W["W_frozen\\n(NF4 4-bit, frozen)"]
    I --> BA["B · A\\n(BF16 LoRA)\\n← only trained weights"]
    W -->|"BF16 output"| S((+))
    BA -->|"BF16 delta"| S
    S --> O([Output])
```"""
    src2, changed = swap_block(src, OLD, NEW)
    if changed:
        set_src(cell, src2)
        print("UPDATED qlora_efficient cell 0")
save(path, nb)

# ─── 11. 05-embeddings/08_QUICKSTART cells 17, 19 ────────────────────────────
path = "jupyter-notebooks/05-embeddings/08_QUICKSTART/08_QUICKSTART.ipynb"
nb = load(path)

OLD17 = "Phase 4: Learn BERT tokenizer\n   ↓\n   ❓ How do I get embeddings from BERT?\n   ↓\nPhase 5: Only showed Sentence Transformers (different models)"
NEW17 = "```mermaid\nflowchart TD\n    A[\"Phase 4: BERT tokenizer\"] --> Q[\"❓ How do I get embeddings from BERT?\"]\n    Q --> B[\"Phase 5: Sentence Transformers\\n(different model family)\"]\n```"

OLD19 = "Phase 4: Learn BERT tokenizer\n   ↓\n   ✅ huggingface_embeddings.py\n   ↓\nPhase 5: Extract BERT embeddings + compare approaches"
NEW19 = "```mermaid\nflowchart TD\n    A[\"Phase 4: BERT tokenizer\"] --> B[\"✅ huggingface_embeddings.py\"]\n    B --> C[\"Phase 5: Extract BERT embeddings\\n+ compare approaches\"]\n```"

for ci, old_t, new_t in [(17, OLD17, NEW17), (19, OLD19, NEW19)]:
    cell = nb['cells'][ci]
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    if old_t in src:
        code_to_md(cell, src.replace(old_t, new_t))
        print(f"UPDATED 08_QUICKSTART cell {ci}")
save(path, nb)

print("\nAll done.")
