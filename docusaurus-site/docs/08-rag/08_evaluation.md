---
title: "9. Evaluation"
sidebar_label: "9. Evaluation"
sidebar_position: 9
format: "md"
---
# RAG Evaluation

## Measuring Whether Your RAG System Is Actually Better

Evaluation is what separates a demo from a defensible system.

A strong RAG evaluation setup answers questions like these:

- Did retrieval improve, or did the answer just sound better?
- Did reranking help enough to justify the latency?
- Did HyDE improve recall on vague questions?
- Is the system grounded in evidence, or hallucinating confidently?
- Is GraphRAG solving a real problem, or compensating for a weak baseline?

### Evaluation Ladder

Measure RAG in this order:

1. **Chunk quality**
2. **Retrieval quality**
3. **Context quality**
4. **Answer quality**
5. **Latency and cost**
6. **Failure behavior**

If you skip the early stages, later metrics become hard to interpret.

### What to Measure

**Retrieval metrics**
- Precision@K
- Recall@K
- MRR (Mean Reciprocal Rank)
- NDCG

**Context / grounding metrics**
- Context precision
- Context recall
- Evidence coverage

**Answer metrics**
- Faithfulness / groundedness
- Answer relevancy
- Correctness
- Citation quality

**Operational metrics**
- Latency
- Token usage
- Cost per query
- Abstention / failure rate

### Core rule

**Do not keep an advanced RAG technique unless it beats a simpler baseline on a benchmark that reflects the real task.**

```python
import math
from statistics import mean

import pandas as pd


# A tiny labeled benchmark for demonstration.
# In a real project, expand this to 50+ examples with source annotations.
evaluation_set = [
    {
        "question": "What is retrieval-augmented generation?",
        "relevant_docs": ["doc_rag_intro", "doc_retrieval_pipeline"],
        "ground_truth": "RAG combines retrieval with generation so an LLM can answer using external knowledge.",
        "category": "direct_lookup",
        "allow_abstain": False,
    },
    {
        "question": "How can you improve vague search queries in RAG?",
        "relevant_docs": ["doc_query_rewrite", "doc_hyde"],
        "ground_truth": "You can use query rewriting, multi-query retrieval, or HyDE to improve retrieval quality.",
        "category": "vague_query",
        "allow_abstain": False,
    },
    {
        "question": "When should a RAG system abstain from answering?",
        "relevant_docs": ["doc_faithfulness", "doc_abstain_policy"],
        "ground_truth": "It should abstain when the retrieved evidence is weak, conflicting, or insufficient.",
        "category": "unsupported_question",
        "allow_abstain": True,
    },
]


# Two toy system variants so we can compute metrics without external services.
variants = {
    "baseline_dense": [
        {
            "retrieved_docs": ["doc_rag_intro", "doc_embeddings", "doc_vector_db"],
            "answer": "RAG combines retrieval with generation so a model can answer using external knowledge.",
            "latency_ms": 620,
            "cost_usd": 0.003,
        },
        {
            "retrieved_docs": ["doc_embeddings", "doc_vector_db", "doc_query_rewrite"],
            "answer": "You can improve vague queries with query rewriting, and sometimes HyDE helps too.",
            "latency_ms": 710,
            "cost_usd": 0.004,
        },
        {
            "retrieved_docs": ["doc_hallucination", "doc_monitoring", "doc_vector_db"],
            "answer": "It should abstain when evidence is weak or insufficient.",
            "latency_ms": 690,
            "cost_usd": 0.004,
        },
    ],
    "hybrid_reranked": [
        {
            "retrieved_docs": ["doc_rag_intro", "doc_retrieval_pipeline", "doc_vector_db"],
            "answer": "RAG combines retrieval and generation so an LLM can answer with grounded external knowledge.",
            "latency_ms": 810,
            "cost_usd": 0.005,
        },
        {
            "retrieved_docs": ["doc_query_rewrite", "doc_hyde", "doc_vector_db"],
            "answer": "Use query rewriting, multi-query retrieval, or HyDE to improve vague search queries.",
            "latency_ms": 930,
            "cost_usd": 0.006,
        },
        {
            "retrieved_docs": ["doc_abstain_policy", "doc_faithfulness", "doc_monitoring"],
            "answer": "A RAG system should abstain when the evidence is weak, conflicting, or missing.",
            "latency_ms": 900,
            "cost_usd": 0.006,
        },
    ],
}


def precision_at_k(retrieved_docs, relevant_docs, k):
    top_k = retrieved_docs[:k]
    if not top_k:
        return 0.0
    hits = sum(1 for doc_id in top_k if doc_id in relevant_docs)
    return hits / len(top_k)



def recall_at_k(retrieved_docs, relevant_docs, k):
    if not relevant_docs:
        return 0.0
    top_k = retrieved_docs[:k]
    hits = sum(1 for doc_id in top_k if doc_id in relevant_docs)
    return hits / len(relevant_docs)



def reciprocal_rank(retrieved_docs, relevant_docs):
    for index, doc_id in enumerate(retrieved_docs, start=1):
        if doc_id in relevant_docs:
            return 1 / index
    return 0.0



def ndcg_at_k(retrieved_docs, relevant_docs, k):
    dcg = 0.0
    for index, doc_id in enumerate(retrieved_docs[:k], start=1):
        if doc_id in relevant_docs:
            dcg += 1 / math.log2(index + 1)

    ideal_hits = min(len(relevant_docs), k)
    idcg = sum(1 / math.log2(index + 1) for index in range(1, ideal_hits + 1))
    return dcg / idcg if idcg else 0.0



def answer_supports_ground_truth(answer, ground_truth):
    answer_tokens = set(answer.lower().replace("-", " ").split())
    truth_tokens = set(ground_truth.lower().replace("-", " ").split())
    overlap = answer_tokens & truth_tokens
    return len(overlap) / max(1, len(truth_tokens))



def score_variant(name, rows, benchmark):
    precision_scores = []
    recall_scores = []
    mrr_scores = []
    ndcg_scores = []
    support_scores = []
    latencies = []
    costs = []

    for expected, actual in zip(benchmark, rows):
        relevant_docs = expected["relevant_docs"]
        retrieved_docs = actual["retrieved_docs"]

        precision_scores.append(precision_at_k(retrieved_docs, relevant_docs, k=3))
        recall_scores.append(recall_at_k(retrieved_docs, relevant_docs, k=3))
        mrr_scores.append(reciprocal_rank(retrieved_docs, relevant_docs))
        ndcg_scores.append(ndcg_at_k(retrieved_docs, relevant_docs, k=3))
        support_scores.append(answer_supports_ground_truth(actual["answer"], expected["ground_truth"]))
        latencies.append(actual["latency_ms"])
        costs.append(actual["cost_usd"])

    return {
        "variant": name,
        "precision@3": round(mean(precision_scores), 3),
        "recall@3": round(mean(recall_scores), 3),
        "mrr": round(mean(mrr_scores), 3),
        "ndcg@3": round(mean(ndcg_scores), 3),
        "answer_support": round(mean(support_scores), 3),
        "latency_ms": round(mean(latencies), 1),
        "cost_usd": round(mean(costs), 4),
    }


results = pd.DataFrame(
    [score_variant(name, rows, evaluation_set) for name, rows in variants.items()]
).sort_values(by=["answer_support", "mrr"], ascending=False)

results
```

## Evaluation Framework

### Build the benchmark before adding architecture

A disciplined RAG evaluation loop looks like this:

1. Build a baseline system.
2. Create a labeled benchmark set.
3. Measure retrieval metrics first.
4. Measure answer quality second.
5. Track latency and cost.
6. Review failure cases manually.
7. Add one advanced technique.
8. Re-run the benchmark.

### Failure taxonomy

When a result is bad, classify it before changing the system:

- **Retrieval miss**: the right evidence was not retrieved.
- **Ranking failure**: the right evidence was retrieved but ranked too low.
- **Context assembly failure**: the right evidence was present but buried in noisy context.
- **Generation failure**: the answer is weak even though the context was good.
- **Architecture mismatch**: the task needs hierarchical, graph, or multimodal retrieval.

### Good comparison habit

Always compare advanced techniques against simpler baselines:

- dense retrieval
- hybrid retrieval
- hybrid + reranking

Only after those baselines should you evaluate HyDE, contextual compression, CRAG, Self-RAG, RAPTOR, or GraphRAG.

```python
# Example: category-level slices for analysis
benchmark_df = pd.DataFrame(evaluation_set)
benchmark_df

# You can use category slices to see where a technique helps.
# For example, HyDE might help vague queries but not direct lookup.
category_breakdown = []
for category in benchmark_df["category"].unique():
    category_rows = benchmark_df[benchmark_df["category"] == category]
    index_positions = list(category_rows.index)

    for name, rows in variants.items():
        subset_expected = [evaluation_set[i] for i in index_positions]
        subset_actual = [rows[i] for i in index_positions]
        row = score_variant(name, subset_actual, subset_expected)
        row["category"] = category
        category_breakdown.append(row)

pd.DataFrame(category_breakdown).sort_values(by=["category", "answer_support"], ascending=[True, False])
```

## Best Practices

✅ Create a labeled benchmark before adding advanced retrieval methods  
✅ Track retrieval metrics separately from answer metrics  
✅ Compare every upgrade against a simpler baseline  
✅ Review failure cases manually, not just aggregate scores  
✅ Measure latency and cost along with quality  
✅ Use abstention metrics for unsupported questions  
✅ Keep a regression set of hard questions and rerun it after every change

## Recommended tools

- **Ragas** for faithfulness, answer relevancy, and context-focused evaluation
- **DeepEval** for broader LLM-judge workflows
- **GroUSE** for contextually grounded generation evaluation
- Manual error review for the hardest and most business-critical examples

## Next step

Pair this notebook with:

- `08_rag_technique_selection.md` for choosing the next upgrade
- `08_rag_evaluation_playbook.md` for designing stronger benchmarks and ablations

**A better RAG system is not the one with the most architecture. It is the one that wins on the right benchmark.**
