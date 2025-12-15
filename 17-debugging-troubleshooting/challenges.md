# Debugging & Troubleshooting Challenges

Progressive challenges to master ML debugging skills.

---

## Challenge 1: The Mystery Bug ⭐⭐

**Difficulty:** Beginner  
**Time:** 30-45 minutes  
**Topic:** Basic debugging workflow

### Scenario
A junior data scientist wrote code that "works" but gives terrible results. Find and fix the bugs!

### Code
```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Shuffle (for randomness!)
np.random.shuffle(X_train)
np.random.shuffle(y_train)

# Train
model = LogisticRegression()
model.fit(X_train, y_train)

print(f"Accuracy: {model.score(X_test, y_test):.3f}")
```

### Requirements
1. Identify all bugs (there are 2)
2. Explain why each is a problem
3. Fix the code
4. Document expected vs actual behavior
5. Verify fix with multiple random seeds

### Success Criteria
- ✅ Bugs identified correctly
- ✅ Clear explanation of issues
- ✅ Fixed code achieves >85% accuracy
- ✅ Documented properly

### Learning Objectives
- Recognize data leakage patterns
- Understand feature-label alignment
- Apply debugging workflow

---

## Challenge 2: Data Detective ⭐⭐⭐

**Difficulty:** Intermediate  
**Time:** 1-2 hours  
**Topic:** Data quality issues

### Scenario
Your model performs well in training but fails in production. Investigate the dataset!

### Dataset
Download: [UCI Adult Income dataset](https://archive.ics.uci.edu/ml/datasets/adult)

### Requirements
1. **Missing Value Analysis**
   - Find all columns with missing data
   - Calculate missing percentage
   - Recommend handling strategy per column
   - Implement and compare 2 strategies

2. **Outlier Detection**
   - Apply Z-score method
   - Apply IQR method
   - Compare results
   - Visualize outliers
   - Decide on handling approach

3. **Duplicate Detection**
   - Find exact duplicates
   - Find near-duplicates (optional)
   - Analyze impact on model

4. **Distribution Shift**
   - Split data by time/group
   - Test for distribution shift
   - Quantify the shift

### Deliverables
- Jupyter notebook with full analysis
- Visualizations for each issue type
- Before/after performance comparison
- Summary report with recommendations

### Success Criteria
- ✅ All data issues identified
- ✅ Multiple detection methods used
- ✅ Clear visualizations
- ✅ Quantified improvements

### Bonus (⭐)
- Detect label noise
- Create automated data quality report
- Build data validation pipeline

---

## Challenge 3: Speed Demon ⭐⭐⭐

**Difficulty:** Intermediate  
**Time:** 2-3 hours  
**Topic:** Performance optimization

### Scenario
Your ML pipeline is too slow for production. Optimize it!

### Code (Slow Pipeline)
```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load data (1M rows)
data = pd.DataFrame(np.random.randn(1000000, 50))
target = np.random.randint(0, 2, 1000000)

# Slow preprocessing
processed = []
for idx, row in data.iterrows():
    normalized = (row - row.mean()) / row.std()
    processed.append(normalized)
data_processed = pd.DataFrame(processed)

# Slow predictions
model = RandomForestClassifier(n_estimators=100)
model.fit(data_processed[:800000], target[:800000])

predictions = []
for i in range(800000, 1000000):
    pred = model.predict(data_processed.iloc[i:i+1])[0]
    predictions.append(pred)
```

### Requirements
1. **Profile the code**
   - Use cProfile
   - Identify top 3 bottlenecks
   - Calculate time percentage for each

2. **Optimize**
   - Vectorize preprocessing
   - Batch predictions
   - Use parallel processing
   - Cache where applicable

3. **Benchmark**
   - Measure before/after speed
   - Measure memory usage
   - Create comparison table
   - Verify results match

### Success Criteria
- ✅ Minimum 10x speedup
- ✅ Memory usage reduced
- ✅ Results identical to original
- ✅ Code is readable and documented

### Bonus (⭐)
- Achieve 50x+ speedup
- Use line_profiler
- Create performance visualization
- Optimize memory further

---

## Challenge 4: Convergence Crisis ⭐⭐⭐⭐

**Difficulty:** Advanced  
**Time:** 2-3 hours  
**Topic:** Model debugging

### Scenario
Your neural network won't converge. Debug and fix it!

### Code
```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.neural_network import MLPClassifier

X, y = make_classification(
    n_samples=10000, n_features=100, 
    n_informative=50, random_state=42
)

# Don't scale features
model = MLPClassifier(
    hidden_layer_sizes=(100, 50),
    learning_rate_init=1.0,  # High learning rate
    max_iter=10,  # Too few iterations
    random_state=42,
    verbose=True
)

model.fit(X, y)
print(f"Score: {model.score(X, y):.3f}")
```

### Requirements
1. **Diagnose Issues**
   - Identify all problems
   - Explain impact of each
   - Prioritize fixes

2. **Fix Systematically**
   - Scale features
   - Tune learning rate
   - Adjust iterations
   - Monitor convergence

3. **Learning Curves**
   - Plot training vs validation loss
   - Diagnose overfitting/underfitting
   - Apply regularization if needed

4. **Hyperparameter Tuning**
   - Try different architectures
   - Test learning rates: [0.001, 0.01, 0.1]
   - Create validation curves

### Success Criteria
- ✅ Model converges properly
- ✅ No convergence warnings
- ✅ Test accuracy >85%
- ✅ Learning curves look healthy

### Bonus (⭐)
- Implement early stopping
- Use GridSearchCV
- Compare with other models
- Analyze gradient flow

---

## Challenge 5: Error Analyzer ⭐⭐⭐⭐

**Difficulty:** Advanced  
**Time:** 3-4 hours  
**Topic:** Error analysis

### Scenario
Your model has 90% accuracy but fails on critical cases. Analyze and improve!

### Dataset
Use MNIST digits or similar multi-class dataset

### Requirements
1. **Confusion Matrix Analysis**
   - Generate confusion matrix
   - Identify top 5 confused pairs
   - Visualize normalized matrix
   - Explain patterns

2. **Per-Class Performance**
   - Calculate precision/recall/F1 per class
   - Identify worst 3 classes
   - Analyze why they perform poorly
   - Propose class-specific fixes

3. **Failure Case Analysis**
   - Collect 20+ failure examples
   - Categorize error types
   - Visualize failure cases
   - Find common patterns

4. **Confidence Analysis**
   - Plot confidence distribution
   - Separate correct/incorrect
   - Find high-confidence errors
   - Create calibration curve

5. **Action Plan**
   - Prioritize improvements
   - Estimate impact
   - Propose data collection strategy
   - Suggest model changes

### Deliverables
- Complete error analysis report
- Visualizations for all analyses
- Categorized failure cases
- Detailed improvement roadmap

### Success Criteria
- ✅ Comprehensive confusion matrix analysis
- ✅ All classes analyzed
- ✅ Failure patterns identified
- ✅ Actionable recommendations

### Bonus (⭐)
- Implement one improvement
- Show before/after comparison
- Create error monitoring dashboard

---

## Challenge 6: The Production Mystery ⭐⭐⭐⭐⭐

**Difficulty:** Expert  
**Time:** 4-6 hours  
**Topic:** Real-world debugging

### Scenario
Your model works perfectly in development but fails in production. Why?

### Given Information
- Training accuracy: 95%
- Test accuracy: 94%
- Production accuracy: 65% (after 1 month)
- No code changes were made
- Different data source in production

### Requirements
1. **Hypothesis Generation**
   - List 5+ possible causes
   - Rank by likelihood
   - Plan investigation steps

2. **Distribution Shift Analysis**
   - Compare train vs production distributions
   - Statistical tests (K-S, chi-square)
   - Visualize differences
   - Quantify shift magnitude

3. **Feature Drift Detection**
   - Monitor feature statistics
   - Detect out-of-range values
   - Identify concept drift
   - Track label distribution

4. **Root Cause Analysis**
   - Investigate data pipeline
   - Check preprocessing consistency
   - Validate assumptions
   - Document findings

5. **Solutions**
   - Propose fixes
   - Implement monitoring
   - Create retraining strategy
   - Build alerting system

### Deliverables
- Investigation report
- Distribution analysis
- Monitoring dashboard design
- Retraining pipeline proposal
- Documentation for ops team

### Success Criteria
- ✅ Root cause identified
- ✅ Distribution shift quantified
- ✅ Solution implemented
- ✅ Monitoring in place
- ✅ Future prevention strategy

### Bonus (⭐⭐)
- Implement automated retraining
- Create A/B testing framework
- Build model versioning system
- Deploy monitoring dashboard

---

## Challenge 7: Debug the Debugger ⭐⭐⭐⭐⭐

**Difficulty:** Expert  
**Time:** 5-8 hours  
**Topic:** Comprehensive debugging

### Scenario
Build a comprehensive debugging toolkit for ML pipelines!

### Requirements
1. **Automated Bug Detection**
   ```python
   class MLPipelineDebugger:
       def check_data_leakage(self, pipeline):
           # Detect common leakage patterns
           pass
       
       def check_feature_target_alignment(self, X, y):
           # Verify alignment
           pass
       
       def check_scaling_issues(self, scaler, X_train, X_test):
           # Detect scaling problems
           pass
       
       def check_class_imbalance(self, y):
           # Identify severe imbalance
           pass
       
       def check_convergence(self, model):
           # Verify model converged
           pass
   ```

2. **Performance Profiler**
   - CPU time tracking
   - Memory usage monitoring
   - Bottleneck identification
   - Optimization suggestions

3. **Model Health Checker**
   - Overfitting detection
   - Underfitting detection
   - Learning curve analysis
   - Validation curve generation

4. **Error Analyzer**
   - Automatic confusion matrix
   - Per-class metrics
   - Failure case collection
   - Confidence analysis

5. **Report Generator**
   - Create HTML report
   - Include all analyses
   - Actionable recommendations
   - Export to PDF

### Deliverables
- `ml_debugger.py` - Complete toolkit
- Test suite with 10+ test cases
- Documentation with examples
- Sample reports (HTML/PDF)
- Tutorial notebook

### Success Criteria
- ✅ All checkers implemented
- ✅ Catches common bugs
- ✅ Works with sklearn models
- ✅ Generates useful reports
- ✅ Well documented

### Bonus (⭐⭐⭐)
- Support PyTorch/TensorFlow
- Add interactive visualizations
- Create CLI tool
- Publish as package
- Add CI/CD integration

---

## 🏆 Completion Tracker

Track your progress:

- [ ] Challenge 1: The Mystery Bug ⭐⭐
- [ ] Challenge 2: Data Detective ⭐⭐⭐
- [ ] Challenge 3: Speed Demon ⭐⭐⭐
- [ ] Challenge 4: Convergence Crisis ⭐⭐⭐⭐
- [ ] Challenge 5: Error Analyzer ⭐⭐⭐⭐
- [ ] Challenge 6: The Production Mystery ⭐⭐⭐⭐⭐
- [ ] Challenge 7: Debug the Debugger ⭐⭐⭐⭐⭐

---

## 💡 Tips

1. **Start Simple:** Begin with Challenge 1 and progress
2. **Document Everything:** Keep notes on what you tried
3. **Measure First:** Always establish baseline before optimizing
4. **Test Thoroughly:** Verify fixes work with different data
5. **Learn from Failures:** Every bug teaches something valuable

---

## 📚 Resources

- [Python Debugging Guide](https://docs.python.org/3/library/pdb.html)
- [Scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)
- [A Recipe for Training Neural Networks - Andrej Karpathy](http://karpathy.github.io/2019/04/25/recipe/)

---

**Happy Debugging! 🐛→🦋**
