# Tokenization Comparison Guide

## Comparing Different Tokenizers & Algorithms

A comprehensive comparison of tokenization approaches to help you choose the right one for your use case.

---

## Table of Contents

1. [Algorithm Comparison](#algorithm-comparison)
2. [Model-Specific Tokenizers](#model-specific-tokenizers)
3. [Performance Benchmarks](#performance-benchmarks)
4. [Language Support](#language-support)
5. [Use Case Recommendations](#use-case-recommendations)

---

## 1. Algorithm Comparison

### Overview Table

| Algorithm | Vocabulary Building | Best For | Used By | Pros | Cons |
|-----------|-------------------|----------|---------|------|------|
| **BPE** | Merge most frequent pairs | General text, code | GPT, RoBERTa, CodeGen | Fast, good compression | May split rare words oddly |
| **WordPiece** | Maximize likelihood | BERT-style tasks | BERT, DistilBERT, ELECTRA | Good for English | Slower training |
| **Unigram** | Probabilistic | Multilingual | T5, ALBERT, XLM-R | Best for many languages | More complex |
| **WordLevel** | Word-based | Simple use cases | FastText, Word2Vec | Simple, fast | Huge vocabulary |
| **CharLevel** | Character-based | Rare languages | Some specialized models | Handles anything | Very long sequences |

### Detailed Comparison

#### Byte-Pair Encoding (BPE)

```python
# How BPE works:
# 1. Start with characters: ['h', 'e', 'l', 'l', 'o']
# 2. Find most frequent pair: 'l', 'l' -> merge to 'll'
# 3. Result: ['h', 'e', 'll', 'o']
# 4. Repeat until vocabulary size reached

from tokenizers import Tokenizer, models, trainers

# Create BPE tokenizer
tokenizer = Tokenizer(models.BPE())
trainer = trainers.BpeTrainer(vocab_size=5000)

# Train
tokenizer.train(["data.txt"], trainer)
```

**Pros**:
- ✅ Fast training and inference
- ✅ Good compression ratio
- ✅ Works well for code
- ✅ Handles rare words via subwords

**Cons**:
- ❌ Can split common words oddly
- ❌ No probabilistic scoring
- ❌ Greedy algorithm

**Best for**: GPT-style models, code generation, English text

---

#### WordPiece

```python
# How WordPiece works:
# Similar to BPE but uses likelihood-based merging
# Prefers merges that maximize training data likelihood

from tokenizers import Tokenizer, models, trainers

tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))
trainer = trainers.WordPieceTrainer(
    vocab_size=30000,
    special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"]
)

tokenizer.train(["data.txt"], trainer)
```

**Pros**:
- ✅ Better linguistic splits than BPE
- ✅ Optimizes for likelihood
- ✅ Good for English

**Cons**:
- ❌ Slower training than BPE
- ❌ Requires pre-tokenization
- ❌ Less code-friendly

**Best for**: BERT-style models, classification, English NLP

---

#### Unigram

```python
# How Unigram works:
# Probabilistic approach - each subword has a probability
# Finds best segmentation based on probabilities

from tokenizers import Tokenizer, models, trainers

tokenizer = Tokenizer(models.Unigram())
trainer = trainers.UnigramTrainer(
    vocab_size=8000,
    special_tokens=["<unk>", "<s>", "</s>"]
)

tokenizer.train(["data.txt"], trainer)
```

**Pros**:
- ✅ Best for multilingual
- ✅ Probabilistic (not greedy)
- ✅ Multiple segmentation options
- ✅ Handles morphologically rich languages

**Cons**:
- ❌ More complex algorithm
- ❌ Slower inference
- ❌ Requires more training data

**Best for**: Multilingual models, T5-style models, diverse languages

---

#### Comparison Example

```python
"""
Compare how different algorithms tokenize the same text
"""
from tokenizers import Tokenizer, models, trainers, pre_tokenizers, normalizers

def create_tokenizer(algorithm="bpe"):
    """Create tokenizer with specified algorithm"""
    if algorithm == "bpe":
        tokenizer = Tokenizer(models.BPE())
        trainer = trainers.BpeTrainer(vocab_size=1000)
    elif algorithm == "wordpiece":
        tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))
        trainer = trainers.WordPieceTrainer(vocab_size=1000)
    elif algorithm == "unigram":
        tokenizer = Tokenizer(models.Unigram())
        trainer = trainers.UnigramTrainer(vocab_size=1000)
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")
    
    # Add normalizer and pre-tokenizer
    tokenizer.normalizer = normalizers.NFKC()
    tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
    
    return tokenizer, trainer

# Train all three
training_data = [
    "The quick brown fox jumps over the lazy dog.",
    "Machine learning is fascinating and powerful.",
    "Tokenization breaks text into smaller pieces.",
] * 100  # Repeat for better training

algorithms = ["bpe", "wordpiece", "unigram"]
tokenizers = {}

for algo in algorithms:
    tokenizer, trainer = create_tokenizer(algo)
    tokenizer.train_from_iterator(training_data, trainer)
    tokenizers[algo] = tokenizer

# Compare on test text
test_text = "Machine learning tokenization example"

print("\n" + "="*60)
print("ALGORITHM COMPARISON")
print("="*60)
print(f"\nTest text: '{test_text}'")
print(f"Length: {len(test_text)} characters\n")

for algo, tokenizer in tokenizers.items():
    encoding = tokenizer.encode(test_text)
    print(f"\n{algo.upper()}:")
    print(f"  Tokens: {encoding.tokens}")
    print(f"  Count: {len(encoding.ids)} tokens")
    print(f"  IDs: {encoding.ids}")
    
    # Calculate compression
    compression = len(test_text) / len(encoding.ids)
    print(f"  Compression: {compression:.2f} chars/token")
```

---

## 2. Model-Specific Tokenizers

### GPT Family (OpenAI)

```python
# GPT-2, GPT-3, GPT-4
# Algorithm: BPE with byte-level encoding

import tiktoken

# GPT-4 / GPT-3.5-turbo
encoding = tiktoken.get_encoding("cl100k_base")
tokens = encoding.encode("Hello, world!")

# Vocabulary: ~100,000 tokens
# Trained on: Diverse internet text + code
# Best for: General purpose, code, English
```

**Characteristics**:
- Vocab size: 50K (GPT-2) to 100K (GPT-4)
- Byte-level BPE (handles any UTF-8)
- No special pre-tokenization
- Optimized for English + code

### BERT Family (Google)

```python
# BERT, DistilBERT, RoBERTa
# Algorithm: WordPiece

from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize("Hello, world!")

# Vocabulary: ~30,000 tokens
# Special tokens: [CLS], [SEP], [MASK], [PAD], [UNK]
# Best for: Classification, NER, sentiment analysis
```

**Characteristics**:
- Vocab size: ~30K
- WordPiece algorithm
- Lowercase normalization (for uncased models)
- Subword tokens prefixed with ##

### T5 Family (Google)

```python
# T5, mT5
# Algorithm: SentencePiece Unigram

from transformers import T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained('t5-base')
tokens = tokenizer.tokenize("Hello, world!")

# Vocabulary: 32,000 tokens
# Multilingual support (mT5)
# Best for: Seq2seq, translation, summarization
```

**Characteristics**:
- Vocab size: 32K
- Unigram algorithm
- Language-agnostic
- No word boundary markers

### LLaMA Family (Meta)

```python
# LLaMA, LLaMA 2, Code LLaMA
# Algorithm: SentencePiece BPE

from transformers import LlamaTokenizer

tokenizer = LlamaTokenizer.from_pretrained('meta-llama/Llama-2-7b-hf')
tokens = tokenizer.tokenize("Hello, world!")

# Vocabulary: 32,000 tokens
# Trained on: Diverse multilingual data
# Best for: General LLM tasks
```

**Characteristics**:
- Vocab size: 32K
- SentencePiece BPE
- Multilingual
- Byte fallback for unknown chars

---

## 3. Performance Benchmarks

### Speed Comparison

```python
import time
from tokenizers import Tokenizer

# Test data
texts = ["Sample text " + str(i) for i in range(10000)]

# Benchmark function
def benchmark_tokenizer(tokenizer, texts, name):
    start = time.time()
    
    # Single encoding
    single_start = time.time()
    for text in texts[:1000]:
        tokenizer.encode(text)
    single_time = time.time() - single_start
    
    # Batch encoding
    batch_start = time.time()
    tokenizer.encode_batch(texts)
    batch_time = time.time() - batch_start
    
    print(f"\n{name}:")
    print(f"  Single: {single_time:.3f}s for 1K texts")
    print(f"  Batch:  {batch_time:.3f}s for 10K texts")
    print(f"  Speedup: {(single_time * 10) / batch_time:.1f}x")
    
    return {
        'single': single_time,
        'batch': batch_time,
        'speedup': (single_time * 10) / batch_time
    }

# Compare tokenizers
tokenizers_to_test = {
    'BPE': Tokenizer.from_pretrained('gpt2'),
    'WordPiece': Tokenizer.from_pretrained('bert-base-uncased'),
}

results = {}
for name, tokenizer in tokenizers_to_test.items():
    results[name] = benchmark_tokenizer(tokenizer, texts, name)

# Print comparison
print("\n" + "="*60)
print("PERFORMANCE COMPARISON")
print("="*60)
for name, result in results.items():
    print(f"{name}: {result['batch']:.3f}s (batch), {result['speedup']:.1f}x speedup")
```

**Typical Results**:
- BPE (HuggingFace Tokenizers): **Fastest** (Rust implementation)
- WordPiece (HuggingFace Tokenizers): Very fast
- Unigram (HuggingFace Tokenizers): Fast
- Python implementations: 10-50x slower

### Memory Usage

```python
import tracemalloc

def measure_memory(tokenizer, texts):
    """Measure peak memory usage"""
    tracemalloc.start()
    
    # Tokenize
    tokenizer.encode_batch(texts)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return peak / 1024 / 1024  # Convert to MB

texts = ["Sample text " + str(i) for i in range(100000)]

for name, tokenizer in tokenizers_to_test.items():
    memory_mb = measure_memory(tokenizer, texts[:10000])
    print(f"{name}: {memory_mb:.2f} MB peak memory")
```

---

## 4. Language Support

### English-Optimized

**Best for English**: GPT, BERT (English variants)

```python
# English text
text = "The quick brown fox jumps over the lazy dog."

# GPT tokenizer (optimized for English)
gpt_tokens = tiktoken.get_encoding("cl100k_base").encode(text)
print(f"GPT: {len(gpt_tokens)} tokens")  # ~10 tokens

# Result: Very efficient for English
```

### Multilingual

**Best for multiple languages**: mBERT, XLM-R, mT5, LLaMA

```python
# Multilingual text
texts = {
    'English': "Hello, how are you?",
    'Chinese': "你好吗？",
    'Arabic': "كيف حالك؟",
    'Hindi': "आप कैसे हैं?",
    'Russian': "Как дела?"
}

# Compare tokenizers
from transformers import AutoTokenizer

# English-optimized
gpt_tokenizer = AutoTokenizer.from_pretrained('gpt2')

# Multilingual
xlmr_tokenizer = AutoTokenizer.from_pretrained('xlm-roberta-base')

print("\n" + "="*60)
print("LANGUAGE COMPARISON")
print("="*60)

for lang, text in texts.items():
    gpt_tokens = gpt_tokenizer.tokenize(text)
    xlmr_tokens = xlmr_tokenizer.tokenize(text)
    
    print(f"\n{lang}: '{text}'")
    print(f"  GPT (English-opt): {len(gpt_tokens)} tokens")
    print(f"  XLM-R (Multilingual): {len(xlmr_tokens)} tokens")
    
    # XLM-R is more efficient for non-English
```

**Efficiency by Language** (tokens per character):

| Language | GPT-2 | mBERT | XLM-R | Best |
|----------|-------|-------|-------|------|
| English | 0.25 | 0.30 | 0.28 | GPT-2 |
| Chinese | 1.50 | 0.80 | 0.70 | XLM-R |
| Arabic | 1.20 | 0.75 | 0.65 | XLM-R |
| Russian | 1.00 | 0.70 | 0.60 | XLM-R |
| Hindi | 1.30 | 0.85 | 0.75 | XLM-R |

**Rule of Thumb**: 
- English-only app → Use GPT/BERT tokenizers
- Multilingual app → Use XLM-R/mT5 tokenizers

---

## 5. Use Case Recommendations

### Text Classification

**Recommended**: BERT WordPiece

```python
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Why BERT?
# - Optimized for classification tasks
# - [CLS] token for sequence representation
# - Fast inference
# - Good English performance
```

### Code Generation

**Recommended**: GPT BPE (cl100k_base or Codex)

```python
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

# Why GPT?
# - Trained on code
# - Handles syntax well
# - Good at indentation
# - Mixed code + natural language
```

### Machine Translation

**Recommended**: mT5 Unigram or XLM-R

```python
from transformers import T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained('t5-base')

# Why T5/mT5?
# - Seq2seq architecture
# - Multilingual support
# - Good for translation tasks
```

### Question Answering

**Recommended**: BERT or RoBERTa

```python
from transformers import RobertaTokenizer

tokenizer = RobertaTokenizer.from_pretrained('roberta-base')

# Why RoBERTa?
# - Optimized for span extraction
# - Character-level alignment
# - Good context understanding
```

### Chatbot / Dialogue

**Recommended**: GPT or LLaMA

```python
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

# Why GPT?
# - Natural conversation flow
# - Good general knowledge
# - Handles context well
```

### Multilingual Search

**Recommended**: XLM-R or mBERT

```python
from transformers import XLMRobertaTokenizer

tokenizer = XLMRobertaTokenizer.from_pretrained('xlm-roberta-base')

# Why XLM-R?
# - 100 languages supported
# - Efficient tokenization
# - Cross-lingual transfer
```

---

## Quick Decision Tree

```
Choose Tokenizer:

Are you using a specific model (GPT-4, BERT, etc.)?
├─ YES → Use that model's tokenizer
└─ NO → Continue...

What's your primary task?
├─ Text Classification/NER → BERT WordPiece
├─ Code Generation → GPT BPE
├─ Translation → mT5 Unigram
├─ General LLM → GPT BPE
└─ Multilingual → XLM-R

What's your language?
├─ English only → GPT/BERT
├─ 2-5 languages → mBERT/XLM-R  
└─ Many languages → XLM-R/mT5

What's your priority?
├─ Speed → HuggingFace Tokenizers (Rust)
├─ Accuracy → Use pretrained tokenizers
└─ Custom domain → Train your own
```

---

## Summary Table

| Use Case | Best Tokenizer | Vocab Size | Speed | Language Support |
|----------|---------------|------------|-------|------------------|
| **English Classification** | BERT WordPiece | 30K | Fast | English |
| **Code Generation** | GPT BPE | 100K | Fast | Code + English |
| **Translation** | mT5 Unigram | 32K | Medium | 100+ languages |
| **Chatbot** | GPT BPE | 100K | Fast | Primarily English |
| **Multilingual Search** | XLM-R | 250K | Medium | 100 languages |
| **Custom Domain** | Train your own | 8-32K | Fast | Your data |

---

## Testing Your Tokenizer Choice

```python
def evaluate_tokenizer_choice(tokenizer, test_texts, language="English"):
    """
    Evaluate if tokenizer is appropriate for your use case
    """
    total_tokens = 0
    total_chars = 0
    unknown_count = 0
    
    for text in test_texts:
        encoding = tokenizer.encode(text)
        total_tokens += len(encoding.ids)
        total_chars += len(text)
        
        # Check for unknown tokens
        if hasattr(tokenizer, 'unk_token'):
            unknown_count += encoding.tokens.count(tokenizer.unk_token)
    
    # Calculate metrics
    avg_compression = total_chars / total_tokens
    unknown_rate = unknown_count / total_tokens if total_tokens > 0 else 0
    
    print(f"\n{language} Evaluation:")
    print(f"  Compression: {avg_compression:.2f} chars/token")
    print(f"  Unknown rate: {unknown_rate:.1%}")
    
    # Recommendations
    if avg_compression < 2:
        print("  ⚠️  Low compression - consider multilingual tokenizer")
    elif avg_compression > 5:
        print("  ⚠️  Very high compression - may lose information")
    else:
        print("  ✅ Good compression ratio")
    
    if unknown_rate > 0.05:
        print("  ⚠️  High unknown rate - consider retraining")
    else:
        print("  ✅ Low unknown rate")

# Test on your data
my_texts = ["Your sample texts here..."]
evaluate_tokenizer_choice(tokenizer, my_texts)
```

---

**Choose wisely based on your specific needs!** 🎯
