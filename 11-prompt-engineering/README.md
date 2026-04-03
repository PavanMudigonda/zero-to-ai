# Phase 10: Prompt Engineering

This module is most useful when treated as systems design for model interaction, not as a bag of prompt hacks. The repo currently focuses on the practical subset you can actually apply in production workflows.

## Actual Module Contents

1. [00_START_HERE.ipynb](00_START_HERE.ipynb)
2. [01_basic_prompting.ipynb](01_basic_prompting.ipynb)
3. [02_chain_of_thought.ipynb](02_chain_of_thought.ipynb)
4. [03_react_prompting.ipynb](03_react_prompting.ipynb)
5. [05_structured_outputs_dspy.ipynb](05_structured_outputs_dspy.ipynb)
6. [06_long_context_strategies.ipynb](06_long_context_strategies.ipynb)
7. [assignment.md](assignment.md)

## What To Learn Here

- How prompt quality changes task reliability
- When few-shot examples are worth the extra tokens
- How ReAct changes model behavior when tools are involved
- Why structured outputs are better than post-hoc parsing
- How to handle long contexts without blindly stuffing documents into prompts

## Recommended Study Order

- Start with [01_basic_prompting.ipynb](01_basic_prompting.ipynb)
- Move to [02_chain_of_thought.ipynb](02_chain_of_thought.ipynb) for reasoning patterns
- Study [03_react_prompting.ipynb](03_react_prompting.ipynb) before Phase 15 agents
- Use [05_structured_outputs_dspy.ipynb](05_structured_outputs_dspy.ipynb) to connect prompting with reliability
- Finish with [06_long_context_strategies.ipynb](06_long_context_strategies.ipynb) before deeper RAG and agent work

## Learning Advice

- Prompting is not a substitute for retrieval, fine-tuning, or evaluation.
- If a task fails, ask whether the real issue is missing context, poor tools, or missing schema constraints.
- Keep examples and output formats explicit; ambiguity is expensive.

## Good Follow-On Projects

- A structured extraction pipeline with validation
- A multi-step research assistant using ReAct
- A long-context summarizer that compares chunk-then-summarize vs direct prompting
