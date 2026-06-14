---
title: "7. Conversation RAG"
sidebar_label: "7. Conversation RAG"
sidebar_position: 8
format: "md"
---
# Conversational RAG

## RAG with Memory

### Maintaining Context Across Turns

Standard RAG treats every query independently, but real conversations are full of pronouns ("it"), ellipsis ("what about the cost?"), and follow-up references that only make sense in the context of prior turns. **Conversational RAG** solves this by maintaining a chat history and reformulating each new query to be self-contained before sending it to the retriever. For example, if the user first asks "What is RAG?" and then asks "How does it handle hallucinations?", the system rewrites the second query to "How does RAG handle hallucinations?" so the retriever can find the right documents.

### Components
1. **Conversation history** -- a buffer or summary of previous turns
2. **Context compression** -- condensing long histories to fit token limits
3. **Query reformulation** -- rewriting ambiguous queries using conversation context

```python
import numpy as np
import pandas as pd
from typing import List, Dict, Tuple
import json
import os
from pathlib import Path
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
```

## Implementation

### Wiring Up Memory with LangChain

LangChain's `ConversationalRetrievalChain` integrates a `ConversationBufferMemory` that stores the full chat history and automatically reformulates each new query by prepending the conversation context. The chain first uses the LLM to produce a standalone version of the latest question (resolving pronouns and references), then retrieves relevant documents, and finally generates a response that is aware of the entire conversation. The `memory_key="chat_history"` parameter tells the chain where to look for prior turns in the prompt template.

```python
memory = ConversationBufferMemory(
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
conversation_chain("What are the benefits?")
```
