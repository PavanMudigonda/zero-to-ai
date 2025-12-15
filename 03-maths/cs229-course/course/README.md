# CS229: Machine Learning Course (Stanford University)

A comprehensive implementation of Stanford's CS229 Machine Learning course using Python. This collection provides hands-on, code-first implementations of all major machine learning algorithms covered in the course.

**🆕 Updated with actual lecture transcripts from Andrew Ng's 2018 MIT course!**  
Real examples, explanations, and insights from the original lectures integrated into interactive notebooks.

## 📚 Course Overview

**Instructor**: Andrew Ng  
**Institution**: Stanford University (Autumn 2018)  
**Source**: Lecture transcripts + [Official Syllabus](https://cs229.stanford.edu/syllabus-autumn2018.html)  
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
**Source**: Lecture 2 Transcript (Linear Regression lecture)

**Topics**:
- Machine learning introduction and motivation
- Portland Housing dataset example (from Craigslist)
- Linear regression hypothesis and cost function
- Gradient descent (batch, stochastic, mini-batch)
- Normal equation (closed-form solution)
- Feature scaling and normalization
- Learning rate tuning

**From the Lecture**:
> "Let's say you want to predict or estimate the prices of houses. This is data from Portland, Oregon..." - Andrew Ng

**Implementations**:
- Portland housing price prediction (real data from lecture!)
- Gradient descent from scratch
- Normal equation solver: θ = (XᵀX)⁻¹Xᵀy
- Vectorized implementations
- Learning rate comparison (α = 0.001, 0.01, 0.1, 0.5)
- Multi-variate regression on California Housing

**Key Equations**:
```
Hypothesis: h_θ(x) = θᵀx
Cost: J(θ) = (1/2m)Σ(h_θ(x⁽ⁱ⁾) - y⁽ⁱ⁾)²
Update: θ := θ - α∇J(θ)
Normal Equation: θ = (XᵀX)⁻¹Xᵀy
```

**Practice**: 8 exercises covering implementation, optimization, and analysis

---

#### Lecture 3: Locally Weighted Regression
**File**: [03_locally_weighted_regression.ipynb](03_locally_weighted_regression.ipynb) **[NEW!]**  
**Source**: Lecture 3 Transcript (LWR, Probabilistic Interpretation)

**Topics**:
- Parametric vs Non-parametric learning algorithms
- Locally weighted regression (LWR) algorithm
- Weight functions and bandwidth parameter τ
- Avoiding feature engineering
- Curse of dimensionality
- When to use LWR vs other methods

**From the Lecture**:
> "If you have curved data... it's quite difficult to find features. Is it √x, log(x), x³? What is the set of features that lets you do this? Locally weighted regression sidesteps all those problems." - Andrew Ng

**Implementations**:
- Complete LWR class from scratch
- Gaussian weight function: w⁽ⁱ⁾ = exp(-(x⁽ⁱ⁾-x)²/(2τ²))
- Weighted least squares: θ = (XᵀWX)⁻¹XᵀWy
- Bandwidth comparison (τ = 0.1, 0.5, 1.0, 2.0)
- Weight visualization for different query points
- Comparison: Linear vs Polynomial vs LWR

**Key Insights**:
- **Non-parametric**: Must keep training data around
- **Local fitting**: Different θ for each prediction
- **Automatic**: No feature engineering needed
- **Computational**: O(n³) per prediction

**Best For**:
✓ Low dimensional data (n ≤ 5)  
✓ Non-linear patterns  
✗ High dimensions  
✗ Real-time prediction

---

#### Lecture 2 & 4: Logistic Regression (Classification)  
**File**: `02_logistic_regression.ipynb` **[ENHANCED!]**  
**Source**: Lectures 3-4 Transcripts (Logistic Regression, Newton's Method)

**Topics**:
- Why linear regression fails for classification
- Binary classification problem
- Logistic/sigmoid function
- Decision boundaries (linear and non-linear)
- Cost function for classification (cross-entropy)
- Gradient descent for logistic regression
- **Newton's Method** (new!)
- Multi-class classification (One-vs-All)
- Regularization for logistic regression

**From the Lecture**:
> "Probably by far the most commonly used classification algorithm... Linear regression is just not a good algorithm for classification." - Andrew Ng

> "Gradient ascent takes baby steps, takes a lot of iterations. Newton's method allows you to take much bigger jumps - you might need only 10 iterations instead of 100 or 1000." - Andrew Ng

**New Implementations**:
- **Newton's Method from scratch**:
  - Second-order optimization
  - Hessian computation: H = XᵀDX
  - Update: θ := θ + H⁻¹∇ℓ(θ)
  - Convergence comparison with gradient ascent
  - 5-20x faster convergence!

**When to Use What**:
- Gradient Ascent: Large n (> 10,000 features)
- Newton's Method: Small to medium n (< 10,000 features)
- L-BFGS: Middle ground (used in sklearn)

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

#### Lecture 8: Regularization and Bias-Variance  
**File**: [04_regularization.ipynb](04_regularization.ipynb) **[ENHANCED!]**

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

#### Lecture 5-6: Generative Learning Algorithms  
**File**: [05_generative_models.ipynb](05_generative_models.ipynb) **[ENHANCED!]**  
**Source**: Lectures 5-6 Transcripts (GDA, Naive Bayes)

**Topics**:
- Discriminative vs Generative learning paradigms
- Bayes' rule framework: P(y|x) = P(x|y)P(y)/P(x)
- **Gaussian Discriminant Analysis (GDA)**
- Multivariate Gaussian distribution
- Covariance matrix visualization
- **Naive Bayes classifier**
- Laplace smoothing
- Text classification and spam filtering

**From the Lecture**:
> "Rather than looking at two classes and trying to find the separation, the algorithm looks at the classes one at a time." - Andrew Ng

**Multivariate Gaussian**:
> "The Gaussian is this familiar bell-shaped curve. A multivariate Gaussian is the generalization to vector-valued random variables." - Andrew Ng

**Implementations**:
- GDA from scratch with MLE
- Multivariate Gaussian visualization (μ and Σ effects)
- Naive Bayes for spam detection
- Laplace smoothing demonstration
- Text classification with Multinomial vs Bernoulli event models

**Comparison**:
- Logistic Regression vs GDA
- When to use generative models

---

#### Lecture 6-7: Support Vector Machines  
**File**: [06_svm.ipynb](06_svm.ipynb) **[ENHANCED!]**  
**Source**: Lectures 6-7 Transcripts (SVM, Kernels)

**Topics**:
- Optimal margin classifier
- Functional and geometric margins
- **Representer theorem**
- Primal and dual formulation
- **The Kernel Trick** (new!)
- Common kernels (Linear, Polynomial, RBF)
- Working in infinite-dimensional feature spaces
- Soft margin (slack variables)

**From the Lecture**:
> "Support vector machine is one of my favorite algorithms - very turnkey, very widely applicable." - Andrew Ng

> "We can work in 100,000 dimensional, or a million dimensional, or 100 billion dimensional, or even **infinite-dimensional feature spaces**." - Andrew Ng

**New Theory**:
- **Representer Theorem**: w = Σ αᵢy⁽ⁱ⁾x⁽ⁱ⁾
  - Even in infinite dimensions, only need to store m coefficients!
- **Kernel Trick**: Never compute φ(x) explicitly
  - Use K(x,z) = ⟨φ(x), φ(z)⟩ instead
  - Example: Polynomial kernel K(x,z) = (xᵀz + 1)ᵈ
  - RBF kernel: K(x,z) = exp(-γ||x-z||²)

**Implementations**:
- Linear SVM with dual formulation
- Kernel SVM (polynomial, RBF)
- Non-linearly separable data (circles, moons)
- Hyperparameter tuning (C, γ)
- Decision boundary visualization
- Support vector identification
- RBF kernel deep dive (gamma effects)

**Applications**:
- Image classification
- Text categorization
- Bioinformatics

---

#### Lecture 8: Regularization and Bias-Variance  
**File**: [04_regularization.ipynb](04_regularization.ipynb) **[ENHANCED!]**  
**Source**: Lecture 8 Transcript (Bias-Variance Tradeoff)

**Topics**:
- **Bias-variance tradeoff theory** (new!)
- Overfitting and underfitting from theoretical perspective
- Ridge regression (L2)
- Lasso regression (L1)
- Elastic Net
- Choosing regularization parameter λ

**From the Lecture**:
> "Bias and variance is one of those concepts that's easy to understand but hard to master. I've had PhD students that worked with me for several years, and their understanding continues to deepen." - Andrew Ng

**New Theoretical Framework**:
- **High Bias (Underfitting)**: "Strong preconceptions that don't match reality"
  - Example: Fitting linear to curved data
  - Model too simple
- **High Variance (Overfitting)**: "Predictions vary wildly with different datasets"
  - Example: 5th-order polynomial through noisy points
  - Model too complex
- **Just Right**: Captures true pattern, generalizes well

**Workflow from Lecture**:
1. Train quick/dirty baseline
2. Identify: High bias or high variance?
3. Apply appropriate fix:
   - High bias → Add features, more complexity, decrease λ
   - High variance → More data, regularization, increase λ

**Demonstrations**:
- Housing price polynomial fits (underfit/just right/overfit)
- Classification overfitting examples
- Regularization path visualization
- Cross-validation for λ selection
- Feature selection with Lasso

---

#### Lecture 11: Neural Networks - Basics
**File**: [08_neural_networks_basics.ipynb](08_neural_networks_basics.ipynb)

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

#### Lecture 12: Neural Networks - Advanced
**File**: [09_neural_networks_advanced.ipynb](09_neural_networks_advanced.ipynb)

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

#### Lecture 14: Clustering
**File**: [12_clustering.ipynb](12_clustering.ipynb)

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

#### Lecture 15-17: Dimensionality Reduction
**File**: [13_dimensionality_reduction.ipynb](13_dimensionality_reduction.ipynb)

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

#### Anomaly Detection
**File**: [14_anomaly_detection.ipynb](14_anomaly_detection.ipynb)

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

#### Lecture 9: Learning Theory  
**File**: [10_learning_theory.ipynb](10_learning_theory.ipynb) **[ENHANCED!]**  
**Source**: Lecture 9 Transcript (Friday Section - Learning Theory)

**Topics**:
- **Core assumptions of learning theory** (new!)
- **Bias and variance from parameter view** (new!)
- Sampling distributions and estimators
- Empirical risk minimization (ERM)
- VC dimension
- PAC learning
- Sample complexity
- Uniform convergence

**From the Lecture**:
> "This deepens your understanding of how machine learning works under the covers. What are the assumptions we're making and why do things generalize." - TA Anand

**New Foundations**:
- **Assumption 1**: Data distribution D exists
  - Training and test data from **same distribution**
  - This is critical for generalization!
- **Assumption 2**: Independent sampling (i.i.d.)

**The Learning Process**:
```
S (random variable) → Algorithm A (deterministic) → θ̂ (random variable)
```

> "When you feed a random variable through a deterministic function, you get a random variable"

**Bias-Variance: Parameter Space View**:
- Imagine running learning algorithm many times with different samples
- Each run gives different θ̂ → cloud of points in parameter space
- **Bias**: Is cloud centered on true θ*? (first moment)
- **Variance**: How spread out is cloud? (second moment)

**Four Algorithm Types**:
| Bias | Variance | Behavior |
|------|----------|----------|
| Low  | Low      | ✓ Best: Centered, tight |
| Low  | High     | Centered but spread out |
| High | Low      | Off-center but consistent |
| High | High     | Worst: Off-center, spread out |

**Effects of Data Size m**:
- ↑ m → ↓ Variance (more stable)
- ↑ m → Bias stays same (assumptions unchanged)

**Effects of Regularization**:
- ↑ λ → ↓ Variance (more constraints)
- ↑ λ → May increase bias (stronger assumptions)

**Theoretical Results**:
- Hoeffding inequality
- Union bound
- Training/test error relationship
- Generalization bounds

---

#### Lecture 10: Decision Trees and Ensembles  
**File**: [07_decision_trees.ipynb](07_decision_trees.ipynb) **[NEW!]**  
**Source**: Lecture 10 Transcript (Decision Trees, Bagging, Boosting)

**Topics**:
- **Decision trees from scratch** (new!)
- Recursive partitioning
- **Split functions and loss functions** (new!)
- Why cross-entropy beats misclassification loss
- Gini impurity
- Tree depth and overfitting
- **Ensemble methods** (new!)
- Bagging and Random Forests
- Boosting (AdaBoost, Gradient Boosting)

**From the Lecture**:
> "Decision trees are one of our first examples of a non-linear model" - TA Raphael Townshend

**The Skiing Example**:
- **Problem**: Predict if you can ski given month and latitude
- **Data**: Northern Hemisphere winter (Jan-Mar), Southern Hemisphere winter (Jun-Aug)
- **Challenge**: Non-linearly separable regions
- **Solution**: Recursive rectangular partitions

> "The tree is basically gonna play 20 Questions with this space"

**Greedy, Top-Down, Recursive Partitioning**:
1. Start with overall space
2. Ask best question: "Is latitude > 30°?" or "Is month < 3?"
3. Split space into two regions
4. Recursively apply to each region
5. Stop when pure or max depth

**Split Function**: S_p(j, t)
```
R₁ = {x ∈ R_p : x_j < t}
R₂ = {x ∈ R_p : x_j ≥ t}
```
- j = feature index
- t = threshold value

**Loss Functions Comparison**:

**Misclassification Loss** (Don't Use!):
```
L = 1 - max_c(p̂_c)
```
**Problem from lecture**: Can't distinguish between splits!
```
Parent: 900 pos, 100 neg → Loss = 100
Split 1: (700,100) + (200,0) → Loss = 100  
Split 2: (400,100) + (500,0) → Loss = 100  (clearly better but same loss!)
```

**Cross-Entropy Loss** (Use This!):
```
L = -Σ p̂_c log(p̂_c)
```
> "From information theory: Number of bits needed to communicate which class"

**Gini Impurity** (Also Good):
```
L = 1 - Σ p̂_c²
```

**Implementations**:
- Skiing classifier (lecture example recreated!)
- Decision tree visualization (20 Questions)
- Loss function comparison (verifying lecture claim)
- Tree depth experiments (2, 4, 8, unlimited)
- Overfitting demonstration
- Bootstrap aggregating (bagging)
- Random Forest
- AdaBoost and Gradient Boosting

**Key Insights**:
- **Advantages**: Interpretable, handles non-linearity, no scaling needed
- **Disadvantage**: High variance (overfits easily)
- **Solution**: Ensemble methods reduce variance!

**When to Use**:
- ✓ Need interpretability
- ✓ Mixed data types
- ✓ Non-linear patterns
- ✗ Need stable predictions → Use Random Forest instead

---

#### Lecture 13: ML Strategy
**File**: [11_ml_strategy.ipynb](11_ml_strategy.ipynb)

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

#### Recommender Systems
**File**: [15_recommender_systems.ipynb](15_recommender_systems.ipynb)

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

#### Lecture 18-20: Reinforcement Learning
**File**: [16_reinforcement_learning.ipynb](16_reinforcement_learning.ipynb)

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
