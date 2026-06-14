---
title: "4. LangChain RAG"
sidebar_label: "4. LangChain RAG"
sidebar_position: 5
format: "md"
---
# LangChain RAG

## Production-Ready RAG with LangChain

LangChain provides high-level abstractions for RAG!

### Features
- Document loaders (PDF, web, databases)
- Text splitters
- Vector store integrations
- LLM integrations
- Chain orchestration

```python
import numpy as np
import pandas as pd
from typing import List, Dict, Tuple
import json
import os
from pathlib import Path
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
```

## Quick Example

### A Complete RAG Pipeline in Five Lines

LangChain's power lies in composability. The code below initializes an embedding model (`OpenAIEmbeddings`), a vector store (`Chroma`), and an LLM (`ChatOpenAI`), then wires them together with `RetrievalQA.from_chain_type`. This single chain handles the full RAG workflow -- embedding the query, searching the vector store for the top-$k$ documents, constructing a prompt with the retrieved context, sending it to the LLM, and returning both the answer and the source documents. In production, you would add document loaders, text splitters, and error handling, but the core orchestration pattern remains the same.

```python
# Initialize components
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
print(result["result"])
```
