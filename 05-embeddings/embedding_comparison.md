# Embedding Models Comparison Guide

> **Last Updated:** April 2026 — Covers latest models including Gemini Embedding, Cohere Embed v4, Jina v4, Voyage 4, and Qwen3-Embedding

Complete comparison of different embedding approaches: HuggingFace Transformers, Sentence Transformers, OpenAI, and the new wave of multimodal/multilingual API providers.

---

## Table of Contents

1. [Overview](#overview)
2. [Quick Comparison](#quick-comparison)
3. [HuggingFace Transformers](#huggingface-transformers)
4. [Sentence Transformers](#sentence-transformers)
5. [OpenAI Embeddings](#openai-embeddings)
6. [New in 2026: Additional Providers](#new-in-2026-additional-providers)
7. [Decision Tree](#decision-tree)
8. [Performance Benchmarks](#performance-benchmarks)
9. [Cost Analysis](#cost-analysis)
10. [Use Case Recommendations](#use-case-recommendations)

---

## Overview

### What Are Embeddings?

Embeddings are **dense vector representations** of text that capture semantic meaning. Similar texts have similar embeddings (measured by cosine similarity).

### Why Different Approaches?

| Factor | Trade-off |
|--------|-----------|
| **Quality** | Better models = larger, slower |
| **Speed** | Faster inference = simpler models |
| **Cost** | Self-hosted vs API costs |
| **Privacy** | Local vs cloud processing |
| **Flexibility** | Custom fine-tuning vs plug-and-play |

---

## Quick Comparison

| Feature | HuggingFace Transformers | Sentence Transformers | OpenAI | Cohere Embed v4 | Google Gemini | Voyage AI |
|---------|-------------------------|----------------------|--------|-----------------|---------------|-----------|
| **Setup Complexity** | ⭐⭐⭐ Medium | ⭐ Easy | ⭐ Easy | ⭐ Easy | ⭐ Easy | ⭐ Easy |
| **Inference Speed** | ⭐⭐ Slower | ⭐⭐⭐ Fast | ⭐⭐⭐ Fast | ⭐⭐⭐ Fast | ⭐⭐⭐ Fast | ⭐⭐⭐ Fast |
| **Quality (MTEB)** | ⭐⭐⭐ High | ⭐⭐⭐ High | ⭐⭐⭐⭐ Very High | ⭐⭐⭐⭐ Very High | ⭐⭐⭐⭐⭐ Best | ⭐⭐⭐⭐ Very High |
| **Cost** | Free (compute) | Free (compute) | $$$ Pay per use | $$ Pay per use | $ Very cheap | $$ Pay per use |
| **Privacy** | ✅ Local | ✅ Local | ❌ Cloud | ❌ Cloud | ❌ Cloud | ❌ Cloud |
| **Fine-tuning** | ✅ Full control | ✅ Easy | ❌ No | ❌ No | ❌ No | ❌ No |
| **Multilingual** | ✅ Available | ✅ Available | ✅ Yes | ✅ Best-in-class | ✅ Excellent | ✅ Yes |
| **Multimodal** | ❌ Text only | ❌ Text only | ❌ Text only | ✅ Text + Images | ✅ All modalities | ✅ Text + Images |
| **Matryoshka (MRL)** | ❌ No | ❌ No | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Embedding Dim** | 768-1024 | 384-768 | 1536-3072 | 1024 | 768-3072 | 256-2048 |
| **Max Context** | 512 | 512 | 8,191 | 128,000 | 8,192 | 32,000 |

---

## HuggingFace Transformers

### Overview

**Raw transformer models** (BERT, RoBERTa, etc.) from HuggingFace. Maximum flexibility but requires more code.

### Pros ✅

- **Full Control**: Access to all model layers and tokens
- **Customizable**: Choose pooling strategy, layers, tokens
- **Fine-tunable**: Easy to fine-tune on your data
- **Free**: Run locally, no API costs
- **Many Models**: Thousands of models on HuggingFace Hub

### Cons ❌

- **More Code**: Need to handle tokenization, pooling
- **Slower**: Not optimized for sentence embeddings
- **GPU Needed**: Slow on CPU for large models
- **Configuration**: Need to choose pooling strategy

### Best For

- Research and experimentation
- Custom fine-tuning requirements
- Token-level embeddings
- When you need full control

### Code Example

```python
from transformers import AutoTokenizer, AutoModel
import torch

# Load model
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModel.from_pretrained('bert-base-uncased')

# Generate embedding
text = "Machine learning is fascinating"
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

# Choose pooling strategy
cls_embedding = outputs.last_hidden_state[:, 0, :]  # CLS token
mean_embedding = outputs.last_hidden_state.mean(dim=1)  # Mean pooling
```

### Popular Models

| Model | Dimension | Parameters | Best For |
|-------|-----------|------------|----------|
| `bert-base-uncased` | 768 | 110M | General English |
| `roberta-base` | 768 | 125M | Better than BERT |
| `distilbert-base-uncased` | 768 | 66M | Faster, smaller |
| `bert-base-multilingual` | 768 | 110M | 104 languages |

---

## Sentence Transformers

### Overview

**Optimized models** specifically trained for sentence embeddings. Built on top of HuggingFace Transformers.

### Pros ✅

- **Simple API**: One line: `model.encode(texts)`
- **Optimized**: Trained specifically for similarity tasks
- **Fast**: Efficient inference
- **Pre-trained**: Many models ready to use
- **Free**: Run locally
- **Batching**: Built-in efficient batching

### Cons ❌

- **Less Flexible**: No access to individual tokens
- **Sentence-only**: Designed for sentence/document embeddings
- **GPU Recommended**: Still benefits from GPU

### Best For

- **Production semantic search**
- **Sentence similarity tasks**
- **Quick prototyping**
- **When quality + speed matter**

### Code Example

```python
from sentence_transformers import SentenceTransformer

# Load model (one line!)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings (super simple!)
texts = ["First sentence", "Second sentence"]
embeddings = model.encode(texts)

# That's it! Embeddings ready to use
```

### Popular Models

| Model | Dimension | Speed | Quality | Best For |
|-------|-----------|-------|---------|----------|
| `all-MiniLM-L6-v2` | 384 | ⚡⚡⚡ Fast | ⭐⭐⭐ Good | General purpose |
| `all-mpnet-base-v2` | 768 | ⚡⚡ Medium | ⭐⭐⭐⭐ Best | High quality |
| `paraphrase-multilingual-MiniLM-L12-v2` | 384 | ⚡⚡⚡ Fast | ⭐⭐⭐ Good | 50+ languages |
| `multi-qa-mpnet-base-dot-v1` | 768 | ⚡⚡ Medium | ⭐⭐⭐⭐ Best | Q&A, search |

### Model Selection Guide

```
For general use:
  - Fast + good quality → all-MiniLM-L6-v2
  - Best quality → all-mpnet-base-v2

For specific tasks:
  - Semantic search → multi-qa-mpnet-base-dot-v1
  - Code search → code-search-net
  - Multilingual → paraphrase-multilingual-MiniLM-L12-v2

For constraints:
  - Limited compute → all-MiniLM-L6-v2 (384 dim)
  - High accuracy needed → all-mpnet-base-v2 (768 dim)
```

---

## OpenAI Embeddings

### Overview

**Cloud-based API** providing state-of-the-art embeddings. No local hosting needed.

### Pros ✅

- **Highest Quality**: State-of-the-art performance
- **No Infrastructure**: No GPUs, no hosting
- **Always Updated**: Latest models automatically
- **Scalable**: Handle any volume
- **Simple API**: One API call

### Cons ❌

- **Cost**: Pay per token ($$$)
- **Privacy**: Data sent to OpenAI
- **Latency**: Network overhead
- **Dependency**: Requires internet + API key
- **No Fine-tuning**: Can't customize

### Best For

- **Enterprise applications** with budget
- **When quality is critical**
- **No ML infrastructure**
- **Rapid prototyping**

### Code Example

```python
import openai

openai.api_key = "your-api-key"

# Generate embeddings
response = openai.embeddings.create(
    input=["Text to embed"],
    model="text-embedding-3-small"
)

embedding = response.data[0].embedding
```

### Available Models

| Model | Dimension | Cost per 1M tokens | Batch Price | Best For |
|-------|-----------|-------------------|-------------|----------|
| `text-embedding-3-small` | 1536 | $0.02 | $0.01 | Cost-effective |
| `text-embedding-3-large` | 3072 | $0.13 | $0.065 | Highest quality |
| `text-embedding-ada-002` | 1536 | $0.10 | $0.05 | Legacy (deprecated) |

> **Tip:** Use the Batch API for 50% savings on bulk embedding jobs (12-hour completion window).

### Cost Calculator

```
Assumptions:
- Average text: 100 tokens
- 1M documents = 100M tokens

Costs for 1M documents:
- text-embedding-3-small: $2 (Batch: $1)
- text-embedding-3-large: $13 (Batch: $6.50)

Monthly costs (re-embedding 1M docs):
- Small model: $24/year (Batch: $12/year)
- Large model: $156/year (Batch: $78/year)
```

---

## New in 2026: Additional Providers

The embedding landscape has expanded significantly. Here are the major new players:

### Google Gemini Embedding

**#1 on MTEB English leaderboard** (score: 68.32) as of March 2026.

```python
import google.generativeai as genai

genai.configure(api_key="your-api-key")

result = genai.embed_content(
    model="models/gemini-embedding-001",
    content="Text to embed",
    task_type="RETRIEVAL_DOCUMENT"
)
embedding = result['embedding']  # 3072 dimensions (truncatable to 768)
```

| Feature | Detail |
|---------|--------|
| **Dimensions** | 3072 (truncatable to 768 via MRL) |
| **Max tokens** | 8,192 |
| **Cost** | ~$0.004 per 1K characters (effectively negligible) |
| **Modalities** | Text, images, video, audio, code (all 5 modalities) |
| **Strengths** | Best MTEB score, best cross-lingual, best long documents |

### Cohere Embed v4

Enterprise-focused multimodal embedding with best-in-class multilingual support.

```python
import cohere

co = cohere.Client("your-api-key")

response = co.embed(
    texts=["Text to embed"],
    model="embed-v4.0",
    input_type="search_document",
    embedding_types=["float"]
)
embedding = response.embeddings.float[0]
```

| Feature | Detail |
|---------|--------|
| **Dimensions** | 1024 |
| **Max tokens** | 128,000 (longest context of any embedding model) |
| **Cost** | $0.12 per 1M tokens |
| **Modalities** | Text + images |
| **Strengths** | Multilingual leader, handles noisy enterprise documents, pairs with Cohere Reranker |

### Voyage AI (Anthropic's Recommended Provider)

Best Matryoshka (MRL) performance. Generous free tier (200M tokens).

```python
import voyageai

vo = voyageai.Client(api_key="your-api-key")

result = vo.embed(
    ["Text to embed"],
    model="voyage-3.5",
    output_dimension=1024
)
embedding = result.embeddings[0]
```

| Model | Dimensions | Cost/1M tokens | Best For |
|-------|-----------|----------------|----------|
| `voyage-4-large` | 256-2048 | ~$0.22 | Highest quality |
| `voyage-4` | 256-2048 | ~$0.12 | General purpose |
| `voyage-3.5` | 256-2048 | $0.06 | Best value |
| `voyage-code-3` | 256-2048 | $0.06 | Code search |
| `voyage-finance-2` | 1024 | Domain-specific | Finance |
| `voyage-law-2` | 1024 | Domain-specific | Legal |

> **Free tier:** 200M tokens for voyage-3.5/3-large/code-3. Best free tier among API providers.

### Jina Embeddings v4

Universal multimodal model built on Qwen2.5-VL (3.8B params). Supports text, images, and PDFs.

| Feature | Detail |
|---------|--------|
| **Dimensions** | 2048 (truncatable to 128 via MRL) |
| **Max tokens** | 32,000 |
| **Architecture** | Decoder-only (Qwen2.5-VL backbone) |
| **Modalities** | Text + images + visual documents (PDFs) |
| **Task adapters** | 3 LoRA adapters (retrieval, similarity, code) |
| **License** | CC-BY-NC-4.0 (commercial use requires API) |

### Qwen3-Embedding (Open Source)

Best open-source embedding model. Apache 2.0 license.

| Feature | Detail |
|---------|--------|
| **Parameters** | 8B |
| **Dimensions** | 32-7168 (flexible via MRL) |
| **Max tokens** | 32,000 |
| **Languages** | 100+ natural languages + code |
| **MMTEB score** | 70.58 (#1 multilingual) |
| **License** | Apache 2.0 (fully commercial) |

### BGE-M3 (Open Source)

The Swiss Army knife of open-source embeddings: dense + sparse + multi-vector in one model.

| Feature | Detail |
|---------|--------|
| **Dimensions** | 1024 |
| **Max tokens** | 8,192 |
| **Retrieval modes** | Dense, sparse, and multi-vector (ColBERT-style) |
| **Languages** | 100+ |
| **License** | Apache 2.0 |
| **MTEB score** | ~63.0 |

---

## Decision Tree

### Choose Your Approach

```
START
│
├─ Do you have budget for API costs?
│  ├─ YES → Do you need multimodal (images/PDFs)?
│  │        ├─ YES → Gemini Embedding (all modalities) or Cohere Embed v4
│  │        └─ NO → Need highest quality?
│  │            ├─ YES → Gemini Embedding (#1 MTEB) or Voyage 4-large
│  │            ├─ CHEAPEST → Gemini Embedding (~$0.004/1K chars)
│  │            └─ BALANCED → Voyage 3.5 ($0.06/1M) or OpenAI 3-small ($0.02/1M)
│  │
│  └─ NO (or prefer self-hosted)
│     │
│     ├─ Do you need multimodal?
│     │  └─ YES → Jina v4 (text + images + PDFs)
│     │
│     ├─ Do you need best open-source quality?
│     │  └─ YES → Qwen3-Embedding-8B (Apache 2.0, #1 MMTEB)
│     │
│     ├─ Do you need hybrid retrieval (dense + sparse)?
│     │  └─ YES → BGE-M3 (dense + sparse + multi-vector)
│     │
│     ├─ Do you need token-level embeddings?
│     │  └─ YES → HuggingFace Transformers
│     │
│     ├─ Do you need to fine-tune?
│     │  ├─ HEAVILY → HuggingFace Transformers
│     │  └─ SLIGHTLY → Sentence Transformers (easier)
│     │
│     └─ Just need sentence embeddings?
│        ├─ Quality > Speed → all-mpnet-base-v2
│        └─ Speed > Quality → all-MiniLM-L6-v2
```

### Quick Decision Guide (April 2026)

| Your Situation | Recommendation |
|----------------|----------------|
| Startup with limited budget | Gemini Embedding (nearly free API) or Sentence Transformers (local) |
| Enterprise with ML budget | Cohere Embed v4 (enterprise features) or Voyage 4-large |
| Best quality overall | Gemini Embedding (#1 MTEB) |
| Research project | HuggingFace Transformers or Qwen3-Embedding |
| Production semantic search | Voyage 3.5 or Sentence Transformers |
| Need absolute best quality | Gemini Embedding or Voyage 4-large |
| Processing sensitive data | Qwen3-Embedding or Sentence Transformers (local) |
| Need multimodal (images + text) | Gemini Embedding or Jina v4 |
| Need to fine-tune on domain data | HuggingFace Transformers |
| Building MVP quickly | OpenAI text-embedding-3-small or Gemini |
| Domain-specific (code/legal/finance) | Voyage AI (code-3, law-2, finance-2) |
| Long documents (>8K tokens) | Cohere Embed v4 (128K) or Jina v4 (32K) |
| Multilingual at scale | Qwen3-Embedding (100+ langs, Apache 2.0) or Cohere v4 |

---

## Performance Benchmarks

### Speed Comparison

Processing 10,000 sentences (CPU):

| Method | Model | Time | Sentences/sec |
|--------|-------|------|---------------|
| Sentence Transformers | all-MiniLM-L6-v2 | 45s | 222 |
| Sentence Transformers | all-mpnet-base-v2 | 120s | 83 |
| HuggingFace | bert-base-uncased | 180s | 56 |
| HuggingFace | roberta-base | 200s | 50 |
| OpenAI | text-embedding-3-small | 30s* | 333 |

*Network latency included, parallel API calls

### GPU Speedup

With GPU (NVIDIA T4):

| Method | CPU Time | GPU Time | Speedup |
|--------|----------|----------|---------|
| Sentence Transformers (MiniLM) | 45s | 8s | 5.6x |
| Sentence Transformers (MPNet) | 120s | 18s | 6.7x |
| HuggingFace (BERT) | 180s | 25s | 7.2x |

### Quality Comparison

#### MTEB English Leaderboard (March 2026)

| Model | MTEB Score | Type | Dimensions |
|-------|-----------|------|------------|
| Google Gemini Embedding 001 | 68.32 | API | 3072 |
| Cohere Embed v4 | 65.2 | API | 1024 |
| OpenAI text-embedding-3-large | 64.6 | API | 3072 |
| Qwen3-Embedding-8B | ~64 | Open-source | 7168 |
| BGE-M3 | 63.0 | Open-source | 1024 |
| all-mpnet-base-v2 | ~59 | Sentence-T | 768 |
| all-MiniLM-L6-v2 | 56.3 | Sentence-T | 384 |

> **Note:** MTEB scores are self-reported. The leaderboard is an average across tasks; a model that dominates classification may underperform on retrieval. See [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard).

#### MMTEB Multilingual Leaderboard

| Model | MMTEB Score | Languages |
|-------|-----------|-----------|
| Qwen3-Embedding-8B | 70.58 | 100+ |
| NVIDIA Llama-Embed-Nemotron-8B | ~69 | 100+ |
| Cohere Embed v4 | ~66 | 100+ |
| BGE-M3 | ~63 | 100+ |

#### Semantic Textual Similarity Benchmark (STS-B)

| Model | Correlation | Type |
|-------|-------------|------|
| Gemini Embedding 001 | 0.93 | API |
| OpenAI text-embedding-3-large | 0.91 | API |
| all-mpnet-base-v2 | 0.88 | Sentence-T |
| OpenAI text-embedding-3-small | 0.87 | API |
| all-MiniLM-L6-v2 | 0.82 | Sentence-T |
| bert-base-uncased (CLS) | 0.76 | HuggingFace |
| bert-base-uncased (mean) | 0.81 | HuggingFace |

**Key Insights:**
- Sentence Transformers models still outperform raw BERT even though BERT is larger
- Gemini Embedding now leads the pack at negligible cost
- Open-source models (Qwen3, BGE-M3) are closing the gap with commercial APIs
- Matryoshka Representation Learning (MRL) lets you trade dimensions for speed with minimal quality loss

---

## Cost Analysis

### Self-Hosted (Sentence Transformers)

**Fixed Costs:**
```
Hardware Options:
1. Cloud VM with GPU:
   - AWS g4dn.xlarge: $0.526/hour = $380/month
   - GCP n1-standard-4 + T4: $0.45/hour = $325/month
   
2. CPU-only (slower):
   - AWS c6i.2xlarge: $0.34/hour = $245/month
   - Can process ~1M sentences/day

3. Your own GPU:
   - One-time: $1000-5000 for GPU
   - Electricity: ~$20-50/month
```

**Variable Costs:**
- Electricity only
- Scales with usage

**Break-even:**
- If processing >10M sentences/month → Self-hosted cheaper
- If sporadic usage → OpenAI cheaper

### API Providers (April 2026 Pricing)

**Cost per 1M tokens:**
```
Gemini Embedding:              ~$0.004/1K chars (nearly free!)
OpenAI text-embedding-3-small: $0.02   (Batch: $0.01)
Voyage 3.5:                    $0.06
OpenAI text-embedding-3-large: $0.13   (Batch: $0.065)
Cohere Embed v4:               $0.12
Voyage 4-large:                ~$0.22
```

**Free Tiers:**
- **Voyage AI:** 200M tokens free (voyage-3.5, 3-large, code-3)
- **Gemini:** Generous free tier included with Google AI Studio
- **Cohere:** Trial API key with rate limits

### Cost Comparison Example

Embedding 10M sentences (100 tokens each = 1B tokens/month):

| Solution | Setup Cost | Monthly Cost | Total Year 1 |
|----------|-----------|--------------|--------------|
| Gemini Embedding | $0 | ~$4 | ~$48 |
| OpenAI Small | $0 | $20 | $240 |
| Voyage 3.5 | $0 | $60 | $720 |
| Cohere Embed v4 | $0 | $120 | $1,440 |
| OpenAI Large | $0 | $130 | $1,560 |
| Cloud GPU (self-hosted) | $0 | $380 | $4,560 |
| Own GPU | $2,000 | $30 | $2,360 |

**Recommendation (2026):**
- <5M sentences/month → Gemini Embedding (cheapest API) or OpenAI Small
- 5-20M sentences/month → Gemini or Voyage 3.5
- >20M sentences/month → Self-hosted (Qwen3-Embedding or BGE-M3)
- Domain-specific needs → Voyage domain models (code, law, finance)

---

## Use Case Recommendations

### Semantic Search

**Best Choice:** Sentence Transformers (`multi-qa-mpnet-base-dot-v1`)

**Why:**
- Specifically trained for search
- Fast inference
- Good quality
- Can fine-tune on your data

**Alternative:** OpenAI (if quality > cost)

---

### Chatbot / Q&A

**Best Choice:** OpenAI `text-embedding-3-small`

**Why:**
- Highest quality understanding
- Low latency needs
- Relatively low volume
- Worth the cost

**Alternative:** Sentence Transformers (`all-mpnet-base-v2`) for budget-conscious

---

### Document Clustering

**Best Choice:** Sentence Transformers (`all-mpnet-base-v2`)

**Why:**
- Batch processing (not real-time)
- Large volumes
- One-time or infrequent
- Quality matters

---

### Recommendation Engine

**Best Choice:** Sentence Transformers (`all-MiniLM-L6-v2`)

**Why:**
- Speed critical (real-time)
- High volume
- Good-enough quality
- Cost matters

---

### Research / Experimentation

**Best Choice:** HuggingFace Transformers

**Why:**
- Full flexibility
- Can experiment with different models
- Access to all layers
- Fine-tuning capability

---

### Multilingual Application

**Best Choice:** Sentence Transformers (`paraphrase-multilingual-MiniLM-L12-v2`)

**Why:**
- Supports 50+ languages
- Single model for all languages
- Good cross-lingual similarity
- Free

**Alternative:** OpenAI (better quality, especially for less common languages)

---

### Production Enterprise App

**Best Choice:** Hybrid Approach

```python
# Use OpenAI for critical queries (5%)
if is_critical_query(query):
    embedding = openai_embedding(query)
else:
    # Use Sentence Transformers for bulk (95%)
    embedding = local_model.encode(query)
```

**Why:**
- Balance cost and quality
- Optimize for 80/20 rule
- Fallback if API fails

---

## Migration Path

### Starting Out
1. **Prototype:** OpenAI (fastest to implement)
2. **Evaluate:** Sentence Transformers (test quality)
3. **Compare:** Measure quality difference
4. **Decide:** Based on volume and budget

### Growing
1. **Start:** Sentence Transformers
2. **Monitor:** Track inference time and quality
3. **Optimize:** Fine-tune if needed
4. **Scale:** Add GPUs as volume grows

### Enterprise
1. **Hybrid:** OpenAI for critical + Sentence-T for bulk
2. **Redundancy:** Have both deployed
3. **Monitor:** Track costs and quality continuously
4. **Optimize:** Regularly re-evaluate

---

## Summary

### TL;DR (April 2026)

| Need | Use This |
|------|----------|
| Quick start | Sentence Transformers or Gemini Embedding API |
| Best quality (API) | Gemini Embedding (#1 MTEB) or Voyage 4-large |
| Best quality (open-source) | Qwen3-Embedding-8B |
| Cheapest API | Gemini Embedding (~$0.004/1K chars) |
| High volume (self-hosted) | Qwen3-Embedding or BGE-M3 + GPU |
| Research | HuggingFace Transformers |
| Multilingual | Qwen3-Embedding (100+ langs) or Cohere v4 |
| Sensitive data (local) | Qwen3-Embedding or Sentence Transformers |
| Token embeddings | HuggingFace Transformers |
| Multimodal (images + text) | Gemini Embedding or Jina v4 |
| Long documents (>8K) | Cohere v4 (128K) or Jina v4 (32K) |
| Domain-specific | Voyage AI (code-3, law-2, finance-2) |
| Production hybrid | Gemini/Voyage for critical + Sentence-T for bulk |

### Golden Rules

1. **Start simple:** Gemini Embedding API (nearly free) or Sentence Transformers (local)
2. **Test quality:** Compare with your data using MTEB eval before committing
3. **Consider Matryoshka:** Many 2026 models support dimension reduction (3072 → 768) with minimal quality loss
4. **Monitor costs:** Track as you scale — Gemini and Voyage 3.5 are the best value APIs
5. **Open-source is competitive:** Qwen3-Embedding and BGE-M3 rival commercial APIs
6. **Keep options open:** Design for easy model swapping with a common embedding interface

### Next Steps

1. Try Gemini Embedding API (free tier) or `all-MiniLM-L6-v2` locally
2. Compare quality with your actual data using cosine similarity
3. If open-source: try Qwen3-Embedding-8B or BGE-M3
4. Measure inference speed and calculate expected costs
5. Check the [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) for latest rankings

---

**Need Help Choosing?** Consider:
- Volume per month?
- Budget constraints?
- Quality requirements?
- Infrastructure available?
- Privacy requirements?
- Multimodal needs (images, PDFs)?
- Long-document support needed?

Answer these questions, then revisit the [Decision Tree](#decision-tree)!
