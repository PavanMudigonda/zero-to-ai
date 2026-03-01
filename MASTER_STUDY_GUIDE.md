# Master Study Guide - Zero to AI Mastery

> **Goal**: Become a competitive AI/ML engineer in 6-12 months, ready to interview and build production AI systems.

---

## How to Use This Guide

1. Read this guide top-to-bottom once to understand the full picture
2. Use [CAREER_ROADMAP.md](CAREER_ROADMAP.md) to target the right job roles
3. Follow [checklist.md](checklist.md) to tick off completions
4. Use [REFERENCES.md](REFERENCES.md) for videos, repos, and courses per phase
5. Use [INTERVIEW_PREP.md](INTERVIEW_PREP.md) for Q&A, coding problems, and system design practice
6. Build portfolio projects progressively — they matter more than certifications

---

## The 2026 AI/ML Job Market Reality

**High-demand roles (ranked by market volume):**
1. **ML Engineer** — build, train, and deploy models at scale ($130k-$250k)
2. **AI Engineer / LLM Engineer** — RAG, agents, fine-tuning, prompt systems ($140k-$280k)
3. **Data Scientist** — experimentation, modeling, insights ($110k-$200k)
4. **MLOps / AI Platform Engineer** — infrastructure, pipelines, monitoring ($130k-$230k)

**Skills that make you stand out in 2026:**
- RAG systems (not just "I know LangChain" — can you explain chunking strategies, reranking, eval?)
- LLM fine-tuning (LoRA/QLoRA, DPO alignment, evaluation)
- AI agents and tool-calling (ReAct, multi-agent, MCP)
- MLOps (experiment tracking, model serving, monitoring)
- Hands-on PyTorch (not just scikit-learn)

---

## Learning Tracks — Choose Your Path

### Track A: AI Engineer (Fastest to Market — 4-6 months)
Focus on LLMs, RAG, agents, and deployment. Skip deep math.

> Checklist fast path: `Phases 0→4→5→6→7→10→13→14→8→11 + Portfolio`

```
Month 1:  Phase 0 (Foundations) → Phase 4 (Embeddings) → Phase 5 (NN basics only)
Month 2:  Phase 6 (Vector DBs) → Phase 7 (RAG — all 10 notebooks) → 18 (Gradio/Streamlit)
Month 3:  Phase 10 (Prompt Engineering) → Phase 13 (Local LLMs) → Phase 14 (AI Agents)
Month 4:  Phase 8 (MLOps) → Phase 11 (Fine-tuning) → Portfolio projects
Month 5:  Interview prep → Job applications → Continue learning
```

### Track B: ML Engineer (Thorough — 8-10 months)
Full foundation plus advanced topics. Best for long-term career.

> Checklist path: `Phases 0→1→2→3→4→5→6→7→8→9→10→11→13→14 + Supplementary (16-19) + Portfolio`

```
Month 1-2: Phases 0-2 (Python, Data Science, Mathematics)
Month 3:   Phases 3-5 (Tokenization, Embeddings, Neural Networks)
Month 4:   Phases 6-7 (Vector DBs, RAG) + Phase 18 (Gradio/Streamlit for demos)
Month 5:   Phases 8-9 (MLOps, Specializations) + Phase 16 (Model Evaluation)
Month 6-7: Phases 10-14 (Prompt Engineering, Fine-tuning, Agents, Local LLMs)
Month 8:   Phase 19 (AI Safety) + Portfolio projects + Phase 15 (Streaming)
Month 9:   Interview prep + Certifications + Job applications
```

### Track C: Data Scientist (Analytics + ML — 6-8 months)
Strong focus on statistics, experimentation, classical ML.

> Checklist fast path: `Phases 0→1→2→27→26→7→10→Model Evaluation + Portfolio`

```
Month 1-2: Phases 0-2 (Python, Statistics, Math)
Month 3-4: Phase 27 (Causal Inference) + Phase 26 (Time Series)
Month 5:   Phase 7 (RAG) + Phase 10 (Prompt Engineering)
Month 6:   Model Evaluation (16-model-evaluation/) + Portfolio + Interview prep
```

---

## Phase-by-Phase Learning Notes

### Phase 0: Foundations (1 week)

**What it covers**: AI/ML terminology, mental models.

**Key concepts to understand:**
- Supervised vs Unsupervised vs Reinforcement Learning
- Training, validation, and test sets — why each exists
- Overfitting and underfitting — the bias-variance tradeoff
- Features, labels, predictions, loss functions
- The difference between ML and deep learning and LLMs

**Text Notes:**
> Machine learning is about finding patterns in data to make predictions without explicitly programming rules. The key insight is that computers can *learn* from examples. Deep learning is a subset using neural networks with many layers. LLMs are deep learning models trained on massive text corpora that learn to predict the next token — but this simple task leads to surprisingly powerful capabilities.

**Start here:** [23-glossary/GLOSSARY.md](23-glossary/GLOSSARY.md)

---

### Phase 1: Python & Data Science (3-4 weeks)

**What it covers**: NumPy, Pandas, scikit-learn, visualization.

**Key concepts to understand:**
- NumPy arrays — vectorized operations are 100x faster than Python loops
- Pandas DataFrames — real-world data is always messy; learn to clean it
- Scikit-learn's fit/predict/transform API — consistent interface for all models
- Train/test split, cross-validation — never evaluate on training data
- Feature engineering — often more impactful than model choice

**Text Notes:**
> Most AI/ML job interviews include a coding screen with pandas and scikit-learn. You must be able to clean a dataset, train a model, and evaluate it in 30-60 minutes. Practice on Kaggle competitions. The 278 scikit-learn notebooks cover every major algorithm — don't try to do all of them, focus on: LinearRegression, LogisticRegression, RandomForest, GradientBoosting, KMeans, PCA.

**Practice Labs:**
- Iris classification end-to-end
- House price prediction with feature engineering
- Customer segmentation with K-Means

**Essential Notebooks:**
- [02-data-science/1-numpy-examples/](02-data-science/1-numpy-examples/)
- [02-data-science/2-pandas-examples/](02-data-science/2-pandas-examples/)
- [02-data-science/5-scikit-learn/linear_model/](02-data-science/5-scikit-learn/linear_model/)
- [02-data-science/5-scikit-learn/ensemble/](02-data-science/5-scikit-learn/ensemble/)

**Key GitHub Repos to Study:**
- [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) — read examples, not source
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) — 26 lessons, very practical

---

### Phase 2: Mathematics for ML (2-3 weeks)

**What it covers**: Linear algebra, calculus, probability, statistics.

**Key concepts to understand:**
- **Linear Algebra**: Vectors as directions, matrices as transformations, dot product as similarity
- **Calculus**: Derivatives measure rate of change — gradient descent uses derivatives to find minima
- **Probability**: Bayes theorem, distributions, expected value — essential for understanding uncertainty
- **Statistics**: Hypothesis testing, confidence intervals, p-values

**Text Notes:**
> You do NOT need to be a mathematics PhD to do AI/ML. You need enough math to understand *why* algorithms work, not to prove theorems from scratch. Focus on intuition first (3Blue1Brown videos), then implement from scratch (notebooks). The most important math for LLM work is: matrix multiplication, softmax, log-likelihood, and gradient descent.

**Priority order** (skip the rest for Track A):
1. Linear algebra basics (vectors, matrices, dot products)
2. Gradient descent mechanics
3. Probability and distributions

**Essential Notebooks:**
- [03-maths/foundational/01_linear_algebra_fundamentals.ipynb](03-maths/foundational/01_linear_algebra_fundamentals.ipynb)
- [03-maths/foundational/04_gradient_descent.ipynb](03-maths/foundational/04_gradient_descent.ipynb)
- [03-maths/foundational/03_probability_statistics.ipynb](03-maths/foundational/03_probability_statistics.ipynb)

---

### Phase 3: Tokenization (1 week)

**What it covers**: How text becomes numbers that models can process.

**Key concepts to understand:**
- Tokens ≠ words. "Hello" = 1 token, "tokenization" = 3-4 tokens, emojis = multiple tokens
- BPE (Byte Pair Encoding) — how GPT-style tokenizers work
- Vocabulary size — GPT-4 has ~100k token vocabulary, this affects model context
- Why tokenization matters: longer tokens = cheaper inference; some languages tokenize inefficiently

**Text Notes:**
> Every LLM prompt you send gets tokenized first. Understanding tokenization helps you write better prompts (avoid token waste), estimate costs (OpenAI charges per token), and debug why models behave differently in different languages. The TikToken library (used by OpenAI) and HuggingFace tokenizers are the two most common in production.

**Essential Notebooks:**
- [04-token/01_tokenizers_quickstart.ipynb](04-token/01_tokenizers_quickstart.ipynb)
- [04-token/tiktoken_example.ipynb](04-token/tiktoken_example.ipynb)

---

### Phase 4: Embeddings (1 week)

**What it covers**: Converting text into numerical vectors that capture semantic meaning.

**Key concepts to understand:**
- Embeddings map text to points in high-dimensional space where similar meanings are close together
- "king" - "man" + "woman" ≈ "queen" — embeddings capture relationships
- Cosine similarity — the standard way to compare embeddings
- The difference between word embeddings (Word2Vec) and sentence embeddings (sentence-transformers)
- OpenAI's `text-embedding-ada-002` and `text-embedding-3-large` — know their dimensions and costs

**Text Notes:**
> Embeddings are the foundation of all modern search and RAG. When you use Google or ask ChatGPT to search your documents, embeddings are what make semantic similarity work. The key skill is choosing the right embedding model for your use case: OpenAI is highest quality but costs money; `bge-m3` and `nomic-embed-text` are excellent free alternatives via Ollama.

**Essential Notebooks:**
- [05-embeddings/embeddings_intro.ipynb](05-embeddings/embeddings_intro.ipynb)
- [05-embeddings/semantic_similarity.ipynb](05-embeddings/semantic_similarity.ipynb)
- [05-embeddings/semantic_search_intro.ipynb](05-embeddings/semantic_search_intro.ipynb)

---

### Phase 5: Neural Networks (2-3 weeks)

**What it covers**: How neural networks learn, attention mechanism, Transformer architecture.

**Key concepts to understand:**
- Neurons, layers, activation functions (ReLU, GELU, Sigmoid)
- Forward pass (prediction) and backward pass (learning via backpropagation)
- Loss functions — what the model is optimizing
- The Transformer architecture — the backbone of every modern LLM
- Self-attention — how models relate different parts of a sequence to each other
- Multi-head attention — learning different types of relationships in parallel

**Text Notes:**
> The Transformer (2017 paper: "Attention Is All You Need") changed everything. Before it, we used RNNs which process sequences step-by-step. Transformers process entire sequences in parallel using the attention mechanism. This is why they scale so well on modern GPUs. You don't need to implement one from scratch, but you should understand the architecture well enough to explain it in an interview.

**The Transformer in plain English:**
1. Tokenize input text
2. Convert tokens to embeddings (learned vectors)
3. Add positional encodings (so the model knows token order)
4. Run through N transformer blocks (attention + feedforward)
5. Project to vocabulary size
6. Softmax → probability over next token

**Essential Notebooks:**
- [06-neural-networks/01_neural_network_basics.ipynb](06-neural-networks/01_neural_network_basics.ipynb)
- [06-neural-networks/04_attention_mechanism.ipynb](06-neural-networks/04_attention_mechanism.ipynb)
- [06-neural-networks/05_transformer_architecture.ipynb](06-neural-networks/05_transformer_architecture.ipynb)

---

### Phase 6: Vector Databases (1 week)

**What it covers**: Storing and querying embeddings at scale.

**Key concepts to understand:**
- ANN (Approximate Nearest Neighbor) search — exact search is too slow at scale
- HNSW (Hierarchical Navigable Small World) — the algorithm most vector DBs use
- ChromaDB — easiest to start with, runs in-memory or persisted locally
- Pinecone — managed cloud vector DB, good for production
- pgvector — vector search inside PostgreSQL — great if you already use Postgres

**Text Notes:**
> Vector databases are what make RAG fast. Without them, you'd have to compare your query embedding to every document embedding sequentially — too slow for thousands of documents. With a vector DB, you can search millions of vectors in milliseconds. ChromaDB is perfect for prototypes; pgvector is great for production if you already have a Postgres database.

**Comparison quick reference:**

| Database | Best For | Cost | Scalability |
|----------|----------|------|-------------|
| ChromaDB | Local/prototype | Free | Medium |
| Qdrant | Self-hosted prod | Free/Paid | High |
| Weaviate | Hybrid search | Free/Paid | High |
| Pinecone | Managed/cloud | Paid | Very High |
| pgvector | Already use Postgres | Free | High |

**Essential Notebooks:**
- [07-vector-databases/01_vector_db_basics.ipynb](07-vector-databases/01_vector_db_basics.ipynb)
- [07-vector-databases/02_chroma_guide.ipynb](07-vector-databases/02_chroma_guide.ipynb)

---

### Phase 7: RAG Systems (2 weeks)

**What it covers**: Retrieval-Augmented Generation — grounding LLMs in your own documents.

**Key concepts to understand:**
- The RAG pipeline: Document → Chunk → Embed → Store → Query → Retrieve → Augment → Generate
- Chunking strategies: fixed-size, semantic, recursive, document-structure-aware
- Retrieval strategies: dense (semantic), sparse (BM25/keyword), hybrid
- Reranking: using a cross-encoder to reorder retrieved results for better relevance
- Context window management: how much context to include without overwhelming the LLM
- Evaluation: RAGAS framework metrics (faithfulness, answer relevancy, context precision)

**Text Notes:**
> RAG is the most in-demand AI skill in enterprise right now. Every company wants to "chat with their documents" without giving their data to OpenAI. The basic RAG is easy to build — the challenge is making it *actually work well*. Common failures: bad chunking (chunks break across key info), wrong similarity metric, too many retrieved chunks overwhelming the LLM. Advanced RAG uses HyDE (Hypothetical Document Embeddings), query expansion, and parent-child retrieval.

**Practice Labs — build these, put them on GitHub:**
1. Basic RAG chatbot over a PDF (LangChain + ChromaDB + OpenAI or Ollama)
2. Advanced RAG with reranking (add a cross-encoder)
3. Fully local RAG (Ollama + ChromaDB — no cloud APIs)
4. RAG with evaluation (RAGAS metrics)

**Essential Notebooks:**
- [08-rag/01_basic_rag.ipynb](08-rag/01_basic_rag.ipynb)
- [08-rag/02_document_processing.ipynb](08-rag/02_document_processing.ipynb)
- [08-rag/05_advanced_retrieval.ipynb](08-rag/05_advanced_retrieval.ipynb)
- [08-rag/07_evaluation.ipynb](08-rag/07_evaluation.ipynb)
- [08-rag/09_advanced_retrieval.ipynb](08-rag/09_advanced_retrieval.ipynb)

---

### Phase 8: MLOps (2 weeks)

**What it covers**: Deploying, monitoring, and maintaining ML systems in production.

**Key concepts to understand:**
- Experiment tracking: MLflow and Weights & Biases — track metrics, parameters, artifacts
- Model serving: FastAPI for lightweight APIs; vLLM/TGI for LLM inference at scale
- Containerization: Docker — package your model and dependencies into a portable image
- Model monitoring: data drift, concept drift, performance degradation
- CI/CD for ML: automated testing, model validation before deployment

**Text Notes:**
> 80% of ML projects fail not because of bad models but because of bad MLOps. Models that work in notebooks break in production. The key discipline: make everything reproducible (seed everything, version data and code), test your data pipeline as rigorously as your model, and set up monitoring from day one. MLflow is free and excellent — use it for every project.

**The MLOps Stack to Learn:**
- MLflow (experiment tracking + model registry)
- FastAPI (model serving)
- Docker (containerization)
- GitHub Actions (CI/CD)
- Prometheus + Grafana (monitoring)

**Essential Notebooks:**
- [09-mlops/01_experiment_tracking.ipynb](09-mlops/01_experiment_tracking.ipynb)
- [09-mlops/02_fastapi_basics.ipynb](09-mlops/02_fastapi_basics.ipynb)
- [09-mlops/03_model_deployment.ipynb](09-mlops/03_model_deployment.ipynb)
- [09-mlops/04_docker_ml.ipynb](09-mlops/04_docker_ml.ipynb)

---

### Phase 9: Specializations (2-3 weeks, choose one)

Pick based on your target role and interests. Do not try to do all three.

**AI Agents** (best for AI Engineer role):
- Learn ReAct pattern, function/tool calling, memory management
- Study LangGraph for stateful multi-agent workflows
- Study MCP (Model Context Protocol) — the emerging standard for AI tool integration
- [10-specializations/ai-agents/](10-specializations/ai-agents/)

**Computer Vision** (best for CV Engineer role):
- Learn CNN architectures, object detection (YOLO), CLIP for vision-language
- [10-specializations/computer-vision/](10-specializations/computer-vision/)

**NLP** (best for NLP Engineer role):
- Learn BERT/GPT task fine-tuning, NER, summarization
- [10-specializations/nlp/](10-specializations/nlp/)

---

### Phase 10: Prompt Engineering (1 week)

**What it covers**: Systematic techniques for getting reliable outputs from LLMs.

**Key concepts to understand:**
- Zero-shot, one-shot, few-shot prompting
- Chain-of-Thought (CoT) — forcing step-by-step reasoning dramatically improves accuracy
- ReAct prompting — interleaving reasoning and action steps
- System prompts vs user prompts vs assistant turns
- Temperature and top-p sampling — controlling output randomness
- Structured outputs — JSON mode, function calling, DSPy for programmable prompts

**Text Notes:**
> Prompt engineering is not just about writing nice prompts — it's about systematic, reproducible, testable prompting. Use DSPy to optimize prompts programmatically. Always evaluate: build an eval set, measure metrics, then improve. The best prompt engineers treat prompting like software engineering: version control, testing, iteration.

**Prompting best practices cheatsheet:**
- Be specific about format, tone, and constraints
- Use examples for complex tasks (few-shot)
- Add "Let's think step by step" for reasoning tasks
- Use XML tags to structure complex prompts: `<instructions>`, `<examples>`, `<context>`
- System prompt: role + constraints + format. User prompt: task + context + examples

**Essential Notebooks:**
- [11-prompt-engineering/01_basic_prompting.ipynb](11-prompt-engineering/01_basic_prompting.ipynb)
- [11-prompt-engineering/02_chain_of_thought.ipynb](11-prompt-engineering/02_chain_of_thought.ipynb)
- [11-prompt-engineering/05_structured_outputs_dspy.ipynb](11-prompt-engineering/05_structured_outputs_dspy.ipynb)

---

### Phase 11: LLM Fine-tuning (2-3 weeks)

**What it covers**: Adapting pre-trained LLMs to specific tasks or domains.

**Key concepts to understand:**
- When to fine-tune vs when to use RAG vs when to use prompting alone
- LoRA (Low-Rank Adaptation) — freeze most weights, train small adapter matrices
- QLoRA — quantize the base model (4-bit) to fit on consumer GPUs, then apply LoRA
- SFT (Supervised Fine-Tuning) — train on examples of input/output pairs
- DPO (Direct Preference Optimization) — align model to human preferences without RL
- Evaluation: perplexity, BLEU, BERTScore, LLM-as-judge

**Text Notes:**
> Fine-tuning is not always the answer. First try: (1) better prompting, (2) RAG, then (3) fine-tuning. Fine-tune when the model needs to learn new facts/format/style that can't be done in context. QLoRA makes fine-tuning accessible: you can fine-tune Llama 3.1 8B on a single A100 (or even RTX 3090). For production, use Unsloth for 2-4x faster training with less memory.

**Decision framework: Prompt → RAG → Fine-tune:**
1. Does the model already know the domain? → Just prompt it well
2. Do you need factual accuracy from your own data? → Add RAG
3. Do you need specific style, format, or behavior not achievable with prompting/RAG? → Fine-tune

**Essential Notebooks:**
- [12-llm-finetuning/00_START_HERE.ipynb](12-llm-finetuning/00_START_HERE.ipynb)
- [12-llm-finetuning/01_dataset_preparation.ipynb](12-llm-finetuning/01_dataset_preparation.ipynb)
- [12-llm-finetuning/04_qlora_efficient.ipynb](12-llm-finetuning/04_qlora_efficient.ipynb)
- [12-llm-finetuning/05_dpo_alignment.ipynb](12-llm-finetuning/05_dpo_alignment.ipynb)
- [12-llm-finetuning/09_unsloth_fast_finetuning.ipynb](12-llm-finetuning/09_unsloth_fast_finetuning.ipynb)

---

### Phase 12: Multimodal AI (1 week)

**What it covers**: Models that handle images, text, and multiple data types.

**Key concepts to understand:**
- CLIP — contrastive learning to align image and text embeddings in the same space
- Vision-Language Models (VLMs): GPT-4V, Claude 3, LLaVA, Qwen-VL
- Stable Diffusion — latent diffusion model for image generation
- Multimodal RAG — retrieve both text and images for richer context

**Essential Notebooks:**
- [13-multimodal/vision-language/01_clip_basics.ipynb](13-multimodal/vision-language/01_clip_basics.ipynb)
- [13-multimodal/image-generation/01_stable_diffusion.ipynb](13-multimodal/image-generation/01_stable_diffusion.ipynb)

---

### Phase 13: Local LLMs (1 week)

**What it covers**: Running open-source LLMs locally for privacy, cost, and speed.

**Key concepts to understand:**
- Ollama — easiest way to run LLMs locally; supports Llama 3.3, Qwen2.5, Mistral, DeepSeek
- llama.cpp — CPU-optimized inference; runs quantized models on any hardware
- vLLM — production-grade LLM server with PagedAttention for max throughput
- Quantization: Q4_K_M, Q8_0 — trade quality for memory. 4-bit = half quality loss, half memory
- OpenAI-compatible API — run local models but use the same code as OpenAI

**Text Notes:**
> Local LLMs are increasingly viable for production. DeepSeek R1 (7B) runs on a laptop and outperforms GPT-3.5 on many tasks. For enterprise, local LLMs provide: (1) data privacy, (2) no per-token cost, (3) no rate limits, (4) customizability. The standard pattern: use Ollama for development, vLLM for production serving.

**Essential Notebooks:**
- [14-local-llms/01_ollama_quickstart.ipynb](14-local-llms/01_ollama_quickstart.ipynb)
- [14-local-llms/03_local_rag_with_ollama.ipynb](14-local-llms/03_local_rag_with_ollama.ipynb)
- [14-local-llms/04_llm_server_and_api.ipynb](14-local-llms/04_llm_server_and_api.ipynb)

---

### Phase 14: AI Agents (2 weeks)

**What it covers**: Autonomous systems that use LLMs to plan and execute multi-step tasks.

**Key concepts to understand:**
- ReAct loop: Reasoning → Acting → Observing → Reasoning... (cycle until goal reached)
- Tool calling / function calling — giving the LLM access to external functions
- Agent memory: in-context (recent messages), external (vector DB), procedural (code)
- Multi-agent systems — specialized agents collaborating (orchestrator + workers)
- MCP (Model Context Protocol) — emerging standard for connecting LLMs to tools/data
- LangGraph — graph-based framework for stateful agent workflows

**Text Notes:**
> Agents are where AI goes from "chat assistant" to "does things for you." The key challenge is reliability — agents fail in unexpected ways. Best practices: (1) keep tools simple and focused, (2) add explicit error handling, (3) test each tool independently, (4) use structured outputs so the LLM response is always parseable, (5) add human-in-the-loop checkpoints for high-stakes actions.

**Essential Notebooks:**
- [15-ai-agents/01_intro_to_agents.ipynb](15-ai-agents/01_intro_to_agents.ipynb)
- [15-ai-agents/02_function_calling.ipynb](15-ai-agents/02_function_calling.ipynb)
- [15-ai-agents/03_react_pattern.ipynb](15-ai-agents/03_react_pattern.ipynb)
- [15-ai-agents/06_mcp_model_context_protocol.ipynb](15-ai-agents/06_mcp_model_context_protocol.ipynb)
- [15-ai-agents/09_autonomous_agents_2026.ipynb](15-ai-agents/09_autonomous_agents_2026.ipynb)

---

### Phase 15: Real-Time Streaming (1 week)

**What it covers**: Streaming LLM responses in production for better UX and latency.

**Essential Notebooks:**
- [20-real-time-streaming/01_streaming_responses.ipynb](20-real-time-streaming/01_streaming_responses.ipynb)
- [20-real-time-streaming/04_production_streaming.ipynb](20-real-time-streaming/04_production_streaming.ipynb)

---

### Supplementary Phases (Do After Core Track)

**Model Evaluation** — [16-model-evaluation/](16-model-evaluation/)
> Essential concepts for any ML role: classification metrics, LLM evaluation, bias/fairness. Do these after Phase 7 (RAG) — RAGAS evaluation is directly applicable.
- [16-model-evaluation/01_classification_metrics.ipynb](16-model-evaluation/01_classification_metrics.ipynb)
- [16-model-evaluation/03_llm_evaluation.ipynb](16-model-evaluation/03_llm_evaluation.ipynb)
- [16-model-evaluation/04_bias_fairness.ipynb](16-model-evaluation/04_bias_fairness.ipynb)

**Debugging & Troubleshooting** — [17-debugging-troubleshooting/](17-debugging-troubleshooting/)
> Learn to debug data issues, performance profiling, and model debugging. Do this alongside your portfolio projects.

**Low-Code AI Tools** — [18-low-code-ai-tools/](18-low-code-ai-tools/)
> Gradio, Streamlit — use these to build quick demos for portfolio projects. Do early; it accelerates everything.

**AI Safety & Red Teaming** — [19-ai-safety-redteaming/](19-ai-safety-redteaming/)
> Prompt injection, PII privacy, bias, red teaming. Important for any production AI role. Do before deploying anything publicly.

---

## Portfolio Projects — What Employers Want to See

### Tier 1: Show You Can Build (Required)

**Project 1: RAG Document Assistant**
- Build a chatbot that answers questions from your own documents (PDF, text, etc.)
- Tech: LangChain/LlamaIndex + ChromaDB + Ollama (or OpenAI) + FastAPI + Streamlit
- Add: hybrid search, reranking, RAGAS evaluation
- Deploy: HuggingFace Spaces or Render

**Project 2: Fine-tuned Domain Expert**
- Pick a domain (legal, medical, customer service, coding)
- Fine-tune a small model (Llama 3.2 3B or Qwen2.5 1.5B) with QLoRA
- Evaluate before/after and document the improvement
- Deploy with Ollama or vLLM

**Project 3: End-to-End MLOps Pipeline**
- Train a model (any domain — your choice)
- Track experiments with MLflow
- Serve with FastAPI + Docker
- Add automated testing with GitHub Actions

### Tier 2: Show You Think Deeply (Differentiators)

**Project 4: AI Agent with Real Tools**
- Build an agent that uses at least 3 tools (web search, calculator, code execution)
- Add memory so it can reference past conversations
- Document failure modes and how you addressed them

**Project 5: Evaluation Framework**
- Build a proper eval harness for any of your projects above
- Automated regression testing for model quality
- This shows engineering maturity that most candidates lack

---

## Quick Reference: Key Papers to Know

You don't need to read these end-to-end. Know the key contributions.

| Paper | Year | Why It Matters |
|-------|------|----------------|
| Attention Is All You Need | 2017 | Transformer architecture — foundation of all LLMs |
| BERT | 2018 | Bidirectional pre-training, fine-tuning paradigm |
| GPT-3 (Language Models are Few-Shot Learners) | 2020 | Scale + few-shot prompting |
| LoRA | 2021 | Parameter-efficient fine-tuning — enables QLoRA |
| InstructGPT (RLHF) | 2022 | Alignment via human feedback |
| RAG (Lewis et al.) | 2020 | Retrieval-augmented generation |
| Chain-of-Thought Prompting | 2022 | Reasoning via step-by-step prompts |
| Toolformer | 2023 | Teaching LLMs to use tools |
| Direct Preference Optimization (DPO) | 2023 | Alignment without RL |

---

## Weekly Study Schedule Template

### Weekday routine (3 hours/day):
- **Hour 1**: Read/watch (theory, new concepts)
- **Hour 2**: Hands-on notebook or lab
- **Hour 3**: Project work or practice problem

### Weekend routine (4-5 hours/day):
- **2-3 hours**: Deep dive on one topic (notebook + implementation)
- **1-2 hours**: Portfolio project work
- **30 min**: Review/notes/Anki cards

### Study tips:
- Explain every concept you learn in your own words (Feynman technique)
- Build something every week — even small things
- Join communities: Hugging Face Discord, r/MachineLearning, AI Twitter/X
- Read one blog post per day: Lilian Weng, Sebastian Ruder, Jay Alammar

---

## Measuring Your Progress

### Checkpoints:

**Week 4**: Can you train a scikit-learn classifier on a new dataset? Clean data? Evaluate properly?

**Week 8**: Can you explain how transformers work? Build a simple neural network in PyTorch?

**Week 12**: Can you build a working RAG system from scratch? Evaluate its quality?

**Week 16**: Can you fine-tune a small LLM? Deploy it with FastAPI?

**Week 20**: Can you build a working AI agent with tools and memory?

**Week 24**: Do you have 3+ portfolio projects on GitHub with READMEs? Can you explain your architecture decisions?

---

## Next: Read These

- [CAREER_ROADMAP.md](CAREER_ROADMAP.md) — job targeting, interview prep, resume tips
- [REFERENCES.md](REFERENCES.md) — all videos, courses, GitHub repos, and papers
- [checklist.md](checklist.md) — track your completion progress
