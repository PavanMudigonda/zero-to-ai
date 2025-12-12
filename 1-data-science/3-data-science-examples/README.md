# Data Science Examples - Curated & Consolidated

This directory contains curated data science learning materials, consolidated from 10+ sources (1.1 GB) into essential, high-value content (106 MB).

## 📁 Directory Structure

### 01-microsoft-course/
**Official Microsoft Data Science for Beginners curriculum**

A comprehensive, structured course from Microsoft covering the complete data science lifecycle.

**Course Modules:**

#### 1-Introduction
- What is Data Science?
- Ethics in Data Science
- Defining Data
- Introduction to Statistics & Probability
- Data Science Scenarios

#### 2-Working-With-Data
- Relational Data
- Non-Relational Data
- Working with Python
- Data Preparation & Cleaning
- Querying Data with SQL

#### 3-Data-Visualization
- Visualizing Quantities
- Visualizing Distributions
- Visualizing Proportions
- Visualizing Relationships
- Making Meaningful Visualizations

#### 4-Data-Science-Lifecycle
- Introduction to the Lifecycle
- Analyzing
- Communication
- Data Science in the Wild

#### 5-Data-Science-In-Cloud
- Working with Cloud Data
- Cloud Data Storage
- Cloud-based Analytics

#### 6-Data-Science-In-Wild
- Real-World Data Science Applications
- Ethics and Best Practices

**Features:**
- Structured learning path
- Real-world datasets included
- Hands-on exercises
- Project-based learning
- Beginner-friendly explanations

**Recommended For:** Complete beginners to data science

**Time to Complete:** 4-6 weeks (10-15 hours/week)

---

### 02-core-topics/
**Essential reference notebooks for core data science libraries**

Quick reference and examples for numpy, pandas, and matplotlib.

#### numpy-reference/
NumPy fundamentals and operations:
- Array operations
- Broadcasting
- Linear algebra
- Statistical functions
- Performance tips

#### pandas-reference/
pandas operations and techniques:
- DataFrame manipulation
- Data cleaning
- GroupBy operations
- Time series
- Merge/Join operations

#### matplotlib-reference/
Data visualization with matplotlib:
- Basic plots (line, scatter, bar, histogram)
- Customization (colors, labels, legends)
- Subplots and layouts
- Advanced visualizations
- Best practices

**Use Case:** Quick lookup and reference while working on projects

---

### 03-machine-learning/
**Machine learning notebooks and competition examples**

#### scikit-learn-reference/
Comprehensive scikit-learn examples:

**Supervised Learning:**
- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forests
- Support Vector Machines (SVM)
- Gradient Boosting (XGBoost, LightGBM)
- Neural Networks (MLPClassifier/Regressor)

**Unsupervised Learning:**
- K-Means Clustering
- Hierarchical Clustering
- DBSCAN
- Principal Component Analysis (PCA)
- t-SNE

**Model Selection & Evaluation:**
- Cross-validation
- Grid Search / Random Search
- Metrics (accuracy, precision, recall, F1, ROC-AUC)
- Confusion matrices
- Learning curves

**Preprocessing:**
- Feature scaling (StandardScaler, MinMaxScaler)
- Encoding (LabelEncoder, OneHotEncoder)
- Handling missing data
- Feature engineering

#### kaggle-notebooks/
Real competition notebooks:
- Titanic survival prediction
- House prices prediction
- Credit card fraud detection
- And more...

**Skills Developed:**
- End-to-end ML pipelines
- Feature engineering
- Model selection and tuning
- Handling real-world messy data
- Competition strategies

---

### 04-deep-learning/
**Deep learning with TensorFlow and Keras**

#### tensorflow-keras/
Deep learning fundamentals:

**Neural Network Basics:**
- Perceptrons and feedforward networks
- Activation functions
- Backpropagation
- Optimization algorithms (SGD, Adam, RMSprop)

**Architectures:**
- Multi-Layer Perceptrons (MLP)
- Convolutional Neural Networks (CNN)
- Recurrent Neural Networks (RNN)
- Long Short-Term Memory (LSTM)
- Autoencoders
- Generative Adversarial Networks (GAN)

**Applications:**
- Image classification (MNIST, CIFAR-10, ImageNet)
- Natural Language Processing
- Time series prediction
- Transfer learning

**Tools & Techniques:**
- TensorFlow 2.x / Keras API
- Model checkpointing
- Early stopping
- Learning rate scheduling
- Regularization (dropout, L1/L2)

#### keras-bootcamp/
Keras bootcamp materials:
- Quick start notebooks
- Common architectures
- Best practices

**Recommended Prerequisites:**
- Strong understanding of ML fundamentals
- Linear algebra and calculus basics
- Experience with numpy and pandas

---

### 05-reference-notebooks/
**Advanced topics and cloud/distributed computing**

#### aws/
AWS data science notebooks:
- AWS SageMaker examples
- S3 data access
- Cloud-based ML pipelines
- Deployment strategies

#### spark/
Big data processing with Apache Spark:
- Spark DataFrames
- Spark SQL
- MLlib (Spark ML)
- Distributed computing patterns

**Use Case:** 
- Working with large datasets (> 1GB)
- Cloud-based ML projects
- Production deployment

---

## 🎯 Learning Paths

### Path 1: Complete Beginner (0-8 weeks)

**Weeks 1-6: Fundamentals**
```
01-microsoft-course/
  ├── Complete all 6 modules in order
  └── Focus on understanding concepts, not memorization

Goal: Build strong foundation in data science
Daily Time: 2-3 hours
```

**Weeks 7-8: Practice**
```
02-core-topics/
  └── Review numpy, pandas, matplotlib references

Goal: Hands-on practice with core libraries
Daily Time: 1-2 hours
```

### Path 2: Machine Learning Focus (8-16 weeks)

**Prerequisites:** Complete Path 1 or equivalent experience

**Weeks 1-4: Supervised Learning**
```
03-machine-learning/scikit-learn-reference/
  ├── Linear models (regression, classification)
  ├── Tree-based models
  ├── SVMs
  └── Model evaluation

Goal: Master supervised ML algorithms
Daily Time: 2-3 hours
```

**Weeks 5-8: Advanced ML**
```
03-machine-learning/
  ├── Ensemble methods (Random Forest, XGBoost)
  ├── Unsupervised learning
  └── Model tuning and optimization

Goal: Advanced ML techniques
Daily Time: 2-3 hours
```

**Weeks 9-16: Kaggle Competitions**
```
03-machine-learning/kaggle-notebooks/
  └── Complete 2-3 competitions end-to-end

Goal: Real-world problem-solving
Daily Time: 3-4 hours
```

### Path 3: Deep Learning Specialization (16-24 weeks)

**Prerequisites:** Path 2 completion

**Weeks 1-8: Neural Network Fundamentals**
```
04-deep-learning/tensorflow-keras/
  ├── Perceptrons and MLPs
  ├── CNNs for image tasks
  ├── RNNs/LSTMs for sequences
  └── Build projects for each architecture

Goal: Understand DL architectures
Daily Time: 3-4 hours
```

**Weeks 9-16: Advanced Architectures**
```
04-deep-learning/
  ├── Autoencoders
  ├── GANs
  ├── Transfer learning
  └── Custom architectures

Goal: Advanced DL techniques
Daily Time: 3-4 hours
```

**Weeks 17-24: Projects**
```
Build 2-3 substantial projects:
  ├── Computer vision (object detection, segmentation)
  ├── NLP (sentiment analysis, text generation)
  └── Time series (forecasting, anomaly detection)

Goal: Portfolio-ready projects
```

### Path 4: Cloud & Production (4-8 weeks)

**Prerequisites:** Paths 1-2 completion

```
05-reference-notebooks/
  ├── AWS SageMaker workflows
  ├── Spark for big data
  └── Deployment best practices

Goal: Production-ready ML
Daily Time: 2-3 hours
```

---

## 📊 Content Statistics

### Files & Size
- **Original Collection:** 919 files, 1.1 GB (10 sources)
- **Consolidated:** 122 notebooks, 106 MB
- **Reduction:** 87% fewer files, 90% size reduction
- **Space Saved:** ~1 GB

### Coverage
- ✅ Complete beginner to advanced progression
- ✅ Microsoft official curriculum
- ✅ Core libraries (numpy, pandas, matplotlib)
- ✅ Machine learning (scikit-learn)
- ✅ Deep learning (TensorFlow/Keras)
- ✅ Real competition notebooks (Kaggle)
- ✅ Cloud/distributed computing (AWS, Spark)

---

## 🗂️ Source Collections

This curated collection extracts the best content from:

1. **Microsoft-Data-Science-For-Beginners**
   - https://github.com/microsoft/Data-Science-For-Beginners
   - Official Microsoft curriculum
   - Structured learning path

2. **data-science-ipython-notebooks**
   - https://github.com/donnemartin/data-science-ipython-notebooks
   - Comprehensive reference notebooks
   - 168 original notebooks → 60 essential ones

3. **python-bootcamp-keras**
   - Keras deep learning bootcamp
   - Quick start materials

**Excluded (Redundant Content):**
- God-Level-Data-Science-ML-Full-Stack
- HypatiaAcademy
- P4DS4D3
- Py_DS_ML_Bootcamp-master
- Python-for-Data-Science-and-Machine-Learning-Bootcamp
- Udemy-Course-Data-Analysis
- py/

**Reason:** These contained duplicate or overlapping material already covered in the curated selections above.

---

## 🚀 Getting Started

### Installation

```bash
# Core data science stack
pip install numpy pandas matplotlib seaborn

# Machine learning
pip install scikit-learn xgboost lightgbm

# Deep learning
pip install tensorflow keras

# Jupyter
pip install jupyter jupyterlab

# Optional: Big data
pip install pyspark

# Optional: AWS
pip install boto3 sagemaker
```

### Quick Start

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Verify installation
print(f"numpy: {np.__version__}")
print(f"pandas: {pd.__version__}")

# You're ready to start!
```

---

## 💡 Study Tips

### 1. Follow the Learning Path
- Don't skip ahead
- Build solid foundations
- Master one topic before moving on

### 2. Code Along
- Type every example
- Don't just read
- Experiment with variations

### 3. Work on Projects
- Apply concepts immediately
- Build a portfolio
- Share on GitHub

### 4. Join Communities
- Kaggle for competitions
- Reddit (r/datascience, r/MachineLearning)
- Discord/Slack channels

### 5. Read Documentation
- Official docs are invaluable
- Learn to search effectively
- Understand the "why" not just "how"

### 6. Practice Daily
- 1 hour daily > 7 hours on weekend
- Consistency is key
- Track your progress

---

## 📖 Key Concepts by Directory

### 01-microsoft-course/
- Data science lifecycle
- Statistics and probability
- Data cleaning and preparation
- Visualization best practices
- Ethics in data science
- Communication skills

### 02-core-topics/
- Array operations (numpy)
- DataFrame manipulation (pandas)
- Data visualization (matplotlib)
- Performance optimization
- Best practices

### 03-machine-learning/
- Supervised vs unsupervised learning
- Classification vs regression
- Feature engineering
- Model evaluation metrics
- Hyperparameter tuning
- Ensemble methods

### 04-deep-learning/
- Neural network architectures
- Gradient descent and backpropagation
- Convolutional layers
- Recurrent architectures
- Transfer learning
- Regularization techniques

### 05-reference-notebooks/
- Cloud computing (AWS)
- Distributed processing (Spark)
- Scalable ML pipelines
- Production deployment

---

## 🎓 Skills You'll Develop

### Technical Skills
- ✅ Python programming for data science
- ✅ Data wrangling and cleaning
- ✅ Exploratory data analysis (EDA)
- ✅ Statistical analysis
- ✅ Data visualization
- ✅ Machine learning algorithms
- ✅ Deep learning architectures
- ✅ Model evaluation and tuning
- ✅ Cloud-based ML (AWS)
- ✅ Big data processing (Spark)

### Soft Skills
- ✅ Problem-solving
- ✅ Critical thinking
- ✅ Communication of insights
- ✅ Project management
- ✅ Ethical considerations
- ✅ Collaboration

---

## 📚 Additional Resources

### Books
- "Python for Data Analysis" by Wes McKinney
- "Hands-On Machine Learning" by Aurélien Géron
- "Deep Learning" by Ian Goodfellow

### Online Courses
- Coursera: Andrew Ng's Machine Learning
- Fast.ai: Practical Deep Learning
- DataCamp: Data Science Career Track

### Practice Platforms
- Kaggle - Competitions and datasets
- LeetCode - Coding challenges
- HackerRank - Data science track

### Documentation
- [NumPy Docs](https://numpy.org/doc/)
- [pandas Docs](https://pandas.pydata.org/docs/)
- [scikit-learn Docs](https://scikit-learn.org/stable/)
- [TensorFlow Docs](https://www.tensorflow.org/api_docs)

---

## 🏆 Career Paths

This collection prepares you for:
- Data Analyst
- Data Scientist
- Machine Learning Engineer
- Deep Learning Engineer
- ML Ops Engineer
- Research Scientist

**Expected Timeline to Job-Ready:**
- Data Analyst: 3-6 months (Paths 1-2)
- Data Scientist: 6-12 months (Paths 1-3)
- ML Engineer: 12-18 months (All paths + projects)

---

## 📄 License

Content sourced from multiple repositories with their respective licenses. Please refer to original repository licenses for attribution and usage rights.

---

**Last Updated:** December 2024  
**Curated From:** 10 sources (1.1 GB, 919 files)  
**Consolidated To:** Essential content (106 MB, 122 notebooks)  
**Efficiency:** 90% size reduction, 87% fewer files  
**Organization:** Structured beginner → advanced learning paths
