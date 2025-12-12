# Phase 10: Prompt Engineering

## 🎯 Overview

Master the art and science of crafting effective prompts for Large Language Models. Learn systematic techniques to get better, more reliable, and more creative outputs from LLMs.

**Prerequisites:**
- ✅ Basic LLM understanding
- ✅ RAG systems (Phase 7)
- ✅ Python programming

**Time:** 2-3 weeks | 40-60 hours  
**Outcome:** Build production-grade prompting systems with advanced techniques

---

## 📚 What You'll Learn

### Core Prompting Techniques
- [ ] Zero-shot, one-shot, and few-shot prompting
- [ ] Chain-of-Thought (CoT) reasoning
- [ ] ReAct (Reasoning + Acting) pattern
- [ ] Tree-of-Thoughts for complex reasoning
- [ ] Self-consistency and multiple sampling
- [ ] System prompts and role engineering

### Advanced Techniques
- [ ] Prompt templates and variables
- [ ] Dynamic few-shot examples
- [ ] Prompt optimization and iteration
- [ ] Context window management
- [ ] Token optimization strategies
- [ ] Fallback and error handling

### Specialized Applications
- [ ] Code generation prompts
- [ ] Data extraction and formatting
- [ ] Creative writing and storytelling
- [ ] Analysis and reasoning tasks
- [ ] Translation and summarization
- [ ] Multi-turn conversations

---

## 🗂️ Module Structure

```
10-prompt-engineering/
├── 00_START_HERE.ipynb              # Overview and quick wins
├── 01_basic_prompting.ipynb         # Zero/one/few-shot
├── 02_chain_of_thought.ipynb        # CoT reasoning
├── 03_react_prompting.ipynb         # ReAct pattern
├── 04_tree_of_thoughts.ipynb        # Complex reasoning
├── 05_prompt_templates.ipynb        # Template systems
├── 06_optimization.ipynb            # Testing and iteration
├── 07_advanced_techniques.ipynb     # Self-consistency, etc.
├── 08_production_patterns.ipynb     # Real-world patterns
├── projects/
│   ├── code_generator.py            # AI coding assistant
│   ├── data_extractor.py            # Structured extraction
│   ├── creative_writer.py           # Story generation
│   └── research_assistant.py        # Analysis tasks
├── examples/
│   ├── good_prompts/                # Effective examples
│   └── bad_prompts/                 # What to avoid
└── templates/
    ├── code_generation.txt
    ├── data_extraction.txt
    ├── analysis.txt
    └── creative.txt
```

---

## 🚀 Quick Start

### The Anatomy of a Good Prompt

```python
# ❌ Bad Prompt
"Write code to sort a list"

# ✅ Good Prompt
"""You are an expert Python developer.

Task: Write a function to sort a list of dictionaries by a specific key.

Requirements:
- Use type hints
- Add docstring
- Handle edge cases (empty list, missing keys)
- Include usage example

Return only the code with comments."""

# 🚀 Even Better: Few-Shot Prompt
"""You are an expert Python developer. Here are examples of my coding style:

Example 1:
def calculate_sum(numbers: list[int]) -> int:
    '''Calculate sum of integers.
    
    Args:
        numbers: List of integers
        
    Returns:
        Sum of all numbers
    '''
    return sum(numbers)

Example 2:
def filter_even(numbers: list[int]) -> list[int]:
    '''Filter even numbers from list.
    
    Args:
        numbers: List of integers
        
    Returns:
        List containing only even numbers
    '''
    return [n for n in numbers if n % 2 == 0]

Now write a function to sort a list of dictionaries by a specific key, following the same style.
"""
```

---

## 📋 Learning Path

### Week 1: Fundamentals
- [ ] Complete `00_START_HERE.ipynb`
- [ ] Master basic prompting in `01_basic_prompting.ipynb`
- [ ] Learn CoT in `02_chain_of_thought.ipynb`
- [ ] **Project:** Build a math problem solver

### Week 2: Advanced Techniques
- [ ] Study ReAct in `03_react_prompting.ipynb`
- [ ] Explore Tree-of-Thoughts in `04_tree_of_thoughts.ipynb`
- [ ] Build templates in `05_prompt_templates.ipynb`
- [ ] **Project:** Create a research assistant

### Week 3: Production & Optimization
- [ ] Learn optimization in `06_optimization.ipynb`
- [ ] Advanced patterns in `07_advanced_techniques.ipynb`
- [ ] Production patterns in `08_production_patterns.ipynb`
- [ ] **Capstone:** Build a multi-purpose AI assistant

---

## 🛠️ Technologies You'll Use

**LLM Providers:**
- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude 3)
- Google (Gemini)
- Local models (via Ollama)

**Frameworks:**
- LangChain (prompt templates)
- Guidance (structured prompting)
- LMQL (query language for LLMs)
- DSPy (declarative prompting)

**Tools:**
- OpenAI Playground
- Anthropic Console
- Prompt flow
- LangSmith (evaluation)

---

## 📊 Key Concepts Explained

### Chain-of-Thought (CoT)
Encourages step-by-step reasoning by adding "Let's think step by step" or providing reasoning examples.

```python
# Without CoT
Q: "A bat and ball cost $1.10. The bat costs $1 more than the ball. How much does the ball cost?"
A: "$0.10"  # ❌ Wrong!

# With CoT
Q: "A bat and ball cost $1.10. The bat costs $1 more than the ball. How much does the ball cost?
Let's think step by step:"
A: """
Step 1: Let's call the ball's cost x
Step 2: Then the bat costs x + $1
Step 3: Together: x + (x + $1) = $1.10
Step 4: 2x + $1 = $1.10
Step 5: 2x = $0.10
Step 6: x = $0.05
The ball costs $0.05."""  # ✅ Correct!
```

### ReAct (Reasoning + Acting)
Combines reasoning with actions/tool use in an iterative loop.

```
Thought: I need to find the current population of Tokyo
Action: search["Tokyo population 2024"]
Observation: 14 million (metropolitan area: 37 million)
Thought: Now I have the answer
Answer: Tokyo has approximately 14 million people in the city proper...
```

### Tree-of-Thoughts
Explores multiple reasoning paths and self-evaluates to find the best solution.

```
Problem → [Path A, Path B, Path C]
Each path → Evaluate quality → Choose best → Continue
```

---

## 🎯 Projects

### 1. AI Code Generator
Build a system that generates production-ready code from natural language descriptions.

**Skills:** Few-shot learning, code templates, validation

### 2. Data Extractor
Extract structured data from unstructured text (emails, documents, web pages).

**Skills:** Output formatting, JSON mode, error handling

### 3. Research Assistant
Analyze documents, answer questions, and generate insights with citations.

**Skills:** CoT, ReAct, source attribution

### 4. Creative Writer
Generate stories, articles, or marketing copy with specific style and tone.

**Skills:** Style control, creative prompting, consistency

---

## 📈 Evaluation & Testing

### Metrics for Prompt Quality
- **Accuracy:** Correct answers/total attempts
- **Consistency:** Same prompt → similar outputs
- **Relevance:** Output matches intent
- **Efficiency:** Tokens used per task
- **Robustness:** Handles edge cases

### Testing Framework
```python
def test_prompt(prompt_template, test_cases):
    results = []
    for case in test_cases:
        prompt = prompt_template.format(**case)
        output = llm.generate(prompt)
        score = evaluate(output, case['expected'])
        results.append(score)
    return sum(results) / len(results)
```

---

## 💡 Best Practices

### DO ✅
- Be specific and detailed
- Provide examples (few-shot)
- Specify output format
- Use delimiters (```, ---, ###)
- Test and iterate
- Add constraints and requirements
- Use system prompts for role/behavior

### DON'T ❌
- Be vague or ambiguous
- Assume LLM has real-time data
- Rely on single-shot for critical tasks
- Ignore token limits
- Skip validation of outputs
- Use overly complex prompts
- Forget about cost optimization

### The Prompt Engineering Workflow
1. **Define** the task clearly
2. **Draft** initial prompt
3. **Test** with examples
4. **Analyze** failures
5. **Iterate** and improve
6. **Template** for reuse
7. **Monitor** in production

---

## 🔗 Resources

### Courses & Guides
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [DeepLearning.AI - ChatGPT Prompt Engineering](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### Papers
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)
- [ReAct: Reasoning and Acting](https://arxiv.org/abs/2210.03629)
- [Tree of Thoughts](https://arxiv.org/abs/2305.10601)
- [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)

### Tools
- [OpenAI Playground](https://platform.openai.com/playground)
- [LangChain Hub](https://smith.langchain.com/hub)
- [Anthropic Console](https://console.anthropic.com/)
- [PromptPerfect](https://promptperfect.jina.ai/)

### Communities
- r/PromptEngineering
- LangChain Discord
- OpenAI Developer Forum

---

## ✅ Completion Checklist

Before moving forward, you should be able to:

- [ ] Write effective zero, one, and few-shot prompts
- [ ] Use Chain-of-Thought for complex reasoning
- [ ] Implement ReAct pattern for tool use
- [ ] Create reusable prompt templates
- [ ] Optimize prompts for cost and quality
- [ ] Test and evaluate prompt performance
- [ ] Handle edge cases and errors
- [ ] Choose the right technique for each task
- [ ] Build production-ready prompting systems
- [ ] Debug and improve failing prompts

---

## 🎓 What's Next?

**Phase 11: LLM Fine-tuning** →
- When prompting isn't enough
- Custom model training
- LoRA and efficient fine-tuning

**Phase 13: Local LLMs** →
- Run models locally
- Privacy and control
- Cost optimization

**Phase 9: AI Agents** →
- Combine prompting with autonomous behavior
- Multi-agent systems
- Production agent frameworks

---

**Ready to master prompt engineering?** → Start with `00_START_HERE.ipynb`

**Questions?** → Check the examples/ folder for patterns

**🎯 Remember: Great prompts are 80% of LLM success!**
