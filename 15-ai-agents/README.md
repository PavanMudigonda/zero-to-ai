# Phase 14: AI Agents & Tool Use

> **Build intelligent agents that can reason, plan, and use tools to accomplish complex tasks**

## 🎯 Learning Objectives

By the end of this phase, you will:

- ✅ Understand what AI agents are and how they differ from simple chatbots
- ✅ Design and implement tool/function schemas for agents
- ✅ Build agents that can use multiple tools to accomplish tasks
- ✅ Implement the ReAct (Reasoning + Acting) pattern
- ✅ Create multi-step agents with memory and state management
- ✅ Use agent frameworks (LangChain, LangGraph, CrewAI)
- ✅ Deploy production-ready AI agents

---

## 📚 What Are AI Agents?

**AI Agent:** An autonomous system that can:
- **Perceive** its environment (receive inputs)
- **Reason** about what action to take
- **Act** by using tools/functions
- **Learn** from feedback to improve

### Chatbot vs Agent

| Feature | Chatbot | AI Agent |
|---------|---------|----------|
| **Capability** | Responds to queries | Takes actions |
| **Tools** | None | Can use external tools |
| **Autonomy** | Passive | Proactive |
| **Memory** | Conversation history | Persistent state + context |
| **Reasoning** | Single-turn | Multi-step planning |
| **Example** | "Tell me about Paris" | "Book me a flight to Paris" |

---

## 📂 Phase Content

### Notebooks

1. **[01_intro_to_agents.ipynb](01_intro_to_agents.ipynb)**
   - What are AI agents?
   - Agent architecture
   - Simple agent example
   - Agent design patterns

2. **[02_function_calling.ipynb](02_function_calling.ipynb)**
   - Tool schema design
   - OpenAI Function Calling API
   - Tool selection strategies
   - Error handling

3. **[03_react_pattern.ipynb](03_react_pattern.ipynb)**
   - ReAct: Reasoning + Acting
   - Chain-of-thought with tools
   - Multi-step problem solving
   - Building a research agent

4. **[04_agent_frameworks.ipynb](04_agent_frameworks.ipynb)**
   - LangChain agents
   - LangGraph for workflows
   - CrewAI for multi-agent systems
   - Framework comparison

5. **[05_multi_agent_systems.ipynb](05_multi_agent_systems.ipynb)**
   - Coordinating multiple agents
   - Agent communication protocols
   - Task delegation
   - Building an agent team

6. **[06_mcp_model_context_protocol.ipynb](06_mcp_model_context_protocol.ipynb)**
   - MCP: the emerging standard for AI tool integration (2026)
   - Connecting LLMs to external tools and data sources
   - Building MCP servers and clients

7. **[07_openai_agents_sdk_langgraph.ipynb](07_openai_agents_sdk_langgraph.ipynb)**
   - OpenAI Agents SDK
   - LangGraph stateful agents
   - Comparing agent frameworks

8. **[08_reasoning_models.ipynb](08_reasoning_models.ipynb)**
   - o1, o3, DeepSeek R1 reasoning models
   - Using reasoning models in agents
   - When to use reasoning vs standard models

9. **[09_autonomous_agents_2026.ipynb](09_autonomous_agents_2026.ipynb)**
   - State of the art: autonomous agents in 2026
   - Production patterns and best practices
   - Future directions

### Assignments & Practice

- **[assignment.md](assignment.md)** - Build a production-ready AI agent
- **[challenges.md](challenges.md)** - 6 hands-on challenges (⭐⭐ to ⭐⭐⭐⭐⭐)

### Quizzes

- **Pre-Quiz:** Assess baseline knowledge
- **Post-Quiz:** Validate learning outcomes

---

## 🛠️ Tools You'll Use

- **OpenAI Function Calling** - Native tool use
- **LangChain** - Agent framework
- **LangGraph** - Workflow orchestration
- **CrewAI** - Multi-agent coordination
- **AutoGPT** - Autonomous agent
- **BabyAGI** - Task-driven agent

---

## 🚀 Real-World Applications

### 1. **Customer Support Agent**
- Answer FAQs
- Query knowledge base
- Create support tickets
- Escalate to humans

### 2. **Research Assistant**
- Search web/papers
- Summarize findings
- Generate reports
- Cite sources

### 3. **Code Generation Agent**
- Understand requirements
- Write code
- Run tests
- Debug errors
- Deploy to production

### 4. **Data Analysis Agent**
- Load datasets
- Exploratory analysis
- Generate visualizations
- Statistical testing
- Create reports

### 5. **Personal Assistant**
- Check calendar
- Send emails
- Book meetings
- Set reminders
- Research topics

---

## 📊 Project: Build Your Own Agent

You'll build one of these agents:

1. **SQL Agent** - Natural language → SQL queries → Results → Insights
2. **Research Agent** - Topic → Search → Summarize → Report
3. **Coding Agent** - Requirements → Code → Test → Fix → Deploy
4. **Customer Service Agent** - Query → Knowledge base → Response → Ticket

---

## ⏱️ Time Commitment

- **Videos/Reading:** 4 hours
- **Notebooks:** 6 hours
- **Assignment:** 8 hours
- **Challenges:** 4-12 hours (optional)
- **Total:** ~18-30 hours

---

## 📖 Prerequisites

Before starting this phase, ensure you understand:

- ✅ **LLM Basics** (Phase 10: Prompt Engineering)
- ✅ **API Usage** (Python, REST APIs)
- ✅ **JSON** (Tool schemas are JSON)
- ✅ **Async Programming** (For concurrent tool calls)
- ✅ **RAG Systems** (Phase 7) - helpful but not required

---

## 🔗 Resources

### Documentation
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [CrewAI Documentation](https://docs.crewai.com/)

### Papers
- [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629)
- [Toolformer](https://arxiv.org/abs/2302.04761)
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)

### Videos
- [AI Agents Explained (10 min)](https://youtube.com/watch?v=...)
- [Building Production Agents (30 min)](https://youtube.com/watch?v=...)
- [LangGraph Tutorial (45 min)](https://youtube.com/watch?v=...)

### Community
- [LangChain Discord](https://discord.gg/langchain)
- [OpenAI Community](https://community.openai.com/)
- [AI Agents Subreddit](https://reddit.com/r/AIAgents)

---

## 🎓 Learning Path

```
Week 1: Fundamentals
├── Day 1-2: What are agents? (Notebook 1)
├── Day 3-4: Function calling (Notebook 2)
└── Day 5-7: ReAct pattern (Notebook 3)

Week 2: Frameworks & Production
├── Day 1-3: Agent frameworks (Notebook 4)
├── Day 4-5: Memory systems (Notebook 5)
└── Day 6-7: Multi-agent (Notebook 6)

Week 3: Project
├── Day 1-2: Design your agent
├── Day 3-5: Build & test
├── Day 6-7: Optimize & deploy
```

---

## ✅ Assessment

### Pre-Quiz (10 questions)
Test your baseline knowledge of:
- Agent concepts
- Tool use patterns
- API design

### Post-Quiz (10 questions)
Validate your mastery of:
- Agent architecture
- Function calling implementation
- ReAct pattern
- Production best practices

### Assignment (100 points)
Build a production-ready agent with:
- Multiple tools (30 pts)
- Error handling (20 pts)
- Memory management (20 pts)
- Evaluation & testing (30 pts)

---

## 🏆 Success Criteria

By the end of this phase, you should be able to:

- ✅ Explain the difference between chatbots and agents
- ✅ Design effective tool schemas
- ✅ Implement function calling with OpenAI API
- ✅ Build a ReAct agent from scratch
- ✅ Use LangChain/LangGraph for complex workflows
- ✅ Implement agent memory and state
- ✅ Deploy a production agent
- ✅ Debug common agent issues

---

## 🚀 Next Steps

After completing this phase:

1. **Phase 15:** Low-Code AI Tools (Gradio, Streamlit)
2. **Phase 16:** Debugging AI Systems
3. **Phase 17:** Model Evaluation & Metrics

Or explore advanced topics:
- Multi-agent collaboration
- Agent fine-tuning
- Reinforcement learning for agents
- Human-in-the-loop systems

---

**Ready to build intelligent agents? Let's go! 🤖✨**
