# Pre-Quiz: Debugging & Troubleshooting

Test your baseline knowledge before starting Phase 16.

**Time:** 10 minutes  
**Questions:** 10  
**Passing Score:** 60%

---

## Instructions

Answer each question and check your responses. This helps identify areas to focus on.

---

## Questions

### 1. What is the first step in debugging an ML model that's not learning?

A) Increase model complexity  
B) Reproduce the bug consistently  
C) Add more data  
D) Try a different algorithm

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** The first step in any debugging workflow is to reproduce the bug consistently. You can't fix what you can't reliably observe. Once you can reproduce the issue, you can then gather data, hypothesize causes, and test fixes.

</details>

---

### 2. Which of the following is a sign of data leakage?

A) Test accuracy much lower than training accuracy  
B) Test accuracy suspiciously close to or higher than training accuracy  
C) Model takes long to train  
D) Missing values in the dataset

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** Data leakage occurs when information from the test set influences training. This typically results in unrealistically high test accuracy that won't generalize. If test accuracy is very close to or exceeds training accuracy, suspect leakage.

</details>

---

### 3. What does a large gap between training and validation accuracy indicate?

A) Underfitting  
B) Overfitting  
C) Good generalization  
D) Data leakage

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** A large gap (training accuracy much higher than validation) indicates overfitting - the model has memorized the training data but doesn't generalize well. Solutions include regularization, more data, or reducing model complexity.

</details>

---

### 4. Which tool would you use for CPU profiling in Python?

A) memory_profiler  
B) cProfile  
C) pdb  
D) pytest

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** cProfile is Python's built-in CPU profiler that shows where your code spends time. memory_profiler is for memory, pdb is for interactive debugging, and pytest is for testing.

</details>

---

### 5. What's the primary benefit of vectorization in ML code?

A) Easier to read  
B) Uses less memory  
C) Much faster execution  
D) Better accuracy

<details>
<summary>Show Answer</summary>

**Correct Answer: C**

**Explanation:** Vectorization replaces Python loops with optimized NumPy operations, resulting in significantly faster execution (often 10-100x speedup). It leverages low-level optimizations and can use SIMD instructions.

</details>

---

### 6. Why is it important to scale features before training?

A) To make the model train faster  
B) To ensure features are on similar scales for convergence  
C) To reduce overfitting  
D) To handle missing values

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** Unscaled features with different ranges can cause convergence issues, especially for gradient-based algorithms. Features on different scales can make some weights update much faster than others, preventing proper convergence.

</details>

---

### 7. What does the diagonal of a confusion matrix represent?

A) False positives  
B) False negatives  
C) Correct predictions  
D) Total predictions

<details>
<summary>Show Answer</summary>

**Correct Answer: C**

**Explanation:** The diagonal elements of a confusion matrix represent correct predictions (true positives and true negatives). Off-diagonal elements represent errors (false positives and false negatives).

</details>

---

### 8. If your model has precision=0.95 and recall=0.40, what should you do?

A) Model is perfect, do nothing  
B) Focus on reducing false negatives  
C) Focus on reducing false positives  
D) Collect more data

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** Low recall (0.40) means the model misses many positive cases (high false negatives). High precision (0.95) means when it predicts positive, it's usually right. To improve recall, you might lower the decision threshold or address class imbalance.

</details>

---

### 9. What's the best way to handle missing values that are >50% of a column?

A) Fill with mean  
B) Fill with median  
C) Consider dropping the column  
D) Fill with mode

<details>
<summary>Show Answer</summary>

**Correct Answer: C**

**Explanation:** When more than 50% of values are missing, the column provides little information and imputation would be mostly guessing. It's often better to drop such columns unless the missingness itself is meaningful.

</details>

---

### 10. What does a learning curve that shows both training and validation scores are low indicate?

A) Overfitting  
B) Underfitting  
C) Perfect fit  
D) Data leakage

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:** When both training and validation scores are low and not improving with more data, it indicates underfitting (high bias). The model is too simple to capture the patterns. Solutions: increase model complexity or add more features.

</details>

---

## Scoring Guide

Count your correct answers:

- **9-10 correct:** Excellent! You have a strong foundation 🎓
- **7-8 correct:** Good! Review a few concepts before starting 👍
- **5-6 correct:** Moderate. Focus on weak areas during Phase 16 📚
- **0-4 correct:** Review prerequisite material before Phase 16 🔄

---

## Key Topics to Review

Based on your score, focus on:

**If you missed 1-3:**
- General debugging workflow
- Common ML pitfalls

**If you missed 4-5:**
- Data quality issues
- Model evaluation metrics
- Performance optimization basics

**If you missed 6-8:**
- Review Phase 15 (Model Evaluation)
- Study debugging fundamentals
- Practice with simple examples

**If you missed 9-10:**
- Complete prerequisite phases first
- Review Python and ML basics
- Start with simpler debugging exercises

---

## Next Steps

1. Review any questions you got wrong
2. Check the explanations carefully
3. Read relevant notebook sections
4. **Begin Phase 16 when ready!**

---

Good luck with Phase 16! 🚀
