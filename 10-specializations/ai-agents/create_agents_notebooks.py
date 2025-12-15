#!/usr/bin/env python3
"""Create AI Agents notebook series"""

import json

def nb(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in text.split("\n")]}

def code(text):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [line + "\n" for line in text.split("\n")]}

def save_notebook(filename, cells):
    with open(filename, 'w') as f:
        json.dump(nb(cells), f, indent=2)

# Notebook 00: START HERE
notebook_00 = [
    md("# AI Agents: Building Autonomous Systems\n\n## 🎯 What You'll Learn\n\nThis series covers building production-ready AI agents:\n\n1. **Function Calling** - Tool use and integration\n2. **ReAct Pattern** - Reasoning and acting loop\n3. **LangGraph** - State machines for agents\n4. **Multi-Agent Systems** - Agent collaboration\n5. **Memory & State** - Long-term memory\n6. **Production Deployment** - Monitoring and scaling\n\n## What is an AI Agent?\n\n**Chatbot**: Responds to questions\n- Input: \"What's the weather?\"\n- Output: \"I don't have access to weather data\"\n\n**Agent**: Takes action to answer\n- Input: \"What's the weather?\"\n- Agent: *calls weather API*\n- Output: \"It's 72°F and sunny in San Francisco\"\n\n### Key Differences\n\n| Feature | Chatbot | Agent |\n|---------|---------|-------|\n| **Tools** | None | Can use external tools |\n| **Planning** | No | Can plan multi-step tasks |\n| **Memory** | Session only | Long-term memory |\n| **Actions** | Text responses | Real-world actions |\n| **Autonomy** | Low | High |"),
    
    md("## Agent Architecture\n\n```\n┌─────────────────────────────────────────────────────┐\n│                   AI AGENT                          │\n├─────────────────────────────────────────────────────┤\n│                                                     │\n│  User Input                                         │\n│      ↓                                              │\n│  ┌──────────┐                                       │\n│  │   LLM    │ ← Planning & Reasoning                │\n│  │  Brain   │                                        │\n│  └────┬─────┘                                       │\n│       │                                              │\n│       ↓                                              │\n│  ┌──────────────────────────┐                       │\n│  │   Tool Selection         │                       │\n│  └────┬─────────────────────┘                       │\n│       │                                              │\n│       ↓                                              │\n│  ┌──────────────────────────┐                       │\n│  │   Tool Execution         │                       │\n│  │  - Web Search            │                       │\n│  │  - Database Query        │                       │\n│  │  - Code Execution        │                       │\n│  │  - API Calls             │                       │\n│  └────┬─────────────────────┘                       │\n│       │                                              │\n│       ↓                                              │\n│  ┌──────────┐                                       │\n│  │  Memory  │ ← Short & Long-term                   │\n│  └──────────┘                                       │\n│       │                                              │\n│       ↓                                              │\n│  Final Response                                     │\n│                                                     │\n└─────────────────────────────────────────────────────┘\n```"),
    
    md("## Quick Demo: Calculator Agent\n\nLet's build a simple agent that can do math:"),
    
    code("# Install dependencies (uncomment to run)\n# !pip install openai"),
    
    code("import json\nimport re\nfrom typing import Dict, List, Any\n\nclass SimpleAgent:\n    \"\"\"A simple calculator agent\"\"\"\n    \n    def __init__(self):\n        self.tools = {\n            \"calculator\": self.calculator,\n            \"is_prime\": self.is_prime\n        }\n        self.conversation_history = []\n    \n    def calculator(self, expression: str) -> float:\n        \"\"\"Evaluate a mathematical expression\"\"\"\n        try:\n            # Safe evaluation (limited to math operations)\n            result = eval(expression, {\"__builtins__\": {}}, {})\n            return result\n        except Exception as e:\n            return f\"Error: {str(e)}\"\n    \n    def is_prime(self, n: int) -> bool:\n        \"\"\"Check if a number is prime\"\"\"\n        if n < 2:\n            return False\n        for i in range(2, int(n ** 0.5) + 1):\n            if n % i == 0:\n                return False\n        return True\n    \n    def parse_action(self, text: str) -> Dict[str, Any]:\n        \"\"\"Extract tool name and arguments from text\"\"\"\n        # Simple parsing for demo\n        if \"calculator\" in text.lower():\n            match = re.search(r'calculator\\(([^)]+)\\)', text)\n            if match:\n                return {\"tool\": \"calculator\", \"args\": match.group(1)}\n        \n        if \"is_prime\" in text.lower():\n            match = re.search(r'is_prime\\((\\d+)\\)', text)\n            if match:\n                return {\"tool\": \"is_prime\", \"args\": int(match.group(1))}\n        \n        return None\n    \n    def run(self, query: str, max_iterations: int = 5) -> str:\n        \"\"\"Run the agent loop\"\"\"\n        print(f\"🤖 Agent received: {query}\\n\")\n        \n        # Simple reasoning (in real agent, LLM does this)\n        iterations = 0\n        \n        while iterations < max_iterations:\n            iterations += 1\n            print(f\"--- Iteration {iterations} ---\")\n            \n            # Decide what to do (simplified)\n            if \"sum\" in query.lower() or \"+\" in query:\n                thought = \"I need to calculate this sum\"\n                action = self.parse_action(\"calculator(23 + 45)\")\n                if action:\n                    print(f\"💭 Thought: {thought}\")\n                    print(f\"🔧 Action: {action['tool']}({action['args']})\")\n                    \n                    result = self.tools[action['tool']](action['args'])\n                    print(f\"📊 Result: {result}\\n\")\n                    return f\"The answer is {result}\"\n            \n            elif \"prime\" in query.lower():\n                # Extract number from query\n                numbers = re.findall(r'\\d+', query)\n                if numbers:\n                    num = int(numbers[0])\n                    thought = f\"I need to check if {num} is prime\"\n                    print(f\"💭 Thought: {thought}\")\n                    print(f\"🔧 Action: is_prime({num})\")\n                    \n                    result = self.tools[\"is_prime\"](num)\n                    print(f\"📊 Result: {result}\\n\")\n                    \n                    if result:\n                        return f\"Yes, {num} is a prime number\"\n                    else:\n                        return f\"No, {num} is not a prime number\"\n            \n            # If we can't determine action, return\n            return \"I'm not sure how to help with that.\"\n        \n        return \"Max iterations reached\"\n\n# Create and test agent\nagent = SimpleAgent()\nprint(\"=\" * 60)\nresponse = agent.run(\"What is 23 + 45?\")\nprint(f\"✅ Final Answer: {response}\")\nprint(\"=\" * 60)"),
    
    md("## ReAct Pattern\n\nThe ReAct (Reasoning + Acting) pattern is the core of modern agents:\n\n```\n1. THOUGHT: Analyze the problem\n2. ACTION: Choose and execute a tool\n3. OBSERVATION: See the result\n4. REPEAT until solved\n5. ANSWER: Provide final response\n```\n\n### Example\n\n**Query**: \"What's the weather in the capital of France?\"\n\n**Iteration 1:**\n- THOUGHT: I need to find the capital of France first\n- ACTION: search(\"capital of France\")\n- OBSERVATION: \"Paris\"\n\n**Iteration 2:**\n- THOUGHT: Now I can get the weather for Paris\n- ACTION: get_weather(\"Paris\")\n- OBSERVATION: \"72°F, sunny\"\n\n**Final Answer**: \"The weather in Paris (capital of France) is 72°F and sunny\""),
    
    md("## What's Next?\n\nIn the following notebooks, you'll learn:\n\n1. **Function Calling** - OpenAI/Anthropic function calling\n2. **ReAct Pattern** - Build reasoning agents\n3. **LangGraph** - State machines for complex workflows\n4. **Multi-Agent Systems** - Agent collaboration\n5. **Memory & State** - Long-term memory systems\n6. **Production** - Deploy and monitor agents\n\n🚀 Ready to build intelligent agents!"),
    
    md("## Key Concepts\n\n### 1. Tools/Functions\nExternal capabilities the agent can use:\n- Web search\n- Database queries\n- Code execution\n- API calls\n- File operations\n\n### 2. Planning\nBreaking complex tasks into steps:\n- Task decomposition\n- Step sequencing\n- Error recovery\n- Parallel execution\n\n### 3. Memory\nRetaining context across interactions:\n- Short-term (conversation)\n- Long-term (knowledge base)\n- Episodic (past experiences)\n- Semantic (facts and concepts)\n\n### 4. Reasoning\nDeciding what to do next:\n- Chain-of-thought\n- ReAct pattern\n- Tree-of-thought\n- Self-reflection")
]

print("Creating AI Agents Notebooks...")
print("=" * 70)

save_notebook("00_START_HERE.ipynb", notebook_00)
print("✓ Notebook 00: AI Agents Overview")

print("=" * 70)
print("🎉 SUCCESS! Created AI Agents starter notebook")
print("\nNext: Create remaining notebooks")
