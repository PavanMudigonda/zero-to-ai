# Phase 16: Debugging & Troubleshooting AI/ML Models

Learn systematic approaches to debug, diagnose, and optimize machine learning models and pipelines.

## 🎯 Learning Objectives

By the end of this phase, you will:
- ✅ Diagnose common ML model failures and performance issues
- ✅ Use debugging tools and techniques for ML workflows
- ✅ Profile and optimize model performance (speed, memory)
- ✅ Analyze and fix data-related problems
- ✅ Implement error handling and monitoring
- ✅ Debug deep learning models effectively
- ✅ Troubleshoot deployment and production issues

---

## 📚 What You'll Learn

### 1. **Model Debugging Fundamentals**
- The ML debugging workflow
- Common failure modes and symptoms
- Debugging checklist and best practices
- Logging and instrumentation

### 2. **Data Issues Diagnosis**
- Data quality problems (missing, duplicates, outliers)
- Label errors and class imbalance
- Distribution shift detection
- Feature correlation issues

### 3. **Performance Optimization**
- Profiling CPU and memory usage
- Identifying bottlenecks
- Optimization techniques (vectorization, caching)
- GPU utilization monitoring

### 4. **Model-Specific Debugging**
- Gradient vanishing/exploding
- Overfitting vs underfitting diagnosis
- Learning curve analysis
- Activation and weight monitoring

### 5. **Error Analysis Framework**
- Systematic error categorization
- Confusion matrix deep dive
- Per-class error analysis
- Failure case collection

---

## 🗂️ Module Structure

### Notebooks

1. **[01_debugging_workflow.ipynb](01_debugging_workflow.ipynb)**
   - ML debugging methodology
   - Sanity checks and baseline models
   - Common pitfalls checklist
   - Debugging tools overview
   - **Duration:** 60-90 minutes

2. **[02_data_issues.ipynb](02_data_issues.ipynb)**
   - Data quality checks (null values, duplicates, outliers)
   - Label noise detection
   - Distribution shift analysis
   - Feature validation
   - **Duration:** 60-90 minutes

3. **[03_performance_profiling.ipynb](03_performance_profiling.ipynb)**
   - CPU profiling with cProfile and line_profiler
   - Memory profiling with memory_profiler
   - Bottleneck identification
   - Optimization strategies
   - **Duration:** 90-120 minutes

4. **[04_model_debugging.ipynb](04_model_debugging.ipynb)**
   - Learning curves and convergence
   - Gradient monitoring
   - Weight initialization issues
   - Overfitting/underfitting diagnosis
   - **Duration:** 90-120 minutes

5. **[05_error_analysis.ipynb](05_error_analysis.ipynb)**
   - Systematic error categorization
   - Per-class performance analysis
   - Failure case analysis
   - Improvement strategies
   - **Duration:** 60-90 minutes

### Supporting Materials

- **[assignment.md](assignment.md)** - Comprehensive debugging project
- **[challenges.md](challenges.md)** - 7 progressive debugging challenges
- **[pre-quiz.md](pre-quiz.md)** - Baseline knowledge assessment
- **[post-quiz.md](post-quiz.md)** - Final knowledge verification

---

## 🛠️ Tools & Libraries

### Profiling Tools
```python
import cProfile          # CPU profiling
import line_profiler     # Line-by-line profiling
import memory_profiler   # Memory usage tracking
import py-spy            # Sampling profiler
```

### Debugging Tools
```python
import pdb              # Python debugger
import logging          # Structured logging
import warnings         # Warning management
import traceback        # Stack trace analysis
```

### Visualization Tools
```python
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import tensorboard      # For deep learning
```

### Analysis Libraries
```python
import pandas as pd
import numpy as np
import scikit-learn
from scipy import stats
```

---

## 📋 Prerequisites

Before starting this phase, you should:
- ✅ Complete Phase 15 (Model Evaluation & Metrics)
- ✅ Understand model training basics
- ✅ Be familiar with Python debugging
- ✅ Know NumPy and pandas fundamentals

---

## 🎓 Learning Path

### Week 1: Fundamentals & Data Issues
- **Day 1-2:** Complete Notebook 1 (Debugging Workflow)
- **Day 3-4:** Complete Notebook 2 (Data Issues)
- **Day 5:** Practice Challenges 1-2

### Week 2: Performance & Model Debugging
- **Day 1-2:** Complete Notebook 3 (Performance Profiling)
- **Day 3-4:** Complete Notebook 4 (Model Debugging)
- **Day 5:** Practice Challenges 3-4

### Week 3: Error Analysis & Integration
- **Day 1-2:** Complete Notebook 5 (Error Analysis)
- **Day 3-4:** Complete Assignment
- **Day 5:** Practice Challenges 5-7, Final Review

---

## 🚀 Quick Start

### Installation

```bash
# Install profiling tools
pip install line-profiler memory-profiler py-spy

# Install debugging utilities
pip install ipdb pytest-sugar

# Install visualization tools
pip install matplotlib seaborn plotly tensorboard

# Install ML libraries
pip install scikit-learn pandas numpy scipy
```

### Jupyter Extensions

```bash
# Install useful Jupyter extensions
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Enable profiling extension
pip install jupyter-resource-usage
```

---

## 🎯 Common Debugging Scenarios

### Scenario 1: Model Not Learning
**Symptoms:** Loss not decreasing, random performance
**Checklist:**
- ✅ Check learning rate (too high/low?)
- ✅ Verify data loading (labels shuffled?)
- ✅ Inspect gradients (vanishing/exploding?)
- ✅ Test with smaller dataset first

### Scenario 2: Poor Validation Performance
**Symptoms:** Train accuracy high, validation accuracy low
**Checklist:**
- ✅ Overfitting? Add regularization
- ✅ Data leakage? Check feature engineering
- ✅ Distribution shift? Analyze train/val split
- ✅ Insufficient data? Try augmentation

### Scenario 3: Slow Training
**Symptoms:** Training takes forever
**Checklist:**
- ✅ Profile code to find bottlenecks
- ✅ Check data loading (I/O bound?)
- ✅ Optimize preprocessing (use vectorization)
- ✅ Use GPU acceleration if available

### Scenario 4: Memory Errors
**Symptoms:** Out of memory crashes
**Checklist:**
- ✅ Profile memory usage
- ✅ Reduce batch size
- ✅ Use gradient accumulation
- ✅ Clear cache between iterations

---

## 📊 Debugging Workflow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    PROBLEM DETECTED                          │
│          (Poor performance, errors, slow speed)              │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                  1. REPRODUCE BUG                            │
│   • Create minimal reproducible example                      │
│   • Isolate the problem                                      │
│   • Document symptoms                                        │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                  2. GATHER DATA                              │
│   • Check logs and error messages                            │
│   • Profile performance                                      │
│   • Inspect intermediate outputs                             │
│   • Visualize data and predictions                           │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                  3. HYPOTHESIZE CAUSE                        │
│   • Review checklist of common issues                        │
│   • Form testable hypothesis                                 │
│   • Prioritize most likely causes                            │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                  4. TEST HYPOTHESIS                          │
│   • Make targeted change                                     │
│   • Re-run experiment                                        │
│   • Compare before/after                                     │
└───────────────────────┬─────────────────────────────────────┘
                        │
                ┌───────┴────────┐
                │                │
        Fixed? YES              NO
                │                │
                ▼                ▼
    ┌───────────────┐   ┌──────────────┐
    │   5. VERIFY    │   │  Try Next    │
    │   • Test edge  │   │  Hypothesis  │
    │     cases      │   └──────┬───────┘
    │   • Document   │          │
    │     solution   │          │
    └───────────────┘          │
                               │
                               └──────► Back to Step 3
```

---

## 🔍 Key Debugging Techniques

### 1. **Sanity Checks**
```python
# Check data shapes
print(f"X_train: {X_train.shape}, y_train: {y_train.shape}")

# Verify label distribution
print(y_train.value_counts())

# Test on single batch
model.fit(X_train[:32], y_train[:32])
```

### 2. **Baseline Models**
```python
# Always start with simple baseline
from sklearn.dummy import DummyClassifier
baseline = DummyClassifier(strategy='most_frequent')
baseline.fit(X_train, y_train)
print(f"Baseline accuracy: {baseline.score(X_test, y_test):.3f}")
```

### 3. **Logging**
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"Training started with {len(X_train)} samples")
logger.warning(f"Found {null_count} missing values")
```

### 4. **Visualization**
```python
# Plot learning curves
plt.plot(history['train_loss'], label='Train')
plt.plot(history['val_loss'], label='Validation')
plt.legend()
plt.show()

# Inspect predictions
pd.DataFrame({'Actual': y_test, 'Predicted': y_pred}).head(20)
```

---

## ⚠️ Common Pitfalls

### Data-Related
- ❌ **Data leakage** (using test data in preprocessing)
- ❌ **Label mismatch** (features and labels not aligned)
- ❌ **Scaling issues** (forgot to normalize/standardize)
- ❌ **Class imbalance** (not handling imbalanced classes)

### Model-Related
- ❌ **Wrong loss function** (MSE for classification)
- ❌ **Learning rate issues** (too high causes divergence)
- ❌ **Random seed not set** (can't reproduce results)
- ❌ **No validation set** (overfitting to test set)

### Code-Related
- ❌ **Shape mismatches** (batch dimension issues)
- ❌ **Gradient accumulation** (not zeroing gradients)
- ❌ **Mode confusion** (model in train vs eval mode)
- ❌ **Memory leaks** (holding references to tensors)

---

## 📈 Success Metrics

After completing this phase, you should be able to:

✅ Systematically debug ML models using structured approach  
✅ Identify and fix data quality issues  
✅ Profile and optimize code for 2-10x speedup  
✅ Diagnose overfitting, underfitting, and convergence problems  
✅ Perform thorough error analysis  
✅ Use debugging tools (pdb, profilers, loggers)  
✅ Handle common production issues

---

## 🎯 Assessment

- **Pre-Quiz:** Baseline knowledge check (10 questions)
- **Notebooks:** 5 interactive debugging exercises
- **Assignment:** Debug and optimize a broken ML pipeline
- **Challenges:** 7 real-world debugging scenarios
- **Post-Quiz:** Comprehensive assessment (18 questions)

**Passing Criteria:** 70% on post-quiz, complete assignment

---

## 📚 Additional Resources

### Documentation
- [Python Debugging Guide](https://docs.python.org/3/library/pdb.html)
- [Memory Profiler Docs](https://pypi.org/project/memory-profiler/)
- [Scikit-learn Debugging Tips](https://scikit-learn.org/stable/common_pitfalls.html)

### Articles
- "Debugging Machine Learning Models" - Papers with Code
- "A Recipe for Training Neural Networks" - Andrej Karpathy
- "Troubleshooting Deep Neural Networks" - Josh Tobin

### Tools
- **TensorBoard:** Visualization for deep learning
- **Weights & Biases:** Experiment tracking
- **Neptune.ai:** ML metadata store

---

## 🚀 Next Steps

After completing Phase 16:
- **Phase 17:** Low-Code AI Tools (Gradio, Streamlit)
- **Phase 18:** Production Deployment
- **Advanced:** MLOps and Model Monitoring

---

## 💡 Tips for Success

1. **Be Systematic:** Follow the debugging workflow, don't guess randomly
2. **Start Simple:** Test with minimal data first, then scale up
3. **Document Everything:** Keep notes on what you tried and results
4. **Use Version Control:** Commit working code before experimenting
5. **Ask for Help:** Share reproducible examples when stuck

---

**Happy Debugging! Remember: Every bug is an opportunity to learn! 🐛→🦋**
