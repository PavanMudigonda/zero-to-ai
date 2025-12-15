# Pre-Quiz: Model Evaluation & Metrics

Test your baseline knowledge before starting Phase 15!

**Time:** 10 minutes  
**Questions:** 10  
**Passing Score:** 60%

---

## Questions

### 1. What is the main limitation of using accuracy for imbalanced datasets?

A) Accuracy is too difficult to calculate  
B) Accuracy can be misleadingly high even if the model doesn't work well  
C) Accuracy only works for regression problems  
D) Accuracy requires too much computational power

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: With imbalanced data (e.g., 99% negative, 1% positive), a model that always predicts "negative" achieves 99% accuracy but is completely useless for detecting the positive class.
</details>

---

### 2. Which metric answers: "Of all positive predictions, how many were correct?"

A) Recall  
B) Precision  
C) F1-Score  
D) Accuracy

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: Precision = TP / (TP + FP), which measures the proportion of positive predictions that are actually correct.
</details>

---

### 3. What does RMSE stand for?

A) Root Mean Square Estimation  
B) Regression Mean Squared Error  
C) Root Mean Squared Error  
D) Random Mean Square Evaluation

<details>
<summary>Show Answer</summary>
**Correct Answer: C**

Explanation: RMSE = Root Mean Squared Error, calculated as sqrt(MSE).
</details>

---

### 4. Why is BLEU score primarily used for machine translation?

A) It only works with translated text  
B) It measures word-level overlap between generated and reference text  
C) It can only evaluate English text  
D) It measures grammatical correctness

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: BLEU compares n-gram overlap between generated and reference text, making it suitable for translation where lexical similarity matters.
</details>

---

### 5. What is demographic parity in fairness metrics?

A) All groups must have equal prediction accuracy  
B) All groups must have equal positive outcome rates  
C) All groups must have the same features  
D) All groups must be the same size

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: Demographic parity requires that the positive outcome rate (e.g., approval rate) is equal across different demographic groups.
</details>

---

### 6. What does an R² score of 0 mean?

A) Perfect predictions  
B) Model is as good as predicting the mean  
C) Model is completely wrong  
D) Cannot calculate R²

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: R² = 0 means the model performs no better than simply predicting the average value for all samples.
</details>

---

### 7. Why use cross-validation instead of a single train/test split?

A) It's faster to compute  
B) It uses less data  
C) It provides a more reliable performance estimate  
D) It always gives better accuracy

<details>
<summary>Show Answer</summary>
**Correct Answer: C**

Explanation: Cross-validation reduces variance in performance estimates by testing on multiple splits of the data.
</details>

---

### 8. What is the primary difference between BLEU and ROUGE?

A) BLEU is for classification, ROUGE is for regression  
B) BLEU is precision-focused, ROUGE is recall-focused  
C) BLEU only works in English  
D) ROUGE is more accurate

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: BLEU emphasizes precision (generated text vs reference), while ROUGE emphasizes recall (reference vs generated text).
</details>

---

### 9. What does a low perplexity score indicate?

A) Model is confused  
B) Model is confident/text is familiar  
C) Model needs more training  
D) Text is too complex

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: Low perplexity means the model assigns high probability to the actual tokens, indicating confidence and familiarity with the text.
</details>

---

### 10. What is the "80% rule" in fairness testing?

A) Model must be 80% accurate  
B) The ratio of positive outcomes between groups should be ≥ 0.8  
C) 80% of features must be fair  
D) Training data must be 80% balanced

<details>
<summary>Show Answer</summary>
**Correct Answer: B**

Explanation: The 80% rule (or 4/5ths rule) states that the selection rate for any protected group should be at least 80% of the rate for the highest group.
</details>

---

## Scoring Guide

- **9-10 correct:** Excellent! You have strong foundational knowledge
- **7-8 correct:** Good! Review a few concepts before starting
- **5-6 correct:** Moderate. Pay extra attention during Phase 15
- **0-4 correct:** Review prerequisite materials before Phase 15

---

## Key Topics to Review

If you scored low, review these topics:
- Classification metrics (precision, recall, F1, accuracy)
- Regression metrics (MAE, RMSE, R²)
- Fairness concepts (demographic parity, equalized odds)
- LLM evaluation (BLEU, ROUGE, perplexity)
- Cross-validation basics

---

**Ready to start Phase 15? Let's go! 🚀**
