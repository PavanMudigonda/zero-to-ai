#!/usr/bin/env python3
"""
Update learning materials based on Artificial Analysis data (April 2026).
Updates model landscape, reasoning models, open source overview, and related notebooks.
"""
import json
import os
import shutil
from pathlib import Path

ROOT = Path("/Users/pavanmudigonda/code/zero-to-ai")
NB_DIR = ROOT / "jupyter-notebooks"
DOCS_DIR = ROOT / "next-docs" / "src" / "app"

# ─────────────────────────────────────────────────────────────
# 1. MODEL LANDSCAPE NOTEBOOK - full cell 0 rewrite
# ─────────────────────────────────────────────────────────────

MODEL_LANDSCAPE_MARKDOWN = r"""# AI Model Landscape: April 27, 2026

A comprehensive reference for learners navigating the rapidly evolving AI ecosystem.
Use this guide to understand which models, tools, and techniques are worth your time right now.

> **Data source**: rankings, pricing, and speed figures come from [Artificial Analysis](https://artificialanalysis.ai/) - an independent benchmarking service that evaluates 499+ models with its Intelligence Index v4.0.4 (10 evaluations: GDPval-AA, τ²-Bench Telecom, Terminal-Bench Hard, SciCode, AA-LCR, AA-Omniscience, IFBench, Humanity's Last Exam, GPQA Diamond, CritPt).

---

## Table of Contents

1. [Frontier Closed Models](#1-frontier-closed-models-april-2026)
2. [Best Open-Weight Models](#2-best-open-weight-models-april-2026)
3. [Best Models for Fine-tuning](#3-best-models-for-fine-tuning-april-2026)
4. [Key Training Techniques](#4-key-training-techniques-2025-2026)
5. [Key Infrastructure](#5-key-infrastructure-2025-2026)
6. [What Changed Since March 2026](#6-what-changed-since-march-2026)
7. [Learning Path for April 2026](#7-what-to-learn-in-what-order)

---

## 1. Frontier Closed Models (April 2026)

These are the state-of-the-art proprietary models available via API. You cannot download or fine-tune them directly, but they set the performance ceiling that open-weight models are converging toward.

### GPT-5.5 (OpenAI) - NEW #1

- **Released**: April 2026
- **Context window**: 922,000 tokens (922K)
- **Intelligence Index**: **60** (#1 overall) - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing**: ~$11.25/1M tokens (blended)
- **Output speed**: 72 tokens/sec
- **Variants**: GPT-5.5 (xhigh), GPT-5.5 (high, score 59), GPT-5.5 (medium, score 57), GPT-5.5 (low, score 51), GPT-5.5 (Non-reasoning, score 41)
- **Key advance**: highest intelligence score ever measured; continues OpenAI's effort-scaling approach with xhigh/high/medium/low tiers
- **Best for**: highest-stakes tasks requiring maximum intelligence; complex reasoning, analysis

### GPT-5.4 (OpenAI)

- **Context window**: 1,050,000 tokens (1.05M)
- **Intelligence Index**: **57** (#2 tied) - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing**: ~$5.63/1M tokens (blended); $2.50/1M input, $15.00/1M output
- **Output speed**: 80 tokens/sec
- **Variants**: GPT-5.4 (xhigh), GPT-5.4 mini (xhigh, score 49, $1.69/1M), GPT-5.4 nano (xhigh, score 44, $0.46/1M)
- **Multimodal**: text, images, code, structured data; native computer use
- **Key feature**: **tool search** - model dynamically looks up tool definitions at inference time
- **Best for**: complex reasoning, agentic workflows, long-document analysis

### Claude Opus 4.7 (Anthropic) - NEW

- **Context window**: 1,000,000 tokens (1M)
- **Intelligence Index**: **57** (#2 tied) - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing**: ~$10.00/1M tokens (blended)
- **Output speed**: 48 tokens/sec
- **Key advance**: successor to Opus 4.6; top-tier coding, agent workflows, and analysis
- **Best for**: teams needing maximum coding quality and instruction-following

### Claude Sonnet 4.6 (Anthropic)

- **Intelligence Index**: **52** (max effort) - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Context window**: 1,000,000 tokens (1M)
- **Pricing**: ~$6.00/1M tokens (blended)
- **Output speed**: 58 tokens/sec
- **Best for**: balanced quality & speed; production coding assistants

### Claude 4.5 Haiku (Anthropic)

- **Intelligence Index**: **37** (reasoning) - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing**: ~$2.00/1M tokens (blended)
- **Output speed**: 98 tokens/sec
- **Best for**: fast, cost-effective tasks; high-volume applications

### Gemini 3.1 Pro Preview (Google) - Top Tier

- **Context window**: 1,000,000 tokens (1M)
- **Intelligence Index**: **57** (#2 tied) - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing**: ~$4.50/1M tokens (blended); $2.00/1M input, $12.00/1M output
- **Output speed**: 119 tokens/sec
- **Key advantage**: best intelligence-to-cost ratio among frontier models
- **Best for**: large-context analysis, multimodal applications, agentic workflows

### Gemini 3 Flash (Google)

- **Intelligence Index**: **46** - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing**: ~$1.13/1M tokens (blended)
- **Output speed**: 158 tokens/sec
- **Best for**: high-throughput production workloads where speed matters more than peak intelligence

### Grok 4.20 (xAI) - NEW

- **Context window**: 2,000,000 tokens (2M - largest context window)
- **Intelligence Index**: **49** - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing**: ~$3.00/1M tokens (blended)
- **Output speed**: 88 tokens/sec
- **Best for**: ultra-long context tasks; real-time information workflows

### Quick Comparison - Frontier Closed Models

| Model | Intelligence Index | Context | Price (blended/1M) | Speed (tok/s) | Best For |
|-------|-------------------|---------|-------------------|--------------|----------|
| GPT-5.5 (xhigh) | **60** (#1) | 922K | $11.25 | 72 | Maximum intelligence |
| Claude Opus 4.7 (max) | **57** (#2) | 1M | $10.00 | 48 | Coding, agents |
| Gemini 3.1 Pro Preview | **57** (#2) | 1M | $4.50 | 119 | Best value frontier |
| GPT-5.4 (xhigh) | **57** (#2) | 1.05M | $5.63 | 80 | Computer use, tool search |
| Claude Sonnet 4.6 (max) | **52** | 1M | $6.00 | 58 | Balanced quality/speed |
| GPT-5.4 mini (xhigh) | **49** | 400K | $1.69 | 146 | Cost-effective reasoning |
| Grok 4.20 v2 | **49** | 2M | $3.00 | 88 | Ultra-long context |
| Gemini 3 Flash | **46** | 1M | $1.13 | 158 | High throughput |
| GPT-5.4 nano (xhigh) | **44** | 400K | $0.46 | 167 | Budget reasoning |
| Claude 4.5 Haiku | **37** | 200K | $2.00 | 98 | Fast, affordable |

*Intelligence Index scores from [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models) - composite of 10 independent benchmarks ranking 499+ models.*

---

## 2. Best Open-Weight Models (April 2026)

Open-weight models can be downloaded, self-hosted, fine-tuned, and run privately. The gap with closed models has narrowed dramatically - the top open-weight model (Kimi K2.6) now scores within 6 points of GPT-5.5.

### Kimi K2.6 (Moonshot AI) - #1 Open-Weight

- **Intelligence Index**: **54** (#1 open-weight) - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing** (API): ~$1.71/1M tokens (blended)
- **Context**: 256K tokens
- **Key feature**: strong reasoning, multilingual, open weights with commercial use
- **Best for**: production deployments needing top open-weight quality

### MiMo-V2.5-Pro (Xiaomi) - #2 Open-Weight, NEW

- **Intelligence Index**: **54** (#2 open-weight, tied with K2.6) - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing** (API): ~$1.50/1M tokens (blended)
- **Context**: 1,000,000 tokens (1M)
- **Output speed**: 63 tokens/sec
- **Key feature**: Xiaomi's top-performing model; excellent quality at low cost
- **Best for**: cost-effective production with 1M context support

### DeepSeek V4 Pro / V4 Flash (DeepSeek) - NEW

- **V4 Pro (Max)**: Intelligence Index **52**, ~$2.17/1M tokens, 38 tok/s
- **V4 Flash (Max)**: Intelligence Index **47**, ~$0.17/1M tokens, 83 tok/s - exceptional value
- **Context**: 1,000,000 tokens (1M) for both
- **Key advance**: DeepSeek V4 generation marks a major quality leap; V4 Flash is one of the cheapest competitive models
- **Best for**: V4 Pro for quality, V4 Flash for budget production workloads

### Muse Spark (Meta) - NEW

- **Intelligence Index**: **52** - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Context**: 262K tokens
- **Key feature**: Meta's newest frontier-class open model
- **Best for**: high-quality open-weight deployment

### GLM-5.1 (Z AI) - Updated

- **Intelligence Index**: **51** (up from GLM-5 at 50) - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing** (API): ~$2.15/1M tokens (blended)
- **Output speed**: 51 tokens/sec
- **Context**: 200K tokens
- **Best for**: top-tier open-weight quality with strong Chinese language support

### MiniMax-M2.7 (MiniMax) - NEW

- **Intelligence Index**: **50** - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing**: ~$0.53/1M tokens (blended) - extremely affordable for its quality
- **Output speed**: 47 tokens/sec
- **Context**: 205K tokens
- **Best for**: budget production where quality still matters

### Qwen 3.5 / 3.6 Family (Alibaba) - Updated

- **Qwen3.6 Max Preview**: Intelligence Index **52**, ~$2.92/1M, 33 tok/s
- **Qwen3.5 397B-A17B**: Intelligence Index **45**, ~$1.35/1M, 52 tok/s
- **Key models**: Qwen3.6 Plus (score 50), Qwen3.5 122B-A10B (score 42), Qwen3.5 9B (score 32)
- **License**: Apache 2.0 lineage for core checkpoints
- **Best for**: one family spanning edge to high-end cluster deployments

### gpt-oss-120B / gpt-oss-20B (OpenAI) - NEW Open Source!

- **gpt-oss-120B (high)**: Intelligence Index **33**, ~$0.26/1M, 209 tok/s - blazing fast
- **gpt-oss-20B (high)**: Intelligence Index **24**, ~$0.10/1M, 273 tok/s - fastest model tested
- **Key breakthrough**: OpenAI's first open-source models! Available on 23 providers
- **License**: check OpenAI open source terms
- **Best for**: ultra-low-cost, high-speed production workloads; API provider competition

### NVIDIA Nemotron 3 Super (NVIDIA) - NEW

- **Intelligence Index**: **36** - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Pricing**: ~$0.41/1M tokens (blended)
- **Output speed**: 155 tokens/sec
- **Context**: 1M tokens
- **Best for**: fast, affordable inference; NVIDIA ecosystem integration

### Gemma 4 31B (Google) - Updated

- **Intelligence Index**: **39** (reasoning mode) - [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models)
- **Context**: 256K tokens
- **Key improvement**: major upgrade from Gemma 3; fits on a single consumer GPU with quantization
- **Best for**: single-GPU deployment, multilingual applications

### DeepSeek V3.2 / R1 (DeepSeek)

- **V3.2**: Intelligence Index **42**, ~$0.32/1M, 82 tok/s
- **R1**: remains strong for specialized reasoning tasks
- **License**: MIT (fully permissive)
- **Best for**: general base model tasks; reasoning research

### Llama 4 Maverick / Scout (Meta)

- **Maverick**: 400B parameter MoE; score 18; competitive on specific tasks
- **Scout**: 10M token context (industry record); score 14
- **License**: Llama 4 Community License
- **Best for**: ultra-long context workflows

### Quick Comparison - Open-Weight Models

| Model | Intelligence Index | Context | Price (blended/1M) | Speed (tok/s) | Best For |
|-------|-------------------|---------|-------------------|--------------|----------|
| Kimi K2.6 | **54** (#1 OW) | 256K | $1.71 | -- | Top open-weight quality |
| MiMo-V2.5-Pro | **54** (#2 OW) | 1M | $1.50 | 63 | Best value open-weight |
| DeepSeek V4 Pro (Max) | **52** | 1M | $2.17 | 38 | Quality reasoning |
| Muse Spark (Meta) | **52** | 262K | -- | -- | Meta's frontier open model |
| Qwen3.6 Max Preview | **52** | 256K | $2.92 | 33 | Alibaba ecosystem |
| GLM-5.1 | **51** | 200K | $2.15 | 51 | Chinese language support |
| MiniMax-M2.7 | **50** | 205K | $0.53 | 47 | Budget quality |
| DeepSeek V4 Flash (Max) | **47** | 1M | $0.17 | 83 | Cheapest competitive model |
| Qwen3.5 397B-A17B | **45** | 262K | $1.35 | 52 | Apache 2.0, broad sizes |
| DeepSeek V3.2 | **42** | 128K | $0.32 | 82 | General purpose, MIT |
| Gemma 4 31B | **39** | 256K | Free | 36 | Single GPU, multilingual |
| NVIDIA Nemotron 3 Super | **36** | 1M | $0.41 | 155 | Fast NVIDIA ecosystem |
| gpt-oss-120B (high) | **33** | 131K | $0.26 | 209 | Ultra-fast, OpenAI open |
| gpt-oss-20B (high) | **24** | 131K | $0.10 | 273 | Fastest, cheapest |

*Intelligence Index (OW = open-weight rank) from [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/models). April 2026 data.*

### Openness Index - How Open Are These Models?

Artificial Analysis now publishes an [Openness Index](https://artificialanalysis.ai/evaluations/artificial-analysis-openness-index) scoring models on model availability and transparency (methodology, training data). Top scores:

| Model | Openness Score | Notes |
|-------|---------------|-------|
| K2 Think V2 | 16.0 | Most open model overall |
| NVIDIA Nemotron 3 Super | 15.0 | Excellent transparency |
| DeepSeek V4 Pro/Flash | 9.0 | Good openness |
| GLM-5.1 | 8.0 | Solid transparency |
| gpt-oss-120B/20B | 7.0 | OpenAI's new open models |
| Gemma 4 31B | 7.0 | Good documentation |

---

## 3. Best Models for Fine-tuning (April 2026)

Not all open-weight models are equally good starting points for fine-tuning. These are the recommended choices grouped by compute budget.

### Small Models (less than 8B parameters)

Best when you have limited GPU memory (less than 24GB) or need fast inference.

| Model | Params | License | Why Fine-tune It |
|-------|--------|---------|-----------------|
| Qwen2.5-7B-Instruct | 7B | Apache 2.0 | Best quality in class, excellent instruction following |
| Qwen3.5-4B | 4B | Apache 2.0 | Newest Qwen small model; Intelligence Index 27 |
| Llama 3.2 3B | 3B | Llama 3.2 | Meta's smallest capable model; widely supported |
| Phi-4-mini | 3.8B | MIT | Strong reasoning for size; MIT license |
| Gemma 4 E4B | ~4B | Gemma ToU | Google's latest small model |

**Recommended starter**: `Qwen/Qwen2.5-7B-Instruct` - best quality, Apache 2.0 license, great tokenizer.

### Medium Models (8B to 14B parameters)

Good balance of quality and fine-tuning cost. Fits in 24GB GPU with QLoRA.

| Model | Params | License | Why Fine-tune It |
|-------|--------|---------|-----------------|
| Phi-4 | 14B | MIT | Best STEM/reasoning quality at 14B |
| Qwen2.5-14B-Instruct | 14B | Apache 2.0 | Strong across all domains |
| Gemma 4 12B (coming) | ~12B | Gemma ToU | Google quality; improved from Gemma 3 |

**Recommended starter**: `microsoft/phi-4` for STEM; `Qwen/Qwen2.5-14B-Instruct` for general.

### Large Models (32B and above)

Requires multi-GPU or A100/H100 for fine-tuning. Produces the highest-quality specialized models.

| Model | Params | License | Why Fine-tune It |
|-------|--------|---------|-----------------|
| Gemma 4 31B | 31B | Gemma ToU | Intelligence Index 39; fits on 2x A100 |
| Qwen2.5-32B-Instruct | 32B | Apache 2.0 | Best quality at 32B; Apache 2.0 |
| Llama 3.3 70B | 70B | Llama 3.3 | Widest tooling support |
| DeepSeek R1 70B Distill | 70B | MIT | Strong reasoning; MIT license |

**Recommended starter**: `Qwen/Qwen2.5-32B-Instruct` if you have 2x A100; `meta-llama/Llama-3.3-70B-Instruct` for widest support.

### Fine-tuning Model Selection Decision Tree

```
Do you have > 2x A100/H100?
  Yes -> Gemma 4 31B, Qwen2.5-32B, or Llama 3.3 70B
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

### GRPO - Group Relative Policy Optimization

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

### DPO / SimPO / KTO - Alignment Without PPO

| Method | Description | When to Use |
|--------|-------------|-------------|
| **DPO** (Direct Preference Optimization) | Fine-tune on (chosen, rejected) pairs directly | Standard alignment; simplest setup |
| **SimPO** (Simple Preference Optimization) | DPO variant with length normalization and margin reward | Better than DPO for instruction following |
| **KTO** (Kahneman-Tversky Optimization) | Works with binary feedback (good/bad) rather than pairs | When you have binary labels, not ranked pairs |

**Current best practice**: SimPO slightly outperforms DPO in most benchmarks; KTO if you only have thumbs-up/thumbs-down data.

### Unsloth - 2-5x Faster Fine-tuning

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
| **SGLang** | Highest (~16,200 tok/s H100) | Production API, RAG, agents - RadixAttention caches shared prefixes | `pip install sglang[all]` |
| **vLLM** | Very High (~12,500 tok/s H100) | Production API, multi-LoRA serving, AMD support | `pip install vllm` |
| **TGI** | High (~9,800 tok/s H100) | HuggingFace ecosystem, Inference Endpoints | Docker |
| **Ollama** | Medium | Local dev, Apple Silicon, edge, no GPU | Single binary |
| **llama.cpp** | Low-Medium | Embedded, CPU-only, maximum portability | Compile from source |

### API Provider Landscape

Artificial Analysis now benchmarks 23+ API providers for popular open models. Key findings:

| Provider | Strengths | Notable Speed |
|----------|-----------|--------------|
| **Cerebras** | Fastest inference for open models | 1,833 tok/s for gpt-oss-120B |
| **SambaNova** | Second fastest | 680 tok/s |
| **Groq** | Fast, developer-friendly | 421 tok/s |
| **DeepInfra** | Cheapest provider for many models | $0.04/1M input for gpt-oss-120B |
| **Together.ai** | Good balance of speed/price | 200 tok/s |
| **Fireworks** | Strong for production workloads | 204 tok/s |
| **Azure / AWS / GCP** | Enterprise SLAs, compliance | Moderate speed |

*Source: [artificialanalysis.ai API providers](https://artificialanalysis.ai/leaderboards/providers)*

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

### General Work AI Agents (April 2026)

Artificial Analysis now tracks [general work AI agents](https://artificialanalysis.ai/agents). Key players:

| Agent | Provider | Platforms | Key Feature | Pricing |
|-------|----------|-----------|-------------|---------|
| **Claude Cowork** | Anthropic | macOS, Windows | Sandboxed Linux VM, local file access, MCP | $20-200/mo |
| **ChatGPT Agent** | OpenAI | Web, Mobile, Desktop | Cloud VM, GPT-5.4 Thinking, ~30min autonomous | $20-200/mo |
| **Manus** | Meta | Web, Desktop, Mobile | Multi-model orchestration, sandboxed env | $20-200/mo |
| **Microsoft Copilot** | Microsoft | All platforms | M365 ecosystem integration, Copilot Studio | $9.99-30/mo |
| **Microsoft Copilot Cowork** | Microsoft | Web | Multi-step M365 automation, sandboxed | $21-30/mo |
| **Google Workspace Studio** | Google | Web | No-code agent builder, Google ecosystem | $8-27/mo |
| **Gemini Enterprise** | Google | Web | Enterprise knowledge search, pre-built agents | $21-30/mo |
| **OpenClaw** | Community | macOS, Linux, Windows | Open-source, self-hosted, WhatsApp/Slack/Teams | Free + API |
| **Hermes Agent** | Nous Research | macOS, Linux, Windows | Open-source, persistent memory, skill system | Free + API |

### Vector Databases (2025-2026)

| Database | Description | Best For |
|----------|-------------|----------|
| **Pinecone** | Managed cloud vector DB; serverless tier available | Production SaaS; zero ops overhead |
| **Qdrant** | Rust-based, high performance; excellent filtering | Self-hosted production; best performance/cost ratio |
| **Chroma** | Rewritten in Rust (2025); much faster than original Python | Local dev and small-medium production |
| **pgvector** | Postgres extension; vectors + SQL in one database | Existing Postgres users |
| **Weaviate** | Feature-rich; built-in hybrid search (BM25 + vector) | Hybrid search requirements |

---

## 6. What Changed Since March 2026

This section captures practical updates since the March snapshot so learners can prioritize what changed.

### Model Selection Updates (April 2026)

- **GPT-5.5 is the new #1**: OpenAI released GPT-5.5 with the highest Intelligence Index score ever (60). It comes in xhigh/high/medium/low tiers with effort-scaling.
- **Claude Opus 4.7 released**: Anthropic's latest Opus model matches Gemini 3.1 Pro and GPT-5.4 at score 57.
- **DeepSeek V4 generation launched**: V4 Pro (score 52) and V4 Flash (score 47, just $0.17/1M!) represent huge leaps in quality and value.
- **OpenAI released open-source models**: gpt-oss-120B and gpt-oss-20B are now available on 23 providers. gpt-oss-20B is the fastest model at 273 tok/s and the cheapest at $0.10/1M.
- **Open-weight leaders shifted**: Kimi K2.6 and MiMo-V2.5-Pro (both score 54) now lead open-weight models, replacing GLM-5 at the top.
- **New entrants**: Muse Spark (Meta, score 52), MiniMax-M2.7 (score 50, just $0.53/1M), NVIDIA Nemotron 3 Super (score 36, 155 tok/s).
- **Intelligence leaderboard snapshot** (artificialanalysis.ai, 499+ models ranked): GPT-5.5 leads at 60; top open-weight is Kimi K2.6/MiMo-V2.5-Pro at 54.

### Benchmark Methodology Updates (April 2026)

- **Intelligence Index v4.0.4**: Now includes 10 evaluations across 4 categories - Agents (25%), Coding (25%), General (25%), Scientific Reasoning (25%).
- **New evaluations added**: GDPval-AA (real-world knowledge work), AA-Omniscience (knowledge & hallucination), CritPt (physics reasoning).
- **Removed from index**: MMLU-Pro, LiveCodeBench, AIME 2025 (still available as standalone evaluations).
- **AA-Omniscience**: New hallucination benchmark - rewards accuracy, penalizes hallucinations, neutral on abstentions. Gemini 3.1 Pro Preview leads (score 33).
- **GDPval-AA**: Agentic task benchmark covering 44 occupations. GPT-5.5 leads (ELO 1780).
- **API Provider benchmarking**: Cerebras is fastest (1,833 tok/s for gpt-oss-120B), DeepInfra is cheapest.

### Training and Alignment Updates (April 2026)

- **SimPO and DPO remain default alignment baselines**.
- **GRPO adoption increased** for reasoning-tuned models and synthetic curriculum training.
- **Unsloth + TRL remains the standard** for small/medium fine-tuning projects.

### April 2026 Practical Defaults

| Layer | April 2026 Default Recommendation |
|------|------------------------------------|
| Best overall | GPT-5.5 (xhigh) |
| Best value frontier | Gemini 3.1 Pro Preview |
| Fast API assistant | GPT-5.4 mini / Claude 4.5 Haiku |
| Hard reasoning | GPT-5.5 / Claude Opus 4.7 / DeepSeek V4 Pro |
| Open-weight #1 (quality) | Kimi K2.6 / MiMo-V2.5-Pro |
| Open-weight general | DeepSeek V4 Flash / Qwen3.5 397B-A17B |
| Open-weight budget | gpt-oss-120B ($0.26/1M) / MiniMax-M2.7 ($0.53/1M) |
| Ultra-fast inference | gpt-oss-20B (273 tok/s) / Cerebras provider |
| Small local model | Phi-4-mini / Gemma 4 E4B |
| Fine-tuning starter | Qwen2.5-7B + QLoRA + RSLoRA |
| Inference server | SGLang (prod) / Ollama (local dev) |
| Agent runtime | LangGraph + MCP + OpenAI Agents SDK |

---

## 7. What to Learn in What Order

A structured learning path for April 2026. Follow this order to build solid foundations before tackling advanced topics.

### Phase 1: Foundations (Weeks 1-4)

**Goal**: Understand what LLMs are and how to use them via API.

1. **Python for AI** - numpy, pandas, matplotlib basics; Jupyter notebooks
2. **Prompt engineering** - zero-shot, few-shot, chain-of-thought; system prompts
3. **OpenAI / Anthropic API** - calling GPT-5.5 and Claude Opus 4.7; streaming; function calling
4. **Tokenization** - how text becomes tokens; tiktoken; why context window size matters
5. **RAG basics** - chunking documents, embedding models, Chroma, similarity search

**Milestone**: Build a document Q&A chatbot using RAG with a frontier API model.

### Phase 2: Open-Weight Models (Weeks 5-8)

**Goal**: Run and understand open-weight models locally and in the cloud.

1. **Hugging Face Transformers** - `pipeline`, `AutoModelForCausalLM`, `AutoTokenizer`
2. **Running models locally** - Ollama (easiest), then llama.cpp
3. **Quantization** - understand BF16 vs GPTQ vs AWQ vs GGUF; trade-offs
4. **Chat templates** - ChatML, Llama 3 template, Qwen template; why they matter
5. **vLLM / SGLang** - run a production-grade API server; benchmark throughput
6. **Model selection** - when to use Kimi K2.6 vs DeepSeek V4 vs Gemma 4; the decision tree above

**Milestone**: Self-host a model via SGLang and serve it behind a FastAPI endpoint.

### Phase 3: Fine-tuning (Weeks 9-14)

**Goal**: Adapt pre-trained models to specific tasks.

1. **Dataset preparation** - instruction format, chat format; quality over quantity
2. **LoRA fundamentals** - what low-rank adapters do mathematically; rank, alpha, target modules
3. **QLoRA with Unsloth** - fine-tune a 7B model in under 4GB VRAM
4. **SFT (Supervised Fine-Tuning)** - `SFTTrainer` from TRL; data formatting; evaluation during training
5. **DPO / SimPO alignment** - preference datasets; `DPOTrainer`; when to align vs just SFT
6. **GRPO for reasoning** - training a model to think step-by-step with RL
7. **Evaluation** - ROUGE, BERTScore, LLM-as-judge; avoiding eval data contamination

**Milestone**: Fine-tune Qwen2.5-7B on a domain-specific dataset, align with DPO, and evaluate with an LLM judge.

### Phase 4: Agents and Advanced RAG (Weeks 15-20)

**Goal**: Build production-grade agentic systems.

1. **Function calling / tool use** - structured outputs, JSON mode; tool definitions
2. **ReAct agents** - Reason + Act loop; building with OpenAI Agents SDK
3. **MCP (Model Context Protocol)** - write an MCP server; connect to Claude Desktop / your agent
4. **Advanced RAG** - hybrid search, reranking (ColBERT, cross-encoders), HyDE, RAPTOR
5. **LangGraph 1.0** - stateful agents, branching workflows, multi-agent handoffs
6. **Agentic evaluation** - trajectory evaluation; tool use accuracy; GDPval-AA benchmarks; AA-AgentPerf

**Milestone**: Build a multi-step research agent using LangGraph + MCP that can search the web, read documents, and write structured reports.

### Phase 5: Production and MLOps (Weeks 21-24)

**Goal**: Deploy and maintain AI systems reliably.

1. **Docker + GPU deployment** - containerizing vLLM/SGLang; docker-compose with GPU support
2. **Monitoring** - structured logging; latency p95/p99; token usage; refusal rate
3. **Cost optimization** - quantization trade-offs; batching strategies; API provider selection using [artificialanalysis.ai](https://artificialanalysis.ai/leaderboards/providers)
4. **Continuous evaluation** - A/B testing model updates; production feedback loops
5. **Security** - prompt injection defense; PII detection; rate limiting; API key management
6. **MLflow / Weights & Biases** - experiment tracking; model registry; deployment tracking

**Milestone**: Deploy your fine-tuned model to a cloud GPU with monitoring, a Docker container, cost tracking, and an A/B testing setup.

---

### Summary: The April 2026 AI Engineer Stack

```
Layer               Tools (April 2026 Best Choices)
---------           --------------------------------
Frontier APIs       GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro Preview
Open Models         Kimi K2.6, MiMo-V2.5-Pro, DeepSeek V4 Pro/Flash
Budget Open         gpt-oss-120B, MiniMax-M2.7, DeepSeek V4 Flash
Fine-tuning Base    Qwen2.5-7B (small), Phi-4 (medium), Gemma 4 31B (large)
Fine-tuning Tools   Unsloth + TRL (SFT/DPO/GRPO)
Inference           SGLang (production), Ollama (local/dev)
API Providers       Cerebras (speed), DeepInfra (cost), Azure/AWS (enterprise)
Agents              MCP + OpenAI Agents SDK + LangGraph 1.0
Work Agents         Claude Cowork, ChatGPT Agent, Manus, OpenClaw (OSS)
Vector DB           Qdrant (production), Chroma (dev), pgvector (Postgres)
Experiment Tracking Weights & Biases or MLflow
Observability       Langfuse (open source) or LangSmith
```

**Key resources**:
- [Artificial Analysis LLM Leaderboard](https://artificialanalysis.ai/leaderboards/models) - live rankings of 499+ models
- [Artificial Analysis Intelligence Index Methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) - how benchmarks are conducted
- [Artificial Analysis API Providers](https://artificialanalysis.ai/leaderboards/providers) - compare speed and cost across 23+ providers
- [Artificial Analysis AI Agents](https://artificialanalysis.ai/agents) - compare general work AI agents
- [Artificial Analysis Image/Video Arena](https://artificialanalysis.ai/image/arena) - compare image and video generation models

The pace of change in this field is fast, but the underlying principles - retrieval, fine-tuning, alignment, evaluation, deployment - remain stable. Master the fundamentals and you will adapt quickly as the specific tools evolve."""

def update_notebook_cell(nb_path, cell_index, new_source):
    """Update a specific cell's source in a notebook."""
    with open(nb_path) as f:
        nb = json.load(f)
    
    # Convert string to list of lines (ipynb format)
    lines = new_source.split('\n')
    nb['cells'][cell_index]['source'] = [line + '\n' for line in lines[:-1]] + [lines[-1]]
    
    with open(nb_path, 'w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print(f"  Updated cell {cell_index} in {nb_path}")


def copy_notebook(src, dst):
    """Copy notebook file, creating directories if needed."""
    dst_path = Path(dst)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"  Synced {src} -> {dst}")


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("Updating learning materials from Artificial Analysis (April 2026)")
    print("=" * 60)
    
    # 1. Update model landscape notebook
    print("\n1. Updating model landscape notebook...")
    landscape_nb = NB_DIR / "00-course-setup" / "01_model_landscape.ipynb"
    update_notebook_cell(landscape_nb, 0, MODEL_LANDSCAPE_MARKDOWN)
    
    # 2. Sync to next-docs mirror
    print("\n2. Syncing to next-docs mirror...")
    landscape_mirror = DOCS_DIR / "00-course-setup" / "01_model_landscape" / "01_model_landscape.ipynb"
    copy_notebook(landscape_nb, landscape_mirror)
    
    print("\n" + "=" * 60)
    print("Model landscape updated successfully!")
    print("=" * 60)
