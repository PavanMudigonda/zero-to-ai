# Phase 15: Model Evaluation & Metrics

Learn how to measure, evaluate, and improve your AI models with comprehensive metrics and testing strategies.

---

## 🎯 Learning Objectives

By the end of this phase, you will be able to:

- ✅ Choose appropriate metrics for different ML tasks
- ✅ Evaluate classification and regression models
- ✅ Measure LLM and generative model performance
- ✅ Detect and mitigate model bias
- ✅ Conduct A/B tests and experiments
- ✅ Compare models effectively
- ✅ Make data-driven model selection decisions

---

## 📚 Phase Contents

### Notebooks

1. **[Classification Metrics](01_classification_metrics.ipynb)** (90 min)
   - Accuracy, Precision, Recall, F1-Score
   - ROC curves and AUC
   - Confusion matrices
   - Multi-class metrics
   - Imbalanced datasets

2. **[Regression Metrics](02_regression_metrics.ipynb)** (75 min)
   - MSE, RMSE, MAE
   - R² and Adjusted R²
   - MAPE and quantile metrics
   - Residual analysis

3. **[LLM Evaluation](03_llm_evaluation.ipynb)** (120 min)
   - Perplexity and cross-entropy
   - BLEU, ROUGE, METEOR scores
   - BERTScore and semantic similarity
   - Human evaluation frameworks
   - Prompt quality assessment

4. **[Bias & Fairness](04_bias_fairness.ipynb)** (90 min)
   - Fairness metrics (demographic parity, equalized odds)
   - Bias detection techniques
   - Mitigation strategies
   - Ethical considerations

5. **[Model Comparison](05_model_comparison.ipynb)** (60 min)
   - Statistical significance testing
   - Cross-validation strategies
   - Learning curves
   - A/B testing for ML

---

## 🛠️ Tools & Libraries

```bash
# Install required packages
pip install scikit-learn numpy pandas matplotlib seaborn
pip install scipy statsmodels
pip install nltk rouge-score bert-score
pip install fairlearn aif360
```

**Key Libraries:**
- **scikit-learn** - ML metrics and evaluation
- **NLTK, Rouge-Score** - NLP metrics
- **Fairlearn, AIF360** - Bias detection
- **SciPy, Statsmodels** - Statistical testing

---

## 📊 Real-World Applications

### 1. Healthcare - Disease Prediction
**Challenge:** Classify patients at risk of diabetes  
**Key Metrics:** Recall (catch all true cases), Precision (avoid false alarms)  
**Why:** Missing a positive case (low recall) is worse than a false alarm

### 2. E-commerce - Sales Forecasting
**Challenge:** Predict next quarter revenue  
**Key Metrics:** MAPE (percentage error), RMSE (magnitude of errors)  
**Why:** Business decisions based on accuracy percentage

### 3. Content Moderation - Toxic Comment Detection
**Challenge:** Filter harmful content  
**Key Metrics:** Recall (catch toxic content), Fairness (avoid bias)  
**Why:** Balance safety with avoiding over-censorship

### 4. Recommendation Systems
**Challenge:** Suggest products users will buy  
**Key Metrics:** Precision@K, NDCG, Diversity  
**Why:** Top recommendations matter most

---

## 🎯 Success Criteria

After completing this phase, you should be able to:

- [ ] Calculate and interpret confusion matrices
- [ ] Choose between precision and recall based on use case
- [ ] Evaluate regression models with multiple metrics
- [ ] Assess LLM outputs using automated metrics
- [ ] Detect bias in model predictions
- [ ] Run statistical significance tests
- [ ] Design and analyze A/B tests
- [ ] Create comprehensive evaluation reports

---

## 📝 Assignments & Challenges

### Assignment: Complete Model Evaluation Pipeline
Build an evaluation framework that:
- Compares 3+ models
- Uses 5+ appropriate metrics
- Tests for statistical significance
- Checks for bias
- Generates visualization reports

**Time Estimate:** 8-10 hours  
**Weight:** 100 points

### Challenges
1. **Imbalanced Classification** (⭐⭐) - Handle 99:1 class imbalance
2. **Regression Analysis** (⭐⭐⭐) - Predict housing prices with error analysis
3. **LLM Evaluation** (⭐⭐⭐⭐) - Compare GPT outputs with BLEU/ROUGE
4. **Bias Detection** (⭐⭐⭐⭐) - Find and fix gender bias in hiring model
5. **A/B Test Analysis** (⭐⭐⭐⭐⭐) - Design experiment, calculate sample size

---

## 🗓️ Learning Path

### Week 1: Classification & Regression
- **Days 1-2:** Classification metrics (accuracy → F1 → ROC)
- **Days 3-4:** Regression metrics (MSE → MAE → R²)
- **Day 5:** Practice with challenges 1-2

### Week 2: Advanced Topics
- **Days 1-2:** LLM evaluation metrics
- **Days 3-4:** Bias detection and fairness
- **Day 5:** Model comparison techniques

### Week 3: Project Work
- **Days 1-3:** Complete assignment
- **Days 4-5:** Review, optimize, document

**Total Time:** ~20-25 hours

---

## 📖 Prerequisites

**Required:**
- Phase 1-4: Python fundamentals and data manipulation
- Phase 5: Machine learning basics
- Phase 7: Model training experience

**Recommended:**
- Statistics knowledge (hypothesis testing, p-values)
- Experience with at least one ML project

---

## 🔗 Additional Resources

### Books
- *Evaluating Machine Learning Models* by Alice Zheng
- *Fairness and Machine Learning* by Barocas, Hardt, Narayanan

### Papers
- [BLEU: A Method for Automatic Evaluation of Machine Translation](https://aclanthology.org/P02-1040/)
- [ROUGE: A Package for Automatic Evaluation of Summaries](https://aclanthology.org/W04-1013/)
- [Fairness Definitions Explained](https://fairware.cs.umass.edu/papers/Verma.pdf)

### Online Courses
- [Model Evaluation by Google](https://developers.google.com/machine-learning/crash-course/classification)
- [Fairness in ML - MIT](https://mlr.cs.umass.edu/)

### Interactive Tools
- [ROC Curve Explorer](http://www.navan.name/roc/)
- [Confusion Matrix Calculator](https://www.scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)

---

## ❓ FAQ

**Q: How do I choose the right metric for my problem?**  
A: Consider: What matters more - false positives or false negatives? Is your data balanced? What's the business impact of errors?

**Q: Why not just use accuracy?**  
A: Accuracy is misleading with imbalanced data. A model that always predicts "negative" on 99:1 data gets 99% accuracy but is useless.

**Q: How many metrics should I track?**  
A: 3-5 metrics that cover different aspects (overall performance, class-specific, business metrics).

**Q: What's a "good" F1 score?**  
A: Depends on domain. Medical diagnosis might need 0.95+, while recommendation systems might be fine with 0.7+.

**Q: Should I always check for bias?**  
A: Yes, especially for models affecting people (hiring, lending, healthcare, criminal justice).

---

## 🎓 Learning Tips

1. **Start with Confusion Matrix** - Visualize before calculating metrics
2. **Compare Multiple Metrics** - One metric never tells the full story
3. **Use Real Data** - Practice with imbalanced, noisy datasets
4. **Visualize Everything** - ROC curves, residual plots, fairness charts
5. **Think Business Impact** - Metrics should align with real-world costs
6. **Test Assumptions** - Check if your test set represents production
7. **Document Trade-offs** - Explain why you chose certain metrics

---

## 🏆 Quiz Yourself

Before starting: [Take the Pre-Quiz](pre-quiz.md)  
After completion: [Take the Post-Quiz](post-quiz.md)

Track your progress and identify areas for deeper study!

---

## 🚀 Next Steps

After mastering model evaluation:
- **Phase 16:** Debugging & Troubleshooting
- **Phase 17:** Production Deployment
- **Phase 18:** MLOps & Monitoring

---

**Ready to become an expert at measuring what matters? Let's dive in! 📊**
