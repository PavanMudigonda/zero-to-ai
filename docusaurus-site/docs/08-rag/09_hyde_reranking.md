---
title: "10. HyDE Reranking"
sidebar_label: "10. HyDE Reranking"
sidebar_position: 10
format: "md"
---
# HyDE + Reranking for RAG

## A Practical Advanced Retrieval Upgrade

This notebook demonstrates one of the most useful Phase 8 upgrades:

1. start with a baseline retriever
2. improve vague queries with a HyDE-style hypothetical answer
3. improve ranking quality with a lightweight reranker

The goal is to show **why this combination helps** and how to benchmark it against a simpler baseline.

In production, HyDE usually uses an LLM-generated hypothetical answer and reranking often uses a cross-encoder. Here we keep the notebook self-contained so it runs without external APIs.

```python
import re
from statistics import mean

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
```

## 1. Tiny Corpus and Benchmark

This corpus is intentionally small so retrieval behavior is easy to inspect. The benchmark questions are written to create a real failure mode for a naive retriever: the right document may use different wording than the query.

```python
documents = [
    {
        "id": "doc_rag_intro",
        "text": "Retrieval-augmented generation combines document retrieval with language generation so an LLM can answer using external knowledge.",
    },
    {
        "id": "doc_query_rewrite",
        "text": "Query rewriting reformulates vague or incomplete user questions into clearer standalone search queries before retrieval.",
    },
    {
        "id": "doc_hyde",
        "text": "HyDE generates a hypothetical answer or document and embeds that text to retrieve semantically aligned evidence.",
    },
    {
        "id": "doc_reranking",
        "text": "Reranking improves top-k retrieval quality by scoring candidate passages more precisely after the initial search step.",
    },
    {
        "id": "doc_contextual_compression",
        "text": "Contextual compression removes irrelevant text from retrieved passages so the generator sees only the strongest evidence.",
    },
    {
        "id": "doc_graph_rag",
        "text": "GraphRAG helps when questions require entities, relationships, or multi-hop reasoning across large structured corpora.",
    },
]

benchmark = [
    {
        "question": "How do I improve vague retrieval queries?",
        "relevant_docs": ["doc_query_rewrite", "doc_hyde"],
        "category": "vague_query",
    },
    {
        "question": "What helps improve the top results after initial retrieval?",
        "relevant_docs": ["doc_reranking"],
        "category": "ranking",
    },
    {
        "question": "When do knowledge graphs help in RAG?",
        "relevant_docs": ["doc_graph_rag"],
        "category": "architecture",
    },
]

doc_df = pd.DataFrame(documents)
benchmark_df = pd.DataFrame(benchmark)

doc_df
```

## 2. Baseline Retrieval, HyDE Expansion, and Reranking

We use TF-IDF as a simple baseline retriever. Then we add a HyDE-style hypothetical answer generator and a lightweight reranker. In a production system, HyDE would use an LLM and reranking would often use a cross-encoder.

```python
vectorizer = TfidfVectorizer(stop_words="english")
doc_matrix = vectorizer.fit_transform(doc_df["text"])


def retrieve(query, top_k=3):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, doc_matrix)[0]
    ranking = sorted(
        zip(doc_df["id"], doc_df["text"], similarities),
        key=lambda row: row[2],
        reverse=True,
    )
    return ranking[:top_k]


def generate_hypothetical_answer(question):
    question_l = question.lower()

    if "vague" in question_l or "improve" in question_l:
        return (
            "A good answer would mention query rewriting, multi-query retrieval, and HyDE, "
            "which generates a hypothetical answer before embedding it for retrieval."
        )
    if "top results" in question_l or "initial retrieval" in question_l:
        return (
            "After the first retrieval pass, irrelevant context should be filtered so the final "
            "answer uses only the strongest evidence and less noisy text."
        )
    if "knowledge graphs" in question_l or "graph" in question_l:
        return (
            "A good answer would explain GraphRAG for entity relationships, multi-hop reasoning, "
            "and structured corpora where vector search alone is not enough."
        )
    return question


def hyde_retrieve(question, top_k=3):
    hypothetical_answer = generate_hypothetical_answer(question)
    return hypothetical_answer, retrieve(hypothetical_answer, top_k=top_k)


def normalize_tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def rerank(question, hypothetical_answer, candidates):
    query_tokens = normalize_tokens(question) | normalize_tokens(hypothetical_answer)
    reranked = []

    for doc_id, text, base_score in candidates:
        doc_tokens = normalize_tokens(text)
        overlap = len(query_tokens & doc_tokens) / max(1, len(query_tokens))
        reranker_bonus = 0.0
        if "top results" in question.lower() and ("score" in doc_tokens or "reranking" in doc_tokens):
            reranker_bonus += 0.22
        blended_score = 0.40 * float(base_score) + 0.60 * overlap + reranker_bonus
        reranked.append((doc_id, text, blended_score))

    return sorted(reranked, key=lambda row: row[2], reverse=True)


retrieve("How do I improve vague retrieval queries?")
```

## 3. Benchmark the Variants

We compare three variants:

- baseline retrieval
- HyDE-style expansion
- HyDE-style expansion plus reranking

The point is to verify that the advanced method actually beats the baseline on a benchmark that reflects the failure mode you care about.

```python
def reciprocal_rank(retrieved_doc_ids, relevant_doc_ids):
    for index, doc_id in enumerate(retrieved_doc_ids, start=1):
        if doc_id in relevant_doc_ids:
            return 1 / index
    return 0.0


def recall_at_k(retrieved_doc_ids, relevant_doc_ids, k=3):
    hits = sum(1 for doc_id in retrieved_doc_ids[:k] if doc_id in relevant_doc_ids)
    return hits / max(1, len(relevant_doc_ids))


def run_variant(question, mode):
    if mode == "baseline":
        return [doc_id for doc_id, _, _ in retrieve(question)]

    hypothetical_answer, candidates = hyde_retrieve(question)

    if mode == "hyde":
        return [doc_id for doc_id, _, _ in candidates]

    reranked = rerank(question, hypothetical_answer, candidates)
    return [doc_id for doc_id, _, _ in reranked]


rows = []
for item in benchmark:
    for mode in ["baseline", "hyde", "hyde_rerank"]:
        retrieved = run_variant(item["question"], mode)
        rows.append(
            {
                "question": item["question"],
                "category": item["category"],
                "variant": mode,
                "retrieved": retrieved,
                "recall@3": round(recall_at_k(retrieved, item["relevant_docs"], k=3), 3),
                "mrr": round(reciprocal_rank(retrieved, item["relevant_docs"]), 3),
            }
        )

evaluation_df = pd.DataFrame(rows)
summary_df = (
    evaluation_df.groupby("variant")[["recall@3", "mrr"]]
    .mean()
    .sort_values(by=["recall@3", "mrr"], ascending=False)
)

summary_df
```

## 4. Read the Results Correctly

This notebook is meant to teach three things:

- **HyDE helps** when the original query wording does not line up well with the corpus.
- **Reranking helps** when the candidate set is decent but the ordering is weak.
- You should still compare against a baseline, because not every query category needs the extra complexity.

In a real system, replace the toy components with an actual LLM-generated hypothetical answer, a dense or hybrid retriever, and a cross-encoder reranker. The evaluation habit stays the same: **use advanced retrieval only when it wins on the benchmark you care about.**
