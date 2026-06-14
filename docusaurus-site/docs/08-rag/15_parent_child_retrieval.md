---
title: "16. Parent Child Retrieval"
sidebar_label: "16. Parent Child Retrieval"
sidebar_position: 14
format: "md"
---
# Parent-Child Retrieval for RAG

## Preserve Local Relevance Without Losing Document Context

Flat chunk retrieval often returns a useful sentence or paragraph but loses the broader section that makes the answer complete. Parent-child retrieval fixes that by:

1. retrieving a small child chunk
2. mapping it back to a larger parent section
3. generating the final answer with both local evidence and wider context

This is one of the best structured-retrieval upgrades to learn before RAPTOR or GraphRAG.

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
```

## 1. Parent Documents and Child Chunks

Each parent document represents a larger section. Each child chunk is a smaller passage indexed for retrieval.

```python
parent_docs = [
    {
        "parent_id": "parent_query_expansion",
        "title": "Query expansion techniques",
        "text": "Query expansion improves weak retrieval by rewriting vague questions, generating multiple search queries, or using HyDE to embed a hypothetical answer. It helps when the user's wording does not match the corpus.",
    },
    {
        "parent_id": "parent_reranking",
        "title": "Reranking and context filtering",
        "text": "Reranking improves the ordering of retrieved passages after the first retrieval pass. Contextual compression removes noisy passages so the final context contains only the strongest evidence.",
    },
    {
        "parent_id": "parent_structured_retrieval",
        "title": "Structured retrieval for long documents",
        "text": "Parent-child retrieval preserves local relevance while expanding back to a larger section. RAPTOR organizes summaries hierarchically, and GraphRAG helps when answers depend on relationships and multi-hop reasoning.",
    },
]

child_chunks = [
    {
        "chunk_id": "chunk_query_rewrite",
        "parent_id": "parent_query_expansion",
        "text": "Query rewriting reformulates vague or incomplete user questions into clearer standalone search queries.",
    },
    {
        "chunk_id": "chunk_hyde",
        "parent_id": "parent_query_expansion",
        "text": "HyDE generates a hypothetical answer before retrieval to improve semantic alignment.",
    },
    {
        "chunk_id": "chunk_reranking",
        "parent_id": "parent_reranking",
        "text": "Reranking rescored candidate passages after initial retrieval to improve top-k quality.",
    },
    {
        "chunk_id": "chunk_compression",
        "parent_id": "parent_reranking",
        "text": "Contextual compression removes irrelevant text before generation.",
    },
    {
        "chunk_id": "chunk_parent_child",
        "parent_id": "parent_structured_retrieval",
        "text": "Parent-child retrieval retrieves fine-grained chunks, then expands to the larger parent section.",
    },
    {
        "chunk_id": "chunk_raptor",
        "parent_id": "parent_structured_retrieval",
        "text": "RAPTOR builds a tree of recursive summaries for long-document retrieval.",
    },
]

parent_df = pd.DataFrame(parent_docs)
child_df = pd.DataFrame(child_chunks)
parent_lookup = {row['parent_id']: row for row in parent_docs}

child_df
```

## 2. Benchmark Questions

These questions are designed so the answer benefits from retrieving a precise child chunk while still needing the broader parent section for complete context.

```python
benchmark = [
    {
        "question": "What helps when a user's wording does not match the corpus?",
        "relevant_chunk": "chunk_hyde",
        "relevant_parent": "parent_query_expansion",
        "category": "query_expansion",
    },
    {
        "question": "Which retrieval pattern keeps a precise match but expands back to a larger section?",
        "relevant_chunk": "chunk_parent_child",
        "relevant_parent": "parent_structured_retrieval",
        "category": "structured_retrieval",
    },
    {
        "question": "What should you do after the initial retrieval pass to improve top results?",
        "relevant_chunk": "chunk_reranking",
        "relevant_parent": "parent_reranking",
        "category": "reranking",
    },
]

pd.DataFrame(benchmark)
```

## 3. Child Retrieval vs Parent-Child Retrieval

The first system returns only the child chunk. The second system retrieves the child chunk and then expands to the parent section.

```python
vectorizer = TfidfVectorizer(stop_words="english")
child_matrix = vectorizer.fit_transform(child_df["text"])

def retrieve_child_chunks(question, top_k=2):
    query_vector = vectorizer.transform([question])
    similarities = cosine_similarity(query_vector, child_matrix)[0]
    ranking = sorted(
        zip(child_df["chunk_id"], child_df["parent_id"], child_df["text"], similarities),
        key=lambda row: row[3],
        reverse=True,
    )
    return ranking[:top_k]

def child_only_context(question):
    retrieved = retrieve_child_chunks(question, top_k=2)
    return {
        "chunks": [chunk_id for chunk_id, _, _, _ in retrieved],
        "parents": [],
        "context": [text for _, _, text, _ in retrieved],
    }

def parent_child_context(question):
    retrieved = retrieve_child_chunks(question, top_k=2)
    parent_ids = []
    parent_context = []

    for _, parent_id, _, _ in retrieved:
        if parent_id not in parent_ids:
            parent_ids.append(parent_id)
            parent_context.append(parent_lookup[parent_id]["text"])

    return {
        "chunks": [chunk_id for chunk_id, _, _, _ in retrieved],
        "parents": parent_ids,
        "context": parent_context,
    }

parent_child_context("Which retrieval pattern keeps a precise match but expands back to a larger section?")
```

## 4. Evaluate the Two Retrieval Modes

We evaluate both chunk-level retrieval and parent-level coverage.

```python
rows = []
for item in benchmark:
    child_only = child_only_context(item["question"])
    parent_child = parent_child_context(item["question"])

    rows.append({
        "question": item["question"],
        "category": item["category"],
        "variant": "child_only",
        "chunk_hit": int(item["relevant_chunk"] in child_only["chunks"]),
        "parent_hit": int(item["relevant_parent"] in child_only["parents"]),
        "retrieved_chunks": child_only["chunks"],
        "retrieved_parents": child_only["parents"],
    })

    rows.append({
        "question": item["question"],
        "category": item["category"],
        "variant": "parent_child",
        "chunk_hit": int(item["relevant_chunk"] in parent_child["chunks"]),
        "parent_hit": int(item["relevant_parent"] in parent_child["parents"]),
        "retrieved_chunks": parent_child["chunks"],
        "retrieved_parents": parent_child["parents"],
    })

evaluation_df = pd.DataFrame(rows)
evaluation_df
```

```python
summary_df = (
    evaluation_df.groupby("variant")[["chunk_hit", "parent_hit"]]
    .mean()
    .sort_values(by=["parent_hit", "chunk_hit"], ascending=False)
)
summary_df
```

## 5. What This Notebook Teaches

Parent-child retrieval is a strong next step when flat chunk retrieval finds the right local passage but loses the broader section needed for complete answers.

Why it matters:

- child chunks preserve local relevance
- parent sections restore surrounding context
- the pattern is much simpler than RAPTOR or GraphRAG

That makes parent-child retrieval one of the best structured-retrieval upgrades to learn before moving into heavier architectures.
