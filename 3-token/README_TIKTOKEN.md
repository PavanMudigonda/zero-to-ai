# Phase 1: Understanding Tokens

**Learning Time:** 1-2 hours | **Difficulty:** Beginner

## What You'll Learn

By the end of this module, you will understand:
- ✅ What tokens are and why they're fundamental to LLMs
- ✅ How tokenization algorithms work (BPE, WordPiece)
- ✅ The difference between tokens, characters, and words
- ✅ How to use tiktoken to encode and decode text
- ✅ Why token count matters for costs and context limits
- ✅ How different languages and contexts affect tokenization

## Quick Start

```bash
# Install required package
pip install tiktoken

# Run the basic example
python tiktoken_example.py

# Run advanced examples
python token_exploration.py

# Try interactive exercises
python token_exercises.py
```

## Files in This Module

| File | Description | Run Time |
|------|-------------|----------|
| `intro.md` | Comprehensive theory and concepts | Read: 15-20 min |
| `tiktoken_example.py` | Basic tokenization example | 1 min |
| `token_exploration.py` | Advanced examples and comparisons | 3-5 min |
| `token_exercises.py` | Interactive practice exercises | 10-15 min |
| `tiktoken_example_output.txt` | Sample output for reference | - |

## Learning Path

### Step 1: Read the Theory (15-20 minutes)
Start with `intro.md` to understand:
- What tokens are and why they exist
- How tokenization works under the hood
- Practical implications for cost and performance

### Step 2: Run Basic Example (5 minutes)
```bash
python tiktoken_example.py
```
See tokenization in action with a simple example.

### Step 3: Explore Advanced Concepts (10 minutes)
```bash
python token_exploration.py
```
Discover how different types of text get tokenized:
- Common vs uncommon words
- Code and special characters
- Different languages
- Context-dependent tokenization

### Step 4: Practice with Exercises (15-20 minutes)
```bash
python token_exercises.py
```
Interactive exercises to test your understanding:
- Predict token counts
- Compare tokenization strategies
- Calculate API costs
- Optimize prompts for token efficiency

## Key Concepts

### Token Fundamentals

```python
# Text → Tokens → Token IDs → Model Processing
"Hello world" → ["Hello", " world"] → [9906, 1917] → [embeddings...]
```

**Token**: A unit of text (word, subword, or character) that a model processes

**Token ID**: A unique integer representing a token in the model's vocabulary

**Encoding**: Converting text into token IDs
**Decoding**: Converting token IDs back to text

### Why Tokens Matter

1. **Cost Calculation**
   - APIs charge per token (not per word or character)
   - Example: GPT-4 = $0.03 per 1K input tokens
   
2. **Context Limits**
   - Models have token limits (e.g., 8K, 32K, 128K tokens)
   - Must fit prompt + response within limit
   
3. **Processing Speed**
   - Fewer tokens = faster inference
   - Efficient tokenization improves performance

4. **Multilingual Support**
   - Subword tokenization handles any language
   - No need for language-specific dictionaries

### Token Count Rules of Thumb

| Text Type | Token Ratio |
|-----------|-------------|
| English text | 1 token ≈ 4 characters |
| English text | 1 token ≈ ¾ word |
| Code | 1 token ≈ 3-4 characters |
| Non-English | 1 token ≈ 2-3 characters |
| Numbers | Often 1-2 digits per token |

**Examples:**
- "Hello world!" = 3 tokens
- "GPT-4 is amazing" = 5 tokens
- "supercalifragilisticexpialidocious" = 7 tokens

## Common Pitfalls

### ❌ Mistake 1: Assuming 1 token = 1 word
```python
# Wrong assumption
text = "I love programming"  # 3 words
# Actual: 3 tokens ✅ (happens to match here)

text = "I love ML"  # 3 words  
# Actual: 4 tokens (M and L are separate) ❌
```

### ❌ Mistake 2: Ignoring leading spaces
```python
# These tokenize differently!
"red"     # Token: 1171
" red"    # Token: 2266 (with space)
```

### ❌ Mistake 3: Underestimating non-English costs
```python
# English: "How are you?" = 4 tokens
# Chinese: "你好吗?" = 6 tokens (for 3 characters!)
```

### ❌ Mistake 4: Not counting special tokens
```python
# Many models add special tokens:
# <|start|> text <|end|>
# These count toward your token limit!
```

## Advanced Topics

### Different Tokenization Algorithms

1. **Byte-Pair Encoding (BPE)** - Used by GPT models
   - Merges frequent character pairs iteratively
   - Good compression, handles any text
   
2. **WordPiece** - Used by BERT
   - Similar to BPE but uses likelihood-based merging
   - Optimized for vocabulary size
   
3. **SentencePiece** - Used by LLaMA, T5
   - Language-agnostic, treats text as raw bytes
   - No pre-tokenization (no word boundaries)

Note: Learn more at 
https://huggingface.co/docs/transformers/en/tokenizer_summary
https://www.reddit.com/r/MachineLearning/comments/rprmq3/d_sentencepiece_wordpiece_bpe_which_tokenizer_is/
https://medium.com/@lmpo/from-text-to-tokens-understanding-bpe-wordpiece-and-sentencepiece-in-nlp-1367d9d610af
https://medium.com/@lmpo/a-brief-history-of-ai-with-deep-learning-26f7948bc87b
https://medium.com/@lmpo/the-evolution-of-artificial-neurons-90619f224f63
### Model-Specific Encodings

| Model | Encoding | Vocab Size | Best For |
|-------|----------|------------|----------|
| GPT-4 | cl100k_base | ~100K | General purpose, code |
| GPT-3.5 | cl100k_base | ~100K | General purpose |
| GPT-3 | p50k_base | ~50K | English text |
| Code Cushman | p50k_edit | ~50K | Code editing |

### Token vs Context Window

**Context Window** = Maximum tokens the model can process at once

- Input tokens (your prompt)
- Output tokens (model's response)
- System tokens (instructions, special tokens)

**Example with 4K context:**
- 3,000 token prompt = only 1,000 tokens left for response
- 500 token prompt = 3,500 tokens available for response

## Practical Applications

### 1. Estimate API Costs
```python
def estimate_cost(text, model="gpt-4"):
    encoding = tiktoken.get_encoding("cl100k_base")
    token_count = len(encoding.encode(text))
    
    # GPT-4 pricing (example)
    input_cost_per_1k = 0.03
    cost = (token_count / 1000) * input_cost_per_1k
    
    return token_count, cost

text = "Your long prompt here..."
tokens, cost = estimate_cost(text)
print(f"Tokens: {tokens}, Cost: ${cost:.4f}")
```

### 2. Optimize Prompts
```python
# Before optimization
prompt = "Please, please, can you help me understand this?"
# 10 tokens

# After optimization
prompt = "Please explain this:"
# 4 tokens (60% reduction!)
```

### 3. Split Long Documents
```python
def chunk_text(text, max_tokens=1000):
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        chunks.append(encoding.decode(chunk_tokens))
    
    return chunks
```

## Practice Exercises

Work through `token_exercises.py` to test your understanding:

1. **Token Counting** - Predict token counts for various texts
2. **Cost Calculator** - Build a simple API cost estimator
3. **Prompt Optimizer** - Reduce token usage while keeping meaning
4. **Language Compare** - See how different languages tokenize
5. **Context Manager** - Fit text within token limits

## Verification Checklist

Before moving to Phase 2 (Embeddings), ensure you can:

- [ ] Explain what tokens are in your own words
- [ ] Use tiktoken to encode and decode text
- [ ] Calculate token counts for given text
- [ ] Understand why "word" ≠ "token"
- [ ] Estimate API costs based on token counts
- [ ] Recognize how context affects tokenization
- [ ] Split text to fit within token limits
- [ ] Compare tokenization across languages

## Common Questions

**Q: Why not just use words instead of tokens?**  
A: Words create a massive vocabulary (170K+ for English alone). Tokens use subwords, keeping vocabulary manageable (~50-100K) while handling any text.

**Q: Do all models use the same tokens?**  
A: No! Each model has its own tokenizer trained on specific data. GPT-4's "hello" might be a different token ID than LLaMA's "hello".

**Q: Are emojis one token?**  
A: Usually multiple tokens. 😀 might be 1-3 tokens depending on the encoding.

**Q: Does whitespace matter?**  
A: Yes! " hello" (with space) is different from "hello" (no space). Leading/trailing spaces create different tokens.

**Q: Can I create my own tokenizer?**  
A: Yes, but it requires training on large text corpora. Most developers use pre-trained tokenizers from model providers.

## Resources for Deeper Learning

### Official Documentation
- [tiktoken GitHub](https://github.com/openai/tiktoken) - Official OpenAI tokenizer
- [OpenAI Tokenizer Tool](https://platform.openai.com/tokenizer) - Interactive web tool

### Articles & Guides
- [OpenAI: What are tokens?](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)
- [Hugging Face: Tokenizers](https://huggingface.co/docs/transformers/tokenizer_summary)
- [BPE Algorithm Explained](https://towardsdatascience.com/byte-pair-encoding-subword-based-tokenization-algorithm-77828a70bee0)

### Videos
- [Andrej Karpathy: Tokenization](https://www.youtube.com/watch?v=zduSFxRajkE) - Deep dive into BPE
- [3Blue1Brown: But what is a GPT?](https://www.youtube.com/watch?v=wjZofJX0v4M) - Visual explanation

## Next Steps

Once you're comfortable with tokens, move to **Phase 2: Embeddings**:

```bash
cd ../2-embeddings
cat README.md
```

**Phase 2 Preview:** Learn how tokens are converted into dense vector representations that capture semantic meaning, enabling:
- Semantic search (find similar content)
- Text classification
- Recommendation systems
- Vector databases

---

**Need Help?**
- Review `intro.md` for detailed explanations
- Run examples multiple times with different inputs
- Try the interactive exercises in `token_exercises.py`
- Experiment with the [OpenAI Tokenizer Tool](https://platform.openai.com/tokenizer)
