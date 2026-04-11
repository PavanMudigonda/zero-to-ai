# Mathematics for ML

Mathematical foundations for the rest of the curriculum. The goal is enough fluency to understand optimization, probability, embeddings, attention, and evaluation without treating them as magic.

## Folder Map

| Folder | Notebooks | Level | What It Covers |
|--------|-----------|-------|---------------|
| [foundational/](foundational/) | 13 | Beginner | Core math: linear algebra, calculus, probability, gradient descent, info theory, neural net math |
| [3blue1brown/](3blue1brown/) | 42 | Beginner | Visual intuition: calculus (12), linear algebra (13), differential equations (8), neural networks (9) |
| [mml-book/](mml-book/) | 24 | Intermediate | Mathematics for Machine Learning: course (10), exercises (4), practice labs (10) |
| [cs229-course/](cs229-course/) | 18 | Intermediate | Stanford CS229: regression, classification, SVMs, learning theory, clustering, RL |
| [islp-book/](islp-book/) | 15 | Intermediate | Intro to Statistical Learning: 13 chapters + practice exercises |
| [mlpp-book/](mlpp-book/) | 13 | Intermediate | ML: A Probabilistic Perspective: Bayesian inference, graphical models, MCMC, EM |
| [dli-book/](dli-book/) | 6 | Intermediate | Deep Learning Interviews: practice labs for logistic regression, info theory, CNNs |
| [slp-book/](slp-book/) | 6 | Intermediate | Speech & Language Processing: NLP labs from tokenization to transformers |
| [advanced/](advanced/) | 16 | Advanced | Research topics: learning theory, PAC-Bayes, NTK, variational inference, state space models |
| [ml-problem/](ml-problem/) | — | Reference | ML problem-solving reference PDF |

**Total: 153 notebooks across 10 folders**

## Quick Start

```bash
# Start here
jupyter notebook foundational/01_linear_algebra_fundamentals.ipynb
```

## Learning Paths

### Path 1: Beginner (start here)

Work through the foundational notebooks first. These cover the essentials:

1. [foundational/01 - Linear Algebra](foundational/01_linear_algebra_fundamentals.ipynb)
2. [foundational/02 - Calculus](foundational/02_calculus_derivatives.ipynb)
3. [foundational/03 - Probability](foundational/03_probability_statistics.ipynb)
4. [foundational/04 - Gradient Descent](foundational/04_gradient_descent.ipynb)
5. [foundational/05 - Information Theory](foundational/05_information_theory.ipynb)
6. [foundational/06 - Statistical Inference](foundational/06_statistical_inference.ipynb)
7. [foundational/07 - Neural Network Math](foundational/07_neural_network_math.ipynb)

Supplement with [3blue1brown/](3blue1brown/) notebooks for visual intuition on any topic that feels abstract.

### Path 2: ML Engineer

After the foundational pass, build depth in ML theory and algorithms:

1. [mml-book/course/](mml-book/course/) — rigorous math foundations (linear algebra through optimization)
2. [cs229-course/](cs229-course/) — Stanford ML algorithms (regression, SVMs, neural nets, RL)
3. [mml-book/practice-labs/](mml-book/practice-labs/) — hands-on implementation of MML concepts
4. [dli-book/](dli-book/) — deep learning interview math

### Path 3: Data Scientist

Statistical and probabilistic foundations:

1. [islp-book/](islp-book/) — statistical learning (regression, classification, resampling, trees, SVMs)
2. [mlpp-book/](mlpp-book/) — probabilistic perspective (Bayesian inference, graphical models, MCMC)
3. [slp-book/](slp-book/) — NLP and language model foundations

### Path 4: Researcher

Graduate-level theory (requires Path 1 + Path 2 as prerequisites):

1. [advanced/](advanced/) — learning theory, concentration inequalities, PAC-Bayes, NTK
2. [foundational/08 - Advanced Linear Algebra](foundational/08_advanced_linear_algebra.ipynb)
3. [foundational/12 - Optimization from Scratch](foundational/12_optimization_from_scratch_adam.ipynb)

## Topic Cross-Reference

Find the same topic at different depths across folders:

| Topic | Beginner | Intermediate | Advanced | Practice |
|-------|----------|-------------|----------|----------|
| **Linear Algebra** | [foundational/01](foundational/01_linear_algebra_fundamentals.ipynb), [3b1b/linear-algebra/](3blue1brown/linear-algebra/) | [mml-book/01](mml-book/course/01_linear_algebra.ipynb) | [foundational/08](foundational/08_advanced_linear_algebra.ipynb) | [mml-labs/01](mml-book/practice-labs/lab_01_linear_algebra.ipynb) |
| **Calculus** | [foundational/02](foundational/02_calculus_derivatives.ipynb), [3b1b/calculus/](3blue1brown/calculus/) | [mml-book/04](mml-book/course/04_vector_calculus.ipynb) | — | [mml-labs/04](mml-book/practice-labs/lab_04_vector_calculus.ipynb) |
| **Probability** | [foundational/03](foundational/03_probability_statistics.ipynb) | [mml-book/05](mml-book/course/05_probability.ipynb), [mlpp/01](mlpp-book/01_probability_fundamentals.ipynb) | — | [mml-labs/05](mml-book/practice-labs/lab_05_probability_distributions.ipynb), [dli/04](dli-book/lab_04_probability_bayesian.ipynb) |
| **Optimization** | [foundational/04](foundational/04_gradient_descent.ipynb) | [mml-book/06](mml-book/course/06_optimization.ipynb), [cs229/02](cs229-course/course/02_gradient_descent.ipynb) | [advanced/09](advanced/09_gradient_descent_convergence.ipynb) | [mml-labs/06](mml-book/practice-labs/lab_06_optimization.ipynb) |
| **Information Theory** | [foundational/05](foundational/05_information_theory.ipynb) | — | — | [dli/02](dli-book/lab_02_information_theory.ipynb) |
| **Regression** | — | [mml-book/07](mml-book/course/07_linear_regression.ipynb), [cs229/01](cs229-course/course/01_linear_regression.ipynb), [islp/03](islp-book/03_linear_regression.ipynb) | — | [mml-labs/07](mml-book/practice-labs/lab_07_linear_regression.ipynb) |
| **Classification** | — | [cs229/04](cs229-course/course/04_logistic_regression.ipynb), [islp/04](islp-book/04_classification.ipynb) | — | [dli/01](dli-book/lab_01_logistic_regression.ipynb) |
| **SVMs** | — | [mml-book/10](mml-book/course/10_svm.ipynb), [cs229/06](cs229-course/course/06_svm.ipynb), [islp/09](islp-book/09_support_vector_machines.ipynb) | — | [mml-labs/10](mml-book/practice-labs/lab_10_svm.ipynb) |
| **PCA** | — | [mml-book/08](mml-book/course/08_pca.ipynb), [cs229/14](cs229-course/course/14_dimensionality_reduction.ipynb) | — | [mml-labs/08](mml-book/practice-labs/lab_08_pca.ipynb) |
| **Neural Networks** | [foundational/07](foundational/07_neural_network_math.ipynb), [3b1b/neural-networks/](3blue1brown/neural-networks/) | [cs229/10-11](cs229-course/course/10_neural_networks_basics.ipynb), [islp/10](islp-book/10_deep_learning.ipynb) | — | [slp/04](slp-book/lab_04_neural_networks.ipynb) |
| **Transformers/LLMs** | — | — | — | [slp/05-06](slp-book/lab_05_transformers_attention.ipynb) |
| **Bayesian Methods** | — | [mlpp/04](mlpp-book/04_bayesian_statistics.ipynb), [mml-book/07](mml-book/course/07_linear_regression.ipynb) | [advanced/07](advanced/07_bayesian_nonparametrics.ipynb) | [dli/04](dli-book/lab_04_probability_bayesian.ipynb) |
| **Clustering/GMM** | — | [mml-book/09](mml-book/course/09_gmm.ipynb), [cs229/13](cs229-course/course/13_clustering.ipynb), [mlpp/11](mlpp-book/11_mixture_models_em.ipynb) | — | [mml-labs/09](mml-book/practice-labs/lab_09_gaussian_mixtures.ipynb) |

## Source PDFs

Each book folder contains its own PDF:

| PDF | Location |
|-----|----------|
| Mathematics for Machine Learning | [mml-book/mml-book.pdf](mml-book/mml-book.pdf) |
| Stanford CS229 Notes | [cs229-course/cs229.pdf](cs229-course/cs229.pdf) |
| Intro to Statistical Learning with Python | [islp-book/ISLP.pdf](islp-book/ISLP.pdf) |
| ML: A Probabilistic Perspective | [mlpp-book/ML-Machine-Learning-A-Probabilistic-Perspective.pdf](mlpp-book/ML-Machine-Learning-A-Probabilistic-Perspective.pdf) |
| Deep Learning Interviews | [dli-book/2201.00650v2.pdf](dli-book/2201.00650v2.pdf) |
| Speech & Language Processing | [slp-book/ed3book_jan26.pdf](slp-book/ed3book_jan26.pdf) |
| ML Problem Solving | [ml-problem/ml-problem.pdf](ml-problem/ml-problem.pdf) |

## Practical Rules

- Learn the intuition before the notation
- Re-derive small examples by hand when possible
- If a symbol-heavy notebook feels abstract, reconnect it to one use case: gradient descent, cosine similarity, cross-entropy, PCA, or attention
- Do not try to finish every notebook before continuing the curriculum
- Do not spend weeks on theorem-level depth if your goal is applied AI engineering

## Next Step

After the foundational notebooks, continue into [05-embeddings/](../05-embeddings/) and [06-neural-networks/](../06-neural-networks/), then come back here as needed.
