# HuggingFace Tokenizers Library - Complete Learning Guide

> **Fast, Blazing-Fast Tokenization Library** 🚀
>
> A comprehensive guide to the 🤗 Tokenizers library - the implementation of today's most used tokenizers that is both easy to use and extremely fast.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [Tokenization Pipeline](#tokenization-pipeline)
5. [Components Deep Dive](#components-deep-dive)
6. [Training Custom Tokenizers](#training-custom-tokenizers)
7. [Working with Pretrained Tokenizers](#working-with-pretrained-tokenizers)
8. [Advanced Features](#advanced-features)
9. [Complete Examples](#complete-examples)
10. [Best Practices](#best-practices)

---

## Introduction

The 🤗 Tokenizers library provides:

- **Speed**: Extremely fast tokenization (can train on 516MB in seconds)
- **Versatility**: Works with all modern tokenization algorithms
- **Full Alignment**: Track mappings between tokens and original text
- **Easy Training**: Simple API to train custom tokenizers
- **Production Ready**: Battle-tested in thousands of applications

### Why Use This Library?

- **Faster than alternatives**: Optimized Rust implementation with Python bindings
- **Alignment tracking**: Know exactly where each token came from in original text
- **Flexible**: Support for BPE, WordPiece, Unigram, and WordLevel algorithms
- **Battle-tested**: Used in transformers, fastai, and many production systems

---

## Installation

```bash
# Basic installation
pip install tokenizers

# Verify installation
python -c "import tokenizers; print(tokenizers.__version__)"
```

---

## Quick Start

### 1. Build a Tokenizer from Scratch (5 minutes)

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

# Step 1: Initialize with a model
tokenizer = Tokenizer(BPE(unk_token="[UNK]"))

# Step 2: Configure pre-tokenizer
tokenizer.pre_tokenizer = Whitespace()

# Step 3: Create trainer with special tokens
trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])

# Step 4: Train on files
files = ["data/train.txt", "data/valid.txt"]
tokenizer.train(files, trainer)

# Step 5: Save for later use
tokenizer.save("my-tokenizer.json")

# Step 6: Use it!
output = tokenizer.encode("Hello, world!")
print(output.tokens)  # ['Hello', ',', 'world', '!']
print(output.ids)     # [245, 16, 689, 23]
```

### 2. Load a Pretrained Tokenizer (1 minute)

```python
from tokenizers import Tokenizer

# From Hugging Face Hub
tokenizer = Tokenizer.from_pretrained("bert-base-uncased")

# From local file
tokenizer = Tokenizer.from_file("my-tokenizer.json")

# Use it
output = tokenizer.encode("Quick tokenization test")
```

---

## Tokenization Pipeline

Every tokenization goes through these steps:

```
Raw Text → Normalization → Pre-Tokenization → Model → Post-Processing → Encoding
```

### Pipeline Visualization

```python
from tokenizers import Tokenizer

# Example text
text = "Hello, y'all! How are you 😁 ?"

# Step-by-step pipeline:
# 1. Normalization:     "Hello, y'all! How are you 😁 ?" 
#                       → (lowercase, remove accents, etc.)
#
# 2. Pre-Tokenization:  → ["Hello", ",", "y", "'", "all", "!", "How", "are", "you", "😁", "?"]
#                       (split on whitespace and punctuation)
#
# 3. Model:             → ["Hello", ",", "y", "'", "all", "!", "How", "are", "you", "[UNK]", "?"]
#                       (map to vocabulary)
#
# 4. Post-Processing:   → ["[CLS]", "Hello", ",", "y", "'", "all", "!", "How", "are", "you", "[UNK]", "?", "[SEP]"]
#                       (add special tokens)

output = tokenizer.encode(text)
```

---

## Components Deep Dive

### 1. Normalizers

**Purpose**: Clean and standardize raw text

#### Available Normalizers

| Normalizer | Description | Example |
|------------|-------------|---------|
| **NFD/NFC/NFKD/NFKC** | Unicode normalization | - |
| **Lowercase** | Convert to lowercase | `HELLO` → `hello` |
| **Strip** | Remove whitespace | `" hi "` → `"hi"` |
| **StripAccents** | Remove accents | `é` → `e` |
| **BertNormalizer** | BERT-style normalization | All-in-one BERT preprocessing |
| **Replace** | Custom replacements | `banana` → `benene` (a→e) |

#### Example Usage

```python
from tokenizers import normalizers
from tokenizers.normalizers import NFD, StripAccents, Lowercase

# Single normalizer
tokenizer.normalizer = Lowercase()

# Combine multiple normalizers
tokenizer.normalizer = normalizers.Sequence([
    NFD(),              # Unicode normalization
    Lowercase(),        # Lowercase everything
    StripAccents()      # Remove accents
])

# Test it
result = tokenizer.normalizer.normalize_str("Héllò HÔW are Ü?")
print(result)  # "hello how are u?"
```

### 2. Pre-Tokenizers

**Purpose**: Split text into words/subwords before model processing

#### Available Pre-Tokenizers

| Pre-Tokenizer | Description | Input | Output |
|---------------|-------------|-------|--------|
| **Whitespace** | Split on word boundaries | `"Hello there!"` | `["Hello", "there", "!"]` |
| **WhitespaceSplit** | Split only on whitespace | `"Hello there!"` | `["Hello", "there!"]` |
| **ByteLevel** | GPT-2 style (byte-level) | `"Hello my friend"` | `["Hello", "Ġmy", "Ġfriend"]` |
| **Punctuation** | Isolate punctuation | `"Hello?"` | `["Hello", "?"]` |
| **Metaspace** | SentencePiece style | `"Hello there"` | `["Hello", "▁there"]` |
| **Digits** | Separate numbers | `"Hello123there"` | `["Hello", "123", "there"]` |
| **CharDelimiterSplit** | Custom delimiter | `"Helloxthere"` | `["Hello", "there"]` |

#### Example Usage

```python
from tokenizers import pre_tokenizers
from tokenizers.pre_tokenizers import Whitespace, Digits

# Single pre-tokenizer
tokenizer.pre_tokenizer = Whitespace()

# Combine multiple pre-tokenizers
tokenizer.pre_tokenizer = pre_tokenizers.Sequence([
    Whitespace(),
    Digits(individual_digits=True)  # Split each digit separately
])

# Test it
result = tokenizer.pre_tokenizer.pre_tokenize_str("Call 911!")
print(result)
# [("Call", (0, 4)), ("9", (5, 6)), ("1", (6, 7)), ("1", (7, 8)), ("!", (8, 9))]
```

### 3. Models

**Purpose**: The core tokenization algorithm

#### Available Models

| Model | Algorithm | Best For | Vocab Size |
|-------|-----------|----------|------------|
| **BPE** | Byte-Pair Encoding | General purpose, GPT | Flexible |
| **WordPiece** | Greedy longest-first | BERT, Google models | 30K typical |
| **Unigram** | Probabilistic | SentencePiece, XLNet | Flexible |
| **WordLevel** | Simple word mapping | Simple tasks, requires large vocab | Large |

#### Model Characteristics

**BPE (Byte-Pair Encoding)**
- Starts with characters, merges frequent pairs
- Used by: GPT-2, GPT-3, RoBERTa, BART
- Pros: Handles unknown words well, compact vocabulary
- Cons: Can be slow to train

**WordPiece**
- Greedy algorithm, builds long words first
- Used by: BERT, DistilBERT, Electra
- Pros: Good for languages with compound words
- Cons: Requires `##` prefix for subwords
- Special marker: `##` for continuing subwords

**Unigram**
- Probabilistic model, finds best tokenization
- Used by: AlBERT, T5, XLNet
- Pros: Multiple tokenization possibilities
- Cons: More complex training

**WordLevel**
- Classic word-to-ID mapping
- Used by: Simple baseline models
- Pros: Very simple, fast
- Cons: Needs huge vocabulary, many unknown tokens

#### Example Usage

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE, WordPiece, Unigram, WordLevel

# BPE Model
bpe_tokenizer = Tokenizer(BPE(
    unk_token="[UNK]",
    continuing_subword_prefix="",
    end_of_word_suffix=""
))

# WordPiece Model (BERT-style)
wordpiece_tokenizer = Tokenizer(WordPiece(
    unk_token="[UNK]",
    max_input_chars_per_word=100
))

# Unigram Model
unigram_tokenizer = Tokenizer(Unigram())

# WordLevel Model
wordlevel_tokenizer = Tokenizer(WordLevel(
    unk_token="[UNK]"
))
```

### 4. Post-Processors

**Purpose**: Add special tokens and format for models

#### Available Post-Processors

| Post-Processor | Description | Use Case |
|----------------|-------------|----------|
| **TemplateProcessing** | Flexible template-based | BERT, RoBERTa style |
| **BertProcessing** | BERT-specific | BERT models |
| **RobertaProcessing** | RoBERTa-specific | RoBERTa models |
| **ByteLevel** | Trim byte-level offsets | GPT-2 style |

#### Example Usage

```python
from tokenizers.processors import TemplateProcessing

# BERT-style post-processing
tokenizer.post_processor = TemplateProcessing(
    single="[CLS] $A [SEP]",
    pair="[CLS] $A [SEP] $B:1 [SEP]:1",
    special_tokens=[
        ("[CLS]", tokenizer.token_to_id("[CLS]")),
        ("[SEP]", tokenizer.token_to_id("[SEP]")),
    ],
)

# Test single sequence
output = tokenizer.encode("Hello world")
print(output.tokens)
# ["[CLS]", "Hello", "world", "[SEP]"]

# Test pair of sequences
output = tokenizer.encode("Hello world", "How are you?")
print(output.tokens)
# ["[CLS]", "Hello", "world", "[SEP]", "How", "are", "you", "?", "[SEP]"]
print(output.type_ids)
# [0, 0, 0, 0, 1, 1, 1, 1, 1]
```

### 5. Decoders

**Purpose**: Convert token IDs back to text

#### Available Decoders

| Decoder | Description | Use With |
|---------|-------------|----------|
| **WordPiece** | Handle `##` prefix | WordPiece models |
| **ByteLevel** | Revert byte-level encoding | GPT-2 style models |
| **Metaspace** | Revert `▁` character | SentencePiece models |
| **BPEDecoder** | Handle BPE suffixes | BPE models |
| **CTC** | CTC decoding | Speech recognition |

#### Example Usage

```python
from tokenizers import decoders

# WordPiece Decoder (for BERT)
tokenizer.decoder = decoders.WordPiece(prefix="##")

# ByteLevel Decoder (for GPT-2)
tokenizer.decoder = decoders.ByteLevel()

# Metaspace Decoder (for SentencePiece)
tokenizer.decoder = decoders.Metaspace()

# Test decoding
output = tokenizer.encode("Hello, world!")
decoded = tokenizer.decode(output.ids)
print(decoded)  # "Hello, world!"
```

---

## Training Custom Tokenizers

### Example 1: Train BPE Tokenizer

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.normalizers import NFD, Lowercase, StripAccents
from tokenizers import normalizers

# 1. Initialize
tokenizer = Tokenizer(BPE(unk_token="[UNK]"))

# 2. Configure normalization
tokenizer.normalizer = normalizers.Sequence([NFD(), Lowercase(), StripAccents()])

# 3. Configure pre-tokenization
tokenizer.pre_tokenizer = Whitespace()

# 4. Create trainer
trainer = BpeTrainer(
    vocab_size=30000,                # Final vocabulary size
    min_frequency=2,                 # Minimum frequency to merge
    special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
    show_progress=True
)

# 5. Train
files = ["data/train.txt", "data/valid.txt", "data/test.txt"]
tokenizer.train(files, trainer)

# 6. Save
tokenizer.save("bpe-tokenizer.json")

print("Training complete! Vocabulary size:", tokenizer.get_vocab_size())
```

### Example 2: Train WordPiece Tokenizer (BERT-style)

```python
from tokenizers import Tokenizer
from tokenizers.models import WordPiece
from tokenizers.trainers import WordPieceTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.normalizers import BertNormalizer
from tokenizers.processors import TemplateProcessing

# 1. Initialize with WordPiece
tokenizer = Tokenizer(WordPiece(unk_token="[UNK]"))

# 2. BERT-style normalization
tokenizer.normalizer = BertNormalizer(
    clean_text=True,
    handle_chinese_chars=True,
    strip_accents=True,
    lowercase=True
)

# 3. Pre-tokenization
tokenizer.pre_tokenizer = Whitespace()

# 4. Create trainer
trainer = WordPieceTrainer(
    vocab_size=30522,  # BERT vocabulary size
    special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
    continuing_subword_prefix="##"
)

# 5. Train
files = ["data/corpus.txt"]
tokenizer.train(files, trainer)

# 6. Add post-processing
tokenizer.post_processor = TemplateProcessing(
    single="[CLS] $A [SEP]",
    pair="[CLS] $A [SEP] $B:1 [SEP]:1",
    special_tokens=[
        ("[CLS]", 1),
        ("[SEP]", 2),
    ],
)

# 7. Save
tokenizer.save("bert-wordpiece.json")
```

### Example 3: Train from Memory (No Files)

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer

# Your data in memory
dataset = [
    "The quick brown fox jumps over the lazy dog.",
    "Machine learning is awesome!",
    "Tokenizers make NLP easier.",
    # ... more sentences
]

# Initialize tokenizer
tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])

# Train from iterator
tokenizer.train_from_iterator(
    dataset,
    trainer=trainer,
    length=len(dataset)  # Optional: for progress bar
)

print(f"Trained on {len(dataset)} sequences")
```

---

## Working with Pretrained Tokenizers

### Load from Hugging Face Hub

```python
from tokenizers import Tokenizer

# Load BERT tokenizer
bert_tokenizer = Tokenizer.from_pretrained("bert-base-uncased")

# Load GPT-2 tokenizer
gpt2_tokenizer = Tokenizer.from_pretrained("gpt2")

# Load with specific revision
tokenizer = Tokenizer.from_pretrained(
    "bert-base-uncased",
    revision="main",
    auth_token="your_token_here"  # For private repos
)
```

### Load from Legacy Vocabulary Files

```python
from tokenizers import BertWordPieceTokenizer

# Load BERT tokenizer from vocab file
tokenizer = BertWordPieceTokenizer(
    "bert-base-uncased-vocab.txt",
    lowercase=True
)

# Download vocab file first:
# wget https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-vocab.txt
```

---

## Advanced Features

### 1. Encoding - The Encoding Object

The `Encoding` object contains all information about tokenization:

```python
output = tokenizer.encode("Hello, y'all! How are you 😁 ?")

# Token strings
print(output.tokens)
# ["Hello", ",", "y", "'", "all", "!", "How", "are", "you", "[UNK]", "?"]

# Token IDs
print(output.ids)
# [27253, 16, 93, 11, 5097, 5, 7961, 5112, 6218, 0, 35]

# Character offsets (alignment tracking)
print(output.offsets)
# [(0, 5), (5, 6), (7, 8), (8, 9), (9, 12), (12, 13), (14, 17), (18, 21), (22, 25), (26, 27), (28, 29)]

# Attention mask
print(output.attention_mask)
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Type IDs (for pairs)
print(output.type_ids)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Special tokens mask
print(output.special_tokens_mask)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Word IDs (which word each token belongs to)
print(output.word_ids)
# [0, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
```

### 2. Alignment Tracking

Find original text from tokens and vice versa:

```python
text = "Hello, y'all! How are you 😁 ?"
output = tokenizer.encode(text)

# Token to original characters
token_index = 9  # The "[UNK]" token
start, end = output.offsets[token_index]
print(f"Token '{output.tokens[token_index]}' came from: '{text[start:end]}'")
# Token '[UNK]' came from: '😁'

# Character to token
char_pos = 26  # Position of emoji
token_idx = output.char_to_token(char_pos)
print(f"Character at position {char_pos} is in token: {output.tokens[token_idx]}")
# Character at position 26 is in token: [UNK]

# Word to tokens
word_idx = 0  # First word
token_range = output.word_to_tokens(word_idx)
print(f"Word {word_idx} maps to tokens: {output.tokens[token_range[0]:token_range[1]]}")
```

### 3. Batch Encoding

Process multiple sequences efficiently:

```python
# Encode multiple sequences
sequences = [
    "Hello, y'all!",
    "How are you?",
    "I'm fine, thank you!"
]

outputs = tokenizer.encode_batch(sequences)

# Each output is an Encoding object
for i, output in enumerate(outputs):
    print(f"Sequence {i}: {output.tokens}")

# Encode pairs of sequences
pairs = [
    ("Hello", "How are you?"),
    ("Good morning", "Nice to meet you")
]

outputs = tokenizer.encode_batch(pairs)
```

### 4. Padding and Truncation

#### Enable Padding

```python
# Enable padding
tokenizer.enable_padding(
    direction="right",        # or "left"
    pad_id=3,                # ID of [PAD] token
    pad_token="[PAD]",
    length=None,             # Pad to longest in batch
    pad_to_multiple_of=8     # Optional: pad to multiple of 8
)

# Encode batch - shorter sequences will be padded
outputs = tokenizer.encode_batch(["Hello", "How are you doing today?"])

print(outputs[0].tokens)
# ["[CLS]", "Hello", "[SEP]", "[PAD]", "[PAD]", "[PAD]", "[PAD]"]

print(outputs[0].attention_mask)
# [1, 1, 1, 0, 0, 0, 0]

# Disable padding
tokenizer.no_padding()
```

#### Enable Truncation

```python
# Enable truncation
tokenizer.enable_truncation(
    max_length=512,
    stride=0,                          # For overflowing tokens
    strategy="longest_first",          # or "only_first", "only_second"
    direction="right"                  # or "left"
)

# Encode long text - will be truncated
long_text = "word " * 1000
output = tokenizer.encode(long_text)
print(f"Truncated to {len(output.tokens)} tokens")

# Access overflowing tokens
if output.overflowing:
    print(f"Found {len(output.overflowing)} overflow chunks")

# Disable truncation
tokenizer.no_truncation()
```

### 5. Special Tokens

```python
# Add special tokens (never split)
tokenizer.add_special_tokens(["[CUSTOM]", "[SPECIAL]"])

# Add regular tokens
num_added = tokenizer.add_tokens(["tensorflow", "pytorch"])
print(f"Added {num_added} new tokens")

# Query token IDs
token_id = tokenizer.token_to_id("[MASK]")
print(f"[MASK] token ID: {token_id}")

# Query token from ID
token = tokenizer.id_to_token(0)
print(f"ID 0 maps to token: {token}")

# Get full vocabulary
vocab = tokenizer.get_vocab()
print(f"Vocabulary size: {len(vocab)}")
```

### 6. Decoding

```python
# Decode single sequence
ids = [1, 27253, 16, 93, 11, 5097, 2]
text = tokenizer.decode(ids)
print(text)
# "Hello , y ' all"

# Decode without special tokens
text = tokenizer.decode(ids, skip_special_tokens=True)
print(text)
# "Hello , y ' all"

# Decode batch
ids_batch = [[1, 27253, 2], [1, 7961, 2]]
texts = tokenizer.decode_batch(ids_batch)
print(texts)
# ["Hello", "How"]
```

---

## Complete Examples

### Example 1: Complete BERT Tokenizer from Scratch

```python
from tokenizers import Tokenizer
from tokenizers.models import WordPiece
from tokenizers.trainers import WordPieceTrainer
from tokenizers.normalizers import BertNormalizer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.processors import TemplateProcessing
from tokenizers.decoders import WordPiece as WordPieceDecoder

def create_bert_tokenizer(vocab_size=30522):
    """Create a complete BERT-style tokenizer"""
    
    # 1. Model
    tokenizer = Tokenizer(WordPiece(unk_token="[UNK]"))
    
    # 2. Normalizer
    tokenizer.normalizer = BertNormalizer(
        clean_text=True,
        handle_chinese_chars=True,
        strip_accents=True,
        lowercase=True
    )
    
    # 3. Pre-tokenizer
    tokenizer.pre_tokenizer = Whitespace()
    
    # 4. Post-processor
    tokenizer.post_processor = TemplateProcessing(
        single="[CLS] $A [SEP]",
        pair="[CLS] $A [SEP] $B:1 [SEP]:1",
        special_tokens=[
            ("[CLS]", 1),
            ("[SEP]", 2),
        ],
    )
    
    # 5. Decoder
    tokenizer.decoder = WordPieceDecoder(prefix="##")
    
    # 6. Trainer
    trainer = WordPieceTrainer(
        vocab_size=vocab_size,
        special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
        continuing_subword_prefix="##"
    )
    
    return tokenizer, trainer

# Create and train
tokenizer, trainer = create_bert_tokenizer()
files = ["data/train.txt"]
tokenizer.train(files, trainer)

# Test
output = tokenizer.encode("Hello, world!", "How are you?")
print(f"Tokens: {output.tokens}")
print(f"IDs: {output.ids}")
print(f"Type IDs: {output.type_ids}")

# Decode
decoded = tokenizer.decode(output.ids)
print(f"Decoded: {decoded}")
```

### Example 2: GPT-2 Style Tokenizer

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import ByteLevel as ByteLevelPreTokenizer
from tokenizers.decoders import ByteLevel as ByteLevelDecoder

def create_gpt2_tokenizer(vocab_size=50257):
    """Create a GPT-2 style tokenizer"""
    
    # 1. Model
    tokenizer = Tokenizer(BPE(unk_token="<|endoftext|>"))
    
    # 2. Pre-tokenizer (ByteLevel)
    tokenizer.pre_tokenizer = ByteLevelPreTokenizer(add_prefix_space=True)
    
    # 3. Decoder
    tokenizer.decoder = ByteLevelDecoder()
    
    # 4. Trainer
    trainer = BpeTrainer(
        vocab_size=vocab_size,
        special_tokens=["<|endoftext|>"],
        show_progress=True
    )
    
    return tokenizer, trainer

# Create and train
tokenizer, trainer = create_gpt2_tokenizer()
files = ["data/corpus.txt"]
tokenizer.train(files, trainer)

# Test
output = tokenizer.encode("Hello world! 🚀")
print(f"Tokens: {output.tokens}")
print(f"IDs: {output.ids}")
```

### Example 3: Custom Domain-Specific Tokenizer

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.normalizers import Lowercase

def create_code_tokenizer():
    """Create a tokenizer optimized for code"""
    
    # 1. Model
    tokenizer = Tokenizer(BPE(unk_token="<UNK>"))
    
    # 2. Normalizer - keep case for code
    # tokenizer.normalizer = None  # Or minimal normalization
    
    # 3. Pre-tokenizer
    tokenizer.pre_tokenizer = Whitespace()
    
    # 4. Trainer with code-specific tokens
    trainer = BpeTrainer(
        vocab_size=20000,
        special_tokens=[
            "<UNK>",
            "<PAD>",
            "<BOS>",  # Beginning of sequence
            "<EOS>",  # End of sequence
            "<INDENT>",
            "<DEDENT>",
            "<NEWLINE>"
        ],
        show_progress=True
    )
    
    return tokenizer, trainer

# Create and train on code files
tokenizer, trainer = create_code_tokenizer()
code_files = ["data/code1.py", "data/code2.py", "data/code3.js"]
tokenizer.train(code_files, trainer)

# Test on code
code = """
def hello_world():
    print("Hello, world!")
    return True
"""

output = tokenizer.encode(code)
print(f"Code tokens: {output.tokens}")
```

### Example 4: Multilingual Tokenizer

```python
from tokenizers import Tokenizer
from tokenizers.models import Unigram
from tokenizers.trainers import UnigramTrainer
from tokenizers.normalizers import NFKC
from tokenizers.pre_tokenizers import Metaspace

def create_multilingual_tokenizer():
    """Create a SentencePiece-style multilingual tokenizer"""
    
    # 1. Model (Unigram is often used for multilingual)
    tokenizer = Tokenizer(Unigram())
    
    # 2. Normalizer
    tokenizer.normalizer = NFKC()
    
    # 3. Pre-tokenizer (Metaspace for SentencePiece compatibility)
    tokenizer.pre_tokenizer = Metaspace()
    
    # 4. Trainer
    trainer = UnigramTrainer(
        vocab_size=32000,
        special_tokens=["<pad>", "<s>", "</s>", "<unk>"],
        unk_token="<unk>",
        show_progress=True
    )
    
    return tokenizer, trainer

# Create and train on multilingual data
tokenizer, trainer = create_multilingual_tokenizer()
multilingual_files = [
    "data/english.txt",
    "data/spanish.txt",
    "data/chinese.txt",
    "data/arabic.txt"
]
tokenizer.train(multilingual_files, trainer)

# Test on different languages
texts = [
    "Hello world",           # English
    "Hola mundo",            # Spanish
    "你好世界",              # Chinese
    "مرحبا بالعالم"          # Arabic
]

for text in texts:
    output = tokenizer.encode(text)
    print(f"{text}: {output.tokens}")
```

---

## Best Practices

### 1. Choosing the Right Model

```python
# Use BPE when:
# - You want a good balance of speed and quality
# - Working with English or Western languages
# - Need good handling of rare words
bpe_tokenizer = Tokenizer(BPE(unk_token="[UNK]"))

# Use WordPiece when:
# - Building BERT-style models
# - Working with compound words (German, etc.)
# - Need compatibility with BERT
wordpiece_tokenizer = Tokenizer(WordPiece(unk_token="[UNK]"))

# Use Unigram when:
# - Working with Asian languages (Japanese, Chinese, Korean)
# - Want probabilistic tokenization
# - Building T5 or XLNet style models
unigram_tokenizer = Tokenizer(Unigram())

# Use WordLevel when:
# - Have a small, controlled vocabulary
# - Building simple baseline models
# - Speed is critical, accuracy less so
wordlevel_tokenizer = Tokenizer(WordLevel(unk_token="[UNK]"))
```

### 2. Vocabulary Size Guidelines

```python
# Small vocabulary (good for limited data)
trainer = BpeTrainer(vocab_size=8000)

# Medium vocabulary (general purpose)
trainer = BpeTrainer(vocab_size=30000)  # BERT standard

# Large vocabulary (for large diverse datasets)
trainer = BpeTrainer(vocab_size=50000)  # GPT-2

# Very large vocabulary (multilingual, massive datasets)
trainer = BpeTrainer(vocab_size=128000)  # XLM-RoBERTa
```

### 3. Training Data Requirements

```python
# Minimum data guidelines:
# - Small vocab (8K):     ~1M tokens  (100KB text)
# - Medium vocab (30K):   ~10M tokens (1MB text)
# - Large vocab (50K):    ~100M tokens (10MB text)
# - Very large (128K):    ~1B tokens (100MB text)

# Train from multiple sources
files = [
    "data/books.txt",        # 50MB
    "data/news.txt",         # 30MB
    "data/wikipedia.txt",    # 100MB
    "data/conversations.txt" # 20MB
]
tokenizer.train(files, trainer)
```

### 4. Special Tokens Strategy

```python
# Minimal special tokens (GPT-2 style)
special_tokens = ["<|endoftext|>"]

# Standard special tokens (BERT style)
special_tokens = ["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"]

# Extended special tokens (task-specific)
special_tokens = [
    "[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]",  # Standard
    "[USER]", "[ASSISTANT]",                        # Chat
    "[PYTHON]", "[JAVASCRIPT]", "[HTML]",           # Code
    "[MATH]", "[TABLE]", "[IMAGE]"                  # Multimodal
]

trainer = BpeTrainer(special_tokens=special_tokens)
```

### 5. Saving and Loading Efficiently

```python
# Save tokenizer (recommended)
tokenizer.save("tokenizer.json")

# Load tokenizer (fast)
tokenizer = Tokenizer.from_file("tokenizer.json")

# Save with pretty formatting (for debugging)
tokenizer.save("tokenizer.json", pretty=True)

# Export to string (for embedding in code)
json_str = tokenizer.to_str(pretty=False)

# Load from string
tokenizer = Tokenizer.from_str(json_str)
```

### 6. Performance Optimization

```python
# Use batch encoding for multiple sequences
sequences = ["text1", "text2", "text3", ...]
outputs = tokenizer.encode_batch(sequences)  # Much faster than loop

# Enable parallel processing when training
trainer = BpeTrainer(
    vocab_size=30000,
    show_progress=True
)

# Use train_from_iterator for large datasets
def data_generator():
    with open("large_file.txt") as f:
        for line in f:
            yield line.strip()

tokenizer.train_from_iterator(
    data_generator(),
    trainer=trainer,
    length=1000000  # Approximate number of sequences
)
```

### 7. Debugging and Visualization

```python
from tokenizers.tools import EncodingVisualizer

# Create visualizer
visualizer = EncodingVisualizer(tokenizer)

# Visualize tokenization
text = "Hello, how are you today?"
visualizer(text)  # Shows HTML visualization in notebook

# Check token alignments
output = tokenizer.encode(text)
for i, token in enumerate(output.tokens):
    start, end = output.offsets[i]
    print(f"Token '{token}' -> Original: '{text[start:end]}'")

# Inspect vocabulary
vocab = tokenizer.get_vocab()
print(f"Total tokens: {len(vocab)}")
print(f"First 10 tokens: {list(vocab.items())[:10]}")
```

### 8. Testing Your Tokenizer

```python
def test_tokenizer(tokenizer, test_cases):
    """Test tokenizer on various cases"""
    
    print("=" * 50)
    print("TOKENIZER TESTING")
    print("=" * 50)
    
    for text in test_cases:
        output = tokenizer.encode(text)
        decoded = tokenizer.decode(output.ids)
        
        print(f"\nInput:   {text}")
        print(f"Tokens:  {output.tokens}")
        print(f"IDs:     {output.ids}")
        print(f"Decoded: {decoded}")
        print(f"Match:   {'✓' if text.replace(' ', '') == decoded.replace(' ', '') else '✗'}")

# Test cases
test_cases = [
    "Hello, world!",
    "The quick brown fox jumps over the lazy dog.",
    "Machine learning is awesome! 🚀",
    "Code: print('Hello')",
    "Email: test@example.com",
    "URL: https://huggingface.co",
    "Number: 12,345.67",
    "Unicode: café, naïve, résumé",
]

test_tokenizer(tokenizer, test_cases)
```

---

## Summary

### Key Takeaways

1. **Choose the right model**: BPE for general use, WordPiece for BERT-style, Unigram for multilingual
2. **Configure the pipeline**: Normalizer → PreTokenizer → Model → PostProcessor → Decoder
3. **Train on sufficient data**: More data = better tokenization
4. **Use batch operations**: Much faster than encoding one-by-one
5. **Test thoroughly**: Verify tokenization/detokenization round-trips
6. **Save properly**: Use JSON format for portability

### Next Steps

1. **Practice**: Train a tokenizer on your own domain-specific data
2. **Experiment**: Try different models and configurations
3. **Benchmark**: Compare speed and quality of different approaches
4. **Integrate**: Use with Transformers library for complete NLP pipelines
5. **Optimize**: Profile and optimize for your specific use case

### Resources

- **Documentation**: https://huggingface.co/docs/tokenizers
- **GitHub**: https://github.com/huggingface/tokenizers
- **Transformers Integration**: https://huggingface.co/docs/transformers
- **Community**: https://discuss.huggingface.co

---

## Time Estimate

- **Quick Start**: 30 minutes
- **Complete Tutorial**: 2-3 hours
- **Master All Features**: 8-10 hours
- **Build Custom Tokenizer**: 1-2 days

---

**Happy Tokenizing! 🚀**
