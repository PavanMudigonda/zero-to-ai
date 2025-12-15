# Post-Quiz: Debugging & Troubleshooting

Test your knowledge after completing Phase 16!

**Time:** 15 minutes  
**Questions:** 18  
**Passing Score:** 70%

---

## Questions

### 1. In the 5-step debugging workflow, what comes after "Reproduce"?

A) Test  
B) Gather  
C) Hypothesize  
D) Verify

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** The workflow is: 1) Reproduce, 2) Gather data/logs/metrics, 3) Hypothesize cause, 4) Test hypothesis, 5) Verify fix. After reproducing the bug, you gather diagnostic information.

</details>

---

### 2. What's the best way to detect if features and labels are misaligned?

A) Check the shapes  
B) Train a simple baseline model  
C) Look at the data visually  
D) All of the above

<details>
<summary>Show Answer</summary>

**Correct Answer: D**

**Explanation:** Multiple approaches help: check shapes for dimension mismatch, train a simple baseline (random performance indicates misalignment), and visually inspect data. Using all methods provides confidence.

</details>

---

### 3. A model with train_acc=0.99, test_acc=0.60 shows signs of:

A) Underfitting  
B) Overfitting  
C) Good generalization  
D) Data leakage

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** Large gap (0.99 vs 0.60) indicates overfitting - the model memorized training data but fails to generalize. Solutions: regularization, more data, reduce complexity, or early stopping.

</details>

---

### 4. Which outlier detection method is most sensitive to extreme values?

A) Z-score  
B) IQR (Interquartile Range)  
C) Isolation Forest  
D) They're all equally sensitive

<details>
<summary>Show Answer</summary>

**Correct Answer: A**

**Explanation:** Z-score uses mean and standard deviation, both of which are heavily influenced by outliers. IQR uses quartiles (robust to outliers), and Isolation Forest is based on tree isolation depth.

</details>

---

### 5. What's the primary advantage of using StandardScaler.fit_transform() on training data?

A) It's faster  
B) It prevents data leakage  
C) It improves accuracy  
D) It handles missing values

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** fit_transform() on training data computes statistics (mean, std) from training only, preventing test data from influencing the transformation. Test data should only use transform() with training statistics.

</details>

---

### 6. In profiling, what does "cumulative time" represent?

A) Time spent in the function only  
B) Time spent in the function and all its callees  
C) Time since program start  
D) Total program runtime

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** Cumulative time includes the time spent in the function itself plus all functions it calls. This helps identify high-level bottlenecks. "tottime" shows only time in the function itself.

</details>

---

### 7. To achieve a 10x speedup, which optimization should you try first?

A) Vectorize Python loops  
B) Use multiprocessing  
C) Upgrade hardware  
D) Rewrite in C++

<details>
<summary>Show Answer</summary>

**Correct Answer: A**

**Explanation:** Vectorization with NumPy often provides 10-100x speedup with minimal code changes. It should be the first optimization. Multiprocessing, hardware, and C++ are more complex and should be later considerations.

</details>

---

### 8. When plotting learning curves, convergence is indicated by:

A) Training and validation curves diverging  
B) Training curve at 100%  
C) Both curves plateauing at similar values  
D) Validation curve above training curve

<details>
<summary>Show Answer</summary>

**Correct Answer: C**

**Explanation:** Convergence means both training and validation performance have stabilized and are close together. This indicates the model has learned as much as it can from the current data and architecture.

</details>

---

### 9. L2 (Ridge) regularization is preferred over L1 (Lasso) when you want to:

A) Perform feature selection  
B) Keep all features with reduced weights  
C) Make predictions faster  
D) Handle missing values

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** L2 shrinks weights toward zero but rarely exactly to zero, keeping all features. L1 can drive weights to exactly zero, effectively performing feature selection. Use L2 when you want to keep all features.

</details>

---

### 10. A model fails to converge. What should you check FIRST?

A) Learning rate  
B) Number of iterations  
C) Feature scaling  
D) Model architecture

<details>
<summary>Show Answer</summary>

**Correct Answer: C**

**Explanation:** Unscaled features are the most common cause of convergence failures. Always scale first. Then adjust learning rate, iterations, and architecture if needed.

</details>

---

### 11. What does a high off-diagonal value in a normalized confusion matrix indicate?

A) Good performance  
B) Systematic confusion between two classes  
C) Random errors  
D) Data leakage

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** High off-diagonal values show the model frequently confuses two specific classes. This suggests they may look similar or share features. It guides where to focus improvement efforts.

</details>

---

### 12. Per-class F1 scores range from 0.2 to 0.95. What's the BEST next step?

A) Celebrate the 0.95!  
B) Focus on improving the 0.2 class  
C) Average them and report overall performance  
D) Drop the 0.2 class

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** Large class-to-class variance indicates some classes need attention. The 0.2 class likely has few samples, poor features, or label noise. Investigate and improve it first.

</details>

---

### 13. High-confidence incorrect predictions are concerning because:

A) They're rare  
B) The model doesn't know it's wrong  
C) They're always false positives  
D) They indicate data leakage

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** When a model is highly confident but wrong, it suggests overconfidence or miscalibration. In production, these errors are dangerous because the system can't flag them as uncertain.

</details>

---

### 14. What does the Kolmogorov-Smirnov (K-S) test detect?

A) Missing values  
B) Outliers  
C) Distribution differences  
D) Correlation

<details>
<summary>Show Answer</summary>

**Correct Answer: C**

**Explanation:** The K-S test compares two distributions and tests if they're significantly different. It's commonly used to detect distribution shift between training and test/production data.

</details>

---

### 15. Batch processing predictions is faster than one-by-one because:

A) It uses less memory  
B) It reduces function call overhead  
C) It enables vectorization  
D) Both B and C

<details>
<summary>Show Answer</summary>

**Correct Answer: D**

**Explanation:** Batch processing reduces the overhead of function calls AND enables vectorized operations. This combination can provide significant speedups (10-100x) compared to iterating through samples.

</details>

---

### 16. A validation curve shows optimal performance at max_depth=5. What does this tell you?

A) Always use max_depth=5  
B) This is the best complexity for this dataset  
C) Deeper trees will overfit  
D) Both B and C

<details>
<summary>Show Answer</summary>

**Correct Answer: D**

**Explanation:** The validation curve identifies the best complexity for the current dataset - in this case max_depth=5. Going deeper would likely overfit (validation score would decrease). However, this is dataset-specific.

</details>

---

### 17. When debugging, why is it important to set random seeds?

A) To make code run faster  
B) To ensure reproducibility  
C) To improve accuracy  
D) To prevent overfitting

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** Setting random seeds ensures experiments are reproducible. You can verify that a fix actually works rather than just getting lucky with a different random initialization. Critical for reliable debugging.

</details>

---

### 18. What's the most systematic way to prioritize model improvements?

A) Fix whatever seems easiest  
B) Always collect more data first  
C) Analyze errors, quantify impact, prioritize by ROI  
D) Try every technique and see what works

<details>
<summary>Show Answer</summary>

**Correct Answer: C**

**Explanation:** Systematic prioritization involves: 1) Analyze errors to identify issues, 2) Estimate potential impact of each fix, 3) Consider implementation cost, 4) Prioritize by return on investment (ROI).

</details>

---

## Bonus Questions

### 19. (Bonus) In-place operations (+=, *=) are preferred because they:

A) Are faster to type  
B) Use less memory  
C) Are more readable  
D) Work with more data types

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** In-place operations modify arrays without creating copies, saving memory. For large arrays, this can be significant. Compare `a = a + b` (creates new array) vs `a += b` (modifies in-place).

</details>

---

### 20. (Bonus) A calibration curve far from the diagonal indicates:

A) Perfect calibration  
B) Model is well-tuned  
C) Model confidence doesn't match actual performance  
D) Data leakage

<details>
<summary>Show Answer</summary>

**Correct Answer: C**

**Explanation:** A calibration curve plots predicted probability vs actual accuracy. If it deviates from the diagonal (y=x), the model's confidence estimates are miscalibrated. For example, when it predicts 80% confidence, actual accuracy might be 60%.

</details>

---

## Scoring Guide

Count your correct answers (out of 18 main questions):

- **16-18 correct:** Excellent! Master level understanding 🎓
- **13-15 correct:** Great! You've learned the material well ✅
- **10-12 correct:** Good! Review a few concepts 📚
- **7-9 correct:** Pass, but review topics you missed ⚠️
- **0-6 correct:** Review Phase 16 materials 🔄

---

## Knowledge Gaps to Address

Based on incorrect answers, review:

**Debugging Workflow (Q1-5):**
- 5-step debugging process
- Data quality checks
- Baseline models
- Overfitting vs underfitting

**Performance (Q6-10):**
- Profiling techniques
- Vectorization
- Regularization
- Convergence issues

**Error Analysis (Q11-16):**
- Confusion matrices
- Per-class metrics
- Confidence calibration
- Distribution shift

**Best Practices (Q17-20):**
- Reproducibility
- Systematic improvement
- Memory optimization
- Model calibration

---

## Next Steps

**If you scored well (13+):**
- ✅ Move to Phase 17 or tackle advanced challenges
- ✅ Complete the comprehensive assignment
- ✅ Try Challenge 6 or 7 for expert-level practice

**If you need review (< 13):**
- 📚 Re-read relevant notebook sections
- 🔄 Redo coding exercises
- 💬 Discuss difficult concepts
- ✍️ Retake quiz after review

---

## Detailed Review Topics

### Must-Know Concepts:

1. **Debugging Workflow**
   - Reproduce → Gather → Hypothesize → Test → Verify
   - Sanity checks and baselines
   - Systematic vs random debugging

2. **Data Quality**
   - Missing value strategies
   - Outlier detection methods
   - Duplicate handling
   - Distribution shift detection

3. **Performance Optimization**
   - Profiling (cProfile, memory_profiler)
   - Vectorization techniques
   - Batch processing
   - Caching and parallelization

4. **Model Debugging**
   - Learning curves interpretation
   - Overfitting vs underfitting
   - Regularization (L1 vs L2)
   - Convergence troubleshooting

5. **Error Analysis**
   - Confusion matrix analysis
   - Per-class metrics
   - Failure case categorization
   - Confidence calibration

---

**Congratulations on completing Phase 16! You're now equipped with essential debugging skills! 🎉**
