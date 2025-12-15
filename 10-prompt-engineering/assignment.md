# Assignment: Build an Advanced Prompt Engineering System

## 🎯 Objective

Build a comprehensive prompt engineering system that demonstrates mastery of various prompting techniques. You'll create a multi-purpose AI assistant that adapts its prompting strategy based on the task type.

**Estimated Time:** 5-7 hours  
**Difficulty:** ⭐⭐⭐ Intermediate  
**Due Date:** 2 weeks from assignment

---

## 📋 Requirements

### Part 1: Prompting Technique Library (30 points)

Implement at least 6 different prompting techniques:

- [ ] **Zero-shot:** Direct task execution without examples
- [ ] **Few-shot:** Learning from 3-5 examples
- [ ] **Chain-of-Thought (CoT):** Step-by-step reasoning
- [ ] **ReAct:** Reasoning + Acting with tools
- [ ] **Self-Consistency:** Multiple reasoning paths with voting
- [ ] **Tree-of-Thoughts:** Exploring multiple solution branches

**Implementation Structure:**
```python
class PromptEngine:
    def __init__(self, api_key, model="gpt-4"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.techniques = {}
    
    def zero_shot(self, task, context=None):
        """Execute task with zero-shot prompting."""
        pass
    
    def few_shot(self, task, examples, context=None):
        """Execute task with few-shot examples."""
        pass
    
    def chain_of_thought(self, task, context=None):
        """Use CoT prompting for complex reasoning."""
        pass
    
    def react(self, task, tools, max_iterations=5):
        """ReAct: Reasoning and Acting with tools."""
        pass
    
    def self_consistency(self, task, n_samples=5):
        """Generate multiple solutions and vote."""
        pass
    
    def tree_of_thoughts(self, task, depth=3, breadth=3):
        """Explore solution tree."""
        pass
```

### Part 2: Adaptive Strategy Selector (25 points)

Create a system that automatically selects the best prompting strategy:

- [ ] Classify task type (simple Q&A, reasoning, creative, analytical)
- [ ] Choose appropriate prompting technique based on task
- [ ] Adjust parameters (temperature, tokens) per technique
- [ ] Track token usage and costs per technique

**Strategy Selection Logic:**
```python
class StrategySelector:
    def classify_task(self, task):
        """
        Classify task into categories:
        - simple: Direct Q&A, facts
        - reasoning: Math, logic, multi-step
        - creative: Writing, brainstorming
        - analytical: Data analysis, summarization
        - tool_use: Requires external APIs/tools
        """
        pass
    
    def select_strategy(self, task):
        """Select best prompting technique for task."""
        task_type = self.classify_task(task)
        
        strategy_map = {
            "simple": "zero_shot",
            "reasoning": "chain_of_thought",
            "creative": "few_shot",
            "analytical": "tree_of_thoughts",
            "tool_use": "react"
        }
        
        return strategy_map.get(task_type, "zero_shot")
```

### Part 3: Real-World Applications (25 points)

Build 4 practical applications using different techniques:

#### App 1: Research Assistant (CoT + Tools)
- [ ] Takes a research question
- [ ] Breaks it into sub-questions
- [ ] Searches web for each sub-question
- [ ] Synthesizes comprehensive answer with citations

#### App 2: Code Reviewer (Few-shot)
- [ ] Analyzes code for bugs, style, performance
- [ ] Uses examples of good/bad code patterns
- [ ] Provides specific, actionable feedback
- [ ] Suggests improvements

#### App 3: Creative Writing Coach (Self-Consistency)
- [ ] Generates multiple story plot variations
- [ ] Gets feedback on each
- [ ] Combines best elements
- [ ] Produces final polished version

#### App 4: Data Analyst (Tree-of-Thoughts)
- [ ] Takes dataset description and question
- [ ] Explores multiple analysis approaches
- [ ] Evaluates each approach
- [ ] Presents best insights

### Part 4: Optimization & Analysis (20 points)

Analyze and optimize your system:

- [ ] **Token Usage:** Track tokens per technique, identify savings opportunities
- [ ] **Cost Analysis:** Calculate cost per task type
- [ ] **Quality Metrics:** Compare output quality across techniques
- [ ] **Speed Benchmarks:** Measure latency for each technique
- [ ] **A/B Testing:** Compare techniques on same tasks

**Required Report:**
- Table comparing all 6 techniques on:
  - Average tokens used
  - Average cost
  - Subjective quality rating (1-5)
  - Average latency
  - Best use cases

---

## 📊 Grading Rubric

| Criteria | Exemplary (A) | Proficient (B) | Adequate (C) | Needs Work (D/F) |
|----------|--------------|----------------|--------------|------------------|
| **Techniques** (30pts) | 6+ techniques, flawless implementation | 5-6 techniques, minor issues | 4-5 techniques, some bugs | <4 techniques or broken |
| **Strategy Selector** (25pts) | Smart auto-selection, handles edge cases | Good selection logic | Basic selection | Poor or no selection |
| **Applications** (25pts) | 4 polished apps, excellent UX | 3-4 good apps | 2-3 basic apps | <2 or poor quality |
| **Analysis** (20pts) | Deep insights, comprehensive data | Good analysis | Basic metrics | Minimal analysis |

---

## 🌟 Bonus Challenges (+10 points each, max +30)

### Bonus 1: Prompt Optimization System (+10)
- [ ] Automatically refine prompts based on output quality
- [ ] Use LLM to critique and improve prompts
- [ ] Show before/after prompt examples with quality improvements

### Bonus 2: Cost Control Dashboard (+10)
- [ ] Real-time token tracking
- [ ] Budget alerts when approaching limits
- [ ] Cost prediction for new tasks
- [ ] Recommendations for cheaper alternatives

### Bonus 3: Multi-Modal Prompting (+10)
- [ ] Integrate image understanding (GPT-4 Vision)
- [ ] Process images + text together
- [ ] Build visual Q&A system
- [ ] Image-to-text and text-to-image workflows

### Bonus 4: Evaluation Framework (+10)
- [ ] Automated quality scoring for outputs
- [ ] Human evaluation interface
- [ ] Inter-rater reliability metrics
- [ ] Continuous improvement tracking

---

## 📦 Submission Requirements

### Repository Structure
```
your-name-prompt-engineering/
├── README.md                    # Setup and usage
├── requirements.txt             # Dependencies
├── src/
│   ├── prompt_engine.py         # Core prompting techniques
│   ├── strategy_selector.py    # Adaptive selection
│   ├── apps/
│   │   ├── research_assistant.py
│   │   ├── code_reviewer.py
│   │   ├── writing_coach.py
│   │   └── data_analyst.py
│   └── utils/
│       ├── token_tracker.py
│       └── cost_calculator.py
├── notebooks/
│   ├── technique_comparison.ipynb
│   ├── application_demos.ipynb
│   └── optimization_analysis.ipynb
├── tests/
│   └── test_techniques.py       # Unit tests
├── data/
│   ├── example_tasks.json       # Test tasks
│   └── results/                 # Experiment results
└── REPORT.md                    # Analysis report
```

### What to Include

1. **Working Code:**
   - All 6 prompting techniques
   - Strategy selector
   - 4 practical applications
   - Tests demonstrating functionality

2. **Analysis Notebook:**
   - Technique comparisons
   - Cost/performance analysis
   - Quality evaluation
   - Optimization recommendations

3. **Report (REPORT.md):**
   - Methodology explanation
   - Results tables and charts
   - Insights and findings
   - Lessons learned
   - Future improvements

4. **Demo:**
   - Video (5 min) or Gradio app showing:
     - Each technique in action
     - Strategy selector working
     - At least 2 applications
     - Cost tracking dashboard

---

## 💡 Example Implementations

<details>
<summary>Example: Chain-of-Thought Implementation</summary>

```python
def chain_of_thought(self, task, context=None):
    """
    Implements Chain-of-Thought prompting.
    Encourages step-by-step reasoning.
    """
    prompt = f"""
    Let's solve this step by step.
    
    Task: {task}
    {f"Context: {context}" if context else ""}
    
    Think through this carefully:
    1) First, let's identify what we know
    2) Then, what steps do we need to take?
    3) Finally, what's the answer?
    
    Please show your reasoning for each step.
    """
    
    response = self.client.chat.completions.create(
        model=self.model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3  # Lower temp for reasoning tasks
    )
    
    return response.choices[0].message.content
```
</details>

<details>
<summary>Example: ReAct with Web Search Tool</summary>

```python
def react(self, task, tools, max_iterations=5):
    """
    ReAct: Reasoning and Acting.
    Alternates between reasoning and tool use.
    """
    messages = [{
        "role": "system",
        "content": """You are a helpful assistant that uses tools to solve problems.
        
        Available tools:
        - web_search(query): Search the web
        - calculate(expression): Calculate math expressions
        
        Use this format:
        Thought: [your reasoning]
        Action: tool_name(arguments)
        Observation: [tool result]
        ... (repeat as needed)
        Answer: [final answer]
        """
    }]
    
    messages.append({"role": "user", "content": task})
    
    for i in range(max_iterations):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        
        content = response.choices[0].message.content
        
        # Check if answer provided
        if "Answer:" in content:
            return content.split("Answer:")[1].strip()
        
        # Extract and execute action
        if "Action:" in content:
            action_line = content.split("Action:")[1].split("\n")[0]
            result = self._execute_tool(action_line, tools)
            messages.append({
                "role": "assistant",
                "content": content
            })
            messages.append({
                "role": "user",
                "content": f"Observation: {result}"
            })
        else:
            break
    
    return "Failed to reach conclusion"
```
</details>

---

## 📚 Resources

### Essential Reading
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [Chain-of-Thought Paper](https://arxiv.org/abs/2201.11903)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

### Tools & Libraries
- [LangChain](https://python.langchain.com/) - Prompt management
- [Guidance](https://github.com/guidance-ai/guidance) - Structured generation
- [PromptTools](https://github.com/hegelai/prompttools) - Testing & evaluation

### Videos
- [Prompt Engineering Course (Andrew Ng)](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- [Advanced Prompting Techniques](https://www.youtube.com/watch?v=ahnGLM-RC1Y)

---

## 🎓 Learning Objectives

After completing this assignment, you will:

- ✅ Master 6+ advanced prompting techniques
- ✅ Build production-ready prompt systems
- ✅ Optimize for cost and performance
- ✅ Evaluate prompt effectiveness systematically
- ✅ Create adaptive AI applications

---

## 💬 Support

- **Office Hours:** Mondays 3-5 PM, Wednesdays 2-4 PM
- **Discussion:** [GitHub Discussions](https://github.com/zero-to-ai/discussions)
- **Email:** instructor@zero-to-ai.com

---

**Happy prompting! 🎨**

Remember: Great prompts are iterative. Test, measure, and refine!
