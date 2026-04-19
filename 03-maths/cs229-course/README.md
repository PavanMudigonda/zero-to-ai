# Stanford CS229 Machine Learning

Notebooks covering the Stanford CS229 ML theory and algorithms course.

**Source PDF:** [cs229.pdf](cs229.pdf)

This folder is the bridge from math foundations to core ML algorithms. Use it when you want to understand how the math turns into modeling choices, error analysis, and learning behavior.

## Notebooks

| # | Notebook | Topics |
|---|---------|--------|
| 01 | [Linear Regression](course/01_linear_regression.ipynb) | Normal equations, least squares, feature scaling |
| 02 | [Gradient Descent](course/02_gradient_descent.ipynb) | Batch, stochastic, mini-batch GD, convergence |
| 03 | [Locally Weighted Regression](course/03_locally_weighted_regression.ipynb) | Non-parametric regression, bandwidth selection |
| 04 | [Logistic Regression](course/04_logistic_regression.ipynb) | Binary classification, sigmoid, cross-entropy |
| 05 | [Generative Models](course/05_generative_models.ipynb) | Gaussian discriminant analysis, Naive Bayes |
| 06 | [Support Vector Machines](course/06_svm.ipynb) | Margin maximization, kernel trick, SMO |
| 07 | [Regularization](course/07_regularization.ipynb) | L1/L2 penalties, bias-variance tradeoff |
| 08 | [Learning Theory](course/08_learning_theory.ipynb) | PAC learning, VC dimension, generalization bounds |
| 09 | [Decision Trees](course/09_decision_trees.ipynb) | CART, pruning, information gain, Gini impurity |
| 10 | [Neural Networks Basics](course/10_neural_networks_basics.ipynb) | Perceptron, feedforward nets, activation functions |
| 11 | [Neural Networks Advanced](course/11_neural_networks_advanced.ipynb) | Backprop, dropout, batch norm, architectures |
| 12 | [ML Strategy](course/12_ml_strategy.ipynb) | Error analysis, dataset splits, debugging ML |
| 13 | [Clustering](course/13_clustering.ipynb) | K-Means, hierarchical, DBSCAN, evaluation |
| 14 | [Dimensionality Reduction](course/14_dimensionality_reduction.ipynb) | PCA, t-SNE, autoencoders |
| 15 | [Reinforcement Learning](course/15_reinforcement_learning.ipynb) | MDPs, Q-learning, policy gradient |
| X01 | [Anomaly Detection](course/X01_anomaly_detection.ipynb) | Gaussian-based, isolation forest |
| X02 | [Recommender Systems](course/X02_recommender_systems.ipynb) | Collaborative filtering, matrix factorization |
| - | [Practice Problems](course/CS229_PRACTICE.ipynb) | Review exercises across all topics |

## Prerequisites

- [foundational/](../foundational/) notebooks 01-04 (linear algebra, calculus, probability, gradient descent)
- Python 3.8+, NumPy, Matplotlib, scikit-learn

## Suggested Order

Follow the numbered sequence (01-15). X01-X02 are supplementary.

## How To Use This Folder Well

- Work through the numbered sequence instead of skipping directly to fashionable topics.
- Pay special attention to optimization, regularization, learning theory, and ML strategy because those ideas transfer across the entire repo.
- Use this folder to connect equations to algorithm behavior, not just to memorize model names.

## Related

- [mml-book/](../mml-book/) - deeper math foundations
- [islp-book/](../islp-book/) - statistical learning perspective on similar topics

## What Comes Next

- Continue to [../islp-book/README.md](../islp-book/README.md) if you want a more statistical interpretation of similar methods.
- Continue to [../advanced/README.md](../advanced/README.md) if you want deeper theory after this layer.
- Return to [../../02-data-science/README.md](../../02-data-science/README.md) or [../../06-neural-networks/README.md](../../06-neural-networks/README.md) to apply the ideas more concretely.
