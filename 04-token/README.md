# Phase 3: Tokenization

> **Goal**: Understand how text is converted into numbers that language models can process. This is the foundational step before embeddings and neural networks.

---

## Why Tokenization Matters

Every LLM interaction starts with tokenization. When you send a prompt to GPT-4 or Claude, it is first split into tokens — sub-word units that the model actually processes. Understanding tokenization helps you:

- **Write better prompts**: Avoid patterns that waste tokens and increase cost
- **Estimate costs accurately**: APIs charge per token, not per word
- **Debug model behavior**: Some languages tokenize less efficiently than English
- **Build production systems**: Fast tokenization is critical for throughput

**Key fact**: "tokenization" is 4 tokens in GPT-4. "Hello" is 1 token. An average English word is ~1.3 tokens.

---

## Notebooks — Work in This Order

| # | Notebook | What You Learn | Time |
|---|----------|----------------|------|
| 1 | [01_tokenizers_quickstart.ipynb](01_tokenizers_quickstart.ipynb) | HuggingFace tokenizers API, encode/decode, special tokens | 45 min |
| 2 | [tiktoken_example.ipynb](tiktoken_example.ipynb) | OpenAI's TikToken library, count tokens in prompts | 30 min |
| 3 | [sentencepiece_example.ipynb](sentencepiece_example.ipynb) | Google's SentencePiece (used in T5, LLaMA) | 30 min |
| 4 | [02_tokenizers_training.ipynb](02_tokenizers_training.ipynb) | Train a BPE tokenizer on your own data | 60 min |
| 5 | [03_advanced_training_methods.ipynb](03_advanced_training_methods.ipynb) | WordPiece, Unigram, and special handling | 45 min |
| 6 | [06_pipeline_components.ipynb](06_pipeline_components.ipynb) | Tokenization as part of the full NLP pipeline | 45 min |
| 7 | [token_exploration.ipynb](token_exploration.ipynb) | Hands-on exploration and visualization | 30 min |
| 8 | [token_exercises.ipynb](token_exercises.ipynb) | Practice problems with solutions | 45 min |

---

## Key Concepts

### The Three Main Tokenization Algorithms

**BPE (Byte Pair Encoding)** — Used by: GPT-2, GPT-3, GPT-4, RoBERTa
- Starts with individual bytes/characters
- Iteratively merges the most frequent pairs
- Result: common words are single tokens, rare words are split

**WordPiece** — Used by: BERT, DistilBERT
- Similar to BPE but uses likelihood instead of frequency
- Unknown words become `##suffix` parts

**SentencePiece / Unigram** — Used by: T5, LLaMA, Mistral, Gemma
- Language-agnostic, treats the text as raw bytes
- Works well for multilingual models

### Token Vocabulary Size

| Model | Vocab Size | Algorithm |
|-------|-----------|-----------|
| GPT-2 | 50,257 | BPE |
| GPT-4 / TikToken | 100,277 | BPE |
| BERT | 30,522 | WordPiece |
| LLaMA 3 | 128,256 | BPE (tiktoken-based) |
| T5 | 32,100 | SentencePiece |

Larger vocabulary = fewer tokens per sentence = faster inference, but larger embedding table.

---

## Reference Guides

- [intro.md](intro.md) — Conceptual introduction to tokenization
- [huggingface_tokenizers_guide.md](huggingface_tokenizers_guide.md) — Comprehensive HuggingFace guide
- [README_TOKENIZERS.md](README_TOKENIZERS.md) — HuggingFace tokenizers library deep dive
- [README_TIKTOKEN.md](README_TIKTOKEN.md) — OpenAI TikToken library guide
- [04_production_guide.md](04_production_guide.md) — Using tokenizers in production
- [05_tokenizer_comparison.md](05_tokenizer_comparison.md) — Comparing different tokenizers
- [06_integration_guide.md](06_integration_guide.md) — Integrating tokenizers into pipelines

---

## Practice Projects

1. **Token Counter Tool**: Build a CLI tool that counts tokens in any text file for a given model
2. **Tokenization Visualizer**: Color-code tokens in a Streamlit app
3. **Multilingual Efficiency Analyzer**: Compare token efficiency across English, Spanish, Chinese, Arabic

---

## What to Learn Next

After tokenization, move to **[05-embeddings/](../05-embeddings/)** to learn how tokens become meaningful vectors.

---

## External Resources

| Resource | Type | Link |
|----------|------|-------|
| Karpathy: Let's build the GPT Tokenizer | Video (90 min) | https://www.youtube.com/watch?v=zduSFxRajkE |
| HuggingFace Tokenizers Docs | Docs | https://huggingface.co/docs/tokenizers |
| TikToken GitHub | Repo | https://github.com/openai/tiktoken |
| SentencePiece GitHub | Repo | https://github.com/google/sentencepiece |
| Tiktokenizer (web tool) | Tool | https://tiktokenizer.vercel.app |
