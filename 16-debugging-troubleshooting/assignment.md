# Assignment: Debug & Optimize a Broken ML Pipeline

**Total Points:** 100 (+ 20 bonus)  
**Duration:** 4-6 hours  
**Difficulty:** ⭐⭐⭐⭐

---

## 📋 Objective

You've been given a broken ML pipeline that has multiple issues affecting performance, speed, and reliability. Your task is to systematically debug, optimize, and document all improvements.

---

## 🎯 Learning Goals

- Apply systematic debugging workflows
- Diagnose data quality issues
- Profile and optimize code performance
- Fix model convergence problems
- Conduct comprehensive error analysis

---

## 📦 Dataset

Choose ONE of the following:
1. **UCI Adult Income** (Classification)
2. **California Housing** (Regression)
3. **MNIST Digits** (Multi-class Classification)
4. **Custom dataset** (with instructor approval)

**Requirements:**
- Minimum 5,000 samples
- At least 10 features
- Real-world dataset (not synthetic)

---

## 🛠️ Part 1: Initial Assessment (15 points)

### Tasks:
1. **Run the provided buggy code** (see below)
2. **Document all issues** you observe
3. **Create a baseline report** with:
   - Current accuracy/performance
   - Execution time
   - Memory usage
   - List of identified problems

### Deliverables:
- `01_initial_assessment.md` - Problem documentation
- Screenshots of errors/warnings
- Baseline performance metrics

### Grading Rubric:
- Comprehensive problem list (8 pts)
- Baseline metrics documented (4 pts)
- Clear documentation (3 pts)

---

## 🐛 Part 2: Data Quality Debugging (20 points)

### Tasks:
1. **Missing values analysis**
   - Identify columns with missing data
   - Recommend handling strategy
   - Implement solution

2. **Duplicate detection**
   - Find and remove duplicates
   - Document impact

3. **Outlier analysis**
   - Use 2+ detection methods
   - Visualize outliers
   - Decide on handling strategy

4. **Distribution shift check**
   - Compare train/test distributions
   - Statistical tests (K-S test)
   - Document findings

### Deliverables:
- `02_data_quality_report.ipynb`
- Visualizations of data issues
- Before/after comparison

### Grading Rubric:
- Missing value handling (5 pts)
- Outlier detection & handling (5 pts)
- Distribution analysis (5 pts)
- Visualization quality (3 pts)
- Documentation (2 pts)

---

## ⚡ Part 3: Performance Profiling & Optimization (25 points)

### Tasks:
1. **CPU Profiling**
   - Use cProfile to identify hotspots
   - Document top 5 slowest functions
   - Calculate time percentages

2. **Memory Profiling**
   - Track memory usage
   - Identify memory leaks
   - Measure peak memory

3. **Optimization**
   - Apply vectorization where possible
   - Implement batch processing
   - Use parallelization (n_jobs=-1)
   - Cache repeated computations

4. **Benchmarking**
   - Before/after timing comparison
   - Document speedup factor
   - Memory reduction percentage

### Deliverables:
- `03_profiling_report.ipynb`
- Profiling output files
- Optimization code with comments
- Performance comparison table

### Grading Rubric:
- Comprehensive profiling (7 pts)
- Multiple optimization techniques (10 pts)
- Quantified improvements (5 pts)
- Code quality & documentation (3 pts)

---

## 🔧 Part 4: Model Debugging (20 points)

### Tasks:
1. **Learning Curves**
   - Plot training vs validation curves
   - Diagnose overfitting/underfitting
   - Determine if more data would help

2. **Convergence Analysis**
   - Check for convergence warnings
   - Scale features properly
   - Tune learning rate
   - Verify convergence

3. **Regularization**
   - Try L1 (Lasso) and L2 (Ridge)
   - Create validation curves
   - Find optimal alpha

4. **Model Comparison**
   - Test 3+ models
   - Compare complexity vs performance
   - Justify final model choice

### Deliverables:
- `04_model_debugging.ipynb`
- Learning curve plots
- Validation curves
- Model comparison table

### Grading Rubric:
- Learning curve analysis (5 pts)
- Convergence fixes (5 pts)
- Regularization experiments (5 pts)
- Model selection justification (5 pts)

---

## 📊 Part 5: Error Analysis (20 points)

### Tasks:
1. **Confusion Matrix Analysis**
   - Generate confusion matrix
   - Identify most confused pairs
   - Normalize by class

2. **Per-Class Performance**
   - Calculate precision, recall, F1 per class
   - Identify worst-performing classes
   - Visualize performance distribution

3. **Failure Case Analysis**
   - Collect 10+ failure examples
   - Categorize error types
   - Analyze patterns

4. **Confidence Calibration**
   - Plot confidence distribution
   - Separate correct/incorrect predictions
   - Create calibration curve

5. **Improvement Recommendations**
   - List top 3 priority improvements
   - Justify with data
   - Estimate expected impact

### Deliverables:
- `05_error_analysis.ipynb`
- Comprehensive error report
- Failure case visualizations
- Improvement roadmap

### Grading Rubric:
- Confusion matrix insights (5 pts)
- Per-class analysis (5 pts)
- Failure case categorization (5 pts)
- Actionable recommendations (5 pts)

---

## 📝 Buggy Code Template

```python
# BUGGY ML PIPELINE - FIX ALL ISSUES!

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
data = pd.read_csv('your_dataset.csv')

# Bug 1: Not handling missing values
X = data.drop('target', axis=1)
y = data['target']

# Bug 2: Wrong test size
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.9  # Should be 0.2!
)

# Bug 3: Shuffling features and labels independently
np.random.shuffle(X_train.values)
np.random.shuffle(y_train.values)

# Bug 4: Scaling on test data
scaler = StandardScaler()
scaler.fit(X_test)  # Should fit on train!
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Bug 5: Row-wise normalization (slow!)
X_train_normalized = []
for row in X_train:
    X_train_normalized.append((row - row.mean()) / row.std())
X_train = np.array(X_train_normalized)

# Bug 6: Wrong labels for training
model = LogisticRegression(max_iter=10)  # Bug 7: Too few iterations
model.fit(X_train, y_test)  # Should be y_train!

# Bug 8: Evaluating on training data
accuracy = model.score(X_train, y_train)

print(f"Accuracy: {accuracy:.3f}")

# Bug 9: No error handling, logging, or validation
# Bug 10: Not checking for convergence
```

**Your task: Fix ALL bugs and add proper debugging/logging!**

---

## 🎁 Bonus Challenges (20 points)

### Bonus 1: Advanced Profiling (5 points)
- Use line_profiler for line-by-line analysis
- Use memory_profiler with decorators
- Create flame graphs or profiling visualizations

### Bonus 2: Automated Bug Detection (5 points)
- Write a function that automatically detects common issues
- Check for: data leakage, scaling problems, shape mismatches
- Create a "pre-flight checklist" tool

### Bonus 3: A/B Testing (5 points)
- Compare optimized vs original pipeline
- Run statistical significance tests
- Document confidence intervals

### Bonus 4: Production Monitoring (5 points)
- Add comprehensive logging
- Implement error alerts
- Create monitoring dashboard
- Set up performance tracking

---

## 📤 Submission Requirements

### File Structure:
```
debugging_assignment/
├── README.md (Summary of all work)
├── 01_initial_assessment.md
├── 02_data_quality_report.ipynb
├── 03_profiling_report.ipynb
├── 04_model_debugging.ipynb
├── 05_error_analysis.ipynb
├── data/
│   └── dataset.csv
├── figures/
│   ├── confusion_matrix.png
│   ├── learning_curves.png
│   └── ...
└── src/
    ├── fixed_pipeline.py
    └── debugging_utils.py
```

### Documentation Requirements:
- Clear markdown headers and sections
- Code comments explaining fixes
- Visualizations with titles and labels
- Summary of improvements in README

### Code Quality:
- PEP 8 compliance
- Proper error handling
- Logging throughout
- Type hints (bonus)

---

## 🎯 Grading Summary

| Component | Points |
|-----------|--------|
| Part 1: Initial Assessment | 15 |
| Part 2: Data Quality | 20 |
| Part 3: Performance Optimization | 25 |
| Part 4: Model Debugging | 20 |
| Part 5: Error Analysis | 20 |
| **Base Total** | **100** |
| Bonus Challenges | +20 |
| **Maximum Total** | **120** |

---

## 💡 Tips for Success

1. **Work Systematically**
   - Follow the debugging workflow
   - Document each fix
   - Test after each change

2. **Measure Everything**
   - Baseline first, then optimize
   - Quantify all improvements
   - Compare before/after

3. **Visualize**
   - Plots reveal patterns
   - Show distributions
   - Highlight insights

4. **Document Well**
   - Explain WHY you made changes
   - Justify decisions with data
   - Write for future you

5. **Test Thoroughly**
   - Verify fixes work
   - Check edge cases
   - Validate with different seeds

---

## 📅 Timeline

**Week 1:**
- Complete Parts 1-2 (Initial Assessment + Data Quality)

**Week 2:**
- Complete Part 3 (Performance Optimization)

**Week 3:**
- Complete Parts 4-5 (Model Debugging + Error Analysis)

**Week 4:**
- Bonus challenges (optional)
- Final polish and submission

---

## 🆘 Getting Help

- **Office Hours:** [Time/Location]
- **Discussion Forum:** [Link]
- **Example Notebooks:** See course materials

---

## ✅ Submission Checklist

Before submitting, verify:
- [ ] All 5 required notebooks completed
- [ ] All bugs in template code fixed
- [ ] Performance improvements quantified
- [ ] Comprehensive error analysis
- [ ] Clear documentation throughout
- [ ] Code runs without errors
- [ ] README.md summarizes all work
- [ ] Files organized properly
- [ ] Visualizations included
- [ ] Submitted on time

---

**Good luck with your debugging! Remember: Every bug you fix makes you a better ML engineer! 🚀**
