# RAG

## 🎯 Overview

Combine your skills from previous phases to build production-grade RAG systems!

**Prerequisites:**
- ✅ Tokenization (Phase 4)
- ✅ Embeddings (Phase 5)
- ✅ Neural Networks (Phase 6)
- ✅ Vector Databases (Phase 7)

**Time:** 3-4 weeks | 60-80 hours  
**Outcome:** Build AI applications that can query your knowledge base

---

## 📚 What You'll Learn

### Core RAG Concepts
- [ ] RAG architecture and pipeline
- [ ] Document processing and chunking strategies
- [ ] Retrieval methods (dense, sparse, hybrid)
- [ ] Context management and prompt construction
- [ ] Re-ranking and result filtering
- [ ] LLM integration (OpenAI, Anthropic, local models)

### Advanced RAG Techniques
- [ ] Hybrid search (vector + keyword)
- [ ] Query transformation and expansion
- [ ] Multi-query retrieval
- [ ] Parent-document retrieval
- [ ] Self-query and metadata filtering
- [ ] Conversation memory and context
- [ ] HyDE and hypothetical-answer retrieval
- [ ] Contextual compression and segment extraction
- [ ] Cross-encoder reranking
- [ ] Hierarchical retrieval, RAPTOR, and parent-child indexing
- [ ] Corrective RAG (CRAG) and self-reflective retrieval loops
- [ ] GraphRAG, multimodal RAG, and agentic retrieval

---

## 🗂️ Module Structure

```
08-rag/
├── 00_START_HERE.ipynb           # RAG overview and quick demo
├── 01_basic_rag.ipynb             # Simple RAG from scratch
├── 02_document_processing.ipynb   # Chunking strategies
├── 03_langchain_rag.ipynb         # Using LangChain framework
├── 04_llamaindex_rag.ipynb        # Using LlamaIndex framework
├── 05_advanced_retrieval.ipynb    # Hybrid search, re-ranking
├── 06_conversation_rag.ipynb      # Chat with memory
├── 07_evaluation.ipynb            # RAG evaluation metrics
├── 08_hyde_reranking.ipynb        # HyDE-style query expansion plus reranking
├── 08_rag_evaluation_playbook.md  # How to benchmark RAG improvements
├── 08_rag_technique_selection.md  # How to choose the right RAG upgrade
├── 09_advanced_retrieval.ipynb    # Parent-child retrieval, ensemble
├── 10_graphrag_visual_rag.ipynb   # GraphRAG and multimodal RAG
├── 11_corrective_rag.ipynb        # CRAG-style retrieval grading, retry, abstention
├── 12_parent_child_retrieval.ipynb # Structured retrieval with chunk-to-parent expansion
├── 13_raptor_retrieval.ipynb       # RAPTOR-style hierarchical summary-tree retrieval
├── assignment.md                  # Phase assignment
├── challenges.md                  # Hands-on challenges
└── README.md                      # This file
```

---

## 🚀 Quick Start

### 1. Basic RAG Pipeline

```python
# The fundamental RAG flow:
# 1. Index documents → embeddings → vector DB
# 2. User query → embedding → similarity search
# 3. Retrieved docs + query → LLM → answer

from sentence_transformers import SentenceTransformer
from your_vector_db import VectorDB  # Chroma, Qdrant, etc.
from openai import OpenAI

# 1. Index your documents
# Use any embedding model - see 05-embeddings/embedding_comparison.md for options
# API: Gemini Embedding (cheapest + best), Voyage 3.5, or OpenAI
# Local: Qwen3-Embedding, BGE-M3, or all-MiniLM-L6-v2
model = SentenceTransformer('all-MiniLM-L6-v2')  # local, fast
docs = ["Your documents here..."]
embeddings = model.encode(docs)
db.add(documents=docs, embeddings=embeddings)

# 2. Retrieve relevant context
query = "What is RAG?"
query_embedding = model.encode(query)
results = db.search(query_embedding, top_k=3)

# 3. Generate answer with LLM (Claude, GPT, Gemini, or local)
context = "\n".join(results)
prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
response = llm.generate(prompt)
```

---

## 📋 Learning Path

### Week 1: RAG Fundamentals
- [ ] Complete `00_START_HERE.ipynb`
- [ ] Build basic RAG in `01_basic_rag.ipynb`
- [ ] Learn chunking strategies in `02_document_processing.ipynb`
- [ ] **Project:** Simple Q&A on your documents

### Week 2: RAG Frameworks
- [ ] Learn LangChain in `03_langchain_rag.ipynb`
- [ ] Explore LlamaIndex in `04_llamaindex_rag.ipynb`
- [ ] Compare frameworks and choose your favorite
- [ ] **Project:** Build a research paper assistant

### Week 3: Advanced Techniques
- [ ] Implement hybrid search in `05_advanced_retrieval.ipynb`
- [ ] Add conversation memory in `06_conversation_rag.ipynb`
- [ ] Learn evaluation in `07_evaluation.ipynb`
- [ ] **Project:** Code search system for your repos

### Week 4: Production Project
- [ ] Build end-to-end RAG application
- [ ] Add proper error handling
- [ ] Implement caching and optimization
- [ ] Deploy as API (preview of Phase 9)
- [ ] **Capstone:** Personal knowledge assistant

### Optional Week 5: Modern RAG Deep Dives
- [ ] Explore HyDE / query rewriting / query decomposition patterns
- [ ] Work through `08_hyde_reranking.ipynb` to compare baseline retrieval vs HyDE + reranking
- [ ] Compare reranking, contextual compression, and relevant-segment extraction
- [ ] Work through `11_corrective_rag.ipynb` to add retrieval grading, retry logic, and abstention
- [ ] Work through `12_parent_child_retrieval.ipynb` before moving to RAPTOR or GraphRAG
- [ ] Work through `13_raptor_retrieval.ipynb` to compare flat, parent-child, and tree-based retrieval
- [ ] Study CRAG, Self-RAG, and retrieval-with-feedback loops
- [ ] Review RAPTOR, GraphRAG, and multimodal RAG architectures
- [ ] Build a small benchmark to compare at least 3 advanced techniques

---

## 🧭 Modern RAG Technique Map

The cloned `RAG_Techniques` repository is strong because it does not treat RAG as one pattern. It treats RAG as a family of retrieval control strategies. Use this map to understand which techniques matter and when.

| Problem | Techniques to Study | Why It Helps | When to Use |
|---------|---------------------|--------------|-------------|
| Queries are vague or underspecified | Query rewriting, query decomposition, multi-query retrieval, HyDE | Makes retrieval better aligned with user intent | User asks short, ambiguous, or multi-part questions |
| Chunks lose too much context | Semantic chunking, proposition chunking, contextual headers, window expansion | Preserves meaning while keeping retrieval precise | Long docs, technical manuals, research papers |
| Retriever finds partly-right docs | Hybrid retrieval, reranking, contextual compression, segment extraction | Improves top-k quality before the LLM sees context | Large corpora, noisy search results, enterprise docs |
| Questions require structure beyond flat chunks | Parent-child retrieval, hierarchical indices, RAPTOR, GraphRAG | Retrieves summaries, entities, relationships, and larger context blocks | Multi-hop reasoning, long reports, knowledge graphs |
| System hallucinates or retrieves weak evidence | Reliable RAG, CRAG, Self-RAG, feedback loops | Adds validation and correction before final answer | High-stakes workflows, compliance, research, support |
| Queries span text, tables, and images | Multimodal RAG, caption-based retrieval, visual RAG, ColPali-style retrieval | Brings non-text content into the retrieval loop | PDFs, dashboards, slide decks, diagrams |
| Workflow needs tools and planning | Agentic RAG, retrieval orchestration, tool selection | Lets the system choose retrieval tools dynamically | Complex research agents, enterprise copilots |

### Suggested progression

1. Learn the baseline pipeline first: chunk, embed, retrieve, answer.
2. Improve retrieval quality next: hybrid search, reranking, metadata filters.
3. Improve query understanding after that: rewriting, multi-query, HyDE.
4. Add reliability controls next: compression, validation, CRAG or Self-RAG.
5. Only then move into GraphRAG, agentic RAG, and multimodal retrieval.

This ordering matters. Most weak RAG systems fail because teams jump to advanced architecture before fixing chunking, retrieval quality, and evaluation.

### Companion guide

Use [08_rag_technique_selection.md](08_rag_technique_selection.md) if you want a compact decision guide for choosing between HyDE, reranking, compression, RAPTOR, CRAG, Self-RAG, and GraphRAG.

Use [08_rag_evaluation_playbook.md](08_rag_evaluation_playbook.md) if you want a practical framework for benchmarking retrieval quality, answer quality, latency, and failure behavior.

---

## 🛠️ Technologies You'll Use

**LLM Frameworks:**
- LangChain - Most popular, extensive ecosystem
- LlamaIndex - Best for document indexing
- Haystack - Production-focused

**LLM Providers:**
- OpenAI (GPT-5.4, GPT-4.1, GPT-4.1-mini)
- Anthropic (Claude Sonnet 4.6, Haiku 4.5)
- Google (Gemini 3.1 Pro, Flash)
- Local models (Qwen 3, Llama 4, DeepSeek R1 via Ollama)

**Vector Databases:**
- Use what you learned in Phase 7!
- Chroma, Qdrant, Weaviate, Milvus

**Embeddings:**
- OpenAI embeddings (text-embedding-3-small/large)
- Sentence Transformers (all-MiniLM-L6-v2, all-mpnet-base-v2)
- Cohere embeddings

---

## 📊 Key Concepts Explained

### 1. RAG Pipeline

```{mermaid}
flowchart TD
    A[Documents] --> B[Split into Chunks]
    B --> C[Embed]
    C --> D[Store in Vector DB]
    E[User Query] --> F[Embed Query]
    F --> G[Similarity Search]
    D --> G
    G --> H[Retrieve Top-K]
    H --> I[Retrieved Docs + Query]
    I --> J[LLM Prompt]
    J --> K[Answer]
```

### 2. Chunking Strategies

**Fixed-size chunks:**
```python
chunk_size = 512  # tokens or characters
overlap = 50      # overlap between chunks
```

**Semantic chunks:**
- Split by paragraphs, sentences
- Preserve document structure
- Maintain context boundaries

**Recursive splitting:**
- Try different separators (\n\n, \n, ., space)
- Preserve hierarchy

### 3. Retrieval Methods

**Dense (Vector Search):**
- Semantic similarity
- Works for paraphrased queries
- Requires embeddings

**Sparse (Keyword Search):**
- BM25, TF-IDF
- Exact keyword matching
- Fast and interpretable

**Hybrid:**
- Combine both approaches
- Re-rank with RRF (Reciprocal Rank Fusion)
- Best of both worlds

### 4. What Upgrades a Good RAG System into a Strong One

**Query-side upgrades:**
- Rewrite vague questions into standalone queries
- Generate multiple retrieval queries and merge the results
- Use HyDE when the question is abstract and semantic similarity is weak

**Document-side upgrades:**
- Use semantic or proposition chunking when fixed windows lose meaning
- Add headers, summaries, or parent references to each chunk
- Use hierarchical retrieval for long documents and section-level reasoning

**Ranking-side upgrades:**
- Retrieve broad candidate sets first
- Re-rank with a cross-encoder or reranker model
- Compress context so the generator only sees the best evidence

**Control-loop upgrades:**
- Detect low-confidence retrieval before answering
- Retry with transformed queries when the first pass is weak
- Add answer verification or evidence grading for high-risk use cases

---

## 🎯 Projects

### Project 1: Personal Documentation Q&A
Build a chatbot that answers questions about your personal notes, docs, PDFs.

**Features:**
- Upload PDFs, TXTs, Markdown files
- Chunk and embed documents
- Conversational interface
- Source citation

### Project 2: Code Search Engine
Semantic search across your GitHub repositories.

**Features:**
- Index code files (Python, JavaScript, etc.)
- Search by intent ("how to connect to database?")
- Show relevant code snippets
- Explain code functionality

### Project 3: Research Assistant
Query academic papers and scientific literature.

**Features:**
- Process research papers (PDFs)
- Extract citations and references
- Summarize papers
- Compare multiple papers

### Project 4: Customer Support Bot
RAG-powered FAQ system.

**Features:**
- Index support documentation
- Handle common questions
- Escalate to human when needed
- Track conversation context

### Project 5: Advanced Enterprise Search
Build a RAG system that combines multiple retrieval strategies and exposes evidence quality.

**Features:**
- Query rewriting and multi-query retrieval
- Hybrid retrieval plus reranking
- Metadata-aware filtering
- Confidence scoring and answer verification
- Failure routing: answer, abstain, or ask follow-up

---

## 📈 Evaluation Metrics

### Retrieval Quality
- **Precision@K:** Relevant docs in top K results
- **Recall@K:** % of relevant docs retrieved
- **MRR (Mean Reciprocal Rank):** Position of first relevant result
- **NDCG:** Normalized Discounted Cumulative Gain

### Generation Quality
- **Faithfulness:** Answer grounded in context
- **Relevance:** Answer addresses the question
- **Correctness:** Factually accurate
- **Human evaluation:** User satisfaction

### System Metrics
- **Latency:** Response time
- **Cost:** API costs per query
- **Cache hit rate:** Efficiency

---

## 💡 Best Practices

### Document Processing
✅ Chunk size: 256-1024 tokens (experiment!)  
✅ Overlap: 10-20% of chunk size  
✅ Preserve metadata (source, date, author)  
✅ Clean text (remove headers, footers)

### Retrieval
✅ Retrieve 3-10 documents (balance context vs noise)  
✅ Use hybrid search when possible  
✅ Re-rank results for better quality  
✅ Filter by metadata when relevant

### Prompting
✅ Provide clear instructions  
✅ Include relevant context only  
✅ Ask LLM to cite sources  
✅ Handle "I don't know" cases

### Production
✅ Cache embeddings and results  
✅ Monitor LLM costs  
✅ Implement rate limiting  
✅ Add error handling and retries
✅ Benchmark retrieval variants before adding architectural complexity
✅ Track answer faithfulness separately from answer fluency
✅ Keep a failure set of hard questions and regressions
✅ Prefer simpler retrieval improvements before adding agents or graphs

---

## 🔗 Resources

### Documentation
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [LlamaIndex Docs](https://docs.llamaindex.ai/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [RAG Techniques Repository](https://github.com/NirDiamant/RAG_Techniques)

### Papers
- [RAG: Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)
- [Improving RAG with Hybrid Search](https://arxiv.org/abs/2210.11416)
- [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://arxiv.org/abs/2401.18059)
- [Corrective Retrieval Augmented Generation](https://arxiv.org/abs/2401.15884)
- [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511)

### Courses
- [DeepLearning.AI - Building RAG Applications](https://www.deeplearning.ai/short-courses/)
- [LangChain Academy](https://academy.langchain.com/)

### Tools
- [Ollama](https://ollama.ai/) - Run local LLMs
- [Chroma](https://www.trychroma.com/) - Vector database
- [LangSmith](https://www.langchain.com/langsmith) - RAG evaluation
- [Ragas](https://github.com/explodinggradients/ragas) - Evaluate retrieval and answer quality
- [DeepEval](https://github.com/confident-ai/deepeval) - LLM evaluation for RAG pipelines

---

## ✅ Completion Checklist

Before moving to Phase 9 (MLOps), you should be able to:

- [ ] Explain RAG architecture and benefits
- [ ] Process and chunk documents effectively
- [ ] Build basic RAG pipeline from scratch
- [ ] Use LangChain or LlamaIndex
- [ ] Implement hybrid search (dense + sparse)
- [ ] Add conversation memory to chatbots
- [ ] Evaluate RAG system quality
- [ ] Explain when to use HyDE, reranking, contextual compression, or GraphRAG
- [ ] Diagnose retrieval failures and choose the right fix
- [ ] Deploy a working RAG application
- [ ] Understand cost/latency tradeoffs
- [ ] Handle edge cases and errors

---

## 🎓 What's Next?

**Phase 9: MLOps & Production** →
- Deploy RAG as scalable API
- Monitor performance and costs
- CI/CD for ML systems
- Cloud deployment (AWS, Azure, GCP)

**Phase 10: Specializations** →
- Multimodal RAG (images + text)
- Agent systems with RAG
- Advanced prompt engineering

---

**Ready to build your first RAG system?** → Start with `00_START_HERE.ipynb`

**Questions?** → Check the `assignment.md`, `challenges.md`, `08_rag_technique_selection.md`, and `08_rag_evaluation_playbook.md` for practice, technique selection, and benchmarking

**🚀 Let's build intelligent systems that can learn from your data!**
