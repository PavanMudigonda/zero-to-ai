# Post-Quiz: Model Evaluation & Metrics

Test your knowledge after completing Phase 15!

**Time:** 15 minutes  
**Questions:** 15  
**Passing Score:** 70%

---

## Questions

### 1. A spam filter has precision=0.95 and recall=0.60. What does this mean?

A) 95% of spam is caught, but 40% of good emails are marked spam  
B) 60% of spam is caught, and 95% of spam predictions are correct  
C) The model is 95% accurate overall  
D) The model misses 5% of spam

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: Precision=0.95 means 95% of spam predictions are actually spam. Recall=0.60 means 60% of actual spam is caught. The model is conservative (high precision, lower recall).
</details>

---

### 2. When comparing MAE and RMSE, what does RMSE >> MAE indicate?

A) The model is perfect  
B) There are large outlier errors  
C) The metrics were calculated incorrectly  
D) The model has consistent small errors

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: RMSE is more sensitive to large errors (due to squaring). When RMSE is much larger than MAE, it indicates the presence of significant outliers.
</details>

---

### 3. Why is BERTScore better than BLEU for evaluating paraphrases?

A) BERTScore is faster to compute  
B) BERTScore uses semantic embeddings, not just word matching  
C) BERTScore only works with BERT models  
D) BERTScore is always higher than BLEU

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: BERTScore uses contextual embeddings to measure semantic similarity, so "the movie was great" and "the film was excellent" score highly even with no word overlap.
</details>

---

### 4. A model has R² = 0.85. What does this mean?

A) 85% of predictions are correct  
B) 85% of variance in the target is explained  
C) The model has 15% error rate  
D) 85% of features are important

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: R² = 0.85 means the model explains 85% of the variance in the target variable. The remaining 15% is unexplained (residual variance).
</details>

---

### 5. What is the key difference between equalized odds and demographic parity?

A) Equalized odds is stricter and requires equal TPR and FPR across groups  
B) Demographic parity is more mathematically rigorous  
C) They are the same thing with different names  
D) Equalized odds only applies to regression

<details>
<summary>Show Answer</summary>
**Correct Answer: A**

Explanation: Demographic parity only requires equal positive outcome rates. Equalized odds additionally requires equal true positive rates AND false positive rates across groups.
</details>

---

### 6. In a paired t-test comparing two models with p-value = 0.03, what can you conclude?

A) Model A is 97% accurate  
B) The difference is statistically significant at α=0.05  
C) Model B is better  
D) The models are identical

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: p-value < 0.05 means we reject the null hypothesis that the models perform equally - there IS a statistically significant difference (though we don't know which is better from the p-value alone).
</details>

---

### 7. Why use stratified k-fold instead of regular k-fold for imbalanced data?

A) It's faster  
B) It maintains class distribution in each fold  
C) It always gives better accuracy  
D) It's required by law

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: Stratified k-fold ensures each fold has the same class distribution as the original dataset, preventing folds with no positive examples in imbalanced scenarios.
</details>

---

### 8. What does perplexity measure?

A) Model accuracy  
B) How surprised/confused the model is by text  
C) Number of parameters  
D) Training time

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: Perplexity measures how well a language model predicts text. Low perplexity = confident/familiar. High perplexity = surprised/confused.
</details>

---

### 9. In A/B testing, what is the purpose of calculating required sample size?

A) To make the test faster  
B) To ensure sufficient statistical power to detect meaningful differences  
C) To reduce costs  
D) To guarantee Model B wins

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: Sample size calculation ensures you have enough data to reliably detect a meaningful effect size with desired statistical power (typically 80%).
</details>

---

### 10. What is the precision-recall trade-off?

A) Precision and recall always move together  
B) Increasing one typically decreases the other  
C) They are completely independent  
D) Precision is always more important

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: When you increase the threshold for positive prediction, precision typically increases (fewer false positives) but recall decreases (more false negatives), and vice versa.
</details>

---

### 11. McNemar's test is used to:

A) Compare regression models  
B) Compare two classifiers on the same test set  
C) Calculate accuracy  
D) Measure model complexity

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: McNemar's test is a statistical test for comparing two classification models by examining their disagreements on the same test set.
</details>

---

### 12. What does ROUGE-L measure?

A) Longest common subsequence between texts  
B) Only unigram overlap  
C) Grammatical correctness  
D) Model training time

<details>
<summary>Show Answer</summary>
**Correct Answer: A**

Explanation: ROUGE-L measures the longest common subsequence (LCS) between generated and reference text, capturing sentence-level structure.
</details>

---

### 13. Why might you choose MAE over RMSE?

A) MAE is always more accurate  
B) MAE is less sensitive to outliers  
C) MAE is faster to compute  
D) MAE works for classification

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: MAE treats all errors equally (absolute values), while RMSE squares errors, making it more sensitive to outliers. Choose MAE when you don't want outliers to dominate the metric.
</details>

---

### 14. What is the "4/5ths rule" in fairness testing?

A) Use 4/5 of data for training  
B) Selection rate for protected group ≥ 80% of highest group's rate  
C) Model must be 80% fair  
D) 4 out of 5 metrics must pass

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: Also called the 80% rule, it states that the selection rate (e.g., hiring, approval) for any group should be at least 80% of the rate for the group with the highest rate.
</details>

---

### 15. When would you use adjusted R² instead of regular R²?

A) When you have multiple features and want to penalize complexity  
B) When data is imbalanced  
C) When doing classification  
D) When R² is negative

<details>
<summary>Show Answer</summary>
**Correct Answer: A**

Explanation: Adjusted R² penalizes model complexity. Regular R² always increases when adding features (even random ones), but adjusted R² only increases if the new feature genuinely improves the model.
</details>

---

## Advanced Understanding Questions

### 16. (Bonus) A model has high precision but low recall for the positive class. What does this suggest about the decision threshold?

A) Threshold is too low  
B) Threshold is too high  
C) Threshold is perfect  
D) Threshold doesn't affect this

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: High precision + low recall means the model is very conservative - it only predicts positive when very confident (high threshold). Lowering the threshold would increase recall but decrease precision.
</details>

---

### 17. (Bonus) Why might statistical significance (p < 0.05) not always mean practical significance?

A) Statistics are always wrong  
B) Small differences can be statistically significant with large sample sizes  
C) P-values are random  
D) Only practical significance matters

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: With large sample sizes, even tiny differences become statistically significant. A 0.1% accuracy improvement might be statistically significant but not worth the deployment cost.
</details>

---

### 18. (Bonus) In RAG evaluation, what does "faithfulness" measure?

A) How well the retrieval works  
B) Whether the generated answer stays true to retrieved context  
C) User satisfaction  
D) Response time

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: Faithfulness measures whether the generated answer is grounded in the retrieved documents - does it make up information or stick to the facts from retrieval?
</details>

---

## Scoring Guide

- **16-18 correct:** Excellent! Master level understanding 🎓
- **13-15 correct:** Great! You've learned the material well ✅
- **10-12 correct:** Good! Review a few concepts 📚
- **7-9 correct:** Pass, but review topics you missed ⚠️
- **0-6 correct:** Review Phase 15 materials 🔄

---

## Knowledge Gaps to Address

Based on your incorrect answers, review:

**Metrics (Q1-4, 13):**
- Classification metrics interpretation
- Regression metrics selection
- Metric trade-offs

**LLM Evaluation (Q3, 8, 12, 18):**
- BLEU vs ROUGE vs BERTScore
- Perplexity
- Semantic evaluation
- RAG-specific metrics

**Fairness (Q5, 14):**
- Demographic parity vs equalized odds
- 80% rule
- Bias measurement

**Statistical Testing (Q6, 9, 11, 17):**
- Hypothesis testing
- Sample size calculation
- Practical vs statistical significance

**Model Comparison (Q7, 10, 15, 16):**
- Cross-validation variants
- Trade-off analysis
- Threshold optimization

---

## Next Steps

**If you scored well (13+):**
- ✅ Move to Phase 16: Debugging & Troubleshooting
- ✅ Complete the Phase 15 assignment
- ✅ Try advanced challenges

**If you need review (< 13):**
- 📚 Re-read relevant notebooks
- 🔄 Redo coding exercises
- 💬 Discuss with peers/instructor
- ✍️ Retake quiz after review

---

## Detailed Review Topics

### Must-Know Concepts:
1. **Classification Metrics**
   - Precision, Recall, F1-Score
   - Confusion matrix interpretation
   - ROC-AUC and PR-AUC
   - Threshold selection

2. **Regression Metrics**
   - MAE, RMSE, R²
   - Residual analysis
   - Metric selection criteria

3. **Fairness Metrics**
   - Demographic parity
   - Equalized odds
   - Bias detection
   - Mitigation strategies

4. **LLM Evaluation**
   - BLEU, ROUGE scores
   - Perplexity
   - Semantic similarity
   - Human evaluation

5. **Statistical Comparison**
   - Cross-validation
   - Hypothesis testing
   - A/B testing
   - Sample size calculation

---

**Congratulations on completing Phase 15! You're now equipped to properly evaluate ML models! 🎉**
