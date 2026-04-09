# Phase 30: Inference Optimization & Model Serving

## 🎯 Learning Objectives
- [ ] Understand the memory and compute bottlenecks of LLM inference (Memory Wall vs Compute Wall).
- [ ] Master PagedAttention and KV Cache management.
- [ ] Apply post-training quantization techniques (AWQ, GPTQ, EXL2).
- [ ] Deploy models using high-throughput serving engines like **vLLM** and **TensorRT-LLM**.
- [ ] Implement advanced decoding strategies like Speculative Decoding to reduce latency.
- [ ] Understand prefix caching, chunked prefill, and continuous batching.
- [ ] Compare local serving engines such as **vLLM**, **TensorRT-LLM**, and **SGLang**.
- [ ] Measure throughput, TTFT, decode speed, and cost-per-token trade-offs.

## ⏱️ Time Estimate
- **Expected time:** 6-8 hours

## 📚 Prerequisites
- Completion of [14-local-llms](../14-local-llms/)
- Completion of [04-token](../04-token/)
- Basic understanding of PyTorch devices and CUDA memory.

## 🛠️ Current and Planned Materials
- [ ] `01_kv_cache_paged_attention.ipynb` - Visualizing and managing the KV cache.
- [ ] `02_quantization_deep_dive.ipynb` - Quantizing a Llama-3 model from FP16 to INT4 using AWQ.
- [x] `03_serving_with_vllm.ipynb` - Quickstart notebook for vLLM-based serving and batching.
- [ ] `04_speculative_decoding.ipynb` - Speeding up inference using a small draft model.
- [ ] Add a TensorRT-LLM / SGLang comparison walkthrough.
- [ ] Add a prefix caching and chunked prefill tuning walkthrough.

## 2026 Topics This Phase Should Cover

- PagedAttention and KV cache layout
- Prefix caching and reuse across repeated prompts
- Chunked prefill, continuous batching, and scheduler behavior
- Quantization stacks: AWQ, GPTQ, EXL2, GGUF, FP8 where available
- Serving runtimes: vLLM, TensorRT-LLM, SGLang, TGI
- Speculative decoding and draft-model assisted generation
- Throughput metrics: TTFT, tokens/sec, concurrency saturation, memory footprint

## 📖 Resources
- [vLLM Documentation](https://vllm.readthedocs.io/)
- [HuggingFace Quantization Guide](https://huggingface.co/docs/transformers/main_classes/quantization)
- [PagedAttention Paper](https://arxiv.org/abs/2309.06180)
- [TensorRT-LLM Documentation](https://nvidia.github.io/TensorRT-LLM/)
- [SGLang Documentation](https://docs.sglang.ai/)
