# AI Agents Specialization

## 🤖 Overview

Build autonomous AI systems that can reason, use tools, and collaborate to solve complex tasks!

**Time:** 3-4 weeks | 60-80 hours  
**Prerequisites:**
- ✅ LLMs & Prompt Engineering (Phase 10)
- ✅ RAG systems (Phase 7)
- ✅ Python programming

**Outcome:** Deploy production-ready AI agent systems with tool use and multi-agent collaboration

---

## 📚 What You'll Learn

### Agent Fundamentals

- [ ] What are AI agents (vs. chatbots)
- [ ] Agent architecture and components
- [ ] ReAct pattern (Reasoning + Acting)
- [ ] Function calling and tool use
- [ ] Planning and decomposition
- [ ] Memory and state management

### Agent Frameworks

- [ ] LangGraph (LangChain's agent framework)
- [ ] Microsoft Agent Framework
- [ ] AutoGen (multi-agent systems)
- [ ] CrewAI (role-based agents)
- [ ] OpenAI Assistants API
- [ ] Anthropic Claude tools

### Advanced Patterns

- [ ] Multi-agent collaboration
- [ ] Hierarchical agents (supervisor pattern)
- [ ] Human-in-the-loop workflows
- [ ] Agent reflection and self-improvement
- [ ] Parallel tool execution
- [ ] Error handling and retries

### Production Deployment

- [ ] Agent monitoring and logging
- [ ] Cost tracking and optimization
- [ ] Safety and guardrails
- [ ] Evaluation metrics
- [ ] Scaling agent systems
- [ ] Security considerations

---

## 🗂️ Module Structure

```
ai-agents/
├── 00_START_HERE.ipynb                # Agent overview & quick demo
├── 01_function_calling.ipynb          # Tool use basics
├── 02_react_pattern.ipynb             # ReAct reasoning loop
├── 03_langgraph_agents.ipynb          # LangGraph framework
├── 04_microsoft_agents.ipynb          # Microsoft Agent Framework
├── 05_autogen_multiagent.ipynb        # Multi-agent systems
├── 06_crewai.ipynb                    # Role-based collaboration
├── 07_memory_state.ipynb              # Long-term memory
├── 08_evaluation.ipynb                # Testing agents
├── 09_production.ipynb                # Deployment patterns
├── projects/
│   ├── research_assistant/            # Web research agent
│   ├── code_reviewer/                 # GitHub PR agent
│   ├── data_analyst/                  # SQL + Python agent
│   ├── customer_support/              # Multi-turn support
│   └── workflow_automation/           # Complex workflows
├── tools/
│   ├── web_search.py
│   ├── code_execution.py
│   ├── database_query.py
│   └── file_operations.py
└── README.md
```

---

## 🚀 Quick Start

### Example: Simple ReAct Agent

```python
from openai import OpenAI
import json

client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            }
        }
    }
]

def web_search(query):
    """Simulate web search."""
    return f"Results for '{query}': [Sample results...]"

# Agent loop
messages = [{"role": "user", "content": "What's the weather in Tokyo?"}]

while True:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        tools=tools
    )
    
    message = response.choices[0].message
    
    # Check if agent wants to use a tool
    if message.tool_calls:
        # Execute tool
        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            if function_name == "web_search":
                result = web_search(**function_args)
                
                # Add tool result to conversation
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
    else:
        # Agent is done
        print(message.content)
        break
```

### Example: Multi-Agent System with AutoGen

```python
from autogen import AssistantAgent, UserProxyAgent

# Define agents with different roles
researcher = AssistantAgent(
    name="Researcher",
    system_message="You research topics thoroughly and provide facts.",
    llm_config={"model": "gpt-4"}
)

writer = AssistantAgent(
    name="Writer",
    system_message="You write clear, engaging content based on research.",
    llm_config={"model": "gpt-4"}
)

critic = AssistantAgent(
    name="Critic",
    system_message="You review and provide constructive feedback.",
    llm_config={"model": "gpt-4"}
)

user = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=3
)

# Agents collaborate
user.initiate_chat(
    researcher,
    message="Write an article about quantum computing"
)
```

---

## 📋 Learning Path

### Week 1: Agent Basics

- [ ] Complete `00_START_HERE.ipynb`
- [ ] Function calling in `01_function_calling.ipynb`
- [ ] ReAct pattern in `02_react_pattern.ipynb`
- [ ] **Project:** Build a calculator agent

### Week 2: Agent Frameworks

- [ ] LangGraph in `03_langgraph_agents.ipynb`
- [ ] Microsoft framework in `04_microsoft_agents.ipynb`
- [ ] Try different frameworks
- [ ] **Project:** Research assistant

### Week 3: Multi-Agent Systems

- [ ] AutoGen in `05_autogen_multiagent.ipynb`
- [ ] CrewAI in `06_crewai.ipynb`
- [ ] Agent collaboration patterns
- [ ] **Project:** Multi-agent workflow

### Week 4: Production

- [ ] Memory in `07_memory_state.ipynb`
- [ ] Evaluation in `08_evaluation.ipynb`
- [ ] Production in `09_production.ipynb`
- [ ] **Capstone:** Production agent system

---

## 🛠️ Technologies You'll Use

**Agent Frameworks:**
- LangGraph (LangChain)
- Microsoft Agent Framework
- AutoGen (Microsoft)
- CrewAI
- Semantic Kernel

**LLM Providers:**
- OpenAI (function calling, Assistants API)
- Anthropic (Claude with tools)
- Local models (via Ollama)

**Tools & Integrations:**
- Web search (Serper, Tavily)
- Code execution (E2B, Docker)
- Database queries (SQL)
- File operations
- API calls

**Orchestration:**
- LangSmith (monitoring)
- LangServe (deployment)
- Temporal (workflows)

---

## 📊 Key Concepts Explained

### Agent vs. Chatbot

```
Chatbot:
User → LLM → Response

Agent:
User → Agent
       ↓
    Reasoning (What do I need?)
       ↓
    Action (Use tools)
       ↓
    Observation (Results)
       ↓
    Repeat until done
       ↓
    Final Answer
```

### ReAct Pattern

```
Thought: I need to find the weather
Action: web_search("Tokyo weather")
Observation: Tokyo is 15°C, sunny
Thought: I have the information
Answer: The weather in Tokyo is 15°C and sunny
```

### Multi-Agent Collaboration

```
User Request
    ↓
Supervisor Agent (coordinates)
    ↓
├─ Researcher (gathers info)
├─ Analyst (processes data)
├─ Writer (creates content)
└─ Critic (reviews)
    ↓
Final Output
```

---

## 🎯 Projects

### 1. Research Assistant

Agent that researches topics using web search and synthesizes information.

**Skills:** Tool use, ReAct, synthesis

### 2. Code Reviewer

Autonomous PR review with suggestions and tests.

**Skills:** GitHub integration, code analysis, feedback

### 3. Data Analyst Agent

Query databases, analyze data, create visualizations.

**Skills:** SQL, Python execution, reasoning

### 4. Customer Support Agent

Multi-turn conversations with CRM integration.

**Skills:** Memory, tool use, escalation

### 5. Workflow Automator

Complex multi-step business workflows.

**Skills:** Multi-agent, orchestration, error handling

---

## 📈 Evaluation Metrics

### Task Success

- **Task completion rate:** % of tasks finished correctly
- **Steps to completion:** Efficiency measure
- **Tool use accuracy:** Correct tool selection
- **Error recovery:** Handling failures

### Quality Metrics

- **Answer accuracy:** Correctness of final output
- **Reasoning quality:** Logical coherence
- **Tool call precision:** Appropriate tool use
- **Response relevance:** On-topic outputs

### Production Metrics

- **Cost per task:** Token usage + API calls
- **Latency:** Time to completion
- **Reliability:** Success rate over time
- **Safety:** Harmful action rate

---

## 💡 Best Practices

### DO ✅

- Start with single-agent before multi-agent
- Provide clear tool descriptions
- Add error handling and retries
- Set maximum iterations (prevent loops)
- Log all agent actions
- Test with edge cases
- Monitor costs closely
- Add human approval for critical actions

### DON'T ❌

- Give agents unrestricted access
- Skip input validation
- Ignore infinite loops
- Forget rate limits
- Trust agent outputs blindly
- Skip safety checks
- Ignore error logs

### Agent Design Principles

1. **Clear Role:** Define specific purpose
2. **Limited Tools:** Only necessary capabilities
3. **Good Prompts:** Detailed instructions
4. **Error Handling:** Graceful failures
5. **Monitoring:** Track all actions
6. **Safety:** Approve critical actions
7. **Testing:** Comprehensive scenarios

---

## 🔗 Resources

### Courses

- [Microsoft AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [DeepLearning.AI - AI Agents](https://www.deeplearning.ai/short-courses/)
- [LangChain Academy](https://academy.langchain.com/)

### Documentation

- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- [AutoGen Docs](https://microsoft.github.io/autogen/)
- [CrewAI Docs](https://docs.crewai.com/)

### Papers

- [ReAct: Reasoning and Acting](https://arxiv.org/abs/2210.03629)
- [Toolformer](https://arxiv.org/abs/2302.04761)
- [AutoGPT: Agent Systems](https://arxiv.org/abs/2306.02224)

### Communities

- LangChain Discord
- AutoGen GitHub
- r/LangChain

---

## ✅ Completion Checklist

Before moving forward, you should be able to:

- [ ] Explain agent vs. chatbot differences
- [ ] Implement function calling
- [ ] Build ReAct agents
- [ ] Use LangGraph for workflows
- [ ] Create multi-agent systems
- [ ] Add memory and state
- [ ] Evaluate agent performance
- [ ] Deploy agents in production
- [ ] Monitor and debug agents
- [ ] Handle errors and edge cases

---

## 🎓 What's Next?

**Real-World Applications** →
- Business process automation
- Research and analysis
- Code generation and review
- Customer service
- Data processing pipelines

**Advanced Topics** →
- Agent fine-tuning
- Custom tool development
- Distributed agent systems
- Agent-to-agent communication

---

**Ready to build autonomous agents?** → Start with `00_START_HERE.ipynb`

**Questions?** → Check the projects/ folder for complete examples

**🤖 Remember: Great agents combine reasoning with reliable tools!**

---

**Start here:** `00_START_HERE.ipynb`
