# Understanding Tokens: The Foundation of Language Models

## What Are Tokens?
**
**Tokens** are the fundamental building blocks that language models use to process text. Think of them as the "words" that AI models understand—though they're not exactly words in the traditional sense.

When you input text like `"Hello, world!"` into an LLM, the model doesn't process it as a continuous string. Instead, it breaks it down into **tokens**—discrete units that can be words, parts of words (subwords), or even individual characters.

## Why Tokens Matter

Language models can't directly understand human text. They need to convert text into numbers (tokens) that can be mathematically processed. This process is called **tokenization**.

**Example:**
```text
Input text: "hello how are you ?"
Tokens: [15339, 1268, 527, 499, 949]
Number of tokens: 5
```

Each number represents a specific piece of text from a pre-defined vocabulary. The model processes these numeric tokens, not the original text.

### Rules of Thumb for English

Understanding token counts helps estimate costs and context limits:

- **1 token ≈ 4 characters**
- **1 token ≈ ¾ of a word**
- **100 tokens ≈ 75 words**
- **1-2 sentences ≈ 30 tokens**
- **1 paragraph ≈ 100 tokens**
- **~1,500 words ≈ 2,048 tokens**

**Real-world examples:**
- "You miss 100% of the shots you don't take" (Wayne Gretzky) = 11 tokens
- US Declaration of Independence = 1,695 tokens
- Average email = 100-300 tokens

### Context Matters: Same Word, Different Tokens

The same word can become **different tokens** based on context:

```python
# Example: The word "red" tokenizes differently based on position
"The apple is red."     # ' red' (with leading space) → token: 2266
"Red is my favorite."   # 'Red' (capitalized, no space) → token: 7738  
"I like Red apples."    # ' Red' (with space, capital) → token: 2297
```

**Why?** The tokenizer learned from real text where:
- Words mid-sentence often have a leading space
- Words at sentence start are capitalized and have no leading space
- Capitalization changes meaning/usage

This context-awareness makes tokenization more efficient than simple word splitting.

## How Tokenization Works

Modern tokenization uses algorithms like **Byte-Pair Encoding (BPE)** or **WordPiece** to intelligently split text:

1. **Common words** → Single token
   - "hello" → 1 token
   - "world" → 1 token

2. **Uncommon words** → Multiple tokens (subwords)
   - "tokenization" → might split into ["token", "ization"]
   - "supercalifragilisticexpialidocious" → many smaller pieces

3. **Numbers and special characters** → Separate tokens
   - "GPT-4" → ["G", "PT", "-", "4"] or ["GPT", "-", "4"]

## Why Not Use Words?

You might wonder: "Why not just split text by spaces into words?" Here's why tokens are better:

### Problem with Word-Based Splitting:
- **Vocabulary explosion**: English has 170,000+ words. Adding other languages would make vocabulary enormous.
- **Out-of-vocabulary words**: New words (like "ChatGPT") wouldn't be recognized.
- **No handling of typos**: "helllo" would be completely different from "hello".
- **Different forms**: "run", "running", "ran" would be treated as completely separate entities.

### Token-Based Benefits:
- **Fixed vocabulary size**: Typically 50,000-100,000 tokens covers all languages.
- **Handles any word**: Unknown words are split into known subword tokens.
- **Related words share tokens**: "happy", "happiness", "unhappy" share the "happy" token.
- **Efficient**: Balances vocabulary size with text representation accuracy.

## Tokenization in Action

Let's see how different text gets tokenized:

```python
import tiktoken

# GPT-4 uses cl100k_base encoding
encoding = tiktoken.get_encoding("cl100k_base")

# Simple sentence
text1 = "hello how are you ?"
tokens1 = encoding.encode(text1)
print(f"'{text1}' → {tokens1}")
# Output: [15339, 1268, 527, 499, 949]  (5 tokens)

# Complex word
text2 = "supercalifragilisticexpialidocious"
tokens2 = encoding.encode(text2)
print(f"'{text2}' → {len(tokens2)} tokens")
# Output: Many tokens (word is split into subwords)

# Code example
text3 = "def hello_world():"
tokens3 = encoding.encode(text3)
print(f"'{text3}' → {tokens3}")
# Output: Each code element becomes tokens
```

## Key Concepts

### 1. Token vs Character vs Word

- **Character**: Single letter/symbol (`'h'`, `'e'`, `'l'`, `'l'`, `'o'`)
- **Token**: Subword unit (`'hello'` = 1 token, or split into smaller pieces)
- **Word**: Space-separated text (`'hello'`, `'world'`)

**Token is the middle ground** between characters (too granular) and words (too many unique units).

### 2. Context Window

LLMs have a **context window** measured in tokens, not characters:
- GPT-3.5: 4,096 tokens (~3,000 words)
- GPT-4: 8,192 or 32,768 tokens (~6,000-25,000 words)
- Claude 3: 200,000 tokens (~150,000 words)

This is why token counting matters—it determines how much text the model can process at once.

### 3. Token IDs

Each token has a unique **token ID** (integer):
- "hello" → 15339
- " world" → 1917 (note the space is part of the token)
- "!" → 0

The model's vocabulary is a mapping of token IDs to text pieces.

## Why Different Models Use Different Tokenizers

Different models use different tokenization schemes:

- **GPT-4, GPT-3.5**: `cl100k_base` (~100,000 tokens)
- **GPT-3**: `p50k_base` (~50,000 tokens)
- **BERT**: WordPiece tokenization
- **LLaMA**: SentencePiece BPE

Each tokenizer was trained on different data, optimizing for:
- Language coverage (English-only vs multilingual)
- Vocabulary size (memory constraints)
- Compression efficiency (fewer tokens = faster processing)

## Practical Implications

### 1. Cost

Many AI APIs charge per token:

- OpenAI GPT-4: $0.03 per 1K tokens (input)
- Knowing token count helps estimate costs

**Token categories for billing:**

- **Input tokens** – Your prompt/request
- **Output tokens** – Model's response (usually more expensive)
- **Cached tokens** – Reused conversation history (often discounted)
- **Reasoning tokens** – Internal "thinking" steps (some advanced models)

### 2. Performance

- Fewer tokens = Faster processing
- More tokens = Higher API costs
- Context window limits based on tokens

### 3. Prompt Engineering

Understanding tokenization helps craft better prompts:

```python
# Inefficient: "Please please please help me"
# tokens: ["Please", " please", " please", " help", " me"] = 5 tokens

# Efficient: "Please help me"
# tokens: ["Please", " help", " me"] = 3 tokens
```

### 4. Non-English Languages

Tokenization is less efficient for non-English text:

```python
# English: "How are you" = 3 tokens
# Spanish: "Cómo estás" = 5 tokens (for 10 characters)
```

Non-English text often has a **higher token-to-character ratio**, which affects:
- API costs (more tokens for same content)
- Context limits (fewer words fit in the same token budget)

## From Tokens to Embeddings

Once text is tokenized, each token is converted into an **embedding** (dense vector). This is the next step in how LLMs process language:

```
Text → Tokens → Embeddings → Model Processing → Output
```

- **Tokenization** (current topic): Text → Token IDs
- **Embeddings** (next topic): Token IDs → Dense vectors with semantic meaning

## Summary

| Aspect | Description |
|--------|-------------|
| **What** | Discrete units of text (subwords) |
| **Why** | Convert text to numbers for models |
| **How** | BPE, WordPiece algorithms |
| **Encoding** | Text → Token IDs (integers) |
| **Decoding** | Token IDs → Text |
| **Typical Size** | 50K-100K vocabulary |
| **Example** | "hello" → [15339] |

## Try It Yourself

Check out `tiktoken_example.py` to see tokenization in action with real examples.

---

**Next Step:** Learn about [Embeddings](../2-embeddings/) - how tokens are converted into meaningful vector representations that capture semantic relationships.

**See Also:**
- [Glossary](../0-glossary/GLOSSARY.md) - Definitions of AI/ML terms
- [Learning Roadmap](../0-glossary/ML_Topic_Guide.md) - Your personalized AI/ML learning path