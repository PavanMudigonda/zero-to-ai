# AI / ML Visual Roadmap

> Interactive Mermaid diagrams covering the full AI & ML landscape — from fundamentals to production systems. Every box maps to a phase in the **Zero to AI** curriculum.
>
> **Split into 4 pages for faster loading.** Each page has ~4-6 diagrams instead of 21.

---

## Pages

| Page | Diagrams | Topics |
|------|----------|--------|
| [**Part 1: Overview**](roadmaps/01_overview.md) | 1–4 | Big Picture, ML Paradigms, Deep Learning Architecture Tree, NLP & LLM Pipeline |
| [**Part 2: Core Systems**](roadmaps/02_core_systems.md) | 5–10 | LLM Landscape (2026), Embeddings & Vector Search, RAG, AI Agents, Multi-Agent Systems, MLOps |
| [**Part 3: Advanced Topics**](roadmaps/03_advanced_topics.md) | 11–14 | Fine-tuning Decision Tree, Multimodal AI, Inference Optimization, AI Safety & Guardrails |
| [**Part 4: End-to-End Flows**](roadmaps/04_end_to_end_flows.md) | 15–21 | Project Flow, RAG Pipeline, Document Ingestion, LLM Training, Agentic RAG, Idea→Production, Multimodal |

---

## All Diagrams

**Overview** — [Part 1](roadmaps/01_overview.md)

1. [The Big Picture](roadmaps/01_overview.md#1-the-big-picture)
2. [Machine Learning Paradigms](roadmaps/01_overview.md#2-machine-learning-paradigms)
3. [Deep Learning Architecture Tree](roadmaps/01_overview.md#3-deep-learning-architecture-tree)
4. [NLP & LLM Pipeline](roadmaps/01_overview.md#4-nlp-llm-pipeline)

**Core Systems** — [Part 2](roadmaps/02_core_systems.md)

5. [The LLM Model Landscape (2026)](roadmaps/02_core_systems.md#5-the-llm-model-landscape-2026)
6. [Embeddings & Vector Search](roadmaps/02_core_systems.md#6-embeddings-vector-search)
7. [RAG (Retrieval-Augmented Generation)](roadmaps/02_core_systems.md#7-rag-retrieval-augmented-generation)
8. [AI Agents Architecture](roadmaps/02_core_systems.md#8-ai-agents-architecture)
9. [Multi-Agent Systems](roadmaps/02_core_systems.md#9-multi-agent-systems)
10. [MLOps Lifecycle](roadmaps/02_core_systems.md#10-mlops-lifecycle)

**Advanced Topics** — [Part 3](roadmaps/03_advanced_topics.md)

11. [Fine-tuning Decision Tree](roadmaps/03_advanced_topics.md#11-fine-tuning-decision-tree)
12. [Multimodal AI](roadmaps/03_advanced_topics.md#12-multimodal-ai)
13. [Inference Optimization](roadmaps/03_advanced_topics.md#13-inference-optimization)
14. [AI Safety & Guardrails](roadmaps/03_advanced_topics.md#14-ai-safety-guardrails)

**End-to-End Flows** — [Part 4](roadmaps/04_end_to_end_flows.md)

15. [End-to-End Project Flow](roadmaps/04_end_to_end_flows.md#15-end-to-end-project-flow)
16. [Docs + Query → Chunks → Embeddings → RAG → Answer](roadmaps/04_end_to_end_flows.md#16-docs-query-chunks-embeddings-rag-answer)
17. [Document Ingestion Pipeline](roadmaps/04_end_to_end_flows.md#17-document-ingestion-pipeline)
18. [Training an LLM (Pre-train → Fine-tune → Deploy)](roadmaps/04_end_to_end_flows.md#18-training-an-llm-pre-train-fine-tune-deploy)
19. [Agentic RAG (Question → Tools → Search → Synthesize)](roadmaps/04_end_to_end_flows.md#19-agentic-rag-question-tools-search-synthesize)
20. [From Idea to Production AI App](roadmaps/04_end_to_end_flows.md#20-from-idea-to-production-ai-app)
21. [Multimodal — Image + Text → Understanding → Generation](roadmaps/04_end_to_end_flows.md#21-multimodal-image-text-understanding-generation)

---

## Suggested Reading Paths

**If you are new to AI/ML**

Start with [1. The Big Picture](roadmaps/01_overview.md#1-the-big-picture), then read [2. Machine Learning Paradigms](roadmaps/01_overview.md#2-machine-learning-paradigms), [3. Deep Learning Architecture Tree](roadmaps/01_overview.md#3-deep-learning-architecture-tree), and [15. End-to-End Project Flow](roadmaps/04_end_to_end_flows.md#15-end-to-end-project-flow).

**If you want to build LLM applications**

Start with [4. NLP & LLM Pipeline](roadmaps/01_overview.md#4-nlp-llm-pipeline), then move to [6. Embeddings & Vector Search](roadmaps/02_core_systems.md#6-embeddings-vector-search), [7. RAG](roadmaps/02_core_systems.md#7-rag-retrieval-augmented-generation), [8. AI Agents](roadmaps/02_core_systems.md#8-ai-agents-architecture), and [20. From Idea to Production](roadmaps/04_end_to_end_flows.md#20-from-idea-to-production-ai-app).

**If you care about production systems**

Start with [10. MLOps Lifecycle](roadmaps/02_core_systems.md#10-mlops-lifecycle), then read [13. Inference Optimization](roadmaps/03_advanced_topics.md#13-inference-optimization), [14. AI Safety](roadmaps/03_advanced_topics.md#14-ai-safety-guardrails), [19. Agentic RAG](roadmaps/04_end_to_end_flows.md#19-agentic-rag-question-tools-search-synthesize), and [20. From Idea to Production](roadmaps/04_end_to_end_flows.md#20-from-idea-to-production-ai-app).

**If you want model internals**

Start with [3. Deep Learning Architecture Tree](roadmaps/01_overview.md#3-deep-learning-architecture-tree), then read [4. NLP & LLM Pipeline](roadmaps/01_overview.md#4-nlp-llm-pipeline), [11. Fine-tuning Decision Tree](roadmaps/03_advanced_topics.md#11-fine-tuning-decision-tree), [12. Multimodal AI](roadmaps/03_advanced_topics.md#12-multimodal-ai), and [18. Training an LLM](roadmaps/04_end_to_end_flows.md#18-training-an-llm-pre-train-fine-tune-deploy).

---

## How to Read These Diagrams

| Symbol | Meaning |
|--------|---------|
| `[Box]` | Concept, tool, or technique |
| `-->` | Leads to / depends on |
| `-.->` | Weak or optional dependency |
| `{Diamond}` | Decision point |
| `subgraph` | Grouping of related concepts |

Each box roughly corresponds to a topic covered in one of the **phases (00–31)** of the Zero to AI curriculum. Follow the arrows to find a natural learning path.

---

*Generated for the Zero to AI curriculum — April 2026*
