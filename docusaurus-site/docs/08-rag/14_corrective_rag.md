---
title: "15. Corrective RAG"
sidebar_label: "15. Corrective RAG"
sidebar_position: 13
format: "md"
---
# Corrective RAG (CRAG-Style)

## Add a Reliability Loop Before Final Answer Generation

This notebook demonstrates a CRAG-style pattern for RAG systems:

1. retrieve evidence
2. grade whether the evidence is strong enough
3. retry with a better query if retrieval is weak
4. abstain if the system still lacks trustworthy support

The goal is to teach the control loop, not to reproduce the full paper implementation. In production, retrieval grading and query rewriting often use LLMs or learned models. Here we keep the logic lightweight and runnable.

```python
import re

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
```

## 1. Corpus and Benchmark

The benchmark includes one unsupported query so the notebook can demonstrate abstention rather than forcing every question into an answer.

```python
documents = [
    {
        "id": "doc_abstain_policy",
        "text": "A RAG system should abstain when retrieved evidence is weak, conflicting, or missing.",
    },
    {
        "id": "doc_query_rewrite",
        "text": "Query rewriting reformulates vague or incomplete questions into clearer standalone retrieval queries.",
    },
    {
        "id": "doc_hyde",
        "text": "HyDE generates a hypothetical answer before retrieval to improve semantic alignment for vague questions.",
    },
    {
        "id": "doc_retrieval_grading",
        "text": "Retrieval grading estimates whether the returned evidence is relevant enough to answer the question safely.",
    },
    {
        "id": "doc_contextual_compression",
        "text": "Contextual compression removes noisy passages so the final prompt contains only the strongest evidence.",
    },
]

benchmark = [
    {
        "question": "How should a RAG system behave when evidence is weak?",
        "relevant_docs": ["doc_abstain_policy", "doc_retrieval_grading"],
        "allow_abstain": False,
        "category": "reliability",
    },
    {
        "question": "How can I improve an underspecified retrieval query?",
        "relevant_docs": ["doc_query_rewrite", "doc_hyde"],
        "allow_abstain": False,
        "category": "query_fix",
    },
    {
        "question": "Who won the 2026 cricket world cup?",
        "relevant_docs": [],
        "allow_abstain": True,
        "category": "unsupported",
    },
]

doc_df = pd.DataFrame(documents)
benchmark_df = pd.DataFrame(benchmark)
doc_df
```

## 2. Baseline Retriever and Corrective Loop

The baseline retriever always answers from the initial result set. The corrective loop adds two behaviors:

- retry with a rewritten query when the first retrieval is weak
- abstain if the second pass is still not trustworthy

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

def normalize_tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def grade_retrieval(question, candidates):
    question_tokens = normalize_tokens(question)
    if not candidates:
        return 0.0

    scores = []
    for _, text, similarity in candidates:
        doc_tokens = normalize_tokens(text)
        overlap = len(question_tokens & doc_tokens) / max(1, len(question_tokens))
        scores.append(0.6 * float(similarity) + 0.4 * overlap)

    return max(scores)

def rewrite_query(question):
    q = question.lower()
    if "weak" in q or "evidence" in q:
        return "abstain when evidence is weak conflicting or missing retrieval grading"
    if "underspecified" in q or "retrieval query" in q:
        return "query rewriting hyde improve vague retrieval query"
    return question

def baseline_answer(question):
    retrieved = retrieve(question)
    top_doc = retrieved[0][0] if retrieved else None
    return {
        "mode": "baseline",
        "retrieved": [doc_id for doc_id, _, _ in retrieved],
        "score": grade_retrieval(question, retrieved),
        "status": "answer",
        "top_doc": top_doc,
    }

def corrective_answer(question, threshold=0.22):
    first_pass = retrieve(question)
    first_score = grade_retrieval(question, first_pass)

    if first_score >= threshold:
        return {
            "mode": "corrective",
            "retrieved": [doc_id for doc_id, _, _ in first_pass],
            "score": first_score,
            "status": "answer",
            "query_used": question,
        }

    rewritten = rewrite_query(question)
    second_pass = retrieve(rewritten)
    second_score = grade_retrieval(rewritten, second_pass)

    if second_score >= threshold:
        return {
            "mode": "corrective",
            "retrieved": [doc_id for doc_id, _, _ in second_pass],
            "score": second_score,
            "status": "answer_after_retry",
            "query_used": rewritten,
        }

    return {
        "mode": "corrective",
        "retrieved": [doc_id for doc_id, _, _ in second_pass],
        "score": second_score,
        "status": "abstain",
        "query_used": rewritten,
    }

baseline_answer("How can I improve an underspecified retrieval query?")
```

## 3. Compare Baseline vs Corrective RAG

We track two reliability-oriented outcomes here:

- whether the system retrieves relevant evidence
- whether it abstains on unsupported questions instead of pretending to know

```python
def recall_at_k(retrieved_doc_ids, relevant_doc_ids, k=3):
    if not relevant_doc_ids:
        return 1.0
    hits = sum(1 for doc_id in retrieved_doc_ids[:k] if doc_id in relevant_doc_ids)
    return hits / max(1, len(relevant_doc_ids))

rows = []
for item in benchmark:
    baseline = baseline_answer(item["question"])
    corrective = corrective_answer(item["question"])

    for name, result in [("baseline", baseline), ("corrective", corrective)]:
        abstain_success = 1 if (item["allow_abstain"] and result["status"] == "abstain") else 0
        rows.append(
            {
                "question": item["question"],
                "category": item["category"],
                "variant": name,
                "retrieved": result["retrieved"],
                "status": result["status"],
                "score": round(result["score"], 3),
                "recall@3": round(recall_at_k(result["retrieved"], item["relevant_docs"], k=3), 3),
                "abstain_success": abstain_success,
            }
        )

evaluation_df = pd.DataFrame(rows)
evaluation_df
```

```python
summary_df = (
    evaluation_df.groupby("variant")[["recall@3", "abstain_success", "score"]]
    .mean()
    .sort_values(by=["abstain_success", "recall@3", "score"], ascending=False)
)
summary_df
```

## 4. What This Notebook Teaches

A corrective loop is useful when the problem is not just ranking, but **whether the system should answer at all**.

The main lesson is simple:

- retrieve first
- grade evidence quality
- retry when retrieval is weak
- abstain when evidence is still not trustworthy

That is often a better reliability upgrade than adding more generation complexity.
