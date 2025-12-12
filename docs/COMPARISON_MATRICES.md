# AI/ML Decision Matrices & Comparison Guides

> Quick reference for choosing the right tools, models, and approaches for your AI/ML projects (December 2025)

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

**When should you use which LLM?**

| Model | Best For | Pros | Cons | Cost (1M tokens) | When to Use |
|-------|----------|------|------|------------------|-------------|
| **GPT-4o** | Production, multimodal | Best quality, 128k context, vision | Expensive | $2.50 in / $10 out | Complex tasks, multimodal, production apps |
| **GPT-4o-mini** | Development, testing | Fast, cheap, good quality | Not as capable as GPT-4o | $0.15 in / $0.60 out | Development, high-volume tasks, chatbots |
| **o1-preview** | Research, reasoning | Best reasoning, complex problems | Slow, expensive, no streaming | $15 in / $60 out | Math, coding, research, complex analysis |
| **o1-mini** | Coding, math | Fast reasoning, cost-effective | Limited general knowledge | $3 in / $12 out | Code generation, STEM problems |
| **Claude 3.5 Sonnet** | Coding, analysis | Excellent at code, 200k context | API only | $3 in / $15 out | Code reviews, long documents, analysis |
| **Llama 3.3 70B** | Self-hosted production | Free, good quality, customizable | Requires GPU | Free (hosting cost) | Privacy needs, cost-sensitive, customization |
| **Qwen 2.5 (7-72B)** | Multilingual, coding | Best open-source, multilingual | Requires hosting | Free (hosting cost) | Non-English, code, self-hosting |
| **Gemini 1.5 Pro** | Multimodal, long context | 2M context, video understanding | Limited availability | $1.25 in / $5 out | Extremely long documents, video |

**Decision Tree:**
```
Need multimodal (images/vision)? 
├─ Yes → GPT-4o or Gemini 1.5 Pro
└─ No → Need complex reasoning?
    ├─ Yes → o1-preview (research) or o1-mini (coding)
    └─ No → Need self-hosting?
        ├─ Yes → Llama 3.3 70B or Qwen 2.5
        └─ No → Budget conscious?
            ├─ Yes → GPT-4o-mini or Claude Haiku
            └─ No → GPT-4o or Claude 3.5 Sonnet
```

---

## Vision Models

**Choosing between vision-language models**

| Model | Best For | Pros | Cons | Cost | When to Use |
|-------|----------|------|------|------|-------------|
| **GPT-4o** | Complex understanding | Best quality, detailed analysis | Expensive | $0.01/image | Complex scene understanding, OCR+reasoning |
| **GPT-4V** | Production vision | Reliable, well-documented | Being replaced by 4o | $0.01/image | Legacy applications |
| **CLIP** | Embeddings, classification | Fast, zero-shot, embeddings | Limited understanding | Free (self-host) | Image search, zero-shot classification |
| **LLaVA 1.6** | Self-hosted VQA | Open-source, customizable | Requires GPU | Free (hosting) | Privacy needs, custom fine-tuning |
| **Qwen2-VL** | Advanced self-hosting | Best open-source quality | Large model | Free (hosting) | High-quality self-hosted VQA |
| **CogVLM2** | Document understanding | Good at OCR, charts | Specialized use | Free (hosting) | Document analysis, charts |

**Use Case Guide:**
- **Image Search/Similarity**: CLIP (fast, efficient)
- **Image Captioning**: GPT-4o (best quality) or LLaVA 1.6 (self-hosted)
- **Visual Question Answering**: GPT-4o (production) or Qwen2-VL (self-hosted)
- **OCR + Understanding**: GPT-4o or CogVLM2
- **Zero-shot Classification**: CLIP

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
```
GPU VRAM Available:
├─ >40GB → Full fine-tuning (best quality)
├─ 16-40GB → LoRA r=64 or DoRA (recommended)
├─ 8-16GB → LoRA r=32 or QLoRA
└─ <8GB → QLoRA (4-bit) or Prompt Tuning

Quality Requirements:
├─ Critical → Full fine-tuning or DoRA
├─ High → LoRA r=64 or DoRA  
├─ Medium → LoRA r=32 or QLoRA
└─ Basic → Adapters or Prompt Tuning
```

**2025 Best Practices:**
- **Default choice**: LoRA with r=64, RSLoRA enabled
- **Budget GPU**: QLoRA with 4-bit quantization
- **Best quality**: DoRA with r=64 (new in 2024)
- **Fastest**: Adapters for quick iteration

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

**Choosing the right embedding model**

| Model | Type | Dimensions | Quality | Speed | Cost | When to Use |
|-------|------|------------|---------|-------|------|-------------|
| **text-embedding-3-large** | API | 3072 | Excellent | Fast | $0.13/1M | Production, best quality |
| **text-embedding-3-small** | API | 1536 | Very good | Very fast | $0.02/1M | Cost-sensitive production |
| **all-MiniLM-L6-v2** | Local | 384 | Good | Very fast | Free | Development, speed critical |
| **all-mpnet-base-v2** | Local | 768 | Very good | Fast | Free | General purpose, local |
| **e5-large-v2** | Local | 1024 | Excellent | Medium | Free | Best open-source quality |
| **bge-large-en-v1.5** | Local | 1024 | Excellent | Medium | Free | English, high quality |
| **multilingual-e5-large** | Local | 1024 | Very good | Medium | Free | Multi language support |

**Decision Factors:**

**By Requirement:**
- **Best Quality**: text-embedding-3-large (API) or e5-large-v2 (local)
- **Best Speed**: all-MiniLM-L6-v2 (local) or text-embedding-3-small (API)
- **Best Cost**: Any local model (free)
- **Multilingual**: multilingual-e5-large
- **Production API**: text-embedding-3-small (balanced)

**Typical Use Cases:**
- **RAG chatbots**: text-embedding-3-small or all-mpnet-base-v2
- **Semantic search**: e5-large-v2 or bge-large-en-v1.5
- **Document Q&A**: text-embedding-3-large
- **Fast prototyping**: all-MiniLM-L6-v2

---

## Image Generation

**Choosing image generation solutions**

| Solution | Quality | Speed | Cost | Control | When to Use |
|----------|---------|-------|------|---------|-------------|
| **DALL-E 3** | Excellent | Fast | $0.04-0.12/image | Low | Quick results, no setup |
| **Midjourney** | Excellent | Medium | $10-60/month | Medium | Best artistic quality |
| **FLUX.1-dev** | Best | Slow | Free (GPU cost) | High | Best open-source, photorealism |
| **SD 3.5 Large** | Excellent | Medium | Free (GPU cost) | High | Production self-hosted |
| **SDXL Turbo** | Very good | Very fast | Free (GPU cost) | High | Fast iteration, prototyping |
| **SDXL** | Very good | Medium | Free (GPU cost) | High | Balanced quality/speed |
| **SD 1.5** | Good | Fast | Free (GPU cost) | Very high | Legacy, LoRA ecosystem |

**Decision Tree:**
```
Need absolute best quality?
├─ Yes, willing to pay → Midjourney
├─ Yes, self-hosted → FLUX.1-dev
└─ No → Need very fast generation?
    ├─ Yes → SDXL Turbo or DALL-E 3
    └─ No → Have GPU?
        ├─ Yes → SD 3.5 or SDXL
        └─ No → DALL-E 3 (API)
```

**By Use Case:**
- **Product mockups**: DALL-E 3 (fast, reliable)
- **Artistic projects**: Midjourney or FLUX.1
- **Photorealistic images**: FLUX.1-dev
- **High-volume generation**: SDXL Turbo (self-hosted)
- **Custom fine-tuning**: SDXL or SD 1.5
- **Production apps**: SD 3.5 or API (DALL-E)

---

## Deployment Options

**Where and how to deploy your AI models**

| Option | Best For | Pros | Cons | Cost | When to Use |
|--------|----------|------|------|------|-------------|
| **OpenAI API** | Quick production | No infrastructure, reliable | Expensive at scale, data privacy | Pay per token | MVP, low-medium volume |
| **Anthropic (Claude)** | Production apps | Great models, reliable | Limited models | Pay per token | Production chatbots |
| **Cloud GPU (AWS/GCP)** | Self-hosted production | Full control, scalable | Complex setup, cost management | $1-5/hour | High-volume production |
| **Modal** | Serverless GPU | Auto-scaling, easy | Limited control | Pay per second | Bursty workloads |
| **Replicate** | Model hosting | Easy deployment, many models | Higher cost | Pay per prediction | Quick deployment |
| **HuggingFace Inference** | Quick hosting | Many models, easy | Limited free tier | Free/Pay | Testing, demos |
| **Local (Ollama)** | Development, privacy | Free, private, fast iteration | Limited by hardware | Free (power cost) | Development, sensitive data |
| **vLLM** | Self-hosted serving | Very fast, efficient | Requires setup | Hosting cost | Production self-hosting |
| **TGI** | HuggingFace models | Optimized for HF models | HF ecosystem only | Hosting cost | HuggingFace models |

**By Requirements:**

**Privacy Critical:**
- Local with Ollama or self-hosted vLLM

**Cost Optimization:**
1. **Low volume (<1M tokens/month)**: OpenAI API
2. **Medium (1-10M)**: Replicate or Claude
3. **High (>10M)**: Self-hosted on cloud GPU

**Speed Requirements:**
- **Fastest**: vLLM (self-hosted) or OpenAI API
- **Low latency**: Edge deployment (TensorFlow Lite, ONNX)
- **Batch processing**: Cloud GPU with large batches

**Development vs Production:**
- **Development**: Ollama (local) or OpenAI API
- **Production**: vLLM (self-hosted) or OpenAI/Claude API
- **Hybrid**: API for dev, self-hosted for production

---

## Quick Decision Guides

### "I want to build a RAG chatbot"

1. **Choose LLM:**
   - Development: GPT-4o-mini
   - Production (budget): Qwen 2.5 7B (self-hosted)
   - Production (quality): GPT-4o

2. **Choose Embeddings:**
   - API: text-embedding-3-small
   - Local: all-mpnet-base-v2

3. **Choose Vector DB:**
   - Learning: ChromaDB
   - Production: Qdrant

4. **Deployment:**
   - MVP: OpenAI API
   - Scale: vLLM + Cloud GPU

### "I need to fine-tune a model"

1. **Check if you really need fine-tuning:**
   - Try prompt engineering first
   - Try RAG (retrieval augmented generation)
   - Only fine-tune if the above don't work

2. **Choose method:**
   - Have 16GB+ VRAM → LoRA r=64
   - Have 8-16GB VRAM → QLoRA
   - Need best quality → DoRA

3. **Choose base model:**
   - General: Llama 3.2 (3B) or Qwen 2.5 (7B)
   - Coding: Qwen 2.5-Coder or Phi-4
   - Chat: Qwen 2.5-Instruct or Llama 3.2-Instruct

### "I need image understanding"

1. **Task type:**
   - Classification → CLIP
   - Detailed Q&A → GPT-4o
   - Self-hosted → Qwen2-VL or LLaVA 1.6
   - OCR + Understanding → GPT-4o

---

**Last Updated:** December 2025  
**Repository:** [zero-to-ai](https://github.com/PavanMudigondaTR/zero-to-ai)

For detailed tutorials on any of these topics, see the relevant phase notebooks in the repository.
