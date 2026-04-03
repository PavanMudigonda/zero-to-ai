# Phase 5: Neural Networks

This module is where the repo shifts from classical ML intuition into modern deep learning. The goal is not just to run PyTorch code, but to understand why gradient-based learning, attention, and transformers work well enough that later LLM modules feel connected instead of magical.

## Recommended Order

1. [00_START_HERE.ipynb](00_START_HERE.ipynb)
2. [01_neural_network_basics.ipynb](01_neural_network_basics.ipynb)
3. [02_backpropagation_explained.ipynb](02_backpropagation_explained.ipynb)
4. [03_pytorch_fundamentals.ipynb](03_pytorch_fundamentals.ipynb)
5. [04_attention_mechanism.ipynb](04_attention_mechanism.ipynb)
6. [05_transformer_architecture.ipynb](05_transformer_architecture.ipynb)

Companion reading:

- [intro.md](intro.md)
- [attention_explained.md](attention_explained.md)
- [transformer_architecture.md](transformer_architecture.md)
- [assignment.md](assignment.md)
- [challenges.md](challenges.md)

## What You Should Be Able To Explain

- Why nonlinear activations are needed
- How backpropagation moves signal through a network
- Why PyTorch autograd matters in practice
- What attention is computing and why scaling matters
- How transformer blocks combine attention, MLPs, residual paths, and normalization

## How To Study This Module

- Spend more time on [02_backpropagation_explained.ipynb](02_backpropagation_explained.ipynb) than on framework syntax.
- Treat [04_attention_mechanism.ipynb](04_attention_mechanism.ipynb) as the bridge into LLM architecture.
- Revisit [03-maths/foundational/07_neural_network_math.ipynb](../03-maths/foundational/07_neural_network_math.ipynb) if gradients feel mechanical instead of intuitive.

## Suggested Practice

- Implement a tiny MLP from scratch with NumPy
- Rebuild the same idea in PyTorch
- Write down tensor shapes at each step of attention
- Explain a transformer block without using the phrase "it just learns it"

## Why This Module Matters

If this phase is weak, later phases on fine-tuning, local LLMs, evaluation, and agents become tool memorization. If this phase is strong, the rest of the repo becomes a connected system.
