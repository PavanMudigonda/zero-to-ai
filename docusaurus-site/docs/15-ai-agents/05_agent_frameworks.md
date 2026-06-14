---
title: "5. Agent Frameworks"
sidebar_label: "5. Agent Frameworks"
sidebar_position: 6
format: "md"
---
```python
# Install required packages
# !pip install langchain langchain-openai langgraph chromadb

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

load_dotenv()
print("✅ Setup complete")
```

<a id="part1"></a>
## Part 1: Framework Overview (2026 Landscape)

The agent ecosystem now spans **fully managed cloud APIs**, **open-source SDKs/frameworks**, **interop protocols**, and **agent runtimes** that let agents share tools and talk to each other.

---

### Fully Managed Agent APIs

These platforms host and run agents for you - bring your prompt and tools, they handle infra, scaling, and monitoring.

| Service | Vendor | Model Lock-in | Key Differentiator |
|---|---|---|---|
| **Anthropic Managed Agents** | Anthropic | Claude only | Versioned agent configs, hosted infra, built-in tool suite |
| **LangGraph Cloud** | LangChain | Model-agnostic | Hosted deployment of LangGraph agents, persistence, streaming |
| **AWS Bedrock Agents** | AWS | Multi-model (Bedrock) | Native AWS integrations (S3, Lambda, Knowledge Bases) |
| **Azure AI Agent Service** | Microsoft (Foundry) | Multi-model (Azure) | Tool connectors (Azure Search, Code Interpreter, Bing), enterprise RBAC |
| **Vertex AI Agent Builder** | Google | Gemini-native | GCP-native, integrated with Vertex AI Search and Conversation |
| **Salesforce Agentforce** | Salesforce | Multi-model | Enterprise agents embedded in CRM workflows |
| **Cohere Agents** | Cohere | Command R+ | Tool-use + multi-step workflows built into Cohere's ecosystem |

---

### Open-Source SDKs & Frameworks

| Framework | Best For | Learning Curve | Key Differentiator |
|-----------|----------|----------------|--------------------|
| **Microsoft Agent Framework** | Unified agent SDK (Python + .NET) | Medium | Successor to AutoGen - full planning, tools, memory, orchestration |
| **LangChain** | General-purpose agents, quick prototypes | Easy | Largest ecosystem of tools and integrations |
| **LangGraph** | Complex workflows, cyclic graphs | Medium-Hard | Graph-based orchestration, most mature for stateful agents |
| **OpenAI Agents SDK** | Lightweight multi-agent handoffs | Easy | Minimal abstractions, built-in tracing, provider-agnostic via LiteLLM |
| **LlamaIndex** | RAG-heavy agents, knowledge graphs | Medium | Graph-based agent orchestration + deep retrieval integration |
| **Google ADK** | GCP-native agents, multi-language | Medium | 4 language SDKs (Python, Java, Go, Node), A2A protocol |
| **CrewAI** | Multi-agent teams, role-based agents | Easy | Easiest onboarding, role-based collaboration model |
| **AutoGen** | Multi-agent conversation/debate | Medium | Microsoft-backed, now merging into Microsoft Agent Framework |
| **Semantic Kernel** | Enterprise .NET + Python agents | Medium | Deep Azure integration, .NET first-class support, plugin system |
| **SmolAgents** | Minimal code-first agents | Easy | Hugging Face, <100 lines to a working agent, code-generation agents |
| **Llama-stack** | Meta/Llama ecosystem | Medium | Safety built-in, Llama-native tooling, on-device support |
| **Haystack** | RAG-heavy agent pipelines | Medium | deepset, pipeline-based, strong retrieval integration |
| **Bee Agent Framework** | Production enterprise agents | Medium | IBM-backed, observability and compliance focus |
| **Custom** | Full control, specific requirements | Hard | No abstractions, maximum flexibility |

---

### Agent Runtimes (Execute Agents: Loops, Scheduling, Orchestration)

Runtimes provide the **execution engine** that runs agent loops, manages state, handles retries, and schedules workflows. While frameworks define *what* agents do, runtimes define *how* they execute reliably in production.

| Runtime | Type | Key Differentiator | Best For |
|---|---|---|---|
| **Temporal.io** | Workflow engine | Durable execution, automatic retries, saga patterns | Production agent workflows that must survive crashes and restarts |
| **AWS Step Functions** | Serverless orchestrator | Event-driven, native AWS integrations, visual workflow editor | Agent workflows on AWS with Lambda-based tool execution |
| **Microsoft Agent Runtime** | Agent execution engine | Part of Microsoft Agent Framework, deterministic execution | Running Microsoft Agent Framework agents in production |
| **LangGraph Runtime** | Agent runtime | Built into LangGraph Cloud, persistence, streaming | Hosted LangGraph agent execution with checkpointing |

**Why runtimes matter:** An agent framework gives you tools, planning, and memory - but when your 10-step agent workflow crashes on step 7, the runtime determines whether it resumes from step 7 or starts over. Temporal and Step Functions both provide **durable execution**: each step's result is persisted, so failures resume rather than restart. This is critical for production agents that call expensive APIs, modify external state, or run for minutes/hours.

---

### Interop Protocols & Standards

| Protocol | Purpose | Status (2026) |
|---|---|---|
| **MCP (Model Context Protocol)** | Standardized tool/resource connectivity for agents | Broadly adopted - Anthropic, OpenAI, Google, Microsoft all support it |
| **A2A (Agent-to-Agent, Google)** | Agent interoperability - agents discovering and delegating to other agents | Early adoption - Google ADK native, growing cross-vendor support |

See [Notebook 06](07_mcp_model_context_protocol.ipynb) for deep coverage of MCP.

---

### Visual / No-Code Agent Builders

For teams that want to build agent workflows without writing Python, several platforms provide drag-and-drop graph editors:

| Platform | Type | Key Feature | Best For |
|---|---|---|---|
| **Langflow** | Open-source | Visual LangChain/LangGraph builder, runs locally or on Datastax cloud | Prototyping LangChain flows, export to Python |
| **Flowise** | Open-source | Low-code LLM app builder, Node.js, Docker-ready | Quick chatbot/agent demos, internal tools |
| **Dify** | Open-source | Full RAG + agent platform with visual workflow editor | End-to-end LLM apps, teams with mixed skill levels |
| **n8n AI** | Open-source + cloud | Workflow automation with AI agent nodes | Connecting agents to 400+ SaaS integrations |

**When to choose no-code:** Rapid prototyping, non-developer stakeholders defining workflows, or simple agent use cases that don't require custom Python logic.

---

### When to Use Each

**Microsoft Agent Framework:**
- ✅ Unified Python + .NET SDK for building agents
- ✅ Full planning, tools, memory, multi-agent orchestration
- ✅ Successor to AutoGen (active development by Microsoft)
- ❌ Newer ecosystem, still evolving

**LangChain:**
- ✅ Quick prototypes
- ✅ Standard agent patterns
- ✅ Rich ecosystem of tools
- ❌ Limited control over agent loop

**LangGraph:**
- ✅ Complex state machines
- ✅ Cyclic workflows
- ✅ Human-in-the-loop
- ❌ Steepest learning curve

**OpenAI Agents SDK:**
- ✅ Lightweight, minimal boilerplate
- ✅ Multi-agent handoffs built-in
- ✅ Provider-agnostic (LiteLLM)
- ❌ Less mature ecosystem than LangChain

**LlamaIndex:**
- ✅ Best-in-class retrieval integration
- ✅ Graph-based agent orchestration
- ✅ Knowledge graph + RAG agent pipelines
- ❌ Retrieval-centric - less general than LangChain

**Google ADK:**
- ✅ Multi-language (Python, Java, Go, Node)
- ✅ Native A2A protocol support
- ✅ GCP integration
- ❌ Smaller community than LangChain/OpenAI

**CrewAI:**
- ✅ Role-based collaboration
- ✅ Easiest onboarding
- ❌ Less flexible for non-team patterns

**Semantic Kernel:**
- ✅ .NET first-class support
- ✅ Deep Azure/Microsoft 365 integration
- ❌ Smaller Python community

**Custom Implementation:**
- ✅ Full control
- ✅ Optimized for specific use case
- ❌ More development time

### Managed vs. Self-Hosted: Key Questions

1. **Cost vs. control** - Are you willing to pay for fully managed agent infra (Anthropic, Azure, AWS), or do you prefer owning the stack?
2. **Lock-in** - Anthropic Managed Agents ties you to Claude. Azure ties you to Azure. Does model/cloud flexibility matter?
3. **Multi-agent in prod** - Running multi-agent setups? LangGraph and AutoGen handle this best. CrewAI is easiest to start.
4. **Interop** - Does your architecture need MCP (tool sharing) or A2A (agent delegation)? These are becoming table stakes for multi-vendor setups.
5. **Durability** - Long-running agent workflows? Consider Temporal.io or AWS Step Functions as your execution runtime.

<a id="part2"></a>
## Part 2: LangChain Agents

### Building Your First LangChain Agent

LangChain abstracts the agent loop into two core components: an **Agent** (the LLM reasoning engine that decides which tool to call) and an **AgentExecutor** (the runtime that manages the observe-think-act cycle, handles tool dispatch, and enforces iteration limits). The `create_openai_functions_agent` constructor wires the LLM to OpenAI's native function-calling API, so the model returns structured JSON tool invocations rather than free-text that must be parsed with brittle regex.

### How LangChain Agents Work

The executor runs a loop: (1) pass the conversation plus a scratchpad of prior tool calls/results to the LLM, (2) if the LLM returns a function call, execute the matching `Tool` and append the result to the scratchpad, (3) repeat until the LLM returns a plain text answer or `max_iterations` is reached. This is functionally equivalent to the ReAct pattern from Notebook 03, but the framework handles prompt formatting, output parsing, and error recovery. The `Tool` wrapper maps a Python callable to a name and natural-language description that the LLM uses to decide when invocation is appropriate, making tool registration a one-liner rather than a manual JSON schema.

<a id="part1b"></a>
## Part 1b: Microsoft Agent Framework

### The Successor to AutoGen

Microsoft Agent Framework is a full SDK for building, orchestrating, and deploying agents in Python and .NET. It unifies concepts from AutoGen (multi-agent conversations) and Semantic Kernel (plugins, planners) into a single framework with first-class support for:

- **Planning:** Built-in task decomposition and step-by-step execution
- **Tools:** Register Python functions as agent tools with type-safe schemas
- **Memory:** Short-term conversation memory + long-term retrieval
- **Multi-agent orchestration:** Agent-to-agent handoffs, coordinator patterns
- **MCP integration:** Connect to any MCP server for standardized tool access

🔗 [GitHub: microsoft/agent-framework](https://github.com/microsoft/agent-framework)

### Why It Matters

AutoGen pioneered multi-agent conversation patterns but was research-oriented. Microsoft Agent Framework is the **production-grade evolution** - it's what Microsoft recommends for building agents that deploy to Azure AI Agent Service, run locally, or integrate with Microsoft 365 Copilot. If you're in the Microsoft/Azure ecosystem, this is your primary agent SDK going forward.

### Quick Example: Agent with Tools

The pattern is similar to other frameworks - define tools as Python functions, create an agent with a system prompt, and run it. The key difference is the unified API across Python and .NET, plus built-in Azure deployment support.

```python
# Microsoft Agent Framework - Conceptual Example
# pip install microsoft-agent-framework

# NOTE: The Microsoft Agent Framework SDK is under active development.
# This example shows the core patterns. Check the GitHub repo for the latest API.
# https://github.com/microsoft/agent-framework

# --- Pattern 1: Single Agent with Tools ---
# The framework uses decorators to register Python functions as agent tools.
# Each tool gets a typed schema that the LLM uses for structured invocation.

"""
from agent_framework import Agent, tool

@tool
def search_web(query: str) -> str:
    \"\"\"Search the web for information.\"\"\"
    # Your search implementation
    return f"Results for: {query}"

@tool
def calculate(expression: str) -> float:
    \"\"\"Evaluate a math expression.\"\"\"
    return eval(expression)  # Use a safe evaluator in production

# Create agent with tools
agent = Agent(
    name="research_assistant",
    instructions="You are a helpful research assistant.",
    tools=[search_web, calculate],
    model="gpt-4"
)

# Run the agent
result = await agent.run("What is the population of France divided by 1000?")
print(result)
"""

# --- Pattern 2: Multi-Agent Orchestration ---
# Microsoft Agent Framework supports agent-to-agent handoffs,
# similar to OpenAI Swarm but with richer orchestration primitives.

"""
from agent_framework import Agent, Orchestrator

researcher = Agent(
    name="researcher",
    instructions="You research topics thoroughly.",
    tools=[search_web]
)

writer = Agent(
    name="writer",
    instructions="You write clear, engaging content based on research.",
    tools=[]
)

# Orchestrator coordinates the agents
orchestrator = Orchestrator(
    agents=[researcher, writer],
    strategy="sequential"  # or "parallel", "coordinator"
)

result = await orchestrator.run("Write a summary of recent AI breakthroughs")
"""

print("✅ Microsoft Agent Framework patterns shown (conceptual)")
print("📦 Install: pip install microsoft-agent-framework")
print("🔗 https://github.com/microsoft/agent-framework")
```

<a id="part1c"></a>
## Part 1c: LlamaIndex Agents

### Graph-Based Agent Orchestration + Deep Retrieval

LlamaIndex started as a RAG framework but has evolved into a full agent platform. Its strength is **retrieval-augmented agents** - agents that reason over structured and unstructured knowledge sources using index-backed tools. LlamaIndex agents can query vector stores, knowledge graphs, SQL databases, and APIs, all within a unified agent loop.

🔗 [GitHub: run-llama/llama_index](https://github.com/run-llama/llama_index)

### Key Concepts

- **QueryEngineTool:** Wraps any LlamaIndex index (vector, knowledge graph, SQL) as a tool the agent can call
- **ReActAgent:** Built-in ReAct implementation that uses LlamaIndex tools
- **Workflows:** Graph-based orchestration for complex multi-step agent pipelines (similar to LangGraph)
- **Observability:** Built-in callback system for tracing agent decisions

### When to Choose LlamaIndex Over LangChain

| Scenario | LlamaIndex | LangChain |
|---|---|---|
| RAG-heavy agents with multiple data sources | ✅ Best choice | Good but more boilerplate |
| Knowledge graph + vector hybrid retrieval | ✅ Native support | Requires custom integration |
| General-purpose agents with many tool types | Good | ✅ Larger tool ecosystem |
| Quick prototyping | Good | ✅ More examples/tutorials |

```python
# LlamaIndex Agent Example
# pip install llama-index llama-index-llms-openai

"""
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata, FunctionTool
from llama_index.llms.openai import OpenAI

# --- Tool 1: RAG over documents ---
# Load documents and create a vector index
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Wrap the query engine as an agent tool
doc_tool = QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(
        name="document_search",
        description="Search through project documentation. Use for questions about the codebase or project."
    )
)

# --- Tool 2: Custom function tool ---
def calculate(expression: str) -> str:
    \"\"\"Evaluate a math expression safely.\"\"\"
    allowed = set("0123456789+-*/.()")
    if all(c in allowed for c in expression.replace(" ", "")):
        return str(eval(expression))
    return "Invalid expression"

calc_tool = FunctionTool.from_defaults(fn=calculate)

# --- Create ReAct Agent ---
llm = OpenAI(model="gpt-4", temperature=0)
agent = ReActAgent.from_tools(
    tools=[doc_tool, calc_tool],
    llm=llm,
    verbose=True
)

# Run the agent
response = agent.chat("How many pages are in the documentation?")
print(response)
"""

print("✅ LlamaIndex agent patterns shown (conceptual)")
print("📦 Install: pip install llama-index llama-index-llms-openai")
print("🔗 https://github.com/run-llama/llama_index")
```

```python
# Initialize LLM
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Define tools
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)

def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b

# Create LangChain tools
tools = [
    Tool(
        name="get_word_length",
        func=get_word_length,
        description="Get the length of any word. Input should be a single word."
    ),
    Tool(
        name="multiply",
        func=lambda x: multiply_numbers(*map(float, x.split(','))),
        description="Multiply two numbers. Input should be two numbers separated by comma, e.g., '5,3'"
    )
]

print(f"✅ Created {len(tools)} tools")
```

```python
# Create agent prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to tools."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# Create agent
agent = create_openai_functions_agent(llm, tools, prompt)

# Create agent executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=5
)

print("✅ LangChain agent ready")
```

```python
# Test the agent
response = agent_executor.invoke({
    "input": "What is the length of the word 'LangChain' multiplied by 3?"
})

print(f"\n🤖 Agent Response: {response['output']}")
```

### Real-World Example: Research Agent

A research agent demonstrates how multiple tools compose to answer questions that no single tool could handle alone. The agent below has access to Wikipedia for factual retrieval, a calculator for arithmetic, and a date tool for temporal context. When the user asks a compound question like "How many years ago was Python created?", the agent autonomously chains tool calls: first querying Wikipedia for the creation date, then calling the calculator to subtract from today's date.

### Why This Pattern Matters

Production LLM applications rarely need just one capability. By registering heterogeneous tools with clear, descriptive docstrings, you let the model's function-calling mechanism serve as an implicit **router** that selects the right tool based on semantic understanding of the query. The quality of tool descriptions directly affects routing accuracy -- vague descriptions cause the agent to pick the wrong tool or hallucinate answers instead of calling any tool at all. Each `Tool` object's `description` field is effectively part of the prompt, so treat it with the same care you would give a system message.

```python
import wikipedia
from datetime import datetime

# Wikipedia search tool
def search_wikipedia(query: str) -> str:
    """Search Wikipedia and return a summary."""
    try:
        return wikipedia.summary(query, sentences=3)
    except:
        return f"Could not find information about '{query}'"

# Current date tool
def get_current_date() -> str:
    """Get the current date."""
    return datetime.now().strftime("%B %d, %Y")

# Calculator tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Invalid expression"

# Create research tools
research_tools = [
    Tool(
        name="wikipedia",
        func=search_wikipedia,
        description="Search Wikipedia for information. Input should be a search query."
    ),
    Tool(
        name="current_date",
        func=get_current_date,
        description="Get today's date. No input required."
    ),
    Tool(
        name="calculator",
        func=calculate,
        description="Calculate mathematical expressions. Input should be a valid math expression."
    )
]

# Create research agent
research_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research assistant. Answer questions using available tools."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

research_agent = create_openai_functions_agent(llm, research_tools, research_prompt)
research_executor = AgentExecutor(
    agent=research_agent,
    tools=research_tools,
    verbose=True
)

print("✅ Research agent ready")
```

```python
# Test research agent
result = research_executor.invoke({
    "input": "Who invented Python programming language and when?"
})

print(f"\n📚 Research Result:\n{result['output']}")
```

<a id="part3"></a>
## Part 3: LangGraph Workflows

### From Linear Chains to Stateful Graphs

LangGraph extends LangChain by modeling agent logic as a **directed graph** where nodes are processing steps and edges define transitions. Unlike a simple sequential chain, LangGraph supports cycles (an agent can loop back to re-plan after receiving new information), conditional branching (route to different nodes based on state), and human-in-the-loop checkpoints. The `StateGraph` class manages a typed state dictionary that flows through the graph, with each node reading and updating shared state via `TypedDict` annotations.

### Why Graph-Based Orchestration Matters

Many real-world agent tasks are not linear pipelines. A coding assistant might plan, write code, run tests, discover a bug, and loop back to rewrite -- a cyclic workflow that cannot be expressed as a simple chain. LangGraph's `add_conditional_edges` method lets you define routing functions that inspect the current state and choose the next node, enabling patterns like retry loops, parallel fan-out/fan-in, and early termination. The `compile()` step converts the graph definition into an executable `Runnable` that supports streaming, async execution, and state persistence for long-running workflows.

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

# Define state
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    next_step: str
    final_answer: str

# Node functions
def planning_node(state: AgentState) -> AgentState:
    """Plan the approach"""
    print("🧠 Planning...")
    state["messages"].append("Created plan")
    state["next_step"] = "research"
    return state

def research_node(state: AgentState) -> AgentState:
    """Conduct research"""
    print("🔍 Researching...")
    state["messages"].append("Gathered information")
    state["next_step"] = "synthesis"
    return state

def synthesis_node(state: AgentState) -> AgentState:
    """Synthesize findings"""
    print("✍️ Synthesizing...")
    state["final_answer"] = "Research complete with findings"
    state["next_step"] = "end"
    return state

# Build graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("planning", planning_node)
workflow.add_node("research", research_node)
workflow.add_node("synthesis", synthesis_node)

# Add edges
workflow.set_entry_point("planning")
workflow.add_edge("planning", "research")
workflow.add_edge("research", "synthesis")
workflow.add_edge("synthesis", END)

# Compile
app = workflow.compile()

print("✅ LangGraph workflow created")
```

```python
# Run the workflow
initial_state = {
    "messages": ["Starting research task"],
    "next_step": "planning",
    "final_answer": ""
}

final_state = app.invoke(initial_state)

print("\n📊 Workflow Result:")
print(f"Messages: {final_state['messages']}")
print(f"Final Answer: {final_state['final_answer']}")
```

<a id="part4"></a>
## Part 4: Memory Integration

### Giving Agents Persistent Context

Without memory, every agent invocation is stateless -- the LLM has no knowledge of prior turns. `ConversationBufferMemory` solves this by storing the full message history and injecting it into the prompt via the `chat_history` placeholder. This enables multi-turn interactions where the agent can reference earlier context ("What was my name?" or "Use the same format as before").

### Memory Strategies and Trade-offs

Buffer memory is the simplest approach but grows linearly with conversation length, eventually exceeding the model's context window. LangChain provides alternatives: `ConversationSummaryMemory` compresses older turns into a running summary (trading fidelity for token efficiency), `ConversationBufferWindowMemory` keeps only the last $k$ turns, and `VectorStoreMemory` embeds messages for semantic retrieval of relevant history. Choosing the right memory strategy depends on your token budget, conversation length, and whether the agent needs exact recall or just topical awareness of past interactions.

```python
from langchain.memory import ConversationBufferMemory

# Create memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Create agent with memory
memory_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Remember previous conversation."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

memory_agent = create_openai_functions_agent(llm, research_tools, memory_prompt)
memory_executor = AgentExecutor(
    agent=memory_agent,
    tools=research_tools,
    memory=memory,
    verbose=True
)

print("✅ Agent with memory ready")
```

```python
# Test memory
print("First message:")
response1 = memory_executor.invoke({"input": "My name is Alice"})
print(response1['output'])

print("\nSecond message (should remember name):")
response2 = memory_executor.invoke({"input": "What's my name?"})
print(response2['output'])
```

<a id="part5"></a>
## Part 5: Framework Comparison

### LangChain vs Custom Implementation

The fundamental trade-off in agent frameworks is **development speed versus control**. LangChain lets you build a functional agent in 5-10 lines by composing pre-built abstractions (`Tool`, `AgentExecutor`, `Memory`), but those abstractions impose opinions about prompt formatting, error handling, and the agent loop that may not suit every use case. A custom implementation requires writing the full observe-think-act loop, tool dispatch, output parsing, and retry logic yourself -- easily 50+ lines -- but gives you complete visibility into every decision the agent makes.

### When Custom Wins

Custom implementations become worthwhile when you need fine-grained control over token budgets (e.g., dynamically pruning tool descriptions based on context), non-standard reasoning patterns (e.g., tree-of-thought with backtracking), or tight integration with proprietary infrastructure. In production systems where latency and cost matter, the overhead of framework abstractions -- extra prompt tokens from verbose templates, unnecessary serialization steps -- can add up. Profile both approaches on your actual workload before committing.

```python
import time

# LangChain approach (5-10 lines)
def langchain_agent():
    tools = [Tool(name="calc", func=lambda x: eval(x), description="Calculator")]
    agent = create_openai_functions_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools)
    return executor.invoke({"input": "What is 15 + 27?"})

# Custom approach (50+ lines)
def custom_agent():
    # Would need: prompt engineering, tool execution, loop control,
    # error handling, parsing, etc.
    pass

print("✅ LangChain: Quick to build, less control")
print("✅ Custom: More code, full control")
```

### Decision Matrix (2026)

| Criteria | LangChain | LangGraph | OpenAI Agents SDK | MS Agent Framework | LlamaIndex | Google ADK | CrewAI | Semantic Kernel | Custom |
|----------|-----------|-----------|-------------------|--------------------|------------|------------|--------|-----------------|--------|
| **Development Speed** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐ |
| **Flexibility** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **RAG Integration** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Multi-Agent** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **MCP Support** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **Model Agnostic** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Documentation** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | N/A |
| **Community** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ |
| **Production Ready** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

<a id="part6"></a>
## Part 6: Production Patterns

### Error Handling and Retries

Production agents face failures that never appear in tutorials: API rate limits, malformed tool outputs, infinite reasoning loops, and context window overflows. Wrapping the `AgentExecutor` in a custom subclass lets you intercept exceptions at the execution boundary, log diagnostic information, and return graceful fallback responses instead of crashing. The pattern below catches any exception during the agent loop and converts it into a structured error response that downstream code can handle.

### Why Defensive Agent Design Matters

An unhandled exception in an agent loop can leave the system in an inconsistent state -- partial tool calls executed, memory corrupted, or user-facing errors exposed. Production agents should implement **circuit breaker** patterns (stop calling a failing tool after $n$ consecutive errors), **timeout guards** (abort if the agent hasn't converged within a time budget), and **graceful degradation** (fall back to a simpler model or direct response when tools are unavailable). The `max_iterations` parameter in `AgentExecutor` is your first line of defense against infinite loops, but application-level error handling provides the safety net.

```python
from langchain.callbacks import StdOutCallbackHandler

# Add custom error handling
class SafeAgentExecutor(AgentExecutor):
    def _call(self, inputs, **kwargs):
        try:
            return super()._call(inputs, **kwargs)
        except Exception as e:
            return {
                "output": f"Error occurred: {str(e)}",
                "error": True
            }

print("✅ Safe agent executor ready")
```

### Monitoring and Logging

Structured logging transforms an opaque agent into an observable system. By subclassing `AgentExecutor` and logging inputs and outputs at the execution boundary, you create an audit trail that answers critical production questions: which tool was called, what arguments were passed, how long each step took, and whether the agent's final answer addressed the user's intent. LangChain's callback system (`StdOutCallbackHandler`, `LangSmithTracer`) provides built-in hooks for tracing every intermediate step -- tool invocations, LLM calls, token counts -- without modifying agent code. In production, pipe these traces to an observability platform (Datadog, Weights & Biases, LangSmith) to monitor latency distributions, error rates, and cost per query across your agent fleet.

```python
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoggingAgentExecutor(AgentExecutor):
    def _call(self, inputs, **kwargs):
        logger.info(f"Agent input: {inputs}")
        result = super()._call(inputs, **kwargs)
        logger.info(f"Agent output: {result}")
        return result

print("✅ Logging configured")
```

<a id="part7"></a>
## Part 7: Agent Runtimes for Production

### Why Frameworks Alone Aren't Enough

Agent frameworks (LangChain, LangGraph, Microsoft Agent Framework) define **what** an agent does - tools, planning, memory. But in production, you also need a **runtime** that handles:

- **Durable execution:** If step 5 of a 10-step workflow crashes, resume from step 5 instead of restarting
- **Retries with backoff:** Automatic retry of failed API calls with exponential backoff
- **Timeouts:** Kill agents that run too long
- **Observability:** Track every step, its duration, inputs, and outputs
- **Scheduling:** Trigger agent workflows on events, timers, or webhooks

Two runtimes dominate production agent deployments: **Temporal.io** and **AWS Step Functions**.

---

### Temporal.io - Durable Workflow Engine

Temporal is an open-source workflow engine that provides **durable execution** for long-running processes. Each step (called an "activity") is automatically persisted, so if your process crashes, it resumes exactly where it left off. This makes it ideal for agent workflows that call expensive APIs, modify external state, or run for minutes/hours.

🔗 [temporal.io](https://temporal.io) | [GitHub: temporalio/temporal](https://github.com/temporalio/temporal)

**Key concepts:**
- **Workflow:** The orchestration logic (your agent's planning loop)
- **Activity:** A single step (tool call, API request, LLM inference)
- **Task Queue:** Workers pick up activities from queues, enabling horizontal scaling
- **Saga pattern:** If step 5 fails, automatically compensate steps 1-4 (undo side effects)

**When to use Temporal:**
- ✅ Agent workflows that take minutes/hours (research agents, code generation pipelines)
- ✅ Workflows that modify external state (database writes, API calls) and need rollback on failure
- ✅ Multi-step agent pipelines where each step is expensive (LLM calls cost money)
- ✅ Self-hosted or Temporal Cloud - you own the infrastructure
- ❌ Overkill for simple, fast agent tasks (< 30 seconds)

---

### AWS Step Functions - Serverless Agent Orchestration

AWS Step Functions is a serverless orchestrator that coordinates AWS services (Lambda, ECS, Bedrock) into workflows defined as state machines. For teams already on AWS, it's a natural choice for running agent workflows without managing infrastructure.

🔗 [AWS Step Functions](https://aws.amazon.com/step-functions/)

**Key concepts:**
- **State machine:** Visual JSON/YAML definition of your agent workflow
- **States:** Task (call Lambda/Bedrock), Choice (conditional routing), Parallel (fan-out), Wait (pause)
- **Express vs. Standard:** Express for short-lived (< 5 min), Standard for long-running (up to 1 year)
- **Native Bedrock integration:** Call foundation models directly from workflow steps

**When to use Step Functions:**
- ✅ Already on AWS - native integrations with Lambda, Bedrock, S3, DynamoDB
- ✅ Event-driven agent workflows triggered by SQS, EventBridge, API Gateway
- ✅ Visual workflow editor for non-developers to understand agent logic
- ✅ Serverless - no infrastructure to manage
- ❌ Vendor lock-in to AWS
- ❌ Less flexible than code-first approaches for complex agent reasoning loops

---

### Runtime Comparison

| Criteria | Temporal.io | AWS Step Functions | LangGraph Cloud |
|---|---|---|---|
| **Hosting** | Self-hosted or Temporal Cloud | Fully managed (AWS) | Fully managed (LangChain) |
| **Language** | Python, Go, Java, TypeScript | JSON/YAML + Lambda (any) | Python |
| **Durability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Cost Model** | Infra-based | Per-transition | Per-invocation |
| **Agent Framework Integration** | Any (wrap activities) | AWS Bedrock Agents native | LangGraph native |
| **Learning Curve** | Medium-Hard | Medium | Easy (if using LangGraph) |
| **Best For** | Complex, long-running workflows | AWS-native event-driven agents | LangGraph agent deployment |

```python
# Agent Runtime Examples (Conceptual)

# --- Temporal.io: Durable Agent Workflow ---
# pip install temporalio

"""
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker
from datetime import timedelta

# Each agent step is an "activity" - automatically retried and persisted
@activity.defn
async def research_step(query: str) -> str:
    \"\"\"Call LLM to research a topic. If this crashes, Temporal retries it.\"\"\"
    # Your LLM call here
    return f"Research results for: {query}"

@activity.defn
async def write_step(research: str) -> str:
    \"\"\"Write content based on research. Durable - survives worker restarts.\"\"\"
    # Your LLM call here
    return f"Written content based on: {research}"

@activity.defn
async def review_step(draft: str) -> str:
    \"\"\"Review and refine the draft.\"\"\"
    return f"Reviewed: {draft}"

# The workflow orchestrates the agent pipeline
@workflow.defn
class ResearchAgentWorkflow:
    @workflow.run
    async def run(self, query: str) -> str:
        # Step 1: Research (retries up to 3 times on failure)
        research = await workflow.execute_activity(
            research_step, query,
            start_to_close_timeout=timedelta(seconds=60),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )
        # Step 2: Write (if this fails, step 1 is NOT re-run)
        draft = await workflow.execute_activity(
            write_step, research,
            start_to_close_timeout=timedelta(seconds=60)
        )
        # Step 3: Review
        final = await workflow.execute_activity(
            review_step, draft,
            start_to_close_timeout=timedelta(seconds=60)
        )
        return final

# Start the workflow
async def main():
    client = await Client.connect("localhost:7233")
    result = await client.execute_workflow(
        ResearchAgentWorkflow.run, "AI agent frameworks 2026",
        id="research-agent-001",
        task_queue="agent-tasks"
    )
    print(result)
"""

# --- AWS Step Functions: Serverless Agent Workflow ---
# Defined as a state machine in JSON/YAML, executed serverlessly on AWS.

"""
# step_functions_definition.json
{
    "Comment": "Research Agent Workflow",
    "StartAt": "Research",
    "States": {
        "Research": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:123456789:function:research-agent",
            "Next": "WriteOrRetry",
            "Retry": [{"ErrorEquals": ["States.ALL"], "MaxAttempts": 3}]
        },
        "WriteOrRetry": {
            "Type": "Choice",
            "Choices": [
                {
                    "Variable": "$.quality_score",
                    "NumericGreaterThan": 0.7,
                    "Next": "Write"
                }
            ],
            "Default": "Research"
        },
        "Write": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:123456789:function:write-agent",
            "Next": "Review"
        },
        "Review": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:123456789:function:review-agent",
            "End": true
        }
    }
}
"""

print("✅ Agent runtime patterns shown (conceptual)")
print("📦 Temporal: pip install temporalio | https://temporal.io")
print("📦 Step Functions: AWS Console or aws-cdk | https://aws.amazon.com/step-functions/")
```

## 🎯 Knowledge Check

**Q1:** Name three fully managed agent API services and their vendor lock-in trade-offs.  
**Q2:** When should you choose LangGraph over the OpenAI Agents SDK?  
**Q3:** What are MCP and A2A, and why do they matter for multi-vendor agent architectures?  
**Q4:** How does memory work in LangChain agents?  
**Q5:** What is the Microsoft Agent Framework and how does it relate to AutoGen?  
**Q6:** When should you use LlamaIndex agents instead of LangChain agents?  
**Q7:** What is the difference between an agent framework and an agent runtime? Why do you need both in production?

<details>
<summary>Click for answers</summary>

**A1:** Anthropic Managed Agents (Claude-only), AWS Bedrock Agents (multi-model on Bedrock), Azure AI Agent Service (multi-model on Azure). Lock-in increases with vendor-specific tool integrations.  
**A2:** LangGraph when you need complex stateful workflows with cycles, conditional branching, human-in-the-loop checkpoints, or persistent state. OpenAI Agents SDK for lightweight multi-agent handoffs with minimal boilerplate.  
**A3:** MCP (Model Context Protocol) standardizes how agents connect to tools/resources - broadly adopted across Anthropic, OpenAI, Google, Microsoft. A2A (Agent-to-Agent) enables agents to discover and delegate tasks to other agents - early but growing adoption. Both reduce vendor lock-in.  
**A4:** Memory stores conversation history and passes it to the agent as context. Strategies include buffer (full history), summary (compressed), window (last k turns), and vector store (semantic retrieval).  
**A5:** Microsoft Agent Framework is the production-grade successor to AutoGen. It unifies multi-agent orchestration (from AutoGen) with planning, tools, and memory into a single Python + .NET SDK. AutoGen is now merging into it.  
**A6:** Choose LlamaIndex when your agent is primarily retrieval-focused - querying multiple data sources (vector stores, knowledge graphs, SQL), building RAG-heavy pipelines, or needing deep index integration. LangChain has a larger general tool ecosystem.  
**A7:** A framework defines *what* an agent does (tools, planning, memory). A runtime defines *how* it executes reliably - durable execution, retries, scheduling, crash recovery. Temporal.io and AWS Step Functions are runtimes. In production, you combine both: e.g., a LangGraph agent running on Temporal for durability.  
</details>

## 🚀 Next Steps

1. Complete the **Agent Framework Challenge**
2. Read Notebook 5: **Multi-Agent Systems**
3. Read Notebook 6: **MCP (Model Context Protocol)**
4. Read Notebook 7: **OpenAI Agents SDK + LangGraph deep dive**
5. Build a production agent with your chosen framework
6. Experiment with LangGraph for complex workflows

---

**Great work! You now have a complete map of the 2026 agent framework landscape! 🎉**
