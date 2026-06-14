---
title: "8. OpenAI Agents SDK Langgraph"
sidebar_label: "8. OpenAI Agents SDK Langgraph"
sidebar_position: 9
format: "md"
---
# OpenAI Agents SDK + LangGraph 1.0
## Production Agent Frameworks

**Module 15 · Notebook 7**

---

Two frameworks dominate production agent deployments in 2025:

| Framework | Released | Best for |
|-----------|----------|----------|
| **OpenAI Agents SDK** | March 2025 | Lightweight, multi-agent handoffs, voice |
| **LangGraph 1.0** | October 2025 | Complex state machines, human-in-the-loop, persistence |

This notebook covers both frameworks with real working code, then gives you a decision guide for choosing between them.

## Table of Contents

**Section A - OpenAI Agents SDK**
1. What is the Agents SDK (and how it differs from Swarm)
2. Core primitives: Agent, Runner, Handoffs, Guardrails, Memory
3. Installation
4. Creating a basic agent
5. Multi-agent handoffs
6. Guardrails (input/output validation)
7. Tool use with the Agents SDK
8. MCP integration
9. Built-in tracing and observability
10. Realtime voice agents
11. Provider-agnostic usage (Claude, Gemini)

**Section B - LangGraph 1.0**
12. What changed in 1.0
13. StateGraph with typed annotations
14. LangGraph Supervisor (hierarchical multi-agent)
15. LangMem SDK for long-term memory
16. Built-in persistence (SQLite, PostgreSQL)
17. Human-in-the-loop with `interrupt()`
18. Dynamic tool calling
19. Streaming tokens

**Section C - Comparison**
20. LangGraph vs OpenAI Agents SDK
21. Production deployment patterns

---
# Section A - OpenAI Agents SDK

## 1. What is the Agents SDK?

OpenAI released the **Agents SDK** in March 2025 as the production-ready successor to the experimental [Swarm](https://github.com/openai/swarm) library.

**Key improvements over Swarm:**
- First-class guardrails (parallel validation of inputs/outputs)
- Built-in tracing via OpenAI's trace dashboard
- Native MCP client support
- Realtime voice agent support
- Provider-agnostic via LiteLLM
- Memory primitive (in-context + persistent)

**Design philosophy:** keep it simple. The SDK has very few abstractions - Agent, Runner, and optionally Handoffs + Guardrails. You write Python functions; the SDK handles the agentic loop.

---
## 2. Core Primitives

```mermaid
flowchart TB
    subgraph R[Runner - orchestrates the agentic loop]
        A[Agent A
tools
guardrails
memory]
        B[Agent B
tools
guardrails
memory]
        A -->|handoff| B
    end
```

| Primitive | Description |
|-----------|-------------|
| **Agent** | An LLM with instructions, tools, handoffs, and guardrails |
| **Runner** | Runs the agentic loop (sync or async); returns a `RunResult` |
| **Handoff** | Transfers control from one agent to another |
| **Guardrail** | Async validation that runs in parallel with the agent |
| **Memory** | In-context list or persistent store of conversation facts |

---
## 3. Installation

The `openai-agents` package provides a lightweight, opinionated framework for building multi-agent systems on top of the OpenAI API. Its core abstractions are deliberately minimal: `Agent` (an LLM with instructions, tools, and handoff targets), `Runner` (the execution engine that manages the agent loop), and `function_tool` (a decorator that converts any Python function into a callable tool with auto-generated JSON Schema). The optional `[voice]` extra adds real-time speech-to-text and text-to-speech pipeline support.

```python
# Install the OpenAI Agents SDK
%pip install openai-agents --quiet

# Optional: install with voice support
# %pip install openai-agents[voice] --quiet

# Verify
import agents
print(f"OpenAI Agents SDK installed")
print(f"Key classes: Agent, Runner, function_tool, handoff, input_guardrail, output_guardrail")
```

---
## 4. Creating a Basic Agent

An `Agent` in the OpenAI Agents SDK is a configuration object that bundles an LLM model, system instructions, tools, and handoff targets into a single deployable unit. The `Runner.run()` method executes the agent loop: it sends the user message plus the agent's instructions to the model, processes any tool calls, and repeats until the model produces a final text response. The returned `RunResult` object provides full introspection into every step -- messages, tool calls, raw API responses, and guardrail outcomes -- making debugging straightforward.

```python
import asyncio
import os
from agents import Agent, Runner

# The simplest possible agent
agent = Agent(
    name="assistant",
    instructions="You are a helpful assistant. Be concise and accurate.",
    model="gpt-4o"
)

async def run_basic_agent():
    result = await Runner.run(agent, "What is the capital of France?")
    print("Final output:", result.final_output)
    return result

# Run (requires OPENAI_API_KEY)
# result = asyncio.run(run_basic_agent())

print("Basic agent created:")
print(f"  Name        : {agent.name}")
print(f"  Model       : {agent.model}")
print(f"  Instructions: {agent.instructions[:50]}...")
print("\nTo run: asyncio.run(run_basic_agent())  # requires OPENAI_API_KEY")
```

```python
# The RunResult object contains everything about the run
from agents import Agent, Runner, RunResult

RUN_RESULT_ANATOMY = """
RunResult object:
  .final_output       -> str   - The last text response from the agent
  .messages           -> list  - Full conversation history
  .new_messages       -> list  - Only messages added during this run
  .last_agent         -> Agent - Which agent produced the final output
  .tool_calls         -> list  - All tool calls made during the run
  .raw_responses      -> list  - Raw API responses for each LLM call
  .input_guardrail_results   -> list  - Results from input guardrails
  .output_guardrail_results  -> list  - Results from output guardrails
"""
print(RUN_RESULT_ANATOMY)

# Sync API (for scripts and notebooks)
SYNC_USAGE = """
# Synchronous usage (wraps asyncio internally)
from agents import Agent, Runner

agent = Agent(name="assistant", instructions="...", model="gpt-4o")

# Single turn
result = Runner.run_sync(agent, "Hello!")
print(result.final_output)

# Streaming
async def stream_demo():
    async with Runner.run_streamed(agent, "Tell me a story") as stream:
        async for event in stream.stream_events():
            if event.type == "raw_response_event":
                print(event.data.delta, end="", flush=True)
"""
print(SYNC_USAGE)
```

---
## 5. Multi-Agent Handoffs

Handoffs are the Agents SDK's mechanism for **delegation between specialized agents**. When a triage agent determines that a user request falls outside its expertise, it invokes a `handoff()` function that transfers control to a specialist agent (billing, technical support, etc.). The handoff appears as a tool call to the LLM -- the triage agent's model sees `transfer_to_billing` as an available function and calls it when the conversation matches billing-related intent. The Runner then seamlessly switches to the target agent, preserving the full conversation history so the specialist has complete context.

```python
from agents import Agent, Runner, handoff

# Specialist agents
billing_agent = Agent(
    name="billing-specialist",
    instructions="""
    You are a billing specialist. You handle:
    - Invoice questions
    - Payment issues
    - Subscription changes
    - Refund requests
    Always greet the customer when taking over from another agent.
    """,
    model="gpt-4o"
)

technical_agent = Agent(
    name="technical-support",
    instructions="""
    You are a technical support specialist. You handle:
    - Bug reports
    - Integration issues
    - API questions
    - Performance problems
    Ask clarifying questions to reproduce issues.
    """,
    model="gpt-4o"
)

# Triage agent - decides which specialist to hand off to
triage_agent = Agent(
    name="triage",
    instructions="""
    You are a customer support triage agent. Classify incoming requests
    and hand them off to the appropriate specialist:
    - Billing issues -> billing-specialist
    - Technical issues -> technical-support
    Do not try to solve the issue yourself; always hand off.
    """,
    model="gpt-4o",
    handoffs=[
        handoff(billing_agent),
        handoff(technical_agent)
    ]
)

print("Multi-agent system created:")
print(f"  Triage agent handoffs: {[h.agent_name for h in triage_agent.handoffs]}")
print("\nUsage:")
print("  result = await Runner.run(triage_agent, 'I have a problem with my invoice')")
print("  # triage_agent hands off to billing_agent automatically")
```

```python
# Handoff with custom message (give context to the receiving agent)
from agents import Agent, Runner, handoff

def on_handoff_to_billing(ctx) -> None:
    """Called when triage hands off to billing - log for observability."""
    print(f"[HANDOFF] Transferring to billing agent")

billing_agent_v2 = Agent(
    name="billing-specialist",
    instructions="You are a billing specialist. Handle all payment and invoice questions.",
    model="gpt-4o"
)

triage_agent_v2 = Agent(
    name="triage",
    instructions="Classify and hand off customer requests.",
    model="gpt-4o",
    handoffs=[
        handoff(
            billing_agent_v2,
            # Override the tool description the LLM sees
            tool_name_override="transfer_to_billing",
            tool_description_override="Transfer the customer to the billing team for payment and invoice issues.",
            on_handoff=on_handoff_to_billing
        )
    ]
)

print("Custom handoff configured:")
print(f"  Tool name: transfer_to_billing")
print(f"  Callback: on_handoff_to_billing")
```

---
## 6. Guardrails (Input and Output Validation)

Guardrails provide a declarative safety layer that runs **in parallel** with the main agent, adding negligible latency. An `@input_guardrail` inspects the user's message before the agent processes it (blocking off-topic requests, detecting prompt injection, enforcing content policies), while an `@output_guardrail` validates the agent's response before returning it to the user (checking for PII leakage, code quality, factual consistency). Each guardrail is itself a lightweight agent -- typically backed by a cheap model like `gpt-4o-mini` -- that returns a structured Pydantic output with a `tripwire_triggered` boolean. If any guardrail trips, the Runner raises an exception rather than returning the unsafe output.

```python
from agents import Agent, Runner, input_guardrail, output_guardrail
from agents import GuardrailFunctionOutput, RunContextWrapper
from pydantic import BaseModel

# ── Input guardrail: block off-topic requests ─────────────────────────────────

class TopicCheckOutput(BaseModel):
    is_on_topic: bool
    reason: str

# The guardrail itself runs as a fast, cheap model check
topic_checker = Agent(
    name="topic-checker",
    instructions="""
    Check if the user's message is about software engineering or coding.
    Return is_on_topic=True only for coding/software questions.
    """,
    model="gpt-4o-mini",  # use a cheap model for guardrails
    output_type=TopicCheckOutput
)

@input_guardrail
async def topic_guardrail(
    ctx: RunContextWrapper,
    agent: Agent,
    input: str
) -> GuardrailFunctionOutput:
    """Block requests that are not about software engineering."""
    result = await Runner.run(topic_checker, input, context=ctx.context)
    check: TopicCheckOutput = result.final_output
    
    return GuardrailFunctionOutput(
        output_info=check,
        tripwire_triggered=not check.is_on_topic
    )

# ── Output guardrail: ensure no code style violations ─────────────────────────

class CodeQualityOutput(BaseModel):
    passes: bool
    issues: list[str]

code_reviewer = Agent(
    name="code-reviewer",
    instructions="Check if the response contains any Python 2 syntax (print statements without parens, etc.).",
    model="gpt-4o-mini",
    output_type=CodeQualityOutput
)

@output_guardrail
async def code_quality_guardrail(
    ctx: RunContextWrapper,
    agent: Agent,
    output: str
) -> GuardrailFunctionOutput:
    """Ensure code suggestions use Python 3 syntax."""
    result = await Runner.run(code_reviewer, f"Check this response: {output}", context=ctx.context)
    check: CodeQualityOutput = result.final_output
    
    return GuardrailFunctionOutput(
        output_info=check,
        tripwire_triggered=not check.passes
    )

# ── Agent with guardrails ─────────────────────────────────────────────────────
coding_assistant = Agent(
    name="coding-assistant",
    instructions="You are an expert Python coding assistant. Always use Python 3 syntax.",
    model="gpt-4o",
    input_guardrails=[topic_guardrail],
    output_guardrails=[code_quality_guardrail]
)

print("Agent with guardrails configured:")
print(f"  Input guardrails : topic_guardrail (blocks off-topic requests)")
print(f"  Output guardrails: code_quality_guardrail (ensures Python 3)")
print("\nGuardrails run in PARALLEL with the main agent for minimal latency.")
```

---
## 7. Tool Use with the Agents SDK

The `@function_tool` decorator converts any typed Python function into a tool the agent can call. The SDK automatically generates a JSON Schema from the function's type hints and docstring -- parameter names, types, descriptions, and required fields are all inferred. At runtime, when the LLM returns a tool call, the Runner deserializes the JSON arguments, invokes the Python function, and feeds the result back to the model as a tool response message. This eliminates the manual schema authoring required by raw OpenAI function calling.

```python
from agents import Agent, Runner, function_tool
import json
from datetime import datetime

# Decorate regular Python functions as tools
@function_tool
def get_weather(city: str, units: str = "celsius") -> dict:
    """
    Get current weather for a city.
    
    Args:
        city: Name of the city
        units: Temperature units - 'celsius' or 'fahrenheit'
    """
    # Mock - replace with real weather API
    return {
        "city": city,
        "temperature": 22 if units == "celsius" else 72,
        "condition": "Partly cloudy",
        "humidity": 65
    }

@function_tool
def search_flights(origin: str, destination: str, date: str) -> list[dict]:
    """
    Search for available flights.
    
    Args:
        origin: IATA airport code (e.g. SFO)
        destination: IATA airport code (e.g. JFK)
        date: Travel date in YYYY-MM-DD format
    """
    # Mock
    return [
        {"flight": "AA101", "departure": "08:00", "arrival": "16:30", "price": 320},
        {"flight": "UA202", "departure": "12:00", "arrival": "20:45", "price": 285},
    ]

@function_tool
def book_flight(flight_number: str, passenger_name: str) -> dict:
    """
    Book a flight for a passenger.
    
    Args:
        flight_number: The flight identifier (e.g. AA101)
        passenger_name: Full name of the passenger
    """
    confirmation = f"CONF-{hash(flight_number + passenger_name) % 99999:05d}"
    return {"confirmation": confirmation, "flight": flight_number, "passenger": passenger_name}

# Agent with tools
travel_agent = Agent(
    name="travel-assistant",
    instructions="""
    You are a helpful travel assistant. Help users:
    1. Check weather at their destination
    2. Find available flights
    3. Book flights when asked
    Always check the weather before recommending a trip.
    """,
    model="gpt-4o",
    tools=[get_weather, search_flights, book_flight]
)

print("Travel agent created with tools:")
for tool in travel_agent.tools:
    print(f"  - {tool.name}: {tool.description[:60]}")
```

```python
# Test tool invocation directly (without LLM)
weather_result = get_weather.on_invoke_tool(None, json.dumps({"city": "Paris", "units": "celsius"}))
print("Direct tool call result:", weather_result)

flights_result = search_flights.on_invoke_tool(None, json.dumps({"origin": "SFO", "destination": "JFK", "date": "2025-12-01"}))
print("Flights result:", flights_result)
```

---
## 8. MCP Integration with the Agents SDK

The Agents SDK includes native MCP client support through `MCPServerStdio` and `MCPServerHttp` classes. When you pass MCP servers to an agent's `mcp_servers` parameter, the SDK automatically discovers all tools exposed by those servers and makes them available alongside the agent's local `@function_tool` functions. This means an agent can seamlessly use both local Python tools and remote MCP tools (filesystem access, database queries, web search) in a single reasoning loop, without any additional glue code.

```python
# The Agents SDK has a built-in MCP client
# Use MCPServerStdio or MCPServerHttp to connect to any MCP server

MCP_INTEGRATION_CODE = """
from agents import Agent, Runner
from agents.mcp import MCPServerStdio, MCPServerHttp
import asyncio

async def agent_with_mcp():
    # Connect to a local STDIO MCP server
    async with MCPServerStdio(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
    ) as fs_server:
        
        # Connect to a remote HTTP MCP server
        async with MCPServerHttp(url="http://localhost:8000/mcp") as remote_server:
            
            agent = Agent(
                name="mcp-agent",
                instructions="Use the available MCP tools to help the user.",
                model="gpt-4o",
                mcp_servers=[fs_server, remote_server]
                # Tools from MCP servers are automatically listed and made available!
            )
            
            result = await Runner.run(
                agent,
                "List the files in /tmp and show me the contents of any .txt files"
            )
            print(result.final_output)

asyncio.run(agent_with_mcp())
"""

print("MCP integration with Agents SDK:")
print(MCP_INTEGRATION_CODE)

print("Key insight: MCP tools appear as regular tools to the agent.")
print("The SDK handles the MCP client lifecycle and tool listing automatically.")
```

---
## 9. Built-in Tracing and Observability

The Agents SDK traces every run by default -- every LLM call, tool invocation, handoff, and guardrail result is recorded and viewable at `platform.openai.com/traces`. The `custom_span` context manager lets you add application-specific metadata (user IDs, session IDs, business metrics) to traces, while `RunConfig` groups related traces under workflow names for dashboard filtering. In production, this zero-config observability eliminates the need to integrate separate tracing libraries like LangSmith or OpenTelemetry for basic agent debugging.

```python
from agents import Agent, Runner
from agents.tracing import get_current_span, custom_span
import agents.tracing as tracing

# Tracing is ON by default - all runs are traced to platform.openai.com/traces
# Disable tracing:
# tracing.disable_tracing()

# Add custom metadata to traces
TRACING_EXAMPLE = """
from agents import Agent, Runner
from agents.tracing import custom_span, get_current_span

# Custom spans appear in the trace timeline
async def run_with_tracing():
    agent = Agent(name="demo", instructions="Be helpful.", model="gpt-4o")
    
    with custom_span("my-business-logic") as span:
        span.set_attribute("user_id", "user-123")
        span.set_attribute("session_id", "sess-456")
        
        result = await Runner.run(
            agent,
            "Hello!",
            run_config=RunConfig(
                workflow_name="customer-support",   # Groups traces in the dashboard
                trace_metadata={"env": "production", "version": "2.1.0"}
            )
        )
    
    # Trace includes:
    # - All LLM calls with inputs, outputs, tokens, latency
    # - All tool calls with inputs and results
    # - Handoffs between agents
    # - Guardrail results
    # - Your custom spans
    return result
"""

print("Tracing is enabled by default. All runs appear at platform.openai.com/traces")
print()
print("What gets traced automatically:")
for item in [
    "Every LLM call (input, output, tokens, latency)",
    "Every tool call (name, input, output)",
    "Handoffs between agents",
    "Guardrail results (triggered or passed)",
    "Full conversation context"
]:
    print(f"  - {item}")

print()
print(TRACING_EXAMPLE)
```

---
## 10. Realtime Voice Agents

The `VoicePipeline` class chains speech-to-text, agent reasoning, and text-to-speech into a single streaming pipeline. Audio input (16-bit PCM at 24kHz) flows through Whisper or the OpenAI Realtime API for transcription, the transcribed text is processed by a standard `Agent` (with full access to tools and handoffs), and the response is streamed back as synthesized audio. The same agent definition works for both text and voice interactions -- only the pipeline wrapper changes -- which means you can develop and test agent logic in text mode and deploy it as a voice assistant without code changes.

```python
# Voice agent pattern using the Agents SDK + OpenAI Realtime API
# Install: pip install openai-agents[voice]

VOICE_AGENT_CODE = """
# pip install openai-agents[voice]
from agents import Agent
from agents.voice import VoicePipeline, AudioInput, AudioOutput
import numpy as np

# Regular agent - works for both text and voice!
voice_agent = Agent(
    name="voice-assistant",
    instructions="You are a helpful voice assistant. Keep answers brief (under 30 words).",
    model="gpt-4o"
)

async def voice_demo():
    # VoicePipeline handles: audio -> STT -> Agent -> TTS -> audio
    pipeline = VoicePipeline(workflow=SingleAgentVoiceWorkflow(voice_agent))
    
    # Feed microphone audio (numpy array, 16-bit PCM, 24kHz)
    audio_input = AudioInput(buffer=np.zeros(24000, dtype=np.int16))  # 1 second of silence
    
    async with pipeline.run(audio_input) as result:
        async for event in result.stream():
            if event.type == "voice_stream_event_audio":
                # Play audio chunk
                audio_data = event.data  # numpy array
                # send to speakers...
                pass
            elif event.type == "voice_stream_event_lifecycle":
                print(f"[Lifecycle] {event.event}")
"""

print("Voice agent pattern (requires: pip install openai-agents[voice])")
print()
print("Voice pipeline stages:")
stages = [
    "Microphone audio (PCM 16-bit, 24kHz)",
    "Speech-to-Text (Whisper or Realtime API)",
    "Agent loop (same as text agents)",
    "Text-to-Speech (TTS-1 or Realtime API)",
    "Audio output to speakers"
]
for i, stage in enumerate(stages, 1):
    print(f"  {i}. {stage}")

print()
print(VOICE_AGENT_CODE)
```

---
## 11. Provider-Agnostic Usage (Claude, Gemini)

Despite being an OpenAI product, the Agents SDK supports any LLM provider through the `OpenAIChatCompletionsModel` wrapper (for OpenAI-compatible APIs) or the `LitellmModel` adapter (for providers with non-standard APIs). This lets you use Claude, Gemini, Mistral, or even local Ollama models while retaining the SDK's agent loop, handoffs, guardrails, and tracing. You can even mix models within a single multi-agent system -- using GPT-4o for expensive reasoning tasks and GPT-4o-mini for cheap guardrail checks -- optimizing the cost-quality trade-off at the agent level.

```python
# The Agents SDK works with any OpenAI-compatible API via LiteLLM
# pip install litellm

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents import set_default_openai_client

PROVIDER_AGNOSTIC_CODE = """
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

# ── Use with Claude (via LiteLLM proxy) ───────────────────────────────────────
claude_client = AsyncOpenAI(
    api_key=os.environ["ANTHROPIC_API_KEY"],
    base_url="https://api.anthropic.com/v1"  # LiteLLM or direct Anthropic compat endpoint
)

claude_agent = Agent(
    name="claude-assistant",
    instructions="You are a helpful assistant.",
    model=OpenAIChatCompletionsModel(
        model="claude-opus-4-6",
        openai_client=claude_client
    )
)

# ── Use with Gemini (via LiteLLM) ─────────────────────────────────────────────
import litellm
from agents.extensions.models.litellm_model import LitellmModel

gemini_agent = Agent(
    name="gemini-assistant",
    instructions="You are a helpful assistant.",
    model=LitellmModel(model="gemini/gemini-2.0-flash")
)

# ── Mix models in a multi-agent system ────────────────────────────────────────
# Use GPT-4o for expensive reasoning, GPT-4o-mini for cheap guardrails
main_agent = Agent(
    name="main",
    instructions="Handle complex reasoning tasks.",
    model="gpt-4o",
    input_guardrails=[fast_guardrail]  # guardrail agent uses gpt-4o-mini
)
"""

print("Provider-agnostic Agents SDK patterns:")
print()
print("Supported providers via LiteLLM:")
providers = [
    ("OpenAI",     "gpt-4o, gpt-4o-mini, o1, o3"),
    ("Anthropic",  "claude-opus-4-6, claude-sonnet-4-6, claude-haiku-3-5"),
    ("Google",     "gemini-2.0-flash, gemini-2.0-pro"),
    ("Mistral",    "mistral-large, mistral-small"),
    ("Ollama",     "llama3.2, qwen2.5-coder (local!)"),
    ("Azure",      "gpt-4o deployed on Azure OpenAI"),
]
for provider, models in providers:
    print(f"  {provider:<12} {models}")

print()
print(PROVIDER_AGNOSTIC_CODE)
```

---
# Section B - LangGraph 1.0

## 12. What Changed in LangGraph 1.0

LangGraph 1.0 was released in **October 2025** as the first stable release. The key promises:
- **No breaking changes until LangGraph 2.0**
- All 0.x deprecation warnings resolved
- Stable API for `StateGraph`, `interrupt()`, persistence, streaming
- `langgraph-supervisor` and `langgraph-swarm` as first-party packages
- LangMem SDK for production memory management

### Core concepts

```mermaid
flowchart TD
    SG[StateGraph]
    SG --> N[Nodes - Python functions that transform state]
    SG --> E[Edges - direct or conditional routing]
    SG --> S[State - typed dict persisted across turns]
    SG --> C[Checkpointer - SQLite or PostgreSQL or Redis]
```

LangGraph is **graph-based** - you model your agent as a directed graph where:
- **Nodes** = processing steps (LLM calls, tool calls, human input)
- **Edges** = transitions between steps (can be conditional)
- **State** = shared memory that flows through the graph

---
## 13. StateGraph with Typed Annotations

`StateGraph` is LangGraph's core abstraction: a directed graph where nodes are Python functions that transform a shared typed state dictionary. The `MessagesState` convenience class provides a pre-configured state with a `messages` key that uses `operator.add` as its reducer, meaning new messages are appended rather than replacing existing ones. For custom workflows, you define your own `TypedDict` with `Annotated` fields to control how each state key merges updates -- `operator.add` for append semantics, or plain assignment for last-write-wins. This typed state contract catches bugs at definition time rather than runtime.

```python
%pip install langgraph langchain-openai langchain-anthropic --quiet
```

```python
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from typing import Annotated
import operator

# LangGraph 1.0: MessagesState is the standard starting point
# It's a TypedDict with a 'messages' key that auto-appends

# ── Simple single-agent graph ─────────────────────────────────────────────────

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def call_agent(state: MessagesState) -> dict:
    """Node: calls the LLM with the current message history."""
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}  # MessagesState auto-appends

# Build the graph
graph_builder = StateGraph(MessagesState)
graph_builder.add_node("agent", call_agent)
graph_builder.add_edge(START, "agent")
graph_builder.add_edge("agent", END)

simple_graph = graph_builder.compile()

print("Simple LangGraph agent created")
print(f"Nodes: {list(simple_graph.nodes.keys())}")

# Usage:
# result = simple_graph.invoke({"messages": [HumanMessage(content="Hello!")]})
# print(result["messages"][-1].content)
```

```python
# Custom state with typed annotations
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage
import operator

# Define custom state - use Annotated with operators to control merging
class ResearchState(TypedDict):
    # messages: new messages are APPENDED (not replaced)
    messages: Annotated[list[BaseMessage], operator.add]
    # topic: last write wins
    topic: str
    # search_results: new results are APPENDED
    search_results: Annotated[list[str], operator.add]
    # final_report: last write wins
    final_report: str
    # iteration: numeric - can use custom reducer
    iteration: int

def research_node(state: ResearchState) -> dict:
    """Simulate a research step."""
    topic = state.get("topic", "unknown")
    iteration = state.get("iteration", 0)
    result = f"Research finding {iteration + 1} about: {topic}"
    return {
        "search_results": [result],
        "iteration": iteration + 1
    }

def should_continue(state: ResearchState) -> str:
    """Conditional edge: continue researching or write report?"""
    return "write_report" if state.get("iteration", 0) >= 3 else "research"

def write_report(state: ResearchState) -> dict:
    """Synthesize all research into a final report."""
    findings = "\n".join(state.get("search_results", []))
    report = f"# Report on {state['topic']}\n\n{findings}"
    return {"final_report": report}

# Build the graph
rg = StateGraph(ResearchState)
rg.add_node("research", research_node)
rg.add_node("write_report", write_report)

rg.add_edge(START, "research")
rg.add_conditional_edges("research", should_continue, ["research", "write_report"])
rg.add_edge("write_report", END)

research_graph = rg.compile()

# Run it
result = research_graph.invoke({"topic": "MCP protocol", "iteration": 0, "search_results": [], "final_report": "", "messages": []})
print(f"Iterations: {result['iteration']}")
print(f"Findings: {len(result['search_results'])}")
print(f"\nFinal report:\n{result['final_report']}")
```

---
## 14. LangGraph Supervisor (Hierarchical Multi-Agent)

The `langgraph-supervisor` package provides a pre-built hierarchical multi-agent pattern where a supervisor agent receives user requests, delegates subtasks to specialist agents (`create_react_agent` instances), collects results, and synthesizes a final answer. Each specialist has its own tools and instructions, and the supervisor's prompt defines the routing logic. The `create_supervisor()` function compiles this into a single `StateGraph` where the supervisor node routes to specialist nodes via conditional edges, and specialists return results that flow back to the supervisor for synthesis or further delegation.

```python
%pip install langgraph-supervisor --quiet
```

```python
from langgraph_supervisor import create_supervisor
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

llm = ChatOpenAI(model="gpt-4o", temperature=0)

# ── Define specialist agents ──────────────────────────────────────────────────

@tool
def search_web(query: str) -> str:
    """Search the web for information."""
    return f"[Web search results for: {query}] Found 5 relevant articles."

@tool
def python_repl(code: str) -> str:
    """Execute Python code and return the output."""
    # In production: use a sandboxed executor like E2B
    try:
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            exec(code, {})
        return buf.getvalue() or "(no output)"
    except Exception as e:
        return f"Error: {e}"

@tool
def write_file(path: str, content: str) -> str:
    """Write content to a file."""
    return f"Written {len(content)} chars to {path}"

# Create specialist agents
research_agent = create_react_agent(
    llm,
    tools=[search_web],
    name="researcher",
    prompt="You are a research specialist. Use search tools to find accurate information."
)

coding_agent = create_react_agent(
    llm,
    tools=[python_repl],
    name="coder",
    prompt="You are a Python expert. Write and execute code to solve problems."
)

writer_agent = create_react_agent(
    llm,
    tools=[write_file],
    name="writer",
    prompt="You are a technical writer. Create clear, structured reports from provided information."
)

# Create the supervisor - it routes tasks to specialists
supervisor = create_supervisor(
    agents=[research_agent, coding_agent, writer_agent],
    model=llm,
    prompt="""
    You are a supervisor managing a team of specialists:
    - researcher: for finding information on the web
    - coder: for writing and running Python code
    - writer: for creating final reports
    
    Break down complex tasks and delegate to the right specialist.
    Collect results and synthesize a final answer.
    """
).compile()

print("LangGraph Supervisor created with 3 specialist agents")
print("Agents: researcher, coder, writer")
print("\nUsage:")
print("  result = supervisor.invoke({'messages': [HumanMessage(content='...')]})")
```

```python
# Test the supervisor with a real task (no LLM needed for structure demo)
from langchain_core.messages import HumanMessage

# Demonstrate the python_repl tool directly
result = python_repl.invoke({"code": """
import math
data = [22, 35, 41, 28, 55, 19, 33]
mean = sum(data) / len(data)
variance = sum((x - mean)**2 for x in data) / len(data)
print(f"Mean: {mean:.2f}")
print(f"Std Dev: {math.sqrt(variance):.2f}")
print(f"Min: {min(data)}, Max: {max(data)}")
"""})
print("Python REPL tool output:")
print(result)

# Demonstrate search tool
search_result = search_web.invoke({"query": "LangGraph 1.0 release features"})
print(f"\nSearch result: {search_result}")

# In a real run:
# result = supervisor.invoke({"messages": [HumanMessage(content="Research LangGraph 1.0 features, compute the number of weeks since its release, and write a summary report.")]})
# print(result["messages"][-1].content)
```

---
## 15. LangMem SDK for Long-Term Memory

LangMem extends LangGraph agents with persistent, cross-conversation memory. The architecture follows a three-node pattern: **load_memories** retrieves relevant facts from a vector store using semantic search over the current query, **agent** runs the LLM with retrieved memories injected as system context, and **save_memories** uses a cheap model to extract new facts from the conversation and store them. The `create_memory_store_manager` function handles fact extraction, deduplication, and storage automatically. Memory is namespaced by user ID, so each user accumulates a personalized knowledge base that grows across sessions.

```python
%pip install langmem --quiet
```

```python
# LangMem SDK: extract, store, and retrieve memories across conversations
from langmem import create_memory_store_manager
from langgraph.store.memory import InMemoryStore
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# ── Set up memory store ───────────────────────────────────────────────────────
# InMemoryStore for development; use PostgresStore in production
store = InMemoryStore(
    index={
        "embed": "openai:text-embedding-3-small",
        "dims": 1536
    }
)

llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Memory manager - extracts important facts from conversations
memory_manager = create_memory_store_manager(
    "openai:gpt-4o-mini",  # Use cheap model for memory extraction
    namespace=("user", "{user_id}"),  # Namespace by user
)

MEMORY_CODE = """
# Full memory-enabled agent
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.store.memory import InMemoryStore
from langmem import create_memory_store_manager
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

store = InMemoryStore(index={"embed": "openai:text-embedding-3-small", "dims": 1536})
llm = ChatOpenAI(model="gpt-4o")
memory_manager = create_memory_store_manager(
    "openai:gpt-4o-mini",
    namespace=("user", "{user_id}")
)

def load_memories(state, config, *, store):
    user_id = config["configurable"]["user_id"]
    # Search for relevant memories given the current conversation
    memories = store.search(("user", user_id), query=state["messages"][-1].content, limit=5)
    memory_text = "\\n".join(m.value["content"] for m in memories)
    return {
        "messages": [SystemMessage(content=f"User memories:\\n{memory_text}")] + state["messages"]
    }

def call_llm(state, config, *, store):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

def save_memories(state, config, *, store):
    # Extract and store new facts from this conversation
    memory_manager.invoke(state, config, store=store)
    return {}

graph = StateGraph(MessagesState)
graph.add_node("load_memories", load_memories)
graph.add_node("agent", call_llm)
graph.add_node("save_memories", save_memories)

graph.add_edge(START, "load_memories")
graph.add_edge("load_memories", "agent")
graph.add_edge("agent", "save_memories")
graph.add_edge("save_memories", END)

memory_agent = graph.compile(store=store)

# First conversation
memory_agent.invoke(
    {"messages": [HumanMessage(content="My name is Alice and I prefer dark mode.")]},
    config={"configurable": {"user_id": "alice"}}
)

# Later conversation - agent remembers!
result = memory_agent.invoke(
    {"messages": [HumanMessage(content="What do you know about my preferences?")]},
    config={"configurable": {"user_id": "alice"}}
)
# Output includes: "You prefer dark mode."
"""

print("LangMem SDK memory architecture:")
print()
for step in [
    "1. load_memories: retrieve relevant facts from the store (semantic search)",
    "2. agent: run the LLM with memories injected into context",
    "3. save_memories: extract new facts and store them"
]:
    print(f"  {step}")
print()
print(MEMORY_CODE)
```

---
## 16. Built-in Persistence (SQLite, PostgreSQL)

LangGraph's checkpointer system saves the full graph state after every node execution, enabling multi-turn conversations that survive process restarts, time-travel debugging (replay from any historical checkpoint), and concurrent conversation management via `thread_id`. The `SqliteSaver` is ideal for development and single-process deployments, while `PostgresSaver` provides ACID-compliant persistence for production multi-server setups. Every state snapshot includes the complete message history, custom state fields, and metadata -- making it possible to fork a conversation from any point and explore alternative agent paths.

```python
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core.messages import HumanMessage, AIMessage

# ── SQLite persistence ────────────────────────────────────────────────────────
# Every state snapshot is saved; can resume any conversation from any point

def echo_node(state: MessagesState) -> dict:
    """Simple echo node for demonstration."""
    last_msg = state["messages"][-1].content
    response = AIMessage(content=f"You said: {last_msg}")
    return {"messages": [response]}

gb = StateGraph(MessagesState)
gb.add_node("agent", echo_node)
gb.add_edge(START, "agent")
gb.add_edge("agent", END)

# Compile with SQLite checkpointer
with SqliteSaver.from_conn_string(":memory:") as checkpointer:
    persistent_graph = gb.compile(checkpointer=checkpointer)
    
    # thread_id enables multi-turn conversations
    config = {"configurable": {"thread_id": "conversation-001"}}
    
    # Turn 1
    result1 = persistent_graph.invoke(
        {"messages": [HumanMessage(content="Hello, my name is Bob.")]},
        config=config
    )
    print("Turn 1:", result1["messages"][-1].content)
    
    # Turn 2 - graph remembers the previous turn
    result2 = persistent_graph.invoke(
        {"messages": [HumanMessage(content="What did I say before?")]},
        config=config
    )
    print("Turn 2:", result2["messages"][-1].content)
    
    # Inspect the full message history
    state = persistent_graph.get_state(config)
    print(f"\nTotal messages in history: {len(state.values['messages'])}")
    for msg in state.values["messages"]:
        role = "Human" if isinstance(msg, HumanMessage) else "AI"
        print(f"  [{role}]: {msg.content}")
```

```python
# PostgreSQL persistence for production
POSTGRES_PERSISTENCE_CODE = """
# pip install langgraph-checkpoint-postgres psycopg
from langgraph.checkpoint.postgres import PostgresSaver

DB_URI = "postgresql://user:password@localhost:5432/agents_db"

with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    # One-time setup: creates the checkpoints table
    checkpointer.setup()
    
    graph = my_graph_builder.compile(checkpointer=checkpointer)
    
    # Resume any past conversation by thread_id
    config = {"configurable": {"thread_id": "existing-conversation-id"}}
    state = graph.get_state(config)
    
    # Time-travel: restore to a specific checkpoint
    checkpoints = list(graph.get_state_history(config))
    old_state = checkpoints[-3]  # 3 steps back
    graph.invoke(None, {"configurable": {"thread_id": "...", "checkpoint_id": old_state.config["configurable"]["checkpoint_id"]}})
"""

print("Persistence options comparison:")
print()
options = [
    ("InMemory",    "Development/testing", "No install",               "No - lost on restart"),
    ("SQLite",      "Small-scale apps",    "pip install langgraph",     "Yes - local file"),
    ("PostgreSQL",  "Production",          "pip install langgraph-checkpoint-postgres", "Yes - full ACID"),
    ("Redis",       "High-performance",    "pip install langgraph-checkpoint-redis",    "Yes - in-memory"),
]
print(f"  {'Backend':<15} {'Use case':<22} {'Install':<45} {'Persistent'}")
print("-" * 105)
for backend, use_case, install, persistent in options:
    print(f"  {backend:<15} {use_case:<22} {install:<45} {persistent}")

print()
print("PostgreSQL persistence code:")
print(POSTGRES_PERSISTENCE_CODE)
```

---
## 17. Human-in-the-Loop with `interrupt()`

The `interrupt()` function pauses graph execution at a designated node and returns control to the caller, enabling human approval workflows for high-stakes actions (database deletions, financial transactions, deployment triggers). The graph state is persisted via the checkpointer, so the process can shut down entirely between the interrupt and the human's response. When the human decides, `update_state()` injects their decision into the graph state, and calling `invoke(None, config)` resumes execution from exactly where it paused. This pattern requires a checkpointer -- without persistence, the graph state would be lost when execution pauses.

```python
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.types import interrupt, Command
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core.messages import HumanMessage, AIMessage
from typing import TypedDict, Annotated
import operator

class ApprovalState(TypedDict):
    messages: Annotated[list, operator.add]
    action: str
    approved: bool

def plan_action(state: ApprovalState) -> dict:
    """Agent proposes an action."""
    # In production, the LLM decides what action to take
    action = "DELETE all records from the 'temp_data' table"
    return {
        "action": action,
        "messages": [AIMessage(content=f"I plan to: {action}")]
    }

def human_approval(state: ApprovalState) -> dict:
    """Pause and wait for human approval."""
    # interrupt() pauses the graph and returns control to the caller
    # The graph resumes when .invoke() or .update_state() is called with the answer
    approval_response = interrupt(
        value={
            "question": f"Approve this action? '{state['action']}'",
            "action": state["action"]
        }
    )
    approved = approval_response.get("approved", False)
    return {
        "approved": approved,
        "messages": [HumanMessage(content=f"Human decision: {'APPROVED' if approved else 'REJECTED'}")]
    }

def execute_action(state: ApprovalState) -> dict:
    """Execute the approved action."""
    if state["approved"]:
        result = f"Executed: {state['action']}"
    else:
        result = "Action cancelled by human."
    return {"messages": [AIMessage(content=result)]}

# Build graph
ag = StateGraph(ApprovalState)
ag.add_node("plan", plan_action)
ag.add_node("human_approval", human_approval)
ag.add_node("execute", execute_action)

ag.add_edge(START, "plan")
ag.add_edge("plan", "human_approval")
ag.add_edge("human_approval", "execute")
ag.add_edge("execute", END)

# Persistence is required for human-in-the-loop
with SqliteSaver.from_conn_string(":memory:") as checkpointer:
    approval_graph = ag.compile(checkpointer=checkpointer, interrupt_before=["human_approval"])
    
    config = {"configurable": {"thread_id": "approval-001"}}
    
    # Step 1: Run until the interrupt
    result = approval_graph.invoke(
        {"messages": [], "action": "", "approved": False},
        config=config
    )
    print("Graph paused at human_approval node")
    print(f"Proposed action: {result['action']}")
    print("(In a real app: send email/Slack to approver, wait for webhook)")
    
    # Step 2: Resume with human's decision
    # Update state to inject the human's answer
    approval_graph.update_state(
        config,
        values={"approved": True},
        as_node="human_approval"
    )
    
    # Step 3: Resume execution
    final = approval_graph.invoke(None, config=config)
    print(f"\nFinal result: {final['messages'][-1].content}")
```

---
## 18. Dynamic Tool Calling

`create_react_agent` is LangGraph's recommended way to build a ReAct agent that automatically handles the tool-call loop. You pass an LLM and a list of `@tool`-decorated functions, and the resulting graph alternates between calling the model and executing tool calls until the model produces a final response without tool invocations. The agent manages prompt construction, tool schema injection, response parsing, and multi-step reasoning internally, letting you focus on defining tool logic rather than orchestration plumbing.

```python
from langgraph.prebuilt import create_react_agent, InjectedToolCallId
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-4o", temperature=0)

# create_react_agent is the recommended ReAct agent in LangGraph 1.0
# It handles the tool-call loop automatically

@tool
def get_stock_price(ticker: str) -> dict:
    """Get the current stock price for a ticker symbol."""
    # Mock prices
    prices = {"AAPL": 185.50, "MSFT": 410.20, "GOOGL": 175.30, "NVDA": 875.00}
    price = prices.get(ticker.upper(), 100.00)
    return {"ticker": ticker.upper(), "price": price, "currency": "USD"}

@tool
def get_company_info(ticker: str) -> dict:
    """Get basic company information for a ticker symbol."""
    info = {
        "AAPL": {"name": "Apple Inc.", "sector": "Technology", "employees": 164000},
        "MSFT": {"name": "Microsoft Corp.", "sector": "Technology", "employees": 221000},
        "NVDA": {"name": "NVIDIA Corp.", "sector": "Semiconductors", "employees": 36000},
    }
    return info.get(ticker.upper(), {"name": ticker, "sector": "Unknown"})

@tool
def calculate_portfolio_value(holdings: dict) -> dict:
    """
    Calculate the total value of a stock portfolio.
    holdings: dict mapping ticker to number of shares, e.g. {'AAPL': 10, 'MSFT': 5}
    """
    prices = {"AAPL": 185.50, "MSFT": 410.20, "GOOGL": 175.30, "NVDA": 875.00}
    total = 0
    breakdown = {}
    for ticker, shares in holdings.items():
        price = prices.get(ticker.upper(), 100.0)
        value = price * shares
        breakdown[ticker] = {"shares": shares, "price": price, "value": round(value, 2)}
        total += value
    return {"total": round(total, 2), "currency": "USD", "breakdown": breakdown}

# ReAct agent handles tool calls automatically
finance_agent = create_react_agent(
    llm,
    tools=[get_stock_price, get_company_info, calculate_portfolio_value],
    prompt="You are a financial analyst assistant. Help users understand stock information and portfolio values."
)

# Test with a direct tool call
stock_result = get_stock_price.invoke({"ticker": "NVDA"})
print("NVDA stock price:", stock_result)

portfolio_result = calculate_portfolio_value.invoke({"holdings": {"AAPL": 10, "MSFT": 5, "NVDA": 2}})
print("Portfolio value:", portfolio_result)

print("\nReAct agent ready. Usage:")
print("  result = finance_agent.invoke({'messages': [HumanMessage(content='What is my portfolio worth if I have 10 AAPL, 5 MSFT, and 2 NVDA?')]})")
```

---
## 19. Streaming Tokens from LangGraph Agents

LangGraph 1.0 provides five streaming modes that give progressively more granular visibility into graph execution. The `messages` mode streams individual tokens as they are generated by the LLM, enabling real-time typewriter-style output in chat UIs. The `updates` mode emits state deltas after each node completes, which is useful for progress indicators in multi-step workflows. The `events` mode provides the most comprehensive view -- node start/end, tool calls, token events, and metadata -- suitable for building real-time monitoring dashboards.

```python
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# LangGraph 1.0 streaming modes
STREAMING_MODES = {
    "values": "Full state after each node completes",
    "updates": "Only the delta (changed keys) after each node",
    "messages": "Individual tokens as they stream from the LLM",
    "events": "All events (node start, tool call, token, node end)",
    "debug": "Verbose debug information",
}

print("LangGraph 1.0 streaming modes:")
for mode, desc in STREAMING_MODES.items():
    print(f"  stream_mode='{mode}': {desc}")

STREAMING_EXAMPLE = """
import asyncio
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-4o", streaming=True)

def agent_node(state):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

g = StateGraph(MessagesState)
g.add_node("agent", agent_node)
g.add_edge(START, "agent")
g.add_edge("agent", END)
graph = g.compile()

# Stream individual tokens
async def stream_tokens():
    async for msg, metadata in graph.astream(
        {"messages": [HumanMessage(content="Tell me about MCP in one paragraph.")]},
        stream_mode="messages"
    ):
        if msg.content and metadata["langgraph_node"] == "agent":
            print(msg.content, end="", flush=True)
    print()  # newline at end

asyncio.run(stream_tokens())

# Stream state updates
for update in graph.stream(
    {"messages": [HumanMessage(content="Hello!")]},
    stream_mode="updates"
):
    node_name, state_delta = list(update.items())[0]
    print(f"Node '{node_name}' produced: {state_delta['messages'][-1].content[:50]}")
"""

print()
print("Streaming code pattern:")
print(STREAMING_EXAMPLE)
```

---
# Section C - Comparison and Production Guidance

## 20. LangGraph vs OpenAI Agents SDK

```python
comparison_table = {
    "Philosophy": {
        "OpenAI Agents SDK": "Minimalist - Agent + Runner + optional handoffs",
        "LangGraph 1.0": "Explicit - model everything as a typed state graph"
    },
    "Learning curve": {
        "OpenAI Agents SDK": "Low - 3 core concepts (Agent, Runner, handoff)",
        "LangGraph 1.0": "Medium - graphs, nodes, edges, state, reducers"
    },
    "Multi-agent": {
        "OpenAI Agents SDK": "Handoffs (push-based delegation)",
        "LangGraph 1.0": "Supervisor or Swarm patterns (pull-based routing)"
    },
    "State management": {
        "OpenAI Agents SDK": "In-context messages + Memory primitive",
        "LangGraph 1.0": "Typed TypedDict with custom reducers, full history"
    },
    "Persistence": {
        "OpenAI Agents SDK": "Manual (save/load messages yourself)",
        "LangGraph 1.0": "Built-in: SQLite, PostgreSQL, Redis, custom"
    },
    "Human-in-the-loop": {
        "OpenAI Agents SDK": "Manual interrupt + resume",
        "LangGraph 1.0": "interrupt() + update_state() built into graph"
    },
    "Streaming": {
        "OpenAI Agents SDK": "Runner.run_streamed() with event stream",
        "LangGraph 1.0": "astream() with 5 modes (values/updates/messages/events/debug)"
    },
    "Tracing": {
        "OpenAI Agents SDK": "Built-in to platform.openai.com/traces",
        "LangGraph 1.0": "LangSmith integration or custom callbacks"
    },
    "MCP support": {
        "OpenAI Agents SDK": "Native MCPServerStdio / MCPServerHttp",
        "LangGraph 1.0": "Via langchain-mcp-adapters package"
    },
    "Voice support": {
        "OpenAI Agents SDK": "Built-in VoicePipeline",
        "LangGraph 1.0": "Not built-in (DIY)"
    },
    "Provider support": {
        "OpenAI Agents SDK": "OpenAI native + LiteLLM for others",
        "LangGraph 1.0": "Any LangChain chat model (100+ providers)"
    },
    "Best for": {
        "OpenAI Agents SDK": "Customer support bots, simple delegation, voice",
        "LangGraph 1.0": "Complex workflows, approval chains, research pipelines"
    },
}

print(f"{'Dimension':<22} {'OpenAI Agents SDK':<52} {'LangGraph 1.0'}")
print("-" * 130)
for dim, vals in comparison_table.items():
    sdk_val = vals["OpenAI Agents SDK"]
    lg_val = vals["LangGraph 1.0"]
    print(f"{dim:<22} {sdk_val:<52} {lg_val}")
```

```python
# Decision guide

decision_guide = """
CHOOSE OpenAI Agents SDK when:
  - You want to get started quickly (under 50 lines of code)
  - Your workflow is primarily linear with optional specialist delegation
  - You need voice support out of the box
  - You want zero-config tracing via platform.openai.com
  - Your team is already using the OpenAI API heavily
  - You need realtime/streaming voice agents

CHOOSE LangGraph 1.0 when:
  - You need complex, branching workflows (loops, cycles, conditionals)
  - You need built-in conversation persistence across restarts
  - You need human-in-the-loop approval workflows
  - You need time-travel debugging (replay from any checkpoint)
  - You want to use non-OpenAI models natively (Claude, Gemini, Ollama)
  - Your use case involves document processing pipelines or multi-step research
  - You need fine-grained control over state management

USE BOTH when:
  - Your platform needs quick-start agents (Agents SDK) AND
    complex backend workflows (LangGraph)
  - They are complementary, not competitive
"""

print(decision_guide)
```

---
## 21. Production Deployment Patterns

Deploying agents to production requires wrapping the agent loop in a web framework (FastAPI, Flask) that handles HTTP request lifecycle, authentication, rate limiting, and error recovery. The three patterns below cover the spectrum: **FastAPI + Agents SDK** for lightweight REST endpoints with streaming support, **FastAPI + LangGraph** for persistent multi-turn conversations backed by PostgreSQL, and **LangGraph Platform** for fully managed deployments with auto-generated REST APIs, cron scheduling, and background task queues. Choose based on your infrastructure maturity and control requirements.

```python
# Pattern 1: FastAPI + OpenAI Agents SDK - REST endpoint for an agent

FASTAPI_AGENTS_SDK = """
# pip install fastapi uvicorn openai-agents
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from agents import Agent, Runner
import asyncio, json

app = FastAPI(title="Agents SDK API")

support_agent = Agent(
    name="support",
    instructions="You are a helpful customer support agent.",
    model="gpt-4o"
)

class ChatRequest(BaseModel):
    message: str
    thread_id: str | None = None

@app.post("/chat")
async def chat(req: ChatRequest):
    result = await Runner.run(support_agent, req.message)
    return {"response": result.final_output, "agent": result.last_agent.name}

@app.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    async def token_generator():
        async with Runner.run_streamed(support_agent, req.message) as stream:
            async for event in stream.stream_events():
                if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
                    yield f"data: {json.dumps({'token': event.data.delta})}\\n\\n"
        yield "data: [DONE]\\n\\n"
    return StreamingResponse(token_generator(), media_type="text/event-stream")

# uvicorn main:app --host 0.0.0.0 --port 8000
"""

print("Pattern 1: FastAPI + OpenAI Agents SDK")
print(FASTAPI_AGENTS_SDK)
```

```python
# Pattern 2: FastAPI + LangGraph - persistent multi-turn conversations

FASTAPI_LANGGRAPH = """
# pip install fastapi uvicorn langgraph langgraph-checkpoint-postgres
from fastapi import FastAPI
from pydantic import BaseModel
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.postgres import PostgresSaver
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import uuid

app = FastAPI(title="LangGraph API")

# Build graph (once at startup)
llm = ChatOpenAI(model="gpt-4o")
g = StateGraph(MessagesState)
g.add_node("agent", lambda s: {"messages": [llm.invoke(s["messages"])]})
g.add_edge(START, "agent")
g.add_edge("agent", END)

# PostgreSQL persistence
checkpointer = PostgresSaver.from_conn_string("postgresql://user:pw@localhost/db")
checkpointer.setup()  # Creates tables once
graph = g.compile(checkpointer=checkpointer)

class ChatRequest(BaseModel):
    message: str
    thread_id: str = None  # None = new conversation

@app.post("/chat")
async def chat(req: ChatRequest):
    thread_id = req.thread_id or str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}
    
    result = graph.invoke(
        {"messages": [HumanMessage(content=req.message)]},
        config=config
    )
    return {
        "response": result["messages"][-1].content,
        "thread_id": thread_id  # Return so client can continue the conversation
    }

@app.get("/threads/{thread_id}/history")
async def get_history(thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    state = graph.get_state(config)
    return {"messages": [{"role": m.type, "content": m.content} for m in state.values["messages"]]}
"""

print("Pattern 2: FastAPI + LangGraph with PostgreSQL persistence")
print(FASTAPI_LANGGRAPH)
```

```python
# Pattern 3: LangGraph Platform (hosted deployment)

LANGGRAPH_PLATFORM = """
LangGraph Platform (formerly LangGraph Cloud) provides:
  - Managed infrastructure for LangGraph agents
  - Built-in persistence, streaming, and async task queues
  - Background agent runs (for long-running tasks)
  - REST API auto-generated from your graph
  - Cron scheduling for periodic agents

langgraph.json (deployment config):
{
  "dependencies": ["."],
  "graphs": {
    "research_agent": "./my_agent.py:graph",
    "support_agent": "./support.py:compiled_graph"
  },
  "env": ".env"
}

Deploy:
  $ pip install langgraph-cli
  $ langgraph up           # Local dev server
  $ langgraph deploy       # Deploy to LangGraph Platform

Generated API endpoints:
  POST /runs             -> start a new agent run
  GET  /runs/{run_id}    -> get run status
  POST /threads          -> create a new thread
  GET  /threads/{id}/state -> get thread state
  POST /runs/stream      -> streaming run
  POST /crons            -> schedule periodic runs
"""

print(LANGGRAPH_PLATFORM)
```

---
## Summary

### OpenAI Agents SDK

| Concept | Key point |
|---------|----------|
| **Agent** | `Agent(name, instructions, model, tools, handoffs, guardrails)` |
| **Runner** | `await Runner.run(agent, message)` returns `RunResult` |
| **Handoff** | `handoff(other_agent)` - delegates to specialist |
| **Guardrail** | `@input_guardrail` / `@output_guardrail` - parallel validation |
| **Tracing** | Auto-traced to platform.openai.com/traces |
| **Voice** | `VoicePipeline` for STT → Agent → TTS |
| **Providers** | Any via `LitellmModel` or `OpenAIChatCompletionsModel` |

### LangGraph 1.0

| Concept | Key point |
|---------|----------|
| **StateGraph** | Typed state + nodes + edges - explicit workflow graph |
| **MessagesState** | Standard starting state with auto-append messages |
| **Persistence** | `SqliteSaver` / `PostgresSaver` / `RedisSaver` |
| **interrupt()** | Pause graph for human input; resume with `update_state()` |
| **Supervisor** | `create_supervisor()` for hierarchical multi-agent |
| **LangMem** | Extract + store + retrieve long-term memories |
| **Streaming** | 5 modes: values, updates, messages, events, debug |

### Next Steps
- OpenAI Agents SDK docs: https://openai.github.io/openai-agents-python/
- LangGraph docs: https://langchain-ai.github.io/langgraph/
- LangGraph Platform: https://langchain-ai.github.io/langgraph/cloud/
- LangMem SDK: https://langchain-ai.github.io/langmem/
