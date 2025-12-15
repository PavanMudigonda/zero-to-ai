# LLM Production Optimization

## 🎯 Overview

Master the art of deploying LLMs cost-effectively and efficiently in production. Learn caching, batching, monitoring, and optimization strategies.

**Part of:** Phase 8 - MLOps

**Prerequisites:**
- ✅ Prompt Engineering (Phase 10)
- ✅ Local LLMs (Phase 13)
- ✅ Basic MLOps

**Outcome:** Deploy optimized, cost-effective LLM applications

---

## 📚 What You'll Learn

### Cost Optimization

- [ ] Token usage tracking and reduction
- [ ] Semantic caching strategies
- [ ] Batch processing for efficiency
- [ ] Model selection (cost vs. capability)
- [ ] Prompt compression techniques
- [ ] Fallback strategies (cheap → expensive)

### Performance Optimization

- [ ] Response time optimization
- [ ] Streaming responses
- [ ] Parallel processing
- [ ] Prefetching and speculation
- [ ] Edge deployment
- [ ] CDN for static responses

### Monitoring & Observability

- [ ] LLM metrics (latency, tokens, cost)
- [ ] Quality monitoring
- [ ] Error tracking
- [ ] User feedback loops
- [ ] A/B testing
- [ ] Cost alerts

### Infrastructure

- [ ] Load balancing
- [ ] Auto-scaling
- [ ] Rate limiting
- [ ] Circuit breakers
- [ ] Retry strategies
- [ ] Fallback models

---

## 🗂️ Module Structure

```
llm-optimization/
├── 00_START_HERE.ipynb                # Overview
├── 01_cost_tracking.ipynb             # Token counting & costs
├── 02_caching_strategies.ipynb        # Semantic caching
├── 03_batching.ipynb                  # Batch processing
├── 04_prompt_optimization.ipynb       # Reduce tokens
├── 05_monitoring.ipynb                # Production monitoring
├── 06_load_balancing.ipynb            # Scaling strategies
├── 07_fallback_patterns.ipynb         # Reliability
├── 08_benchmarking.ipynb              # Performance testing
├── examples/
│   ├── semantic_cache.py
│   ├── batch_processor.py
│   ├── cost_tracker.py
│   └── load_balancer.py
└── README.md
```

---

## 🚀 Quick Optimization Wins

### 1. Semantic Caching

```python
from openai import OpenAI
import hashlib
import redis

client = OpenAI()
cache = redis.Redis(host='localhost', port=6379, db=0)

def get_embedding_hash(text):
    """Create semantic hash for similar queries."""
    # Use embeddings for semantic similarity
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    embedding = response.data[0].embedding
    # Hash first few dimensions for bucketing
    return hashlib.md5(str(embedding[:10]).encode()).hexdigest()

def cached_completion(prompt, threshold=0.9):
    """Check cache before calling LLM."""
    cache_key = get_embedding_hash(prompt)
    
    # Check cache
    cached = cache.get(cache_key)
    if cached:
        return cached.decode(), 0  # $0 cost!
    
    # Call LLM
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    result = response.choices[0].message.content
    tokens = response.usage.total_tokens
    
    # Cache for 1 hour
    cache.setex(cache_key, 3600, result)
    
    return result, tokens

# Usage - similar queries hit cache!
result1, cost1 = cached_completion("What is Python?")
result2, cost2 = cached_completion("Tell me about Python")  # Cache hit!
```

### 2. Batch Processing

```python
from openai import OpenAI
import asyncio

client = OpenAI()

async def process_batch(prompts, batch_size=10):
    """Process prompts in batches for efficiency."""
    results = []
    
    for i in range(0, len(prompts), batch_size):
        batch = prompts[i:i+batch_size]
        
        # Create batch request
        tasks = [
            client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": p}]
            )
            for p in batch
        ]
        
        # Process in parallel
        responses = await asyncio.gather(*tasks)
        results.extend([r.choices[0].message.content for r in responses])
    
    return results

# 10x faster than sequential
prompts = ["Explain AI" for _ in range(100)]
results = asyncio.run(process_batch(prompts))
```

### 3. Prompt Compression

```python
def compress_prompt(long_prompt):
    """Reduce tokens while keeping meaning."""
    
    # Bad: Verbose prompt (200 tokens)
    bad_prompt = """
    I would like you to please help me understand the following concept.
    Could you please explain it in a way that is easy to understand?
    I am particularly interested in learning about the main points.
    Please make sure to cover all the important aspects.
    """
    
    # Good: Concise prompt (20 tokens)
    good_prompt = "Explain [concept] clearly. Cover main points."
    
    # 90% token reduction = 90% cost reduction!
    return good_prompt

# Techniques:
# - Remove filler words
# - Use abbreviations
# - Remove redundancy
# - Use structured format
# - System prompt for style (don't repeat)
```

### 4. Model Fallback

```python
from openai import OpenAI

client = OpenAI()

def smart_completion(prompt, complexity="auto"):
    """Use cheapest model that works."""
    
    if complexity == "auto":
        # Estimate complexity
        complexity = estimate_complexity(prompt)
    
    models = {
        "simple": "gpt-3.5-turbo",      # $0.50/1M tokens
        "medium": "gpt-4o-mini",        # $1.50/1M tokens  
        "complex": "gpt-4o"             # $15/1M tokens
    }
    
    try:
        model = models[complexity]
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    
    except Exception as e:
        # Fallback to more capable model
        if model != "gpt-4o":
            return smart_completion(prompt, "complex")
        raise e

def estimate_complexity(prompt):
    """Estimate task complexity."""
    keywords = {
        "simple": ["explain", "what is", "define"],
        "complex": ["analyze", "compare", "design", "code"]
    }
    
    prompt_lower = prompt.lower()
    for keyword in keywords["complex"]:
        if keyword in prompt_lower:
            return "complex"
    
    return "simple"

# 10x cost savings for simple queries!
```

---

## 📊 Cost Optimization Strategies

### Token Reduction Techniques

| Technique | Savings | Effort |
|-----------|---------|--------|
| Remove filler words | 10-20% | Low |
| Use abbreviations | 5-15% | Low |
| Compress examples | 20-40% | Medium |
| Smaller model | 50-95% | Medium |
| Semantic caching | 60-90% | High |
| Fine-tuned model | 50-80% | High |

### Model Selection Guide

```
Simple tasks (FAQ, classification):
└─ GPT-3.5-turbo or local 7B model

Medium tasks (summarization, extraction):
└─ GPT-4o-mini or local 13B model

Complex tasks (reasoning, analysis):
└─ GPT-4o or Claude 3.5 Sonnet

Very complex (code, math, research):
└─ o1-mini or o1-preview
```

### Caching Strategy

```
Level 1: Exact match cache (Redis)
├─ Hit rate: 20-30%
├─ Cost savings: High
└─ Latency: <1ms

Level 2: Semantic cache (Vector DB)
├─ Hit rate: 40-60%
├─ Cost savings: Medium
└─ Latency: 10-50ms

Level 3: Prefetch common queries
├─ Hit rate: 10-20%
├─ Cost savings: Medium
└─ Latency: <1ms
```

---

## 💡 Best Practices

### Cost Optimization

**DO ✅**
- Track all token usage
- Cache aggressively
- Use cheapest capable model
- Compress prompts
- Batch similar requests
- Set budget alerts
- Review costs weekly

**DON'T ❌**
- Use GPT-4 for everything
- Ignore caching
- Process one-by-one
- Keep verbose prompts
- Skip monitoring
- Forget rate limits

### Performance Optimization

**DO ✅**
- Stream responses
- Use async/parallel
- Implement timeouts
- Add retries with backoff
- Monitor latency
- Use CDN for static content
- Prefetch common queries

**DON'T ❌**
- Block on LLM calls
- Ignore streaming
- Skip error handling
- Use synchronous code
- Forget timeout limits

### Monitoring

```python
# Production monitoring template
import time
from dataclasses import dataclass

@dataclass
class LLMMetrics:
    model: str
    tokens_input: int
    tokens_output: int
    latency_ms: float
    cost_usd: float
    cache_hit: bool
    error: str = None

def track_llm_call(func):
    """Decorator to track LLM metrics."""
    def wrapper(*args, **kwargs):
        start = time.time()
        cache_hit = False
        error = None
        
        try:
            result, metrics = func(*args, **kwargs)
            cache_hit = metrics.get('cache_hit', False)
            
            # Log metrics
            log_metrics(LLMMetrics(
                model=metrics['model'],
                tokens_input=metrics['tokens_in'],
                tokens_output=metrics['tokens_out'],
                latency_ms=(time.time() - start) * 1000,
                cost_usd=calculate_cost(metrics),
                cache_hit=cache_hit
            ))
            
            return result
        
        except Exception as e:
            error = str(e)
            # Log error
            log_error(error)
            raise
    
    return wrapper
```

---

## 🔗 Resources

### Tools

- [LangSmith](https://www.langchain.com/langsmith) - LLM monitoring
- [Helicone](https://www.helicone.ai/) - LLM observability
- [Portkey](https://portkey.ai/) - Gateway & caching
- [LiteLLM](https://github.com/BerriAI/litellm) - Unified interface

### Cost Calculators

- [OpenAI Pricing](https://openai.com/api/pricing/)
- [Anthropic Pricing](https://www.anthropic.com/pricing)
- [Token Counter](https://platform.openai.com/tokenizer)

### Caching Solutions

- Redis (in-memory)
- GPTCache (semantic)
- Momento (managed)
- Upstash (serverless)

---

## ✅ Optimization Checklist

- [ ] Track all token usage
- [ ] Implement semantic caching
- [ ] Use appropriate model for task
- [ ] Compress prompts (remove filler)
- [ ] Batch similar requests
- [ ] Set up monitoring dashboard
- [ ] Configure cost alerts
- [ ] Test fallback strategies
- [ ] Implement rate limiting
- [ ] Monitor cache hit rate
- [ ] Review costs monthly
- [ ] Optimize based on metrics

---

## 📈 Expected Savings

**Well-optimized LLM application:**
- 60-80% cost reduction via caching
- 50-70% cost reduction via model selection
- 10-20% cost reduction via prompt optimization
- 3-10x latency improvement via streaming
- 5-20x throughput via batching

**Total:** **80-95% cost reduction** possible!

---

**Start optimizing:** Track your current costs first, then apply techniques incrementally.

**Measure everything:** You can't optimize what you don't measure!

**🚀 Remember: Every token saved is money saved!**
