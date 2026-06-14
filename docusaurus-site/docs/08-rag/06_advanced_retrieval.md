---
title: "6. Advanced Retrieval"
sidebar_label: "6. Advanced Retrieval"
sidebar_position: 7
format: "md"
---
# Advanced Retrieval

## Hybrid Search

Combine vector search with keyword search!

### Why Hybrid?
- Vector: Semantic similarity
- Keyword: Exact matches
- Together: Best of both worlds

> **Navigation note:** This notebook is a **conceptual overview** of hybrid search and reranking (pseudo-code only).
> For **runnable, self-contained** implementations of these techniques see:
>
> | Technique | Self-contained notebook | API-dependent notebook |
> |-----------|------------------------|------------------------|
> | HyDE + reranking | `08_hyde_reranking.ipynb` | `09_advanced_retrieval.ipynb` |
> | CRAG / retrieval grading | `11_corrective_rag.ipynb` | - |
> | Parent-child retrieval | `12_parent_child_retrieval.ipynb` | `09_advanced_retrieval.ipynb` |
> | RAPTOR hierarchical retrieval | `13_raptor_retrieval.ipynb` | `09_advanced_retrieval.ipynb` |
>
> The self-contained notebooks use TF-IDF + toy data and require **no API keys**.

```python
import numpy as np
import pandas as pd
from typing import List, Dict, Tuple
import json
import os
from pathlib import Path
```

## Re-ranking

### Improving Retrieval Quality with a Second Pass

Initial vector search is fast but can be imprecise: it relies on a single dot product between compressed embeddings. **Re-ranking** adds a second stage where a **cross-encoder** model scores each (query, document) pair independently, considering the full interaction between query and document tokens. Cross-encoders are far more accurate than bi-encoders but too slow to run over the entire corpus, so the standard pattern is: first retrieve a broad candidate set (e.g., top 20) with fast vector search, then re-rank that set with the cross-encoder and return the refined top-$k$. This two-stage approach gives you the speed of vector search with the precision of cross-attention.

```python
# Pseudo-code for re-ranking
def rerank(query, initial_results):
    # Use cross-encoder for precise scoring
    scores = cross_encoder.predict([(query, doc) for doc in initial_results])
    # Sort by new scores
    reranked = sorted(zip(initial_results, scores), key=lambda x: x[1], reverse=True)
    return reranked
```
