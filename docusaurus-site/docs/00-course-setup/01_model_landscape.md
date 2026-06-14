---
title: "2. Model Landscape"
sidebar_label: "2. Model Landscape"
sidebar_position: 2
format: "md"
---
# AI Model Landscape: May 24, 2026

A practical reference for learners navigating the fast-moving AI ecosystem.
Use this guide to decide what to learn first, which models are worth testing now, and where the field is clearly trending.

> **Data source**: rankings, pricing, speed, context, and openness notes in this notebook are based primarily on [Artificial Analysis](https://artificialanalysis.ai/), especially its live [LLM leaderboard](https://artificialanalysis.ai/leaderboards/models) and [Openness Index](https://artificialanalysis.ai/evaluations/artificial-analysis-openness-index). Their leaderboard is live over a rolling measurement window, so exact prices, latency, and rank order can move between updates.

---

## Table of Contents

1. [Frontier Closed Models](#1-frontier-closed-models-may-2026)
2. [Best Open-Weight Models](#2-best-open-weight-models-may-2026)
3. [Best Models for Fine-tuning](#3-best-models-for-fine-tuning-may-2026)
4. [Key Training Techniques](#4-key-training-techniques-2025-2026)
5. [Key Infrastructure](#5-key-infrastructure-2025-2026)
6. [What Changed Since April 2026](#6-what-changed-since-april-2026)
7. [Learning Path for May 2026](#7-what-to-learn-in-what-order)

---

## 1. Frontier Closed Models (May 2026)

These are the strongest proprietary models available through hosted APIs. You cannot usually self-host or fine-tune them directly, but they set the practical ceiling for reasoning, coding, multimodal quality, and agent workflows.

### GPT-5.5 (OpenAI) - Current #1

- **Leaderboard status**: currently the top-ranked model on Artificial Analysis.
- **Best-known tier**: `GPT-5.5 (xhigh)` at **60** Intelligence Index.
- **Other notable tiers**: `GPT-5.5 (high)` at **59**, `GPT-5.5 (medium)` at **57**.
- **Context window**: 922K tokens.
- **Why it matters**: strongest general-purpose reasoning model in the current leaderboard snapshot; OpenAI's effort-scaled tiers still define the premium end of hosted reasoning.
- **Best for**: highest-stakes reasoning, planning, coding, long-form analysis, and premium agent backends.

### Claude Opus 4.7 (Anthropic)

- **Leaderboard status**: top-tier frontier model at **57** Intelligence Index.
- **Context window**: 1M tokens.
- **Why it matters**: remains one of the strongest coding and instruction-following models, especially for agentic loops and high-quality writing or review work.
- **Best for**: coding-heavy assistants, document analysis, safety-sensitive workflows, and high-quality tool use.

### Gemini 3.1 Pro Preview (Google)

- **Leaderboard status**: top-tier frontier model at **57** Intelligence Index.
- **Context window**: 1M tokens.
- **Output speed**: among the faster frontier models in the current snapshot.
- **Why it matters**: still one of the best quality-to-cost frontier choices for large-context and multimodal work.
- **Best for**: large-context reasoning, multimodal apps, and cost-aware frontier deployments.

### GPT-5.4 Family (OpenAI)

- **Leaderboard status**: still in the top frontier tier, with `GPT-5.4 (xhigh)` remaining highly competitive.
- **Notable variants**: `GPT-5.4`, `GPT-5.4 mini`, `GPT-5.4 nano`.
- **Why it matters**: the family remains very relevant when you want OpenAI quality at lower price or higher speed than GPT-5.5.
- **Best for**: agent backends, structured tool use, reasoning at lower cost than the flagship tier.

### Qwen3.7 Max (Alibaba)

- **Leaderboard status**: currently in the top closed-model tier at **57** Intelligence Index.
- **Context window**: 1M tokens.
- **Why it matters**: strong evidence that Alibaba is no longer just competitive in open-weight releases; it is also shipping frontier-class hosted models.
- **Best for**: teams that want a frontier-capable hosted model outside the OpenAI/Anthropic/Google trio.

### Claude Sonnet 4.6 (Anthropic)

- **Leaderboard status**: still a strong production model, below the very top tier but highly usable.
- **Why it matters**: often a practical default when you want a better cost/speed balance than Opus.
- **Best for**: coding assistants, general enterprise copilots, and balanced quality/speed deployments.

### Grok 4.x / 4.20 / 4.3 (xAI)

- **Context window story**: Grok variants remain notable for very large context windows, and Grok 4.x family members continue to appear in the current leaderboard.
- **Why it matters**: xAI remains relevant where long context and live-information workflows matter more than absolute benchmark leadership.
- **Best for**: long-context assistants, retrieval-heavy workflows, and ecosystem-specific experimentation.

### Quick Comparison - Frontier Closed Models

| Model | Intelligence Index | Context | Why It Stands Out | Best For |
|-------|-------------------|---------|-------------------|----------|
| GPT-5.5 (xhigh) | **60** | 922K | Current #1 model overall | Highest-stakes reasoning |
| GPT-5.5 (high) | **59** | 922K | Near-flagship quality | Premium production reasoning |
| Claude Opus 4.7 | **57** | 1M | Elite coding and agent work | Coding, review, agents |
| Gemini 3.1 Pro Preview | **57** | 1M | Frontier quality with strong value | Large-context + multimodal |
| GPT-5.4 (xhigh) | **57** | 1.05M | Still highly competitive | Tool use, reasoning, agents |
| Qwen3.7 Max | **57** | 1M | Alibaba now in the frontier API tier | Alternative frontier hosting |
| Claude Sonnet 4.6 | **52** | 1M | Strong balanced production default | Quality/speed trade-off |

**Practical lesson**: the frontier is no longer just about one winner. The real decision is usually between maximum quality, acceptable latency, tool quality, multimodality, and budget.

---

## 2. Best Open-Weight Models (May 2026)

Open-weight models can be self-hosted, fine-tuned, inspected more directly, and integrated without depending entirely on a proprietary vendor. The gap to closed frontier models is still real, but the best open-weight models are now good enough for serious production use.

### Kimi K2.6 - Current Open-Weight Leader

- **Leaderboard status**: current top open-weight model on Artificial Analysis.
- **Intelligence Index**: **54**.
- **Context window**: 256K tokens.
- **Why it matters**: currently the clearest quality-first open-weight choice.
- **Best for**: teams wanting the strongest open-weight reasoning model before fine-tuning or self-hosting.

### MiMo-V2.5-Pro (Xiaomi)

- **Leaderboard status**: tied at the top of open-weight quality at **54**.
- **Context window**: 1M tokens.
- **Why it matters**: combines strong intelligence with large context, making it unusually practical for long-context open deployments.
- **Best for**: cost-effective self-hosted or API-based open-weight deployments with long context needs.

### DeepSeek V4 Pro / V4 Flash

- **DeepSeek V4 Pro**: strong open-weight quality tier at **52**.
- **DeepSeek V4 Flash**: lower quality than V4 Pro but still one of the most compelling value models in the market.
- **Why it matters**: this family has become the benchmark for the quality/value trade-off in open-weight deployment.
- **Best for**: V4 Pro for quality-focused open-weight work; V4 Flash for aggressive cost control.

### Muse Spark (Meta)

- **Leaderboard status**: still among the strongest open-weight models at **52**.
- **Why it matters**: Meta remains relevant at the high end of open-weight quality, even if its most interesting releases are not always the easiest to deploy.
- **Best for**: high-quality open-weight experimentation and advanced self-hosted use cases.

### Qwen 3.6 / 3.5 Family (Alibaba)

- **Why it matters**: one of the most complete model families in the market, spanning small, mid-size, coder, omni, and higher-end reasoning variants.
- **Practical lesson**: Qwen is no longer just a good fallback. For many teams it is the default open family because it covers edge deployment, fine-tuning, and larger hosted/open-weight serving with one ecosystem.
- **Best for**: broad deployment coverage, Apache-friendly workflows, and a single family from small to large.

### GLM-5.1 (Z AI)

- **Intelligence Index**: still around the top open-weight tier.
- **Why it matters**: strong multilingual and Chinese-language relevance keeps it important even when it is not the absolute top model.
- **Best for**: multilingual and especially Chinese-heavy production usage.

### MiniMax-M2.7

- **Why it matters**: a reminder that value models keep getting stronger; not every good deployment needs a flagship model.
- **Best for**: budget-sensitive production where you still want respectable reasoning quality.

### Gemma 4 31B and Smaller Gemma 4 Variants

- **Why it matters**: Gemma remains one of the strongest options for local experimentation and smaller-scale self-hosting, especially where Google's model quality matters more than absolute openness.
- **Best for**: local research, single-node deployment, and smaller multilingual/self-hosted projects.

### gpt-oss-120B / gpt-oss-20B

- **Why they matter**: they are extremely cheap and fast relative to their quality tier, and they changed the conversation around low-cost hosted open-style inference.
- **Important caveat**: do not confuse "open weights" with fully open-source or highly transparent. Their normalized openness score is much lower than the most open models in the field.
- **Best for**: ultra-low-cost inference and experimentation with widely available providers.

### Quick Comparison - Open-Weight Models

| Model | Intelligence Index | Context | Why It Stands Out | Best For |
|-------|-------------------|---------|-------------------|----------|
| Kimi K2.6 | **54** | 256K | Current #1 open-weight quality | Best open-weight reasoning |
| MiMo-V2.5-Pro | **54** | 1M | Top quality plus long context | Long-context open deployment |
| DeepSeek V4 Pro | **52** | 1M | Strong quality/value balance | Quality open serving |
| Muse Spark | **52** | 262K | Meta's strongest current open-weight tier | Advanced self-hosting |
| GLM-5.1 | **51** | 200K | Strong multilingual profile | Chinese + multilingual |
| MiniMax-M2.7 | **50** | 205K | Budget-friendly quality | Cost-aware production |
| DeepSeek V4 Flash | **47** | 1M | Very strong value | Budget open inference |
| Gemma 4 31B | **39** | 256K | Strong local / smaller-cluster option | Local or single-node work |
| gpt-oss-120B | **33** | 131K | Fast and cheap for its size | Cheap hosted inference |
| gpt-oss-20B | **24** | 131K | Very cheap, very fast | Budget workloads |

### Openness Index - Open Weights vs Real Openness

Artificial Analysis now separates **open weights** from **overall openness and transparency**.
That is an important correction for learners: being downloadable is not the same thing as being fully open.

Current high-openness leaders include:

| Model | Normalized Openness Score | Why It Matters |
|-------|---------------------------|----------------|
| OLMo 3 7B Instruct | **88.89** | One of the clearest examples of genuinely open release practices |
| OLMo 3.1 32B Think | **88.89** | High openness with stronger reasoning capability |
| OLMo 3 7B Think | **88.89** | Strong openness baseline for learners and researchers |
| K2 Think V2 | **88.89** | High-openness and useful reasoning profile |
| NVIDIA Nemotron 3 Super | **83.33** | Good balance of openness and stronger practical capability |

**Important distinction**:
- **Best open-weight quality** is currently led by Kimi K2.6 / MiMo-V2.5-Pro.
- **Most open and transparent** releases are led by OLMo-family models and a few highly documented research/open releases.

---

## 3. Best Models for Fine-tuning (May 2026)

Not every strong model is the right fine-tuning base. For most learners and small teams, licensing, tokenizer quality, memory footprint, and ecosystem support matter at least as much as raw benchmark score.

### Small Models (less than 8B parameters)

Best when you have limited GPU memory, want cheap iteration, or need local experimentation.

| Model | Approx Size | Why Fine-tune It |
|-------|-------------|------------------|
| Qwen3.5 4B | 4B | Strong small-model baseline, broad tooling support |
| Gemma 4 E4B / E2B | ~2B-4B class | Practical for local experimentation and small-GPU work |
| Phi-4 Mini | ~4B class | Strong reasoning reputation for size |
| OLMo 3 7B Instruct | 7B | Great if openness/transparency matters to you |

**Recommended starter**: Qwen3.5 4B if you want a broadly practical base; OLMo 3 7B Instruct if openness matters more than raw ecosystem scale.

### Medium Models (8B to 14B parameters)

Good balance of cost, fine-tuning simplicity, and downstream quality.

| Model | Approx Size | Why Fine-tune It |
|-------|-------------|------------------|
| Qwen3.5 9B | 9B | Practical balance of quality and cost |
| Phi-4 | 14B | Strong reasoning and STEM profile |
| Granite 4.1 8B | 8B | Useful for enterprise-oriented or structured tasks |
| Gemma 4 12B-class variants | ~12B | Good quality for teams comfortable with Gemma terms |

**Recommended starter**: Qwen3.5 9B for general fine-tuning; Phi-4 if your task is coding, math, or technical reasoning heavy.

### Large Models (27B and above)

Use these when you already know your task is valuable enough to justify heavier infra.

| Model | Approx Size | Why Fine-tune It |
|-------|-------------|------------------|
| Qwen3.6 27B / 35B A3B | 27B-35B | Strong open family with good deployment coverage |
| Gemma 4 31B | 31B | Strong large open model for specialist work |
| Kimi K2.6 | large frontier-style open-weight | Best if you can support the highest-quality open-weight base |
| MiMo-V2.5-Pro | large frontier-style open-weight | Long-context fine-tuning candidate |

**Recommended starter**: Qwen3.6 27B or 35B A3B if you want a realistic large-model base without overcomplicating your stack.

### Fine-tuning Model Selection Decision Tree

```
Do you need the strongest practical open-weight base?
  Yes -> Kimi K2.6 or MiMo-V2.5-Pro
  No  -> Continue

Do you want the easiest broadly-supported fine-tuning path?
  Yes -> Qwen3.5 4B / 9B or Qwen3.6 27B / 35B
  No  -> Continue

Is openness and reproducibility a major concern?
  Yes -> OLMo-family or NVIDIA Nemotron family
  No  -> Continue

Are you memory constrained?
  <= 24GB GPU -> Qwen3.5 4B, Phi-4 Mini, Gemma 4 E4B
  48-80GB GPU  -> Qwen3.5 9B, Phi-4, Granite 4.1 8B
  Multi-GPU    -> Qwen3.6 27B/35B, Gemma 4 31B, Kimi K2.6
```

---

## 4. Key Training Techniques (2025-2026)

### GRPO - Group Relative Policy Optimization

- **What it is**: a reinforcement learning method for reasoning models that does not require a separate critic network in the same way PPO traditionally does.
- **Why it matters**: GRPO remains one of the key ideas behind the current reasoning-model wave and is still relevant for synthetic curriculum training and reasoning-focused post-training.
- **Use when**: you are working on reasoning-style RL, math/coding optimization, or structured-verifier feedback loops.

### LoRA / QLoRA / DoRA / rsLoRA

Parameter-efficient fine-tuning (PEFT) still matters because even in 2026 most teams do not full-fine-tune frontier-scale models.

| Method | Description | When to Use |
|--------|-------------|-------------|
| **LoRA** | Low-rank adapters added to frozen weights | Standard PEFT baseline |
| **QLoRA** | LoRA over 4-bit quantized weights | Best default under memory constraints |
| **DoRA** | Separates magnitude and direction updates | When plain LoRA underfits |
| **rsLoRA** | Rank-stabilized scaling for higher-rank adapters | Better stability for larger LoRA ranks |

**Current best practice**: QLoRA + rsLoRA remains the safest default for most practical fine-tuning.

### DPO / SimPO / KTO

Preference optimization continues to replace older PPO-heavy alignment stacks for many teams.

| Method | Description | When to Use |
|--------|-------------|-------------|
| **DPO** | Direct optimization on chosen/rejected pairs | Simple baseline for preference alignment |
| **SimPO** | Preference optimization with stronger practical behavior in many setups | Good default over plain DPO |
| **KTO** | Works from binary good/bad feedback | Useful when pairwise preference data is unavailable |

**Practical default**: start with SFT, then move to SimPO or DPO if behavior tuning is the real bottleneck.

### Unsloth - Faster Fine-tuning for Real Projects

- **What it is**: a speed- and memory-focused fine-tuning stack for common open model families.
- **Why it matters**: it remains one of the easiest ways to reduce GPU cost and iteration time for LoRA, QLoRA, DPO, and GRPO-style workflows.
- **Where it fits**: especially useful for Qwen, Gemma, Llama, Phi, and similar practical open-weight bases.

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="Qwen/Qwen3.5-4B-Instruct",
    max_seq_length=8192,
    load_in_4bit=True,
)

model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    lora_alpha=16,
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj"
    ],
    use_rslora=True,
)
```

---

## 5. Key Infrastructure (2025-2026)

### Inference Engines

For self-hosting, the practical stack is still concentrated around a few tools:

| Tool | Best For | Notes |
|------|----------|-------|
| **SGLang** | Highest-throughput production serving, agent backends, prefix reuse | Often the best answer when throughput matters most |
| **vLLM** | General production serving, multi-LoRA, broad ecosystem support | Still the most common recommendation |
| **TGI** | Hugging Face-native deployments | Good if you already live in HF infrastructure |
| **Ollama** | Local development and laptop workflows | Easiest local starting point |
| **llama.cpp** | CPU, edge, embedded, maximum portability | Great for constrained environments |

### API Provider Landscape

Provider-level performance changes quickly, so treat this as a live comparison problem, not a memorize-once fact set.

Common providers learners should know:
- **Cerebras**: often among the fastest for supported open models.
- **Groq**: popular for low-latency developer workflows.
- **SambaNova**: strong throughput on selected hosted models.
- **DeepInfra**: often competitive on price.
- **Fireworks / Together**: common production-friendly open-model hosts.
- **Azure / AWS / GCP**: enterprise constraints, procurement, compliance, and ecosystem integration often matter more than raw speed.

**Practical lesson**: choose model first, then compare providers for that exact model rather than assuming one provider is always best.

### Fine-tuning Frameworks

| Tool | Best For |
|------|----------|
| **Unsloth** | Most single-node PEFT work |
| **Axolotl** | Config-driven fine-tuning and team workflows |
| **TRL** | Reference implementations and maximum compatibility |

### Agent Frameworks

The agent ecosystem is much more stable than it was a year ago.

| Tool | Description | Best For |
|------|-------------|----------|
| **MCP (Model Context Protocol)** | Open tool/data connectivity standard | Cross-model tool integration |
| **OpenAI Agents SDK** | Official OpenAI agent runtime | Production agents on OpenAI models |
| **LangGraph** | Stateful graph-based orchestration | Complex agent systems and multi-step workflows |
| **LlamaIndex Workflows** | Event-driven orchestration | RAG-heavy agent pipelines |

### General Work AI Agents

Consumer and prosumer agent products change quickly, but the broad categories are stable:

- **ChatGPT Agent**: polished general-purpose agent experience in OpenAI's ecosystem.
- **Claude Cowork**: strong tool/file workflows with MCP-style integration story.
- **Microsoft Copilot**: strongest where M365 integration matters.
- **Gemini Enterprise / Workspace tools**: strongest where Google Workspace integration matters.
- **Open-source / self-hosted agents**: valuable for privacy, customization, and experimentation, but usually require more engineering maturity.

### Vector Databases

| Database | Best For |
|----------|----------|
| **Pinecone** | managed production SaaS |
| **Qdrant** | self-hosted production, excellent filtering |
| **Chroma** | local development and smaller projects |
| **pgvector** | teams already standardized on Postgres |
| **Weaviate** | hybrid search and feature-rich managed/self-hosted setups |

---

## 6. What Changed Since April 2026

This section captures the practical deltas learners should notice between an April snapshot and a late-May snapshot.

### Model Selection Updates (May 2026)

- **GPT-5.5 remains the clear #1** in the current Artificial Analysis snapshot, with `xhigh` at 60 and `high` at 59.
- **The frontier cluster tightened**: Claude Opus 4.7, Gemini 3.1 Pro Preview, GPT-5.4, and Qwen3.7 Max are now best understood as a high-end pack rather than a simple single-vendor hierarchy under GPT-5.5.
- **Qwen3.7 Max entered the serious frontier conversation** as a hosted closed model, not just an open-family side story.
- **Kimi K2.6 and MiMo-V2.5-Pro still define the top open-weight tier** at 54 Intelligence Index.
- **DeepSeek V4 Pro / Flash are now the easiest shorthand for open-weight quality/value** in production discussions.
- **Openness became more nuanced**: the most open models are not necessarily the strongest open-weight deployment models. OLMo-family releases currently dominate openness rankings more clearly than many popular commercial open-weight models.
- **"Open weights" and "open source" should not be treated as synonyms** anymore. This distinction is now explicit in mainstream benchmarking.

### Benchmark and Measurement Updates (May 2026)

- **The leaderboard snapshot is live** rather than a fixed once-per-quarter table, so price/speed/latency numbers should be treated as rolling measurements.
- **Artificial Analysis now highlights model openness more explicitly**, which makes transparency a first-class selection criterion alongside price, speed, and intelligence.
- **The current leaderboard context emphasizes 366 ranked models** and rolling measurement windows rather than a static spreadsheet mentality.

### Training and Infrastructure Updates (May 2026)

- **QLoRA + rsLoRA is still the default practical fine-tuning recipe** for learners and most small teams.
- **SimPO/DPO remain more practical than PPO-heavy alignment stacks** for most applied work.
- **SGLang and vLLM are still the central self-hosted serving choices**, with Ollama remaining the easiest local path.
- **Provider arbitrage matters more than ever**: many strong open-weight models are now differentiated as much by provider latency/cost as by the base checkpoint itself.

### May 2026 Practical Defaults

| Layer | May 2026 Default Recommendation |
|------|----------------------------------|
| Best overall | GPT-5.5 (xhigh) |
| Best frontier value | Gemini 3.1 Pro Preview or Qwen3.7 Max |
| Fast frontier assistant | GPT-5.4 mini or Claude 4.5 Haiku |
| Hard reasoning | GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro Preview |
| Open-weight #1 | Kimi K2.6 or MiMo-V2.5-Pro |
| Open-weight quality/value | DeepSeek V4 Pro / DeepSeek V4 Flash |
| Open family to learn deeply | Qwen 3.5 / 3.6 |
| Small local model | Gemma 4 E4B or Phi-4 Mini |
| Fine-tuning starter | Qwen3.5 4B + QLoRA + rsLoRA |
| Production inference server | SGLang or vLLM |
| Local dev runtime | Ollama |
| Agent runtime | MCP + LangGraph + provider SDK |

---

## 7. What to Learn in What Order

A structured learning path for May 2026. The order matters more than the exact model names.

### Phase 1: Foundations (Weeks 1-4)

**Goal**: understand what LLMs are and how to use them well through hosted APIs.

1. **Python for AI** - numpy, pandas, plotting, notebooks.
2. **Prompting basics** - zero-shot, few-shot, constraints, structured output.
3. **API usage** - call hosted models, stream output, use tool calls, handle retries.
4. **Tokenization and context** - why context windows, truncation, and chunking matter.
5. **RAG basics** - embeddings, chunking, vector search, answer generation.

**Milestone**: build a document Q&A assistant using a hosted model and a simple vector store.

### Phase 2: Open-Weight Models (Weeks 5-8)

**Goal**: understand self-hosted model trade-offs.

1. **Transformers basics** - tokenizers, chat templates, generation configs.
2. **Run models locally** - Ollama first, then `llama.cpp` or a hosted local server.
3. **Quantization** - BF16 vs 8-bit vs 4-bit vs GGUF/AWQ/GPTQ trade-offs.
4. **Production serving** - vLLM and SGLang.
5. **Model selection** - when to use Kimi K2.6, MiMo-V2.5-Pro, DeepSeek V4, Qwen, or Gemma.

**Milestone**: self-host an open-weight model behind an API and compare its quality/cost to a frontier API model.

### Phase 3: Fine-tuning (Weeks 9-14)

**Goal**: adapt models to a specific domain or behavior.

1. **Dataset design** - format, curation, and eval splits.
2. **LoRA fundamentals** - rank, alpha, target modules.
3. **QLoRA with Unsloth** - memory-efficient tuning.
4. **SFT** - build a reliable supervised baseline before RL.
5. **DPO / SimPO** - align behavior after SFT.
6. **GRPO** - reasoning-focused post-training.
7. **Evaluation** - LLM-as-judge, task evals, and human review.

**Milestone**: fine-tune a Qwen or Gemma model on a domain-specific task, then evaluate before and after alignment.

### Phase 4: Agents and Advanced RAG (Weeks 15-20)

**Goal**: build systems that use tools, state, and retrieval effectively.

1. **Structured outputs and tool use**
2. **MCP basics**
3. **LangGraph or comparable orchestration**
4. **Advanced RAG** - hybrid search, reranking, caching, evaluation
5. **Tracing and agent evaluation**

**Milestone**: build a research or operations agent that can use tools, retrieve documents, and produce structured reports.

### Phase 5: Production and MLOps (Weeks 21-24)

**Goal**: ship, monitor, and improve AI systems reliably.

1. **Containerization and deployment**
2. **Monitoring** - latency, failures, token use, refusals
3. **Cost optimization** - model routing, batching, provider selection
4. **Continuous evaluation** - shadow testing and A/B comparison
5. **Security** - prompt injection, secrets, PII, abuse controls
6. **Experiment tracking and observability**

**Milestone**: deploy one real system end-to-end with monitoring, evaluation, and rollback discipline.

---

### Summary: The May 2026 AI Engineer Stack

```
Layer               Tools (May 2026 Practical Choices)
---------           ----------------------------------
Frontier APIs       GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro, Qwen3.7 Max
Open Models         Kimi K2.6, MiMo-V2.5-Pro, DeepSeek V4 Pro, Qwen 3.6 family
Budget Open         DeepSeek V4 Flash, MiniMax-M2.7, gpt-oss-120B/20B
Fine-tuning Base    Qwen3.5 4B/9B, Phi-4, Gemma 4, Qwen3.6 27B/35B
Fine-tuning Tools   Unsloth + TRL + PEFT
Inference           SGLang or vLLM (production), Ollama (local)
API Providers       Compare per-model on the live provider leaderboard
Agents              MCP + LangGraph + provider SDKs
Vector DB           Qdrant, Pinecone, Chroma, pgvector
Observability       Langfuse, LangSmith, W&B, MLflow
```

**Key resources**:
- [Artificial Analysis LLM Leaderboard](https://artificialanalysis.ai/leaderboards/models) - live model rankings
- [Artificial Analysis Openness Index](https://artificialanalysis.ai/evaluations/artificial-analysis-openness-index) - openness and transparency comparison
- [Artificial Analysis Methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) - benchmark details
- [Artificial Analysis Providers Leaderboard](https://artificialanalysis.ai/leaderboards/providers) - compare hosts for the same model
- [Artificial Analysis AI Agents](https://artificialanalysis.ai/agents) - general-work agent comparisons

The field is moving fast, but the durable skills are still the same: choosing the right model for the task, evaluating reliably, building retrieval and tool workflows, fine-tuning only when it is justified, and operating systems with discipline.
