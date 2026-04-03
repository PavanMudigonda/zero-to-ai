# 29. Inference Optimization & Model Serving

## 🎯 Learning Objectives
- [ ] Understand the memory and compute bottlenecks of LLM inference (Memory Wall vs Compute Wall).
- [ ] Master PagedAttention and KV Cache management.
- [ ] Apply post-training quantization techniques (AWQ, GPTQ, EXL2).
- [ ] Deploy models using high-throughput serving engines like **vLLM** and **TensorRT-LLM**.
- [ ] Implement advanced decoding strategies like Speculative Decoding to reduce latency.

## ⏱️ Time Estimate
- **Expected time:** 4-6 hours

## 📚 Prerequisites
- Completion of [14-local-llms](../14-local-llms/)
- Completion of [04-token](../04-token/)
- Basic understanding of PyTorch devices and CUDA memory.

## 🛠️ Deliverables
- [ ] `01_kv_cache_paged_attention.ipynb` - Visualizing and managing the KV cache.
- [ ] `02_quantization_deep_dive.ipynb` - Quantizing a Llama-3 model from FP16 to INT4 using AWQ.
- [ ] `03_serving_with_vllm.py` - Setting up a production-ready vLLM FastAPI server.
- [ ] `04_speculative_decoding.ipynb` - Speeding up inference using a small draft model.

## 📖 Resources
- [vLLM Documentation](https://vllm.readthedocs.io/)
- [HuggingFace Quantization Guide](https://huggingface.co/docs/transformers/main_classes/quantization)
- [PagedAttention Paper](https://arxiv.org/abs/2309.06180)
