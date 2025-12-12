# Phase 13: Local LLMs & Optimization

## 🎯 Overview

Run powerful LLMs on your own hardware! Learn to deploy, optimize, and serve local models for privacy, cost savings, and full control.

**Prerequisites:**
- ✅ LLMs & Prompt Engineering (Phase 10)
- ✅ Optional: Fine-tuning (Phase 11)
- ✅ Python programming

**Time:** 2-3 weeks | 40-60 hours  
**Outcome:** Deploy production-ready local LLM inference systems

---

## 📚 What You'll Learn

### Local LLM Fundamentals

- [ ] Why run models locally (privacy, cost, control)
- [ ] Hardware requirements and optimization
- [ ] Model formats (GGUF, GPTQ, AWQ, EXL2)
- [ ] Quantization techniques (2-bit to 16-bit)
- [ ] Memory vs. speed tradeoffs

### Deployment Tools

- [ ] Ollama (easiest, Mac/Linux/Windows)
- [ ] llama.cpp (C++ inference)
- [ ] vLLM (high-throughput serving)
- [ ] Text Generation WebUI (GGUF/GPTQ)
- [ ] LocalAI (OpenAI-compatible API)
- [ ] LM Studio (GUI application)

### Performance Optimization

- [ ] Flash Attention
- [ ] KV cache optimization
- [ ] Batching strategies
- [ ] Quantization comparison (4-bit, 8-bit)
- [ ] CPU vs GPU inference
- [ ] Model pruning and distillation

### Production Serving

- [ ] OpenAI-compatible API servers
- [ ] Load balancing and scaling
- [ ] Caching strategies
- [ ] Monitoring and logging
- [ ] Rate limiting
- [ ] Cost tracking

---

## 🗂️ Module Structure

```
13-local-llms/
├── 00_START_HERE.ipynb                # Overview & setup
├── 01_ollama_basics.ipynb             # Easiest way to start
├── 02_llamacpp.ipynb                  # llama.cpp deep dive
├── 03_model_formats.ipynb             # GGUF, GPTQ, AWQ comparison
├── 04_quantization.ipynb              # Quantization techniques
├── 05_vllm_serving.ipynb              # High-performance serving
├── 06_optimization.ipynb              # Speed & memory tricks
├── 07_api_server.ipynb                # OpenAI-compatible API
├── 08_production.ipynb                # Production deployment
├── projects/
│   ├── local_chatbot.py               # Full chatbot with memory
│   ├── api_server.py                  # Production API
│   ├── code_assistant.py              # Local code helper
│   └── rag_local.py                   # RAG with local LLM
├── benchmarks/
│   ├── speed_tests.py
│   ├── memory_tests.py
│   └── quality_comparison.py
└── configs/
    ├── ollama_models.txt
    ├── recommended_models.md
    └── hardware_guide.md
```

---

## 🚀 Quick Start

### Option 1: Ollama (Recommended for Beginners)

```bash
# Install Ollama (Mac/Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Pull a model (auto-downloads and runs)
ollama pull llama3.2

# Run interactive chat
ollama run llama3.2

# Use in Python
from ollama import Client
client = Client()

response = client.chat(model='llama3.2', messages=[
    {'role': 'user', 'content': 'Explain quantum computing'}
])
print(response['message']['content'])
```

### Option 2: llama.cpp

```bash
# Clone and build
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make

# Download a GGUF model
# From HuggingFace: TheBloke/Llama-2-7B-GGUF

# Run inference
./main -m models/llama-2-7b.Q4_K_M.gguf -p "Explain AI in simple terms" -n 128
```

### Option 3: vLLM (Production Serving)

```python
from vllm import LLM, SamplingParams

# Load model
llm = LLM(model="meta-llama/Llama-2-7b-hf")

# Configure sampling
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.9,
    max_tokens=256
)

# Generate (batched for efficiency)
prompts = [
    "Explain machine learning",
    "What is deep learning?"
]

outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    print(output.outputs[0].text)
```

---

## 📋 Learning Path

### Week 1: Getting Started

- [ ] Complete `00_START_HERE.ipynb`
- [ ] Set up Ollama in `01_ollama_basics.ipynb`
- [ ] Try different models
- [ ] **Project:** Build local chatbot

### Week 2: Optimization

- [ ] Learn quantization in `04_quantization.ipynb`
- [ ] Compare formats in `03_model_formats.ipynb`
- [ ] Optimize performance in `06_optimization.ipynb`
- [ ] **Project:** Benchmark different configs

### Week 3: Production

- [ ] vLLM serving in `05_vllm_serving.ipynb`
- [ ] Build API in `07_api_server.ipynb`
- [ ] Production patterns in `08_production.ipynb`
- [ ] **Capstone:** Production-ready local LLM API

---

## 🛠️ Technologies & Tools

### Inference Engines

**Ollama** ⭐ Best for beginners
- One-command setup
- Automatic model management
- Built-in API server
- Mac/Linux/Windows

**llama.cpp** ⭐ Most flexible
- Pure C++ (very fast)
- CPU and GPU support
- GGUF format
- Low memory usage

**vLLM** ⭐ Best for production
- Highest throughput
- PagedAttention
- OpenAI-compatible API
- Continuous batching

**Text Generation WebUI**
- User-friendly GUI
- Multiple model formats
- Extensions ecosystem
- Good for experimentation

**LM Studio**
- Desktop GUI app
- Easy model discovery
- Cross-platform
- No coding needed

### Model Formats Explained

```
GGUF (GPT-Generated Unified Format)
├─ Q2_K: 2.5-3 bits (smallest, lowest quality)
├─ Q4_K_M: 4.5 bits (recommended balance)
├─ Q5_K_M: 5.5 bits (high quality)
├─ Q6_K: 6.5 bits (very high quality)
└─ Q8_0: 8 bits (near original quality)

GPTQ (GPU-optimized)
├─ 4-bit, 3-bit
└─ Faster on GPU

AWQ (Activation-aware Weight Quantization)
├─ Better quality at same size
└─ Good for production

EXL2 (ExLlama v2)
├─ Highly optimized
└─ Variable bit widths
```

---

## 📊 Hardware Requirements

### Minimum (CPU-only)

```
7B model (Q4): 6GB RAM, modern CPU
13B model (Q4): 10GB RAM
30B model (Q4): 20GB RAM

Expect: 1-5 tokens/sec on CPU
```

### Recommended (GPU)

```
GPU with 8GB VRAM:
├─ 7B models (Q4-Q6)
├─ 13B models (Q4)
└─ Speed: 20-50 tokens/sec

GPU with 16GB VRAM:
├─ 13B models (Q5-Q8)
├─ 30B models (Q4)
└─ Speed: 30-80 tokens/sec

GPU with 24GB+ VRAM:
├─ 30B models (Q5-Q8)
├─ 70B models (Q4)
└─ Speed: 40-100 tokens/sec
```

### Apple Silicon (M1/M2/M3)

```
Unified memory = GPU + CPU RAM

16GB: 7B-13B models
32GB: 30B models, multiple 7B
64GB: 70B models
96GB+: Multiple large models

Metal acceleration: ~20-60 tokens/sec
```

---

## 📈 Model Recommendations

### Best Local Models (December 2024)

**For Coding:**
- CodeLlama 7B/13B/34B
- DeepSeek Coder 6.7B/33B
- Phind CodeLlama

**For General Chat:**
- Llama 3.2 (8B, 70B)
- Mistral 7B v0.3
- Mixtral 8x7B (MoE)
- Qwen 2.5 (7B, 14B, 72B)

**For Specific Tasks:**
- Nous Hermes (uncensored)
- OpenHermes (fine-tuned)
- Vicuna (conversation)
- Orca 2 (reasoning)

**Tiny Models (< 3B):**
- Phi-3 Mini (3.8B)
- StableLM 2 1.6B
- Gemma 2B

---

## 💡 Best Practices

### Model Selection

**DO ✅**
- Start with 7B models (faster to test)
- Use Q4_K_M quantization (good balance)
- Match model to task (coding, chat, etc.)
- Test locally before deploying

**DON'T ❌**
- Use Q2 (too lossy)
- Load models too big for your VRAM
- Ignore context length limits
- Skip benchmarking

### Performance Optimization

```python
# Good vLLM config
vllm_config = {
    "max_model_len": 4096,      # Match your needs
    "gpu_memory_utilization": 0.9,  # Use most of GPU
    "tensor_parallel_size": 1,   # Multi-GPU if available
    "trust_remote_code": False,  # Security
    "dtype": "half",             # FP16 for speed
}

# Good sampling params
sampling_params = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_tokens": 512,
    "repetition_penalty": 1.1
}
```

### Production Deployment

**DO ✅**
- Use OpenAI-compatible API
- Implement request queuing
- Add response caching
- Monitor GPU/CPU usage
- Set rate limits
- Log all requests

**DON'T ❌**
- Expose without authentication
- Skip error handling
- Ignore memory leaks
- Forget to version models

---

## 🎯 Projects

### 1. Local AI Assistant

Full-featured chatbot with memory and personality.

**Skills:** Ollama, conversation management, persistence

### 2. Code Helper API

API server for code completion and explanation.

**Skills:** vLLM, API design, specialized prompts

### 3. Private RAG System

RAG system with local embeddings and LLM.

**Skills:** Local embeddings, vector DB, privacy

### 4. Multi-Model Router

Route requests to different models based on task.

**Skills:** Model serving, load balancing, optimization

---

## 🔗 Resources

### Documentation

- [Ollama Docs](https://github.com/ollama/ollama)
- [llama.cpp Guide](https://github.com/ggerganov/llama.cpp)
- [vLLM Documentation](https://docs.vllm.ai/)
- [LocalAI](https://localai.io/)

### Model Sources

- [Hugging Face](https://huggingface.co/models?pipeline_tag=text-generation)
- [TheBloke's GGUF Models](https://huggingface.co/TheBloke)
- [Ollama Library](https://ollama.com/library)

### Communities

- r/LocalLLaMA
- Ollama Discord
- LLaMA.cpp discussions

### Hardware Guides

- [GPU Buying Guide](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
- [Apple Silicon Performance](https://github.com/ggerganov/llama.cpp#apple-silicon)

---

## ✅ Completion Checklist

Before moving forward, you should be able to:

- [ ] Install and run Ollama
- [ ] Use llama.cpp for inference
- [ ] Understand quantization formats
- [ ] Choose appropriate models for hardware
- [ ] Optimize inference speed and memory
- [ ] Set up vLLM production server
- [ ] Create OpenAI-compatible API
- [ ] Monitor and log inference
- [ ] Deploy local RAG systems
- [ ] Compare cloud vs local tradeoffs

---

## 🎓 What's Next?

**Phase 8: MLOps** →
- Deploy and monitor local models
- CI/CD for model updates
- Production best practices

**Phase 9: AI Agents** →
- Build agents with local LLMs
- Privacy-focused autonomous systems
- Tool use with local models

**Real-World Applications** →
- On-premise enterprise AI
- Privacy-sensitive applications
- Offline AI systems
- Cost-optimized production

---

**Ready to run LLMs locally?** → Start with `00_START_HERE.ipynb`

**Questions?** → Check configs/ for hardware recommendations

**🚀 Remember: Privacy, control, and $0 API costs!**
