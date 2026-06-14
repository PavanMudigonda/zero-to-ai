---
title: "17. Raptor Retrieval"
sidebar_label: "17. Raptor Retrieval"
sidebar_position: 15
format: "md"
---
# RAPTOR-Style Hierarchical Retrieval

**RAPTOR** (Recursive Abstractive Processing for Tree-Organized Retrieval) builds a
**tree of summaries** over your chunk corpus. Leaf nodes are original chunks; higher
nodes are progressively coarser summaries. At query time the system can retrieve
at whatever level of detail matches the question.

This notebook implements a minimal, self-contained RAPTOR-style pipeline using only
TF-IDF and rule-based summarisation so it runs without API keys.

**What you will learn:**
1. How to build a hierarchical summary tree from chunks.
2. Why tree-based retrieval beats flat retrieval for multi-hop questions.
3. How to compare *flat*, *parent-child*, and *RAPTOR* retrieval on a toy benchmark.

**Prerequisite:** Work through `12_parent_child_retrieval.ipynb` first.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math
import statistics
```

## 1 - Build the Corpus

We use three *sections* of text, each split into two leaf chunks.  This mirrors a
small knowledge base about a fictional AI startup.

```python
# ---------------------------------------------------------------------------
# Leaf chunks - the finest grain of information
# ---------------------------------------------------------------------------
leaf_chunks = [
    # Section A - Founding
    {"id": "A1", "section": "A", "text": "NovaMind was founded in 2022 by Dr. Lena Torres and Marcus Chen in Austin, Texas."},
    {"id": "A2", "section": "A", "text": "The founders met at MIT where they published early work on retrieval-augmented generation."},
    # Section B - Product
    {"id": "B1", "section": "B", "text": "NovaMind's flagship product, Cortex, is an enterprise RAG engine that indexes internal documents."},
    {"id": "B2", "section": "B", "text": "Cortex uses a two-stage pipeline: sparse BM25 pre-retrieval followed by dense cross-encoder reranking."},
    # Section C - Funding
    {"id": "C1", "section": "C", "text": "In July 2024 NovaMind raised a 40 million dollar Series B led by Sequoia Capital."},
    {"id": "C2", "section": "C", "text": "The funds will be used to expand internationally and double the engineering team to 120 people."},
]

print(f"{len(leaf_chunks)} leaf chunks across {len(set(c['section'] for c in leaf_chunks))} sections")
```

## 2 - Build the Summary Tree

RAPTOR clusters leaf nodes, then summarises each cluster to produce **level-1**
nodes.  Level-1 nodes are then clustered and summarised into **level-2** nodes,
continuing until a single root summary exists.

Here we use a simple rule-based summariser (sentence concatenation + truncation)
instead of an LLM.  In production you would replace `summarise()` with a call to
GPT-4o, Claude, or a local model.

```python
# ---------------------------------------------------------------------------
# Rule-based summariser (substitute with LLM in production)
# ---------------------------------------------------------------------------
def summarise(texts: list[str], max_words: int = 40) -> str:
    """Combine texts and truncate to max_words as a cheap summary proxy."""
    combined = " ".join(texts)
    words = combined.split()
    return " ".join(words[:max_words]) + ("..." if len(words) > max_words else "")


# ---------------------------------------------------------------------------
# Build the tree bottom-up
# ---------------------------------------------------------------------------
# Level 0: leaf chunks (already defined)
level_0 = {c["id"]: c["text"] for c in leaf_chunks}

# Level 1: one summary per section (group by section)
sections = sorted(set(c["section"] for c in leaf_chunks))
level_1 = {}
for sec in sections:
    texts = [c["text"] for c in leaf_chunks if c["section"] == sec]
    level_1[f"L1_{sec}"] = summarise(texts, max_words=30)

# Level 2: single root summary over all level-1 nodes
level_2 = {"ROOT": summarise(list(level_1.values()), max_words=50)}

# Combine all nodes into a single index
tree_nodes = {}
for nid, text in level_0.items():
    tree_nodes[nid] = {"level": 0, "text": text}
for nid, text in level_1.items():
    tree_nodes[nid] = {"level": 1, "text": text}
for nid, text in level_2.items():
    tree_nodes[nid] = {"level": 2, "text": text}

print("=== Summary tree ===")
for nid, info in sorted(tree_nodes.items(), key=lambda x: (x[1]["level"], x[0])):
    print(f"  [{info['level']}] {nid:8s}  {info['text'][:80]}")
```

## 3 - Define the Benchmark

We create questions at three granularity levels:

| Type | Example | Best retrieval level |
|------|---------|---------------------|
| Detail | Who cofounded NovaMind? | Leaf (level 0) |
| Section | What does Cortex do? | Section summary (level 1) |
| Overview | Summarise NovaMind | Root summary (level 2) |

```python
benchmark = [
    # Detail questions - best answered by leaf chunks
    {
        "query": "Who cofounded NovaMind?",
        "relevant_ids": {"A1", "A2"},
        "category": "detail",
    },
    {
        "query": "How much did NovaMind raise in Series B?",
        "relevant_ids": {"C1"},
        "category": "detail",
    },
    # Section-level question - best answered by a section summary
    {
        "query": "How does the Cortex product pipeline work?",
        "relevant_ids": {"B1", "B2", "L1_B"},
        "category": "section",
    },
    # Overview question - best answered by the root summary
    {
        "query": "Give me a high-level overview of NovaMind",
        "relevant_ids": {"L1_A", "L1_B", "L1_C", "ROOT"},
        "category": "overview",
    },
]

print(f"{len(benchmark)} benchmark questions")
for q in benchmark:
    print(f"  [{q['category']:8s}] {q['query']}")
```

## 4 - Retrieval Variants

We compare three strategies:

1. **Flat** - search only leaf chunks (level 0).  This is standard RAG.
2. **Parent-child** - search leaf chunks, then expand to include the section summary.
3. **RAPTOR** - search *all* tree nodes (leaves + summaries) simultaneously.

```python
def retrieve_top_k(query: str, candidates: dict[str, str], k: int = 3) -> list[tuple[str, float]]:
    """Return top-k (node_id, score) pairs by TF-IDF cosine similarity."""
    ids = list(candidates.keys())
    texts = list(candidates.values())
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(texts + [query])
    scores = cosine_similarity(tfidf[-1:], tfidf[:-1]).flatten()
    ranked = sorted(zip(ids, scores), key=lambda x: x[1], reverse=True)
    return ranked[:k]


# --- Flat retrieval: only leaf chunks ---------------------------------
def flat_retrieve(query: str, k: int = 3) -> list[str]:
    candidates = {nid: info["text"] for nid, info in tree_nodes.items() if info["level"] == 0}
    return [nid for nid, _ in retrieve_top_k(query, candidates, k)]


# --- Parent-child: retrieve leaves then expand to section summary -----
def parent_child_retrieve(query: str, k: int = 3) -> list[str]:
    leaf_results = flat_retrieve(query, k)
    result_ids = list(leaf_results)
    # expand: for each leaf, add its L1 section summary
    for lid in leaf_results:
        sec = next((c["section"] for c in leaf_chunks if c["id"] == lid), None)
        if sec:
            l1_id = f"L1_{sec}"
            if l1_id not in result_ids:
                result_ids.append(l1_id)
    return result_ids


# --- RAPTOR: search the full tree ------------------------------------
def raptor_retrieve(query: str, k: int = 3) -> list[str]:
    candidates = {nid: info["text"] for nid, info in tree_nodes.items()}
    return [nid for nid, _ in retrieve_top_k(query, candidates, k)]


# Quick sanity check
sample_q = "Give me a high-level overview of NovaMind"
print("Flat:        ", flat_retrieve(sample_q))
print("Parent-child:", parent_child_retrieve(sample_q))
print("RAPTOR:      ", raptor_retrieve(sample_q))
```

## 5 - Evaluate

For each question we measure:
- **Recall@k** - fraction of relevant IDs present in the retrieved set.
- **Highest level hit** - the highest tree level returned that is relevant (0 = leaf, 1 = section, 2 = root).

```python
variants = {
    "flat": flat_retrieve,
    "parent_child": parent_child_retrieve,
    "raptor": raptor_retrieve,
}

results = []
for q in benchmark:
    for vname, vfn in variants.items():
        retrieved = vfn(q["query"])
        hits = set(retrieved) & q["relevant_ids"]
        recall = len(hits) / len(q["relevant_ids"]) if q["relevant_ids"] else 0
        # highest tree level among relevant hits
        max_level = max((tree_nodes[h]["level"] for h in hits), default=-1)
        results.append({
            "category": q["category"],
            "query": q["query"],
            "variant": vname,
            "retrieved": retrieved,
            "recall": recall,
            "max_level": max_level,
        })

# ---------------------------------------------------------------------------
# Per-question results
# ---------------------------------------------------------------------------
print(f"{'Category':<10} {'Variant':<14} {'Recall':>7} {'MaxLvl':>7}  Query")
print("-" * 80)
for r in results:
    print(f"{r['category']:<10} {r['variant']:<14} {r['recall']:>7.2f} {r['max_level']:>7}  {r['query'][:40]}")

# ---------------------------------------------------------------------------
# Aggregate
# ---------------------------------------------------------------------------
print("\n=== Aggregate recall by variant ===")
for vname in variants:
    recalls = [r["recall"] for r in results if r["variant"] == vname]
    print(f"  {vname:<14} mean_recall={statistics.mean(recalls):.3f}")

print("\n=== Aggregate recall by category x variant ===")
for cat in ["detail", "section", "overview"]:
    for vname in variants:
        recalls = [r["recall"] for r in results if r["variant"] == vname and r["category"] == cat]
        if recalls:
            print(f"  {cat:<10} {vname:<14} mean_recall={statistics.mean(recalls):.3f}")
```

## 6 - Interpretation

| Observation | Explanation |
|-------------|-------------|
| **Flat** retrieval scores well on *detail* questions | Leaf chunks directly contain the answer tokens. |
| **Flat** struggles on *overview* questions | It can only return individual chunks - no summaries exist in its search space. |
| **Parent-child** improves section-level recall | Expanding to the section summary adds context the leaf alone misses. |
| **RAPTOR** wins on *overview* and ties on *detail* | Because it searches **all** levels simultaneously, the root/section summary can surface for broad queries while leaf chunks still win for specific ones. |

### Key takeaway

RAPTOR's value shows up when your question set spans multiple **granularity levels**.
If every query is a narrow fact lookup, flat retrieval is fine.  But the moment users
ask *"what is this about?"* or *"summarise the funding history"*, a tree index gives
the retriever something appropriate to return.

### Production notes

- Replace `summarise()` with an LLM call (GPT-4o-mini, Claude Haiku, etc.) for
  real abstractive summaries.
- Use clustering (k-means on embeddings) instead of pre-defined sections to
  discover natural groupings.
- Store the tree in your vector DB with a `level` metadata field so you can filter
  by granularity at query time.
- Consider **collapsed tree retrieval**: search all nodes together (like we did)
  versus **tree traversal**: start at the root and descend.  The RAPTOR paper
  found collapsed search works better in most benchmarks.

### Next steps

- Try adding a *level-3* summary if you have a larger corpus.
- Replace TF-IDF with a real embedding model and re-run.
- Move on to `10_graphrag_visual_rag.ipynb` for entity-based retrieval,
  or revisit `08_rag_technique_selection.md` to choose your next upgrade.
