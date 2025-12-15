# Phase 7: Retrieval-Augmented Generation (RAG) - Pre-Quiz

**Time:** 15 minutes  
**Questions:** 10  
**Passing Score:** 70%  
**Purpose:** Assess your baseline knowledge before learning about RAG systems

---

## Question 1 (Easy)

What does RAG stand for?

A) Random Access Generation  
B) Retrieval-Augmented Generation ✓  
C) Recursive Automated Generation  
D) Rapid AI Gateway  

<details>
<summary>Explanation</summary>

**Answer: B) Retrieval-Augmented Generation**

RAG is a technique that combines information retrieval with language generation. It retrieves relevant documents/passages and uses them to augment the LLM's response, grounding answers in factual sources.

**Reference:** Phase 7 - Introduction to RAG

</details>

---

## Question 2 (Easy)

What is the main problem that RAG solves?

A) Slow inference speed  
B) LLM hallucinations and outdated knowledge ✓  
C) High training costs  
D) Model size limitations  

<details>
<summary>Explanation</summary>

**Answer: B) LLM hallucinations and outdated knowledge**

**RAG addresses:**
- **Hallucinations:** LLMs making up facts → RAG grounds responses in retrieved documents
- **Outdated knowledge:** LLMs trained on old data → RAG accesses current information
- **Domain-specific needs:** LLMs lack specialized knowledge → RAG retrieves from custom knowledge bases

**Reference:** Phase 7 - Why RAG?

</details>

---

## Question 3 (Medium)

What are the three main components of a RAG system?

A) Train, Test, Deploy  
B) Indexing, Retrieval, Generation ✓  
C) Input, Process, Output  
D) Encode, Store, Decode  

<details>
<summary>Explanation</summary>

**Answer: B) Indexing, Retrieval, Generation**

**RAG Pipeline:**

1. **Indexing (Offline):**
   - Split documents into chunks
   - Create embeddings
   - Store in vector database

2. **Retrieval (Query time):**
   - Embed user query
   - Find similar chunks
   - Retrieve top-k relevant passages

3. **Generation (Query time):**
   - Combine query + retrieved docs
   - Send to LLM
   - Generate grounded response

**Reference:** Phase 7 - RAG Architecture

</details>

---

## Question 4 (Medium)

What is a vector embedding?

A) A compressed file format  
B) A numerical representation of text in high-dimensional space ✓  
C) A type of database index  
D) A machine learning model  

<details>
<summary>Explanation</summary>

**Answer: B) A numerical representation of text in high-dimensional space**

**Vector Embedding:**
- Converts text → array of numbers (e.g., 384, 768, or 1536 dimensions)
- Similar meaning → similar vectors (close in vector space)
- Enables semantic search (beyond keyword matching)

**Example:**
```python
"dog" → [0.12, -0.34, 0.56, ..., 0.78]  # 384 dims
"puppy" → [0.15, -0.31, 0.54, ..., 0.81]  # Similar!
"car" → [-0.45, 0.67, -0.23, ..., -0.12]  # Different
```

**Reference:** Phase 7 - Embeddings & Vector Search

</details>

---

## Question 5 (Medium)

What is the purpose of "chunking" documents in RAG?

A) To compress file size  
B) To break large documents into smaller, retrievable pieces ✓  
C) To encrypt data  
D) To format text for display  

<details>
<summary>Explanation</summary>

**Answer: B) To break large documents into smaller, retrievable pieces**

**Why chunk?**
- LLMs have token limits (can't process entire books)
- Retrieve only relevant sections (not entire documents)
- Better precision (specific paragraphs vs. whole pages)

**Chunking strategies:**
- **Fixed size:** 500 tokens per chunk
- **Sentence-based:** Complete sentences only
- **Semantic:** Chunks by topic/section
- **Overlap:** Chunks share 50-100 tokens

**Reference:** Phase 7 - Document Processing

</details>

---

## Question 6 (Hard)

Which similarity metric is commonly used to find relevant chunks?

A) Euclidean distance  
B) Manhattan distance  
C) Cosine similarity ✓  
D) Hamming distance  

<details>
<summary>Explanation</summary>

**Answer: C) Cosine similarity**

**Cosine Similarity:**
```python
similarity = (A · B) / (||A|| * ||B||)
```

**Range:** -1 to +1
- +1: Identical direction
- 0: Orthogonal (unrelated)
- -1: Opposite direction

**Why cosine?**
- Measures angle, not magnitude
- Works well for high-dimensional text embeddings
- Efficient to compute

**Alternatives:**
- **Dot product:** Faster but magnitude-sensitive
- **Euclidean:** Can work but less common

**Reference:** Phase 7 - Similarity Search

</details>

---

## Question 7 (Medium)

What is a vector database?

A) A SQL database with vectors  
B) A specialized database optimized for similarity search ✓  
C) A NoSQL document store  
D) A graph database  

<details>
<summary>Explanation</summary>

**Answer: B) A specialized database optimized for similarity search**

**Vector Databases:**
- Store high-dimensional embeddings efficiently
- Perform fast approximate nearest neighbor (ANN) search
- Scale to millions/billions of vectors

**Popular vector DBs:**
- Pinecone (managed)
- Weaviate (open-source)
- Qdrant (open-source)
- Chroma (lightweight)
- FAISS (Facebook AI library)

**Traditional databases can't:** Efficiently search "find most similar vectors" at scale

**Reference:** Phase 9 - Vector Databases

</details>

---

## Question 8 (Hard)

In a RAG system, what is the "context window"?

A) The time limit for queries  
B) The maximum tokens the LLM can process ✓  
C) The number of documents indexed  
D) The embedding dimension  

<details>
<summary>Explanation</summary>

**Answer: B) The maximum tokens the LLM can process**

**Context Window:**
- Maximum tokens LLM can handle in one request
- Includes: system prompt + retrieved docs + user query + response

**Example (GPT-3.5):**
- Context window: 4,096 tokens
- System prompt: 500 tokens
- Retrieved docs: 2,000 tokens
- User query: 100 tokens
- **Available for response:** 1,496 tokens

**Modern models:**
- GPT-4: 8K-128K tokens
- Claude 3: 200K tokens
- Gemini 1.5: 1M tokens

**RAG consideration:** Must fit retrieved chunks within context window!

**Reference:** Phase 7 - LLM Context Limits

</details>

---

## Question 9 (Medium)

What does "k" represent in "top-k retrieval"?

A) The number of keywords  
B) The number of documents to retrieve ✓  
C) The embedding dimension  
D) The chunk size  

<details>
<summary>Explanation</summary>

**Answer: B) The number of documents to retrieve**

**Top-k Retrieval:**
- Retrieve the **k most similar** chunks
- Common values: k = 3, 5, or 10

**Example:**
```python
# Query: "What is RAG?"
# Vector DB contains 10,000 chunks
# top_k = 5

results = vector_db.search(query_embedding, top_k=5)
# Returns 5 most relevant chunks
```

**Trade-offs:**
- **Small k (3):** Fast, focused, but might miss context
- **Large k (10):** More context, but slower and noisier

**Reference:** Phase 7 - Retrieval Strategies

</details>

---

## Question 10 (Hard)

What is the main difference between RAG and fine-tuning?

A) RAG is faster to deploy  
B) RAG retrieves external knowledge; fine-tuning updates model weights ✓  
C) RAG is more accurate  
D) Fine-tuning doesn't require data  

<details>
<summary>Explanation</summary>

**Answer: B) RAG retrieves external knowledge; fine-tuning updates model weights**

| Aspect | RAG | Fine-Tuning |
|--------|-----|-------------|
| **Knowledge source** | External documents (retrieved) | Model parameters (learned) |
| **Updates** | Add/remove documents anytime | Retrain model (expensive) |
| **Use case** | Factual Q&A, current data | Domain adaptation, style |
| **Cost** | Low (no retraining) | High (GPU hours) |
| **Transparency** | Can cite sources | Black box |

**When to use:**
- **RAG:** Frequently changing data, need citations
- **Fine-tuning:** Specialized behavior, consistent style
- **Both:** Often combined for best results!

**Reference:** Phase 7 - RAG vs Fine-Tuning

</details>

---

## Scoring Guide

**0-3 correct (0-30%):** RAG is an advanced topic. Make sure you've completed:
- Phase 5 (Neural Networks)
- Phase 10 (Prompt Engineering)
- Phase 8 (LangChain basics)

**4-5 correct (40-50%):** You have some relevant background. Review vector embeddings and LLM basics before starting.

**6-7 correct (60-70%):** Good foundation! You're ready to learn RAG with focused effort.

**8-9 correct (80-90%):** Excellent! You understand the core concepts. This phase will teach you implementation.

**10 correct (100%):** Outstanding! You may have RAG experience. You'll learn production best practices and advanced techniques.

---

## Prerequisites Checklist

Before starting Phase 7, ensure you understand:

- ✅ How LLMs work (Phase 10)
- ✅ Vector embeddings (Phase 9)
- ✅ Python and APIs
- ✅ Basic prompt engineering
- ✅ JSON and data structures

---

## Next Steps

**After this pre-quiz:**

1. **Score < 50%:** Review prerequisites first
   - Phase 10: Prompt Engineering
   - Phase 9: Vector Databases intro
   - LLM fundamentals

2. **Score 50-70%:** Start Phase 7 but take it slow
   - Revisit embedding concepts
   - Practice with simple examples
   - Ask questions in community

3. **Score > 70%:** Dive into Phase 7!
   - Build a RAG system
   - Complete the assignment
   - Try advanced challenges

---

**Remember:** RAG is complex but incredibly powerful. Take your time and build incrementally! 🚀📚
