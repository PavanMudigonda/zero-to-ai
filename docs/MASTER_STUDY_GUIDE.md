# Master Study Guide

> Phase-by-phase learning notes, study schedule, and track recommendations.
> Read this first, then use [checklist.md](checklist.md) to track your progress.

This is the canonical learner navigation document for the repository.

---

## How to Use This Guide

1. **Pick your track** below based on your career goal
2. **Follow the phase order** - each phase builds on the previous
3. **Open `00_START_HERE.ipynb`** in each phase directory for guided entry
4. **Track progress** in [checklist.md](checklist.md)
5. **Use [REFERENCES.md](REFERENCES.md)** for supplementary videos, papers, and courses
6. **Treat later WIP phases honestly** - some advanced modules are still being expanded

---

## Choose Your Learning Track

Not every phase is equally important for every role. Pick the track that matches your goal, then follow the priority order.

<div id="track-ai-engineer"></div>

### Track A: AI Engineer (LLM / Agent / RAG Focus)

**Target roles:** AI Engineer, LLM Engineer, GenAI Engineer, AI Platform Engineer

| Priority | Phase | Directory | Hours | Why |
|----------|-------|-----------|-------|-----|
| 1 | Python & Data Basics | `01-python/`, `02-data-science/` | 20–40 | Fluency in Python, NumPy, pandas |
| 2 | Tokenization | `04-token/` | 4–6 | How LLMs see text |
| 3 | Embeddings | `05-embeddings/` | 6–8 | Semantic representations |
| 4 | Neural Networks | `06-neural-networks/` | 10–15 | Transformers from scratch |
| 5 | Vector Databases | `07-vector-databases/` | 6–8 | Storage for retrieval systems |
| 6 | RAG | `08-rag/` | 12–18 | Core production pattern |
| 7 | Prompt Engineering | `11-prompt-engineering/` | 6–8 | Systematic prompting |
| 8 | AI Agents | `15-ai-agents/` | 12–15 | Function calling, MCP, multi-agent |
| 9 | Local LLMs | `14-local-llms/` | 6–8 | Ollama, llama.cpp, local serving |
| 10 | LLM Fine-tuning | `12-llm-finetuning/` | 15–23 | LoRA, QLoRA, DPO |
| 11 | Real-Time Streaming | `20-real-time-streaming/` | 6–8 | Production streaming patterns |
| 12 | MLOps | `09-mlops/` | 10–15 | Deployment & monitoring |

**Optional depth:** `19-ai-safety-redteaming/`, `16-model-evaluation/`, `30-inference-optimization/`, `31-ai-powered-dev-tools/`

<div id="track-ml-engineer"></div>

### Track B: ML Engineer (Classical ML + Deep Learning)

**Target roles:** ML Engineer, Applied Scientist, ML Platform Engineer

| Priority | Phase | Directory | Hours | Why |
|----------|-------|-----------|-------|-----|
| 1 | Python & Data Science | `01-python/`, `02-data-science/` | 40–60 | Deep scikit-learn, pandas, EDA |
| 2 | Mathematics | `03-maths/` | 30–50 | Linear algebra, calculus, stats, optimization |
| 3 | Neural Networks | `06-neural-networks/` | 10–15 | Backprop, PyTorch, transformers |
| 4 | MLOps | `09-mlops/` | 10–15 | MLflow, FastAPI, Docker, CI/CD |
| 5 | Model Evaluation | `16-model-evaluation/` | 6–8 | Metrics, fairness, comparison tests |
| 6 | Debugging | `17-debugging-troubleshooting/` | 6–8 | Profiling, data issues, error analysis |
| 7 | LLM Fine-tuning | `12-llm-finetuning/` | 15–23 | Adapt models to your domain |
| 8 | Time Series | `26-time-series-analysis/` | 6–8 | ARIMA, Prophet, LSTM forecasting |
| 9 | Reinforcement Learning | `25-reinforcement-learning/` | 8–10 | MDP, Q-learning, policy gradients |
| 10 | Advanced Deep Learning | `24-advanced-deep-learning/` | 20–30 | GANs, VAEs, diffusion, NeRF |

**Optional depth:** `27-causal-inference/`, `29-ai-hardware-llm-validation/`, `30-inference-optimization/`

<div id="track-data-scientist"></div>

### Track C: Data Scientist (Analysis + ML + Communication)

**Target roles:** Data Scientist, Analytics Engineer, Research Analyst

| Priority | Phase | Directory | Hours | Why |
|----------|-------|-----------|-------|-----|
| 1 | Python & Data Science | `01-python/`, `02-data-science/` | 40–60 | Core daily tools |
| 2 | Mathematics & Statistics | `03-maths/` | 30–50 | Inference, hypothesis testing, regression |
| 3 | Low-Code AI Tools | `18-low-code-ai-tools/` | 6–8 | Gradio, Streamlit for demos |
| 4 | Neural Networks | `06-neural-networks/` | 10–15 | Conceptual understanding |
| 5 | Model Evaluation | `16-model-evaluation/` | 6–8 | Statistical comparison, fairness |
| 6 | Causal Inference | `27-causal-inference/` | 8–10 | Beyond correlation |
| 7 | Time Series | `26-time-series-analysis/` | 6–8 | Forecasting and anomaly detection |
| 8 | RAG | `08-rag/` | 12–18 | Retrieval over documents |
| 9 | Practical Data Science | `28-practical-data-science/` | 20–30 | Interview prep and applied practice |
| 10 | Prompt Engineering | `11-prompt-engineering/` | 6–8 | Using LLMs effectively |

**Optional depth:** `05-embeddings/`, `07-vector-databases/`, `12-llm-finetuning/`

---

## Phase-by-Phase Study Notes

### Phase 0: Course Setup (`00-course-setup/`)
- Read `2026_model_landscape.md` to understand what models exist today
- Run `install_dependencies.sh` to set up your environment
- Bookmark [02_troubleshooting.md](../00-course-setup/02_troubleshooting.md) - you will need it

### Phase 1: Python (`01-python/`)
- If new to Python, complete the [Python Bro Code](https://github.com/PavanMudigonda/python-bro-code) course first
- Use [../01-python/README.md](../01-python/README.md) as your readiness checklist before moving on
- If you already know Python, skip to Phase 2

### Phase 2: Data Science (`02-data-science/`)
- **Start with:** `1-numpy-examples/` → `2-pandas-examples/` → `4-matplotlib/`
- **Then:** `3-data-science-examples/` for real-world scenarios
- **Deep dive:** `5-scikit-learn/` has 278 example notebooks - use as a reference library, not a cover-to-cover read
- The sub-directory structure can feel complex; follow the numbered order within each

### Phase 3: Mathematics (`03-maths/`)
- **Start with:** `foundational/` - 7 notebooks from linear algebra to neural network math
- **Then:** `mml-book/` for textbook-aligned exercises
- **Optional depth:** `islp-book/` (13 notebooks), `cs229-course/`, `advanced/`
- You don't need to complete all 153 notebooks - focus on `foundational/` first

### Phase 4: Tokenization (`04-token/`)
- Start with `00_START_HERE.ipynb`
- Key insight: understand BPE, WordPiece, and SentencePiece before moving to embeddings
- ~4–6 hours

### Phase 5: Embeddings (`05-embeddings/`)
- Start with `00_START_HERE.ipynb`
- Understand that embeddings are the bridge between text and math
- Practice semantic search - this is the foundation of RAG
- ~6–8 hours

### Phase 6: Neural Networks (`06-neural-networks/`)
- Start with `00_START_HERE.ipynb`
- Build a neural network from scratch in NumPy before using PyTorch
- The transformer notebook (05) is the most important - everything after depends on it
- ~10–15 hours

### Phase 7: Vector Databases (`07-vector-databases/`)
- Start with `00_START_HERE.ipynb`
- Try at least two databases (Chroma + one other) to compare
- ~6–8 hours

### Phase 8: RAG (`08-rag/`)
- Start with `00_START_HERE.ipynb`
- This is the most notebook-rich teaching phase (14 notebooks)
- Complete the assignment - building a RAG system is an essential portfolio project
- ~12–18 hours

### Phase 9: MLOps (`09-mlops/`)
- Start with `00_START_HERE.ipynb`
- Focus on MLflow → FastAPI → Docker pipeline first
- Cloud deployment can wait until you have a model worth deploying
- ~10–15 hours

### Phase 10: Specializations (`10-specializations/`)
- Hub phase - pick the path matching your track: Computer Vision, NLP, or AI Agents
- Each sub-path has 6 notebooks
- ~8–12 hours per path

### Phase 11: Prompt Engineering (`11-prompt-engineering/`)
- Start with `00_START_HERE.ipynb`
- Chain-of-thought and ReAct are the most important techniques
- ~6–8 hours

### Phase 12: LLM Fine-tuning (`12-llm-finetuning/`)
- Start with `00_START_HERE.ipynb`
- Follow: `00 → 01 → 02 → 03 → 04 → 06 → 07` for first pass
- Second pass for alignment: `05 → 08 → 11`
- QLoRA on a free Colab T4 is the most practical starting point
- ~15–23 hours

### Phase 13: Multimodal (`13-multimodal/`)
- Start with `00_START_HERE.ipynb`
- Three sub-paths: audio, image-generation, vision-language
- ~8–12 hours

### Phase 14: Local LLMs (`14-local-llms/`)
- Start with `00_START_HERE.ipynb`
- Install Ollama first - it takes 5 minutes and changes everything
- ~6–8 hours

### Phase 15: AI Agents (`15-ai-agents/`)
- Start with `00_START_HERE.ipynb`
- This is the hottest topic in 2026 AI - take your time
- Take the pre-quiz before starting, post-quiz after
- Complete the assignment - building an agent is essential
- ~12–15 hours

### Phases 16–19: Evaluation, Debugging, Low-Code, Safety
- These are the most "production-ready" phases (all have quizzes + assignments)
- Do them alongside or after the core track

### Phase 20: Real-Time Streaming (`20-real-time-streaming/`)
- Start with `00_START_HERE.ipynb`
- Focused on SSE, WebSocket, and production streaming
- Treat this as an introduction today, not a full specialty track yet
- ~6–8 hours

### Phases 24–27: Advanced Topics
- Deep Learning (39 notebooks), RL (7), Time Series (7), Causal Inference (7)
- All have `00_START_HERE.ipynb` - let them guide you
- Do these after completing your core track

### Phase 28: Practical Data Science (`28-practical-data-science/`)
- Interview preparation and applied practice
- 10 specialty sub-tracks + 3 interview prep notebooks
- ~20–30 hours

### Phase 29: AI Hardware (`29-ai-hardware-llm-validation/`)
- Specialized for silicon validation roles
- 9 guides + 8 lab notebooks
- Only pursue if hardware/infrastructure is your focus

### Phase 30: Inference Optimization (`30-inference-optimization/`)
- Currently a work-in-progress (vLLM notebook available, more planned)
- Covers KV cache, quantization, speculative decoding
- ~6–8 hours when complete

### Phase 31: AI-Powered Dev Tools (`31-ai-powered-dev-tools/`)
- VS Code + Copilot configuration, MCP deep dive, custom instructions
- Read `00_ai_dev_tools_2026.md` early - it compares all major coding tools
- ~10–15 hours

---

## Suggested Weekly Schedule

### If you have 10–15 hours/week:

| Week | Focus |
|------|-------|
| 1–2 | Python basics, NumPy, pandas (Phases 1–2) |
| 3 | Mathematics foundational notebooks (Phase 3) |
| 4 | Tokenization + Embeddings (Phases 4–5) |
| 5–6 | Neural Networks (Phase 6) |
| 7 | Vector Databases (Phase 7) |
| 8–9 | RAG (Phase 8) |
| 10 | MLOps basics (Phase 9) |
| 11 | Prompt Engineering (Phase 11) |
| 12–13 | LLM Fine-tuning (Phase 12) |
| 14 | Local LLMs (Phase 14) |
| 15–16 | AI Agents (Phase 15) |
| 17+ | Specializations, advanced topics, projects |

### If you have 20+ hours/week:
Halve the timeline above. Add the supplementary phases (16–19) in between core phases.

---

## Tips for Novice Learners

1. **Don't try to do everything.** Pick your track, follow the order, skip what your track marks as optional.
2. **Run every code cell.** Reading notebooks is not the same as running them. Type the code yourself when possible.
3. **Break things on purpose.** Change a hyperparameter, remove a layer, corrupt the data. Understanding failure modes teaches more than success.
4. **Use the glossary** ([23-glossary/01_GLOSSARY.md](../23-glossary/01_GLOSSARY.md)) whenever you hit an unfamiliar term.
5. **Ask for help.** Use [GitHub Discussions](https://github.com/PavanMudigonda/zero-to-ai/discussions) if you get stuck.
6. **Build projects.** Each phase suggests projects at the end - do at least one per phase.
7. **Track your progress.** Print [checklist.md](checklist.md) or check off items as you go.

---

*Last updated: April 2026*
