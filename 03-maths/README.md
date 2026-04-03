# Phase 2: Mathematics for ML

This folder provides the mathematical intuition behind the rest of the curriculum. The goal is not to turn this repo into a pure math degree. The goal is to give you enough fluency to understand optimization, probability, embeddings, attention, and evaluation without treating them as magic.

## Folder Map

- `foundational/`: the main starting point for most learners
- `mml-book/course/`: Mathematics for Machine Learning notebook sequence
- `mml-book/exercises/`: additional practice
- `islp-book/`: statistical learning and classical ML foundations
- `cs229-course/course/`: Stanford-style ML theory and algorithms
- `mlpp-book/`: probabilistic modeling depth
- `advanced/`: research-level topics; selective, not required on a first pass
- `resources/`: PDFs and reference material

## Recommended First Pass

1. [foundational/01_linear_algebra_fundamentals.ipynb](foundational/01_linear_algebra_fundamentals.ipynb)
2. [foundational/02_calculus_derivatives.ipynb](foundational/02_calculus_derivatives.ipynb)
3. [foundational/03_probability_statistics.ipynb](foundational/03_probability_statistics.ipynb)
4. [foundational/04_gradient_descent.ipynb](foundational/04_gradient_descent.ipynb)
5. [foundational/06_statistical_inference.ipynb](foundational/06_statistical_inference.ipynb)
6. [foundational/07_neural_network_math.ipynb](foundational/07_neural_network_math.ipynb)

## Strong Follow-On Paths

- For ML engineer depth:
  [mml-book/course/](mml-book/course/) and [cs229-course/course/](cs229-course/course/)
- For data science depth:
  [islp-book/](islp-book/) and selected [mlpp-book/](mlpp-book/) notebooks
- For research curiosity:
  selected topics in [advanced/](advanced/)

## Practical Learning Rules

- Learn the intuition before the notation.
- Re-derive small examples by hand when possible.
- If a symbol-heavy notebook feels abstract, reconnect it to one downstream use case:
  gradient descent, cosine similarity, cross-entropy, PCA, or attention.

## High-Value Modules

- Linear algebra: embeddings, PCA, attention, matrix ops
- Calculus and optimization: training dynamics and backprop
- Probability and statistics: uncertainty, evaluation, inference, Bayesian thinking
- Information theory: cross-entropy and KL divergence

## What To Avoid

- Do not try to finish every notebook before continuing the curriculum.
- Do not spend weeks on theorem-level depth if your goal is applied AI engineering.
- Do not skip probability and statistics just because you prefer neural networks.

## Best Next Step

After the foundational notebooks, continue into [05-embeddings/](../05-embeddings/) and [06-neural-networks/](../06-neural-networks/), then come back here as needed.
