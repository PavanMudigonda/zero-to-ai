# AI/ML Decision Matrices & Comparison Guides

> Quick reference for choosing the right tools, models, and approaches for your AI/ML projects (April 2026)

## Table of Contents
- [LLM Model Selection](#llm-model-selection)
- [Vision Models](#vision-models)
- [Fine-tuning Methods](#fine-tuning-methods)
- [Vector Databases](#vector-databases)
- [Embedding Models](#embedding-models)
- [Image Generation](#image-generation)
- [Deployment Options](#deployment-options)

---

## LLM Model Selection

**When should you use which LLM? (April 2026)**

| Model | Best For | Pros | Cons | Cost (1M tokens) | When to Use |
|-------|----------|------|------|------------------|-------------|
| **GPT-5.4** | Production, multimodal | Latest OpenAI flagship, vision + audio | Expensive | $2.50 in / $10 out | Complex tasks, multimodal, production apps |
| **GPT-4.1** | Development, balanced | Great quality, 1M context window | Higher cost than mini tiers | $2 in / $8 out | General production, long-context tasks |
| **GPT-4.1-mini** | Development, testing | Fast, cheap, good quality | Not as capable | $0.40 in / $1.60 out | Development, high-volume tasks, chatbots |
| **o3** | Research, reasoning | Top reasoning, complex problems | Slow, expensive | $10 in / $40 out | Math, coding, research, complex analysis |
| **o4-mini** | Coding, math | Fast reasoning, cost-effective | Limited general knowledge | $1.10 in / $4.40 out | Code generation, STEM problems |
| **Claude Opus 4.6** | Complex coding, agents | Best at code, 200k context, tool use | Expensive | $15 in / $75 out | Agentic coding, deep analysis, complex tasks |
| **Claude Sonnet 4.6** | Coding, analysis | Excellent at code, 200k context | API only | $3 in / $15 out | Code reviews, daily coding, balanced cost |
| **Claude Haiku 4.5** | Speed, high volume | Fastest Claude, very cheap | Less capable | $0.80 in / $4 out | Chatbots, classification, high throughput |
| **Gemini 3.1 Pro** | Multimodal, long context | 2M context, video + audio understanding | API only | $1.25 in / $5 out | Extremely long documents, video, multimodal |
| **DeepSeek R1** | Reasoning, self-hosted | Open-weight, strong reasoning | Requires GPU | Free (hosting cost) | Privacy + reasoning, cost-sensitive |
| **DeepSeek V3.2** | General, self-hosted | Excellent quality, MoE efficient | Requires GPU | Free (hosting cost) | Self-hosted production, general tasks |
| **Llama 4 (Scout/Maverick)** | Self-hosted production | Free, MoE, 10M context (Scout) | Large models | Free (hosting cost) | Privacy, cost-sensitive, long context |
| **Qwen 3 (0.6-235B)** | Multilingual, MoE | Best open-source, thinking modes | Requires hosting | Free (hosting cost) | Non-English, code, self-hosting |
| **Phi-4** | Small/edge, reasoning | Tiny but powerful (14B) | Limited vs larger models | Free (hosting cost) | Edge deployment, limited hardware |

**Decision Tree:**
```{mermaid}
flowchart TD
    A{Need multimodal?} -->|Yes| B[GPT-5.4 / Gemini 3.1 Pro / Claude Sonnet 4.6]
    A -->|No| C{Need complex reasoning?}
    C -->|Yes| D[o3 / o4-mini / DeepSeek R1]
    C -->|No| E{Need self-hosting?}
    E -->|Yes| F[Qwen 3 / Llama 4 / DeepSeek V3.2]
    E -->|No| G{Budget conscious?}
    G -->|Yes| H[GPT-4.1-mini / Claude Haiku 4.5 / Gemini Flash]
    G -->|No| I[Claude Sonnet 4.6 / GPT-5.4 / Gemini 3.1 Pro]
```

---

## Vision Models

**Choosing between vision-language models (April 2026)**

| Model | Best For | Pros | Cons | Cost | When to Use |
|-------|----------|------|------|------|-------------|
| **GPT-5.4** | Complex understanding | Best quality, multimodal native | Expensive | $2.50+/1M in | Complex scene understanding, OCR+reasoning |
| **Gemini 3.1 Pro** | Long video, multimodal | 2M context, video + audio | API only | $1.25/1M in | Video analysis, long documents, multimodal |
| **Claude Sonnet 4.6** | Document + image analysis | Great at charts, PDFs, code screenshots | API only | $3/1M in | Document analysis, visual code review |
| **CLIP / SigLIP** | Embeddings, classification | Fast, zero-shot, embeddings | Limited understanding | Free (self-host) | Image search, zero-shot classification |
| **Qwen2.5-VL** | Advanced self-hosting | Best open-source VLM quality | Large model | Free (hosting) | High-quality self-hosted VQA |
| **LLaVA-OneVision** | Self-hosted VQA | Open-source, customizable | Requires GPU | Free (hosting) | Privacy needs, custom fine-tuning |
| **InternVL 3** | Research, benchmarks | Top open-source on many benchmarks | Complex setup | Free (hosting) | Research, multilingual vision |

**Use Case Guide:**
- **Image Search/Similarity**: CLIP or SigLIP (fast, efficient)
- **Image Captioning**: GPT-5.4 (best quality) or Qwen2.5-VL (self-hosted)
- **Visual Question Answering**: Gemini 3.1 Pro (production) or Qwen2.5-VL (self-hosted)
- **OCR + Understanding**: GPT-5.4 or Claude Sonnet 4.6
- **Video Understanding**: Gemini 3.1 Pro (native video support)
- **Zero-shot Classification**: CLIP or SigLIP

---

## Fine-tuning Methods

**Which fine-tuning approach should you use?**

| Method | Parameters Trained | VRAM (7B model) | Training Time | Quality | When to Use |
|--------|-------------------|-----------------|---------------|---------|-------------|
| **Full Fine-tuning** | 100% | 40GB+ | Days | Best | Research, unlimited resources |
| **LoRA (r=64)** | 2-5% | 8-12GB | Hours | Excellent | Most production use cases |
| **QLoRA** | 2-5% | 4-6GB | Hours | Very good | Limited GPU, good quality needed |
| **DoRA** | 2-5% | 8-12GB | Hours | Better than LoRA | Best quality with adapters |
| **Adapters** | <1% | 6-8GB | Hours | Good | Quick experimentation |
| **Prompt Tuning** | <0.1% | Minimal | Minutes | Fair | Extremely limited resources |

**Decision Matrix:**
```{mermaid}
flowchart TD
    A{GPU VRAM?} -->|">40GB"| B[Full fine-tuning]
    A -->|"16-40GB"| C[LoRA r=64 or DoRA]
    A -->|"8-16GB"| D[LoRA r=32 or QLoRA]
    A -->|"<8GB"| E["QLoRA (4-bit) or Prompt Tuning"]

    F{Quality needed?} -->|Critical| G[Full fine-tuning or DoRA]
    F -->|High| H[LoRA r=64 or DoRA]
    F -->|Medium| I[LoRA r=32 or QLoRA]
    F -->|Basic| J[Adapters or Prompt Tuning]
```

**2026 Best Practices:**
- **Default choice**: LoRA with r=64, RSLoRA enabled
- **Budget GPU**: QLoRA with 4-bit quantization (NF4)
- **Best quality**: DoRA with r=64
- **Fastest training**: Unsloth (2-5x speedup over standard HF)
- **Fastest iteration**: Adapters or prompt tuning

---

## Vector Databases

**Comparing vector database options**

| Database | Best For | Pros | Cons | Deployment | When to Use |
|----------|----------|------|------|------------|-------------|
| **ChromaDB** | Development, prototyping | Easy setup, Python-native | Basic features | Embedded/Server | Quick prototypes, learning |
| **Qdrant** | Production, performance | Fast, feature-rich, Rust | More complex | Docker/Cloud | Production apps, high performance |
| **Weaviate** | Hybrid search | Built-in vectorization, GraphQL | Resource-heavy | Docker/Cloud | Hybrid search, complex schemas |
| **Milvus** | Scale, big data | Highly scalable, distributed | Complex setup | Kubernetes | Large-scale (millions+ vectors) |
| **Pinecone** | Managed service | Fully managed, easy | Expensive, vendor lock-in | Cloud only | Quick production, no ops |
| **pgvector** | Existing PostgreSQL | PostgreSQL extension, familiar | Limited features | PostgreSQL | Already using Postgres |
| **FAISS** | Research, offline | Fast similarity search | No persistence layer | In-memory | Research, benchmarking |

**Selection Guide:**

**By Scale:**
- **<100K vectors**: ChromaDB (simplest)
- **100K-1M vectors**: Qdrant or Weaviate
- **1M-10M vectors**: Qdrant or Milvus
- **>10M vectors**: Milvus or Pinecone

**By Use Case:**
- **Learning/Prototyping**: ChromaDB
- **Production RAG**: Qdrant
- **Hybrid (keyword + vector)**: Weaviate
- **Existing Postgres**: pgvector
- **No DevOps**: Pinecone
- **Maximum scale**: Milvus

---

## Embedding Models

**Choosing the right embedding model (April 2026)**

| Model | Type | Dimensions | MTEB | Cost | When to Use |
|-------|------|------------|------|------|-------------|
| **Gemini Embedding 001** | API | 3072 (MRL) | 68.32 (#1) | ~$0.004/1K chars | Best quality, cheapest API |
| **Cohere Embed v4** | API | 1024 | 65.2 | $0.12/1M tokens | Enterprise, 128K context, multilingual |
| **text-embedding-3-large** | API | 3072 (MRL) | 64.6 | $0.13/1M | OpenAI ecosystem |
| **Voyage 3.5** | API | 256-2048 (MRL) | ~64 | $0.06/1M | Best value API, 200M free tokens |
| **text-embedding-3-small** | API | 1536 | ~62 | $0.02/1M | Budget API |
| **Qwen3-Embedding-8B** | Local | 32-7168 (MRL) | ~64 / 70.58 MMTEB | Free | Best open-source, 100+ langs |
| **BGE-M3** | Local | 1024 | 63.0 | Free | Hybrid retrieval (dense+sparse) |
| **all-mpnet-base-v2** | Local | 768 | ~59 | Free | General purpose, local |
| **all-MiniLM-L6-v2** | Local | 384 | 56.3 | Free | Speed critical, prototyping |

**Decision Factors:**

**By Requirement:**
- **Best Quality (API)**: Gemini Embedding (#1 MTEB) or Voyage 3.5
- **Best Quality (local)**: Qwen3-Embedding-8B
- **Cheapest API**: Gemini Embedding (~free) then OpenAI Small ($0.02/1M)
- **Best Speed**: all-MiniLM-L6-v2 (local) or Gemini Embedding (API)
- **Multilingual**: Qwen3-Embedding (100+ langs, MMTEB #1) or Cohere v4
- **Multimodal**: Gemini Embedding (all modalities) or Jina v4 (text+images+PDFs)
- **Long context**: Cohere v4 (128K tokens) or Jina v4/Voyage (32K)
- **Domain-specific**: Voyage (code-3, law-2, finance-2)

**Typical Use Cases:**
- **RAG chatbots**: Gemini Embedding, Voyage 3.5, or all-mpnet-base-v2
- **Semantic search**: Qwen3-Embedding (local) or Gemini Embedding (API)
- **Document Q&A**: Cohere v4 (long context) or Gemini Embedding
- **Fast prototyping**: all-MiniLM-L6-v2 or Gemini free tier
- **Hybrid search**: BGE-M3 (dense + sparse + multi-vector)

---

## Image Generation

**Choosing image generation solutions (April 2026)**

| Solution | Quality | Speed | Cost | Control | When to Use |
|----------|---------|-------|------|---------|-------------|
| **GPT-5.4 (native)** | Excellent | Fast | API pricing | Low | Text+image generation in one model |
| **DALL-E 3** | Excellent | Fast | $0.04-0.12/image | Low | Quick results, no setup |
| **Midjourney v7** | Excellent | Medium | $10-60/month | Medium | Best artistic quality |
| **FLUX 1.1 Pro** | Best | Medium | API or self-host | High | Best open-source, photorealism |
| **Stable Diffusion 3.5** | Excellent | Medium | Free (GPU cost) | High | Production self-hosted |
| **Ideogram 3** | Excellent | Fast | API | Medium | Best text rendering in images |
| **SDXL Turbo** | Very good | Very fast | Free (GPU cost) | High | Fast iteration, prototyping |

**Decision Tree:**
```{mermaid}
flowchart TD
    A{Need absolute best quality?} -->|"Yes, willing to pay"| B[Midjourney v7 or FLUX 1.1 Pro]
    A -->|"Yes, self-hosted"| C[FLUX 1.1 dev]
    A -->|No| D{Need very fast generation?}
    D -->|Yes| E[SDXL Turbo or DALL-E 3]
    D -->|No| F{Have GPU?}
    F -->|Yes| G[SD 3.5 or FLUX]
    F -->|No| H["DALL-E 3 or Ideogram 3 (API)"]
```

**By Use Case:**
- **Product mockups**: DALL-E 3 or Ideogram 3 (fast, reliable)
- **Artistic projects**: Midjourney v7 or FLUX 1.1
- **Photorealistic images**: FLUX 1.1 Pro
- **Text in images**: Ideogram 3 (best text rendering)
- **High-volume generation**: SDXL Turbo (self-hosted)
- **Custom fine-tuning**: FLUX or SD 3.5
- **Production apps**: FLUX 1.1 Pro or API (DALL-E)

---

## Deployment Options

**Where and how to deploy your AI models**

| Option | Best For | Pros | Cons | Cost | When to Use |
|--------|----------|------|------|------|-------------|
| **OpenAI API** | Quick production | No infrastructure, reliable | Expensive at scale, data privacy | Pay per token | MVP, low-medium volume |
| **Anthropic (Claude)** | Production apps | Great models, reliable | Limited models | Pay per token | Production chatbots |
| **AWS Bedrock** | Managed foundation models | No GPU ops, enterprise-friendly | Less control than self-hosting | Pay per token | Fast AWS-native production |
| **Azure AI Foundry / Azure OpenAI** | Managed foundation models | Strong enterprise integration | Region/model availability varies | Pay per token | Azure-native production |
| **Google Vertex AI** | Gemini and managed ML | Good Google ecosystem integration | Less flexible than self-hosting | Pay per token / endpoint | Google-native production |
| **SageMaker / Azure ML / Vertex custom endpoints** | Custom model deployment | Managed training + serving | More platform complexity | Endpoint + compute cost | Classical ML and custom DL |
| **Cloud GPU (AWS/GCP/Azure)** | Self-hosted production | Full control, scalable | Complex setup, cost management | $1-5+/hour | High-volume production |
| **Modal** | Serverless GPU | Auto-scaling, easy | Limited control | Pay per second | Bursty workloads |
| **Replicate** | Model hosting | Easy deployment, many models | Higher cost | Pay per prediction | Quick deployment |
| **HuggingFace Inference** | Quick hosting | Many models, easy | Limited free tier | Free/Pay | Testing, demos |
| **Local (Ollama)** | Development, privacy | Free, private, fast iteration | Limited by hardware | Free (power cost) | Development, sensitive data |
| **vLLM** | Self-hosted serving | Very fast, efficient | Requires setup | Hosting cost | Production self-hosting |
| **TGI** | HuggingFace models | Optimized for HF models | HF ecosystem only | Hosting cost | HuggingFace models |
| **Triton Inference Server** | Mixed model fleets | Supports ONNX, TensorRT, PyTorch | More infra work | Hosting cost | Multi-model production |
| **ONNX Runtime** | Edge and portable inference | Fast, cross-platform, flexible | You still need hosting | Hosting/device cost | Edge, mobile, portable serving |
| **llama.cpp / SGLang / Ollama** | Open-source local or self-hosted | Maximum control, low cost | More ops and tuning | Infra cost | Open-weight models |

**Key distinction:**

- **Managed APIs**: Bedrock, Azure AI Foundry, Vertex AI.
- **Managed custom model platforms**: SageMaker, Azure ML, Vertex AI endpoints.
- **Open-source self-hosting**: vLLM, TGI, Triton, SGLang, Ollama, llama.cpp.
- **Portable runtime**: ONNX Runtime.

**By Requirements:**

**Privacy Critical:**
- Local with Ollama, llama.cpp, ONNX Runtime, or self-hosted vLLM

**Cost Optimization:**
1. **Low volume (<1M tokens/month)**: OpenAI API
2. **Medium (1-10M)**: Bedrock / Azure AI Foundry / Vertex AI or Claude
3. **High (>10M)**: Self-hosted vLLM / TGI / Triton on cloud GPU

**Speed Requirements:**
- **Fastest**: vLLM (self-hosted) or OpenAI API
- **Low latency**: Edge deployment (ONNX Runtime, TensorFlow Lite)
- **Batch processing**: Cloud GPU with large batches

**Development vs Production:**
- **Development**: Ollama (local) or OpenAI API
- **Production**: Bedrock / Azure AI Foundry / Vertex AI or vLLM / Triton
- **Hybrid**: Managed API for MVP, self-hosted for scale

---

## Quick Decision Guides

### "I want to build a RAG chatbot"

1. **Choose LLM:**
   - Development: GPT-4.1-mini or Claude Haiku 4.5
   - Production (budget): Qwen 3 8B (self-hosted) or Gemini 3.1 Flash
   - Production (quality): Claude Sonnet 4.6 or GPT-5.4

2. **Choose Embeddings:**
   - API (best): Gemini Embedding (cheapest + highest quality)
   - API (ecosystem): text-embedding-3-small or Voyage 3.5
   - Local: Qwen3-Embedding or all-mpnet-base-v2

3. **Choose Vector DB:**
   - Learning: ChromaDB
   - Production: Qdrant

4. **Deployment:**
   - MVP: OpenAI/Anthropic/Google API
   - Scale: vLLM + Cloud GPU

### "I need to fine-tune a model"

1. **Check if you really need fine-tuning:**
   - Try prompt engineering first
   - Try RAG (retrieval augmented generation)
   - Only fine-tune if the above don't work

2. **Choose method:**
   - Have 16GB+ VRAM → LoRA r=64 (use Unsloth for 2-5x speedup)
   - Have 8-16GB VRAM → QLoRA
   - Need best quality → DoRA

3. **Choose base model:**
   - General: Qwen 3 (0.6-32B) or Llama 4 Scout
   - Coding: Qwen 3-Coder or DeepSeek Coder V2
   - Chat: Qwen 3-Instruct or Llama 4
   - Tiny/edge: Phi-4 (14B) or Qwen 3 (0.6B-4B)

### "I need image understanding"

1. **Task type:**
   - Classification → CLIP or SigLIP
   - Detailed Q&A → GPT-5.4 or Gemini 3.1 Pro
   - Self-hosted → Qwen2.5-VL or LLaVA-OneVision
   - OCR + Understanding → Claude Sonnet 4.6 or GPT-5.4
   - Video → Gemini 3.1 Pro

---

**Last Updated:** April 2026  
**Repository:** [zero-to-ai](https://github.com/PavanMudigonda/zero-to-ai)

For detailed tutorials on any of these topics, see the relevant phase notebooks in the repository.
