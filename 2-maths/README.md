# Mathematics for Machine Learning

This directory contains comprehensive Jupyter notebooks covering the mathematical foundations essential for understanding and implementing machine learning algorithms. The content is organized into well-structured folders for easy navigation:

- **📁 foundational/** - Core math topics (9 notebooks)
- **📁 mml-book/** - MML book chapters covering theory and ML applications (10 notebooks)
- **📁 islp-book/** - Introduction to Statistical Learning with Python (13 chapters)
- **📁 cs229-course/** - Stanford CS229 Machine Learning course implementation (14 lectures) 🆕
- **📁 exercises/** - Practice exercises with solutions (4 notebooks)
- **📁 resources/** - Reference materials (MML textbook, ISLP book, CS229 notes)

## 📚 Table of Contents

- [Directory Structure](#-directory-structure)
- [Part I: Foundational Math Notebooks](#part-i-foundational-math-notebooks)
- [Part II: MML Book - Mathematical Foundations](#part-ii-mml-book---mathematical-foundations-chapters-2-7)
- [Part III: MML Book - ML Applications](#part-iii-mml-book---ml-applications-chapters-9-12)
- [Part IV: ISLP Book - Statistical Learning](#part-iv-islp-book---statistical-learning-with-python)
- [Part V: CS229 Course - Machine Learning Algorithms](#part-v-cs229-course---stanford-machine-learning-) 🆕
- [Practice Exercises](#️-practice-with-exercises)
- [Learning Paths](#-learning-paths)
- [Quick Start](#-quick-start)
- [Resources](#-additional-mathematics-resources)

---

## 📁 Directory Structure

```
2-maths/
├── README.md                    # This file
├── foundational/                # Core mathematical topics (00-08)
│   ├── 00_python_ml_libraries.ipynb
│   ├── 01_linear_algebra_fundamentals.ipynb
│   ├── 02_calculus_derivatives.ipynb
│   ├── 03_probability_statistics.ipynb
│   ├── 04_gradient_descent.ipynb
│   ├── 05_information_theory.ipynb
│   ├── 06_statistical_inference.ipynb
│   ├── 07_neural_network_math.ipynb
│   └── 08_advanced_linear_algebra.ipynb
├── mml-book/                    # MML textbook chapters (01-10)
│   ├── 01_linear_algebra.ipynb
│   ├── 02_analytic_geometry.ipynb
│   ├── 03_matrix_decompositions.ipynb
│   ├── 04_vector_calculus.ipynb
│   ├── 05_probability.ipynb
│   ├── 06_optimization.ipynb
│   ├── 07_linear_regression.ipynb
│   ├── 08_pca.ipynb
│   ├── 09_gmm.ipynb
│   └── 10_svm.ipynb
├── islp-book/                   # ISLP textbook implementation (13 chapters)
│   ├── README.md
│   ├── PRACTICE_EXERCISES.md
│   └── 02_statistical_learning.ipynb through 13_multiple_testing.ipynb
├── cs229-course/                # Stanford CS229 Machine Learning (14 lectures) 🆕
│   ├── README.md
│   ├── CS229_PRACTICE.md
│   ├── requirements.txt
│   ├── 01_linear_regression.ipynb
│   ├── 02_logistic_regression.ipynb
│   ├── 03_regularization.ipynb
│   └── (Lectures 04-14 in progress)
├── exercises/                   # Practice problems & solutions
│   ├── mml_exercises_part1.ipynb
│   ├── mml_solutions_part1.ipynb
│   ├── mml_exercises_part2.ipynb
│   └── mml_solutions_part2.ipynb
└── resources/                   # Reference materials
    ├── mml-book.pdf
    ├── ISLP.pdf
    └── cs229.pdf
```

---

## Part I: Foundational Math Notebooks

**Location**: `foundational/` folder

### [00. Python ML Libraries](./foundational/00_python_ml_libraries.ipynb)
**Prerequisites for all math notebooks** ⭐ Start here!
- NumPy fundamentals and array operations
- Matplotlib for plotting and visualization
- Seaborn for statistical plots
- SciPy for scientific computing
- scikit-learn basics for ML applications
- **Bonus sections**: Broadcasting, fancy indexing, advanced numpy operations, sklearn pipelines

**Duration**: 2-3 hours

---

### [01. Linear Algebra Fundamentals](./foundational/01_linear_algebra_fundamentals.ipynb)
**Topics covered:**
- Vectors and vector operations (addition, scalar multiplication, dot product)
- Matrices and matrix operations (multiplication, transpose, inverse)
- Eigenvalues and eigenvectors
- Linear transformations
- **ML Applications**: Linear regression using the Normal Equation, data transformations

**Key takeaway**: Linear algebra is the language of ML - from data representation to neural network operations.

**Duration**: 3-4 hours

---

### [02. Calculus & Derivatives](./foundational/02_calculus_derivatives.ipynb)
**Topics covered:**
- Derivatives and their geometric interpretation
- Common activation functions (ReLU, Sigmoid, Tanh) and their derivatives
- Partial derivatives for multivariable functions
- Gradient vectors
- Chain rule for backpropagation
- Gradient descent basics

**ML Applications**: Understanding how neural networks learn through gradient-based optimization.

**Key takeaway**: Calculus enables optimization - the foundation of training ML models.

**Duration**: 3-4 hours

---

### [03. Probability & Statistics](./foundational/03_probability_statistics.ipynb)
**Topics covered:**
- Probability fundamentals (rules, conditional probability)
- Random variables (discrete and continuous)
- Common distributions (Bernoulli, Binomial, Normal/Gaussian)
- Bayes' theorem
- Central Limit Theorem
- Expected value and variance

**ML Applications**: Maximum Likelihood Estimation (MLE), Naive Bayes classifier.

**Key takeaway**: Probability theory provides the mathematical framework for reasoning under uncertainty.

**Duration**: 4-5 hours

---

### [04. Gradient Descent](./foundational/04_gradient_descent.ipynb)
**Topics covered:**
- Gradient descent algorithm
- Learning rate effects (too small, too large, optimal)
- 1D and 2D visualizations
- Non-convex functions and local minima
- Batch vs Stochastic vs Mini-batch GD
- Momentum
- Advanced optimizers (Adam, RMSprop)

**ML Applications**: Training neural networks, optimizing loss functions.

**Key takeaway**: Gradient descent is the workhorse algorithm that powers modern deep learning.

**Duration**: 3-4 hours

---

### [05. Information Theory](./foundational/05_information_theory.ipynb)
**Topics covered:**
- Shannon entropy and information content
- Cross-entropy loss (the main loss function in deep learning)
- Kullback-Leibler (KL) divergence
- Mutual information
- Binary and categorical cross-entropy

**ML Applications**: Neural network loss functions, model evaluation, distribution comparison.

**Key takeaway**: Information theory provides the mathematical foundation for loss functions and measuring uncertainty.

**Duration**: 2-3 hours

---

### [06. Statistical Inference](./foundational/06_statistical_inference.ipynb)
**Topics covered:**
- Population vs sample statistics
- Confidence intervals
- Hypothesis testing framework
- p-values and significance
- Type I and Type II errors
- Statistical power
- Frequentist vs Bayesian approaches
- Bayesian updating

**ML Applications**: Model evaluation, A/B testing, comparing model performance.

**Key takeaway**: Statistical inference enables us to make valid conclusions from data and evaluate ML models rigorously.

**Duration**: 3-4 hours

---

### [07. Neural Network Mathematics](./foundational/07_neural_network_math.ipynb)
**Topics covered:**
- Backpropagation and chain rule
- Vanishing and exploding gradients
- Residual connections (ResNets)
- Batch normalization mathematics
- Attention mechanisms (scaled dot-product)
- Convolution operations

**ML Applications**: Understanding modern deep learning architectures, debugging training issues.

**Key takeaway**: Modern neural networks combine multiple mathematical techniques to enable deep learning.

**Duration**: 4-5 hours

---

### [08. Advanced Linear Algebra](./foundational/08_advanced_linear_algebra.ipynb)
**Topics covered:**
- Eigendecomposition in depth
- Singular Value Decomposition (SVD)
- Low-rank matrix approximation
- Principal Component Analysis (PCA)
- Image compression with SVD
- Matrix factorization for recommender systems

**ML Applications**: Dimensionality reduction, feature extraction, collaborative filtering, data compression.

**Key takeaway**: Matrix decompositions are the foundation of many ML algorithms from PCA to recommender systems.

**Duration**: 4-5 hours

---

## Part II: MML Book - Mathematical Foundations (Chapters 2-7)

**Location**: `mml-book/` folder

> **Based on**: [Mathematics for Machine Learning](https://mml-book.github.io/) by Deisenroth, Faisal, and Ong

These notebooks provide hands-on Python implementations of the mathematical concepts from the MML textbook, with ~150+ executable code cells covering all foundational chapters.

### [01. Linear Algebra](./mml-book/01_linear_algebra.ipynb) - Chapter 2
**Topics covered:**
- Systems of linear equations and Gaussian elimination
- Matrices and matrix operations
- Solving linear systems (geometric and algorithmic perspectives)
- Vector spaces, linear independence, basis, and rank
- Linear mappings and transformations
- Affine spaces

**Implementations**: Gaussian elimination from scratch, matrix operations, Gram-Schmidt orthogonalization, geometric transformations (rotation, scaling, shear)

**Key ML connections**: Data representation, linear regression, neural network layers

**Cells**: 20+ | **Duration**: 5-6 hours

---

### [02. Analytic Geometry](./mml-book/02_analytic_geometry.ipynb) - Chapter 3
**Topics covered:**
- Norms (L1, L2, L∞) and their properties
- Inner products and orthogonality
- Lengths, distances, and angles
- Orthonormal bases and Gram-Schmidt process
- Orthogonal projections (vectors and subspaces)
- Rotations and reflections

**Implementations**: Different norm visualizations, inner product computations, Gram-Schmidt, 2D/3D projections, rotation matrices

**Key ML connections**: Distance metrics, similarity measures, feature transformations

**Cells**: 18+ | **Duration**: 4-5 hours

---

### [03. Matrix Decompositions](./mml-book/03_matrix_decompositions.ipynb) - Chapter 4
**Topics covered:**
- Determinant and trace
- Eigenvalues and eigenvectors (geometric interpretation)
- Cholesky decomposition
- Eigendecomposition and diagonalization
- Singular Value Decomposition (SVD)
- Matrix approximation (low-rank)

**Implementations**: Eigenvalue computation, Cholesky solving, SVD visualization, image compression demo, matrix powers via eigendecomposition

**Key ML connections**: PCA, spectral clustering, image compression, collaborative filtering

**Cells**: 22+ | **Duration**: 5-6 hours

---

### [04. Vector Calculus](./mml-book/04_vector_calculus.ipynb) - Chapter 5
**Topics covered:**
- Differentiation of univariate functions
- Partial differentiation and gradients
- Jacobian matrices
- Gradients of vector-valued functions
- Backpropagation and automatic differentiation
- Higher-order derivatives (Hessian)
- Taylor series approximation

**Implementations**: Numerical derivatives, gradient computation, Jacobian examples, manual backpropagation, Hessian computation, Taylor approximations

**Key ML connections**: Gradient descent, neural network training, second-order optimization

**Cells**: 25+ | **Duration**: 6-7 hours

---

### [05. Probability and Distributions](./mml-book/05_probability.ipynb) - Chapter 6
**Topics covered:**
- Probability spaces and probability theory axioms
- Discrete and continuous distributions
- Sum rule, product rule, Bayes' theorem
- Summary statistics (mean, variance, covariance)
- Gaussian distribution (univariate and multivariate)
- Joint, marginal, and conditional distributions
- Covariance and correlation

**Implementations**: Distribution sampling and visualization, Bayes' theorem examples, multivariate Gaussians, covariance matrix analysis

**Key ML connections**: Probabilistic models, MLE, Bayesian inference, GMMs

**Cells**: 20+ | **Duration**: 5-6 hours

---

### [06. Continuous Optimization](./mml-book/06_optimization.ipynb) - Chapter 7
**Topics covered:**
- Optimization using gradient descent
- Gradients and directional derivatives
- Constrained optimization and Lagrange multipliers
- Convex optimization
- Learning rate selection and momentum
- Numerical vs analytical solutions

**Implementations**: Gradient descent (1D and 2D), momentum variants, Lagrange multiplier examples, convexity demonstrations, learning rate comparisons

**Key ML connections**: Training algorithms, loss minimization, SVM dual problem

**Cells**: 25+ | **Duration**: 5-6 hours

---

## Part III: MML Book - ML Applications (Chapters 9-12)

These notebooks demonstrate how the mathematical foundations are applied to real machine learning algorithms, with complete implementations from scratch plus sklearn comparisons.

### [07. Linear Regression](./mml-book/07_linear_regression.ipynb) - Chapter 9
**Topics covered:**
- Problem formulation (matrix form)
- Maximum Likelihood Estimation (MLE)
- Normal equations: w = (X^T X)^{-1} X^T y
- Regularization: Ridge (L2) and Lasso (L1)
- Bayesian linear regression with uncertainty quantification
- Model selection and bias-variance tradeoff

**Implementations**: MLE from scratch, polynomial regression, Ridge/Lasso comparison, Bayesian regression with predictive uncertainty, cross-validation

**Real-world examples**: Synthetic data fitting, high-dimensional sparse problems, uncertainty visualization

**Key insights**: MLE ≡ minimizing squared error, L1 produces sparsity, Bayesian approach quantifies uncertainty

**Cells**: 22+ | **Duration**: 5-6 hours

---

### [08. Dimensionality Reduction with PCA](./mml-book/08_pca.ipynb) - Chapter 10
**Topics covered:**
- Problem setting (high-D → low-D)
- Maximum variance perspective
- Projection and reconstruction perspective
- Eigendecomposition of covariance matrix
- SVD for PCA (efficient computation)
- Scree plots and explained variance
- Data whitening and preprocessing

**Implementations**: PCA from scratch (both eigendecomposition and SVD), scree plots, reconstruction with varying components, whitening transformation

**Real-world examples**: Handwritten digits (MNIST), 3D → 2D visualization, image compression

**Key insights**: Maximizing variance ≡ minimizing reconstruction error, principal components are eigenvectors of covariance matrix

**Cells**: 20+ | **Duration**: 5-6 hours

---

### [09. Density Estimation with GMM](./mml-book/09_gmm.ipynb) - Chapter 11
**Topics covered:**
- Gaussian Mixture Models (mixture of Gaussians)
- Expectation-Maximization (EM) algorithm
- E-step: Computing responsibilities (soft assignments)
- M-step: Updating parameters (means, covariances, weights)
- Soft vs hard clustering
- Model selection with BIC/AIC
- Latent variable perspective

**Implementations**: EM algorithm from scratch, responsibility visualization with pie charts, covariance ellipses, BIC/AIC comparison, anomaly detection

**Real-world examples**: Synthetic mixture data, density estimation, clustering with uncertainty

**Key insights**: EM guarantees convergence, soft clustering captures uncertainty, GMM can model complex distributions

**Cells**: 18+ | **Duration**: 5-6 hours

---

### [10. Classification with SVM](./mml-book/10_svm.ipynb) - Chapter 12
**Topics covered:**
- Separating hyperplanes and margins
- Maximum margin principle
- Primal optimization problem (convex QP)
- Dual formulation with Lagrange multipliers
- Support vectors and KKT conditions
- Kernel trick (linear, polynomial, RBF)
- Soft margin SVM (slack variables and C parameter)

**Implementations**: Linear SVM visualization, kernel comparisons (linear/poly/RBF), decision boundaries, support vector identification, hyperparameter tuning

**Real-world examples**: XOR pattern (nonlinear), handwritten digit classification (3 vs 8), overlapping data

**Key insights**: Kernel trick enables nonlinear classification without explicit feature mapping, C controls bias-variance tradeoff

**Cells**: 20+ | **Duration**: 5-6 hours

---

## 🎯 Learning Paths

Choose your path based on your goals and background:

### Path 1: Foundations First (Recommended for Beginners)
**Best for**: Those new to ML or wanting a solid mathematical foundation

**Estimated time**: 6-8 weeks (30-40 hours)

1. **00. Python ML Libraries** (2-3h) - Essential tools
2. **01. Linear Algebra Fundamentals** (3-4h) - Core concepts
3. **02. Calculus & Derivatives** (3-4h) - Optimization basics
4. **03. Probability & Statistics** (4-5h) - Uncertainty and inference
5. **04. Gradient Descent** (3-4h) - Core training algorithm
6. **05. Information Theory** (2-3h) - Loss functions
7. **06. Statistical Inference** (3-4h) - Model evaluation
8. **07. Neural Network Mathematics** (4-5h) - Deep learning math
9. **08. Advanced Linear Algebra** (4-5h) - Dimensionality reduction

### Path 2: MML Book Track (Comprehensive Theory + Practice)
**Best for**: Those following the MML textbook or wanting rigorous mathematical treatment

**Estimated time**: 10-12 weeks (60-70 hours)

**Part I - Mathematical Foundations** (6-8 weeks, 30-35 hours):
1. **00. Python ML Libraries** (2-3h) - Setup
2. **01. Linear Algebra** (5-6h) - Chapter 2
3. **02. Analytic Geometry** (4-5h) - Chapter 3  
4. **03. Matrix Decompositions** (5-6h) - Chapter 4
5. **04. Vector Calculus** (6-7h) - Chapter 5
6. **05. Probability and Distributions** (5-6h) - Chapter 6
7. **06. Continuous Optimization** (5-6h) - Chapter 7

**Part II - ML Applications** (4-6 weeks, 20-25 hours):
8. **07. Linear Regression** (5-6h) - Chapter 9
9. **08. PCA** (5-6h) - Chapter 10
10. **09. GMM** (5-6h) - Chapter 11
11. **10. SVM** (5-6h) - Chapter 12

### Path 3: Quick ML Essentials (Fast Track)
**Best for**: Practitioners who need ML math quickly

**Estimated time**: 3-4 weeks (15-20 hours)

1. **00. Python ML Libraries** (2h) - Speed through
2. **01. Linear Algebra Fundamentals** (2h) - Core operations
3. **02. Calculus & Derivatives** (2h) - Gradients only
4. **04. Gradient Descent** (2h) - Main algorithm
5. **07. Linear Regression** (3h) - First ML algorithm
6. **08. PCA** (3h) - Dimensionality reduction
7. **10. SVM** (3h) - Classification

### Path 4: Deep Learning Focus
**Best for**: Those specifically interested in neural networks

**Estimated time**: 4-5 weeks (20-25 hours)

1. **00. Python ML Libraries** (2h)
2. **02. Calculus & Derivatives** (3h) - Backpropagation foundation
3. **04. Gradient Descent** (3h) - Optimizer algorithms
4. **04. Vector Calculus** (4h) - Chain rule, Jacobians
5. **05. Information Theory** (2h) - Loss functions
6. **07. Neural Network Mathematics** (4h) - Backprop, attention
7. **07. Linear Regression** (3h) - Basic neural net
8. **03. Matrix Decompositions** (3h) - Advanced architectures

---

## 📊 Complete Coverage Status

| Notebook | Topic | Type | Cells | Duration | Status |
|----------|-------|------|-------|----------|--------|
| 00 | Python ML Libraries | Foundation | 18+ | 2-3h | ✅ Complete |
| 01a | Linear Algebra Fundamentals | Foundation | 15+ | 3-4h | ✅ Complete |
| 02 | Calculus & Derivatives | Foundation | 20+ | 3-4h | ✅ Complete |
| 03 | Probability & Statistics | Foundation | 20+ | 4-5h | ✅ Complete |
| 04 | Gradient Descent | Foundation | 18+ | 3-4h | ✅ Complete |
| 05 | Information Theory | Foundation | 15+ | 2-3h | ✅ Complete |
| 06 | Statistical Inference | Foundation | 18+ | 3-4h | ✅ Complete |
| 07 | Neural Network Math | Foundation | 20+ | 4-5h | ✅ Complete |
| 08 | Advanced Linear Algebra | Foundation | 20+ | 4-5h | ✅ Complete |
| 01 | Linear Algebra (Ch 2) | MML Theory | 20+ | 5-6h | ✅ Complete |
| 02 | Analytic Geometry (Ch 3) | MML Theory | 18+ | 4-5h | ✅ Complete |
| 03 | Matrix Decompositions (Ch 4) | MML Theory | 22+ | 5-6h | ✅ Complete |
| 04 | Vector Calculus (Ch 5) | MML Theory | 25+ | 6-7h | ✅ Complete |
| 05 | Probability (Ch 6) | MML Theory | 20+ | 5-6h | ✅ Complete |
| 06 | Optimization (Ch 7) | MML Theory | 25+ | 5-6h | ✅ Complete |
| 07 | Linear Regression (Ch 9) | MML Application | 22+ | 5-6h | ✅ Complete |
| 08 | PCA (Ch 10) | MML Application | 20+ | 5-6h | ✅ Complete |
| 09 | GMM (Ch 11) | MML Application | 18+ | 5-6h | ✅ Complete |
| 10 | SVM (Ch 12) | MML Application | 20+ | 5-6h | ✅ Complete |

**Total**: 19 notebooks | **~350+ code cells** | **~80-100 hours of content**

---

## � Prerequisites & Setup

### Required Python Libraries

All notebooks use standard scientific Python stack:

```bash
# Core dependencies
pip install numpy matplotlib seaborn scipy scikit-learn jupyter

# Optional (for specific notebooks)
pip install sympy  # Symbolic mathematics (some advanced notebooks)
```

### Using with Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### Library Usage Across Notebooks

- **NumPy**: Numerical computing, array operations, linear algebra
- **Matplotlib**: 2D/3D plotting and visualization
- **Seaborn**: Statistical plots and heatmaps
- **SciPy**: Scientific computing, optimization, distributions
- **scikit-learn**: ML algorithms for comparison/validation
- **SymPy**: Symbolic math (derivatives, integrals)

---

## 🚀 Getting Started

### Step 1: Set Up Environment

```bash
# Navigate to directory
cd aiml/2-maths

# Install dependencies (if not already installed)
pip install numpy matplotlib seaborn scipy scikit-learn jupyter
```

### Step 2: Launch Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook

# Or use JupyterLab (modern interface)
jupyter lab
```

### Step 3: Choose Your Path

- **New to ML?** → Start with [Path 1](#path-1-foundations-first-recommended-for-beginners)
- **Following MML book?** → Follow [Path 2](#path-2-mml-book-track-comprehensive-theory--practice)
- **Need quick essentials?** → Try [Path 3](#path-3-quick-ml-essentials-fast-track)
- **Deep learning focus?** → Use [Path 4](#path-4-deep-learning-focus)

### Step 4: Run & Learn

Each notebook is self-contained and follows this structure:

1. **Overview** - What you'll learn and why it matters
2. **Setup** - Imports and configuration
3. **Theory** - Mathematical concepts with clear explanations
4. **Implementations** - Python code from scratch
5. **Visualizations** - Plots and diagrams for intuition
6. **Applications** - Real ML use cases
7. **Summary** - Key takeaways and connections

**💡 Pro Tip**: Run every code cell sequentially! Experiment with parameters to build intuition.

---

## ✍️ Practice with Exercises

**Location**: `exercises/` folder

Master the concepts through hands-on exercises! Four dedicated exercise notebooks with solutions:

### Part I: Mathematical Foundations (Chapters 2-7)

**📝 [mml_exercises_part1.ipynb](./exercises/mml_exercises_part1.ipynb)** - Practice problems for:
- Linear Algebra (Gaussian elimination, bases, transformations)
- Analytic Geometry (norms, projections, Gram-Schmidt)
- Matrix Decompositions (eigenvalues, SVD, Cholesky)
- Vector Calculus (gradients, Jacobians, backpropagation)
- Probability (Bayes' theorem, Gaussians, distributions)
- Optimization (gradient descent, momentum, constraints)

**24+ exercises** with difficulty levels: 🟢 Basic | 🟡 Intermediate | 🔴 Advanced

**✅ [mml_solutions_part1.ipynb](./exercises/mml_solutions_part1.ipynb)** - Complete solutions with:
- Step-by-step implementations
- Detailed explanations
- Visualizations and plots
- Verification steps

### Part II: ML Applications (Chapters 9-12)

**📝 [mml_exercises_part2.ipynb](./exercises/mml_exercises_part2.ipynb)** - Apply math to ML:
- Linear Regression (MLE, regularization, Bayesian uncertainty)
- PCA (eigendecomposition, SVD, dimensionality reduction)
- GMM (EM algorithm, model selection, soft clustering)
- SVM (kernels, margin, multi-class classification)

**16+ exercises** including end-to-end ML pipeline challenge

**✅ [mml_solutions_part2.ipynb](./exercises/mml_solutions_part2.ipynb)** - Comprehensive solutions featuring:
- From-scratch implementations
- Comparison with sklearn
- Performance analysis
- Real dataset applications

### Exercise Workflow

1. **Attempt exercises** without looking at solutions
2. **Compare your approach** with provided solutions
3. **Experiment** - Modify parameters, try variations
4. **Build intuition** - Understand why, not just how

**⏱️ Time estimate**: ~15-20 hours for all exercises (worthwhile investment!)

---

## 📖 Additional Mathematics Resources

For deeper study beyond the notebooks, explore these curated resources.

### 📚 Essential Textbooks

**Primary Reference:**
- **[Mathematics for Machine Learning](https://mml-book.github.io/)** by Deisenroth, Faisal, and Ong (2020)
  - Free textbook covering linear algebra, calculus, probability for ML
  - Part I: Mathematical foundations | Part II: ML applications

**Classic ML Texts:**
- **Bishop (2006)** - *Pattern Recognition and Machine Learning*
- **Murphy (2022)** - *Probabilistic Machine Learning*

### 🎥 Video Courses & Channels

**[3Blue1Brown](https://www.3blue1brown.com/)** by Grant Sanderson (⭐ Highly recommended)
- [Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
- Differential Equations, Multivariable Calculus
- Central Limit Theorem, Convolutions
- Binomial Distributions, Neural Networks

**University Courses:**
- **[MIT 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)** - Gilbert Strang's Linear Algebra (legendary!)
- **[Khan Academy](https://www.khanacademy.org/)** - Linear Algebra, Calculus, Statistics & Probability
- **Professor Leonard** - Comprehensive Calculus series
- **Steve Brunton** - Control theory, SVD, Dynamic Mode Decomposition

**Specialized Channels:**
- Math Visual Proofs
- MIT 6.006 Introduction to Algorithms

### 💻 Online Learning Platforms

**Interactive Courses:**
- **[Coursera](https://www.coursera.org/)** - Mathematics for Machine Learning Specialization
- **EdX** - Math for Machine Learning with Python
- **[Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)** - Prerequisites section
- **[Seeing Theory](https://seeing-theory.brown.edu/)** - Visual introduction to probability and statistics
- **Linear Algebra Done Right** - Videos by Axler
- **Probability for Data Science (P4D)**

### 🧮 Advanced Topics Reference

**Statistical Thinking (M0):**
- Probability, random variables, distributions
- Model vs. reality, digital twins
- Structure and causality
- Inference vs. generalization
- Measurement errors

**Statistical Inference (M1):**
- Data generating process, sample vs. population
- Frequentist and Bayesian approaches
- Model quality and performance measurement

**Econometrics (M2):**
- Linear regression and OLS
- Violation of OLS assumptions
- Estimation techniques: OLS, GMM, MLE, Bayesian

**Advanced Mathematics (M8):**
- Combinatorics
- Mathematical statistics (point estimation, confidence intervals, hypothesis testing)
- Central limit theorems, asymptotics, convergence
- Non-parametric statistics
- Differential equations and random processes
- Measure theory foundations

### 🤖 Math for Neural Networks & Deep Learning

**Core Concepts:**
- Gradient descent and backpropagation
- Matrix multiplication for layer operations
- Chain rule for backpropagation
- Derivatives for optimization
- Linear algebra for transformations

**Advanced NN Math:**
- Gradient flow through deep networks
- Residual connections for gradient preservation
- Gradient accumulation for large batches
- Vanishing/exploding gradients problem
- Attention mechanisms (mathematical foundations)

---

## Part V: CS229 Course - Stanford Machine Learning 🆕

**Location**: `cs229-course/` folder  
**Instructor**: Andrew Ng, Stanford University  
**Status**: 3/14 lectures complete, more coming soon!

### What is CS229?

Stanford's **CS229: Machine Learning** is one of the most influential ML courses in the world. This implementation provides:
- Comprehensive lecture notebooks with theory and code
- Real dataset implementations
- 140+ practice exercises
- 10 major projects
- Complete Python implementations from scratch

### Available Lectures

1. **[Linear Regression](./cs229-course/01_linear_regression.ipynb)** ✅
   - Normal equation, gradient descent variants
   - Learning rate analysis, feature scaling
   - California Housing dataset
   
2. **[Logistic Regression](./cs229-course/02_logistic_regression.ipynb)** ✅
   - Binary and multi-class classification
   - Decision boundaries, ROC curves
   - Breast cancer prediction
   
3. **[Regularization](./cs229-course/03_regularization.ipynb)** ✅
   - Ridge, Lasso, Elastic Net
   - Cross-validation, learning curves
   - Feature selection with Lasso

**Coming Soon**: Generative Models, SVMs, Neural Networks, Clustering, PCA, RL, and more!

### Resources

- **[CS229 README](./cs229-course/README.md)** - Complete course guide
- **[Practice Exercises](./cs229-course/CS229_PRACTICE.md)** - 140+ problems
- **[Requirements](./cs229-course/requirements.txt)** - Python dependencies

**Estimated time**: 14 weeks (8-15 hours/week)

---

### 🐍 Essential Python Libraries

**Mathematical Computing:**
- **NumPy** - Numerical computing, arrays, linear algebra
- **SciPy** - Scientific computing, optimization, statistics
- **SymPy** - Symbolic mathematics
- **Pandas** - Data manipulation and analysis

**Visualization:**
- **Matplotlib** - Foundational plotting library
- **Seaborn** - Statistical data visualization
- **Plotly** - Interactive visualizations

### 💡 Study Tips

> **Important**: You need basic comfort with mathematical notation rather than expert-level mathematics. The key areas are:
> 
> 1. **Linear Algebra** - Matrix multiplication, transformations
> 2. **Calculus** - Derivatives, gradients, chain rule
> 3. **Probability** - Distributions, expected values, variance
> 
> **Understanding concepts is more important than deep mathematical mastery!**

**Recommended approach:**
1. Work through the notebooks in this directory first
2. Use external resources to deepen understanding of specific topics
3. Practice with real ML problems to cement concepts
4. Return to theory when you encounter gaps in understanding

