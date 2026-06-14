---
title: "3. Document Processing"
sidebar_label: "3. Document Processing"
sidebar_position: 4
format: "md"
---
# Document Processing and Chunking

## Why Chunking Matters

LLMs have token limits. Documents must be split into chunks!

### Challenges
- Chunk too small → lose context
- Chunk too large → exceed token limits
- Poor splits → break semantic meaning

### Strategies
1. Fixed-size chunks
2. Sentence-based
3. Paragraph-based
4. Semantic chunking
5. Recursive chunking

```python
import numpy as np
import pandas as pd
from typing import List, Dict, Tuple
import json
import os
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
```

## Strategy 1: Fixed-Size Chunks

### The Simplest Approach -- Split by Character Count

Fixed-size chunking divides text into segments of a predetermined number of characters, optionally with an **overlap** window so that sentences at chunk boundaries are not lost. The overlap ensures continuity -- if a key fact spans two chunks, it will appear in full in at least one of them. While this method is fast and predictable, it pays no attention to sentence or paragraph boundaries, so chunks may start or end mid-sentence. Despite this limitation, fixed-size chunking is a reasonable baseline and is often sufficient when combined with a generous overlap (10-20% of chunk size).

```python
text = """Artificial intelligence has transformed many industries. 
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
    print()
```

## Strategy 2: Sentence-Based

### Preserving Linguistic Boundaries

Sentence-based chunking uses a tokenizer (such as NLTK's `sent_tokenize`) to split text at sentence boundaries, then groups a fixed number of sentences per chunk. Because it never breaks a sentence in half, each chunk is more coherent than a fixed-character chunk. The trade-off is that chunk sizes vary depending on sentence length, which can cause some chunks to be much larger or smaller than others. Grouping 2-5 sentences per chunk is a good starting point for Q&A-style RAG systems.

```python
import nltk
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
print(f"Total chunks: {len(chunks)}\n")
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}: {chunk}")
    print()
```

## Strategy 3: Recursive Chunking

### Hierarchical Splitting for Structured Text

LangChain's `RecursiveCharacterTextSplitter` tries a prioritized list of separators -- first double newlines (paragraph breaks), then single newlines, then sentence-ending periods, then spaces, and finally individual characters. It picks the highest-priority separator that produces chunks within the target `chunk_size`. This strategy naturally respects document structure: it will split at paragraph boundaries when possible, fall back to sentences when paragraphs are too long, and resort to character-level splitting only as a last resort. This makes it the recommended default splitter for most RAG applications.

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30,
    separators=["\n\n", "\n", ". ", " ", ""]
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
print(f"Created {len(chunks)} chunks:\n")
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i} ({len(chunk)} chars):")
    print(chunk)
    print("-" * 50)
```

## Strategy 4: Semantic Chunking

### Splitting Based on Meaning, Not Just Length

Semantic chunking uses an embedding model to measure the **cosine similarity** between consecutive sentences. When the similarity drops below a threshold, it signals a topic shift, and a new chunk begins. Sentences about the same topic stay together regardless of length, while topic transitions produce clean chunk boundaries. The downside is the added compute cost of embedding every sentence, but for corpora where topical coherence within chunks is critical (e.g., technical documentation, legal text), the retrieval quality improvement justifies the expense.

```python
from sentence_transformers import SentenceTransformer

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
print(f"Semantic chunks: {len(semantic_chunks)}\n")
for i, chunk in enumerate(semantic_chunks, 1):
    print(f"Semantic Chunk {i}:")
    print(chunk)
    print()
```

## Best Practices

### Chunk Size Guidelines

| Use Case | Chunk Size | Overlap |
|----------|-----------|----------|
| Short Q&A | 200-500 | 50-100 |
| Documents | 500-1000 | 100-200 |
| Code | 1000-2000 | 200-300 |

### Tips

✅ Keep context intact (don't split mid-sentence)
✅ Add overlap to preserve context across chunks
✅ Include metadata (source, page number, etc.)
✅ Test different strategies for your domain
✅ Monitor retrieval quality

**Next**: Using LangChain for production RAG!
