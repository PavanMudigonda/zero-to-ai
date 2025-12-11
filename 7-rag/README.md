# Phase 7: RAG (Retrieval-Augmented Generation)

## 🎯 Overview

Combine your skills from previous phases to build production-grade RAG systems!

**Prerequisites:**
- ✅ Tokenization (Phase 3)
- ✅ Embeddings (Phase 4)
- ✅ Neural Networks (Phase 5)
- ✅ Vector Databases (Phase 6)

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

---

## 🗂️ Module Structure

```
7-rag/
├── 00_START_HERE.ipynb           # RAG overview and quick demo
├── 01_basic_rag.ipynb             # Simple RAG from scratch
├── 02_document_processing.ipynb   # Chunking strategies
├── 03_langchain_rag.ipynb         # Using LangChain framework
├── 04_llamaindex_rag.ipynb        # Using LlamaIndex framework
├── 05_advanced_retrieval.ipynb    # Hybrid search, re-ranking
├── 06_conversation_rag.ipynb      # Chat with memory
├── 07_evaluation.ipynb            # RAG evaluation metrics
├── projects/                      # Hands-on projects
│   ├── personal_docs_qa.py        # Chat with your documents
│   ├── code_search.py             # Semantic code search
│   └── research_assistant.py      # Academic paper Q&A
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
model = SentenceTransformer('all-MiniLM-L6-v2')
docs = ["Your documents here..."]
embeddings = model.encode(docs)
db.add(documents=docs, embeddings=embeddings)

# 2. Retrieve relevant context
query = "What is RAG?"
query_embedding = model.encode(query)
results = db.search(query_embedding, top_k=3)

# 3. Generate answer with LLM
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
- [ ] Deploy as API (preview of Phase 8)
- [ ] **Capstone:** Personal knowledge assistant

---

## 🛠️ Technologies You'll Use

**LLM Frameworks:**
- LangChain - Most popular, extensive ecosystem
- LlamaIndex - Best for document indexing
- Haystack - Production-focused

**LLM Providers:**
- OpenAI (GPT-3.5, GPT-4)
- Anthropic (Claude)
- Local models (Llama, Mistral via Ollama)

**Vector Databases:**
- Use what you learned in Phase 6!
- Chroma, Qdrant, Weaviate, Milvus

**Embeddings:**
- OpenAI embeddings (text-embedding-3-small/large)
- Sentence Transformers (all-MiniLM-L6-v2, all-mpnet-base-v2)
- Cohere embeddings

---

## 📊 Key Concepts Explained

### 1. RAG Pipeline

```
Documents → Split → Embed → Store in Vector DB
                                    ↓
User Query → Embed → Search → Retrieve Top-K
                                    ↓
Retrieved Docs + Query → LLM Prompt → Answer
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

---

## 🔗 Resources

### Documentation
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [LlamaIndex Docs](https://docs.llamaindex.ai/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)

### Papers
- [RAG: Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)
- [Improving RAG with Hybrid Search](https://arxiv.org/abs/2210.11416)

### Courses
- [DeepLearning.AI - Building RAG Applications](https://www.deeplearning.ai/short-courses/)
- [LangChain Academy](https://academy.langchain.com/)

### Tools
- [Ollama](https://ollama.ai/) - Run local LLMs
- [Chroma](https://www.trychroma.com/) - Vector database
- [LangSmith](https://www.langchain.com/langsmith) - RAG evaluation

---

## ✅ Completion Checklist

Before moving to Phase 8 (MLOps), you should be able to:

- [ ] Explain RAG architecture and benefits
- [ ] Process and chunk documents effectively
- [ ] Build basic RAG pipeline from scratch
- [ ] Use LangChain or LlamaIndex
- [ ] Implement hybrid search (dense + sparse)
- [ ] Add conversation memory to chatbots
- [ ] Evaluate RAG system quality
- [ ] Deploy a working RAG application
- [ ] Understand cost/latency tradeoffs
- [ ] Handle edge cases and errors

---

## 🎓 What's Next?

**Phase 8: MLOps & Production** →
- Deploy RAG as scalable API
- Monitor performance and costs
- CI/CD for ML systems
- Cloud deployment (AWS, Azure, GCP)

**Phase 9: Specializations** →
- Multimodal RAG (images + text)
- Agent systems with RAG
- Advanced prompt engineering

---

**Ready to build your first RAG system?** → Start with `00_START_HERE.ipynb`

**Questions?** → Check the projects/ folder for working examples

**🚀 Let's build intelligent systems that can learn from your data!**
