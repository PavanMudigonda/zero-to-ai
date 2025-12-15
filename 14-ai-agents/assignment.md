# Phase 14: AI Agents - Assignment

**Build a Production-Ready AI Agent System**

---

## 📋 Assignment Overview

**Objective:** Build a fully functional AI agent that can autonomously accomplish complex tasks using multiple tools and reasoning.

**Estimated Time:** 10-15 hours  
**Weight:** 100 points + 20 bonus points  
**Due:** End of Week 3  

---

## 🎯 Learning Objectives

After completing this assignment, you will be able to:

- ✅ Design and implement tool schemas for AI agents
- ✅ Build agents that use multiple tools effectively
- ✅ Implement error handling and validation
- ✅ Add memory and state management
- ✅ Evaluate agent performance
- ✅ Deploy a production-ready agent

---

## 📦 Deliverables

1. **Agent Implementation** (Python code)
2. **Tool Definitions** (JSON schemas + implementations)
3. **Test Suite** (Unit tests + integration tests)
4. **Documentation** (README + API docs)
5. **Demo Video or Live Demo** (3-5 minutes)
6. **Report** (2-3 pages analyzing your agent)

---

## 🏗️ Part 1: Agent Design & Implementation (40 points)

### Choose ONE Agent Type:

#### Option A: SQL Agent (Recommended for beginners)
**Purpose:** Natural language → SQL queries → Execute → Present results

**Required Tools:**
- `generate_sql_query(question, schema)` - Convert NL to SQL
- `execute_query(sql)` - Run SQL on database
- `explain_results(data)` - Interpret results
- `visualize_data(data, chart_type)` - Create charts

**Example Interaction:**
```
User: "Show me the top 5 customers by revenue in 2024"

Agent:
1. Generates SQL: SELECT customer_id, SUM(revenue) ... 
2. Executes query
3. Returns: "Here are your top 5 customers:
   1. Acme Corp - $1.2M
   2. TechStart - $980K
   ..."
4. Creates bar chart visualization
```

**Bonus:** Handle follow-up questions, query optimization suggestions

---

#### Option B: Research Agent
**Purpose:** Topic → Search → Summarize → Compile → Report

**Required Tools:**
- `web_search(query, num_results)` - Search the web
- `scrape_webpage(url)` - Extract content
- `summarize_text(text, max_length)` - Create summaries
- `generate_report(sections)` - Compile final report

**Example Interaction:**
```
User: "Research the latest developments in quantum computing"

Agent:
1. Searches for "quantum computing 2024 breakthroughs"
2. Scrapes top 5 articles
3. Summarizes each article
4. Compiles comprehensive report with citations
```

**Bonus:** Fact-checking, multi-source verification, citation formatting

---

#### Option C: Code Debugging Agent
**Purpose:** Buggy code → Analyze → Identify issues → Fix → Test

**Required Tools:**
- `analyze_code(code, language)` - Static analysis
- `run_tests(code, tests)` - Execute test suite
- `suggest_fixes(errors)` - Propose solutions
- `apply_fix(code, fix)` - Implement fix

**Example Interaction:**
```
User: "Debug this Python function that's failing tests"

Agent:
1. Analyzes code structure
2. Runs test suite
3. Identifies: "Index out of bounds error on line 15"
4. Suggests fix: "Add bounds checking"
5. Applies fix
6. Re-runs tests → All pass ✅
```

**Bonus:** Performance optimization, code quality improvements

---

#### Option D: Personal Assistant Agent
**Purpose:** Manage calendar, emails, tasks, reminders

**Required Tools:**
- `check_calendar(date_range)` - View events
- `schedule_meeting(title, time, attendees)` - Create events
- `send_email(to, subject, body)` - Send emails
- `set_reminder(task, time)` - Create reminders
- `web_search(query)` - Research information

**Example Interaction:**
```
User: "Schedule a meeting with John next Tuesday at 2pm to discuss Q1 planning"

Agent:
1. Checks calendar for conflicts
2. Finds available slot
3. Creates meeting event
4. Sends email invitation to John
5. Sets reminder for 1 hour before
```

**Bonus:** Smart scheduling (avoid lunch hours, respect time zones), meeting prep

---

### Requirements (All Options):

**1. Agent Architecture (15 points)**
- [ ] Clean separation of concerns (agent logic, tools, utilities)
- [ ] Configurable (system prompts, tool selection, parameters)
- [ ] Logging of all agent actions
- [ ] Error recovery mechanisms

**2. Tool Implementation (15 points)**
- [ ] At least 4 tools implemented
- [ ] Proper JSON schemas for all tools
- [ ] Input validation and error handling
- [ ] Tool execution logging

**3. Agent Reasoning (10 points)**
- [ ] Intelligent tool selection
- [ ] Multi-step planning for complex tasks
- [ ] Ability to self-correct when errors occur
- [ ] Clear reasoning traces (what, why, how)

---

## 🧠 Part 2: Memory & State Management (20 points)

Implement memory systems for your agent:

### 2.1 Conversation History (8 points)
```python
class ConversationMemory:
    def __init__(self, max_messages=10):
        self.messages = []
        self.max_messages = max_messages
    
    def add_message(self, role, content):
        """Add message to history"""
        pass
    
    def get_context(self):
        """Return recent context for LLM"""
        pass
    
    def summarize_old_messages(self):
        """Compress old messages"""
        pass
```

**Requirements:**
- [ ] Store conversation history
- [ ] Limit context window (token management)
- [ ] Summarize old messages to save tokens
- [ ] Clear context on user request

### 2.2 Task Memory (7 points)
```python
class TaskMemory:
    def __init__(self):
        self.completed_steps = []
        self.pending_steps = []
    
    def record_step(self, step, result):
        """Record completed step"""
        pass
    
    def get_progress(self):
        """Return task progress"""
        pass
```

**Requirements:**
- [ ] Track completed vs. pending steps
- [ ] Resume from failures
- [ ] Progress reporting

### 2.3 Long-Term Memory (Optional - 5 bonus points)
- [ ] Vector database for facts/knowledge
- [ ] Retrieve relevant past interactions
- [ ] Personalization based on history

---

## 🧪 Part 3: Testing & Evaluation (20 points)

### 3.1 Unit Tests (8 points)
Test each tool individually:

```python
def test_tool_name():
    """Test tool with valid inputs"""
    result = my_tool(valid_input)
    assert result == expected_output
    
def test_tool_error_handling():
    """Test tool with invalid inputs"""
    with pytest.raises(ValueError):
        my_tool(invalid_input)
```

**Requirements:**
- [ ] Test all tools with valid inputs
- [ ] Test error cases
- [ ] Test edge cases
- [ ] Achieve >80% code coverage

### 3.2 Integration Tests (7 points)
Test agent end-to-end:

```python
def test_agent_simple_query():
    """Test agent with straightforward query"""
    response = agent.run("simple query")
    assert "expected" in response.lower()

def test_agent_multi_step():
    """Test agent with complex multi-step task"""
    response = agent.run("complex task requiring multiple tools")
    assert agent.tools_used >= 2
    assert response.success == True
```

**Requirements:**
- [ ] Test simple queries
- [ ] Test multi-step tasks
- [ ] Test error recovery
- [ ] Test with real/mocked APIs

### 3.3 Evaluation Metrics (5 points)
Measure agent performance:

```python
metrics = {
    "task_success_rate": 0.85,  # % of tasks completed successfully
    "avg_tool_calls": 3.2,       # Average tools used per task
    "avg_response_time": 5.4,    # Seconds
    "token_usage": 1500,         # Average tokens per interaction
    "error_rate": 0.05           # % of errors
}
```

**Requirements:**
- [ ] Success rate on test cases
- [ ] Average response time
- [ ] Token efficiency
- [ ] Error recovery rate

---

## 📝 Part 4: Documentation & Demo (20 points)

### 4.1 README.md (8 points)
```markdown
# [Your Agent Name]

## Overview
Brief description of what your agent does

## Features
- Feature 1
- Feature 2

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from my_agent import Agent
agent = Agent()
result = agent.run("your query")
```

## Architecture
Diagram showing components

## API Reference
Tool descriptions and parameters

## Examples
5+ example interactions
```

### 4.2 Code Documentation (5 points)
- [ ] Docstrings for all functions
- [ ] Type hints
- [ ] Inline comments for complex logic
- [ ] API reference (auto-generated)

### 4.3 Demo (7 points)
**Option 1: Video Demo (3-5 minutes)**
- Show agent handling 3+ different queries
- Explain tool selection decisions
- Demonstrate error handling

**Option 2: Live Demo + Gradio UI**
- Build web interface
- Demo during presentation
- Include example queries

---

## 🎁 Bonus Challenges (+20 points)

### Bonus 1: Advanced Reasoning (+5 points)
Implement **ReAct** (Reasoning + Acting) pattern:
```
Thought: I need to find the revenue data
Action: execute_query("SELECT SUM(revenue) FROM sales WHERE year=2024")
Observation: Total revenue is $5.2M
Thought: Now I should compare to 2023
Action: execute_query("SELECT SUM(revenue) FROM sales WHERE year=2023")
Observation: 2023 revenue was $4.1M
Thought: Growth is 26.8%, I can now respond
Final Answer: Revenue grew by 26.8% from $4.1M to $5.2M
```

### Bonus 2: Parallel Tool Execution (+5 points)
- Execute multiple independent tools concurrently
- Aggregate results efficiently
- Handle parallel errors gracefully

### Bonus 3: Agent Optimization (+5 points)
- Cache frequent API calls
- Optimize token usage
- Reduce latency with streaming
- Smart tool selection (skip unnecessary tools)

### Bonus 4: Production Deployment (+5 points)
- Deploy as REST API (FastAPI/Flask)
- Add authentication
- Rate limiting
- Monitoring dashboard
- Docker containerization

---

## 📊 Grading Rubric

### Part 1: Agent Design & Implementation (40 points)
| Criteria | Points | Description |
|----------|--------|-------------|
| **Architecture** | 15 | Clean code, separation of concerns, configurability |
| **Tools** | 15 | All tools work correctly, proper schemas, error handling |
| **Reasoning** | 10 | Intelligent tool selection, multi-step planning |

### Part 2: Memory & State (20 points)
| Criteria | Points | Description |
|----------|--------|-------------|
| **Conversation History** | 8 | Properly stores and retrieves context |
| **Task Memory** | 7 | Tracks progress, resumes from failures |
| **Implementation** | 5 | Clean code, efficient storage |

### Part 3: Testing & Evaluation (20 points)
| Criteria | Points | Description |
|----------|--------|-------------|
| **Unit Tests** | 8 | Comprehensive coverage, edge cases |
| **Integration Tests** | 7 | End-to-end scenarios, error cases |
| **Metrics** | 5 | Proper evaluation methodology |

### Part 4: Documentation & Demo (20 points)
| Criteria | Points | Description |
|----------|--------|-------------|
| **README** | 8 | Clear, comprehensive, examples |
| **Code Docs** | 5 | Docstrings, type hints, comments |
| **Demo** | 7 | Shows key features, explains decisions |

### Bonus (up to +20 points)
- ReAct pattern: +5
- Parallel execution: +5
- Optimization: +5
- Deployment: +5

---

## 💡 Hints & Tips

### Getting Started
1. **Start simple:** Build basic agent with 1-2 tools first
2. **Test early:** Write tests as you build tools
3. **Iterate:** Add features incrementally
4. **Use frameworks:** LangChain can simplify development

### Tool Design
- Keep tools focused (single responsibility)
- Validate inputs rigorously
- Return structured data (JSON)
- Include helpful error messages

### Debugging
- Log all LLM calls and tool executions
- Test tools independently before agent integration
- Use `print` statements liberally
- Check token usage to avoid context overflow

### Common Pitfalls
- ❌ Tools that do too much (break into smaller tools)
- ❌ Poor error handling (always validate inputs)
- ❌ No logging (impossible to debug)
- ❌ Ignoring context limits (manage tokens carefully)

---

## 📚 Resources

### Code Examples
- [OpenAI Function Calling Examples](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models)
- [LangChain Agent Templates](https://python.langchain.com/docs/modules/agents/agent_types/)
- [Agent Design Patterns](https://github.com/microsoft/ai-agents-for-beginners)

### Testing
- [Pytest Documentation](https://docs.pytest.org/)
- [Unit Testing Best Practices](https://realpython.com/python-testing/)

### Deployment
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Docker for Python](https://docs.docker.com/language/python/)

---

## 🤝 Collaboration Policy

- **Individual assignment:** Complete independently
- **Getting help:** Office hours, Discord, Stack Overflow
- **Code sharing:** Don't share solutions, but discuss approaches
- **AI assistance:** OK to use for debugging, not for writing entire agent

---

## 📅 Submission

**Submit via GitHub:**
1. Create repo: `ai-agent-[your-name]`
2. Include all deliverables
3. Add comprehensive README
4. Submit repo link

**Deadline:** [Date]

**Late Policy:** -10% per day, up to 3 days

---

## ❓ FAQ

**Q: Can I use LangChain or must I build from scratch?**  
A: You can use frameworks, but you must understand and explain the code.

**Q: How many tools are required?**  
A: Minimum 4 tools. More is better if they're all useful.

**Q: Can I use mock/fake APIs for testing?**  
A: Yes for testing, but include at least one real API integration.

**Q: What if my agent makes mistakes?**  
A: That's OK! Document the failure cases and explain why they occur.

**Q: Can I work in a team?**  
A: No, this is individual. But you can discuss ideas with classmates.

---

**Good luck building your AI agent! 🚀🤖**
