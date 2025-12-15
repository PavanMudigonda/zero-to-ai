# Phase 15 Challenges: Model Evaluation & Metrics

Complete these progressive challenges to master model evaluation techniques!

---

## Challenge 1: Imbalanced Classification Metrics ⭐⭐

**Difficulty:** Beginner  
**Time:** 30-45 minutes  
**Topics:** Classification metrics, imbalanced data

### Task

You're building a fraud detection system where only 1% of transactions are fraudulent.

**Dataset:**
- 10,000 transactions
- 100 fraudulent (1%)
- 9,900 legitimate (99%)

**Your Tasks:**

1. Create a "dummy" classifier that always predicts "Not Fraud"
   - Calculate accuracy, precision, recall, F1
   - Explain why high accuracy is misleading

2. Build a better classifier (any algorithm)
   - Use appropriate metrics (F1, ROC-AUC, PR-AUC)
   - Create confusion matrix visualization
   - Calculate precision@K for different K values

3. Compare the two classifiers
   - Which metric best shows improvement?
   - What threshold would you recommend?

### Success Criteria

- [ ] Dummy classifier implemented
- [ ] Demonstrate accuracy paradox
- [ ] Better classifier with F1 > 0.50
- [ ] ROC and PR curves created
- [ ] Threshold analysis completed
- [ ] Written justification (200+ words)

### Learning Objectives

- Understanding accuracy limitations
- Choosing metrics for imbalanced data
- Threshold optimization
- Precision-recall trade-offs

---

## Challenge 2: Regression Error Analysis ⭐⭐⭐

**Difficulty:** Intermediate  
**Time:** 1-2 hours  
**Topics:** Regression metrics, residual analysis

### Task

Build a house price prediction model and perform comprehensive error analysis.

**Dataset:** Use California Housing or Boston Housing dataset

**Your Tasks:**

1. **Train 3 regression models:**
   - Linear Regression
   - Random Forest
   - Gradient Boosting

2. **Calculate metrics:**
   - MAE, RMSE, R², MAPE
   - Compare MAE/RMSE ratio (detect outliers)
   - Calculate by price range (low/mid/high)

3. **Residual analysis:**
   - Plot residuals vs predicted
   - Check normality (Q-Q plot, Shapiro-Wilk test)
   - Identify heteroscedasticity
   - Find worst predictions

4. **Error breakdown:**
   - Errors by neighborhood/location
   - Errors by price range
   - Identify systematic errors

### Success Criteria

- [ ] 3 models trained and compared
- [ ] All metrics calculated
- [ ] Residual plots created (4+ plots)
- [ ] Outliers identified and analyzed
- [ ] Systematic errors documented
- [ ] Model improvement recommendations (300+ words)

### Learning Objectives

- Regression metric selection
- Residual diagnostics
- Outlier detection
- Model debugging

---

## Challenge 3: LLM Output Evaluation ⭐⭐⭐

**Difficulty:** Intermediate  
**Time:** 2-3 hours  
**Topics:** BLEU, ROUGE, BERTScore, semantic similarity

### Task

Compare different LLM outputs for a summarization task.

**Dataset:** Create or use:
- CNN/DailyMail summaries
- XSum dataset
- Or generate 20+ article-summary pairs

**Your Tasks:**

1. **Generate summaries from 3 different approaches:**
   - Extractive (select key sentences)
   - Rule-based (heuristics)
   - LLM-based (GPT/Claude if available, or use pre-generated)

2. **Calculate metrics:**
   - BLEU (1-gram through 4-gram)
   - ROUGE (ROUGE-1, ROUGE-2, ROUGE-L)
   - BERTScore (if possible)

3. **Analysis:**
   - Which metric correlates best with quality?
   - Find examples where BLEU is misleading
   - Compare lexical (BLEU/ROUGE) vs semantic (BERTScore)

4. **Human evaluation:**
   - Create rubric (fluency, coherence, relevance)
   - Evaluate 10 summaries manually
   - Compare automated vs human scores

### Success Criteria

- [ ] 3 summarization approaches implemented
- [ ] BLEU and ROUGE scores calculated
- [ ] BERTScore calculated (or alternative semantic metric)
- [ ] Human evaluation completed (10+ samples)
- [ ] Correlation analysis between metrics
- [ ] Findings report (400+ words)

### Learning Objectives

- LLM evaluation techniques
- Metric limitations
- Semantic vs lexical matching
- Human evaluation design

---

## Challenge 4: Bias Detection & Measurement ⭐⭐⭐⭐

**Difficulty:** Advanced  
**Time:** 3-4 hours  
**Topics:** Fairness metrics, bias detection, group analysis

### Task

Audit a hiring/lending model for bias across protected groups.

**Dataset:** Use:
- UCI Adult Income dataset
- German Credit dataset
- COMPAS recidivism data (if available)
- Or synthetic dataset with known bias

**Your Tasks:**

1. **Data analysis:**
   - Document class distribution by protected group
   - Statistical tests for independence
   - Feature correlation with protected attributes

2. **Train biased model:**
   - Any classifier
   - Evaluate overall performance
   - Calculate group-wise metrics

3. **Fairness metrics:**
   - Demographic parity difference/ratio
   - Equalized odds difference
   - Equal opportunity difference
   - Check 80% rule

4. **Disparate impact analysis:**
   - Confusion matrices by group
   - FPR and FNR by group
   - Precision and recall by group
   - Visualize disparities

5. **Bias mitigation:**
   - Implement 2 mitigation techniques
   - Compare fairness before/after
   - Document accuracy-fairness trade-off

### Success Criteria

- [ ] Comprehensive bias audit completed
- [ ] 5+ fairness metrics calculated
- [ ] Group-wise performance analyzed
- [ ] Statistical significance tested
- [ ] 2 mitigation techniques applied
- [ ] Trade-off analysis documented
- [ ] Report with recommendations (600+ words)

### Learning Objectives

- Fairness metric calculation
- Bias detection in practice
- Mitigation techniques
- Accuracy-fairness trade-offs
- Ethical AI considerations

---

## Challenge 5: Statistical Model Comparison ⭐⭐⭐⭐

**Difficulty:** Advanced  
**Time:** 3-4 hours  
**Topics:** Cross-validation, statistical tests, significance testing

### Task

Rigorously compare 5+ models with statistical validation.

**Dataset:** Any classification or regression dataset (1000+ samples)

**Your Tasks:**

1. **Model training:**
   - Train 5 different model types
   - Use stratified 10-fold cross-validation
   - Track all metrics across folds

2. **Statistical testing:**
   - Paired t-tests (all pairwise comparisons)
   - McNemar's test (classification)
   - Create significance matrix
   - Bonferroni correction for multiple comparisons

3. **Confidence intervals:**
   - Calculate 95% CI for each model
   - Bootstrap confidence intervals
   - Visualize with error bars

4. **Power analysis:**
   - Calculate statistical power
   - Determine minimum sample size
   - Sensitivity analysis

5. **Learning curves:**
   - Plot for all models
   - Identify overfitting/underfitting
   - Recommend training data size

### Success Criteria

- [ ] 5+ models compared
- [ ] 10-fold cross-validation used
- [ ] Statistical tests performed (10+ comparisons)
- [ ] Significance matrix created
- [ ] Confidence intervals calculated
- [ ] Learning curves generated
- [ ] Power analysis completed
- [ ] Detailed methodology report (500+ words)

### Learning Objectives

- Rigorous model comparison
- Statistical hypothesis testing
- Multiple testing corrections
- Power and sample size analysis
- Scientific method in ML

---

## Challenge 6: A/B Testing Simulation ⭐⭐⭐⭐⭐

**Difficulty:** Expert  
**Time:** 4-6 hours  
**Topics:** A/B testing, production evaluation, sequential testing

### Task

Design and simulate a complete A/B test for model deployment.

**Scenario:**
- Current model (A) in production
- New model (B) to test
- Simulate 10,000 user interactions

**Your Tasks:**

1. **Experimental design:**
   - Define primary and secondary metrics
   - Calculate required sample size
   - Design randomization scheme
   - Set up guardrail metrics

2. **Simulation:**
   - Generate synthetic user interactions
   - Randomly assign to A or B (50/50)
   - Track metrics over time
   - Simulate various scenarios (B wins, loses, tie)

3. **Sequential analysis:**
   - Implement sequential probability ratio test
   - Early stopping rules
   - Monitor p-values over time
   - Handle peeking problem

4. **Results analysis:**
   - Statistical significance test
   - Confidence intervals for lift
   - Heterogeneous treatment effects (if applicable)
   - Cost-benefit analysis

5. **Monitoring dashboard:**
   - Create visualizations for stakeholders
   - Real-time metric tracking
   - Decision framework
   - Rollout plan

### Success Criteria

- [ ] Sample size calculation correct
- [ ] A/B test simulation implemented
- [ ] Sequential testing applied
- [ ] 3+ scenarios tested (win/lose/tie)
- [ ] Statistical analysis complete
- [ ] Dashboard mockup created
- [ ] Rollout plan documented
- [ ] Comprehensive report (800+ words)

### Learning Objectives

- A/B test design
- Sequential hypothesis testing
- Production ML evaluation
- Stakeholder communication
- Decision-making under uncertainty

---

## Challenge 7: Multi-Objective Model Selection ⭐⭐⭐⭐⭐

**Difficulty:** Expert  
**Time:** 4-6 hours  
**Topics:** Pareto optimality, trade-off analysis, decision making

### Task

Select the best model when objectives conflict (accuracy vs fairness vs speed).

**Dataset:** Any real-world dataset with protected attributes

**Your Tasks:**

1. **Train diverse model zoo (8+ models):**
   - Various complexity levels
   - Different algorithms
   - Measure: accuracy, fairness, speed, memory, interpretability

2. **Pareto frontier:**
   - Identify Pareto-optimal models
   - Visualize in 2D/3D
   - Eliminate dominated models

3. **Multi-criteria decision analysis:**
   - Weighted sum approach
   - TOPSIS method
   - Analytic Hierarchy Process (AHP)

4. **Sensitivity analysis:**
   - Test different weight configurations
   - Identify robust choices
   - Scenario planning (accuracy-focused, fairness-focused, balanced)

5. **Stakeholder analysis:**
   - Define 3 stakeholder profiles
   - Recommend model for each
   - Document trade-offs

### Success Criteria

- [ ] 8+ models trained
- [ ] 5+ objectives measured
- [ ] Pareto frontier identified
- [ ] 3 MCDA methods applied
- [ ] Sensitivity analysis complete
- [ ] Stakeholder recommendations made
- [ ] Interactive visualization created
- [ ] Decision framework documented (1000+ words)

### Learning Objectives

- Multi-objective optimization
- Pareto optimality
- Decision analysis techniques
- Stakeholder management
- Real-world ML deployment

---

## 🏆 Challenge Completion Tracker

| Challenge | Status | Date | Notes |
|-----------|--------|------|-------|
| 1. Imbalanced Classification | ⬜ | | |
| 2. Regression Error Analysis | ⬜ | | |
| 3. LLM Output Evaluation | ⬜ | | |
| 4. Bias Detection | ⬜ | | |
| 5. Statistical Comparison | ⬜ | | |
| 6. A/B Testing | ⬜ | | |
| 7. Multi-Objective Selection | ⬜ | | |

---

## 💡 General Tips

1. **Start simple:** Begin with basic versions, then enhance
2. **Document everything:** Explain your choices and interpret results
3. **Visualize:** Create clear, professional plots
4. **Test edge cases:** Don't just test the happy path
5. **Seek feedback:** Share results with peers or mentors

---

**Complete all 7 challenges to become a model evaluation expert! 🎯**
