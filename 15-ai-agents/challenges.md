# Phase 14: AI Agents - Challenges

Test your understanding of AI agents with these hands-on challenges! Each challenge builds on the concepts from the notebooks.

---

## 🎯 Challenge 1: Calculator Agent

**Difficulty:** ⭐⭐ (Beginner)  
**Time:** 30-45 minutes

### Objective
Build a calculator agent that can handle complex math expressions using function calling.

### Requirements
Create an agent with these tools:
- `add(a, b)` - Addition
- `subtract(a, b)` - Subtraction
- `multiply(a, b)` - Multiplication
- `divide(a, b)` - Division
- `power(base, exponent)` - Exponentiation
- `sqrt(n)` - Square root

### Test Cases
```python
queries = [
    "What is 15 plus 27?",
    "Calculate 144 divided by 12",
    "What's the square root of 256?",
    "What is 2 to the power of 10?",
    "Calculate (15 + 27) * 3",  # Multi-step
]
```

### Success Criteria
- ✅ Handles all basic operations
- ✅ Can chain multiple operations
- ✅ Proper error handling (divide by zero, negative sqrt)
- ✅ Returns clear, formatted answers

### Hints
- Start with simple operations first
- Test each tool individually before integration
- Handle edge cases (division by zero, etc.)

---

## 🎯 Challenge 2: Weather Agent with API

**Difficulty:** ⭐⭐⭐ (Intermediate)  
**Time:** 1-2 hours

### Objective
Build an agent that fetches real weather data and answers questions about it.

### Requirements
Create tools for:
- `get_current_weather(city)` - Current conditions
- `get_forecast(city, days)` - Future forecast
- `compare_weather(city1, city2)` - Compare two locations
- `get_weather_alerts(city)` - Severe weather warnings

### API Options
- OpenWeatherMap (free tier)
- Weather API
- MeteoStat

### Test Cases
```python
queries = [
    "What's the weather like in London today?",
    "Will it rain in Seattle this week?",
    "Is it warmer in Miami or Los Angeles right now?",
    "Any weather alerts for San Francisco?",
    "Should I bring an umbrella in New York tomorrow?",
]
```

### Success Criteria
- ✅ Makes real API calls
- ✅ Handles API errors gracefully
- ✅ Caches results (avoid redundant API calls)
- ✅ Provides natural language responses
- ✅ Includes relevant details (temp, humidity, conditions)

### Bonus
- Add temperature unit conversion (C ↔ F)
- Historical weather data
- Weather recommendations (clothing, activities)

---

## 🎯 Challenge 3: Multi-Tool Research Agent

**Difficulty:** ⭐⭐⭐ (Intermediate)  
**Time:** 2-3 hours

### Objective
Build an agent that can research topics by combining multiple information sources.

### Requirements
Implement these tools:
- `wikipedia_search(topic)` - Search Wikipedia
- `web_search(query)` - DuckDuckGo or similar
- `arxiv_search(topic)` - Academic papers
- `summarize_text(text, max_words)` - Summarization

### Test Cases
```python
queries = [
    "What is machine learning?",
    "Summarize the latest research on quantum computing",
    "Explain the history of artificial intelligence",
    "What are the applications of neural networks?",
]
```

### Success Criteria
- ✅ Searches multiple sources
- ✅ Synthesizes information from different sources
- ✅ Cites sources properly
- ✅ Handles "no results found" gracefully
- ✅ Summarizes long content effectively

### Bonus
- Fact-checking across sources
- Include images/diagrams
- Generate bibliography

### Libraries to Use
```python
import wikipedia
import requests
from duckduckgo_search import DDGS
import arxiv
```

---

## 🎯 Challenge 4: Code Review Agent

**Difficulty:** ⭐⭐⭐⭐ (Advanced)  
**Time:** 3-4 hours

### Objective
Create an agent that reviews Python code and provides feedback.

### Requirements
Build tools for:
- `check_syntax(code)` - Syntax validation
- `check_style(code)` - PEP 8 compliance
- `find_bugs(code)` - Static analysis
- `suggest_improvements(code)` - Optimization tips
- `calculate_complexity(code)` - Cyclomatic complexity

### Test Cases
```python
# Test with various code samples
buggy_code = """
def divide(a, b):
    return a / b  # No zero check!
"""

inefficient_code = """
def find_max(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] > numbers[j]:
                ...
"""

messy_code = """
def x(a,b,c):
 if a>b:
  if b>c:
   return a
  else:return c
"""
```

### Success Criteria
- ✅ Identifies syntax errors
- ✅ Detects common bugs (division by zero, off-by-one, etc.)
- ✅ Suggests style improvements
- ✅ Provides specific line numbers
- ✅ Explains WHY each issue matters
- ✅ Prioritizes issues (critical → minor)

### Libraries to Use
```python
import ast  # Parse Python code
import pylint
from radon.complexity import cc_visit  # Complexity
from autopep8 import fix_code  # Style fixes
```

### Bonus
- Suggest specific fixes (not just identify issues)
- Security vulnerability detection
- Performance profiling
- Generate unit tests for the code

---

## 🎯 Challenge 5: Memory-Enhanced Chatbot

**Difficulty:** ⭐⭐⭐⭐ (Advanced)  
**Time:** 3-4 hours

### Objective
Build a chatbot that remembers previous conversations and user preferences.

### Requirements
Implement memory systems:
- **Short-term memory:** Last 10 messages
- **Long-term memory:** User facts stored in vector DB
- **Summarization:** Compress old conversations

Tools needed:
- `remember_fact(fact)` - Store user information
- `recall_facts(query)` - Retrieve relevant facts
- `summarize_conversation()` - Compress history
- `get_user_profile()` - Return known preferences

### Test Scenario
```python
# Session 1
User: "Hi, my name is Alice"
Bot: "Nice to meet you, Alice!"

User: "I love pizza and hiking"
Bot: "Great! I'll remember that you enjoy pizza and hiking."

# Session 2 (new session, should remember)
User: "What do you know about me?"
Bot: "Your name is Alice, and you enjoy pizza and hiking."

User: "Recommend a weekend activity"
Bot: "Based on your interest in hiking, how about exploring a nearby trail?"
```

### Success Criteria
- ✅ Stores facts from conversation
- ✅ Retrieves relevant facts when needed
- ✅ Persists between sessions (file/DB storage)
- ✅ Handles contradictions ("I don't like pizza anymore")
- ✅ Summarizes when context gets too long

### Implementation Options

**Option A: Simple JSON storage**
```python
import json

class SimpleMemory:
    def __init__(self):
        self.facts = {}
    
    def remember(self, key, value):
        self.facts[key] = value
        self.save()
    
    def save(self):
        with open('memory.json', 'w') as f:
            json.dump(self.facts, f)
    
    def load(self):
        with open('memory.json', 'r') as f:
            self.facts = json.load(f)
```

**Option B: Vector database**
```python
from sentence_transformers import SentenceTransformer
import chromadb

class VectorMemory:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("memories")
    
    def remember(self, fact):
        embedding = self.model.encode([fact])[0]
        self.collection.add(
            embeddings=[embedding.tolist()],
            documents=[fact],
            ids=[str(time.time())]
        )
    
    def recall(self, query, n=5):
        query_embedding = self.model.encode([query])[0]
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=n
        )
        return results['documents'][0]
```

### Bonus
- Semantic search over memories
- Automatic fact extraction from conversation
- Memory importance scoring (forget trivial facts)
- Export conversation history

---

## 🎯 Challenge 6: Multi-Agent System

**Difficulty:** ⭐⭐⭐⭐⭐ (Expert)  
**Time:** 5-8 hours

### Objective
Build a system where multiple specialized agents collaborate to solve complex tasks.

### System Design
Create 3 specialized agents:
1. **Planner Agent** - Breaks down tasks into steps
2. **Executor Agent** - Performs individual steps
3. **Reviewer Agent** - Checks quality and accuracy

### Example Task Flow
```
User: "Research climate change and write a 500-word summary"

Planner:
  Step 1: Search for climate change information
  Step 2: Extract key facts
  Step 3: Write summary
  Step 4: Review and edit

Executor (Step 1):
  [Searches web, Wikipedia, academic sources]
  [Returns: List of facts]

Executor (Step 3):
  [Writes draft summary]

Reviewer (Step 4):
  Issues found:
  - Summary is only 350 words (need 500)
  - Missing citation for statistic
  Action: Request revision

Executor (Revision):
  [Expands summary to 500 words, adds citation]

Reviewer:
  ✅ All requirements met
  Final output ready
```

### Requirements
- ✅ Clear separation of responsibilities
- ✅ Inter-agent communication protocol
- ✅ Shared memory/context
- ✅ Error handling and recovery
- ✅ Feedback loops (reviewer → executor)

### Test Cases
```python
tasks = [
    "Research and summarize quantum computing in 500 words",
    "Find the best Italian restaurant in Seattle and make a reservation",
    "Debug this Python code and write test cases for it",
    "Plan a 3-day trip to Tokyo with budget under $2000",
]
```

### Success Criteria
- ✅ Agents collaborate effectively
- ✅ Work is distributed appropriately
- ✅ Handles complex multi-step tasks
- ✅ Quality control via reviewer
- ✅ Graceful failure recovery

### Architecture Example
```python
class MultiAgentSystem:
    def __init__(self):
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.reviewer = ReviewerAgent()
        self.shared_memory = SharedMemory()
    
    def execute_task(self, task):
        # 1. Planner creates plan
        plan = self.planner.create_plan(task)
        self.shared_memory.store_plan(plan)
        
        # 2. Executor performs steps
        for step in plan.steps:
            result = self.executor.execute(step)
            self.shared_memory.store_result(step.id, result)
            
            # 3. Reviewer checks quality
            review = self.reviewer.review(step, result)
            
            if not review.approved:
                # Retry with feedback
                result = self.executor.execute(
                    step, 
                    feedback=review.feedback
                )
        
        # 4. Final compilation
        return self.compile_results()
```

### Bonus Challenges
- Add a 4th "Coordinator" agent to manage others
- Implement voting mechanism for disagreements
- Parallel execution of independent steps
- Real-time progress tracking UI
- Agent specialization (ResearchAgent, WritingAgent, etc.)

---

## 🎯 Challenge 7: Autonomous Task Scheduler

**Difficulty:** ⭐⭐⭐⭐⭐ (Expert)  
**Time:** 6-10 hours

### Objective
Build an agent that autonomously manages and executes scheduled tasks.

### Features Required
1. **Task Management**
   - Add/remove/update tasks
   - Priority levels (high, medium, low)
   - Dependencies between tasks
   - Recurring tasks (daily, weekly, etc.)

2. **Intelligent Scheduling**
   - Optimize task order based on:
     - Dependencies
     - Deadlines
     - Estimated duration
     - Resource availability
   
3. **Autonomous Execution**
   - Run tasks automatically at scheduled times
   - Retry failed tasks
   - Send notifications
   - Generate reports

### Example Usage
```python
scheduler = TaskSchedulerAgent()

# Add tasks
scheduler.add_task(
    name="Daily Backup",
    action="run_backup",
    schedule="daily at 2am",
    priority="high"
)

scheduler.add_task(
    name="Generate Weekly Report",
    action="create_report",
    schedule="every Monday at 9am",
    dependencies=["collect_data", "analyze_data"],
    priority="medium"
)

# Agent runs autonomously
scheduler.start()
```

### Tools to Implement
- `add_task(task_config)` - Create new task
- `run_task(task_id)` - Execute specific task
- `check_dependencies(task_id)` - Verify prerequisites
- `estimate_duration(task_id)` - Predict runtime
- `send_notification(message, channel)` - Alerts
- `generate_schedule()` - Optimize task order

### Success Criteria
- ✅ Handles task dependencies correctly
- ✅ Executes tasks at scheduled times
- ✅ Retries with exponential backoff
- ✅ Sends success/failure notifications
- ✅ Generates execution reports
- ✅ Optimizes schedule to meet deadlines
- ✅ Handles concurrent task execution

### Advanced Features
- Conflict detection (two tasks need same resource)
- Dynamic rescheduling when tasks run long
- Learning from past executions (improve estimates)
- Resource allocation (CPU, memory, API quotas)

### Libraries to Use
```python
import schedule
import asyncio
from apscheduler.schedulers.background import BackgroundScheduler
import networkx as nx  # For dependency graphs
```

### Bonus
- Web UI for managing tasks
- Integration with calendar APIs
- ML-based duration estimation
- Multi-agent delegation (distribute work)

---

## 🎯 Challenge 8: Real-Time Monitoring Agent

**Difficulty:** ⭐⭐⭐⭐ (Advanced)  
**Time:** 4-5 hours

### Objective
Build an agent that monitors systems/services and takes action when issues are detected.

### What to Monitor
Choose ONE or build multiple:
- **Website uptime** - Check if sites are accessible
- **API health** - Monitor response times and errors
- **System resources** - CPU, memory, disk usage
- **Log files** - Detect errors/warnings
- **Social media** - Track mentions or hashtags

### Required Tools
- `check_health(target)` - Perform health check
- `analyze_metrics(data)` - Identify anomalies
- `send_alert(severity, message)` - Notify on issues
- `take_action(issue)` - Auto-remediation
- `generate_report()` - Status summary

### Example: Website Monitor
```python
monitor = MonitoringAgent(
    targets=["https://example.com", "https://api.example.com"],
    check_interval=60  # seconds
)

monitor.start()

# When issue detected:
# 1. Check health → Site down
# 2. Analyze → 503 error, server overload
# 3. Alert → Send Slack notification
# 4. Action → Restart server, scale resources
# 5. Report → Log incident details
```

### Success Criteria
- ✅ Continuous monitoring (background process)
- ✅ Configurable check intervals
- ✅ Anomaly detection (what's unusual?)
- ✅ Multi-channel alerts (email, Slack, SMS)
- ✅ Auto-remediation for common issues
- ✅ Detailed incident reports

### Alert Levels
```python
class AlertLevel:
    INFO = "info"        # FYI, no action needed
    WARNING = "warning"  # Attention required
    ERROR = "error"      # Immediate action needed
    CRITICAL = "critical" # System down, escalate
```

### Auto-Remediation Examples
- Website down → Restart web server
- API slow → Scale up instances
- Disk full → Clean temp files
- Memory leak → Restart process

### Bonus
- Anomaly detection with ML
- Predictive alerts (issue likely soon)
- Dashboard visualization
- Integration with PagerDuty/OpsGenie
- Historical trend analysis

---

## 🏆 Completion Checklist

Track your progress:

- [ ] Challenge 1: Calculator Agent ⭐⭐
- [ ] Challenge 2: Weather Agent ⭐⭐⭐
- [ ] Challenge 3: Research Agent ⭐⭐⭐
- [ ] Challenge 4: Code Review Agent ⭐⭐⭐⭐
- [ ] Challenge 5: Memory-Enhanced Chatbot ⭐⭐⭐⭐
- [ ] Challenge 6: Multi-Agent System ⭐⭐⭐⭐⭐
- [ ] Challenge 7: Task Scheduler ⭐⭐⭐⭐⭐
- [ ] Challenge 8: Monitoring Agent ⭐⭐⭐⭐

---

## 💡 General Tips

### Starting Out
1. **Read the requirements carefully** - Understand what's needed
2. **Plan before coding** - Sketch out tool designs
3. **Start simple** - Get basic version working first
4. **Test incrementally** - Don't build everything then test

### Tool Design Best Practices
```python
# ✅ GOOD: Focused, single responsibility
def search_web(query: str, num_results: int = 5) -> list:
    """Search web and return results"""
    pass

# ❌ BAD: Too many responsibilities
def do_research(topic, summarize=True, translate=False, save_file=True):
    """Does too much, hard to test and debug"""
    pass
```

### Error Handling
```python
# Always validate inputs
def divide(a: float, b: float) -> float:
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected number, got {type(a)}")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Graceful degradation
def fetch_weather(city: str) -> dict:
    try:
        response = requests.get(f"api.weather.com/{city}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Weather API failed: {e}")
        return {"error": "Weather data unavailable", "city": city}
```

### Testing Strategy
```python
# Test each tool independently first
def test_search_web():
    results = search_web("python programming")
    assert len(results) > 0
    assert "title" in results[0]
    assert "url" in results[0]

# Then test agent integration
def test_agent_uses_search():
    agent = ResearchAgent()
    response = agent.run("What is Python?")
    assert agent.tools_called["search_web"] >= 1
```

### Debugging
- **Log everything:** Tool calls, LLM responses, errors
- **Use verbose mode:** See agent's reasoning
- **Test tools solo:** Before integrating with agent
- **Check API limits:** Don't exceed rate limits

---

## 📚 Resources

### APIs (Free Tiers)
- **Weather:** OpenWeatherMap, Weather API
- **Web Search:** DuckDuckGo, SerpAPI
- **Knowledge:** Wikipedia API, Wolfram Alpha
- **Communication:** Twilio (SMS), SendGrid (email)

### Libraries
```bash
pip install openai langchain requests
pip install wikipedia-api arxiv duckduckgo-search
pip install chromadb sentence-transformers  # Vector memory
pip install schedule apscheduler  # Task scheduling
pip install pytest pytest-cov  # Testing
```

### Documentation
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [Agent Design Patterns](https://www.promptingguide.ai/research/llm-agents)

---

## 🤝 Getting Help

**Stuck? Try these steps:**
1. Re-read the challenge requirements
2. Review notebook examples
3. Check your tool schemas (proper JSON?)
4. Test tools individually
5. Check agent logs for errors
6. Ask in Discord/forum with:
   - What you're trying to do
   - What error you're getting
   - Code snippet (relevant parts)

**Common Issues:**
- "Agent not calling tools" → Check tool schemas
- "API errors" → Verify API key, check rate limits
- "Context too long" → Reduce message history
- "Agent loops infinitely" → Add max iterations limit

---

## 🎓 Learning Outcomes

By completing these challenges, you will:
- ✅ Master tool design and implementation
- ✅ Build robust error handling
- ✅ Implement agent memory systems
- ✅ Create multi-agent architectures
- ✅ Deploy production-ready agents
- ✅ Debug complex agent behaviors
- ✅ Optimize for performance and cost
- ✅ Build real-world agent applications

---

**Ready to build? Start with Challenge 1 and work your way up! 🚀**
