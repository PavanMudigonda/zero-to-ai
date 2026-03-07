# AI Model Landscape: March 6, 2026

A comprehensive reference for learners navigating the rapidly evolving AI ecosystem.
Use this guide to understand which models, tools, and techniques are worth your time right now.

---

## Table of Contents

1. [Frontier Closed Models](#1-frontier-closed-models-march-2026)
2. [Best Open-Weight Models](#2-best-open-weight-models-march-2026)
3. [Best Models for Fine-tuning](#3-best-models-for-fine-tuning-march-2026)
4. [Key Training Techniques](#4-key-training-techniques-2025-2026)
5. [Key Infrastructure](#5-key-infrastructure-2025-2026)
6. [What Changed Since February 2026](#6-what-changed-since-february-2026)
7. [Learning Path for March 2026](#7-what-to-learn-in-what-order)

---

## 1. Frontier Closed Models (March 2026)

These are the state-of-the-art proprietary models available via API. You cannot download or fine-tune them directly, but they set the performance ceiling that open-weight models are converging toward.

### GPT-5.2 (OpenAI)

- **Context window**: 400,000 tokens (~300 pages of text)
- **Benchmark**: 100% on AIME 2025 math competition problems
- **Multimodal**: text, images, code, structured data
- **API**: `gpt-5.2` via OpenAI API
- **Pricing**: ~$15/1M input tokens, ~$60/1M output tokens
- **Best for**: complex reasoning, long-document analysis, highest-stakes tasks
- **Note**: the most capable model available as of Feb 2026; use when quality matters more than cost

### o3 / o4-mini (OpenAI — Reasoning Models)

- **Architecture**: inference-time compute scaling ("thinking" before answering)
- **o3**: flagship reasoning model; best at math, science, coding competitions
- **o4-mini**: much cheaper than o3, retains most reasoning capability
- **Context**: 200K tokens (o3), 128K tokens (o4-mini)
- **Use case**: problems that benefit from step-by-step chain-of-thought reasoning
- **Limitation**: slower than standard models (generates reasoning traces internally)
- **Best for**: theorem proving, complex code debugging, multi-step planning

### Claude 3.7 (Anthropic)

- **Key feature**: extended thinking mode — can spend more tokens "thinking" before responding
- **Context**: 200,000 tokens
- **Strengths**: long document analysis, nuanced instruction following, coding, safety
- **Extended thinking**: toggleable; dramatically improves accuracy on hard problems
- **API**: `claude-3-7-sonnet-20250219` via Anthropic API or Amazon Bedrock
- **Best for**: enterprise tasks requiring careful instruction following, long-context analysis

### Gemini 3.1 Pro (Google)

- **Context window**: 1,000,000 tokens (largest among frontier models)
- **Multimodal**: text, images, video, audio, code — native
- **Strengths**: 1M context for entire codebases or video analysis, strong multilingual performance
- **API**: `gemini-3.1-pro` via Google AI Studio / Vertex AI
- **Best for**: video understanding, massive codebase analysis, multimodal applications

### Mistral Large 3 (Mistral AI)

- **Architecture**: 675B parameter Mixture-of-Experts (MoE)
- **Active parameters**: ~45B activated per forward pass (sparse MoE)
- **Cost**: approximately 15% the cost of GPT-5.2 at equivalent quality for most tasks
- **Context**: 128K tokens
- **Strengths**: European GDPR compliance, strong multilingual, cost-efficient
- **API**: `mistral-large-latest` via Mistral AI platform (la Plateforme)
- **Best for**: cost-sensitive production workloads where GPT-5.2 quality is not required

### Quick Comparison

| Model | Context | Strengths | Relative Cost |
|-------|---------|-----------|---------------|
| GPT-5.2 (OpenAI) | 400K | All-around best, 100% AIME 2025 | Highest |
| o3 (OpenAI) | 200K | Math, science, reasoning | Very High |
| o4-mini (OpenAI) | 128K | Reasoning, cost-efficient | Medium |
| Claude 3.7 (Anthropic) | 200K | Long docs, instruction following | High |
| Gemini 3.1 Pro (Google) | 1M | Video, multimodal, massive context | High |
| Mistral Large 3 (Mistral) | 128K | Cost-efficient, multilingual, GDPR | Low-Medium |

---

## 2. Best Open-Weight Models (March 2026)

Open-weight models can be downloaded, self-hosted, fine-tuned, and run privately. The gap with closed models has narrowed dramatically.

### Llama 4 Maverick / Scout (Meta)

- **Maverick**: 400B parameter MoE; flagship, matches GPT-5.2 on most benchmarks
- **Scout**: 17B active / 109B total MoE; fastest, designed for edge deployment
- **Context**: up to 10,000,000 tokens (10M — industry record for open-weight)
- **Multimodal**: native image and text understanding
- **License**: Llama 4 Community License (commercial use permitted with restrictions)
- **Download**: `meta-llama/Llama-4-Maverick`, `meta-llama/Llama-4-Scout`
- **Best for**: the best open-weight option when you need top-tier quality; RAG with very long contexts

### Qwen 3 235B-A22B (Alibaba)

- **Architecture**: 235B total / 22B active parameters (MoE)
- **Key feature**: hybrid thinking/non-thinking mode — toggle chain-of-thought per request
- **Benchmark**: best open-source model overall as of Feb 2026 on most standard benchmarks
- **Context**: 128K tokens
- **License**: Apache 2.0 (fully permissive commercial use)
- **Download**: `Qwen/Qwen3-235B-A22B`
- **Best for**: production OSS deployments where quality is top priority; reasoning tasks
- **Note**: the 22B active parameter count means inference cost is much lower than the 235B total suggests

### DeepSeek R1 (DeepSeek)

- **Architecture**: 671B MoE with 37B active parameters; trained end-to-end with GRPO reinforcement learning
- **Training cost**: approximately $6 million — a landmark efficiency achievement
- **Specialization**: reasoning, mathematics, coding, scientific problems
- **Context**: 128K tokens
- **License**: MIT (fully permissive, including fine-tuning and commercial use)
- **Download**: `deepseek-ai/DeepSeek-R1`
- **Also available**: DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B (distilled smaller versions)
- **Best for**: reasoning-heavy tasks; studying how to train reasoning models (RL with GRPO)

### DeepSeek V3.2 (DeepSeek)

- **Architecture**: 685B MoE (37B active); successor to DeepSeek V3
- **Strengths**: strongest base model for general-purpose tasks from DeepSeek
- **License**: MIT
- **Download**: `deepseek-ai/DeepSeek-V3`
- **Best for**: base model fine-tuning for general applications when maximum capability is needed

### Gemma 3 27B (Google)

- **Context**: 128K tokens
- **Languages**: 140+ languages natively supported
- **Hardware**: fits on a single consumer GPU (RTX 4090 24GB with quantization)
- **License**: Gemma Terms of Use (permissive commercial use)
- **Download**: `google/gemma-3-27b-it`
- **Key feature**: among the most capable models that fit on a single GPU
- **Best for**: multilingual applications; single-GPU production deployment; fine-tuning on consumer hardware

### Phi-4 (Microsoft)

- **Size**: 14B parameters
- **Specialization**: STEM — math, science, coding; trained on high-quality synthetic data
- **License**: MIT (fully permissive)
- **Download**: `microsoft/phi-4`
- **Strengths**: punches far above its weight on reasoning and math; excellent for structured outputs
- **Best for**: math tutoring, code generation, scientific Q&A; fine-tuning when training compute is limited

### Phi-4-mini (Microsoft)

- **Size**: 3.8B parameters
- **License**: MIT
- **Download**: `microsoft/phi-4-mini`
- **Best for**: on-device inference, mobile, or when you need a capable small model

### Quick Comparison

| Model | Params (active) | Context | License | Best For |
|-------|----------------|---------|---------|----------|
| Llama 4 Maverick | 400B MoE | 10M | Llama 4 | Top quality, ultra-long context |
| Llama 4 Scout | 17B active | 10M | Llama 4 | Fast, long-context, edge |
| Qwen 3 235B-A22B | 22B active | 128K | Apache 2.0 | Best OSS overall |
| DeepSeek R1 | 37B active | 128K | MIT | Reasoning, math, coding |
| DeepSeek V3.2 | 37B active | 128K | MIT | General base model |
| Gemma 3 27B | 27B | 128K | Gemma ToU | Single GPU, multilingual |
| Phi-4 | 14B | 16K | MIT | STEM, math, coding |
| Phi-4-mini | 3.8B | 16K | MIT | On-device, mobile |

---

## 3. Best Models for Fine-tuning (March 2026)

Not all open-weight models are equally good starting points for fine-tuning. These are the recommended choices grouped by compute budget.

### Small Models (less than 8B parameters)

Best when you have limited GPU memory (less than 24GB) or need fast inference.

| Model | Params | License | Why Fine-tune It |
|-------|--------|---------|-----------------|
| Qwen2.5-7B-Instruct | 7B | Apache 2.0 | Best quality in class, excellent instruction following, tokenizer supports 100+ languages |
| Llama 3.2 3B | 3B | Llama 3.2 | Meta's smallest capable model; fast inference; widely supported |
| Phi-4-mini | 3.8B | MIT | Strong reasoning for size; MIT license; good for STEM tasks |
| Gemma 3 4B | 4B | Gemma ToU | Google quality at 4B; 128K context; good multilingual |

**Recommended starter**: `Qwen/Qwen2.5-7B-Instruct` — best quality, Apache 2.0 license, great tokenizer.

### Medium Models (8B to 14B parameters)

Good balance of quality and fine-tuning cost. Fits in 24GB GPU with QLoRA.

| Model | Params | License | Why Fine-tune It |
|-------|--------|---------|-----------------|
| Phi-4 | 14B | MIT | Best STEM/reasoning quality at 14B; MIT license |
| Qwen2.5-14B-Instruct | 14B | Apache 2.0 | Strong across all domains; excellent for structured output fine-tuning |
| Gemma 3 12B | 12B | Gemma ToU | Google quality, 128K context; solid multilingual support |

**Recommended starter**: `microsoft/phi-4` for STEM/coding tasks; `Qwen/Qwen2.5-14B-Instruct` for general tasks.

### Large Models (32B and above)

Requires multi-GPU or A100/H100 for fine-tuning. Produces the highest-quality specialized models.

| Model | Params | License | Why Fine-tune It |
|-------|--------|---------|-----------------|
| Qwen2.5-32B-Instruct | 32B | Apache 2.0 | Best quality at 32B; fits on 2x A100 with QLoRA |
| Llama 3.3 70B | 70B | Llama 3.3 | Meta's most capable dense model; widely supported by fine-tuning tooling |
| DeepSeek R1 70B Distill | 70B | MIT | Distilled from DeepSeek R1; strong reasoning; MIT license |

**Recommended starter**: `Qwen/Qwen2.5-32B-Instruct` if you have 2x A100; `meta-llama/Llama-3.3-70B-Instruct` for the widest tooling support.

### Fine-tuning Model Selection Decision Tree

```
Do you have > 2x A100/H100?
  Yes -> Qwen2.5-32B or Llama 3.3 70B
  No  -> Single A100/H100 (80GB)?
           Yes -> Qwen2.5-14B or Phi-4 (with QLoRA)
           No  -> Single 24GB GPU (e.g. RTX 4090)?
                    Yes -> Qwen2.5-7B or Phi-4-mini (QLoRA)
                    No  -> Phi-4-mini or Llama 3.2 3B (4-bit QLoRA)

Is your task math/coding/STEM?
  Yes -> Prefer Phi-4 or DeepSeek R1 distilled variants

Do you need Apache 2.0 / MIT license?
  Yes -> Qwen2.5 (Apache 2.0) or Phi-4 / DeepSeek R1 (MIT)
  -> Avoid Llama 4 / Gemma (more restrictive licenses)
```

---

## 4. Key Training Techniques (2025-2026)

### GRPO — Group Relative Policy Optimization

- **What it is**: A reinforcement learning algorithm for training reasoning models without a critic network.
- **Why it matters**: DeepSeek R1 was trained with GRPO, achieving o1-level reasoning at a fraction of the cost. GRPO samples multiple responses per prompt and uses group-relative rewards instead of a value function baseline.
- **Advantage over PPO**: no separate critic model needed (halves training memory); more stable for LLM RLHF.
- **Implementation**: available in TRL (`trl.GRPOTrainer`) and Unsloth.
- **Use when**: training reasoning/math models from scratch or fine-tuning with RL-based feedback.

### LoRA / QLoRA / DoRA / RSLoRA

Parameter-efficient fine-tuning (PEFT) methods that update only a small fraction of model parameters.

| Method | Description | When to Use |
|--------|-------------|-------------|
| **LoRA** | Low-Rank Adapters: insert small A*B matrices alongside frozen weights | Standard fine-tuning; 2-5% of params |
| **QLoRA** | LoRA on top of 4-bit quantized base model | Limited GPU memory (fits 70B in 48GB) |
| **DoRA** | Decomposed LoRA: separates magnitude and direction updates | When LoRA underfits; slightly better quality |
| **RSLoRA** | Rank-Stabilized LoRA: scales learning rates by sqrt(rank) | High-rank LoRA (r>=64) for better stability |

**Current best practice**: QLoRA with rsLoRA scaling and rank=16-64 for most fine-tuning tasks.

### DPO / SimPO / KTO — Alignment Without PPO

Methods for aligning model outputs to human preferences without the complexity of PPO.

| Method | Description | When to Use |
|--------|-------------|-------------|
| **DPO** (Direct Preference Optimization) | Fine-tune on (chosen, rejected) pairs directly | Standard alignment; simplest setup |
| **SimPO** (Simple Preference Optimization) | DPO variant with length normalization and margin reward | Better than DPO for instruction following |
| **KTO** (Kahneman-Tversky Optimization) | Works with binary feedback (good/bad) rather than pairs | When you have binary labels, not ranked pairs |

**Current best practice**: SimPO slightly outperforms DPO in most benchmarks; KTO if you only have thumbs-up/thumbs-down data.

### Unsloth — 2-5x Faster Fine-tuning

- **What it is**: A library that rewrites CUDA kernels for transformer operations to be more memory-efficient and faster.
- **Speedup**: 2-5x faster training vs standard Hugging Face + PEFT; 50-70% less GPU memory.
- **Integration**: drop-in replacement for Hugging Face `AutoModelForCausalLM.from_pretrained`.
- **Supports**: LoRA, QLoRA, DoRA, GRPO, DPO, SFT; works with Qwen, Llama, Mistral, Phi, Gemma.
- **Install**: `pip install unsloth`

```python
# Unsloth replaces the standard HF model loading
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="Qwen/Qwen2.5-7B-Instruct",
    max_seq_length=8192,
    load_in_4bit=True,          # QLoRA
)
model = FastLanguageModel.get_peft_model(
    model,
    r=16,                        # LoRA rank
    lora_alpha=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    use_rslora=True,             # RSLoRA scaling
)
```

---

## 5. Key Infrastructure (2025-2026)

### Inference Engines (ranked by throughput)

**SGLang > vLLM > TGI > Ollama / llama.cpp**

| Tool | Throughput | Best For | Install |
|------|-----------|----------|---------|
| **SGLang** | Highest (~16,200 tok/s H100) | Production API, RAG, agents — RadixAttention caches shared prefixes | `pip install sglang[all]` |
| **vLLM** | Very High (~12,500 tok/s H100) | Production API, multi-LoRA serving, AMD support | `pip install vllm` |
| **TGI** | High (~9,800 tok/s H100) | HuggingFace ecosystem, Inference Endpoints | Docker |
| **Ollama** | Medium | Local dev, Apple Silicon, edge, no GPU | Single binary |
| **llama.cpp** | Low-Medium | Embedded, CPU-only, maximum portability | Compile from source |

**Key 2025-2026 development**: SGLang's RadixAttention provides automatic KV cache reuse for shared prefixes (system prompts, RAG context, few-shot examples). For agent and RAG workloads, this means 5-10x faster time-to-first-token after the first request.

### Fine-tuning Frameworks (ranked by efficiency)

**Unsloth > Axolotl > standard TRL**

| Tool | Speedup | Best For |
|------|---------|----------|
| **Unsloth** | 2-5x faster, 50-70% less memory | Most fine-tuning tasks; LoRA, QLoRA, GRPO, DPO |
| **Axolotl** | 1.5-2x (config-driven) | Teams that prefer YAML config over code; multi-GPU |
| **TRL (HuggingFace)** | Baseline | Reference implementation; maximum compatibility |

### Agent Frameworks (2025-2026)

The agent ecosystem has consolidated around a few dominant tools:

| Tool | Description | Best For |
|------|-------------|----------|
| **MCP (Model Context Protocol)** | Anthropic's open standard for connecting LLMs to tools/data sources | Universal tool/plugin standard; works across Claude, GPT, open models |
| **OpenAI Agents SDK** | Official SDK for building multi-agent systems; includes tracing and handoffs | Production agents with OpenAI models; clean abstraction |
| **LangGraph 1.0** | Graph-based agent orchestration with persistent state | Complex multi-step agents, branching workflows, stateful agents |
| **LlamaIndex Workflows** | Event-driven agent workflows | RAG-heavy agents, document pipelines |

**Key insight**: MCP has become the standard "USB for AI tools" — build MCP servers once, connect to any MCP-compatible agent framework. In 2026, most enterprise tools (databases, APIs, file systems) have MCP servers available.

### Vector Databases (2025-2026)

| Database | Description | Best For |
|----------|-------------|----------|
| **Pinecone** | Managed cloud vector DB; serverless tier available | Production SaaS; zero ops overhead |
| **Qdrant** | Rust-based, high performance; excellent filtering | Self-hosted production; best performance/cost ratio |
| **Chroma** | Rewritten in Rust (2025); much faster than original Python | Local dev and small-medium production; easiest setup |
| **pgvector** | Postgres extension; vectors + SQL in one database | Existing Postgres users; no separate infrastructure |
| **Weaviate** | Feature-rich; built-in hybrid search (BM25 + vector) | Hybrid search requirements; GraphQL API |

**Current recommendation**: Chroma for development (easiest), Qdrant for self-hosted production (best performance), pgvector if you already run Postgres.

---

## 6. What Changed Since February 2026

This section captures practical updates since the February snapshot so learners can prioritize what changed.

### Model Selection Updates (March 2026)

- **Reasoning-first routing is now standard**: use reasoning models (`o3`, `o4-mini`, DeepSeek R1 family) for math/coding/planning tasks; use standard chat models for latency-sensitive UX.
- **Very-long-context workflows matured**: 1M+ token workflows are increasingly practical for repository analysis, long legal docs, and multimodal audit pipelines.
- **Open-weight quality ceiling improved**: Qwen3, Llama 4, and DeepSeek families are now viable for many production tasks that previously required frontier APIs.
- **License-aware model choice is now mandatory**: teams increasingly split by policy: Apache/MIT-first stacks for commercial redistribution, and restricted-license stacks for internal-only deployments.

### Training and Alignment Updates (March 2026)

- **SimPO and DPO remain default alignment baselines** for most teams; PPO-style stacks are mostly reserved for specialized research workflows.
- **GRPO adoption increased** for reasoning-tuned models and synthetic curriculum training.
- **Unsloth + TRL became a common default** for small/medium fine-tuning projects due to speed and memory efficiency.

### Inference and Agent Stack Updates (March 2026)

- **SGLang and vLLM remain the top two production inference choices**; SGLang keeps an edge in high-throughput agent/RAG workloads with shared-prefix caching.
- **MCP solidified as the cross-vendor tool protocol** in agent ecosystems.
- **LangGraph + OpenAI Agents SDK + MCP** is a common production architecture for stateful, tool-using systems.

### March 2026 Practical Defaults

| Layer | March 2026 Default Recommendation |
|------|------------------------------------|
| Fast API assistant | `o4-mini` / Claude Sonnet class |
| Hard reasoning | `o3` / DeepSeek R1 |
| Open-weight general | Qwen3 235B-A22B |
| Open-weight long context | Llama 4 Maverick/Scout |
| Small local model | Phi-4-mini / Gemma 3 4B |
| Fine-tuning starter | Qwen2.5-7B + QLoRA + RSLoRA |
| Inference server | SGLang (prod) / Ollama (local dev) |
| Agent runtime | LangGraph + MCP + OpenAI Agents SDK |

---

## 7. What to Learn in What Order

A structured learning path for March 2026. Follow this order to build solid foundations before tackling advanced topics.

### Phase 1: Foundations (Weeks 1-4)

**Goal**: Understand what LLMs are and how to use them via API.

1. **Python for AI** — numpy, pandas, matplotlib basics; Jupyter notebooks
2. **Prompt engineering** — zero-shot, few-shot, chain-of-thought; system prompts
3. **OpenAI / Anthropic API** — calling GPT-5.2 and Claude 3.7; streaming; function calling
4. **Tokenization** — how text becomes tokens; tiktoken; why context window size matters
5. **RAG basics** — chunking documents, embedding models, Chroma, similarity search

**Milestone**: Build a document Q&A chatbot using RAG with a frontier API model.

### Phase 2: Open-Weight Models (Weeks 5-8)

**Goal**: Run and understand open-weight models locally and in the cloud.

1. **Hugging Face Transformers** — `pipeline`, `AutoModelForCausalLM`, `AutoTokenizer`
2. **Running models locally** — Ollama (easiest), then llama.cpp
3. **Quantization** — understand BF16 vs GPTQ vs AWQ vs GGUF; trade-offs
4. **Chat templates** — ChatML, Llama 3 template, Qwen template; why they matter
5. **vLLM / SGLang** — run a production-grade API server; benchmark throughput
6. **Model selection** — when to use Qwen2.5-7B vs Llama 4 vs Gemma 3; the decision tree above

**Milestone**: Self-host a Qwen2.5-7B model via SGLang and serve it behind a FastAPI endpoint.

### Phase 3: Fine-tuning (Weeks 9-14)

**Goal**: Adapt pre-trained models to specific tasks.

1. **Dataset preparation** — instruction format, chat format; quality over quantity
2. **LoRA fundamentals** — what low-rank adapters do mathematically; rank, alpha, target modules
3. **QLoRA with Unsloth** — fine-tune a 7B model in under 4GB VRAM
4. **SFT (Supervised Fine-Tuning)** — `SFTTrainer` from TRL; data formatting; evaluation during training
5. **DPO / SimPO alignment** — preference datasets; `DPOTrainer`; when to align vs just SFT
6. **GRPO for reasoning** — training a model to think step-by-step with RL
7. **Evaluation** — ROUGE, BERTScore, LLM-as-judge; avoiding eval data contamination

**Milestone**: Fine-tune Qwen2.5-7B on a domain-specific dataset, align with DPO, and evaluate with an LLM judge.

### Phase 4: Agents and Advanced RAG (Weeks 15-20)

**Goal**: Build production-grade agentic systems.

1. **Function calling / tool use** — structured outputs, JSON mode; tool definitions
2. **ReAct agents** — Reason + Act loop; building with OpenAI Agents SDK
3. **MCP (Model Context Protocol)** — write an MCP server; connect to Claude Desktop / your agent
4. **Advanced RAG** — hybrid search, reranking (ColBERT, cross-encoders), HyDE, RAPTOR
5. **LangGraph 1.0** — stateful agents, branching workflows, multi-agent handoffs
6. **Agentic evaluation** — trajectory evaluation; tool use accuracy; multi-turn benchmarks

**Milestone**: Build a multi-step research agent using LangGraph + MCP that can search the web, read documents, and write structured reports.

### Phase 5: Production and MLOps (Weeks 21-24)

**Goal**: Deploy and maintain AI systems reliably.

1. **Docker + GPU deployment** — containerizing vLLM/SGLang; docker-compose with GPU support
2. **Monitoring** — structured logging; latency p95/p99; token usage; refusal rate
3. **Cost optimization** — quantization trade-offs; batching strategies; spot vs on-demand pricing
4. **Continuous evaluation** — A/B testing model updates; production feedback loops
5. **Security** — prompt injection defense; PII detection; rate limiting; API key management
6. **MLflow / Weights & Biases** — experiment tracking; model registry; deployment tracking

**Milestone**: Deploy your fine-tuned model to a cloud GPU with monitoring, a Docker container, cost tracking, and an A/B testing setup for comparing model versions.

---

### Summary: The 2026 AI Engineer Stack

```
Layer               Tools (March 2026 Best Choices)
---------           ------------------------------
Frontier APIs       GPT-5.2, Claude 3.7, Gemini 3.1 Pro
Open Models         Qwen3 235B-A22B, Llama 4 Maverick, DeepSeek R1
Fine-tuning Base    Qwen2.5-7B (small), Phi-4 (medium), Qwen2.5-32B (large)
Fine-tuning Tools   Unsloth + TRL (SFT/DPO/GRPO)
Inference           SGLang (production), Ollama (local/dev)
Agents              MCP + OpenAI Agents SDK + LangGraph 1.0
Vector DB           Qdrant (production), Chroma (dev), pgvector (Postgres users)
Experiment Tracking Weights & Biases or MLflow
Observability       Langfuse (open source) or LangSmith
```

The pace of change in this field is fast, but the underlying principles — retrieval, fine-tuning, alignment, evaluation, deployment — remain stable. Master the fundamentals and you will adapt quickly as the specific tools evolve.
