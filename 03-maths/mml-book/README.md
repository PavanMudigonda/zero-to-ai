# Mathematics for Machine Learning (MML)

Notebook series following the *Mathematics for Machine Learning* textbook by Deisenroth, Faisal, Ong.

**Source PDF:** [mml-book.pdf](mml-book.pdf)

This folder is the best next step after the foundational notebooks if you want structured, rigorous math depth without immediately jumping into research-level theory.

## Course Notebooks

| # | Notebook | Book Chapter | Topics |
|---|---------|-------------|--------|
| 01 | [Linear Algebra](course/01_linear_algebra.ipynb) | Ch 2 | Systems of equations, vector spaces, basis, rank, linear mappings |
| 02 | [Analytic Geometry](course/02_analytic_geometry.ipynb) | Ch 3 | Norms, inner products, projections, rotations |
| 03 | [Matrix Decompositions](course/03_matrix_decompositions.ipynb) | Ch 4 | Eigenvalues, Cholesky, SVD, low-rank approximation |
| 04 | [Vector Calculus](course/04_vector_calculus.ipynb) | Ch 5 | Gradients, Jacobians, backpropagation, Taylor series |
| 05 | [Probability](course/05_probability.ipynb) | Ch 6 | Distributions, Bayes' theorem, Gaussian, exponential family |
| 06 | [Optimization](course/06_optimization.ipynb) | Ch 7 | Gradient descent, Lagrange multipliers, convexity |
| 07 | [Linear Regression](course/07_linear_regression.ipynb) | Ch 8-9 | MLE, MAP, Bayesian linear regression |
| 08 | [PCA](course/08_pca.ipynb) | Ch 10 | Maximum variance, projection, dimensionality reduction |
| 09 | [Gaussian Mixture Models](course/09_gmm.ipynb) | Ch 11 | GMM, EM algorithm, latent variables |
| 10 | [Support Vector Machines](course/10_svm.ipynb) | Ch 12 | Separating hyperplanes, kernels, dual formulation |

## Exercises

| Notebook | Content |
|---------|---------|
| [Exercises Part 1](exercises/mml_exercises_part1.ipynb) | Practice problems for Ch 2-7 |
| [Exercises Part 2](exercises/mml_exercises_part2.ipynb) | Practice problems for Ch 8-12 |
| [Solutions Part 1](exercises/mml_solutions_part1.ipynb) | Solutions for Part 1 |
| [Solutions Part 2](exercises/mml_solutions_part2.ipynb) | Solutions for Part 2 |

## Prerequisites

- [foundational/](../foundational/) notebooks 01-04
- Python 3.8+, NumPy, Matplotlib

## Suggested Order

Follow the course notebooks 01-10 in order. The book has two parts:
- **Part I** (01-06): Mathematical foundations
- **Part II** (07-10): Central ML problems that apply those foundations

## How To Use This Folder Well

- Work in order unless you already know exactly which chapter you need.
- Treat Part I as the core and Part II as the application payoff for that theory.
- Use the practice labs when you want the concepts to become more operational.

## Practice Labs

For hands-on implementations of each chapter, see [practice-labs/](practice-labs/).

## Related

- [cs229-course/](../cs229-course/) — ML algorithms (less math, more applied)
- [advanced/](../advanced/) — research-level extensions of these topics
- [mlpp-book/](../mlpp-book/) — probabilistic perspective on ML

## What Comes Next

- Continue to [../cs229-course/README.md](../cs229-course/README.md) for the algorithm-focused layer.
- Continue to [../advanced/README.md](../advanced/README.md) if you want research-oriented theory after this.
- Continue to [../mlpp-book/README.md](../mlpp-book/README.md) if you want more Bayesian and probabilistic depth.
