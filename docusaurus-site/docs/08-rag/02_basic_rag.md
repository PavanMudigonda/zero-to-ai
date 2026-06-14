---
title: "2. Basic RAG"
sidebar_label: "2. Basic RAG"
sidebar_position: 3
format: "md"
---
# Basic RAG from Scratch

## Building a Complete RAG System

Let's build a real RAG system step-by-step!

### Components
1. Document loader
2. Text chunker
3. Embedding generator
4. Vector store
5. Retriever
6. Generator (LLM)

```python
import numpy as np
import pandas as pd
from typing import List, Dict, Tuple
import json
import os
from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
```

## Step 1: Load Documents

### Ingesting Your Knowledge Base

Every RAG system starts with a **document corpus** -- the collection of texts the model will draw upon when answering questions. Documents can come from files (PDF, HTML, Markdown), APIs, databases, or any other source. Each document is stored with an `id`, the raw `content`, and optional `metadata` (source file name, topic tag, creation date) that can be used for filtering at query time. In production, you would use dedicated document loaders (e.g., LangChain's `DirectoryLoader` or LlamaIndex's `SimpleDirectoryReader`) to handle diverse file formats automatically.

```python
# Sample knowledge base
documents = [
    {
        "id": "doc1",
        "content": "Artificial Intelligence (AI) is the simulation of human intelligence by machines. It includes machine learning, natural language processing, and computer vision.",
        "metadata": {"source": "ai_basics.txt", "topic": "AI"}
    },
    {
        "id": "doc2", 
        "content": "Machine Learning is a subset of AI that enables systems to learn from data without explicit programming. Common algorithms include decision trees, neural networks, and support vector machines.",
        "metadata": {"source": "ml_guide.txt", "topic": "ML"}
    },
    {
        "id": "doc3",
        "content": "RAG (Retrieval-Augmented Generation) combines information retrieval with text generation. It retrieves relevant documents and uses them as context for generating responses.",
        "metadata": {"source": "rag_explained.txt", "topic": "RAG"}
    },
    {
        "id": "doc4",
        "content": "Vector databases store data as high-dimensional vectors (embeddings). They enable fast similarity search using techniques like HNSW and IVF indexes.",
        "metadata": {"source": "vectordb_intro.txt", "topic": "Databases"}
    },
    {
        "id": "doc5",
        "content": "Embeddings are numerical representations of text that capture semantic meaning. Similar texts have similar embeddings in vector space.",
        "metadata": {"source": "embeddings_101.txt", "topic": "Embeddings"}
    }
]

print(f"Loaded {len(documents)} documents")
for doc in documents:
    print(f"  - {doc['id']}: {doc['content'][:50]}...")
```

## Step 2: Create Embeddings

### Converting Text to Searchable Vectors

Raw text cannot be compared mathematically, so we convert each document into a dense vector (embedding) using a pre-trained encoder. The `SentenceTransformer` model `all-MiniLM-L6-v2` maps text to 384-dimensional vectors such that semantically similar sentences are close together in the vector space. This is the same embedding step used when building a vector database, and the quality of your embeddings directly determines the quality of your retrieval -- if two texts that should match are far apart in embedding space, the retriever will never surface them together.

```python
# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')  # 384-dimensional

# Generate embeddings
texts = [doc["content"] for doc in documents]
embeddings = model.encode(texts)

print(f"Embedding shape: {embeddings.shape}")
print(f"Dimension: {embeddings.shape[1]}")
print(f"\nFirst embedding (truncated):")
print(embeddings[0][:10])
```

## Step 3: Store in Vector Database

### Indexing Documents for Fast Retrieval

Once embeddings are computed, they are stored in a **vector database** that builds an index for fast similarity search. We use ChromaDB here because it runs in-process with zero configuration, making it ideal for prototyping. The `collection.add()` call stores each document's embedding, raw text, and metadata together. At query time, ChromaDB will use its internal HNSW index to find the nearest embeddings in sub-linear time, avoiding the cost of comparing against every document.

```python
# Initialize ChromaDB
client = chromadb.Client(Settings(
    anonymized_telemetry=False,
    allow_reset=True
))

# Create collection
collection = client.create_collection(
    name="knowledge_base",
    metadata={"description": "RAG knowledge base"}
)

# Add documents
collection.add(
    ids=[doc["id"] for doc in documents],
    embeddings=embeddings.tolist(),
    documents=texts,
    metadatas=[doc["metadata"] for doc in documents]
)

print(f"Added {collection.count()} documents to vector store")
```

## Step 4: Implement Retrieval

### Querying the Vector Store for Relevant Context

The retrieval function takes a natural-language question, embeds it with the same model used for documents, and queries the vector database for the `top_k` nearest neighbors. The key insight is that because both query and documents live in the same embedding space, semantic similarity translates directly into vector proximity. Results include the document text, distance score, and metadata, giving the downstream generator everything it needs to produce a grounded answer with source citations.

```python
def retrieve_context(query: str, top_k: int = 3):
    """Retrieve relevant documents for a query."""
    # Embed query
    query_embedding = model.encode([query])[0]
    
    # Search vector DB
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )
    
    # Format results
    contexts = []
    for i in range(len(results['documents'][0])):
        contexts.append({
            'id': results['ids'][0][i],
            'content': results['documents'][0][i],
            'distance': results['distances'][0][i],
            'metadata': results['metadatas'][0][i]
        })
    
    return contexts

# Test retrieval
query = "What is machine learning?"
results = retrieve_context(query, top_k=2)

print(f"Query: {query}\n")
for i, result in enumerate(results, 1):
    print(f"{i}. Document: {result['id']}")
    print(f"   Distance: {result['distance']:.4f}")
    print(f"   Content: {result['content'][:100]}...")
    print()
```

## Step 5: Generate Response

### Grounding the LLM with Retrieved Evidence

The generator builds a prompt that injects the retrieved documents as context and instructs the LLM to answer based only on that context. This "closed-book with evidence" approach dramatically reduces hallucination compared to asking the LLM to rely solely on its parametric memory. In production, you would call an API like `openai.ChatCompletion.create` or `anthropic.messages.create` to send this prompt. The returned answer can be paired with source document IDs for transparent attribution.

```python
def generate_response(query: str, context_docs: List[Dict]) -> str:
    """Generate answer using retrieved context."""
    # Build context string
    context = "\n\n".join([
        f"[Source: {doc['id']}] {doc['content']}" 
        for doc in context_docs
    ])
    
    # Create prompt
    prompt = f"""You are a helpful AI assistant. Answer the question based only on the provided context.

Context:
{context}

Question: {query}

Answer (cite sources):"""
    
    # In production, send to OpenAI/Anthropic/etc
    # For demo, return prompt
    return prompt

# Generate
response_prompt = generate_response(query, results)
print(response_prompt)
print("\n" + "="*70)
print("Send this to GPT-4, Claude, or other LLM")
```

## Complete RAG Pipeline

### Encapsulating the Full Workflow

The `SimpleRAG` class below wraps retrieval and prompt generation into a single `query` method, establishing the pattern you will see in every RAG framework. The pipeline executes three steps per request: **(1)** embed the user's question, **(2)** retrieve the top-$k$ most relevant documents from the vector store, and **(3)** assemble a prompt that combines the question with the retrieved context. In a production deployment, a fourth step would send this prompt to an LLM and return the generated answer alongside source citations.

```python
class SimpleRAG:
    """Simple RAG system."""
    
    def __init__(self, embedding_model, vector_store):
        self.model = embedding_model
        self.collection = vector_store
    
    def query(self, question: str, top_k: int = 3) -> Dict:
        """Execute RAG query."""
        # 1. Retrieve
        contexts = retrieve_context(question, top_k)
        
        # 2. Generate prompt
        prompt = generate_response(question, contexts)
        
        # 3. Return (would call LLM here)
        return {
            'question': question,
            'retrieved_docs': contexts,
            'prompt': prompt,
            'sources': [doc['id'] for doc in contexts]
        }

# Initialize RAG
rag = SimpleRAG(model, collection)

# Test queries
test_queries = [
    "Explain vector databases",
    "What is the difference between AI and ML?",
    "How does RAG work?"
]

for q in test_queries:
    print(f"Q: {q}")
    result = rag.query(q, top_k=2)
    print(f"Sources: {result['sources']}")
    print()
```

## Summary

### RAG Pipeline

1. **Index Phase** (one-time)
   - Load documents
   - Generate embeddings
   - Store in vector DB

2. **Query Phase** (per request)
   - Embed user query
   - Retrieve similar docs
   - Generate response with context

### Key Takeaways

✅ RAG provides LLMs with relevant context
✅ Vector search finds semantically similar docs
✅ No fine-tuning needed - works with any LLM
✅ Easy to update - just add new documents

**Next**: Learn advanced chunking strategies!
