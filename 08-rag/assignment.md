# Assignment: Build a Production-Ready RAG System

## 🎯 Objective

Build a complete Retrieval-Augmented Generation (RAG) system for a real-world use case. Your system should handle document ingestion, intelligent retrieval, and high-quality answer generation with proper evaluation metrics.

**Estimated Time:** 8-10 hours  
**Difficulty:** ⭐⭐⭐⭐ Advanced  
**Due Date:** 2 weeks from assignment

---

## 📋 Requirements

### Part 1: Document Processing Pipeline (20 points)

Build a robust document ingestion system:

- [ ] **Multi-format support:** PDF, DOCX, TXT, Markdown, HTML
- [ ] **Intelligent chunking:** 
  - Semantic chunking (keep related content together)
  - Overlapping chunks for context preservation
  - Metadata extraction (title, author, date, section)
- [ ] **Text cleaning:** Remove headers, footers, page numbers
- [ ] **Deduplication:** Detect and remove duplicate chunks

```python
class DocumentProcessor:
    def __init__(self, chunk_size=512, chunk_overlap=50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def process_document(self, file_path):
        """Process document and return structured chunks."""
        # TODO: Implement
        pass
    
    def chunk_text(self, text, metadata=None):
        """Split text into semantic chunks."""
        # TODO: Implement semantic chunking
        pass
    
    def extract_metadata(self, document):
        """Extract document metadata."""
        # TODO: Implement
        pass
```

### Part 2: Vector Database & Retrieval (25 points)

Implement advanced retrieval strategies:

- [ ] **Vector store setup:** Use ChromaDB, Pinecone, or Weaviate
- [ ] **Embedding generation:** Use OpenAI embeddings or open-source alternatives
- [ ] **Hybrid search:** Combine dense (semantic) + sparse (keyword) retrieval
- [ ] **Re-ranking:** Implement cross-encoder re-ranking for top results
- [ ] **Metadata filtering:** Filter by date, author, document type

```python
class RAGRetriever:
    def __init__(self, vector_store, embedding_model):
        self.vector_store = vector_store
        self.embedding_model = embedding_model
        self.reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
    
    def hybrid_search(self, query, top_k=10, alpha=0.5):
        """
        Combine semantic and keyword search.
        
        Args:
            query: User question
            top_k: Number of results
            alpha: Weight for semantic vs keyword (0-1)
        """
        # TODO: Implement hybrid search
        pass
    
    def rerank_results(self, query, candidates):
        """Re-rank retrieved documents using cross-encoder."""
        # TODO: Implement re-ranking
        pass
    
    def filter_by_metadata(self, results, filters):
        """Apply metadata filters to results."""
        # TODO: Implement filtering
        pass
```

### Part 3: Answer Generation (25 points)

Create an intelligent answer generator:

- [ ] **Context assembly:** Select and order most relevant chunks
- [ ] **Prompt engineering:** Design effective RAG prompts
- [ ] **Citation tracking:** Include source references in answers
- [ ] **Confidence scoring:** Estimate answer confidence
- [ ] **Fallback handling:** Graceful handling when no good answer exists

```python
class AnswerGenerator:
    def __init__(self, llm_client, model="gpt-4-turbo"):
        self.client = llm_client
        self.model = model
    
    def generate_answer(self, query, context_chunks, include_citations=True):
        """
        Generate answer from retrieved context.
        
        Returns:
            {
                "answer": str,
                "citations": List[dict],
                "confidence": float,
                "sources_used": List[str]
            }
        """
        # TODO: Implement answer generation
        pass
    
    def build_prompt(self, query, context):
        """Build RAG prompt with query and context."""
        prompt = f"""Answer the question based on the context below. 
        If the answer is not in the context, say "I don't have enough information."
        
        Context:
        {context}
        
        Question: {query}
        
        Answer with citations:"""
        return prompt
    
    def estimate_confidence(self, answer, context):
        """Estimate answer confidence (0-1)."""
        # TODO: Implement confidence scoring
        pass
```

### Part 4: Evaluation & Testing (30 points)

Comprehensively evaluate your RAG system:

- [ ] **Create test dataset:** 50+ questions with ground truth answers
- [ ] **Retrieval metrics:**
  - Precision@K, Recall@K
  - Mean Reciprocal Rank (MRR)
  - Normalized Discounted Cumulative Gain (NDCG)
- [ ] **Generation metrics:**
  - ROUGE scores
  - BERTScore
  - Semantic similarity
  - Faithfulness (no hallucinations)
- [ ] **End-to-end metrics:**
  - Answer accuracy
  - Latency (< 3 seconds)
  - Cost per query

```python
class RAGEvaluator:
    def __init__(self, rag_system):
        self.rag_system = rag_system
    
    def evaluate_retrieval(self, test_set):
        """
        Evaluate retrieval quality.
        
        Returns metrics: precision, recall, MRR, NDCG
        """
        pass
    
    def evaluate_generation(self, test_set):
        """
        Evaluate answer quality.
        
        Returns metrics: ROUGE, BERTScore, faithfulness
        """
        pass
    
    def evaluate_end_to_end(self, test_set):
        """
        Full system evaluation.
        
        Returns: accuracy, latency, cost
        """
        pass
    
    def create_evaluation_report(self):
        """Generate comprehensive evaluation report."""
        pass
```

---

## 📊 Grading Rubric

| Criteria | Exemplary (A: 90-100%) | Proficient (B: 80-89%) | Adequate (C: 70-79%) | Needs Work (D/F: <70%) |
|----------|---------------------|-------------------|-----------------|-------------------|
| **Document Processing** (20pts) | Multi-format, semantic chunking, metadata | Good chunking, basic metadata | Simple chunking only | Broken or incomplete |
| **Retrieval** (25pts) | Hybrid search + reranking, excellent relevance | Good retrieval, some reranking | Basic semantic search | Poor retrieval quality |
| **Generation** (25pts) | Citations, confidence, high quality answers | Good answers, some citations | Basic answers generated | Poor answer quality |
| **Evaluation** (30pts) | Comprehensive metrics, >50 test cases, deep analysis | Good metrics, 30-50 tests | Basic eval, 20-30 tests | Incomplete evaluation |

---

## 🎯 Use Case Options (Choose One)

### Option 1: Technical Documentation Assistant
**Dataset:** Python/React/AWS documentation  
**Challenge:** Handle code examples, API references  
**Special requirement:** Syntax highlighting in answers

### Option 2: Research Paper Q&A
**Dataset:** ArXiv papers in your field of interest  
**Challenge:** Mathematical notation, citations  
**Special requirement:** LaTeX rendering

### Option 3: Company Knowledge Base
**Dataset:** Internal docs, wikis, Slack conversations  
**Challenge:** Privacy, access control  
**Special requirement:** User permissions

### Option 4: Legal Document Analysis
**Dataset:** Court cases, statutes, regulations  
**Challenge:** Precise language, citations critical  
**Special requirement:** Confidence scoring

### Option 5: Medical Literature Search
**Dataset:** PubMed articles, clinical trials  
**Challenge:** Technical terminology, accuracy critical  
**Special requirement:** Source verification

---

## 🌟 Bonus Challenges (+10 points each, max +40)

### Bonus 1: Conversational RAG (+10)
- [ ] Multi-turn conversations with context
- [ ] Follow-up question handling
- [ ] Conversation memory management
- [ ] Context window optimization

### Bonus 2: Advanced Retrieval (+10)
- [ ] Query expansion with LLMs
- [ ] Multi-query retrieval
- [ ] Parent document retrieval
- [ ] Hypothetical Document Embeddings (HyDE)

### Bonus 3: Deployment (+10)
- [ ] FastAPI backend
- [ ] Gradio/Streamlit frontend
- [ ] Docker containerization
- [ ] Deploy to cloud (Hugging Face Spaces/Railway)

### Bonus 4: Monitoring & Analytics (+10)
- [ ] Query analytics dashboard
- [ ] User feedback collection
- [ ] A/B testing framework
- [ ] Cost tracking per user/query

---

## 📦 Submission Requirements

### Repository Structure
```
your-name-rag-system/
├── README.md                          # Setup and usage guide
├── requirements.txt                   # Dependencies
├── .env.example                       # Environment variables template
├── src/
│   ├── document_processor.py          # Part 1
│   ├── retriever.py                   # Part 2
│   ├── generator.py                   # Part 3
│   ├── evaluator.py                   # Part 4
│   └── rag_system.py                  # Main system
├── data/
│   ├── documents/                     # Source documents
│   ├── test_set.json                  # Evaluation questions
│   └── ground_truth.json              # Expected answers
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_retrieval_experiments.ipynb
│   ├── 03_generation_tuning.ipynb
│   └── 04_evaluation_analysis.ipynb
├── tests/
│   ├── test_processor.py
│   ├── test_retriever.py
│   ├── test_generator.py
│   └── test_integration.py
├── results/
│   ├── metrics.json
│   ├── error_analysis.md
│   └── charts/
└── EVALUATION_REPORT.md               # Detailed analysis
```

### Deliverables

1. **Working RAG System:**
   - All 4 parts implemented
   - Passes all tests
   - CLI or API interface
   - Demo notebook

2. **Evaluation Report:**
   - Methodology description
   - Metrics tables and charts
   - Error analysis
   - Optimization attempts
   - Conclusions

3. **Test Dataset:**
   - 50+ diverse questions
   - Ground truth answers
   - Difficulty levels
   - Coverage of edge cases

4. **Demo:**
   - 5-minute video OR
   - Live Gradio/Streamlit app
   - Show: ingestion → retrieval → generation → evaluation

---

## 💡 Advanced Tips

<details>
<summary>Tip 1: Semantic Chunking Strategy</summary>

```python
def semantic_chunking(text, max_chunk_size=512):
    """
    Chunk text at semantic boundaries.
    Priority: paragraphs > sentences > words
    """
    # Try paragraph-level first
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        if len(current_chunk) + len(para) < max_chunk_size:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks
```
</details>

<details>
<summary>Tip 2: Hybrid Search Implementation</summary>

```python
def hybrid_search(self, query, top_k=10, alpha=0.7):
    """
    Combine dense (embeddings) + sparse (BM25) search.
    
    alpha: weight for dense search (1-alpha for sparse)
    """
    # Dense retrieval
    query_embedding = self.embed(query)
    dense_results = self.vector_store.similarity_search(
        query_embedding, k=top_k*2
    )
    
    # Sparse retrieval (BM25)
    sparse_results = self.bm25.get_top_n(query, self.documents, n=top_k*2)
    
    # Combine with weighted scoring
    combined_scores = {}
    for doc, score in dense_results:
        combined_scores[doc.id] = alpha * score
    
    for doc, score in sparse_results:
        combined_scores[doc.id] = (
            combined_scores.get(doc.id, 0) + (1-alpha) * score
        )
    
    # Sort and return top k
    sorted_docs = sorted(
        combined_scores.items(), 
        key=lambda x: x[1], 
        reverse=True
    )[:top_k]
    
    return [self.get_doc(doc_id) for doc_id, _ in sorted_docs]
```
</details>

<details>
<summary>Tip 3: Citation Extraction</summary>

```python
def generate_with_citations(self, query, chunks):
    """Generate answer with inline citations."""
    # Number each chunk
    context = "\n\n".join([
        f"[{i+1}] {chunk.text}"
        for i, chunk in enumerate(chunks)
    ])
    
    prompt = f"""Answer using the numbered sources below. 
    Include citations like [1], [2] in your answer.
    
    {context}
    
    Question: {query}
    Answer:"""
    
    answer = self.llm(prompt)
    
    # Extract citations and map to sources
    import re
    citations = re.findall(r'\[(\d+)\]', answer)
    sources = [chunks[int(c)-1].metadata for c in set(citations)]
    
    return {
        "answer": answer,
        "sources": sources,
        "citation_count": len(set(citations))
    }
```
</details>

---

## 📚 Resources

### Essential Reading
- [RAG Survey Paper](https://arxiv.org/abs/2312.10997)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [LangChain RAG Guide](https://python.langchain.com/docs/use_cases/question_answering/)
- [Advanced RAG Techniques](https://blog.langchain.dev/semi-structured-multi-modal-rag/)

### Tools & Libraries
- **Vector Stores:** ChromaDB, Pinecone, Weaviate, Qdrant
- **Embeddings:** OpenAI, Cohere, Sentence-Transformers
- **Frameworks:** LangChain, LlamaIndex, Haystack
- **Evaluation:** RAGAS, DeepEval

### Papers
- [Dense Passage Retrieval](https://arxiv.org/abs/2004.04906)
- [ColBERT](https://arxiv.org/abs/2004.12832)
- [BEIR Benchmark](https://arxiv.org/abs/2104.08663)

---

## 🎓 Learning Objectives

After completing this assignment, you will:

- ✅ Build end-to-end RAG systems
- ✅ Implement advanced retrieval techniques
- ✅ Optimize for quality, speed, and cost
- ✅ Evaluate RAG systems comprehensively
- ✅ Deploy production-ready AI applications

---

## 💬 Support

- **Office Hours:** Tuesdays/Thursdays 2-5 PM
- **Discussion:** [GitHub Discussions](https://github.com/zero-to-ai/discussions)
- **Email:** instructor@zero-to-ai.com

Good luck building your RAG system! 🚀
