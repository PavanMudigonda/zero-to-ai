# Phase 5: Neural Networks - Post-Quiz

**Time:** 15 minutes  
**Questions:** 10  
**Passing Score:** 70%  
**Purpose:** Validate your learning after completing Phase 5

---

## Question 1 (Medium)

What is the output of the sigmoid activation function when input = 0?

A) 0.0  
B) 0.5 ✓  
C) 1.0  
D) Undefined  

<details>
<summary>Explanation</summary>

**Answer: B) 0.5**

**Sigmoid function:** σ(x) = 1 / (1 + e^(-x))

When x = 0:
```
σ(0) = 1 / (1 + e^0)
     = 1 / (1 + 1)
     = 1 / 2
     = 0.5
```

This is the midpoint of the sigmoid curve, which ranges from 0 to 1.

**Reference:** Phase 6 - Activation Functions

</details>

---

## Question 2 (Hard)

```python
def forward_pass(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = relu(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)
    return A2
```

In this 2-layer network, what does `Z1` represent?

A) Activated output of first layer  
B) Pre-activation output of first layer ✓  
C) Input to the network  
D) Final output  

<details>
<summary>Explanation</summary>

**Answer: B) Pre-activation output of first layer**

**Notation:**
- **Z = Pre-activation** (weighted sum + bias, before activation function)
- **A = Activation** (after applying activation function)

So the sequence is:
1. `Z1 = XW1 + b1` ← Pre-activation
2. `A1 = ReLU(Z1)` ← Activation
3. `Z2 = A1W2 + b2` ← Pre-activation
4. `A2 = Sigmoid(Z2)` ← Final output

**Reference:** Phase 5 - Forward Propagation

</details>

---

## Question 3 (Medium)

Why is the ReLU activation function preferred over sigmoid in hidden layers?

A) It's easier to compute  
B) It mitigates the vanishing gradient problem ✓  
C) It always outputs positive values  
D) It's more accurate  

<details>
<summary>Explanation</summary>

**Answer: B) It mitigates the vanishing gradient problem**

**ReLU advantages:**
- Gradient is either 0 or 1 (doesn't shrink like sigmoid)
- Faster training (no exponential computation)
- Prevents vanishing gradients in deep networks

**ReLU:** f(x) = max(0, x)  
**Gradient:** f'(x) = 1 if x > 0, else 0

**Sigmoid problems:**
- Gradient saturates (very small) for large |x|
- Causes vanishing gradients in deep networks

**Reference:** Phase 6 - Activation Functions

</details>

---

## Question 4 (Hard)

What is the derivative of the ReLU function at x = 0?

A) 0  
B) 1  
C) 0.5  
D) Technically undefined, but set to 0 in practice ✓  

<details>
<summary>Explanation</summary>

**Answer: D) Technically undefined, but set to 0 in practice**

**ReLU:** f(x) = max(0, x)

**Derivative:**
- f'(x) = 1 if x > 0
- f'(x) = 0 if x < 0
- f'(x) = undefined at x = 0 (discontinuity)

**In practice:** We set f'(0) = 0 (or sometimes 0.5), which works well in gradient descent.

**Reference:** Phase 6 - Activation Function Derivatives

</details>

---

## Question 5 (Medium)

In gradient descent, weights are updated using:

A) `W = W + learning_rate * gradient`  
B) `W = W - learning_rate * gradient` ✓  
C) `W = W * learning_rate * gradient`  
D) `W = W / learning_rate * gradient`  

<details>
<summary>Explanation</summary>

**Answer: B) W = W - learning_rate * gradient**

**Gradient Descent Update Rule:**
```
W_new = W_old - α * ∂L/∂W
```

Where:
- α = learning rate
- ∂L/∂W = gradient of loss w.r.t. weight

**Why subtract?** Gradient points in direction of increasing loss. We want to go in the opposite direction (decreasing loss).

**Reference:** Phase 5 - Gradient Descent

</details>

---

## Question 6 (Hard)

```python
def backprop_step(dZ, A_prev, W):
    m = A_prev.shape[0]
    dW = (1/m) * np.dot(A_prev.T, dZ)
    db = (1/m) * np.sum(dZ, axis=0, keepdims=True)
    dA_prev = np.dot(dZ, W.T)
    return dW, db, dA_prev
```

What does `dW` represent?

A) Change in weights  
B) Gradient of loss with respect to weights ✓  
C) New weight values  
D) Weight updates after learning rate  

<details>
<summary>Explanation</summary>

**Answer: B) Gradient of loss with respect to weights**

**Backpropagation calculates:**
- `dW = ∂L/∂W` (gradient of loss w.r.t. weights)
- `db = ∂L/∂b` (gradient of loss w.r.t. biases)
- `dA_prev = ∂L/∂A_prev` (gradient to pass to previous layer)

**The actual weight update is:**
```python
W = W - learning_rate * dW
```

**Reference:** Phase 5 - Backpropagation Implementation

</details>

---

## Question 7 (Medium)

What is the purpose of dividing by `m` (batch size) in gradient calculation?

A) To speed up computation  
B) To average gradients across the batch ✓  
C) To normalize weights  
D) To prevent overflow  

<details>
<summary>Explanation</summary>

**Answer: B) To average gradients across the batch**

When training on a batch of `m` examples, we calculate the **average gradient** across all examples:

```python
dW = (1/m) * Σ(gradient_for_each_example)
```

**Why average?**
- Makes gradients independent of batch size
- Ensures consistent learning rate effect
- Reduces gradient variance (more stable training)

**Reference:** Phase 5 - Mini-Batch Gradient Descent

</details>

---

## Question 8 (Hard)

Which initialization strategy is best for deep networks with ReLU?

A) All zeros  
B) All ones  
C) Random small values from N(0, 0.01)  
D) He initialization ✓  

<details>
<summary>Explanation</summary>

**Answer: D) He initialization**

**He Initialization:** 
```python
W = np.random.randn(n_in, n_out) * np.sqrt(2 / n_in)
```

**Why it works:**
- Designed for ReLU activation
- Maintains variance across layers
- Prevents vanishing/exploding gradients

**Wrong answers:**
- **All zeros:** Neurons learn same features (symmetry problem)
- **All ones:** Same issue, worse
- **N(0, 0.01):** Too small for deep networks (vanishing gradients)

**For sigmoid/tanh:** Use Xavier initialization instead

**Reference:** Phase 5 - Weight Initialization

</details>

---

## Question 9 (Medium)

What is "one epoch" in neural network training?

A) One forward pass  
B) One backward pass  
C) One complete pass through the entire training dataset ✓  
D) One weight update  

<details>
<summary>Explanation</summary>

**Answer: C) One complete pass through the entire training dataset**

**Training terminology:**
- **Iteration:** One forward + backward pass on one batch
- **Epoch:** Complete pass through all training data
- **Batch:** Subset of training data processed together

**Example:**
- 1000 training samples, batch size = 100
- 1 epoch = 10 iterations (1000/100)

**Reference:** Phase 5 - Training Process

</details>

---

## Question 10 (Hard)

```python
# Training loop
for epoch in range(100):
    # Forward pass
    A = forward_pass(X, W1, b1, W2, b2)
    loss = compute_loss(A, Y)
    
    # Backward pass
    dW1, db1, dW2, db2 = backprop(X, Y, A, W1, b1, W2, b2)
    
    # Update weights
    W1 = W1 - learning_rate * dW1
    b1 = b1 - learning_rate * db1
    W2 = W2 - learning_rate * dW2
    b2 = b2 - learning_rate * db2
```

This implements which optimization algorithm?

A) Stochastic Gradient Descent (SGD)  
B) Batch Gradient Descent ✓  
C) Mini-Batch Gradient Descent  
D) Adam  

<details>
<summary>Explanation</summary>

**Answer: B) Batch Gradient Descent**

**Clue:** `forward_pass(X, ...)` processes entire dataset `X` at once.

**Gradient Descent variants:**

**Batch GD:**
- Uses entire dataset for each update
- Most accurate gradients, but slow
- What's shown in the code

**Stochastic GD (SGD):**
- Uses one example at a time
- Fast but noisy updates

**Mini-Batch GD:**
- Uses small batches (e.g., 32, 64, 128)
- Good balance: fast + stable
- Most commonly used in practice

**Adam:**
- Adaptive learning rates
- Requires momentum terms (not shown)

**Reference:** Phase 5 - Optimization Algorithms

</details>

---

## Scoring Guide

**0-5 correct (0-50%):** Review Phase 5 content more carefully. Focus on:
- Forward and backward propagation
- Activation functions and their derivatives
- Weight initialization and updates

**6-7 correct (60-70%):** Good progress! Review the questions you missed and practice implementing a neural network from scratch.

**8-9 correct (80-90%):** Excellent! You have solid understanding. Practice on real datasets to reinforce concepts.

**10 correct (100%):** Outstanding! You've mastered neural network fundamentals. Ready for advanced topics (CNNs, RNNs, Transformers).

---

## Compare Your Scores

**Pre-Quiz Score:** ___ / 10  
**Post-Quiz Score:** ___ / 10  
**Improvement:** +___ points

**Typical improvement:** 3-5 points  
**Strong improvement:** 6+ points

---

## Next Steps

1. **Score < 70%:**
   - Re-watch Phase 5 videos
   - Redo the assignment
   - Work through challenges
   - Implement a neural network from scratch

2. **Score ≥ 70%:**
   - ✅ Move to Phase 6 (Advanced topics)
   - Try the bonus challenges
   - Build a project using neural networks

3. **Score = 100%:**
   - Mentor others in the community
   - Contribute to the repository
   - Explore research papers on neural architectures

---

**Congratulations on completing Phase 5! 🎉🧠**
