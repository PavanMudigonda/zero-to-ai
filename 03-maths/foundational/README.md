# Foundational Mathematics

Core mathematical building blocks for machine learning. Start here if you're new to the math side.

## Notebooks

| # | Notebook | Topics |
|---|---------|--------|
| 00 | [Python ML Libraries](00_python_ml_libraries.ipynb) | NumPy, Matplotlib, SciPy essentials for ML math |
| 01 | [Linear Algebra Fundamentals](01_linear_algebra_fundamentals.ipynb) | Vectors, matrices, operations, systems of equations |
| 02 | [Calculus & Derivatives](02_calculus_derivatives.ipynb) | Derivatives, chain rule, partial derivatives, gradients |
| 03 | [Probability & Statistics](03_probability_statistics.ipynb) | Distributions, Bayes' theorem, expectation, variance |
| 04 | [Gradient Descent](04_gradient_descent.ipynb) | Optimization basics, learning rate, convergence |
| 05 | [Information Theory](05_information_theory.ipynb) | Entropy, cross-entropy, KL divergence |
| 06 | [Statistical Inference](06_statistical_inference.ipynb) | Hypothesis testing, confidence intervals, MLE |
| 07 | [Neural Network Math](07_neural_network_math.ipynb) | Forward pass, backpropagation, loss functions |
| 08 | [Advanced Linear Algebra](08_advanced_linear_algebra.ipynb) | Eigendecomposition, SVD, PCA foundations |
| 09 | [Analytical vs Numerical](09_math_architecture_analytical_vs_numerical.ipynb) | Closed-form vs iterative solutions, numerical stability |
| 10 | [Control Theory for AI](10_ai_foundations_control_theory.ipynb) | Control theory connections to RL and optimization |
| 11 | [Markov Models & HMMs](11_markov_models_hmm.ipynb) | Markov chains, hidden Markov models, Viterbi |
| 12 | [Optimization from Scratch](12_optimization_from_scratch_adam.ipynb) | SGD, momentum, Adam optimizer implementation |

## Prerequisites

- Python 3.8+
- NumPy, Matplotlib

## Suggested Order

**Essential first pass** (covers what you need for 90% of ML):
1. 01 Linear Algebra → 02 Calculus → 03 Probability → 04 Gradient Descent

**Then pick based on need:**
- Going into NLP? → 05 Information Theory
- Going into neural nets? → 07 Neural Network Math → 12 Optimization
- Going into Bayesian ML? → 06 Statistical Inference
- Going into sequence models? → 11 Markov Models

## Next Steps

After completing the essential pass, continue to:
- [mml-book/](../mml-book/) for rigorous math depth
- [cs229-course/](../cs229-course/) for ML algorithms
- [mml-book/practice-labs/](../mml-book/practice-labs/) for hands-on implementation
