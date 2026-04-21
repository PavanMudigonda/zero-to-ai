# RAG Technique Selection Guide

Use this guide after you understand baseline RAG. The goal is to answer one practical question:

**What should you add next to improve your system, and what problem is it actually solving?**

This guide is informed by the patterns collected in the `RAG_Techniques` repository, but organized for curriculum use rather than as a long catalog.

---

## 1. Start with Failure Mode, Not Hype

Most RAG teams choose the wrong upgrade because they choose by trend instead of failure mode.

Use this sequence:

1. Identify how the system fails.
2. Decide whether the failure is query-side, document-side, retrieval-side, or control-loop related.
3. Add the smallest technique that directly fixes that failure.
4. Benchmark against the simpler baseline before keeping it.

---

## 2. Technique Selection Matrix

| If your system fails like this | Start with these techniques | Why they help | Cost / complexity | Hands-on notebooks |
|---|---|---|---|---|
| User questions are vague, short, or ambiguous | Query rewriting, multi-query retrieval, HyDE | Better query-document alignment | Low to medium | `08_hyde_reranking.ipynb` (self-contained), `05_advanced_retrieval.ipynb` |
| Relevant facts are split across document sections | Parent-child retrieval, hierarchical retrieval, RAPTOR | Preserves both local detail and broader context | Medium to high | `12_parent_child_retrieval.ipynb`, `13_raptor_retrieval.ipynb` (both self-contained) |
| Top-k results are close but noisy | Hybrid retrieval, reranking, contextual compression | Improves ranking quality before generation | Medium | `08_hyde_reranking.ipynb` (self-contained), `09_advanced_retrieval.ipynb` (API-dependent) |
| Retrieved chunks miss structure or context | Semantic chunking, proposition chunking, contextual headers, window expansion | Improves chunk quality and context boundaries | Medium | `02_document_processing.ipynb` |
| System answers with weak evidence | Reliable RAG, CRAG, Self-RAG, retrieval feedback loops | Adds correction and abstention behavior | Medium to high | `11_corrective_rag.ipynb` (self-contained), `07_evaluation.ipynb` |
| Questions require entity relationships or multi-hop reasoning | GraphRAG, hierarchical indices, RAPTOR | Better reasoning over relationships and summaries | High | `13_raptor_retrieval.ipynb` (self-contained), `10_graphrag_visual_rag.ipynb` |
| Inputs contain charts, screenshots, or scanned PDFs | Visual RAG, multimodal retrieval, caption-based retrieval | Makes non-text evidence retrievable | High | `10_graphrag_visual_rag.ipynb` |
| You need tool use and dynamic routing | Agentic RAG, retrieval orchestration | Lets the system choose retrieval tools dynamically | High | Phase 15 later builds on this |

---

## 3. Best Next Upgrade by System Stage

### Stage A: Your first baseline works

Add these first:

1. Better chunking
2. Hybrid retrieval
3. Reranking

Reason: these usually produce the biggest quality gain per unit of complexity.

### Stage B: Retrieval quality is okay, but query understanding is weak

Add these next:

1. Query rewriting
2. Multi-query retrieval
3. HyDE

Reason: these help when user intent is not expressed in the same language as your indexed content.

### Stage C: You have partially good retrieval, but answers are still unreliable

Add these next:

1. Contextual compression
2. Evidence grading
3. CRAG-style retry or abstention

Reason: the problem is often not finding documents, but passing too much or too little evidence into generation.

### Stage D: Your corpus is large, structured, or multi-hop

Add these next:

1. Parent-child retrieval
2. RAPTOR or hierarchy-based retrieval
3. GraphRAG

Reason: flat chunk retrieval does not capture long-range document structure well.

---

## 4. Recommended Study Order

If you want a disciplined path through the advanced material, use this order:

1. `02_document_processing.ipynb` - chunking strategies
2. `07_evaluation.ipynb` - metrics and benchmarking (run this early so you can measure everything that follows)
3. `08_hyde_reranking.ipynb` - HyDE query expansion + reranking **(self-contained, no API keys)**
4. `11_corrective_rag.ipynb` - CRAG-style retrieval grading, retry, abstention **(self-contained)**
5. `12_parent_child_retrieval.ipynb` - chunk-to-parent expansion **(self-contained)**
6. `13_raptor_retrieval.ipynb` - hierarchical summary-tree retrieval **(self-contained)**
7. `09_advanced_retrieval.ipynb` - ColBERT, Cohere reranking, full pipeline (requires OpenAI + Cohere API keys)
8. `10_graphrag_visual_rag.ipynb` - entity-relationship and multimodal retrieval
9. `challenges.md` / `assignment.md`

Notebooks 3-6 above are **self-contained** (TF-IDF + toy data, no API keys needed) so you can
run them immediately. Notebook 7 (`09_advanced_retrieval.ipynb`) requires API keys but covers
production-grade libraries (LangChain, ChromaDB, Cohere) for the same concepts.

This ordering mirrors how strong systems are actually built:

- first improve chunks,
- then set up evaluation,
- then improve query understanding and ranking,
- then add reliability controls,
- then introduce hierarchical structure,
- then expand into graph and multimodal patterns.

---

## 5. Technique Tradeoffs That Matter

### HyDE

Use when:
- queries are abstract
- semantic similarity is weak
- users ask concept-heavy questions

Avoid when:
- latency and query-time LLM cost are strict constraints
- your baseline query rewriting already works well

### Reranking

Use when:
- top-k contains near misses
- you can afford a second-stage ranker
- precision matters more than raw recall

Avoid when:
- latency budgets are extremely tight
- your corpus is small and clean

### Contextual Compression

Use when:
- retrieved chunks are too long or noisy
- model context windows are being wasted
- answers degrade because too much irrelevant text is included

Avoid when:
- your base chunks are already short and precise

### RAPTOR / Hierarchical Retrieval

Use when:
- documents are long and structured
- queries require section-level synthesis
- flat chunk retrieval misses broad context

Avoid when:
- corpus is small and shallow
- the overhead is not justified by question complexity

### CRAG / Self-RAG

Use when:
- you need reliability and abstention
- hallucinations are costly
- retrieval quality varies heavily across questions

Avoid when:
- the system is still missing basic evaluation and retrieval baselines

### GraphRAG

Use when:
- answers depend on entities and relationships
- multi-hop reasoning is common
- your domain already has graph-like structure

Avoid when:
- you have not yet validated that simpler retrieval methods fail

---

## 6. Mapping to the Cloned Repository

Use the cloned `RAG_Techniques` repo as an idea bank, not as a checklist to blindly implement.

Good references to study:

- Query-side: `query_transformations.ipynb`, `HyDe_Hypothetical_Document_Embedding.ipynb`
- Chunking/context: `semantic_chunking.ipynb`, `proposition_chunking.ipynb`, `contextual_compression.ipynb`
- Retrieval quality: `fusion_retrieval.ipynb`, `reranking.ipynb`, `relevant_segment_extraction.ipynb`
- Structure: `hierarchical_indices.ipynb`, `raptor.ipynb`, `graph_rag.ipynb`, `Microsoft_GraphRag.ipynb`
- Reliability: `reliable_rag.ipynb`, `crag.ipynb`, `self_rag.ipynb`, `retrieval_with_feedback_loop.ipynb`
- Multimodal: `multi_model_rag_with_captioning.ipynb`, `multi_model_rag_with_colpali.ipynb`

Public repo link:

- [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)

---

## 7. Practical Build Recipes

### Recipe 1: Best general-purpose upgrade path

1. Improve chunking
2. Add hybrid retrieval
3. Add reranking
4. Add evaluation and failure analysis

This is the default recommendation for most production RAG systems.

### Recipe 2: Best path for enterprise search

1. Metadata-aware chunking
2. Hybrid retrieval
3. Reranking
4. Contextual compression
5. Abstention and evidence checks

### Recipe 3: Best path for research or long reports

1. Semantic or proposition chunking
2. Parent-child retrieval
3. RAPTOR or hierarchy-based retrieval
4. GraphRAG if multi-hop reasoning still fails

### Recipe 4: Best path for support bots and copilots

1. Query rewriting
2. Multi-query retrieval
3. Reranking
4. Conversational context handling
5. Reliability loop for weak retrieval cases

---

## 8. What Not to Do

- Do not jump to GraphRAG before baseline retrieval is measured.
- Do not add agentic orchestration before reranking and evaluation are working.
- Do not assume a more advanced architecture is better for a small or clean corpus.
- Do not evaluate only answer fluency; evaluate retrieval and faithfulness separately.

---

## 9. Suggested Capstone Extensions

If you want to extend the Phase 8 capstone, pick one of these paths:

1. **Retrieval quality path:** hybrid search + reranking + compression → start with `08_hyde_reranking.ipynb`.
2. **Reliability path:** evidence grading + CRAG-style retry + abstention → start with `11_corrective_rag.ipynb`.
3. **Structured reasoning path:** parent-child retrieval → RAPTOR → start with `12_parent_child_retrieval.ipynb` then `13_raptor_retrieval.ipynb`.
4. **Advanced architecture path:** GraphRAG or multimodal RAG → `10_graphrag_visual_rag.ipynb`.

Pick one path and measure it properly. That is better than adding five advanced techniques without evidence.