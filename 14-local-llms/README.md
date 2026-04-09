# Phase 14: Local LLMs

This module should help you answer a practical question: when does running models locally make sense, and what trade-offs do you accept in exchange for privacy, cost control, and deployment flexibility?

## Actual Module Contents

1. [00_START_HERE.ipynb](00_START_HERE.ipynb)
2. [01_ollama_quickstart.ipynb](01_ollama_quickstart.ipynb)
3. [02_open_source_models_overview.ipynb](02_open_source_models_overview.ipynb)
4. [03_local_rag_with_ollama.ipynb](03_local_rag_with_ollama.ipynb)
5. [04_llm_server_and_api.ipynb](04_llm_server_and_api.ipynb)
6. [05_speculative_decoding.ipynb](05_speculative_decoding.ipynb)

## Recommended Order

- Start with Ollama and the model overview
- Then build a local RAG workflow
- Then study serving and API patterns
- Finish with speculative decoding and performance considerations

## What To Learn Here

- The difference between hosted APIs and local inference
- How quantization and model size affect usability
- What Ollama is good at and where it is limiting
- How to expose a local model behind an API
- Why latency and throughput tuning matter once a prototype works

## Current Local LLM Stack To Know In 2026

- Ollama for the simplest developer experience
- llama.cpp and GGUF for broad hardware compatibility
- MLX for Apple Silicon-native training and inference
- vLLM and SGLang for higher-throughput serving on stronger local GPUs
- OpenAI-compatible local gateways for app portability across hosted and self-hosted backends

## Study Advice

- Keep the first pass practical: install one tool, run one model, ship one API.
- Do not optimize before measuring.
- Compare local quality against your hosted baseline before committing to an on-device stack.

## Good Follow-On Projects

- A private document assistant
- A local coding helper with retrieval
- A lightweight OpenAI-compatible local serving layer
- A Mac-first MLX workflow for Apple Silicon laptops
- A benchmark that compares Ollama, llama.cpp, and vLLM on the same model
