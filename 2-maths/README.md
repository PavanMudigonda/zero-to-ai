# Mathematics for Machine Learning

This directory contains comprehensive Jupyter notebooks covering the mathematical foundations essential for understanding and implementing machine learning algorithms.

## 📚 Interactive Notebooks

### [00. Python ML Libraries](./00_python_ml_libraries.ipynb)
**Prerequisites for all math notebooks**
- NumPy fundamentals and array operations
- Matplotlib for plotting and visualization
- Seaborn for statistical plots
- SciPy for scientific computing
- scikit-learn basics for ML applications

**Start here** if you're new to Python's scientific computing ecosystem.

---

### [01. Linear Algebra Fundamentals](./01_linear_algebra_fundamentals.ipynb)
**Topics covered:**
- Vectors and vector operations (addition, scalar multiplication, dot product)
- Matrices and matrix operations (multiplication, transpose, inverse)
- Eigenvalues and eigenvectors
- Linear transformations
- **ML Applications**: Linear regression using the Normal Equation, data transformations

**Key takeaway**: Linear algebra is the language of ML - from data representation to neural network operations.

---

### [02. Calculus & Derivatives](./02_calculus_derivatives.ipynb)
**Topics covered:**
- Derivatives and their geometric interpretation
- Common activation functions (ReLU, Sigmoid, Tanh) and their derivatives
- Partial derivatives for multivariable functions
- Gradient vectors
- Chain rule for backpropagation
- Gradient descent basics

**ML Applications**: Understanding how neural networks learn through gradient-based optimization.

**Key takeaway**: Calculus enables optimization - the foundation of training ML models.

---

### [03. Probability & Statistics](./03_probability_statistics.ipynb)
**Topics covered:**
- Probability fundamentals (rules, conditional probability)
- Random variables (discrete and continuous)
- Common distributions (Bernoulli, Binomial, Normal/Gaussian)
- Bayes' theorem
- Central Limit Theorem
- Expected value and variance

**ML Applications**: Maximum Likelihood Estimation (MLE), Naive Bayes classifier.

**Key takeaway**: Probability theory provides the mathematical framework for reasoning under uncertainty.

---

### [04. Gradient Descent](./04_gradient_descent.ipynb)
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

---

### [05. Information Theory](./05_information_theory.ipynb)
**Topics covered:**
- Shannon entropy and information content
- Cross-entropy loss (the main loss function in deep learning)
- Kullback-Leibler (KL) divergence
- Mutual information
- Binary and categorical cross-entropy

**ML Applications**: Neural network loss functions, model evaluation, distribution comparison.

**Key takeaway**: Information theory provides the mathematical foundation for loss functions and measuring uncertainty.

---

### [06. Statistical Inference](./06_statistical_inference.ipynb)
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

---

### [07. Neural Network Mathematics](./07_neural_network_math.ipynb)
**Topics covered:**
- Backpropagation and chain rule
- Vanishing and exploding gradients
- Residual connections (ResNets)
- Batch normalization mathematics
- Attention mechanisms (scaled dot-product)
- Convolution operations

**ML Applications**: Understanding modern deep learning architectures, debugging training issues.

**Key takeaway**: Modern neural networks combine multiple mathematical techniques to enable deep learning.

---

### [08. Advanced Linear Algebra](./08_advanced_linear_algebra.ipynb)
**Topics covered:**
- Eigendecomposition in depth
- Singular Value Decomposition (SVD)
- Low-rank matrix approximation
- Principal Component Analysis (PCA)
- Image compression with SVD
- Matrix factorization for recommender systems

**ML Applications**: Dimensionality reduction, feature extraction, collaborative filtering, data compression.

**Key takeaway**: Matrix decompositions are the foundation of many ML algorithms from PCA to recommender systems.

---

## 🎯 Learning Path

**Recommended order for beginners:**

1. **00. Python ML Libraries** - Get familiar with the tools
2. **01. Linear Algebra** - Foundation for data representation
3. **02. Calculus** - Understand optimization mechanics
4. **03. Probability** - Handle uncertainty and probabilistic models
5. **04. Gradient Descent** - The core training algorithm

**Advanced topics** (can be studied in any order after the basics):

6. **05. Information Theory** - Understanding loss functions
7. **06. Statistical Inference** - Model evaluation and testing
8. **07. Neural Network Math** - Deep learning foundations
9. **08. Advanced Linear Algebra** - Dimensionality reduction and decompositions

## 📊 Coverage Status

| Topic | Notebook | Status |
|-------|----------|--------|
| Python Libraries | 00 | ✅ Complete |
| Linear Algebra Basics | 01 | ✅ Complete |
| Calculus & Derivatives | 02 | ✅ Complete |
| Probability & Statistics | 03 | ✅ Complete |
| Gradient Descent | 04 | ✅ Complete |
| Information Theory | 05 | ✅ Complete |
| Statistical Inference | 06 | ✅ Complete |
| Neural Network Math | 07 | ✅ Complete |
| Advanced Linear Algebra | 08 | ✅ Complete |

## 🔧 Prerequisites

### Required Python Libraries
```bash
pip install numpy matplotlib seaborn scipy scikit-learn jupyter
```

### Individual imports used across notebooks:
- **NumPy**: Numerical computing, matrix operations
- **Matplotlib**: Plotting and visualization
- **Seaborn**: Statistical visualizations
- **SciPy**: Scientific computing, statistical distributions
- **scikit-learn**: ML demonstrations

## 🚀 Quick Start

1. **Clone or navigate to this directory**
   ```bash
   cd aiml/2-maths
   ```

2. **Launch Jupyter**
   ```bash
   jupyter notebook
   ```

3. **Open any notebook** and run cells sequentially

## 💡 How to Use These Notebooks

Each notebook follows this structure:
- **Theory**: Mathematical concepts explained clearly
- **Code Examples**: Hands-on Python implementations
- **Visualizations**: Plots to build intuition
- **ML Applications**: Real-world machine learning use cases
- **Practice Exercises**: Test your understanding

**Tip**: Run every code cell! The notebooks are designed to be interactive - experiment with parameters and see how results change.

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

