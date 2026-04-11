# Practice Labs: Math for ML (MML Book)

**Source PDF:** [Mathematics for Machine Learning](https://mml-book.github.io/book/mml-book.pdf)
**Book:** *Mathematics for Machine Learning* by Marc Peter Deisenroth, A. Aldo Faisal, Cheng Soon Ong (Cambridge University Press, 2020)

This book covers the mathematical foundations that underpin machine learning: linear algebra, calculus, probability, optimization, and four central ML algorithms (regression, PCA, GMM, SVM).

## Labs

| Lab | Topic | Book Chapter | Key Concepts |
|-----|-------|-------------|--------------|
| [Lab 01](lab_01_linear_algebra.ipynb) | Linear Algebra | Ch 2 | Systems of equations, Gaussian elimination, vector spaces, basis, rank, linear mappings |
| [Lab 02](lab_02_analytic_geometry.ipynb) | Analytic Geometry | Ch 3 | Norms, inner products, Gram-Schmidt, orthogonal projections, rotations |
| [Lab 03](lab_03_matrix_decompositions.ipynb) | Matrix Decompositions | Ch 4 | Eigenvalues, Cholesky, SVD, low-rank approximation |
| [Lab 04](lab_04_vector_calculus.ipynb) | Vector Calculus | Ch 5 | Gradients, Jacobians, backpropagation, Hessians, Taylor series |
| [Lab 05](lab_05_probability_distributions.ipynb) | Probability & Distributions | Ch 6 | Bayes' theorem, Gaussian, exponential family, conjugacy |
| [Lab 06](lab_06_optimization.ipynb) | Continuous Optimization | Ch 7 | Gradient descent, momentum, Lagrange multipliers, Newton's method, convexity |
| [Lab 07](lab_07_linear_regression.ipynb) | Linear Regression | Ch 8-9 | MLE, Bayesian regression, overfitting, cross-validation |
| [Lab 08](lab_08_pca.ipynb) | PCA | Ch 10 | Maximum variance, projection, scree plot, high-dimensional PCA |
| [Lab 09](lab_09_gaussian_mixtures.ipynb) | Gaussian Mixture Models | Ch 11 | GMM, EM algorithm, K-Means, model selection |
| [Lab 10](lab_10_svm.ipynb) | Support Vector Machines | Ch 12 | Margin maximization, hinge loss, kernels, soft margin |

## How to Use

1. Each lab is a Jupyter notebook with theory (markdown) and fully implemented code cells
2. Read the theory cells, study the implementations, and run each cell
3. Open in Jupyter: `jupyter notebook lab_01_linear_algebra.ipynb`

## Prerequisites

- Python 3.8+
- NumPy
- Matplotlib

## Suggested Order

The book has two parts. Follow Part I (math foundations) first, then Part II (ML applications):

**Part I: Mathematical Foundations**
1. **Lab 01** - Linear Algebra (the language of ML)
2. **Lab 02** - Analytic Geometry (geometry of data)
3. **Lab 03** - Matrix Decompositions (factoring matrices)
4. **Lab 04** - Vector Calculus (training and optimization)
5. **Lab 05** - Probability & Distributions (uncertainty)
6. **Lab 06** - Optimization (finding best parameters)

**Part II: Central ML Problems**
7. **Lab 07** - Linear Regression (prediction)
8. **Lab 08** - PCA (dimensionality reduction)
9. **Lab 09** - Gaussian Mixtures (density estimation)
10. **Lab 10** - SVM (classification)
