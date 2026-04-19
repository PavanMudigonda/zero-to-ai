# AI Agents

> **Build intelligent agents that can reason, plan, and use tools to accomplish complex tasks**

## 🎯 Learning Objectives

By the end of this phase, you will:

- ✅ Understand what AI agents are and how they differ from simple chatbots
- ✅ Design and implement tool/function schemas for agents
- ✅ Build agents that can use multiple tools to accomplish tasks
- ✅ Implement the ReAct (Reasoning + Acting) pattern
- ✅ Create multi-step agents with memory and state management
- ✅ Use agent frameworks (LangChain, LangGraph, OpenAI Agents SDK, CrewAI)
- ✅ Understand MCP and modern agent interoperability patterns
- ✅ Compare managed vs self-hosted agent stacks
- ✅ Understand the 2026 agentic platform landscape (OpenHands, OpenCode, Lingxi, mini-swe-agent, computer-use agents)
- ✅ Evaluate and observe agents in production
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
   - Managed vs self-hosted agent APIs
   - Open-source framework comparison
   - Interop protocols (MCP, A2A)

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
   - Reasoning-capable models for agent workflows
   - Deliberate planning vs fast-response models
   - When longer thinking improves tool use

9. **[09_autonomous_agents_2026.ipynb](09_autonomous_agents_2026.ipynb)**
   - State of the art: autonomous agents in 2026
   - OpenHands, OpenCode, Lingxi, mini-swe-agent, and computer-use agents
   - Production patterns and best practices
   - Future directions

10. **[10_agent_evaluation.ipynb](10_agent_evaluation.ipynb)**
    - Why agent evaluation is hard (non-determinism, side-effects)
    - Four dimensions: task success, trajectory quality, tool correctness, safety
    - Offline eval with LLM-as-Judge scoring
    - Online eval: observability, tracing, cost tracking
    - Frameworks: promptfoo, LangSmith, Braintrust, Arize Phoenix

### Assignments & Practice

- **[assignment.md](assignment.md)** - Build a production-ready AI agent (6 bonus options incl. MCP & eval)
- **[challenges.md](challenges.md)** - 9 hands-on challenges (⭐⭐ to ⭐⭐⭐⭐⭐)

### Quizzes

- **Pre-Quiz:** Assess baseline knowledge
- **Post-Quiz:** Validate learning outcomes

## How To Use This Phase Well

- Treat this as one of the core production phases in the repo, not just a trend topic.
- Build one agent end to end instead of sampling every framework shallowly.
- Evaluate the system you build. Agent work without measurement turns into demos very quickly.

---

## 🛠️ Tools You'll Use

- **OpenAI Function Calling** - Native tool use
- **LangChain** - Agent framework
- **LangGraph** - Workflow orchestration
- **OpenAI Agents SDK** - Lightweight multi-agent handoffs and tracing
- **CrewAI** - Role-based multi-agent coordination
- **Google ADK / Semantic Kernel** - Additional framework families to be aware of
- **MCP** - Standard tool connectivity across agent runtimes
- **OpenHands / OpenCode / mini-swe-agent / Lingxi** - Important 2026 agentic coding platforms

## 2026 Agent Topics To Know

- Managed agent APIs vs self-hosted frameworks
- Open-source agentic coding platforms vs proprietary IDE agents
- MCP for tool integration and A2A for agent delegation
- Agent observability: tracing, tool-call inspection, latency and cost tracking
- Agent evaluation: task success, trajectory quality, tool correctness, and safety gates
- Long-running and proactive agents rather than single-request assistants

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

- ✅ **LLM Basics** (Phase 11: Prompt Engineering)
- ✅ **API Usage** (Python, REST APIs)
- ✅ **JSON** (Tool schemas are JSON)
- ✅ **Async Programming** (For concurrent tool calls)
- ✅ **RAG Systems** (Phase 8) - helpful but not required

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
- [GitHub Discussions](https://github.com/zero-to-ai/discussions)
- [OpenAI Community](https://community.openai.com/)
- [AI Agents Subreddit](https://reddit.com/r/AIAgents)

---

## 🎓 Learning Path

```
Week 1: Fundamentals
├── Day 1-2: What are agents? (Notebook 1)
├── Day 3-4: Function calling (Notebook 2)
└── Day 5-7: ReAct pattern (Notebook 3)

Week 2: Frameworks & Protocols
├── Day 1-2: Agent frameworks & no-code builders (Notebook 4)
├── Day 3-4: Multi-agent systems & A2A (Notebook 5)
├── Day 5:   MCP deep-dive (Notebook 6)
└── Day 6-7: OpenAI Agents SDK & LangGraph (Notebook 7)

Week 3: Advanced & Evaluation
├── Day 1-2: Reasoning models in agent loops (Notebook 8)
├── Day 3-4: Autonomous agents 2026 (Notebook 9)
├── Day 5:   Agent evaluation & safety (Notebook 10)
└── Day 6-7: Assignment - build, evaluate & deploy
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

### Assignment
Build a production-ready agent with:
- Multiple tools
- Error handling
- Memory management
- Evaluation and testing

## What Comes Next

- Continue to [../16-model-evaluation/README.md](../16-model-evaluation/README.md) to measure task success, trajectory quality, and safety.
- Continue to [../19-ai-safety-redteaming/README.md](../19-ai-safety-redteaming/README.md) to harden agent systems against failure and misuse.
- Continue to [../31-ai-powered-dev-tools/README.md](../31-ai-powered-dev-tools/README.md) if you want to understand coding agents and MCP-heavy workflows more deeply.

---

## 🏆 Success Criteria

By the end of this phase, you should be able to:

- ✅ Explain the difference between chatbots and agents
- ✅ Design effective tool schemas
- ✅ Implement function calling with OpenAI API
- ✅ Build a ReAct agent from scratch
- ✅ Use LangChain/LangGraph for complex workflows
- ✅ Implement agent memory and state
- ✅ Evaluate agents with LLM-as-Judge and trajectory scoring
- ✅ Deploy a production agent
- ✅ Debug common agent issues

---

## 🚀 Next Steps

After completing this phase:

1. **Phase 16:** Model Evaluation & Metrics
2. **Phase 17:** Debugging AI Systems
3. **Phase 18:** Low-Code AI Tools (Gradio, Streamlit)

Or explore advanced topics:
- Multi-agent collaboration
- Agent fine-tuning
- Reinforcement learning for agents
- Human-in-the-loop systems

---

**Ready to build intelligent agents? Let's go! 🤖✨**
