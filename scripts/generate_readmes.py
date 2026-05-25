#!/usr/bin/env python3
"""
Generate README.md stubs for all jupyter-notebooks sections.
Run from repo root: python3 scripts/generate_readmes.py
"""
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "jupyter-notebooks")

SECTIONS = [
    {
        "dir": "00-course-setup",
        "hub": "00-course-setup.ipynb",
        "title": "Course Setup",
        "status": "complete",
        "description": "Environment setup, repo orientation, and quick-start guide for the Zero to AI curriculum.",
        "topics": [
            "Fork, clone, and install dependencies",
            "Jupyter and virtual environment setup",
            "Model landscape overview and troubleshooting",
        ],
        "prereqs": "None — this is the starting point.",
        "next": "[01-python/README.md](../01-python/README.md) — Python Fundamentals",
    },
    {
        "dir": "01-python",
        "hub": "01-python.ipynb",
        "title": "Python Fundamentals",
        "status": "developing",
        "description": "A lightweight bridge into the curriculum — cover Python basics before diving into data science and ML.",
        "topics": [
            "Variables, data types, loops, and functions",
            "Classes, modules, and virtual environments",
            "Recommended external resources and readiness checklist",
        ],
        "prereqs": "None.",
        "next": "[02-data-science/README.md](../02-data-science/README.md) — Data Science",
    },
    {
        "dir": "02-data-science",
        "hub": "02-data-science.ipynb",
        "title": "Data Science",
        "status": "complete",
        "description": "NumPy, pandas, matplotlib, and scikit-learn — the essential toolkit for every ML practitioner.",
        "topics": [
            "NumPy arrays, broadcasting, and vectorised operations",
            "pandas DataFrames, groupby, merges, and cleaning",
            "Matplotlib and seaborn visualisations",
            "scikit-learn pipelines, preprocessing, and model basics",
        ],
        "prereqs": "[01-python/README.md](../01-python/README.md)",
        "next": "[03-maths/README.md](../03-maths/README.md) or [04-token/README.md](../04-token/README.md)",
    },
    {
        "dir": "03-maths",
        "hub": "03-maths.ipynb",
        "title": "Math Foundations",
        "status": "complete",
        "description": "Linear algebra, calculus, statistics, and probability — the mathematical backbone of machine learning (153 notebooks across 10 learning tracks).",
        "topics": [
            "Linear algebra: vectors, matrices, eigenvalues",
            "Calculus: derivatives, gradients, and optimisation",
            "Probability and statistics for ML",
            "Tracks: 3Blue1Brown, MML-Book, CS229, ISLP, MLPP, DLI, SLP, and more",
        ],
        "prereqs": "[01-python/README.md](../01-python/README.md)",
        "next": "[04-token/README.md](../04-token/README.md)",
    },
    {
        "dir": "04-token",
        "hub": "04-token.ipynb",
        "title": "Tokenization",
        "status": "complete",
        "description": "How text becomes numbers — tokenizers, vocabularies, training, and production tokenization pipelines.",
        "topics": [
            "BPE, WordPiece, and SentencePiece tokenizers",
            "HuggingFace `tokenizers` library and tiktoken",
            "Vocabulary training and specialised domain tokenizers",
            "Production integration and pipeline components",
        ],
        "prereqs": "[02-data-science/README.md](../02-data-science/README.md)",
        "next": "[05-embeddings/README.md](../05-embeddings/README.md)",
    },
    {
        "dir": "05-embeddings",
        "hub": "05-embeddings.ipynb",
        "title": "Embeddings",
        "status": "complete",
        "description": "Dense vector representations for semantic search, paraphrase mining, and similarity tasks.",
        "topics": [
            "Sentence transformers and embedding model comparison",
            "Semantic textual similarity and paraphrase mining",
            "OpenAI and HuggingFace embedding APIs",
            "Vector database integration",
        ],
        "prereqs": "[04-token/README.md](../04-token/README.md)",
        "next": "[06-neural-networks/README.md](../06-neural-networks/README.md) or [07-vector-databases/README.md](../07-vector-databases/README.md)",
    },
    {
        "dir": "06-neural-networks",
        "hub": "06-neural-networks.ipynb",
        "title": "Neural Networks",
        "status": "complete",
        "description": "Backpropagation, PyTorch fundamentals, attention mechanisms, and the transformer architecture.",
        "topics": [
            "Neural network basics and backpropagation",
            "PyTorch tensors, autograd, and training loops",
            "Attention mechanism and self-attention",
            "Transformer architecture end-to-end",
        ],
        "prereqs": "[03-maths/README.md](../03-maths/README.md) · [05-embeddings/README.md](../05-embeddings/README.md)",
        "next": "[07-vector-databases/README.md](../07-vector-databases/README.md)",
    },
    {
        "dir": "07-vector-databases",
        "hub": "07-vector-databases.ipynb",
        "title": "Vector Databases",
        "status": "complete",
        "description": "Similarity search, approximate nearest neighbours, and vector database systems for production RAG.",
        "topics": [
            "FAISS, Chroma, Pinecone, Weaviate, and Qdrant",
            "ANN algorithms: HNSW, IVF, and PQ",
            "Metadata filtering and hybrid search",
            "Indexing and query performance trade-offs",
        ],
        "prereqs": "[05-embeddings/README.md](../05-embeddings/README.md)",
        "next": "[08-rag/README.md](../08-rag/README.md)",
    },
    {
        "dir": "08-rag",
        "hub": "08-rag.ipynb",
        "title": "RAG Systems",
        "status": "complete",
        "description": "Retrieval-Augmented Generation — from basic document retrieval to production RAG pipelines with evaluation.",
        "topics": [
            "Basic RAG with chunking, embedding, and retrieval",
            "LangChain and LlamaIndex integration",
            "Advanced retrieval: HyDE, reranking, and multi-query",
            "RAG evaluation with RAGAS and Arize Phoenix",
        ],
        "prereqs": "[07-vector-databases/README.md](../07-vector-databases/README.md) · [05-embeddings/README.md](../05-embeddings/README.md)",
        "next": "[09-mlops/README.md](../09-mlops/README.md) or [11-prompt-engineering/README.md](../11-prompt-engineering/README.md)",
    },
    {
        "dir": "09-mlops",
        "hub": "09-mlops.ipynb",
        "title": "MLOps",
        "status": "complete",
        "description": "Deploy, monitor, and maintain ML models as production systems — experiment tracking, serving, CI/CD, and cloud deployment.",
        "topics": [
            "MLflow experiment tracking and model registry",
            "FastAPI model serving and Docker containerisation",
            "Data drift detection and production monitoring",
            "GitHub Actions CI/CD pipelines for ML",
            "Cloud deployment (AWS, GCP, Azure)",
        ],
        "prereqs": "[08-rag/README.md](../08-rag/README.md)",
        "next": "[10-specializations/README.md](../10-specializations/README.md) or [11-prompt-engineering/README.md](../11-prompt-engineering/README.md)",
    },
    {
        "dir": "10-specializations",
        "hub": "10-specializations.ipynb",
        "title": "Specializations",
        "status": "developing",
        "description": "Three focused deep-dive tracks — Computer Vision, Advanced NLP, and AI Agents — for domain expertise after the core curriculum.",
        "topics": [
            "Computer Vision: image classification, object detection, CLIP, Stable Diffusion",
            "Advanced NLP: NER, translation, summarisation, information extraction",
            "AI Agents specialisation: AutoGen, LangGraph, multi-agent systems",
        ],
        "prereqs": "Phases 00–09 complete.",
        "next": "[11-prompt-engineering/README.md](../11-prompt-engineering/README.md) or your chosen advanced phase",
    },
    {
        "dir": "11-prompt-engineering",
        "hub": "11-prompt-engineering.ipynb",
        "title": "Prompt Engineering",
        "status": "complete",
        "description": "Systematic model interaction design — few-shot prompting, chain-of-thought, structured outputs, and 2026 reasoning-model patterns.",
        "topics": [
            "Zero-shot, one-shot, and few-shot prompting",
            "Chain-of-thought and ReAct prompting",
            "Structured outputs with JSON schema constraints",
            "Long context strategies and prompt caching",
        ],
        "prereqs": "[08-rag/README.md](../08-rag/README.md)",
        "next": "[12-llm-finetuning/README.md](../12-llm-finetuning/README.md)",
    },
    {
        "dir": "12-llm-finetuning",
        "hub": "12-llm-finetuning.ipynb",
        "title": "LLM Fine-Tuning",
        "status": "complete",
        "description": "SFT, LoRA, QLoRA, DPO, and GRPO — when and how to fine-tune large language models responsibly.",
        "topics": [
            "Supervised fine-tuning and dataset preparation",
            "LoRA and QLoRA for memory-efficient training",
            "DPO and GRPO alignment techniques",
            "Evaluation, quantisation (GPTQ/AWQ), and deployment",
        ],
        "prereqs": "[11-prompt-engineering/README.md](../11-prompt-engineering/README.md) · [09-mlops/README.md](../09-mlops/README.md)",
        "next": "[13-multimodal/README.md](../13-multimodal/README.md) or [14-local-llms/README.md](../14-local-llms/README.md)",
    },
    {
        "dir": "13-multimodal",
        "hub": "13-multimodal.ipynb",
        "title": "Multimodal AI",
        "status": "developing",
        "description": "Vision-language models, image generation, audio AI, and systems that combine text, images, and audio.",
        "topics": [
            "Vision-language models: CLIP, LLaVA, GPT-4V, Gemini Vision",
            "Image generation: Stable Diffusion, DALL-E 3, ControlNet",
            "Audio and speech: Whisper, TTS, audio classification",
            "Multimodal RAG combining text and image retrieval",
        ],
        "prereqs": "[06-neural-networks/README.md](../06-neural-networks/README.md) · [11-prompt-engineering/README.md](../11-prompt-engineering/README.md)",
        "next": "[14-local-llms/README.md](../14-local-llms/README.md) or [15-ai-agents/README.md](../15-ai-agents/README.md)",
    },
    {
        "dir": "14-local-llms",
        "hub": "14-local-llms.ipynb",
        "title": "Local LLMs",
        "status": "complete",
        "description": "Run models locally with Ollama, llama.cpp, MLX, and vLLM — privacy, cost control, and deployment flexibility.",
        "topics": [
            "Ollama quickstart and open-source model overview",
            "Local RAG with Ollama",
            "LLM server setup and OpenAI-compatible API",
            "Speculative decoding and performance considerations",
            "2026 stack: MLX for Apple Silicon, vLLM and SGLang for GPU serving",
        ],
        "prereqs": "[12-llm-finetuning/README.md](../12-llm-finetuning/README.md)",
        "next": "[30-inference-optimization/README.md](../30-inference-optimization/README.md) or [15-ai-agents/README.md](../15-ai-agents/README.md)",
    },
    {
        "dir": "15-ai-agents",
        "hub": "15-ai-agents.ipynb",
        "title": "AI Agents",
        "status": "complete",
        "description": "Autonomous AI systems — function calling, ReAct, multi-agent frameworks, MCP, and agentic evaluation.",
        "topics": [
            "Function calling and tool use",
            "ReAct and reasoning agent patterns",
            "Multi-agent frameworks: AutoGen, LangGraph, OpenAI Agents SDK",
            "Model Context Protocol (MCP) integration",
            "Autonomous agents and agentic evaluation",
        ],
        "prereqs": "[11-prompt-engineering/README.md](../11-prompt-engineering/README.md) · [08-rag/README.md](../08-rag/README.md)",
        "next": "[16-model-evaluation/README.md](../16-model-evaluation/README.md)",
    },
    {
        "dir": "16-model-evaluation",
        "hub": "16-model-evaluation.ipynb",
        "title": "Model Evaluation",
        "status": "complete",
        "description": "Classification, regression, LLM, and agent evaluation — metrics, LLM-as-judge, bias detection, and A/B testing.",
        "topics": [
            "Classification metrics: accuracy, precision, recall, AUC",
            "LLM evaluation: BLEU, ROUGE, BERTScore, LLM-as-judge",
            "Bias and fairness measurement",
            "Agent evaluation: tool use, task success, multi-step scoring",
        ],
        "prereqs": "[09-mlops/README.md](../09-mlops/README.md) · [15-ai-agents/README.md](../15-ai-agents/README.md)",
        "next": "[17-debugging-troubleshooting/README.md](../17-debugging-troubleshooting/README.md)",
    },
    {
        "dir": "17-debugging-troubleshooting",
        "hub": "17-debugging-troubleshooting.ipynb",
        "title": "Debugging & Troubleshooting",
        "status": "developing",
        "description": "Systematic ML debugging — data issues, model failures, performance profiling, and production diagnostics.",
        "topics": [
            "ML debugging workflow and failure modes",
            "Data quality issues: missing values, label errors, distribution shift",
            "Performance profiling: CPU, memory, GPU utilisation",
            "Gradient issues, overfitting/underfitting diagnosis",
            "Production monitoring and error analysis",
        ],
        "prereqs": "[16-model-evaluation/README.md](../16-model-evaluation/README.md)",
        "next": "[18-low-code-ai-tools/README.md](../18-low-code-ai-tools/README.md)",
    },
    {
        "dir": "18-low-code-ai-tools",
        "hub": "18-low-code-ai-tools.ipynb",
        "title": "Low-Code AI Tools",
        "status": "complete",
        "description": "Gradio, Streamlit, Hugging Face Spaces, and AutoML — build and deploy ML demos fast.",
        "topics": [
            "Gradio interfaces and Blocks API",
            "Streamlit data apps and dashboards",
            "Hugging Face Spaces deployment",
            "AutoML platforms for rapid prototyping",
        ],
        "prereqs": "Phases 01–15 complete · Basic Python.",
        "next": "[19-ai-safety-redteaming/README.md](../19-ai-safety-redteaming/README.md)",
    },
    {
        "dir": "19-ai-safety-redteaming",
        "hub": "19-ai-safety-redteaming.ipynb",
        "title": "AI Safety & Red-Teaming",
        "status": "complete",
        "description": "Prompt injection, jailbreaking, adversarial testing, and responsible AI practices for production systems.",
        "topics": [
            "Prompt injection and jailbreak attack patterns",
            "Red-teaming methodology and adversarial testing",
            "Safety layers: input filtering, output guardrails, monitoring",
            "Responsible AI: bias, fairness, and governance",
        ],
        "prereqs": "[15-ai-agents/README.md](../15-ai-agents/README.md) · [11-prompt-engineering/README.md](../11-prompt-engineering/README.md)",
        "next": "[20-real-time-streaming/README.md](../20-real-time-streaming/README.md)",
    },
    {
        "dir": "20-real-time-streaming",
        "hub": "20-real-time-streaming.ipynb",
        "title": "Real-Time & Streaming AI",
        "status": "intro",
        "description": "SSE, WebSockets, streaming RAG, and real-time voice pipelines for live AI applications.",
        "topics": [
            "Server-Sent Events (SSE) and streaming LLM responses",
            "WebSocket-based real-time chat applications",
            "Streaming RAG pipelines with progressive loading",
            "Real-time voice and multimodal interaction patterns",
        ],
        "prereqs": "[15-ai-agents/README.md](../15-ai-agents/README.md) · [09-mlops/README.md](../09-mlops/README.md)",
        "next": "[09-mlops/README.md](../09-mlops/README.md) · [13-multimodal/README.md](../13-multimodal/README.md)",
    },
    {
        "dir": "21-quizzes",
        "hub": "21-quizzes.ipynb",
        "title": "Quizzes",
        "status": "developing",
        "description": "Phase-level pre- and post-quizzes to assess mastery and identify knowledge gaps throughout the curriculum.",
        "topics": [
            "Pre-quiz: baseline knowledge check before a phase",
            "Post-quiz: learning validation after completing a phase",
            "Currently available: Phases 15–18 (Agents, Evaluation, Debugging, Low-Code)",
        ],
        "prereqs": "Varies by quiz — see the hub notebook.",
        "next": "[22-references/README.md](../22-references/README.md)",
    },
    {
        "dir": "22-references",
        "hub": "22-references.ipynb",
        "title": "References & External Resources",
        "status": "complete",
        "description": "Curated external resource shelf — Microsoft labs, Stanford courses, YouTube educators, and cloud platform guides.",
        "topics": [
            "Microsoft AI/ML learning labs (AI for Beginners, Generative AI for Beginners, etc.)",
            "Stanford CS229, CS224N, CS231N lecture collections",
            "3Blue1Brown, Andrej Karpathy, StatQuest video resources",
            "AWS, Google Cloud, and Azure ML learning paths",
        ],
        "prereqs": "None — use as a supplement at any point.",
        "next": "[23-glossary/README.md](../23-glossary/README.md)",
    },
    {
        "dir": "23-glossary",
        "hub": "23-glossary.ipynb",
        "title": "Glossary & Foundations",
        "status": "complete",
        "description": "Vocabulary reference for the entire curriculum — look up AI/ML terms before they slow you down in later phases.",
        "topics": [
            "A–Z definitions for core AI, ML, and LLM terminology",
            "Terms sourced from production use and across all 34 phases",
            "Useful before embeddings, RAG, fine-tuning, safety, and agents phases",
        ],
        "prereqs": "None — read before any phase, or keep open as a reference.",
        "next": "Return to your current learning phase.",
    },
    {
        "dir": "24-advanced-deep-learning",
        "hub": "24-advanced-deep-learning.ipynb",
        "title": "Advanced Deep Learning",
        "status": "complete",
        "description": "GANs, VAEs, diffusion models, graph neural networks, vision transformers, meta-learning, and interpretability.",
        "topics": [
            "Generative models: GANs, VAEs, normalising flows, diffusion",
            "Graph neural networks and geometric deep learning",
            "Vision transformers (ViT) and advanced transformer variants",
            "Meta-learning, neural architecture search, and interpretability",
        ],
        "prereqs": "[06-neural-networks/README.md](../06-neural-networks/README.md) · [03-maths/README.md](../03-maths/README.md)",
        "next": "[25-reinforcement-learning/README.md](../25-reinforcement-learning/README.md)",
    },
    {
        "dir": "25-reinforcement-learning",
        "hub": "25-reinforcement-learning.ipynb",
        "title": "Reinforcement Learning",
        "status": "complete",
        "description": "MDPs, Q-learning, DQN, policy gradients, and multi-agent RL — from theory to game-playing and robotics.",
        "topics": [
            "Markov Decision Processes and Bellman equations",
            "Value-based methods: Q-learning, SARSA, DQN",
            "Policy-based methods: REINFORCE, A2C, PPO",
            "Multi-agent RL, hierarchical RL, and inverse RL",
        ],
        "prereqs": "[06-neural-networks/README.md](../06-neural-networks/README.md) · [03-maths/README.md](../03-maths/README.md)",
        "next": "[26-time-series-analysis/README.md](../26-time-series-analysis/README.md)",
    },
    {
        "dir": "26-time-series-analysis",
        "hub": "26-time-series-analysis.ipynb",
        "title": "Time Series Analysis & Forecasting",
        "status": "complete",
        "description": "ARIMA, Prophet, LSTM, and transformer-based forecasting — from classical statistics to deep learning for temporal data.",
        "topics": [
            "Time series fundamentals: stationarity, autocorrelation, seasonality",
            "Classical methods: ARIMA, SARIMA, exponential smoothing",
            "Facebook Prophet for trend and seasonality modelling",
            "Deep learning: LSTM, GRU, temporal CNN, and transformer forecasters",
        ],
        "prereqs": "[02-data-science/README.md](../02-data-science/README.md) · [03-maths/README.md](../03-maths/README.md)",
        "next": "[27-causal-inference/README.md](../27-causal-inference/README.md)",
    },
    {
        "dir": "27-causal-inference",
        "hub": "27-causal-inference.ipynb",
        "title": "Causal Inference",
        "status": "developing",
        "description": "Distinguishing correlation from causation — RCTs, propensity scoring, instrumental variables, and causal ML.",
        "topics": [
            "Causal graphs (DAGs) and counterfactual reasoning",
            "RCTs, matching methods, and propensity score estimation",
            "Instrumental variables and regression discontinuity",
            "Causal machine learning and heterogeneous treatment effects",
        ],
        "prereqs": "[02-data-science/README.md](../02-data-science/README.md) · [03-maths/README.md](../03-maths/README.md)",
        "next": "[28-practical-data-science/README.md](../28-practical-data-science/README.md)",
    },
    {
        "dir": "28-practical-data-science",
        "hub": "28-practical-data-science.ipynb",
        "title": "Practical Data Science",
        "status": "complete",
        "description": "Interview preparation, end-to-end projects, and applied workflows across CV, NLP, ML, SQL, and time series.",
        "topics": [
            "Data science interview prep: statistics, ML, SQL, and coding",
            "End-to-end project workflows with real datasets",
            "Applied tracks: computer vision, NLP, recommender systems, causal ML",
            "MLOps and statistics for production data scientists",
        ],
        "prereqs": "Phases 00–16 complete.",
        "next": "[29-ai-hardware-llm-validation/README.md](../29-ai-hardware-llm-validation/README.md)",
    },
    {
        "dir": "29-ai-hardware-llm-validation",
        "hub": "29-ai-hardware-llm-validation.ipynb",
        "title": "AI Hardware & Validation",
        "status": "complete",
        "description": "End-to-end validation for AI accelerators — hardware bring-up, kernel correctness, model performance, and datacenter-scale testing.",
        "topics": [
            "Hardware validation: power, thermals, memory, and stability",
            "Kernel correctness: GEMM, conv, attention, softmax, and layernorm",
            "Model performance benchmarking: throughput, TTFT, and latency",
            "Distributed training validation and datacenter observability",
            "Industry benchmarks: MLPerf, AA-SLT, and LMSys Arena",
        ],
        "prereqs": "[06-neural-networks/README.md](../06-neural-networks/README.md) · [09-mlops/README.md](../09-mlops/README.md) · Linux proficiency.",
        "next": "[30-inference-optimization/README.md](../30-inference-optimization/README.md)",
    },
    {
        "dir": "30-inference-optimization",
        "hub": "30-inference-optimization.ipynb",
        "title": "Inference Optimization",
        "status": "developing",
        "description": "KV cache, quantisation (AWQ/GPTQ/EXL2), speculative decoding, and high-throughput serving with vLLM and TensorRT-LLM.",
        "topics": [
            "PagedAttention and KV cache management",
            "Quantisation: AWQ, GPTQ, EXL2, GGUF, and FP8",
            "Serving runtimes: vLLM, TensorRT-LLM, SGLang, and TGI",
            "Speculative decoding and continuous batching",
        ],
        "prereqs": "[14-local-llms/README.md](../14-local-llms/README.md) · [04-token/README.md](../04-token/README.md)",
        "next": "[09-mlops/README.md](../09-mlops/README.md) or [29-ai-hardware-llm-validation/README.md](../29-ai-hardware-llm-validation/README.md)",
    },
    {
        "dir": "31-ai-powered-dev-tools",
        "hub": "31-ai-powered-dev-tools.ipynb",
        "title": "AI-Powered Development Tools",
        "status": "complete",
        "description": "GitHub Copilot agent mode, MCP servers, custom instructions, and AI-native VS Code workflows.",
        "topics": [
            "Copilot completions, chat, and agent mode",
            "MCP (Model Context Protocol) server configuration and building",
            "Custom instructions: `.github/copilot-instructions.md`, `.instructions.md`, `.prompt.md`",
            "Model routing between GPT-4o, Claude, o3, and Gemini",
        ],
        "prereqs": "Phases 00–08 complete · Python · VS Code.",
        "next": "[32-cheatsheets/README.md](../32-cheatsheets/README.md)",
    },
    {
        "dir": "32-cheatsheets",
        "hub": "32-cheatsheets.ipynb",
        "title": "Cheatsheets",
        "status": "complete",
        "description": "Quick-reference guides for Docker, Kubernetes, Git, GitHub Actions, cloud CLIs, Linux, and AI/ML DevOps.",
        "topics": [
            "Docker, Kubernetes, and container orchestration commands",
            "Git, GitHub CLI, and GitHub Actions CI/CD",
            "AWS, Azure, GCP CLI commands and Terraform",
            "Linux, shell scripting, SQL, and monitoring (Prometheus/Grafana)",
            "Cloud DevOps for AI/ML: MLOps, GPU compute, model serving",
        ],
        "prereqs": "None — use as a quick reference at any time.",
        "next": "[33-roadmaps/README.md](../33-roadmaps/README.md)",
    },
    {
        "dir": "33-roadmaps",
        "hub": None,
        "title": "Learning Roadmaps",
        "status": "developing",
        "description": "Visual curriculum diagrams and learning roadmaps for the full Zero to AI journey.",
        "topics": [
            "Overview roadmap: full curriculum flow from Foundations to Production",
            "Core systems: tokenisation → embeddings → neural networks → RAG",
            "Advanced topics: agents, multimodal, fine-tuning, safety",
            "End-to-end flows: data ingestion to deployed AI product",
        ],
        "prereqs": "None — use at any point for orientation.",
        "next": "Start from [00-course-setup/README.md](../00-course-setup/README.md) or your chosen entry phase.",
    },
]

STATUS_BADGE = {
    "complete": "![Status: complete](https://img.shields.io/badge/status-complete-brightgreen)",
    "developing": "![Status: developing](https://img.shields.io/badge/status-developing-yellow)",
    "intro": "![Status: intro](https://img.shields.io/badge/status-intro-orange)",
}


def build_readme(s: dict) -> str:
    hub_line = (
        f"Open [`{s['hub']}`](./{s['hub']}) for learning objectives, "
        "prerequisites, and recommended reading order."
        if s["hub"]
        else "Browse the sub-folders below for visual roadmap notebooks."
    )
    topics_md = "\n".join(f"- {t}" for t in s["topics"])
    badge = STATUS_BADGE[s["status"]]
    return f"""# {s["title"]}

> {s["description"]}

{badge}

{hub_line}

## Topics Covered

{topics_md}

## Prerequisites

{s["prereqs"]}

## What Comes Next

{s["next"]}
"""


def main():
    created = 0
    skipped = 0
    for s in SECTIONS:
        path = os.path.join(BASE, s["dir"], "README.md")
        if os.path.exists(path):
            print(f"SKIP  {s['dir']}/README.md (already exists)")
            skipped += 1
            continue
        content = build_readme(s)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"WROTE {s['dir']}/README.md")
        created += 1
    print(f"\nDone — {created} created, {skipped} skipped.")


if __name__ == "__main__":
    main()
