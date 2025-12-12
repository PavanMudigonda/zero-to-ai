# CS229: Machine Learning Course (Stanford University)

A comprehensive implementation of Stanford's CS229 Machine Learning course using Python. This collection provides hands-on, code-first implementations of all major machine learning algorithms covered in the course.

## 📚 Course Overview

**Instructor**: Andrew Ng  
**Institution**: Stanford University  
**Focus**: Foundational machine learning algorithms and theory  
**Implementation**: Python with NumPy, scikit-learn, and modern ML libraries  

### What You'll Learn

- **Supervised Learning**: Regression, Classification, Neural Networks
- **Unsupervised Learning**: Clustering, PCA, ICA
- **Learning Theory**: Bias-variance, VC dimension, PAC learning
- **Optimization**: Gradient descent variants, Newton's method
- **Practical Skills**: Feature engineering, debugging ML systems

## 🗂️ Lecture Structure

### Part I: Supervised Learning

#### Lecture 1: Linear Regression
**File**: `01_linear_regression.ipynb`

**Topics**:
- Machine learning introduction and motivation
- Linear regression hypothesis and cost function
- Gradient descent (batch, stochastic, mini-batch)
- Normal equation (closed-form solution)
- Feature scaling and normalization
- Learning rate tuning

**Implementations**:
- Gradient descent from scratch
- Normal equation solver
- Vectorized implementations
- Learning rate comparison
- Multi-variate regression on California Housing

**Key Equations**:
```
Hypothesis: h_θ(x) = θᵀx
Cost: J(θ) = (1/2m)Σ(h_θ(x⁽ⁱ⁾) - y⁽ⁱ⁾)²
Update: θ := θ - α∇J(θ)
```

**Practice**: 8 exercises covering implementation, optimization, and analysis

---

#### Lecture 2: Logistic Regression (Classification)
**File**: `02_logistic_regression.ipynb`

**Topics**:
- Binary classification problem
- Logistic/sigmoid function
- Decision boundaries
- Cost function for classification
- Gradient descent for logistic regression
- Multi-class classification (One-vs-All)
- Advanced optimization (Newton's method)

**Implementations**:
- Sigmoid function and properties
- Binary classifier on breast cancer data
- Decision boundary visualization
- Multi-class classification on digits
- Comparison with linear regression for classification

**Key Equations**:
```
Hypothesis: h_θ(x) = g(θᵀx) where g(z) = 1/(1+e⁻ᶻ)
Cost: J(θ) = -(1/m)Σ[y log(h_θ(x)) + (1-y)log(1-h_θ(x))]
```

**Metrics**: Accuracy, Precision, Recall, F1-Score, ROC-AUC

---

#### Lecture 3: Regularization
**File**: `03_regularization.ipynb`

**Topics**:
- Overfitting and underfitting
- Regularization intuition
- Ridge regression (L2)
- Lasso regression (L1)
- Elastic Net
- Regularized logistic regression
- Choosing regularization parameter λ

**Demonstrations**:
- Polynomial overfitting example
- Regularization path visualization
- Cross-validation for λ selection
- Feature selection with Lasso
- Comparison of regularization methods

**Key Concepts**:
- Bias-variance trade-off
- Model complexity vs performance
- Structural risk minimization

---

#### Lecture 4: Generative Learning Algorithms
**File**: `04_generative_models.ipynb`

**Topics**:
- Discriminative vs generative models
- Gaussian Discriminant Analysis (GDA)
- Naive Bayes
- Laplace smoothing
- Text classification with Naive Bayes
- Event models for text

**Implementations**:
- GDA from scratch
- Naive Bayes for spam detection
- Multinomial vs Bernoulli event models
- Feature engineering for text

**Comparison**:
- Logistic Regression vs GDA
- When to use generative models

---

#### Lecture 5: Support Vector Machines
**File**: `05_support_vector_machines.ipynb`

**Topics**:
- Optimal margin classifier
- Functional and geometric margins
- Primal and dual formulation
- Kernel trick
- Common kernels (Linear, Polynomial, RBF, Sigmoid)
- Soft margin (slack variables)
- SMO algorithm (conceptual)

**Implementations**:
- SVM with different kernels
- Hyperparameter tuning (C, γ)
- Decision boundary visualization
- Support vector identification
- Multi-class SVM (OvO, OvR)

**Applications**:
- Image classification
- Text categorization
- Bioinformatics

---

#### Lecture 6: Neural Networks - Basics
**File**: `06_neural_networks_basics.ipynb`

**Topics**:
- Biological motivation
- Perceptron and activation functions
- Multi-layer perceptrons
- Backpropagation algorithm
- Gradient checking
- Weight initialization
- Mini-batch training

**Implementations**:
- Neural network from scratch
- Backpropagation step-by-step
- MNIST digit classification
- Activation function comparison
- Learning curve analysis

**Key Algorithms**:
- Forward propagation
- Backward propagation
- Parameter updates

---

#### Lecture 7: Neural Networks - Advanced
**File**: `07_neural_networks_advanced.ipynb`

**Topics**:
- Convolutional Neural Networks (CNNs)
- Recurrent Neural Networks (RNNs)
- Regularization techniques (Dropout, Batch Norm)
- Optimization algorithms (Adam, RMSprop)
- Transfer learning
- Practical tips and tricks

**Projects**:
- Image classification with CNNs
- Sequence modeling with RNNs
- Fine-tuning pretrained models

---

### Part II: Unsupervised Learning

#### Lecture 8: Clustering
**File**: `08_clustering.ipynb`

**Topics**:
- K-Means algorithm
- Choosing K (elbow method, silhouette)
- Hierarchical clustering
- DBSCAN
- Gaussian Mixture Models (GMM)
- EM algorithm

**Implementations**:
- K-Means from scratch
- Hierarchical clustering (all linkages)
- GMM with EM
- Cluster validation metrics
- Real applications (customer segmentation)

---

#### Lecture 9: Dimensionality Reduction
**File**: `09_dimensionality_reduction.ipynb`

**Topics**:
- Principal Component Analysis (PCA)
- Eigenvalue decomposition
- Singular Value Decomposition (SVD)
- Choosing number of components
- Independent Component Analysis (ICA)
- Factor Analysis
- Autoencoders

**Applications**:
- Data visualization
- Noise reduction
- Feature extraction
- Compression

---

#### Lecture 10: Anomaly Detection
**File**: `10_anomaly_detection.ipynb`

**Topics**:
- Gaussian distribution
- Anomaly detection algorithm
- Multivariate Gaussian
- Choosing threshold ε
- Anomaly detection vs supervised learning
- One-class SVM

**Use Cases**:
- Fraud detection
- Manufacturing defects
- System monitoring

---

### Part III: Learning Theory

#### Lecture 11: Learning Theory
**File**: `11_learning_theory.ipynb`

**Topics**:
- Bias and variance
- Regularization and model selection
- VC dimension
- PAC learning
- Sample complexity
- Error analysis

**Theoretical Results**:
- Hoeffding inequality
- Union bound
- Training/test error relationship

---

#### Lecture 12: ML Strategy
**File**: `12_ml_strategy.ipynb`

**Topics**:
- Orthogonalization
- Single number evaluation metric
- Train/dev/test distributions
- Human-level performance
- Error analysis
- Bias and variance with mismatched data
- Transfer learning
- Multi-task learning
- End-to-end deep learning

**Practical Advice**:
- Debugging learning algorithms
- Getting more data
- Feature engineering vs deep learning

---

### Part IV: Special Topics

#### Lecture 13: Recommender Systems
**File**: `13_recommender_systems.ipynb`

**Topics**:
- Content-based filtering
- Collaborative filtering
- Matrix factorization
- Deep learning for recommendations
- Evaluation metrics

**Implementation**:
- Movie recommendation system
- Item-item collaborative filtering
- Neural collaborative filtering

---

#### Lecture 14: Reinforcement Learning
**File**: `14_reinforcement_learning.ipynb`

**Topics**:
- Markov Decision Processes
- Value iteration
- Policy iteration
- Q-Learning
- Deep Q-Networks (DQN)
- Policy gradients

**Examples**:
- GridWorld
- CartPole
- Atari games (conceptual)

---

## 🚀 Getting Started

### Prerequisites

**Python**: 3.8+

**Required Libraries**:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy tensorflow torch
```

Or install from requirements:
```bash
pip install -r requirements.txt
```

### Installation

```bash
# Clone repository
git clone https://github.com/PavanMudigondaTR/aiml.git
cd aiml/2-maths/cs229-course

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

### Quick Start

```bash
# Start with Lecture 1
jupyter notebook 01_linear_regression.ipynb
```

## 📖 Learning Path

### Beginner Track (Weeks 1-4)
Focus on supervised learning fundamentals:
1. **Lecture 1**: Linear Regression
2. **Lecture 2**: Logistic Regression  
3. **Lecture 3**: Regularization
4. **Lecture 4**: Generative Models

**Time**: 4 weeks (10-15 hours/week)

### Intermediate Track (Weeks 5-8)
Advanced supervised learning:
5. **Lecture 5**: Support Vector Machines
6. **Lecture 6**: Neural Networks (Basics)
7. **Lecture 7**: Neural Networks (Advanced)
8. **Lecture 8**: Clustering

**Time**: 4 weeks (12-18 hours/week)

### Advanced Track (Weeks 9-12)
Unsupervised learning and theory:
9. **Lecture 9**: Dimensionality Reduction
10. **Lecture 10**: Anomaly Detection
11. **Lecture 11**: Learning Theory
12. **Lecture 12**: ML Strategy

**Time**: 4 weeks (10-15 hours/week)

### Specialized Topics (Weeks 13-14)
13. **Lecture 13**: Recommender Systems
14. **Lecture 14**: Reinforcement Learning

**Time**: 2 weeks (8-12 hours/week)

**Total Duration**: 14 weeks for comprehensive mastery

## 🎯 How to Use

### For Self-Study
1. Watch CS229 lecture videos (available on YouTube)
2. Read corresponding lecture notes
3. Work through notebook with code examples
4. Complete practice exercises
5. Implement algorithms from scratch
6. Apply to real datasets

### For Coursework
- Use as lab assignments
- Code walkthroughs in recitation
- Project templates
- Exam preparation

### For Reference
- Algorithm implementations
- Mathematical derivations
- Debugging templates
- Best practices

## 📊 Datasets Used

| Dataset | Lectures | Description |
|---------|----------|-------------|
| **California Housing** | 1, 3 | Regression, 8 features, 20k samples |
| **Breast Cancer** | 2, 5 | Binary classification, 30 features |
| **MNIST Digits** | 2, 6, 7 | Image classification, 28×28 pixels |
| **Iris** | 2, 4, 8 | Multi-class, 4 features, 150 samples |
| **20 Newsgroups** | 4 | Text classification |
| **MovieLens** | 13 | Recommender systems |
| **Synthetic** | Multiple | Generated for demonstrations |

## 🔑 Key Concepts Reference

### Supervised Learning

**Linear Models**:
```python
# Linear Regression
h(x) = θᵀx
J(θ) = (1/2m)Σ(h(x⁽ⁱ⁾) - y⁽ⁱ⁾)²

# Logistic Regression  
h(x) = σ(θᵀx) where σ(z) = 1/(1+e⁻ᶻ)
J(θ) = -(1/m)Σ[y log(h(x)) + (1-y)log(1-h(x))]
```

**Regularization**:
```python
# Ridge (L2)
J(θ) = MSE + λΣθⱼ²

# Lasso (L1)
J(θ) = MSE + λΣ|θⱼ|
```

**Neural Networks**:
```python
# Forward pass
aˡ = σ(Wˡaˡ⁻¹ + bˡ)

# Backward pass
δˡ = (Wˡ⁺¹)ᵀδˡ⁺¹ ⊙ σ'(zˡ)
```

### Unsupervised Learning

**K-Means**:
```python
1. Initialize centroids randomly
2. Assign points to nearest centroid
3. Update centroids as mean of assigned points
4. Repeat until convergence
```

**PCA**:
```python
1. Standardize data: X' = (X - μ)/σ
2. Compute covariance: Σ = (1/m)XᵀX
3. Eigendecomposition: Σ = UΛUᵀ
4. Project: X_reduced = XU_k
```

## 💡 Best Practices

### Code Quality
✅ Vectorize operations (avoid loops)  
✅ Document functions with docstrings  
✅ Use meaningful variable names  
✅ Add type hints  
✅ Write unit tests  

### Model Development
✅ Always split train/dev/test  
✅ Start simple, increase complexity  
✅ Visualize data before modeling  
✅ Monitor training curves  
✅ Perform error analysis  
✅ Compare multiple baselines  

### Debugging
When model doesn't work:
1. **Check data**: Visualize, check statistics
2. **Check implementation**: Gradient checking
3. **Check hyperparameters**: Learning rate, regularization
4. **Check convergence**: Plot cost function
5. **Check for bugs**: Unit tests, assertions

## 📝 Practice Problems

Each lecture includes:
- **5-8 in-lecture exercises**: Integrated with material
- **8-10 practice problems**: End of notebook
- **1-2 projects**: Apply to real datasets

### Additional Resources
See [CS229_PRACTICE.md](CS229_PRACTICE.md) for:
- 140+ additional exercises
- 10 comprehensive projects
- 5 challenge problems
- Solutions and hints

## 🏆 Projects

### Project 1: Housing Price Prediction
- **Dataset**: Boston/California Housing
- **Goal**: Predict prices with < 10% error
- **Techniques**: Linear regression, regularization, feature engineering

### Project 2: Spam Detection
- **Dataset**: SMS/Email spam
- **Goal**: Classify with > 95% accuracy
- **Techniques**: Naive Bayes, logistic regression, feature extraction

### Project 3: Handwritten Digit Recognition
- **Dataset**: MNIST
- **Goal**: Achieve > 98% test accuracy
- **Techniques**: Neural networks, CNNs

### Project 4: Customer Segmentation
- **Dataset**: E-commerce data
- **Goal**: Identify meaningful customer groups
- **Techniques**: K-Means, GMM, PCA

### Project 5: Movie Recommender
- **Dataset**: MovieLens
- **Goal**: Personalized recommendations
- **Techniques**: Collaborative filtering, matrix factorization

## 🤝 Contributing

Contributions welcome! Areas:
- Additional examples
- More exercises
- Bug fixes
- Performance improvements
- Documentation enhancements

## 📚 References

### Course Materials
- **CS229 Lecture Notes**: [Stanford CS229](http://cs229.stanford.edu/)
- **Video Lectures**: [YouTube Playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)
- **Andrew Ng**: Coursera Machine Learning

### Books
- **Pattern Recognition and Machine Learning**: Bishop
- **The Elements of Statistical Learning**: Hastie, Tibshirani, Friedman
- **Deep Learning**: Goodfellow, Bengio, Courville
- **Reinforcement Learning**: Sutton and Barto

### Online Resources
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Kaggle Learn](https://www.kaggle.com/learn)

## 📈 Progress Tracker

### Core Lectures (14 total)
- [ ] Lecture 1: Linear Regression
- [ ] Lecture 2: Logistic Regression
- [ ] Lecture 3: Regularization
- [ ] Lecture 4: Generative Models
- [ ] Lecture 5: Support Vector Machines
- [ ] Lecture 6: Neural Networks (Basics)
- [ ] Lecture 7: Neural Networks (Advanced)
- [ ] Lecture 8: Clustering
- [ ] Lecture 9: Dimensionality Reduction
- [ ] Lecture 10: Anomaly Detection
- [ ] Lecture 11: Learning Theory
- [ ] Lecture 12: ML Strategy
- [ ] Lecture 13: Recommender Systems
- [ ] Lecture 14: Reinforcement Learning

**Progress**: 0/14 lectures

### Practice
- [ ] Complete all in-lecture exercises (100+ problems)
- [ ] Complete practice problems (100+ problems)
- [ ] Complete 3+ projects
- [ ] Implement 1+ algorithm from scratch
- [ ] Participate in Kaggle competition

## 🎓 Learning Outcomes

After completing this course, you will:

✅ Understand fundamental ML algorithms deeply  
✅ Implement algorithms from scratch  
✅ Apply ML to real-world problems  
✅ Debug and improve ML systems  
✅ Choose appropriate algorithms for tasks  
✅ Understand theoretical foundations  
✅ Follow ML best practices  
✅ Build end-to-end ML pipelines  

## ⚖️ License

MIT License - Free for educational and commercial use

## 📧 Contact

**Repository**: [github.com/PavanMudigondaTR/aiml](https://github.com/PavanMudigondaTR/aiml)  
**Issues**: Report bugs via GitHub Issues  

## 🙏 Acknowledgments

- **Andrew Ng** and Stanford CS229 teaching staff
- scikit-learn, TensorFlow, and PyTorch communities
- All contributors to this repository

---

**Start Learning Today! 🚀**

*"Machine learning is the science of getting computers to learn without being explicitly programmed." - Arthur Samuel*
