---
title: "5. LlamaIndex RAG"
sidebar_label: "5. LlamaIndex RAG"
sidebar_position: 6
format: "md"
---
# LlamaIndex RAG

## Alternative RAG Framework

LlamaIndex (formerly GPT Index) specializes in data indexing!

### Key Features
- Data connectors (100+ sources)
- Index structures (vector, keyword, graph)
- Query engines
- Response synthesis

```python
import numpy as np
import pandas as pd
from typing import List, Dict, Tuple
import json
import os
from pathlib import Path
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms import OpenAI
```

## Quick Example

### From Directory to Answers in Three Steps

LlamaIndex takes a data-first approach to RAG. `SimpleDirectoryReader` loads all files from a directory (PDF, TXT, DOCX, and more), `VectorStoreIndex.from_documents` chunks the text, generates embeddings, and builds an in-memory vector index in one call, and `index.as_query_engine()` returns a query interface that handles retrieval and generation. Under the hood, LlamaIndex manages chunk sizes, embedding batching, prompt templates, and response synthesis. This makes it exceptionally fast to prototype RAG applications -- you can go from raw documents to a working question-answering system in under ten lines of code.

```python
# Load documents
documents = SimpleDirectoryReader("./data").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine()
response = query_engine.query("Explain RAG")
print(response)
```
