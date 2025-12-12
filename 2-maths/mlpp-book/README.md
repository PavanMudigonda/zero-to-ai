# Machine Learning: A Probabilistic Perspective

This folder contains practical examples and implementations from Kevin Murphy's "Machine Learning: A Probabilistic Perspective" (MLPP). The book provides a comprehensive introduction to machine learning from a unified probabilistic perspective.

## 📚 Overview

The examples are organized by major topics from the book, focusing on hands-on implementation of key concepts and algorithms.

## 📁 Notebooks (13 Total)

### Part I: Foundations (Chapters 2-5)

1. **01_probability_fundamentals.ipynb** - Probability theory basics, Bayes' rule, probability distributions, information theory
2. **02_generative_models.ipynb** - Generative classifiers, Naive Bayes, discriminant analysis (Chapters 3-4)
3. **03_gaussian_models.ipynb** - Multivariate Gaussians, MVN inference, missing data, Gaussian mixtures
4. **04_bayesian_statistics.ipynb** - Bayesian inference, conjugate priors, posterior computation, empirical Bayes

### Part II: Regression and Classification (Chapters 7-8)

5. **05_linear_logistic_regression.ipynb** - Linear regression (MLE, Ridge, Bayesian), Logistic regression, Softmax classification

### Part III: Sparse Models and Regularization (Chapter 13)

6. **06_sparse_linear_models.ipynb** - Lasso, Elastic Net, coordinate descent, feature selection

### Part IV: Kernel Methods and Gaussian Processes (Chapter 14)

7. **07_kernels_gaussian_processes.ipynb** - Kernel trick, kernel ridge regression, SVMs, GP regression

### Part V: Graphical Models and Sequential Data (Chapters 10, 16-17)

8. **08_graphical_models.ipynb** - Bayesian networks, d-separation, Naive Bayes, Markov chains
9. **09_hidden_markov_models.ipynb** - HMMs, forward-backward algorithm, Viterbi decoding, Baum-Welch learning

### Part VI: Sampling and Inference (Chapters 21-24)

10. **10_mcmc_sampling.ipynb** - Monte Carlo methods, Metropolis-Hastings, Gibbs sampling, convergence diagnostics

### Part VII: Unsupervised Learning (Chapters 9, 11, 12, 25)

11. **11_mixture_models_em.ipynb** - Gaussian mixture models, EM algorithm, K-means, mixture of Bernoullis, BIC/AIC
12. **12_dimensionality_reduction.ipynb** - PCA, Probabilistic PCA, Factor Analysis, ICA, source separation
13. **13_clustering.ipynb** - K-means, hierarchical, spectral, DBSCAN, affinity propagation, evaluation metrics

## 🎯 Learning Objectives

After working through these notebooks, you will:

- Understand probability theory and Bayesian inference fundamentals
- Implement generative and discriminative classification models
- Work with graphical models, Bayesian networks, and HMMs
- Apply sparse models, regularization, and feature selection
- Use kernel methods, SVMs, and Gaussian processes
- Perform Bayesian inference with MCMC sampling methods
- Master unsupervised learning: clustering, dimensionality reduction, mixture models
- Understand EM algorithm and its applications
- Evaluate and compare different clustering algorithms

## 🚀 Quick Start

**Step 1:** Ensure you have the required dependencies:

```bash
pip install numpy scipy matplotlib scikit-learn pandas seaborn
```

**Step 2:** Start with the foundational notebooks (01-04) before moving to advanced topics

**Step 3:** Each notebook contains:

- Theory overview
- Code implementations
- Visualizations
- Practical examples
- Exercises

## 📖 Book Reference

Murphy, Kevin P. "Machine Learning: A Probabilistic Perspective." MIT Press, 2012.

The PDF is available in: `../resources/ML Machine Learning-A Probabilistic Perspective.pdf`

## 🔗 Related Sections

- [Foundational Math](../foundational/) - Core mathematical concepts
- [MML Book](../mml-book/) - Mathematics for Machine Learning
- [ISLP Book](../islp-book/) - Statistical Learning with Python
- [CS229 Course](../cs229-course/) - Stanford ML Course

## 💡 Tips

- The book uses MATLAB examples; these notebooks use Python equivalents
- Focus on understanding probabilistic reasoning and Bayesian inference
- Practice implementing algorithms from scratch before using libraries
- Compare implementations with scikit-learn and other ML libraries
- Follow the suggested order for foundational concepts, but feel free to explore topics independently
- Each notebook is self-contained with theory, code, and visualizations

## 📊 Coverage Summary

This collection covers approximately **50% of Murphy's MLPP book**, focusing on:

- ✅ Foundations (probability, Bayesian statistics)
- ✅ Supervised learning (regression, classification)
- ✅ Unsupervised learning (clustering, dimensionality reduction, mixture models)
- ✅ Graphical models (Bayesian networks, HMMs)
- ✅ Kernel methods and Gaussian processes
- ✅ MCMC and sampling methods
- ✅ EM algorithm and latent variable models

**Topics not yet covered:**

- Deep learning (Chapters 27-28)
- Advanced variational inference
- Advanced reinforcement learning
- Some specialized models and techniques

## 🤝 Contributing

Feel free to add more examples or improve existing ones following the established format.
