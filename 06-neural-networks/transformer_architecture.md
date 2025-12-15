# Transformer Architecture: Complete Guide

## Table of Contents

1. [Overview](#overview)
2. [The Big Picture](#the-big-picture)
3. [Input Processing](#input-processing)
4. [Encoder Block](#encoder-block)
5. [Decoder Block](#decoder-block)
6. [Three Transformer Variants](#three-transformer-variants)
7. [Training and Inference](#training-and-inference)
8. [Modern Innovations](#modern-innovations)

---

## Overview

The Transformer, introduced in "Attention Is All You Need" (2017), revolutionized AI by replacing recurrent layers with attention mechanisms.

### Key Innovation

```
Before (RNN/LSTM):
  Sequential processing → Slow training, gradient issues

After (Transformer):
  Parallel attention → Fast training, better performance
```

### Core Components

1. **Multi-Head Self-Attention**: Focus on relevant parts
2. **Position-wise Feed-Forward**: Process each position
3. **Positional Encoding**: Add sequence order information
4. **Layer Normalization**: Stabilize training
5. **Residual Connections**: Help gradient flow

---

## The Big Picture

### Original Transformer (Encoder-Decoder)

```
Input Sequence → [ENCODER] → Context → [DECODER] → Output Sequence
   "Hello"         ↓                       ↓           "Bonjour"
                6x layers              6x layers
                   ↓                       ↓
              Representation          Generation
```

### Architecture Diagram

```
                    OUTPUT
                      ↑
                [Linear + Softmax]
                      ↑
                [Decoder Stack]
                 (N x Decoder)
              /      ↑      \
    [Multi-Head  [Feed     [Add &
     Attention]  Forward]   Norm]
         ↑          ↑          ↑
    [Encoder Stack Output]    |
         ↓                     |
    [Encoder Stack]            |
     (N x Encoder)             |
         ↑                     |
    [Input Embedding + Positional Encoding]
         ↑
      INPUT
```

---

## Input Processing

### 1. Token Embedding

Convert tokens to dense vectors:

```python
# Input: Token IDs
tokens = [2054, 2003, 1996]  # "what is the"

# Embedding layer
embedding = nn.Embedding(vocab_size=30000, embedding_dim=512)
embedded = embedding(tokens)
# Shape: (seq_len, d_model) = (3, 512)
```

### 2. Positional Encoding

**Problem:** Attention has no notion of order!

```
"cat sat on mat" == "mat on sat cat" (to attention mechanism)
```

**Solution:** Add position information to embeddings.

**Formula (Sinusoidal Encoding):**

```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

Where:
- pos = position in sequence (0, 1, 2, ...)
- i = dimension index (0, 1, 2, ..., d_model/2)
- d_model = embedding dimension (512 in original)
```

**Implementation:**

```python
import torch
import math

def positional_encoding(seq_len, d_model):
    """Generate positional encodings"""
    pe = torch.zeros(seq_len, d_model)
    
    position = torch.arange(0, seq_len).unsqueeze(1)  # (seq_len, 1)
    div_term = torch.exp(
        torch.arange(0, d_model, 2) * 
        -(math.log(10000.0) / d_model)
    )
    
    # Apply sin to even indices
    pe[:, 0::2] = torch.sin(position * div_term)
    # Apply cos to odd indices
    pe[:, 1::2] = torch.cos(position * div_term)
    
    return pe

# Generate positional encodings
pos_enc = positional_encoding(seq_len=100, d_model=512)
```

**Why Sinusoidal?**
- ✅ Unique encoding for each position
- ✅ Relative positions have consistent patterns
- ✅ Can extrapolate to longer sequences than seen during training
- ✅ No learned parameters (generalizes better)

**Final Input:**

```python
input_representation = token_embedding + positional_encoding
# Both have shape (seq_len, d_model)
```

---

## Encoder Block

Each encoder consists of two main components:

### 1. Multi-Head Self-Attention

```python
class EncoderBlock(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        
        # Multi-head attention
        self.attention = MultiHeadAttention(d_model, num_heads)
        self.norm1 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(dropout)
        
        # Feed-forward network
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Linear(d_ff, d_model)
        )
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout2 = nn.Dropout(dropout)
    
    def forward(self, x, mask=None):
        # Multi-head attention with residual connection
        attn_output = self.attention(x, x, x, mask)
        x = self.norm1(x + self.dropout1(attn_output))
        
        # Feed-forward with residual connection
        ffn_output = self.ffn(x)
        x = self.norm2(x + self.dropout2(ffn_output))
        
        return x
```

### Components Breakdown

#### Multi-Head Self-Attention

```
Input (seq_len, d_model)
    ↓
[Linear projections to Q, K, V]
    ↓
[Split into num_heads]
    ↓
[Scaled dot-product attention per head]
    ↓
[Concatenate heads]
    ↓
[Linear projection]
    ↓
Output (seq_len, d_model)
```

**Parameters:**
- Original transformer: 8 heads, d_model=512, d_k=d_v=64

#### Add & Norm (Residual Connection + Layer Normalization)

**Residual Connection:**
```python
output = x + sublayer(x)
```

**Why?**
- Helps gradients flow during backpropagation
- Allows training very deep networks
- Model can learn identity function if needed

**Layer Normalization:**
```python
# Normalize across features for each sample
mean = x.mean(dim=-1, keepdim=True)
std = x.std(dim=-1, keepdim=True)
normalized = (x - mean) / (std + epsilon)
output = gamma * normalized + beta  # Learnable parameters
```

**Why?**
- Stabilizes training
- Reduces internal covariate shift
- Allows higher learning rates

#### Position-wise Feed-Forward Network

```python
FFN(x) = max(0, x @ W1 + b1) @ W2 + b2
       = ReLU(x @ W1 + b1) @ W2 + b2
```

**Architecture:**
```
Input (seq_len, d_model=512)
    ↓
[Linear Layer: 512 → 2048]
    ↓
[ReLU Activation]
    ↓
[Linear Layer: 2048 → 512]
    ↓
Output (seq_len, d_model=512)
```

**Why?**
- Adds non-linearity and model capacity
- Processes each position independently
- d_ff typically 4x larger than d_model

### Complete Encoder

Stack N encoder blocks (N=6 in original):

```python
class Encoder(nn.Module):
    def __init__(self, num_layers, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        self.layers = nn.ModuleList([
            EncoderBlock(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])
        self.norm = nn.LayerNorm(d_model)
    
    def forward(self, x, mask=None):
        for layer in self.layers:
            x = layer(x, mask)
        return self.norm(x)
```

---

## Decoder Block

### Architecture

Similar to encoder but with additional components:

```python
class DecoderBlock(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        
        # Masked multi-head self-attention
        self.self_attention = MultiHeadAttention(d_model, num_heads)
        self.norm1 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(dropout)
        
        # Cross-attention to encoder output
        self.cross_attention = MultiHeadAttention(d_model, num_heads)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout2 = nn.Dropout(dropout)
        
        # Feed-forward network
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Linear(d_ff, d_model)
        )
        self.norm3 = nn.LayerNorm(d_model)
        self.dropout3 = nn.Dropout(dropout)
    
    def forward(self, x, encoder_output, src_mask=None, tgt_mask=None):
        # Masked self-attention
        self_attn = self.self_attention(x, x, x, tgt_mask)
        x = self.norm1(x + self.dropout1(self_attn))
        
        # Cross-attention to encoder
        cross_attn = self.cross_attention(x, encoder_output, encoder_output, src_mask)
        x = self.norm2(x + self.dropout2(cross_attn))
        
        # Feed-forward
        ffn_output = self.ffn(x)
        x = self.norm3(x + self.dropout3(ffn_output))
        
        return x
```

### Three Attention Mechanisms

#### 1. Masked Self-Attention (Causal Attention)

**Purpose:** Prevent decoder from seeing future tokens

```
When generating word 3, can only see words 0, 1, 2

Mask (lower triangular):
  [[1, 0, 0, 0],
   [1, 1, 0, 0],
   [1, 1, 1, 0],
   [1, 1, 1, 1]]

0 positions get -∞ in attention scores, 
resulting in 0 attention weight after softmax
```

**Why?**
- During training: Model learns to generate sequentially
- During inference: Matches training behavior

#### 2. Cross-Attention (Encoder-Decoder Attention)

**Purpose:** Decoder attends to encoder outputs

```
Query: From decoder current state
Key & Value: From encoder output

Example (Translation):
English (encoder): "I love machine learning"
French (decoder): "J'adore"

When generating next French word:
- Query: Current decoder state for "J'adore"
- Attends to: All English words
- Focuses on: "love" and "machine learning"
- Generates: "l'apprentissage"
```

#### 3. Feed-Forward Network

Same as encoder FFN.

---

## Three Transformer Variants

### 1. Encoder-Only (BERT)

```
Input → [Encoder Stack] → Output

Use cases:
- Text classification (sentiment, topic)
- Named entity recognition
- Question answering (extractive)
- Text similarity

Examples: BERT, RoBERTa, DistilBERT, ALBERT
```

**Architecture:**
```python
class BERTModel:
    def __init__(self):
        self.embedding = Embedding()
        self.encoder = Encoder(num_layers=12)
        
    def forward(self, input_ids):
        x = self.embedding(input_ids)
        encoded = self.encoder(x)
        return encoded  # Use for downstream tasks
```

**Training:** Masked Language Modeling (MLM)
```
Input:  "The [MASK] sat on the mat"
Target: "cat"
```

### 2. Decoder-Only (GPT)

```
Input → [Decoder Stack] → Next Token

Use cases:
- Text generation
- Completion
- Chatbots
- Code generation

Examples: GPT, GPT-2, GPT-3, GPT-4, LLaMA, Mistral
```

**Architecture:**
```python
class GPTModel:
    def __init__(self):
        self.embedding = Embedding()
        self.decoder = Decoder(num_layers=12)  # Only self-attention, no cross-attention
        self.lm_head = nn.Linear(d_model, vocab_size)
        
    def forward(self, input_ids):
        x = self.embedding(input_ids)
        decoded = self.decoder(x, causal_mask=True)
        logits = self.lm_head(decoded)
        return logits  # Probabilities for next token
```

**Training:** Causal Language Modeling (CLM)
```
Input:  "The cat sat"
Target: "cat sat on"
```

### 3. Encoder-Decoder (T5, BART)

```
Input → [Encoder] → Context → [Decoder] → Output

Use cases:
- Machine translation
- Summarization
- Question answering (generative)
- Text-to-text tasks

Examples: T5, BART, mT5, MarianMT
```

**Architecture:**
```python
class Seq2SeqModel:
    def __init__(self):
        self.encoder = Encoder(num_layers=6)
        self.decoder = Decoder(num_layers=6)
        
    def forward(self, src_ids, tgt_ids):
        # Encode source
        encoder_output = self.encoder(src_ids)
        
        # Decode target
        decoder_output = self.decoder(tgt_ids, encoder_output)
        return decoder_output
```

**Training:** Seq2Seq
```
Source: "Translate to French: I love AI"
Target: "J'adore l'IA"
```

---

## Training and Inference

### Training Process

```python
# 1. Forward pass
encoder_output = encoder(source_tokens)
decoder_output = decoder(target_tokens, encoder_output)
logits = output_layer(decoder_output)

# 2. Compute loss
loss = cross_entropy(logits, target_labels)

# 3. Backward pass
loss.backward()

# 4. Update weights
optimizer.step()
```

### Inference (Generation)

**Autoregressive Generation:**

```python
def generate(model, prompt, max_length=50):
    """Generate text token by token"""
    tokens = tokenize(prompt)
    
    for _ in range(max_length):
        # Forward pass
        logits = model(tokens)
        
        # Get next token prediction
        next_token_logits = logits[-1]  # Last position
        next_token = sample(next_token_logits)  # Sample or argmax
        
        # Append to sequence
        tokens.append(next_token)
        
        # Stop if EOS token
        if next_token == EOS_TOKEN:
            break
    
    return detokenize(tokens)
```

**Sampling Strategies:**

1. **Greedy**: Always pick most likely token
```python
next_token = torch.argmax(logits)
```

2. **Top-k**: Sample from top k most likely tokens
```python
top_k_logits, top_k_indices = torch.topk(logits, k=50)
probs = softmax(top_k_logits)
next_token = sample(top_k_indices, probs)
```

3. **Top-p (Nucleus)**: Sample from tokens comprising top p probability mass
```python
sorted_probs, sorted_indices = torch.sort(probs, descending=True)
cumsum = torch.cumsum(sorted_probs, dim=-1)
nucleus = cumsum <= p
nucleus_probs = sorted_probs[nucleus]
next_token = sample(sorted_indices[nucleus], nucleus_probs)
```

4. **Temperature**: Control randomness
```python
logits = logits / temperature  # Higher temp = more random
probs = softmax(logits)
```

---

## Modern Innovations

### 1. Efficient Attention

**Problem:** Standard attention is O(n²) in sequence length

**Solutions:**

**Sparse Attention (GPT-3):**
- Only attend to subset of positions
- Local + strided patterns
- O(n√n) complexity

**Linear Attention:**
- Reformulate attention to be O(n)
- Kernel-based methods
- Examples: Performer, Linear Transformer

**Flash Attention:**
- GPU memory-optimized
- Faster training/inference
- No approximation, exact attention

### 2. Architectural Improvements

**Pre-Norm vs Post-Norm:**
```python
# Post-Norm (original)
x = norm(x + sublayer(x))

# Pre-Norm (more stable)
x = x + sublayer(norm(x))
```

**RMSNorm:** Simpler, faster than LayerNorm

**SwiGLU Activation:** Better than ReLU for LLMs

### 3. Positional Encodings

**Relative Positional Encoding (T5):**
- Attention scores modified based on relative distance
- Better for variable-length sequences

**Rotary Position Embedding (RoPE):**
- Used in GPT-NeoX, LLaMA
- Encodes relative positions via rotation
- Better extrapolation to longer sequences

**ALiBi (Attention with Linear Biases):**
- Add distance-based bias to attention scores
- Simple, effective for long sequences

### 4. Mixture of Experts (MoE)

```
Input → [Router] → Select K experts → Average outputs

Benefits:
- Larger model capacity
- Same inference cost (only K experts active)
- Used in GPT-4, Mixtral
```

### 5. Model Sizes

**Evolution:**
- 2018 BERT-base: 110M parameters
- 2019 GPT-2: 1.5B parameters
- 2020 GPT-3: 175B parameters
- 2023 GPT-4: ~1.7T parameters (rumored, MoE)

---

## Summary

**Key Takeaways:**

1. **Attention** replaces recurrence for sequence modeling
2. **Parallel processing** makes training efficient
3. **Positional encoding** adds sequence order information
4. **Residual connections** enable deep networks
5. **Layer normalization** stabilizes training

**Three variants:**
- **Encoder-only**: Understanding tasks (BERT)
- **Decoder-only**: Generation tasks (GPT)
- **Encoder-decoder**: Transformation tasks (T5)

**Modern developments:**
- Efficient attention mechanisms
- Better positional encodings
- Architectural improvements
- Scaling to trillions of parameters

**Next Steps:**
- Implement transformer components in code
- Fine-tune pre-trained models
- Build applications with Hugging Face Transformers

The transformer architecture is the foundation of modern AI! 🚀
