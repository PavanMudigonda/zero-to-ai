#!/usr/bin/env python3
"""Generate RAG (Retrieval-Augmented Generation) Notebooks"""
import json

def nb(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

def md(text):
    lines = text.split('\n')
    return {"cell_type": "markdown", "metadata": {}, "source": lines}

def code(text):
    lines = text.split('\n')
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": lines}

# Standard imports
std_imports = """import numpy as np
import pandas as pd
from typing import List, Dict, Tuple
import json
import os
from pathlib import Path"""

# Save helper function
def save_notebook(filename, cells):
    with open(filename, 'w') as f:
        json.dump(nb(cells), f, indent=2)

print("Creating RAG Notebooks...\n")
print("=" * 70)

# Notebook 0: START HERE
cells0 = [
    md("# RAG: Retrieval-Augmented Generation - START HERE\n\n## What is RAG?\n\n**RAG** = Retrieval-Augmented Generation\n\nA technique that enhances LLMs by giving them access to external knowledge!\n\n### The Problem\n\nLLMs have limitations:\n- Knowledge cutoff date\n- Can't access private/proprietary data\n- May hallucinate facts\n- Can't update without retraining\n\n### The Solution: RAG\n\n1. Store documents in a vector database\n2. When user asks a question, retrieve relevant docs\n3. Send docs + question to LLM\n4. LLM generates answer using retrieved context"),
    code(std_imports),
    md("## RAG Architecture\n\n```\nUser Query\n    ↓\n[Embed Query] → Vector DB\n    ↓             ↓\n    ↓      [Retrieve Top-K]\n    ↓             ↓\n    └─→ [Combine with Context]\n              ↓\n          [Send to LLM]\n              ↓\n          Response\n```\n\n**Key Components:**\n1. Document Store (Vector DB)\n2. Embedding Model\n3. Retriever\n4. LLM (Generator)"),
    md("## Quick Demo: Minimal RAG\n\nLet's build a tiny RAG system from scratch!"),
    code('''# Simple document store
documents = [
    "Python is a high-level programming language created by Guido van Rossum.",
    "Machine learning is a subset of AI that learns from data.",
    "RAG combines retrieval and generation for better LLM responses.",
    "Vector databases store embeddings for similarity search.",
    "LangChain is a framework for building LLM applications."
]

# Simulate embeddings (normally use OpenAI/sentence-transformers)
import numpy as np
np.random.seed(42)
doc_embeddings = np.random.randn(len(documents), 384)

print(f"Loaded {len(documents)} documents")
print(f"Embedding dimension: {doc_embeddings.shape[1]}")'''),
    md("## Retrieval Function\n\nFind most similar documents using cosine similarity"),
    code('''def cosine_similarity(a, b):
    """Compute cosine similarity between vectors."""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve(query_embedding, top_k=2):
    """Retrieve top-k most similar documents."""
    similarities = []
    for i, doc_emb in enumerate(doc_embeddings):
        sim = cosine_similarity(query_embedding, doc_emb)
        similarities.append((i, sim))
    
    # Sort by similarity
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Return top-k
    results = []
    for i, sim in similarities[:top_k]:
        results.append({
            'document': documents[i],
            'similarity': sim
        })
    return results

# Test retrieval
query_emb = np.random.randn(384)
results = retrieve(query_emb, top_k=2)

print("Retrieved Documents:")
for i, result in enumerate(results, 1):
    print(f"\\n{i}. Similarity: {result['similarity']:.4f}")
    print(f"   {result['document']}")'''),
    md("## Generation with Context\n\nCombine retrieved docs with query for LLM"),
    code('''def create_prompt(query: str, context_docs: List[str]) -> str:
    """Create prompt with retrieved context."""
    context = "\\n\\n".join([f"Document {i+1}: {doc}" 
                           for i, doc in enumerate(context_docs)])
    
    prompt = f"""Answer the question based on the context below.

Context:
{context}

Question: {query}

Answer:"""
    return prompt

# Example
query = "What is RAG?"
retrieved_docs = [r['document'] for r in results]
prompt = create_prompt(query, retrieved_docs)

print(prompt)
print("\\n" + "="*70)
print("This prompt would be sent to an LLM (GPT-4, Claude, etc.)")'''),
    md("## Why RAG Works\n\n### Benefits\n\n✅ **Up-to-date information** - Add new docs anytime\n✅ **Domain-specific knowledge** - Use your own data\n✅ **Reduced hallucinations** - LLM has facts to reference\n✅ **Source attribution** - Know where answers come from\n✅ **Cost effective** - No need to fine-tune LLM\n\n### Use Cases\n\n- Customer support chatbots\n- Document Q&A systems\n- Research assistants\n- Code documentation search\n- Legal/medical information retrieval"),
    md("## Next Steps\n\nThis series covers:\n\n1. **Basic RAG** - Build from scratch\n2. **Document Processing** - Chunking strategies\n3. **LangChain RAG** - Production framework\n4. **LlamaIndex RAG** - Alternative framework\n5. **Advanced Retrieval** - Hybrid search, re-ranking\n6. **Conversation RAG** - Memory and context\n7. **Evaluation** - Measuring RAG performance\n\nLet's dive in! 🚀")
]
save_notebook("00_START_HERE.ipynb", cells0)
print("✓ Notebook 00: START HERE - RAG Overview")

# Notebook 1: Basic RAG
cells1 = [
    md("# Basic RAG from Scratch\n\n## Building a Complete RAG System\n\nLet's build a real RAG system step-by-step!\n\n### Components\n1. Document loader\n2. Text chunker\n3. Embedding generator\n4. Vector store\n5. Retriever\n6. Generator (LLM)"),
    code(std_imports + "\nfrom sentence_transformers import SentenceTransformer\nimport chromadb\nfrom chromadb.config import Settings"),
    md("## Step 1: Load Documents\n\nIn production, you'd load from files, APIs, databases, etc."),
    code('''# Sample knowledge base
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
    print(f"  - {doc['id']}: {doc['content'][:50]}...")'''),
    md("## Step 2: Create Embeddings\n\nConvert text to vectors using a pre-trained model"),
    code('''# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')  # 384-dimensional

# Generate embeddings
texts = [doc["content"] for doc in documents]
embeddings = model.encode(texts)

print(f"Embedding shape: {embeddings.shape}")
print(f"Dimension: {embeddings.shape[1]}")
print(f"\\nFirst embedding (truncated):")
print(embeddings[0][:10])'''),
    md("## Step 3: Store in Vector Database\n\nUsing ChromaDB for local vector storage"),
    code('''# Initialize ChromaDB
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

print(f"Added {collection.count()} documents to vector store")'''),
    md("## Step 4: Implement Retrieval\n\nQuery the vector database for similar documents"),
    code('''def retrieve_context(query: str, top_k: int = 3):
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

print(f"Query: {query}\\n")
for i, result in enumerate(results, 1):
    print(f"{i}. Document: {result['id']}")
    print(f"   Distance: {result['distance']:.4f}")
    print(f"   Content: {result['content'][:100]}...")
    print()'''),
    md("## Step 5: Generate Response\n\nCombine retrieval with LLM generation"),
    code('''def generate_response(query: str, context_docs: List[Dict]) -> str:
    """Generate answer using retrieved context."""
    # Build context string
    context = "\\n\\n".join([
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
print("\\n" + "="*70)
print("Send this to GPT-4, Claude, or other LLM")'''),
    md("## Complete RAG Pipeline\n\nPutting it all together"),
    code('''class SimpleRAG:
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
    print()'''),
    md("## Summary\n\n### RAG Pipeline\n\n1. **Index Phase** (one-time)\n   - Load documents\n   - Generate embeddings\n   - Store in vector DB\n\n2. **Query Phase** (per request)\n   - Embed user query\n   - Retrieve similar docs\n   - Generate response with context\n\n### Key Takeaways\n\n✅ RAG provides LLMs with relevant context\n✅ Vector search finds semantically similar docs\n✅ No fine-tuning needed - works with any LLM\n✅ Easy to update - just add new documents\n\n**Next**: Learn advanced chunking strategies!")
]
save_notebook("01_basic_rag.ipynb", cells1)
print("✓ Notebook 01: Basic RAG from Scratch")

# Notebook 2: Document Processing
cells2 = [
    md("# Document Processing and Chunking\n\n## Why Chunking Matters\n\nLLMs have token limits. Documents must be split into chunks!\n\n### Challenges\n- Chunk too small → lose context\n- Chunk too large → exceed token limits\n- Poor splits → break semantic meaning\n\n### Strategies\n1. Fixed-size chunks\n2. Sentence-based\n3. Paragraph-based\n4. Semantic chunking\n5. Recursive chunking"),
    code(std_imports + "\nfrom langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter"),
    md("## Strategy 1: Fixed-Size Chunks\n\nSimplest approach - split by character count"),
    code('''text = """Artificial intelligence has transformed many industries. 
Machine learning algorithms can now process vast amounts of data. 
Deep learning networks achieve human-level performance in many tasks.
Natural language processing enables computers to understand human language.
Computer vision allows machines to interpret visual information."""

def fixed_size_chunk(text: str, chunk_size: int = 100, overlap: int = 20):
    """Split text into fixed-size chunks with overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

chunks = fixed_size_chunk(text)
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}: {chunk}...")
    print()'''),
    md("## Strategy 2: Sentence-Based\n\nSplit at sentence boundaries"),
    code('''import nltk
# nltk.download('punkt')  # Run once

def sentence_chunk(text: str, sentences_per_chunk: int = 2):
    """Split by sentences."""
    sentences = nltk.sent_tokenize(text)
    chunks = []
    for i in range(0, len(sentences), sentences_per_chunk):
        chunk = ' '.join(sentences[i:i+sentences_per_chunk])
        chunks.append(chunk)
    return chunks, sentences

chunks, sentences = sentence_chunk(text)
print(f"Total sentences: {len(sentences)}")
print(f"Total chunks: {len(chunks)}\\n")
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}: {chunk}")
    print()'''),
    md("## Strategy 3: Recursive Chunking\n\nTry multiple separators hierarchically"),
    code('''splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30,
    separators=["\\n\\n", "\\n", ". ", " ", ""]
)

long_text = """
Retrieval-Augmented Generation (RAG) is a powerful technique.

It combines two key components:
1. Information Retrieval
2. Text Generation

The retrieval step searches a knowledge base.
The generation step uses an LLM to create responses.

This approach has several advantages.
It reduces hallucinations and provides source attribution.
"""

chunks = splitter.split_text(long_text)
print(f"Created {len(chunks)} chunks:\\n")
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i} ({len(chunk)} chars):")
    print(chunk)
    print("-" * 50)'''),
    md("## Strategy 4: Semantic Chunking\n\nSplit based on meaning, not just length"),
    code('''from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_chunk(text: str, threshold: float = 0.5):
    """Chunk based on semantic similarity."""
    sentences = nltk.sent_tokenize(text)
    
    if len(sentences) <= 1:
        return [text]
    
    # Get embeddings
    embeddings = model.encode(sentences)
    
    # Compute similarities
    chunks = []
    current_chunk = [sentences[0]]
    
    for i in range(1, len(sentences)):
        # Similarity with previous
        sim = np.dot(embeddings[i], embeddings[i-1])
        sim /= (np.linalg.norm(embeddings[i]) * np.linalg.norm(embeddings[i-1]))
        
        if sim > threshold:
            current_chunk.append(sentences[i])
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentences[i]]
    
    chunks.append(' '.join(current_chunk))
    return chunks

semantic_chunks = semantic_chunk(text, threshold=0.6)
print(f"Semantic chunks: {len(semantic_chunks)}\\n")
for i, chunk in enumerate(semantic_chunks, 1):
    print(f"Semantic Chunk {i}:")
    print(chunk)
    print()'''),
    md("## Best Practices\n\n### Chunk Size Guidelines\n\n| Use Case | Chunk Size | Overlap |\n|----------|-----------|----------|\n| Short Q&A | 200-500 | 50-100 |\n| Documents | 500-1000 | 100-200 |\n| Code | 1000-2000 | 200-300 |\n\n### Tips\n\n✅ Keep context intact (don't split mid-sentence)\n✅ Add overlap to preserve context across chunks\n✅ Include metadata (source, page number, etc.)\n✅ Test different strategies for your domain\n✅ Monitor retrieval quality\n\n**Next**: Using LangChain for production RAG!")
]
save_notebook("02_document_processing.ipynb", cells2)
print("✓ Notebook 02: Document Processing & Chunking")

# Continue with shorter versions for remaining notebooks
cells3 = [
    md("# LangChain RAG\n\n## Production-Ready RAG with LangChain\n\nLangChain provides high-level abstractions for RAG!\n\n### Features\n- Document loaders (PDF, web, databases)\n- Text splitters\n- Vector store integrations\n- LLM integrations\n- Chain orchestration"),
    code(std_imports + "\nfrom langchain.vectorstores import Chroma\nfrom langchain.embeddings import OpenAIEmbeddings\nfrom langchain.chat_models import ChatOpenAI\nfrom langchain.chains import RetrievalQA"),
    md("## Quick Example"),
    code('''# Initialize components
embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Create vector store
vectorstore = Chroma(
    collection_name="my_docs",
    embedding_function=embeddings
)

# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)

# Query
result = qa_chain("What is machine learning?")
print(result["result"])''')
]
save_notebook("03_langchain_rag.ipynb", cells3)
print("✓ Notebook 03: LangChain RAG")

cells4 = [
    md("# LlamaIndex RAG\n\n## Alternative RAG Framework\n\nLlamaIndex (formerly GPT Index) specializes in data indexing!\n\n### Key Features\n- Data connectors (100+ sources)\n- Index structures (vector, keyword, graph)\n- Query engines\n- Response synthesis"),
    code(std_imports + "\nfrom llama_index import VectorStoreIndex, SimpleDirectoryReader\nfrom llama_index.llms import OpenAI"),
    md("## Quick Example"),
    code('''# Load documents
documents = SimpleDirectoryReader("./data").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine()
response = query_engine.query("Explain RAG")
print(response)''')
]
save_notebook("04_llamaindex_rag.ipynb", cells4)
print("✓ Notebook 04: LlamaIndex RAG")

cells5 = [
    md("# Advanced Retrieval\n\n## Hybrid Search\n\nCombine vector search with keyword search!\n\n### Why Hybrid?\n- Vector: Semantic similarity\n- Keyword: Exact matches\n- Together: Best of both worlds"),
    code(std_imports),
    md("## Re-ranking\n\nImprove retrieval quality by re-scoring results"),
    code('''# Pseudo-code for re-ranking
def rerank(query, initial_results):
    # Use cross-encoder for precise scoring
    scores = cross_encoder.predict([(query, doc) for doc in initial_results])
    # Sort by new scores
    reranked = sorted(zip(initial_results, scores), key=lambda x: x[1], reverse=True)
    return reranked''')
]
save_notebook("05_advanced_retrieval.ipynb", cells5)
print("✓ Notebook 05: Advanced Retrieval")

cells6 = [
    md("# Conversational RAG\n\n## RAG with Memory\n\nMaintain conversation context across turns!\n\n### Components\n1. Conversation history\n2. Context compression\n3. Query reformulation"),
    code(std_imports + "\nfrom langchain.memory import ConversationBufferMemory\nfrom langchain.chains import ConversationalRetrievalChain"),
    md("## Implementation"),
    code('''memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    memory=memory
)

# Multi-turn conversation
conversation_chain("What is RAG?")
conversation_chain("How does it work?")  # "it" refers to RAG
conversation_chain("What are the benefits?")''')
]
save_notebook("06_conversation_rag.ipynb", cells6)
print("✓ Notebook 06: Conversational RAG")

cells7 = [
    md("# RAG Evaluation\n\n## Measuring RAG Performance\n\n### Key Metrics\n1. **Retrieval Metrics**\n   - Precision@K\n   - Recall@K\n   - MRR (Mean Reciprocal Rank)\n\n2. **Generation Metrics**\n   - Faithfulness (to context)\n   - Answer relevancy\n   - Context precision\n\n3. **End-to-End**\n   - User satisfaction\n   - Response time"),
    code(std_imports + "\nfrom ragas import evaluate\nfrom ragas.metrics import faithfulness, answer_relevancy"),
    md("## Evaluation Framework"),
    code('''# Define test cases
test_cases = [
    {
        "question": "What is machine learning?",
        "expected_context": "ML definition",
        "ground_truth": "ML is a subset of AI..."
    }
]

# Evaluate
results = evaluate(
    test_cases,
    metrics=[faithfulness, answer_relevancy]
)

print(f"Faithfulness: {results['faithfulness']}")
print(f"Relevancy: {results['answer_relevancy']}")'''),
    md("## Best Practices\n\n✅ Create evaluation datasets\n✅ Monitor retrieval quality\n✅ Track latency and costs\n✅ A/B test different approaches\n✅ Collect user feedback\n\n**Congratulations!** You now understand RAG systems! 🎉")
]
save_notebook("07_evaluation.ipynb", cells7)
print("✓ Notebook 07: RAG Evaluation")

print("=" * 70)
print("\n🎉 SUCCESS! All 8 RAG notebooks created!")
print("\nTopics covered:")
print("  • RAG fundamentals and architecture")
print("  • Building RAG from scratch")
print("  • Document processing & chunking")
print("  • LangChain framework")
print("  • LlamaIndex framework")
print("  • Advanced retrieval techniques")
print("  • Conversational RAG")
print("  • Evaluation metrics")
print("\n" + "=" * 70)
