# Example: Enhanced Lesson - Token Optimization

> **This is a template showing how to incorporate interactive learning elements**

## [Pre-Lecture Quiz](https://forms.example.com/pre-quiz)

Before starting, test your knowledge:
- What are tokens in LLMs?
- How does tokenization affect model performance?
- What is the relationship between tokens and cost?

---

## Learning Objectives

By the end of this lesson, you will be able to:
- [ ] Understand how different tokenization methods affect token count
- [ ] Optimize prompts to reduce token usage
- [ ] Calculate token costs for API calls
- [ ] Choose appropriate models based on token requirements
- [ ] Implement token tracking in applications

**Estimated Time:** 45 minutes

---

## Introduction

Tokens are the fundamental units that language models process. Understanding how to optimize token usage is crucial for:
- **Cost Efficiency:** Reducing API costs
- **Performance:** Faster processing with fewer tokens
- **Context Management:** Fitting more information in context windows
- **Quality:** Clearer, more effective prompts

---

## 1. Understanding Tokenization

### What is a Token?

A token can be:
- A word: `"hello"` = 1 token
- Part of a word: `"tokenization"` = 2-3 tokens depending on tokenizer
- Punctuation: `"!"` = 1 token
- Whitespace: Usually combined with adjacent tokens

```python
import tiktoken

# Initialize tokenizer for GPT-3.5
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Example texts
texts = [
    "Hello, world!",
    "Artificial Intelligence",
    "🌟 Emojis count too!",
    "verylongwordwithoutspaces",
]

# Count tokens
for text in texts:
    tokens = encoding.encode(text)
    print(f"Text: '{text}'")
    print(f"Tokens: {tokens}")
    print(f"Count: {len(tokens)}")
    print(f"Decoded: {[encoding.decode([t]) for t in tokens]}")
    print()
```

✅ **Knowledge Check:**
1. Why does "Artificial Intelligence" have more tokens than "AI"?
2. How many tokens would "don't" likely be?
3. What happens to emojis during tokenization?

<details>
<summary>Click to reveal answers</summary>

1. **Answer:** Longer words and multiple words increase token count. "Artificial Intelligence" = ~3 tokens vs "AI" = 1 token
2. **Answer:** Typically 2 tokens: "don" and "'t" (contractions are split)
3. **Answer:** Emojis are often 1-3 tokens each, depending on the emoji
</details>

---

## 2. Token Counting Tools

### Implementing a Token Counter

```python
from typing import List, Dict
import tiktoken

class TokenCounter:
    """Utility class for counting tokens across different models"""
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model
        self.encoding = tiktoken.encoding_for_model(model)
    
    def count_tokens(self, text: str) -> int:
        """Count tokens in a single text"""
        return len(self.encoding.encode(text))
    
    def count_message_tokens(self, messages: List[Dict]) -> int:
        """Count tokens in a message list (chat format)"""
        total_tokens = 0
        
        for message in messages:
            # Every message has format tokens
            total_tokens += 4  # <im_start>{role}\n{content}<im_end>\n
            
            for key, value in message.items():
                total_tokens += self.count_tokens(value)
        
        total_tokens += 2  # Assistant reply priming
        return total_tokens
    
    def estimate_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        """Estimate cost based on token count"""
        # Pricing as of 2024 (update as needed)
        prices = {
            "gpt-3.5-turbo": {"prompt": 0.0015, "completion": 0.002},  # per 1K tokens
            "gpt-4": {"prompt": 0.03, "completion": 0.06},
            "gpt-4-turbo": {"prompt": 0.01, "completion": 0.03},
        }
        
        if self.model not in prices:
            raise ValueError(f"Unknown model: {self.model}")
        
        prompt_cost = (prompt_tokens / 1000) * prices[self.model]["prompt"]
        completion_cost = (completion_tokens / 1000) * prices[self.model]["completion"]
        
        return prompt_cost + completion_cost

# Example usage
counter = TokenCounter("gpt-3.5-turbo")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is machine learning?"},
]

token_count = counter.count_message_tokens(messages)
print(f"Total tokens: {token_count}")
print(f"Estimated cost (with 100 token response): ${counter.estimate_cost(token_count, 100):.4f}")
```

### 🧪 Exercise: Token Counting Practice

**Task:** Count tokens in these examples and predict the cost

```python
# Example 1: Simple question
example1 = [
    {"role": "user", "content": "What is 2+2?"}
]

# Example 2: Detailed context
example2 = [
    {"role": "system", "content": "You are an expert data scientist..."},
    {"role": "user", "content": "Explain neural networks with examples..."},
]

# TODO: Calculate token count and cost for each
# Your code here
```

<details>
<summary>Click to see solution</summary>

```python
counter = TokenCounter("gpt-3.5-turbo")

# Example 1
tokens1 = counter.count_message_tokens(example1)
cost1 = counter.estimate_cost(tokens1, 10)  # Assuming short response
print(f"Example 1: {tokens1} tokens, ${cost1:.6f}")

# Example 2
tokens2 = counter.count_message_tokens(example2)
cost2 = counter.estimate_cost(tokens2, 200)  # Assuming detailed response
print(f"Example 2: {tokens2} tokens, ${cost2:.6f}")
```
</details>

---

## 3. Token Optimization Strategies

### Strategy 1: Remove Unnecessary Words

```python
def optimize_prompt(verbose_prompt: str) -> str:
    """Reduce token count while maintaining meaning"""
    
    # Before
    verbose = """
    I would like to kindly request that you please provide me with 
    a detailed explanation of the various ways in which one might 
    go about optimizing prompts in order to reduce the number of 
    tokens that are being used.
    """
    
    # After
    concise = "Explain prompt optimization techniques to reduce token usage."
    
    counter = TokenCounter()
    print(f"Verbose: {counter.count_tokens(verbose)} tokens")
    print(f"Concise: {counter.count_tokens(concise)} tokens")
    print(f"Reduction: {(1 - counter.count_tokens(concise)/counter.count_tokens(verbose)) * 100:.1f}%")
    
    return concise

optimize_prompt("")
```

✅ **Knowledge Check:**
1. What's a good token reduction target while maintaining quality?
2. Which words can usually be removed without losing meaning?
3. When should you NOT optimize for tokens?

---

### Strategy 2: Use System Messages Efficiently

```python
# ❌ Inefficient: Repeating instructions
messages_inefficient = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Be concise. What is AI?"},
    {"role": "assistant", "content": "AI is..."},
    {"role": "user", "content": "Be concise. What is ML?"},  # Repeated instruction
]

# ✅ Efficient: Single system message
messages_efficient = [
    {"role": "system", "content": "You are a helpful assistant. Always be concise."},
    {"role": "user", "content": "What is AI?"},
    {"role": "assistant", "content": "AI is..."},
    {"role": "user", "content": "What is ML?"},  # Instruction implied
]

# Compare
counter = TokenCounter()
print(f"Inefficient: {counter.count_message_tokens(messages_inefficient)} tokens")
print(f"Efficient: {counter.count_message_tokens(messages_efficient)} tokens")
```

---

### Strategy 3: Truncate Conversation History

```python
def truncate_conversation(messages: List[Dict], max_tokens: int = 2000) -> List[Dict]:
    """Keep conversation within token budget"""
    counter = TokenCounter()
    
    # Always keep system message
    system_message = [msg for msg in messages if msg["role"] == "system"]
    conversation = [msg for msg in messages if msg["role"] != "system"]
    
    # Start with most recent messages
    truncated = []
    current_tokens = counter.count_message_tokens(system_message)
    
    for message in reversed(conversation):
        message_tokens = counter.count_message_tokens([message])
        if current_tokens + message_tokens <= max_tokens:
            truncated.insert(0, message)
            current_tokens += message_tokens
        else:
            break
    
    return system_message + truncated

# Example: Long conversation
long_conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Question 1?"},
    {"role": "assistant", "content": "Answer 1..."},
    # ... 50 more exchanges ...
    {"role": "user", "content": "Current question?"},
]

optimized = truncate_conversation(long_conversation, max_tokens=500)
print(f"Original: {len(long_conversation)} messages")
print(f"Truncated: {len(optimized)} messages")
```

---

## 🚀 Challenge: Build a Token Budget Manager

**Difficulty:** Intermediate  
**Time:** 30-45 minutes

**Objective:** Create a class that manages token budgets for a chat application

**Requirements:**
1. Track token usage per user/session
2. Warn when approaching limits
3. Auto-truncate conversations to stay within budget
4. Calculate daily cost estimates
5. Support multiple models

**Starter Code:**
```python
class TokenBudgetManager:
    def __init__(self, daily_budget_tokens: int = 10000):
        self.daily_budget = daily_budget_tokens
        self.usage = {}  # {user_id: token_count}
    
    def add_usage(self, user_id: str, tokens: int):
        """Track token usage for a user"""
        # TODO: Implement
        pass
    
    def can_afford(self, user_id: str, estimated_tokens: int) -> bool:
        """Check if user has budget for request"""
        # TODO: Implement
        pass
    
    def get_remaining_budget(self, user_id: str) -> int:
        """Get remaining tokens for user"""
        # TODO: Implement
        pass

# TODO: Implement the class and test it
```

**Bonus Challenges (+5 points each):**
- [ ] Add cost tracking in dollars
- [ ] Implement rolling window (last 24 hours)
- [ ] Send alerts at 50%, 75%, 90% usage
- [ ] Support different budgets per user tier
- [ ] Generate usage reports

<details>
<summary>Hint 1: User tracking</summary>
Use a dictionary with user_id as key and cumulative token count as value.
</details>

<details>
<summary>Hint 2: Budget checking</summary>
Compare current usage + estimated tokens against daily budget.
</details>

---

## 💼 Real-World Application

### Case Study: ChatGPT Token Optimization

**Problem:** OpenAI needed to serve millions of users while keeping costs reasonable.

**Solution:**
- Efficient tokenization (tiktoken library)
- Smart context window management
- Model selection based on task complexity
- Response streaming to reduce perceived latency
- Token limits per user tier

**Results:**
- 90% cost reduction from GPT-3 to GPT-3.5-turbo
- 8x faster responses with same quality
- Scalable to millions of users

**Lessons:**
1. Token optimization directly impacts business viability
2. Model selection matters (GPT-4 vs GPT-3.5 cost difference)
3. User experience can be maintained while reducing tokens
4. Monitoring and analytics are crucial

**Resources:**
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [Best Practices Guide](https://help.openai.com/en/articles/...)
- [Cost Optimization Strategies](https://cookbook.openai.com/...)

---

## Summary

### Key Takeaways

1. **Tokens are the currency** of LLM APIs - optimize them like you'd optimize code
2. **Different models, different costs** - choose wisely based on requirements
3. **Measure before optimizing** - use tiktoken to count accurately
4. **Context management is crucial** - truncate conversations intelligently
5. **Balance quality and cost** - don't sacrifice UX for minor savings

### Token Optimization Checklist

- [ ] Count tokens before sending requests
- [ ] Remove unnecessary words and phrases
- [ ] Use efficient system messages
- [ ] Truncate long conversations
- [ ] Choose appropriate models for tasks
- [ ] Monitor and track usage
- [ ] Set budget alerts
- [ ] Implement caching where possible

---

## [Post-Lecture Quiz](https://forms.example.com/post-quiz)

Test your understanding:
1. How do you count tokens in a chat message?
2. What are 3 strategies to reduce token usage?
3. How does token count affect cost?

---

## Assignment

[Build a Token Optimization Tool](assignment.md)

**Due:** 1 week from today  
**Points:** 100  
**Rubric:** See assignment file

---

## Further Reading

### Essential Resources
- 📖 [OpenAI Tokenization Guide](https://platform.openai.com/docs/guides/tokenization)
- 🎥 [Token Optimization Best Practices](https://youtube.com/...)
- 💻 [tiktoken GitHub](https://github.com/openai/tiktoken)
- 📊 [Token Economics Calculator](https://gptforwork.com/tools/openai-chatgpt-api-pricing-calculator)

### Advanced Topics
- Token-aware truncation strategies
- Semantic compression techniques
- Multi-model routing
- Token caching patterns

---

## Next Lesson

**Coming Next:** [Embeddings and Semantic Search](../04-embeddings/01-intro.ipynb)

Preview what you'll learn:
- How embeddings represent meaning in vector space
- Building semantic search engines
- Vector similarity and distance metrics
- Applications: recommendations, search, RAG

---

**Questions? Discussion? Feedback?**

💬 [Join the discussion](https://github.com/yourrepo/discussions)  
🐛 [Report an issue](https://github.com/yourrepo/issues)  
⭐ [Star this repo](https://github.com/yourrepo) if you found it helpful!

---

**Lesson Stats:**
- **Created:** December 2024
- **Updated:** December 15, 2024
- **Difficulty:** ⭐⭐ Intermediate
- **Completion Time:** ~45 minutes
- **Prerequisites:** Phase 0 (Python), Phase 1 (Data Science basics)
