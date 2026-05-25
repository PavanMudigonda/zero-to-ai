#!/usr/bin/env python3
"""
Create stub notebooks for 30-inference-optimization planned content.
Run from repo root: python3 scripts/create_inference_notebooks.py
"""
import json
import os

BASE = os.path.join(
    os.path.dirname(__file__), "..", "jupyter-notebooks", "30-inference-optimization"
)

NOTEBOOKS = [
    {
        "folder": "03_kv_cache_paged_attention",
        "filename": "03_kv_cache_paged_attention.ipynb",
        "cells": [
            {
                "type": "markdown",
                "source": """# KV Cache & PagedAttention

> **Status:** Content notebook — theory complete, hands-on exercises require a GPU runtime.

## Learning Objectives

By the end of this notebook, you will be able to:

- [ ] Explain the Key-Value (KV) cache and why it exists in autoregressive decoding
- [ ] Describe the memory layout of KV cache tensors and how they scale with batch size and sequence length
- [ ] Understand the memory fragmentation problem that PagedAttention solves
- [ ] Explain how vLLM's PagedAttention manages non-contiguous KV blocks
- [ ] Estimate KV cache memory requirements for a given model and request profile
- [ ] Identify when KV cache is the bottleneck vs compute

---

## Prerequisites

- [01_START_HERE.ipynb](../01_START_HERE/01_START_HERE.ipynb)
- Basic understanding of the transformer architecture (Phase 6)
- Familiarity with GPU memory concepts

---

## 1. Why Does a KV Cache Exist?

During autoregressive decoding, a transformer generates one token at a time.
At each step, the attention mechanism computes queries, keys, and values for
**all** positions in the sequence so far. Without caching, the K and V tensors
for earlier tokens would be recomputed at every step.

The **KV cache** stores the K and V projections for all previously generated tokens,
so each decoding step only computes K/V for the **new** token and appends it to the cache.

```
Memory per token (per layer) = 2 × (num_heads × head_dim) × dtype_bytes
```

For Llama-3 8B (32 layers, 32 heads, head_dim=128, float16):
- Per token, per layer = 2 × (32 × 128) × 2 bytes = **16 KB**
- For 4096-token sequence, full cache = 16 KB × 32 layers = **2 GB**

---

## 2. The Memory Fragmentation Problem

Traditional KV cache implementations pre-allocate a **contiguous block** of GPU memory
per request, sized for the maximum possible sequence length. This causes:

1. **Internal fragmentation** — short requests waste reserved memory
2. **No memory sharing** — parallel decoding cannot share prefix cache blocks
3. **Poor batching** — unpredictable actual lengths make batching inefficient

---

## 3. PagedAttention

PagedAttention (introduced in vLLM, OSDI 2023) manages KV cache using **fixed-size blocks**
(pages), similar to virtual memory paging in operating systems.

Key design choices:
- Each block holds a fixed number of tokens (block_size = 16 or 32 typically)
- Blocks are allocated on-demand, not pre-allocated
- Non-contiguous physical blocks are mapped through a **block table**
- Prefix blocks can be **shared** across requests with the same prefix

```
Block Table for Request A:
  logical block 0 → physical block 7
  logical block 1 → physical block 2
  logical block 2 → physical block 15 (still being filled)
```

---

## 4. Memory Layout Calculation

The GPU memory budget for KV cache is whatever remains after loading model weights.

```
kv_cache_bytes = (gpu_memory_total - model_weight_bytes) × gpu_memory_utilization
num_blocks = kv_cache_bytes // (block_size × 2 × num_layers × num_heads × head_dim × dtype_bytes)
```

vLLM computes this automatically at startup and reports:
```
# vLLM startup log example
INFO: # GPU blocks: 2048, # CPU blocks: 512
```

---

## 5. Measuring KV Cache Pressure

```python
# Inspect vLLM KV cache stats (requires vLLM installed with GPU)
from vllm import LLM, SamplingParams

llm = LLM(model="meta-llama/Meta-Llama-3-8B-Instruct", gpu_memory_utilization=0.90)

# After inference, check cache usage via metrics
# llm.llm_engine.scheduler.block_manager.get_num_free_gpu_blocks()
```

---

## 6. Key Metrics

| Metric | What it measures | Target |
|--------|------------------|--------|
| KV cache hit rate | Fraction of requests reusing cached prefixes | > 50% for shared-prefix workloads |
| GPU block utilisation | Fraction of allocated blocks in use | > 80% |
| Cache eviction rate | How often blocks are swapped to CPU | Should be near 0 in steady state |
| TTFT (Time to First Token) | Latency from request to first output token | Depends on SLO; typically < 500ms |

---

## Exercises

1. Estimate the KV cache memory requirement for a Llama-3 70B model at 8K context length.
2. Explain what happens to memory usage as you increase `gpu_memory_utilization` from 0.7 to 0.95.
3. Describe a workload where prefix caching provides the most benefit.

---

## References

- [PagedAttention paper (Kwon et al., OSDI 2023)](https://arxiv.org/abs/2309.06180)
- [vLLM documentation — Memory Management](https://docs.vllm.ai/en/latest/design/arch_overview.html)
- [Continuous Batching blog (Anyscale)](https://www.anyscale.com/blog/continuous-batching-llm-inference)

## What Comes Next

- [04_quantization_deep_dive.ipynb](../04_quantization_deep_dive/04_quantization_deep_dive.ipynb) — Reduce model weight memory with AWQ and GPTQ
- [05_speculative_decoding.ipynb](../05_speculative_decoding/05_speculative_decoding.ipynb) — Speed up decode latency
""",
            },
        ],
    },
    {
        "folder": "04_quantization_deep_dive",
        "filename": "04_quantization_deep_dive.ipynb",
        "cells": [
            {
                "type": "markdown",
                "source": """# Quantization Deep Dive

> **Status:** Content notebook — AWQ and GPTQ exercises require a GPU with sufficient VRAM.

## Learning Objectives

By the end of this notebook, you will be able to:

- [ ] Explain the difference between post-training quantization (PTQ) and quantization-aware training (QAT)
- [ ] Describe the AWQ, GPTQ, EXL2, and GGUF quantization schemes and their trade-offs
- [ ] Load a quantized model using `bitsandbytes`, `AutoAWQ`, or `auto-gptq`
- [ ] Benchmark the quality/performance trade-off of different quantization levels
- [ ] Choose the right quantization scheme for a given hardware and latency target

---

## Prerequisites

- [01_START_HERE.ipynb](../01_START_HERE/01_START_HERE.ipynb)
- [03_kv_cache_paged_attention.ipynb](../03_kv_cache_paged_attention/03_kv_cache_paged_attention.ipynb)
- Basic PyTorch knowledge

---

## 1. Why Quantize?

LLMs store weights as 32-bit (FP32) or 16-bit (BF16/FP16) floats by default.

| Precision | Bytes/param | Llama-3 8B memory | Llama-3 70B memory |
|-----------|-------------|-------------------|--------------------|
| FP32      | 4           | ~32 GB            | ~280 GB            |
| BF16/FP16 | 2           | ~16 GB            | ~140 GB            |
| INT8      | 1           | ~8 GB             | ~70 GB             |
| INT4      | 0.5         | ~4 GB             | ~35 GB             |
| INT2      | 0.25        | ~2 GB             | ~17 GB             |

Quantization lets you run larger models on smaller hardware while trading off some quality.

---

## 2. Quantization Schemes

### bitsandbytes (BnB) — 8-bit and 4-bit
- Simple drop-in quantization via HuggingFace `load_in_8bit=True` / `load_in_4bit=True`
- NF4 (Normal Float 4) data type for 4-bit with double quantization
- Best for: fast experimentation, fine-tuning with LoRA

### GPTQ (Generative Pre-trained Transformer Quantization)
- PTQ using a calibration dataset to minimize layer-wise reconstruction error
- Produces INT4 weights with ~1% quality loss vs FP16
- Compatible with `auto-gptq` and ExLlamaV2
- Best for: inference speed on NVIDIA GPUs

### AWQ (Activation-Aware Weight Quantization)
- Protects the most salient weights (high activation magnitude) from quantization error
- Achieves better quality than GPTQ at the same bit-width
- Supported by `autoawq` and vLLM natively
- Best for: deployment in production vLLM stacks

### EXL2 (ExLlamaV2 format)
- Mixed-precision quantization per-layer using calibration data
- Can specify average bits (e.g., 4.0, 5.0) with per-layer variation
- Highest quality at 4-bit among local inference formats
- Best for: consumer GPU inference with quality priority

### GGUF (llama.cpp format)
- k-quant levels: Q4_K_M, Q5_K_M, Q8_0
- CPU-friendly; runs on Apple Silicon, CPUs, and low-VRAM GPUs
- Best for: Ollama, LM Studio, offline/local use

---

## 3. Loading Quantized Models

```python
# BitsAndBytes 4-bit (requires bitsandbytes, transformers)
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Meta-Llama-3-8B-Instruct",
    quantization_config=bnb_config,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B-Instruct")
```

```python
# AWQ via AutoAWQ (requires autoawq)
from awq import AutoAWQForCausalLM

model = AutoAWQForCausalLM.from_quantized(
    "casperhansen/llama-3-8b-instruct-awq",
    fuse_layers=True,
)
```

```python
# Serve AWQ model with vLLM
from vllm import LLM, SamplingParams

llm = LLM(
    model="casperhansen/llama-3-8b-instruct-awq",
    quantization="awq",
    dtype="float16",
)
outputs = llm.generate(["Explain quantization in one sentence."], SamplingParams(max_tokens=100))
print(outputs[0].outputs[0].text)
```

---

## 4. Quality Benchmarking

Use `lm-evaluation-harness` to measure perplexity and accuracy across tasks:

```bash
# Install
pip install lm-eval

# Run evaluation on a quantized model
lm_eval --model hf \
  --model_args pretrained=casperhansen/llama-3-8b-instruct-awq,dtype=float16 \
  --tasks hellaswag,arc_easy,mmlu \
  --device cuda:0 \
  --batch_size 8
```

Typical quality retention at INT4 (vs BF16): ~97–99% on standard benchmarks.

---

## 5. Choosing the Right Scheme

| Use case | Recommended |
|----------|------------|
| Fine-tuning on consumer GPU | BnB 4-bit (QLoRA) |
| Production vLLM serving | AWQ |
| Maximum quality at 4-bit | GPTQ or EXL2 |
| CPU / Apple Silicon / Ollama | GGUF Q4_K_M or Q5_K_M |
| Minimal code changes | BnB 8-bit |

---

## Exercises

1. Load `meta-llama/Meta-Llama-3-8B-Instruct` in both BF16 and 4-bit NF4 and compare GPU memory usage.
2. Benchmark inference throughput (tokens/sec) for BF16 vs AWQ INT4 on the same prompt batch.
3. Run `lm-evaluation-harness` on a GGUF model and compare MMLU scores vs the full-precision baseline.

---

## References

- [AWQ paper](https://arxiv.org/abs/2306.00978)
- [GPTQ paper](https://arxiv.org/abs/2210.17323)
- [bitsandbytes docs](https://huggingface.co/docs/bitsandbytes)
- [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)

## What Comes Next

- [05_speculative_decoding.ipynb](../05_speculative_decoding/05_speculative_decoding.ipynb) — Speed up decode latency without quality loss
- [06_serving_runtimes_comparison.ipynb](../06_serving_runtimes_comparison/06_serving_runtimes_comparison.ipynb) — Compare vLLM, TRT-LLM, and SGLang
""",
            },
        ],
    },
    {
        "folder": "05_speculative_decoding",
        "filename": "05_speculative_decoding.ipynb",
        "cells": [
            {
                "type": "markdown",
                "source": """# Speculative Decoding

> **Status:** Content notebook — hands-on benchmarks require a GPU with at least 24 GB VRAM.

## Learning Objectives

By the end of this notebook, you will be able to:

- [ ] Explain speculative decoding and why it reduces latency without changing output quality
- [ ] Describe the role of the draft model and the verification step
- [ ] Implement a basic speculative decoding loop from scratch
- [ ] Enable speculative decoding in vLLM and measure the speedup
- [ ] Understand when speculative decoding helps and when it doesn't
- [ ] Describe alternative approaches: Medusa heads, EAGLE, and prompt lookup decoding

---

## Prerequisites

- [03_kv_cache_paged_attention.ipynb](../03_kv_cache_paged_attention/03_kv_cache_paged_attention.ipynb)
- Familiarity with autoregressive decoding

---

## 1. The Latency Problem in Autoregressive Decoding

Standard decoding generates **one token per forward pass** of the full model.
The forward pass is often memory-bandwidth bound (especially with KV cache), not
compute bound — meaning the large model is underutilized on each single-token step.

Speculative decoding exploits this by using a **fast draft model** to propose
multiple tokens at once, then **verifying** them in a single parallel pass of the
large target model.

---

## 2. The Algorithm

```
Algorithm: Speculative Decoding (Chen et al., 2023)
--------------------------------------------------
Given: target model M_target, draft model M_draft, speculation length γ

For each decoding step:
  1. Draft: Run M_draft autoregressively for γ steps → tokens [t1, t2, ..., tγ]
  2. Verify: Run M_target on all γ draft tokens in PARALLEL (one forward pass)
  3. Accept/Reject: For each draft token ti:
       - Sample qi from M_target(ti | context)
       - Sample pi from M_draft(ti | context)
       - Accept with probability min(1, qi/pi)
       - On first rejection: resample from adjusted distribution and stop
  4. Result: Between 1 and γ+1 tokens accepted per target model forward pass
```

Key property: **The output distribution is identical to standard sampling from M_target.**
No quality loss — only latency improvement.

---

## 3. Speedup Analysis

Speedup depends on the **acceptance rate** — how often draft tokens match the target.

```python
# Theoretical speedup formula
# alpha = mean acceptance rate per draft token
# gamma = number of draft tokens

def expected_speedup(alpha: float, gamma: int) -> float:
    # Expected tokens per target model call
    expected_tokens = (1 - alpha**(gamma + 1)) / (1 - alpha)
    # Cost: 1 target call + gamma draft calls (draft is ~10-100x cheaper)
    # Speedup vs baseline (1 token per target call)
    return expected_tokens  # simplified (ignoring draft cost)

# Example: alpha=0.8, gamma=4
print(f"Speedup ≈ {expected_speedup(0.8, 4):.2f}x")  # ~3.36x
```

Typical real-world speedup: **1.5–3.5x** depending on task, draft model quality,
and hardware.

---

## 4. Draft Model Options

| Draft strategy | Description | Notes |
|----------------|-------------|-------|
| Small model (same family) | e.g., Llama-3.2-1B drafts for Llama-3-70B | Most common; best acceptance rates for matched families |
| N-gram / prompt lookup | Match draft tokens against prompt text | Works well for long-document summarization |
| Medusa heads | Add parallel prediction heads to the target | No separate model needed; faster at inference |
| EAGLE | Lightweight feature predictor on target hidden states | High acceptance rate with minimal overhead |

---

## 5. Speculative Decoding in vLLM

```python
# vLLM >= 0.4.0 supports speculative decoding
from vllm import LLM, SamplingParams

llm = LLM(
    model="meta-llama/Meta-Llama-3-70B-Instruct",
    speculative_model="meta-llama/Llama-3.2-1B-Instruct",
    num_speculative_tokens=5,
    dtype="bfloat16",
)

outputs = llm.generate(
    ["Explain the attention mechanism in transformers."],
    SamplingParams(temperature=0.0, max_tokens=256),
)
print(outputs[0].outputs[0].text)
```

```python
# Benchmark with and without speculative decoding
import time

# Without speculative decoding
llm_base = LLM(model="meta-llama/Meta-Llama-3-70B-Instruct")
start = time.time()
_ = llm_base.generate(prompts, SamplingParams(max_tokens=200))
baseline_time = time.time() - start

# With speculative decoding
llm_spec = LLM(
    model="meta-llama/Meta-Llama-3-70B-Instruct",
    speculative_model="meta-llama/Llama-3.2-1B-Instruct",
    num_speculative_tokens=5,
)
start = time.time()
_ = llm_spec.generate(prompts, SamplingParams(max_tokens=200))
spec_time = time.time() - start

print(f"Baseline: {baseline_time:.1f}s | Speculative: {spec_time:.1f}s | Speedup: {baseline_time/spec_time:.2f}x")
```

---

## 6. When Does It Help?

**Speculative decoding helps most when:**
- The task has predictable outputs (code generation, summarization, translation)
- The draft model is from the same family as the target
- Batch size is small (single-user or low-concurrency serving)

**Speculative decoding helps least when:**
- Creative or highly varied outputs (high temperature, story generation)
- Large batch sizes where the target model is already compute-saturated
- The draft model's token distribution diverges significantly from the target

---

## Exercises

1. Implement a simple speculative decoding loop with HuggingFace transformers using
   a Llama-3.2-1B draft and Llama-3-8B target.
2. Measure acceptance rate for different tasks: code generation vs creative writing.
3. Compare Medusa (if available) against the draft-model approach on the same benchmark.

---

## References

- [Speculative Decoding paper (Chen et al., 2023)](https://arxiv.org/abs/2302.01318)
- [Medusa paper](https://arxiv.org/abs/2401.10774)
- [EAGLE paper](https://arxiv.org/abs/2401.15077)
- [vLLM speculative decoding docs](https://docs.vllm.ai/en/latest/features/spec_decode.html)

## What Comes Next

- [06_serving_runtimes_comparison.ipynb](../06_serving_runtimes_comparison/06_serving_runtimes_comparison.ipynb) — vLLM vs TRT-LLM vs SGLang trade-offs
- [07_prefix_caching_chunked_prefill.ipynb](../07_prefix_caching_chunked_prefill/07_prefix_caching_chunked_prefill.ipynb) — Prefix caching and chunked prefill
""",
            },
        ],
    },
    {
        "folder": "06_serving_runtimes_comparison",
        "filename": "06_serving_runtimes_comparison.ipynb",
        "cells": [
            {
                "type": "markdown",
                "source": """# Serving Runtimes Comparison: vLLM · TensorRT-LLM · SGLang

> **Status:** Content notebook — benchmarks require NVIDIA GPU hardware.

## Learning Objectives

By the end of this notebook, you will be able to:

- [ ] Describe the design philosophy of vLLM, TensorRT-LLM, and SGLang
- [ ] Identify the key trade-offs across runtimes (TTFT, throughput, ease of deployment)
- [ ] Choose the right runtime for a given use case and hardware budget
- [ ] Run a benchmark comparing throughput and latency across runtimes
- [ ] Understand TGI (Text Generation Inference) as an alternative

---

## Prerequisites

- [02_serving_with_vllm.ipynb](../02_serving_with_vllm/02_serving_with_vllm.ipynb)
- [03_kv_cache_paged_attention.ipynb](../03_kv_cache_paged_attention/03_kv_cache_paged_attention.ipynb)

---

## 1. Runtime Overview

| Feature | vLLM | TensorRT-LLM | SGLang |
|---------|------|--------------|--------|
| Backend | PyTorch + CUDA kernels | TensorRT engine (NVIDIA-only) | PyTorch + RadixAttention |
| Quantization | AWQ, GPTQ, FP8 | AWQ, GPTQ, FP8, INT8 SmoothQuant | AWQ, GPTQ, FP8 |
| Speculative decoding | ✅ | ✅ | ✅ |
| Prefix caching | ✅ (automatic prefix caching) | ✅ | ✅ (RadixAttention) |
| Multi-modal | ✅ | ✅ | ✅ |
| OpenAI-compatible API | ✅ | ✅ | ✅ |
| Hardware | NVIDIA, AMD (ROCm) | NVIDIA only | NVIDIA, AMD |
| Build complexity | Low | High (engine build required) | Low |
| Best for | General purpose production | Maximum NVIDIA throughput | Structured generation, research |

---

## 2. vLLM

vLLM (Virtual Large Language Model) is the most widely deployed open-source
LLM serving framework. Key innovations:
- **PagedAttention** for efficient KV cache management
- **Continuous batching** — new requests join mid-generation
- **Chunked prefill** — large prefill split across multiple steps
- **Automatic prefix caching** — reuse KV blocks for shared prefixes

```bash
# Install
pip install vllm

# Start server
python -m vllm.entrypoints.openai.api_server \\
  --model meta-llama/Meta-Llama-3-8B-Instruct \\
  --port 8000 \\
  --dtype bfloat16 \\
  --enable-prefix-caching
```

```python
# Call vLLM OpenAI-compatible API
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")
response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[{"role": "user", "content": "What is PagedAttention?"}],
    max_tokens=200,
)
print(response.choices[0].message.content)
```

---

## 3. TensorRT-LLM

NVIDIA's TensorRT-LLM compiles models into optimized TensorRT engines.
Significantly higher throughput than vLLM on NVIDIA hardware, but:
- Requires a multi-hour engine build step
- NVIDIA hardware only
- More complex deployment pipeline

```python
# Conceptual TensorRT-LLM workflow
# Step 1: Convert model weights to TRT-LLM format
# tensorrt_llm convert_checkpoint --model_dir llama-3-8b --output_dir trtllm_ckpt

# Step 2: Build engine
# trtllm-build --checkpoint_dir trtllm_ckpt --output_dir trtllm_engine \
#   --max_batch_size 32 --max_input_len 4096 --max_output_len 1024

# Step 3: Serve
# python -m tensorrt_llm.serve --engine_dir trtllm_engine --port 8001
```

---

## 4. SGLang

SGLang (Structured Generation Language) focuses on structured generation,
multi-call programs, and research workloads.

Key innovation: **RadixAttention** — a radix-tree-based prefix cache that
automatically identifies and shares common prefixes across requests, achieving
higher cache hit rates than vLLM's block-based prefix cache.

Best for:
- Structured outputs (JSON schema, regex)
- Agent programs with many LLM calls sharing long system prompts
- Research and evaluation pipelines

```bash
# Install
pip install "sglang[all]"

# Start server
python -m sglang.launch_server \\
  --model-path meta-llama/Meta-Llama-3-8B-Instruct \\
  --port 30000 \\
  --enable-torch-compile
```

---

## 5. Benchmarking

Use the standard LLM performance benchmark (`vllm benchmark_throughput.py`)
or the `genai-perf` tool from NVIDIA:

```bash
# vLLM throughput benchmark
python benchmarks/benchmark_throughput.py \\
  --model meta-llama/Meta-Llama-3-8B-Instruct \\
  --dataset sharegpt \\
  --num-prompts 1000 \\
  --backend vllm

# Key metrics to collect:
# - Throughput: output tokens/second
# - TTFT: time to first token (p50, p95, p99)
# - ITL: inter-token latency
# - Request latency: total request duration
```

---

## 6. Decision Guide

```
Start with vLLM for:          Use TRT-LLM when:          Use SGLang when:
- Fast deployment             - NVIDIA hardware only     - Heavy structured output
- Multi-hardware support      - Max throughput needed    - Agent multi-call programs
- AWQ/GPTQ quantization      - Enterprise NVIDIA stack  - Research/eval pipelines
- Active community support    - Engine build is OK       - Prefix cache optimization
```

---

## Exercises

1. Start a vLLM server and benchmark throughput at batch sizes of 1, 4, 16, and 64.
2. Measure the cache hit rate with prefix caching enabled vs disabled on a workload
   with a long shared system prompt.
3. Compare TTFT (p95) between vLLM and SGLang on the same model and request distribution.

---

## References

- [vLLM documentation](https://docs.vllm.ai)
- [TensorRT-LLM documentation](https://nvidia.github.io/TensorRT-LLM/)
- [SGLang documentation](https://docs.sglang.ai)
- [LLM Inference Survey (2024)](https://arxiv.org/abs/2312.11514)

## What Comes Next

- [07_prefix_caching_chunked_prefill.ipynb](../07_prefix_caching_chunked_prefill/07_prefix_caching_chunked_prefill.ipynb) — Prefix caching and chunked prefill tuning
""",
            },
        ],
    },
    {
        "folder": "07_prefix_caching_chunked_prefill",
        "filename": "07_prefix_caching_chunked_prefill.ipynb",
        "cells": [
            {
                "type": "markdown",
                "source": """# Prefix Caching & Chunked Prefill

> **Status:** Content notebook — experiments require a GPU runtime with vLLM installed.

## Learning Objectives

By the end of this notebook, you will be able to:

- [ ] Explain how prefix caching reduces TTFT for requests sharing a common prompt prefix
- [ ] Describe how chunked prefill prevents long-prompt requests from starving ongoing decode
- [ ] Enable and tune both features in vLLM
- [ ] Measure the impact of prefix caching on cache hit rate and latency
- [ ] Understand continuous batching and why it matters for real-time serving

---

## Prerequisites

- [03_kv_cache_paged_attention.ipynb](../03_kv_cache_paged_attention/03_kv_cache_paged_attention.ipynb)
- [02_serving_with_vllm.ipynb](../02_serving_with_vllm/02_serving_with_vllm.ipynb)

---

## 1. Prefix Caching

When multiple requests share the same prefix — e.g., a long system prompt, RAG-retrieved
documents, or few-shot examples — recomputing the KV cache for that prefix on every
request is wasteful.

**Prefix caching** stores KV blocks for repeated prefixes and reuses them across requests.

```
Request 1: [SYSTEM PROMPT (2048 tokens)] [User: "What is X?"]
                ↓
           KV blocks for system prompt cached with hash key

Request 2: [SYSTEM PROMPT (2048 tokens)] [User: "What is Y?"]
                ↓
           System prompt KV blocks reused → TTFT drops from ~500ms to ~50ms
```

### vLLM Automatic Prefix Caching

```bash
# Enable automatic prefix caching
python -m vllm.entrypoints.openai.api_server \\
  --model meta-llama/Meta-Llama-3-8B-Instruct \\
  --enable-prefix-caching \\
  --max-model-len 8192
```

```python
# Test prefix cache hit rate
from openai import OpenAI
import time

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

SYSTEM_PROMPT = "You are a helpful AI assistant. " * 200  # Long shared prefix

def query(user_msg: str) -> float:
    start = time.time()
    resp = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ],
        max_tokens=50,
    )
    elapsed = time.time() - start
    return elapsed

# First request: no cache
t1 = query("What is 2+2?")
# Second request: prefix cached
t2 = query("What is 3+3?")
print(f"Cold start: {t1:.2f}s | Cached: {t2:.2f}s | Speedup: {t1/t2:.1f}x")
```

---

## 2. Continuous Batching

Traditional static batching waits for a full batch before starting inference.
This causes high latency for short requests that arrive when the batch is partially done.

**Continuous batching** allows new requests to join an in-progress batch at any
token boundary. vLLM uses continuous batching by default.

```
Static batching:        Continuous batching:
[R1][R2][R3][R4]       [R1          ]
Wait → Process → Done  [   R2       ]  ← R2 joins mid-stream
                       [      R3    ]  ← R3 joins mid-stream
                       [         R4]  ← R4 joins mid-stream
```

---

## 3. Chunked Prefill

**Problem:** A request with a 16K-token prompt monopolizes the GPU for its entire
prefill phase, causing all other requests (especially streaming ones) to wait.

**Chunked prefill** splits large prefill operations into smaller chunks (e.g., 2048
tokens per chunk), interleaving prefill chunks with ongoing decode steps.

```bash
# Enable chunked prefill with a 2048-token chunk size
python -m vllm.entrypoints.openai.api_server \\
  --model meta-llama/Meta-Llama-3-8B-Instruct \\
  --enable-prefix-caching \\
  --enable-chunked-prefill \\
  --max-num-batched-tokens 2048
```

Effect: Decode ITL (inter-token latency) variance decreases significantly for
mixed short/long request workloads.

---

## 4. Key Tuning Parameters

| Parameter | Effect | Typical value |
|-----------|--------|---------------|
| `--enable-prefix-caching` | Enable hash-based KV reuse | Always enable in prod |
| `--max-num-batched-tokens` | Chunk size for prefill | 512–4096 |
| `--gpu-memory-utilization` | KV cache budget | 0.85–0.95 |
| `--max-num-seqs` | Max concurrent sequences | 256–1024 |
| `--swap-space` | CPU KV swap buffer (GB) | 4–16 |

---

## 5. Measuring Cache Performance

vLLM exposes Prometheus metrics for monitoring cache performance:

```
# vLLM metrics endpoint
curl http://localhost:8000/metrics

# Key metrics to watch:
# vllm:cache_config_info          - Block size, total GPU/CPU blocks
# vllm:gpu_cache_usage_perc       - Fraction of GPU KV cache in use
# vllm:cpu_cache_usage_perc       - CPU swap usage (high = OOM risk)
# vllm:num_preemptions_total      - Requests evicted (should be near 0)
```

---

## Exercises

1. Run a benchmark with 100 requests sharing a 2048-token system prompt, with and
   without prefix caching. Report TTFT improvement.
2. Simulate a mixed workload: 50% short requests (256 tokens) and 50% long-context
   requests (8K tokens). Compare P95 TTFT with and without chunked prefill.
3. Graph GPU cache utilisation over time during a sustained load test.

---

## References

- [vLLM Prefix Caching docs](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching.html)
- [Chunked Prefill explanation (vLLM blog)](https://blog.vllm.ai/2024/09/05/perf-update.html)
- [Sarathi-Serve paper (chunked prefill)](https://arxiv.org/abs/2308.16369)

## What Comes Next

- Return to the hub: [30-inference-optimization.ipynb](../30-inference-optimization.ipynb)
- Related: [14-local-llms/README.md](../../14-local-llms/README.md)
- Related: [09-mlops/README.md](../../09-mlops/README.md)
""",
            },
        ],
    },
]


def make_notebook(cells):
    nb_cells = []
    for i, c in enumerate(cells):
        cell = {
            "id": f"cell-{i:04d}",
            "cell_type": c["type"],
            "metadata": {},
            "source": c["source"].splitlines(keepends=True),
        }
        if c["type"] == "markdown":
            pass
        else:
            cell["outputs"] = []
            cell["execution_count"] = None
        nb_cells.append(cell)

    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.11.0"},
        },
        "cells": nb_cells,
    }


def main():
    for nb_spec in NOTEBOOKS:
        folder_path = os.path.join(BASE, nb_spec["folder"])
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, nb_spec["filename"])
        if os.path.exists(file_path):
            print(f"SKIP  {nb_spec['filename']} (already exists)")
            continue
        nb = make_notebook(nb_spec["cells"])
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        print(f"WROTE {nb_spec['folder']}/{nb_spec['filename']}")

    print("\nDone.")


if __name__ == "__main__":
    main()
