# Master Study Guide

Goal: Become a competitive AI/ML engineer in 6-12 months.

## How to Use This Guide

1. Read top-to-bottom once for the full picture
2. Use [CAREER_ROADMAP.md](CAREER_ROADMAP.md) to target job roles
3. Follow [checklist.md](checklist.md) to track progress
4. Use [REFERENCES.md](REFERENCES.md) for courses and papers per phase
5. Use [INTERVIEW_PREP.md](INTERVIEW_PREP.md) for practice
6. Build portfolio projects progressively — they matter more than certifications

---

## Learning Tracks

### Track A: AI Engineer (4-6 months)
Focus on LLMs, RAG, agents, deployment. Skip deep math.

```
Month 1:  Phase 0 (Foundations) → Phase 4 (Embeddings) → Phase 5 (NN basics only)
Month 2:  Phase 6 (Vector DBs) → Phase 7 (RAG) → Phase 18 (Low-code demos)
Month 3:  Phase 10 (Prompt Eng) → Phase 13 (Local LLMs) → Phase 14 (Agents)
Month 4:  Phase 8 (MLOps) → Phase 11 (Fine-tuning) → Portfolio projects
Month 5:  Interview prep → Applications
```

### Track B: ML Engineer (8-10 months)
Full foundation plus advanced topics.

```
Month 1-2: Phases 0-2 (Python, Data Science, Math)
Month 3:   Phases 3-5 (Tokenization, Embeddings, Neural Networks)
Month 4:   Phases 6-7 (Vector DBs, RAG) + Phase 18 (demos)
Month 5:   Phases 8-9 (MLOps, Specializations) + Phase 16 (Eval)
Month 6-7: Phases 10-14 (Prompt Eng, Fine-tuning, Agents, Local LLMs)
Month 8:   Phase 19 (Safety) + Portfolio + Phase 15 (Streaming)
Month 9:   Interview prep + Applications
```

### Track C: Data Scientist (6-8 months)
Statistics, experimentation, classical ML.

```
Month 1-2: Phases 0-2 (Python, Statistics, Math)
Month 3-4: Phase 27 (Causal Inference) + Phase 26 (Time Series)
Month 5:   Phase 7 (RAG) + Phase 10 (Prompt Eng)
Month 6:   Phase 16 (Eval) + Portfolio + Interview prep
```

---

## Phase-by-Phase Notes

### Phase 0: Foundations (1 week)
Supervised vs unsupervised vs RL. Train/val/test splits. Overfitting. Loss functions. ML vs deep learning vs LLMs.

Start: [23-glossary/GLOSSARY.md](../23-glossary/GLOSSARY.md)

### Phase 1: Python & Data Science (3-4 weeks)
NumPy, pandas, scikit-learn. Focus on: LinearRegression, LogisticRegression, RandomForest, GradientBoosting, KMeans, PCA.

Key notebooks: [02-data-science/](../02-data-science/)

### Phase 2: Mathematics for ML (2-3 weeks)
Linear algebra (vectors, matrices, dot products), gradient descent, probability. You need intuition, not proofs.

Key notebooks: [03-maths/foundational/](../03-maths/foundational/)

### Phase 3: Tokenization (1 week)
Tokens != words. BPE tokenization. Why it matters for cost and context. TikToken and HuggingFace tokenizers.

Key notebooks: [04-token/](../04-token/)

### Phase 4: Embeddings (1 week)
Text to vectors. Cosine similarity. Word vs sentence embeddings. Choosing between local models and APIs (Gemini Embedding, Voyage, OpenAI, Sentence Transformers).

Key notebooks: [05-embeddings/](../05-embeddings/)

### Phase 5: Neural Networks (2-3 weeks)
Neurons, layers, activations, backprop. The Transformer architecture. Self-attention. Multi-head attention.

Key notebooks: [06-neural-networks/](../06-neural-networks/)

### Phase 6: Vector Databases (1 week)
ANN search, HNSW. ChromaDB for prototypes, Qdrant for production, pgvector if you already use Postgres.

Key notebooks: [07-vector-databases/](../07-vector-databases/)

### Phase 7: RAG Systems (2 weeks)
The RAG pipeline: chunk → embed → store → retrieve → rerank → generate. Chunking strategies. Hybrid search. RAGAS evaluation.

> RAG is the most in-demand AI skill in enterprise right now. The basic version is easy — making it work *well* is the challenge.

Key notebooks: [08-rag/](../08-rag/)

### Phase 8: MLOps (2 weeks)
MLflow, FastAPI, Docker, GitHub Actions, monitoring. 80% of ML projects fail because of bad ops, not bad models.

Key notebooks: [09-mlops/](../09-mlops/)

### Phase 9: Specializations (2-3 weeks, pick one)
- **AI Agents**: ReAct, tool calling, LangGraph, MCP — [10-specializations/ai-agents/](../10-specializations/ai-agents/)
- **Computer Vision**: CNNs, YOLO, CLIP — [10-specializations/computer-vision/](../10-specializations/computer-vision/)
- **NLP**: BERT fine-tuning, NER, summarization — [10-specializations/nlp/](../10-specializations/nlp/)

### Phase 10: Prompt Engineering (1 week)
Zero/few-shot, Chain-of-Thought, ReAct, structured outputs, DSPy. Treat prompting like software engineering: version control, testing, iteration.

Key notebooks: [11-prompt-engineering/](../11-prompt-engineering/)

### Phase 11: LLM Fine-tuning (2-3 weeks)
Decision: prompt → RAG → fine-tune. LoRA, QLoRA, SFT, DPO. Use Unsloth for 2-5x faster training.

Key notebooks: [12-llm-finetuning/](../12-llm-finetuning/)

### Phase 12: Multimodal AI (1 week)
CLIP, vision-language models (GPT-5.4, Claude Sonnet 4.6, Qwen2.5-VL), Stable Diffusion, multimodal RAG.

Key notebooks: [13-multimodal/](../13-multimodal/)

### Phase 13: Local LLMs (1 week)
Ollama (Qwen 3, Llama 4, DeepSeek R1), llama.cpp, vLLM. Quantization formats. TurboQuant for KV cache compression (ICLR 2026). OpenAI-compatible local APIs.

Key notebooks: [14-local-llms/](../14-local-llms/)

### Phase 14: AI Agents (2 weeks)
ReAct loop, tool calling, agent memory, multi-agent systems, MCP, LangGraph.

Key notebooks: [15-ai-agents/](../15-ai-agents/)

### Supplementary Phases
- **Model Evaluation** — [16-model-evaluation/](../16-model-evaluation/) — do after Phase 7
- **Debugging** — [17-debugging-troubleshooting/](../17-debugging-troubleshooting/) — alongside portfolio projects
- **Low-Code Tools** — [18-low-code-ai-tools/](../18-low-code-ai-tools/) — Gradio/Streamlit for demos
- **AI Safety** — [19-ai-safety-redteaming/](../19-ai-safety-redteaming/) — before deploying anything publicly
- **Streaming** — [20-real-time-streaming/](../20-real-time-streaming/) — for production UX

---

## Portfolio Projects

### Required (3 projects)

**Project 1: RAG Document Assistant**
LangChain/LlamaIndex + ChromaDB + Ollama/OpenAI + FastAPI + Streamlit. Add hybrid search, reranking, RAGAS eval.

**Project 2: Fine-tuned Domain Expert**
Pick a domain. Fine-tune Qwen 3 4B or Phi-4 Mini with QLoRA. Evaluate before/after. Deploy with Ollama or vLLM.

**Project 3: End-to-End MLOps Pipeline**
Train a model. Track with MLflow. Serve with FastAPI + Docker. CI/CD with GitHub Actions.

### Differentiators

**Project 4: AI Agent with Real Tools** — 3+ tools, memory, documented failure modes

**Project 5: Evaluation Framework** — automated regression testing for model quality

---

## Key Papers to Know

| Paper | Year | Contribution |
|-------|------|-------------|
| Attention Is All You Need | 2017 | Transformer architecture |
| BERT | 2018 | Bidirectional pre-training |
| GPT-3 | 2020 | Scale + few-shot prompting |
| RAG (Lewis et al.) | 2020 | Retrieval-augmented generation |
| LoRA | 2021 | Parameter-efficient fine-tuning |
| InstructGPT (RLHF) | 2022 | Alignment via human feedback |
| Chain-of-Thought | 2022 | Reasoning via step-by-step prompts |
| DPO | 2023 | Alignment without RL |

---

## Weekly Schedule Template

**Weekdays (3 hrs/day)**: 1 hr theory → 1 hr notebook → 1 hr project work

**Weekends (4-5 hrs/day)**: 2-3 hrs deep dive → 1-2 hrs portfolio → 30 min review

---

## Progress Checkpoints

- **Week 4**: Can you train a scikit-learn classifier, clean data, evaluate properly?
- **Week 8**: Can you explain transformers? Build a simple neural network in PyTorch?
- **Week 12**: Can you build a working RAG system? Evaluate its quality?
- **Week 16**: Can you fine-tune a small LLM? Deploy it with FastAPI?
- **Week 20**: Can you build a working AI agent with tools and memory?
- **Week 24**: 3+ portfolio projects on GitHub with READMEs?

---

## Related Files

- [CAREER_ROADMAP.md](CAREER_ROADMAP.md) — job targeting, resume, networking
- [INTERVIEW_PREP.md](INTERVIEW_PREP.md) — questions, coding, system design
- [REFERENCES.md](REFERENCES.md) — videos, courses, repos, papers
- [checklist.md](checklist.md) — track completion

*Last Updated: April 2026*
