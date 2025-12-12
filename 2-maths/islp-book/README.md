# Introduction to Statistical Learning with Python (ISLP)

A comprehensive collection of Jupyter notebooks covering the foundational concepts and advanced techniques in statistical learning and machine learning, based on "An Introduction to Statistical Learning" adapted for Python.

## 📚 Overview

This series provides hands-on implementations of statistical learning methods with Python, featuring:

- **13 comprehensive chapters** covering fundamental to advanced topics
- **Theory + Practice**: Mathematical formulations with executable code
- **Real datasets**: Practical examples using classic ML datasets
- **Visualizations**: Professional plots for understanding concepts
- **Exercises**: Practice problems for each chapter
- **100+ additional exercises**: See [PRACTICE_EXERCISES.md](PRACTICE_EXERCISES.md)

## 🗂️ Chapter Guide

### Chapter 1: Introduction
**File**: `01_introduction.ipynb` (NEW!)

**Topics**:
- What is statistical learning?
- Supervised vs unsupervised learning
- Real-world applications
- The ML workflow
- Model assessment metrics
- Overfitting vs underfitting

**Demonstrations**:
- California Housing (regression example)
- Breast Cancer (classification example)
- Iris Clustering (unsupervised example)
- Train-test split and overfitting visualization
- Comprehensive metrics comparison

**Key Concepts**:
- The learning framework: Y = f(X) + ε
- Bias-variance trade-off
- Train-test split importance
- Regression vs classification metrics
- Supervised vs unsupervised paradigms

**Practice**: 8 comprehensive exercises covering all intro concepts

---

### Chapter 2: Statistical Learning
**File**: `02_statistical_learning.ipynb` (25KB)

**Topics**:
- Supervised vs unsupervised learning
- Regression vs classification
- Bias-variance trade-off
- Training vs test error
- Model assessment and selection

**Key Concepts**:
- Reducible vs irreducible error
- Overfitting and underfitting
- Cross-validation basics

---

### Chapter 3: Linear Regression
**File**: `03_linear_regression.ipynb` (40KB)

**Topics**:
- Simple linear regression
- Multiple linear regression
- Least squares estimation
- Hypothesis testing (t-tests, F-tests)
- R² and adjusted R²
- Residual analysis

**Demonstrations**:
- Boston Housing dataset
- Advertising dataset
- Confidence vs prediction intervals
- Diagnostic plots

**Key Formulas**:
```
β̂ = (X'X)⁻¹X'y
RSS = Σ(yi - ŷi)²
R² = 1 - RSS/TSS
```

---

### Chapter 4: Classification
**File**: `04_classification.ipynb` (32KB)

**Topics**:
- Logistic regression
- Linear Discriminant Analysis (LDA)
- Quadratic Discriminant Analysis (QDA)
- Naive Bayes
- K-Nearest Neighbors (KNN)

**Demonstrations**:
- Binary classification (Default dataset)
- Multi-class classification (Iris)
- Decision boundaries
- Confusion matrices
- ROC curves and AUC

**Metrics**:
- Accuracy, precision, recall, F1-score
- Sensitivity and specificity
- Classification error rate

---

### Chapter 5: Resampling Methods
**File**: `05_resampling_methods.ipynb` (37KB)

**Topics**:
- Cross-validation (LOOCV, k-fold)
- Bootstrap
- Model selection
- Uncertainty estimation

**Demonstrations**:
- k-fold CV for polynomial degree selection
- LOOCV vs k-fold comparison
- Bootstrap confidence intervals
- Bootstrap standard errors

**Applications**:
- Estimating test error
- Model comparison
- Parameter uncertainty
- Sample size effects

---

### Chapter 6: Linear Model Selection and Regularization
**File**: `06_regularization.ipynb` (46KB)

**Topics**:
- Subset selection (best subset, forward, backward)
- Ridge regression (L2 penalty)
- Lasso regression (L1 penalty)
- Elastic Net
- Principal Component Regression (PCR)

**Key Concepts**:
- Regularization path
- Cross-validation for λ selection
- Feature selection vs shrinkage
- Multicollinearity handling

**Formulas**:
```
Ridge: minimize RSS + λΣβj²
Lasso: minimize RSS + λΣ|βj|
Elastic Net: minimize RSS + λ₁Σ|βj| + λ₂Σβj²
```

---

### Chapter 7: Moving Beyond Linearity
**File**: `07_beyond_linearity.ipynb` (35KB)

**Topics**:
- Polynomial regression
- Step functions
- Regression splines (B-splines)
- Smoothing splines
- Generalized Additive Models (GAMs)

**Demonstrations**:
- Polynomial degree selection via CV
- Spline knot placement
- GAMs with multiple predictors
- Method comparison

**Use Cases**:
- Non-linear relationships
- Flexible modeling
- Interpretable non-linearity
- Smooth curve fitting

---

### Chapter 8: Tree-Based Methods
**File**: `08_tree_based_methods.ipynb` (40-45KB)

**Topics**:
- Decision trees (CART)
- Bagging (Bootstrap Aggregation)
- Random Forests
- Boosting (AdaBoost, Gradient Boosting)
- Feature importance

**Demonstrations**:
- Tree pruning and depth control
- Out-of-bag (OOB) error
- Feature importance visualization
- Ensemble comparison
- Breast Cancer dataset

**Key Algorithms**:
- DecisionTreeClassifier/Regressor
- BaggingClassifier
- RandomForestClassifier
- AdaBoostClassifier
- GradientBoostingClassifier

---

### Chapter 9: Support Vector Machines
**File**: `09_support_vector_machines.ipynb` (40-45KB)

**Topics**:
- Maximal margin classifier
- Support Vector Classifier (soft margin)
- Kernel methods (Linear, Polynomial, RBF)
- Multi-class SVMs
- Support Vector Regression (SVR)

**Demonstrations**:
- C parameter tuning (margin control)
- Kernel comparison
- Gamma parameter effects (RBF)
- Hyperparameter grid search
- Breast Cancer classification

**Key Concepts**:
- Margin maximization
- Support vectors
- Kernel trick
- Slack variables (ξ)

---

### Chapter 10: Deep Learning
**File**: `10_deep_learning.ipynb` (35-40KB)

**Topics**:
- Neural network fundamentals
- Activation functions (ReLU, sigmoid, tanh, softmax)
- Single vs deep networks
- Backpropagation
- Regularization (L2, dropout, early stopping)
- MLPClassifier and MLPRegressor

**Demonstrations**:
- California Housing (regression)
- MNIST digit classification
- Hidden layer comparison
- Learning curves
- Regularization effects

**Architecture**:
```python
Input → Hidden₁ → Hidden₂ → ... → Output
Each layer: z = Wx + b, a = σ(z)
```

---

### Chapter 11: Survival Analysis
**File**: `11_survival_analysis.ipynb` (45-50KB)

**Topics**:
- Survival functions
- Censoring (right, left, interval)
- Kaplan-Meier estimator
- Log-Rank test
- Cox Proportional Hazards model
- Hazard ratios

**Demonstrations**:
- Rossi recidivism dataset
- Survival curves by group
- Median survival time
- Hazard ratio interpretation
- Proportional hazards assumption

**Key Library**: `lifelines`

**Applications**:
- Time-to-event analysis
- Medical studies
- Customer churn
- Equipment failure

---

### Chapter 12: Unsupervised Learning
**File**: `12_unsupervised_learning.ipynb` (40-45KB)

**Topics**:
- Principal Component Analysis (PCA)
- K-Means clustering
- Hierarchical clustering
- DBSCAN
- Dimensionality reduction

**Demonstrations**:
- Iris dataset (PCA: 4D → 2D)
- Scree plots and variance explained
- Elbow method for K selection
- Silhouette analysis
- Dendrogram visualization
- MNIST digits clustering

**Linkage Methods**:
- Complete
- Average
- Single
- Ward

**Validation**:
- Silhouette score
- Davies-Bouldin index
- Inertia (within-cluster SS)

---

### Chapter 13: Multiple Testing
**File**: `13_multiple_testing.ipynb` (35-40KB)

**Topics**:
- Multiple testing problem
- Family-Wise Error Rate (FWER)
- False Discovery Rate (FDR)
- Bonferroni correction
- Holm's method
- Benjamini-Hochberg procedure
- Benjamini-Yekutieli procedure

**Demonstrations**:
- Simulation of Type I error inflation
- FWER vs FDR comparison
- Threshold visualization
- Power analysis
- Method selection guidelines

**Key Library**: `statsmodels.stats.multitest`

**Applications**:
- Genomics (thousands of tests)
- Neuroimaging
- A/B testing
- Clinical trials

**Decision Guide**:
- Small m (< 20): Bonferroni or Holm
- Large m (≥ 100): Benjamini-Hochberg (FDR)
- Confirmatory studies: FWER control
- Exploratory studies: FDR control

---

## 🚀 Getting Started

### Prerequisites

**Python Version**: 3.8+

**Required Libraries**:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy statsmodels lifelines
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/PavanMudigondaTR/aiml.git
cd aiml/2-maths/islp-book
```

2. **Create virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Launch Jupyter**:
```bash
jupyter notebook
```

---

## 📖 Learning Path

### Beginner Track (Fundamentals)
1. **Chapter 1**: Introduction → Overview and motivation
2. **Chapter 2**: Statistical Learning → Understand core concepts
3. **Chapter 3**: Linear Regression → First predictive model
4. **Chapter 4**: Classification → Categorical outcomes
5. **Chapter 5**: Resampling → Model validation

**Time**: 2-4 weeks

### Intermediate Track (Advanced Methods)
6. **Chapter 6**: Regularization → Handle complex models
7. **Chapter 7**: Beyond Linearity → Non-linear relationships
8. **Chapter 8**: Tree Methods → Ensemble learning
9. **Chapter 9**: SVMs → Powerful classification

**Time**: 3-4 weeks

### Advanced Track (Specialized Topics)
10. **Chapter 10**: Deep Learning → Neural networks
11. **Chapter 11**: Survival Analysis → Time-to-event
12. **Chapter 12**: Unsupervised → Clustering and PCA
13. **Chapter 13**: Multiple Testing → Statistical inference

**Time**: 3-4 weeks

**Total Program**: 9-12 weeks for comprehensive mastery

---

## 🎯 How to Use These Notebooks

### For Self-Study
1. **Read theory sections** (markdown cells) carefully
2. **Run code cells** sequentially (Shift+Enter)
3. **Modify parameters** to see effects
4. **Complete exercises** at the end
5. **Compare your solutions** with demonstrations

### For Teaching
- Use as lecture supplements
- Live coding demonstrations
- Student projects and assignments
- Flipped classroom materials

### For Reference
- Quick lookup of methods
- Code snippets for projects
- Visualization templates
- Best practices

---

## 📊 Datasets Used

| Dataset | Used In | Description |
|---------|---------|-------------|
| **Boston Housing** | Ch 3, 6, 7 | House prices with 13 features |
| **Advertising** | Ch 3 | Sales vs TV/Radio/Newspaper |
| **Default** | Ch 4 | Credit card default prediction |
| **Iris** | Ch 4, 12 | 3 species, 4 features |
| **Breast Cancer** | Ch 8, 9 | Binary classification, 30 features |
| **California Housing** | Ch 10 | Regression, 8 features |
| **MNIST Digits** | Ch 10, 12 | 64 features (8×8 pixels) |
| **Rossi** | Ch 11 | Recidivism survival data |
| **Synthetic** | Multiple | Generated for demonstrations |

Most datasets are built into scikit-learn or easily accessible.

---

## 🔑 Key Libraries Reference

### Core
```python
import numpy as np              # Numerical computing
import pandas as pd             # Data manipulation
import matplotlib.pyplot as plt # Plotting
import seaborn as sns          # Statistical visualization
```

### Machine Learning
```python
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, BaggingClassifier
from sklearn.svm import SVC, SVR
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, auc
```

### Statistical
```python
from scipy import stats                              # Statistical tests
from statsmodels.stats.multitest import multipletests # Multiple testing
from lifelines import KaplanMeierFitter, CoxPHFitter  # Survival analysis
```

---

## 🎓 Concepts Covered

### Fundamental Concepts
- Bias-variance trade-off
- Overfitting and regularization
- Cross-validation
- Feature engineering
- Model selection

### Regression Techniques
- Linear regression
- Polynomial regression
- Ridge and Lasso
- Splines and GAMs
- SVR

### Classification Methods
- Logistic regression
- LDA/QDA
- Decision trees
- Random forests
- Boosting
- SVMs
- Neural networks

### Unsupervised Learning
- PCA
- K-Means
- Hierarchical clustering
- Dimensionality reduction

### Statistical Inference
- Hypothesis testing
- Confidence intervals
- Bootstrap
- Multiple testing correction
- Survival analysis

---

## 💡 Best Practices

### Code Style
- Set random seeds for reproducibility: `np.random.seed(42)`
- Use train-test splits: `train_test_split(test_size=0.2)`
- Scale features when needed: `StandardScaler()`
- Validate with cross-validation

### Visualization
- Clear labels and titles
- Appropriate color schemes
- Grid lines for readability
- Legend placement
- Figure size optimization

### Model Development
1. **Explore data** (EDA)
2. **Split data** (train/test)
3. **Preprocess** (scaling, encoding)
4. **Train model**
5. **Validate** (cross-validation)
6. **Tune hyperparameters**
7. **Test** (final evaluation)
8. **Interpret results**

---

## 🔍 Quick Method Lookup

### Choose Regression Method
- **Linear relationships**: Linear Regression
- **Multicollinearity**: Ridge or Lasso
- **Feature selection**: Lasso
- **Non-linear**: Polynomial, Splines, GAMs
- **Complex patterns**: Random Forest, Gradient Boosting
- **Small sample**: Ridge

### Choose Classification Method
- **Linear boundary**: Logistic Regression, LDA
- **Non-linear boundary**: QDA, KNN, SVM (RBF)
- **Interpretability**: Logistic Regression, Decision Tree
- **High accuracy**: Random Forest, Gradient Boosting, SVM
- **Large dataset**: Logistic Regression, Neural Network
- **Small dataset**: LDA, Naive Bayes

### Choose Unsupervised Method
- **Dimensionality reduction**: PCA
- **Clustering (spherical)**: K-Means
- **Clustering (arbitrary shape)**: Hierarchical, DBSCAN
- **Visualization**: PCA + scatter plot

---

## 📝 Practice Exercises

### In-Chapter Exercises
Each chapter includes 5-8 practice exercises covering:
- **Conceptual**: Understanding theory
- **Applied**: Using methods on new datasets
- **Computational**: Implementing from scratch
- **Analysis**: Interpreting results

### Additional Practice
**[PRACTICE_EXERCISES.md](PRACTICE_EXERCISES.md)** includes 100+ extra problems:
- 3 additional problems per chapter (39 total)
- 8 comprehensive projects
- 5 challenge problems
- Solutions and hints
- Progress tracker

**Difficulty Levels**:
- Beginner: Chapters 1-5 (25 exercises)
- Intermediate: Chapters 6-10 (25 exercises)
- Advanced: Chapters 11-13 + Projects (50+ exercises)

**Recommended Approach**:
1. Complete in-chapter exercises first
2. Attempt additional exercises in [PRACTICE_EXERCISES.md](PRACTICE_EXERCISES.md)
3. Work on 2-3 projects
4. Try 1 challenge problem
5. Participate in Kaggle competition

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:

- Additional datasets
- More exercises
- Alternative implementations
- Error corrections
- Clarifications
- Extended examples

**Process**:
1. Fork repository
2. Create feature branch
3. Make changes
4. Test notebooks (run all cells)
5. Submit pull request

---

## 📚 Additional Resources

### Books
- **ISLR** (original): James, Witten, Hastie, Tibshirani
- **ESL**: Elements of Statistical Learning (advanced)
- **Python Data Science Handbook**: Jake VanderPlas
- **Hands-On Machine Learning**: Aurélien Géron

### Online Courses
- Stanford CS229 (Machine Learning)
- Fast.ai (Practical Deep Learning)
- Coursera Machine Learning Specialization

### Documentation
- [scikit-learn](https://scikit-learn.org/)
- [statsmodels](https://www.statsmodels.org/)
- [lifelines](https://lifelines.readthedocs.io/)
- [seaborn](https://seaborn.pydata.org/)

---

## ⚖️ License

MIT License - feel free to use for learning and teaching.

---

## 📧 Contact

**Repository**: [PavanMudigondaTR/aiml](https://github.com/PavanMudigondaTR/aiml)

**Issues**: Report bugs or suggest improvements via GitHub Issues

---

## 🎉 Acknowledgments

- Based on "An Introduction to Statistical Learning" by James, Witten, Hastie, and Tibshirani
- scikit-learn team for excellent ML library
- Python community for data science ecosystem
- Contributors and users of this repository

---

## 📈 Progress Tracker

Track your learning progress:

### Core Chapters
- [ ] Chapter 1: Introduction
- [ ] Chapter 2: Statistical Learning
- [ ] Chapter 3: Linear Regression
- [ ] Chapter 4: Classification
- [ ] Chapter 5: Resampling Methods
- [ ] Chapter 6: Regularization
- [ ] Chapter 7: Beyond Linearity
- [ ] Chapter 8: Tree-Based Methods
- [ ] Chapter 9: Support Vector Machines
- [ ] Chapter 10: Deep Learning
- [ ] Chapter 11: Survival Analysis
- [ ] Chapter 12: Unsupervised Learning
- [ ] Chapter 13: Multiple Testing

**Core Progress**: 0/13 chapters

### Additional Practice
- [ ] Complete all in-chapter exercises (60+ problems)
- [ ] Complete additional exercises from [PRACTICE_EXERCISES.md](PRACTICE_EXERCISES.md) (39 problems)
- [ ] Complete 2-3 projects (8 available)
- [ ] Complete 1+ challenge problem (5 available)
- [ ] Participate in Kaggle competition

**Overall Mastery**: Track your journey to becoming an ISLP expert!

---

## 🏆 Learning Goals

After completing this series, you will be able to:

✅ Understand fundamental statistical learning concepts  
✅ Implement regression and classification models  
✅ Apply regularization techniques  
✅ Use ensemble methods effectively  
✅ Work with neural networks  
✅ Perform survival analysis  
✅ Apply unsupervised learning methods  
✅ Handle multiple testing problems  
✅ Choose appropriate methods for different problems  
✅ Interpret and validate model results  
✅ Communicate findings effectively  

**Happy Learning! 🚀**
