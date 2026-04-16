# Neural Networks - Pre-Quiz

**Time:** 15 minutes  
**Questions:** 10  
**Passing Score:** 70%  
**Purpose:** Assess your baseline knowledge before learning about neural networks

---

## Question 1 (Easy)

What is a neural network inspired by?

A) Computer circuits  
B) The human brain ✓  
C) Mathematical functions  
D) Decision trees  

<details>
<summary>Explanation</summary>

**Answer: B) The human brain**

Neural networks are loosely inspired by biological neurons in the brain. They consist of interconnected nodes (neurons) that process information, similar to how biological neurons fire signals.

**Reference:** Phase 6 - Introduction to Neural Networks

</details>

---

## Question 2 (Easy)

What is the basic unit of a neural network called?

A) Cell  
B) Node  
C) Neuron ✓  
D) Layer  

<details>
<summary>Explanation</summary>

**Answer: C) Neuron**

While "node" is also commonly used, the formal term is "neuron" or "artificial neuron," reflecting the biological inspiration.

**Reference:** Phase 6 - Neural Network Basics

</details>

---

## Question 3 (Medium)

In a neural network, what does a "weight" represent?

A) The size of the network  
B) The strength of a connection between neurons ✓  
C) The number of neurons  
D) The learning rate  

<details>
<summary>Explanation</summary>

**Answer: B) The strength of a connection between neurons**

Weights are parameters that determine how much influence one neuron has on another. During training, these weights are adjusted to improve the network's performance.

**Reference:** Phase 6 - Weights and Biases

</details>

---

## Question 4 (Medium)

What is the purpose of an activation function?

A) To speed up training  
B) To introduce non-linearity ✓  
C) To reduce overfitting  
D) To normalize inputs  

<details>
<summary>Explanation</summary>

**Answer: B) To introduce non-linearity**

Activation functions introduce non-linearity into the network, allowing it to learn complex patterns. Without activation functions, a neural network would just be a linear regression model regardless of how many layers it has.

**Reference:** Phase 6 - Activation Functions

</details>

---

## Question 5 (Easy)

What are the three main types of layers in a typical neural network?

A) Input, Output, Middle  
B) Input, Hidden, Output ✓  
C) Start, Process, End  
D) Data, Compute, Result  

<details>
<summary>Explanation</summary>

**Answer: B) Input, Hidden, Output**

- **Input layer:** Receives the initial data
- **Hidden layer(s):** Process the data (can be multiple)
- **Output layer:** Produces the final prediction

**Reference:** Phase 6 - Network Architecture

</details>

---

## Question 6 (Hard)

What is backpropagation used for?

A) Forward pass computation  
B) Calculating gradients for weight updates ✓  
C) Initializing weights  
D) Preventing overfitting  

<details>
<summary>Explanation</summary>

**Answer: B) Calculating gradients for weight updates**

Backpropagation is an algorithm that calculates the gradient of the loss function with respect to each weight using the chain rule of calculus. These gradients are then used to update the weights via gradient descent.

**Reference:** Phase 6 - Backpropagation

</details>

---

## Question 7 (Medium)

What does the "learning rate" control?

A) How fast the network learns  
B) The size of weight updates ✓  
C) The number of epochs  
D) The batch size  

<details>
<summary>Explanation</summary>

**Answer: B) The size of weight updates**

The learning rate (α) determines how much the weights are adjusted during each training step. Too large: training becomes unstable. Too small: training is very slow.

Formula: `new_weight = old_weight - learning_rate * gradient`

**Reference:** Phase 6 - Training Hyperparameters

</details>

---

## Question 8 (Hard)

```python
import numpy as np
weights = np.array([0.5, -0.3, 0.8])
inputs = np.array([1, 2, 3])
bias = 0.1
output = np.dot(weights, inputs) + bias
```

What is the value of `output`?

A) 1.4  
B) 2.0  
C) 2.4 ✓  
D) 3.0  

<details>
<summary>Explanation</summary>

**Answer: C) 2.4**

**Calculation:**
```
output = (0.5 × 1) + (-0.3 × 2) + (0.8 × 3) + 0.1
       = 0.5 + (-0.6) + 2.4 + 0.1
       = 2.4
```

This is a simple neuron computation: weighted sum of inputs plus bias.

**Reference:** Phase 6 - Forward Pass

</details>

---

## Question 9 (Medium)

What is the main difference between a shallow and a deep neural network?

A) Input size  
B) Number of hidden layers ✓  
C) Activation function used  
D) Learning rate  

<details>
<summary>Explanation</summary>

**Answer: B) Number of hidden layers**

- **Shallow network:** 1-2 hidden layers
- **Deep network:** 3+ hidden layers (hence "deep learning")

Deep networks can learn more complex, hierarchical representations of data.

**Reference:** Phase 6 - Deep Learning Basics

</details>

---

## Question 10 (Hard)

Which statement about the vanishing gradient problem is TRUE?

A) It only affects the output layer  
B) It makes gradients in early layers very small ✓  
C) It speeds up training  
D) It only occurs with ReLU activation  

<details>
<summary>Explanation</summary>

**Answer: B) It makes gradients in early layers very small**

In deep networks with certain activation functions (e.g., sigmoid, tanh), gradients can become extremely small as they propagate backward through layers. This makes it difficult to update weights in early layers.

**Solution:** Use ReLU activation or batch normalization

**Reference:** Phase 6 - Training Challenges

</details>

---

## Self-Check Guide

**0-3 correct:** Start with the basics and take your time.

**4-5 correct:** You have some foundation; review linear algebra and calculus before diving in.

**6-7 correct:** Good baseline for learning neural networks.

**8-9 correct:** Strong fundamentals; this phase should deepen them well.

**10 correct:** Excellent starting point, with room to sharpen implementation details.

---

## Next Steps

After taking this pre-quiz:

1. **If you found the quiz difficult:** Review these prerequisites first:
   - Linear algebra (matrix multiplication)
   - Basic calculus (derivatives)
   - Python programming

2. **If the concepts felt familiar:** Proceed with Phase 6 content

3. **Retake after Phase 6:** Take the post-quiz to measure your progress

---

**Remember:** A low score is perfectly normal! This quiz shows where you're starting, not where you'll end up. 🚀
