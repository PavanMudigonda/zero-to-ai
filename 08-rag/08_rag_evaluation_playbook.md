# RAG Evaluation Playbook

This guide is the practical companion to `07_evaluation.ipynb`.

Use it when you need to answer questions like these:

- Is my retriever actually improving?
- Did HyDE help, or just add latency?
- Did reranking improve answer quality or only move chunks around?
- Is GraphRAG worth it for this corpus?
- Am I measuring answer quality, retrieval quality, or both?

The core rule is simple:

**Do not keep an advanced RAG technique unless it beats your simpler baseline on a benchmark that reflects your real task.**

---

## 1. Evaluation Ladder

Measure RAG in this order:

1. **Chunk quality**
2. **Retrieval quality**
3. **Context quality**
4. **Answer quality**
5. **Latency and cost**
6. **Failure behavior**

If you skip the early layers, later metrics become hard to interpret.

Example:

- If answers are bad, that might be a generation problem.
- But it might also be because retrieval missed the right chunk.
- Or because the right chunk was retrieved and then buried in noisy context.

That is why evaluation has to separate the stages.

---

## 2. What to Measure

### Retrieval metrics

Use these when judging the retriever itself:

- **Precision@K**: how many of the top-k results are relevant
- **Recall@K**: whether the needed evidence appears in the top-k set
- **MRR**: how early the first relevant result appears
- **NDCG**: whether the ranking order is useful, not just the set membership

Use retrieval metrics when comparing:

- embedding models
- chunking strategies
- hybrid vs dense retrieval
- query rewriting vs HyDE
- reranking vs no reranking

### Context metrics

Use these when judging what the generator actually receives:

- **Context precision**: how much of the supplied context is relevant
- **Context recall**: whether the supplied context covers what is needed to answer
- **Compression quality**: whether filtering removes noise without dropping key evidence

These matter a lot when using:

- contextual compression
- relevant segment extraction
- parent-child retrieval
- RAPTOR-style summary trees

### Answer metrics

Use these when judging final output quality:

- **Faithfulness / groundedness**: answer is supported by retrieved evidence
- **Answer relevancy**: answer addresses the user question
- **Correctness**: answer matches expected facts or labels
- **Citation quality**: citations point to the supporting evidence

### Operational metrics

Use these when deciding whether an upgrade is worth shipping:

- latency per query
- token usage
- model cost per query
- retriever cost
- cache hit rate
- failure / abstention rate

---

## 3. The Baselines You Should Always Have

Before evaluating advanced RAG, define at least these baselines:

1. **Baseline A:** dense retrieval only
2. **Baseline B:** dense + hybrid retrieval
3. **Baseline C:** dense/hybrid + reranking

Only after that should you compare:

- HyDE
- contextual compression
- CRAG or Self-RAG
- RAPTOR
- GraphRAG

If you do not have these baselines, you cannot tell whether the advanced method is solving a real problem or compensating for a weak base system.

---

## 4. Recommended Benchmark Design

### Build a question set with categories

Do not rely on one generic question list. Split your benchmark into categories:

| Category | What it tests |
|---|---|
| Direct lookup | simple factual retrieval |
| Vague queries | need for query rewriting or HyDE |
| Noisy corpus | need for reranking or compression |
| Multi-hop / cross-section | need for hierarchical retrieval or GraphRAG |
| Unsupported questions | abstention and hallucination resistance |
| Conversational follow-ups | context carry-over and rewrite quality |

Aim for at least:

- 15 to 20 questions for a quick benchmark
- 50+ questions for a meaningful chapter project
- 100+ questions for serious production comparison

### Label what “good” looks like

For each question, record:

- expected answer or answer rubric
- relevant source chunks or source documents
- whether abstention is the correct behavior
- whether multi-hop retrieval is required

This turns evaluation from vague impression into an actual experiment.

---

## 5. Failure Analysis Taxonomy

When a RAG answer is bad, classify the failure before changing the architecture.

### Failure Type 1: Retrieval miss

The needed evidence was not retrieved.

Likely fixes:

- better chunking
- better embeddings
- hybrid retrieval
- query rewriting or HyDE

### Failure Type 2: Ranking failure

The right evidence was in the candidate pool but too low in the ranking.

Likely fixes:

- reranking
- reciprocal rank fusion
- metadata filters

### Failure Type 3: Context assembly failure

The right evidence was retrieved but not passed cleanly to the generator.

Likely fixes:

- contextual compression
- segment extraction
- parent-child retrieval

### Failure Type 4: Generation failure

The context was good, but the answer was still weak or hallucinated.

Likely fixes:

- stronger prompting
- answer verification
- abstention policy
- CRAG / Self-RAG style control loops

### Failure Type 5: Architecture mismatch

The problem requires structure beyond flat chunk retrieval.

Likely fixes:

- hierarchical retrieval
- RAPTOR
- GraphRAG
- multimodal retrieval

---

## 6. What to Compare for Each Advanced Technique

### HyDE

Compare:

- baseline query vs rewritten query vs HyDE
- recall@k
- MRR
- latency and token cost

Success condition:

- higher retrieval quality on ambiguous questions without unacceptable cost increase

### Reranking

Compare:

- hybrid retrieval alone vs hybrid + reranker
- precision@k
- answer faithfulness
- latency

Success condition:

- better top-k quality or answer faithfulness with tolerable latency increase

### Contextual compression

Compare:

- raw retrieved context vs compressed context
- context precision
- faithfulness
- token usage

Success condition:

- same or better answer quality with less noise and lower context cost

### CRAG / Self-RAG

Compare:

- answer quality on weak-evidence questions
- abstention quality
- hallucination rate
- retry overhead

Success condition:

- fewer unsupported answers and better recovery from low-quality retrieval

### RAPTOR / GraphRAG

Compare:

- performance on multi-hop or long-document tasks only
- recall on cross-section questions
- answer correctness
- pipeline complexity and maintenance cost

Success condition:

- consistent gains on structure-heavy questions, not just isolated wins

---

## 7. Minimal Ablation Template

Use a table like this for your chapter project:

| Variant | Retrieval | Rerank | Compression | Reliability Loop | Precision@5 | MRR | Faithfulness | Latency |
|---|---|---|---|---|---:|---:|---:|---:|
| Baseline | Dense | No | No | No |  |  |  |  |
| Variant 1 | Hybrid | No | No | No |  |  |  |  |
| Variant 2 | Hybrid | Yes | No | No |  |  |  |  |
| Variant 3 | Hybrid | Yes | Yes | No |  |  |  |  |
| Variant 4 | Hybrid | Yes | Yes | CRAG-style |  |  |  |  |

This is the kind of evidence that makes a technique decision defensible.

---

## 8. Evaluation Tools to Know

### In your current Phase 8 material

- `07_evaluation.ipynb` introduces core RAG evaluation thinking and `ragas`

### In the cloned `RAG_Techniques` repository

- `evaluation/evaluation_deep_eval.ipynb`
  Use when you want broader LLM-judge style evaluation for correctness, faithfulness, and contextual relevancy.

- `evaluation/evaluation_grouse.ipynb`
  Use when you want a more structured contextual grounding evaluation framework and judge-oriented meta-evaluation.

### Good default evaluation stack

For most learners, the practical default is:

1. retrieval metrics with a labeled test set
2. `ragas` for faithfulness and answer relevance
3. manual failure review on the hardest 20 questions

Only add more judge frameworks if you need them.

---

## 9. Shipping Criteria

Do not ship an “improved” RAG system unless it clears all of these:

1. Beats the baseline on the question category it was meant to improve.
2. Does not regress badly on easier question categories.
3. Keeps latency and cost within an acceptable range.
4. Improves failure behavior, not just average-case scores.

That last point matters. A production RAG system is judged as much by how it fails as by how it answers.

---

## 10. Recommended Phase 8 Workflow

Use this order in your project work:

1. build the baseline
2. create the benchmark set
3. measure retrieval quality
4. measure answer quality
5. add one advanced technique
6. rerun the benchmark
7. study failure cases
8. either keep the change or revert it

That workflow is much better than stacking techniques without measurement.