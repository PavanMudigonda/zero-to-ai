# Statistics & Probability for AI/ML

> **Essential statistical concepts every AI practitioner must know**

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Probability Fundamentals](#probability-fundamentals)
3. [Descriptive Statistics](#descriptive-statistics)
4. [Probability Distributions](#probability-distributions)
5. [Statistical Inference](#statistical-inference)
6. [Hypothesis Testing](#hypothesis-testing)
7. [Correlation & Causation](#correlation--causation)
8. [Practical Applications in ML](#practical-applications-in-ml)

---

## Introduction

Statistics is the foundation of machine learning. Understanding probability, distributions, and statistical inference is crucial for:

- **Model Evaluation:** Understanding accuracy, precision, recall
- **A/B Testing:** Comparing model versions
- **Feature Selection:** Identifying important variables
- **Uncertainty Quantification:** Knowing model confidence
- **Hyperparameter Tuning:** Making informed choices

This notebook covers the essential statistics you need for AI/ML work, with practical examples using real datasets.

---

## Probability Fundamentals

### What is Probability?

**Probability** is a number between 0 and 1 that expresses how likely an **event** is to occur.

$$P(E) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}}$$

### Example: Rolling a Die

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

# Simulate rolling a fair die 1000 times
np.random.seed(42)
die_rolls = np.random.randint(1, 7, size=1000)

# Calculate probabilities
unique, counts = np.unique(die_rolls, return_counts=True)
probabilities = counts / len(die_rolls)

# Visualize
plt.figure(figsize=(10, 5))
plt.bar(unique, probabilities, alpha=0.7, color='steelblue', edgecolor='black')
plt.axhline(y=1/6, color='red', linestyle='--', label='Theoretical (1/6)')
plt.xlabel('Die Face', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title('Empirical Probability Distribution of Die Rolls', fontsize=14)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()

print("Observed probabilities:")
for face, prob in zip(unique, probabilities):
    print(f"Face {face}: {prob:.3f} (expected: {1/6:.3f})")
```

✅ **Knowledge Check:**
1. What's the probability of rolling an even number on a fair die?
2. If you roll two dice, what's the probability of getting a sum of 7?
3. Why do empirical probabilities differ from theoretical ones?

<details>
<summary>Click for answers</summary>

1. **Answer:** 3/6 = 0.5 (faces 2, 4, 6 are even)
2. **Answer:** 6/36 = 1/6 (combinations: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1)
3. **Answer:** Random sampling variation. With infinite rolls, empirical → theoretical
</details>

---

### Random Variables

**Random Variable:** A variable whose value is determined by a random process.

- **Discrete:** Countable values (e.g., number of heads in coin flips)
- **Continuous:** Any value in a range (e.g., height, weight, time)

### Sample Space

The **sample space** is the set of all possible outcomes.

```python
# Example: Flipping 3 coins
from itertools import product

outcomes = list(product(['H', 'T'], repeat=3))
print(f"Sample space (n={len(outcomes)}):")
for outcome in outcomes:
    print(''.join(outcome))

# Random variable: Number of heads
num_heads = [sum([1 for flip in outcome if flip == 'H']) for outcome in outcomes]
print(f"\nNumber of heads: {set(num_heads)}")

# Probability distribution
unique_heads, counts = np.unique(num_heads, return_counts=True)
prob_dist = counts / len(outcomes)

plt.figure(figsize=(8, 5))
plt.bar(unique_heads, prob_dist, alpha=0.7, color='coral', edgecolor='black')
plt.xlabel('Number of Heads', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title('Probability Distribution: Number of Heads in 3 Coin Flips', fontsize=14)
plt.xticks(unique_heads)
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\nProbability distribution:")
for heads, prob in zip(unique_heads, prob_dist):
    print(f"P(X = {heads}) = {prob:.3f} = {counts[heads]}/8")
```

---

## Descriptive Statistics

### Measures of Central Tendency

Let's analyze a real dataset: MLB baseball player weights and heights.

```python
# Load baseball player data
# (Using simulated data - in practice, load from data/mlb_height_weight.csv)
np.random.seed(42)
n_players = 1034  # Real dataset size

# Generate realistic player data (based on actual MLB statistics)
heights = np.random.normal(loc=73.7, scale=2.3, size=n_players)  # inches
weights = np.random.normal(loc=201.7, scale=21.0, size=n_players)  # pounds

mlb_data = pd.DataFrame({
    'height': heights,
    'weight': weights,
    'position': np.random.choice(['1B', '2B', 'SS', '3B', 'C', 'OF', 'P'], n_players)
})

# First 20 weights (like in the reference)
sample_weights = weights[:20]
print("First 20 player weights (lbs):")
print(sample_weights)
print(f"\nMean: {np.mean(sample_weights):.2f}")
print(f"Median: {np.median(sample_weights):.2f}")
```

### Mean, Median, Mode

```python
# Calculate statistics
mean_weight = mlb_data['weight'].mean()
median_weight = mlb_data['weight'].median()
mode_weight = mlb_data['weight'].mode()[0] if len(mlb_data['weight'].mode()) > 0 else None

std_weight = mlb_data['weight'].std()
var_weight = mlb_data['weight'].var()

print(f"Weight Statistics:")
print(f"  Mean: {mean_weight:.2f} lbs")
print(f"  Median: {median_weight:.2f} lbs")
print(f"  Std Dev: {std_weight:.2f} lbs")
print(f"  Variance: {var_weight:.2f}")
print(f"\nHeight Statistics:")
print(f"  Mean: {mlb_data['height'].mean():.2f} inches ({mlb_data['height'].mean()/12:.2f} feet)")
print(f"  Median: {mlb_data['height'].median():.2f} inches")
print(f"  Std Dev: {mlb_data['height'].std():.2f} inches")

# Visualize distributions
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Weight distribution
axes[0].hist(mlb_data['weight'], bins=30, alpha=0.7, color='steelblue', edgecolor='black')
axes[0].axvline(mean_weight, color='red', linestyle='--', label=f'Mean: {mean_weight:.1f}')
axes[0].axvline(median_weight, color='green', linestyle='--', label=f'Median: {median_weight:.1f}')
axes[0].set_xlabel('Weight (lbs)', fontsize=12)
axes[0].set_ylabel('Frequency', fontsize=12)
axes[0].set_title('Distribution of Player Weights', fontsize=14)
axes[0].legend()
axes[0].grid(axis='y', alpha=0.3)

# Height distribution
axes[1].hist(mlb_data['height'], bins=30, alpha=0.7, color='coral', edgecolor='black')
axes[1].axvline(mlb_data['height'].mean(), color='red', linestyle='--', label=f'Mean: {mlb_data["height"].mean():.1f}"')
axes[1].axvline(mlb_data['height'].median(), color='green', linestyle='--', label=f'Median: {mlb_data["height"].median():.1f}"')
axes[1].set_xlabel('Height (inches)', fontsize=12)
axes[1].set_ylabel('Frequency', fontsize=12)
axes[1].set_title('Distribution of Player Heights', fontsize=14)
axes[1].legend()
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

✅ **Knowledge Check:**
1. When is the median more useful than the mean?
2. What does a large standard deviation tell you?
3. Why might mode not be useful for continuous data?

<details>
<summary>Click for answers</summary>

1. **Answer:** When there are outliers or skewed distributions. Median is robust to extreme values.
2. **Answer:** Data is spread out widely from the mean. High variability.
3. **Answer:** Continuous data rarely has exact repeats. Better for categorical data.
</details>

---

## Probability Distributions

### Normal (Gaussian) Distribution

The most important distribution in statistics!

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$$

```python
# Fit normal distribution to height data
mu, sigma = mlb_data['height'].mean(), mlb_data['height'].std()

# Generate theoretical distribution
x = np.linspace(mlb_data['height'].min(), mlb_data['height'].max(), 100)
theoretical_dist = stats.norm.pdf(x, mu, sigma)

plt.figure(figsize=(12, 6))
plt.hist(mlb_data['height'], bins=30, density=True, alpha=0.6, 
         color='steelblue', edgecolor='black', label='Observed')
plt.plot(x, theoretical_dist, 'r-', linewidth=2, label=f'Normal(μ={mu:.1f}, σ={sigma:.1f})')
plt.xlabel('Height (inches)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Player Heights vs Normal Distribution', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# 68-95-99.7 Rule
print("68-95-99.7 Rule (Empirical Rule):")
print(f"  68% of data within 1σ: [{mu-sigma:.1f}, {mu+sigma:.1f}]")
print(f"  95% of data within 2σ: [{mu-2*sigma:.1f}, {mu+2*sigma:.1f}]")
print(f"  99.7% of data within 3σ: [{mu-3*sigma:.1f}, {mu+3*sigma:.1f}]")

# Verify
within_1sigma = ((mlb_data['height'] >= mu-sigma) & (mlb_data['height'] <= mu+sigma)).mean()
within_2sigma = ((mlb_data['height'] >= mu-2*sigma) & (mlb_data['height'] <= mu+2*sigma)).mean()
within_3sigma = ((mlb_data['height'] >= mu-3*sigma) & (mlb_data['height'] <= mu+3*sigma)).mean()

print(f"\nActual data:")
print(f"  Within 1σ: {within_1sigma:.1%} (expected: 68%)")
print(f"  Within 2σ: {within_2sigma:.1%} (expected: 95%)")
print(f"  Within 3σ: {within_3sigma:.1%} (expected: 99.7%)")
```

### Other Important Distributions

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Binomial Distribution
n, p = 10, 0.5
x_binom = np.arange(0, n+1)
pmf_binom = stats.binom.pmf(x_binom, n, p)
axes[0, 0].bar(x_binom, pmf_binom, alpha=0.7, color='steelblue', edgecolor='black')
axes[0, 0].set_title(f'Binomial Distribution (n={n}, p={p})', fontsize=12)
axes[0, 0].set_xlabel('Number of successes')
axes[0, 0].set_ylabel('Probability')
axes[0, 0].grid(axis='y', alpha=0.3)

# 2. Poisson Distribution
lambda_param = 3
x_poisson = np.arange(0, 15)
pmf_poisson = stats.poisson.pmf(x_poisson, lambda_param)
axes[0, 1].bar(x_poisson, pmf_poisson, alpha=0.7, color='coral', edgecolor='black')
axes[0, 1].set_title(f'Poisson Distribution (λ={lambda_param})', fontsize=12)
axes[0, 1].set_xlabel('Number of events')
axes[0, 1].set_ylabel('Probability')
axes[0, 1].grid(axis='y', alpha=0.3)

# 3. Exponential Distribution
lambda_exp = 1.5
x_exp = np.linspace(0, 5, 100)
pdf_exp = stats.expon.pdf(x_exp, scale=1/lambda_exp)
axes[1, 0].plot(x_exp, pdf_exp, linewidth=2, color='green')
axes[1, 0].fill_between(x_exp, pdf_exp, alpha=0.3, color='green')
axes[1, 0].set_title(f'Exponential Distribution (λ={lambda_exp})', fontsize=12)
axes[1, 0].set_xlabel('Time between events')
axes[1, 0].set_ylabel('Density')
axes[1, 0].grid(alpha=0.3)

# 4. Uniform Distribution
a, b = 0, 10
x_uniform = np.linspace(a-1, b+1, 100)
pdf_uniform = stats.uniform.pdf(x_uniform, a, b-a)
axes[1, 1].plot(x_uniform, pdf_uniform, linewidth=2, color='purple')
axes[1, 1].fill_between(x_uniform, pdf_uniform, alpha=0.3, color='purple')
axes[1, 1].set_title(f'Uniform Distribution U({a}, {b})', fontsize=12)
axes[1, 1].set_xlabel('Value')
axes[1, 1].set_ylabel('Density')
axes[1, 1].grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Statistical Inference

### Confidence Intervals

A **confidence interval** gives a range where we expect the true population parameter to lie.

```python
# Calculate 95% confidence interval for player heights
confidence = 0.95
sample_mean = mlb_data['height'].mean()
sample_std = mlb_data['height'].std()
sample_size = len(mlb_data)

# Standard error
se = sample_std / np.sqrt(sample_size)

# Confidence interval using t-distribution
ci = stats.t.interval(confidence, 
                       df=sample_size-1,
                       loc=sample_mean,
                       scale=se)

print(f"95% Confidence Interval for Player Height:")
print(f"  Point estimate (mean): {sample_mean:.2f} inches")
print(f"  Standard error: {se:.4f}")
print(f"  Confidence interval: [{ci[0]:.2f}, {ci[1]:.2f}] inches")
print(f"\nInterpretation: We are 95% confident that the true average height")
print(f"of all MLB players is between {ci[0]:.2f} and {ci[1]:.2f} inches.")

# Visualize
plt.figure(figsize=(10, 6))
x = np.linspace(sample_mean - 4*se, sample_mean + 4*se, 1000)
y = stats.t.pdf(x, df=sample_size-1, loc=sample_mean, scale=se)
plt.plot(x, y, linewidth=2, color='steelblue', label='Sampling Distribution')
plt.axvline(sample_mean, color='red', linestyle='--', linewidth=2, label='Sample Mean')
plt.axvline(ci[0], color='green', linestyle='--', label='95% CI Bounds')
plt.axvline(ci[1], color='green', linestyle='--')
plt.fill_between(x, 0, y, where=(x >= ci[0]) & (x <= ci[1]), alpha=0.3, color='green')
plt.xlabel('Height (inches)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Sampling Distribution of Mean Height with 95% CI', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

---

## Hypothesis Testing

### Comparing Two Groups

**Question:** Are first basemen (1B) significantly taller than second basemen (2B)?

```python
# Extract heights for each position
heights_1b = mlb_data[mlb_data['position'] == '1B']['height']
heights_2b = mlb_data[mlb_data['position'] == '2B']['height']

print(f"First Basemen (1B): n={len(heights_1b)}, mean={heights_1b.mean():.2f}")
print(f"Second Basemen (2B): n={len(heights_2b)}, mean={heights_2b.mean():.2f}")
print(f"Difference in means: {heights_1b.mean() - heights_2b.mean():.2f} inches")

# Hypothesis Test
# H0 (null): μ_1B = μ_2B (no difference)
# H1 (alternative): μ_1B ≠ μ_2B (there is a difference)

t_stat, p_value = stats.ttest_ind(heights_1b, heights_2b)

print(f"\nTwo-Sample t-test:")
print(f"  t-statistic: {t_stat:.4f}")
print(f"  p-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"\n✅ Result: REJECT null hypothesis (p < {alpha})")
    print(f"   First basemen are significantly taller than second basemen.")
else:
    print(f"\n❌ Result: FAIL TO REJECT null hypothesis (p >= {alpha})")
    print(f"   No significant difference in heights.")

# Visualize
plt.figure(figsize=(12, 6))
plt.hist(heights_1b, bins=20, alpha=0.5, label=f'1B (n={len(heights_1b)})', 
         color='steelblue', edgecolor='black')
plt.hist(heights_2b, bins=20, alpha=0.5, label=f'2B (n={len(heights_2b)})', 
         color='coral', edgecolor='black')
plt.axvline(heights_1b.mean(), color='blue', linestyle='--', linewidth=2)
plt.axvline(heights_2b.mean(), color='red', linestyle='--', linewidth=2)
plt.xlabel('Height (inches)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title(f'Height Distribution: 1B vs 2B (p={p_value:.4f})', fontsize=14)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()
```

✅ **Knowledge Check:**
1. What does a p-value tell you?
2. What's the difference between statistical and practical significance?
3. Why do we use α = 0.05?

---

## Correlation & Causation

### Measuring Correlation

```python
# Calculate correlation between height and weight
correlation = mlb_data['height'].corr(mlb_data['weight'])
print(f"Pearson correlation (height, weight): {correlation:.4f}")

# Visualize
plt.figure(figsize=(10, 6))
plt.scatter(mlb_data['height'], mlb_data['weight'], alpha=0.5, s=20, color='steelblue')
plt.xlabel('Height (inches)', fontsize=12)
plt.ylabel('Weight (lbs)', fontsize=12)
plt.title(f'Height vs Weight (r = {correlation:.3f})', fontsize=14)
plt.grid(alpha=0.3)

# Add regression line
from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err = linregress(mlb_data['height'], mlb_data['weight'])
line_x = np.array([mlb_data['height'].min(), mlb_data['height'].max()])
line_y = slope * line_x + intercept
plt.plot(line_x, line_y, 'r-', linewidth=2, label=f'y = {slope:.2f}x + {intercept:.2f}')
plt.legend()
plt.show()

print(f"\nRegression Results:")
print(f"  Slope: {slope:.2f} lbs/inch")
print(f"  R²: {r_value**2:.4f}")
print(f"  Interpretation: For every 1 inch increase in height,")
print(f"  weight increases by {slope:.2f} lbs on average.")
```

### ⚠️ Correlation ≠ Causation!

```python
print("Remember:")
print("✅ Correlation measures LINEAR relationship strength")
print("✅ Range: -1 (perfect negative) to +1 (perfect positive)")
print("❌ Correlation does NOT imply causation!")
print("❌ Confounding variables may be the true cause")
print("❌ Correlation can be spurious (random)")
```

---

## Practical Applications in ML

### 1. Model Evaluation with Confidence Intervals

```python
# Simulate model accuracy over multiple runs
np.random.seed(42)
n_runs = 30
accuracies = np.random.normal(loc=0.85, scale=0.03, size=n_runs)

mean_acc = accuracies.mean()
ci_acc = stats.t.interval(0.95, len(accuracies)-1,
                          loc=mean_acc,
                          scale=stats.sem(accuracies))

print(f"Model Performance (30 runs):")
print(f"  Mean accuracy: {mean_acc:.4f}")
print(f"  95% CI: [{ci_acc[0]:.4f}, {ci_acc[1]:.4f}]")
print(f"  Std Dev: {accuracies.std():.4f}")
```

### 2. A/B Testing Models

```python
# Compare two model versions
model_a_acc = np.random.normal(0.84, 0.03, 25)
model_b_acc = np.random.normal(0.87, 0.03, 25)

t_stat, p_val = stats.ttest_ind(model_a_acc, model_b_acc)

print(f"\nA/B Test: Model A vs Model B")
print(f"  Model A: {model_a_acc.mean():.4f} ± {model_a_acc.std():.4f}")
print(f"  Model B: {model_b_acc.mean():.4f} ± {model_b_acc.std():.4f}")
print(f"  p-value: {p_val:.4f}")

if p_val < 0.05:
    print(f"  ✅ Model B is significantly better!")
else:
    print(f"  ❌ No significant difference")
```

---

## 🎯 Summary

### Key Takeaways

1. **Probability:** Foundation for understanding uncertainty
2. **Distributions:** Normal distribution is everywhere in ML
3. **Statistics:** Mean, median, std describe data
4. **Inference:** Confidence intervals quantify uncertainty
5. **Hypothesis Testing:** Compare models/features rigorously
6. **Correlation:** Measures relationships, NOT causation
7. **Applications:** Essential for model evaluation, A/B testing

### Next Steps

- ✅ Practice with real datasets
- ✅ Apply hypothesis testing to your ML experiments
- ✅ Use confidence intervals in model evaluation
- ✅ Be cautious with correlation claims
- ✅ Always visualize your data!

---

## 📚 Resources

- [Statistics for Machine Learning (MIT)](https://ocw.mit.edu/)
- [Think Stats (Book)](https://greenteapress.com/thinkstats/)
- [Seeing Theory (Interactive)](https://seeing-theory.brown.edu/)
- [StatQuest (YouTube)](https://www.youtube.com/c/joshstarmer)

---

**Remember:** Statistics is a tool for making informed decisions under uncertainty - crucial for AI/ML! 📊
