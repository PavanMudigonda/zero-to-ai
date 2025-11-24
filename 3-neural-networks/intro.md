# Neural Networks: From Basics to Transformers

## Table of Contents

1. [What is a Neural Network?](#what-is-a-neural-network)
2. [The Biological Inspiration](#the-biological-inspiration)
3. [Components of Neural Networks](#components-of-neural-networks)
4. [Forward Propagation](#forward-propagation)
5. [Activation Functions](#activation-functions)
6. [Loss Functions](#loss-functions)
7. [Backward Propagation](#backward-propagation)
8. [Optimization](#optimization)
9. [Training Process](#training-process)
10. [Common Architectures](#common-architectures)
11. [From RNNs to Transformers](#from-rnns-to-transformers)

---

## What is a Neural Network?

A **neural network** is a computational model inspired by the human brain that learns to perform tasks by considering examples, without being programmed with task-specific rules.

### The Core Idea

Instead of writing explicit rules:
```python
# Traditional programming
if word in positive_words:
    sentiment = "positive"
else:
    sentiment = "negative"
```

Neural networks learn patterns from data:
```python
# Machine learning approach
model = train_on_examples(training_data)
sentiment = model.predict(new_text)
```

### Why Neural Networks?

**Problems they solve:**
- Recognize patterns in complex data
- Handle non-linear relationships
- Adapt to new patterns automatically
- Scale to large datasets
- Transfer knowledge between tasks

**Real-world applications:**
- Image recognition (faces, objects, medical scans)
- Natural language (translation, summarization, chatbots)
- Speech recognition and synthesis
- Recommendation systems
- Game playing (Chess, Go, video games)
- Drug discovery and protein folding

---

## The Biological Inspiration

### Human Neurons

In your brain:
1. **Dendrites** receive signals from other neurons
2. **Cell body** processes these signals
3. **Axon** sends output to other neurons if threshold is reached
4. **Synapses** connect neurons with varying strengths

### Artificial Neurons (Perceptrons)

A mathematical approximation:
1. **Inputs** (x₁, x₂, ..., xₙ) come from previous layer
2. **Weights** (w₁, w₂, ..., wₙ) represent connection strength
3. **Bias** (b) represents neuron's threshold
4. **Activation function** determines output

```
         inputs
           ↓
    [x₁]──w₁──┐
    [x₂]──w₂──┤
    [x₃]──w₃──├──→ Σ(wᵢxᵢ + b) ──→ activation ──→ output
       ...    │
    [xₙ]──wₙ──┘
```

### Mathematical Formula

```
output = f(Σ(wᵢ × xᵢ) + b)

Where:
- xᵢ = input values
- wᵢ = weights (learnable parameters)
- b = bias (learnable parameter)
- f = activation function
- Σ = sum
```

---

## Components of Neural Networks

### 1. Layers

**Input Layer:**
- Receives raw data
- One neuron per feature
- Example: For 28×28 image = 784 input neurons

**Hidden Layers:**
- Process and transform data
- Multiple layers = "deep" learning
- Each layer learns increasingly abstract features

**Output Layer:**
- Produces final prediction
- Size depends on task:
  - Binary classification: 1 neuron
  - Multi-class (10 classes): 10 neurons
  - Regression: 1 neuron

```
Input → [Hidden Layer 1] → [Hidden Layer 2] → Output
 784      [128 neurons]      [64 neurons]      10
```

### 2. Weights and Biases

**Weights:** The "knowledge" of the network
- Initially random
- Updated during training
- Determine strength of connections

**Biases:** Offset values
- One per neuron
- Allow neurons to activate even with zero input
- Help model fit data better

**Total parameters:**
```
Layer 1: (784 × 128) + 128 = 100,480 parameters
Layer 2: (128 × 64) + 64 = 8,256 parameters
Output:  (64 × 10) + 10 = 650 parameters
Total: 109,386 learnable parameters
```

### 3. Architecture

**Fully Connected (Dense) Layers:**
- Every neuron connects to all neurons in next layer
- Most common in basic networks

**Specialized Layers:**
- **Convolutional (Conv)**: For images, spatial patterns
- **Recurrent (RNN, LSTM, GRU)**: For sequences, temporal patterns
- **Attention**: For focusing on relevant information
- **Dropout**: For regularization (randomly disable neurons)
- **Batch Normalization**: For training stability

---

## Forward Propagation

Forward propagation is how data flows through the network to produce predictions.

### Step-by-Step Process

**1. Input Layer → Hidden Layer 1**

```python
# For each neuron in hidden layer 1
z1 = W1 @ x + b1  # Linear transformation (matrix multiplication)
a1 = activation(z1)  # Apply activation function
```

**2. Hidden Layer 1 → Hidden Layer 2**

```python
z2 = W2 @ a1 + b2
a2 = activation(z2)
```

**3. Hidden Layer 2 → Output**

```python
z3 = W3 @ a2 + b3
output = softmax(z3)  # For classification
```

### Example: 2-Layer Network

```python
import numpy as np

# Input: 4 features
x = np.array([1.0, 0.5, 0.2, 0.9])

# Layer 1: 4 → 3 neurons
W1 = np.random.randn(3, 4)  # Shape: (3, 4)
b1 = np.random.randn(3)
z1 = W1 @ x + b1
a1 = np.maximum(0, z1)  # ReLU activation

# Layer 2: 3 → 2 neurons (output)
W2 = np.random.randn(2, 3)
b2 = np.random.randn(2)
z2 = W2 @ a1 + b2
# a2 = softmax(z2) for classification

print(f"Input shape: {x.shape}")
print(f"Hidden activation shape: {a1.shape}")
print(f"Output shape: {z2.shape}")
```

---

## Activation Functions

Activation functions introduce **non-linearity**, allowing networks to learn complex patterns.

### Why Non-linearity?

Without activation functions, multiple layers collapse into one:
```
f(W2 @ (W1 @ x + b1) + b2) = f((W2 @ W1) @ x + (W2 @ b1 + b2))
                            = f(W_combined @ x + b_combined)
# This is just a single linear layer!
```

### Common Activation Functions

#### 1. ReLU (Rectified Linear Unit) ⭐

**Formula:** `f(x) = max(0, x)`

```
f(x) = { x   if x > 0
       { 0   if x ≤ 0

Graph:
  │
  │    ╱
  │   ╱
  │  ╱
──┼─────
  │
```

**Pros:**
- ✅ Computationally efficient
- ✅ Helps with vanishing gradient problem
- ✅ Sparse activation (many zeros)

**Cons:**
- ❌ "Dying ReLU" - neurons can get stuck at 0

**Usage:** Hidden layers in most modern networks

#### 2. Sigmoid

**Formula:** `f(x) = 1 / (1 + e^(-x))`

```
Output range: (0, 1)

Graph:
  1.0 │     ╱──
      │    ╱
  0.5 │   ╱
      │  ╱
  0.0 │─╱
      └─────────
```

**Pros:**
- ✅ Output interpretable as probability
- ✅ Smooth gradient

**Cons:**
- ❌ Vanishing gradients for large |x|
- ❌ Outputs not zero-centered

**Usage:** Binary classification output, gates in LSTM

#### 3. Tanh (Hyperbolic Tangent)

**Formula:** `f(x) = (e^x - e^(-x)) / (e^x + e^(-x))`

```
Output range: (-1, 1)

Graph:
  1.0 │     ╱──
      │    ╱
  0.0 │   ╱
      │  ╱
 -1.0 │─╱
      └─────────
```

**Pros:**
- ✅ Zero-centered (better than sigmoid)
- ✅ Stronger gradients than sigmoid

**Cons:**
- ❌ Still suffers from vanishing gradients

**Usage:** RNN/LSTM hidden states

#### 4. Softmax

**Formula:** `f(xᵢ) = e^(xᵢ) / Σⱼ e^(xⱼ)`

Converts vector to probability distribution:
```
Input:  [2.0, 1.0, 0.5]
Output: [0.659, 0.242, 0.099]  # Sums to 1.0
```

**Usage:** Multi-class classification output layer

#### 5. GELU (Gaussian Error Linear Unit)

**Formula:** `f(x) = x * Φ(x)` where Φ is Gaussian CDF

**Usage:** Modern transformers (GPT, BERT)

**Why better than ReLU:**
- Smooth, differentiable everywhere
- Better gradient flow
- Used in state-of-the-art models

---

## Loss Functions

Loss functions measure how wrong the model's predictions are.

### Regression Tasks

#### Mean Squared Error (MSE)

```
L = (1/n) Σ (ŷᵢ - yᵢ)²

Where:
- ŷᵢ = predicted value
- yᵢ = actual value
- n = number of samples
```

**Usage:** Continuous value prediction (house prices, temperatures)

#### Mean Absolute Error (MAE)

```
L = (1/n) Σ |ŷᵢ - yᵢ|
```

**Benefit:** Less sensitive to outliers than MSE

### Classification Tasks

#### Binary Cross-Entropy

```
L = -(1/n) Σ [yᵢ log(ŷᵢ) + (1-yᵢ) log(1-ŷᵢ)]
```

**Usage:** Binary classification (spam/not spam)

#### Categorical Cross-Entropy

```
L = -(1/n) Σᵢ Σⱼ yᵢⱼ log(ŷᵢⱼ)

Where:
- i = sample index
- j = class index
- y = one-hot encoded true labels
```

**Usage:** Multi-class classification (digit recognition, sentiment analysis)

**Example:**
```python
# True label: class 2 (one-hot: [0, 0, 1, 0, 0])
y_true = [0, 0, 1, 0, 0]

# Predictions (probabilities)
y_pred = [0.1, 0.2, 0.5, 0.1, 0.1]

# Loss focuses on predicted probability for true class
loss = -log(0.5) = 0.693
```

---

## Backward Propagation

Backpropagation is how the network learns by computing gradients and updating weights.

### The Core Idea

**Goal:** Minimize loss function by adjusting weights

**Method:** Use calculus chain rule to compute how much each weight contributes to the error

### Chain Rule

```
∂L/∂w = ∂L/∂a × ∂a/∂z × ∂z/∂w

Where:
- L = loss
- w = weight
- z = pre-activation (w @ x + b)
- a = post-activation f(z)
```

### Backward Pass

**Step 1: Compute output gradient**
```python
# For classification with softmax + cross-entropy
d_output = predictions - true_labels
```

**Step 2: Propagate through layer 2**
```python
d_W2 = d_output @ a1.T
d_b2 = d_output
d_a1 = W2.T @ d_output
```

**Step 3: Apply activation gradient**
```python
# For ReLU: gradient is 1 if input > 0, else 0
d_z1 = d_a1 * (z1 > 0)
```

**Step 4: Propagate through layer 1**
```python
d_W1 = d_z1 @ x.T
d_b1 = d_z1
```

### Update Weights

```python
# Simple gradient descent
learning_rate = 0.01
W1 -= learning_rate * d_W1
b1 -= learning_rate * d_b1
W2 -= learning_rate * d_W2
b2 -= learning_rate * d_b2
```

---

## Optimization

Optimization algorithms update network weights to minimize loss.

### Gradient Descent Variants

#### 1. Stochastic Gradient Descent (SGD)

```python
# Update after each sample
for x, y in dataset:
    loss = compute_loss(model(x), y)
    gradients = compute_gradients(loss)
    weights -= learning_rate * gradients
```

**Pros:** Fast updates, can escape local minima
**Cons:** Noisy updates, slow convergence

#### 2. Mini-Batch Gradient Descent

```python
# Update after batch of samples
for batch_x, batch_y in dataloader:
    loss = compute_loss(model(batch_x), batch_y)
    gradients = compute_gradients(loss)
    weights -= learning_rate * gradients
```

**Common batch sizes:** 32, 64, 128, 256

**Pros:** Balance between speed and stability

#### 3. SGD with Momentum

```python
velocity = 0
for batch in dataset:
    gradients = compute_gradients(batch)
    velocity = momentum * velocity - learning_rate * gradients
    weights += velocity
```

**Benefit:** Accelerates convergence, dampens oscillations

### Modern Optimizers

#### Adam (Adaptive Moment Estimation) ⭐

Most popular optimizer for deep learning:

```python
# Combines momentum and adaptive learning rates
m = 0  # First moment (mean)
v = 0  # Second moment (variance)

for batch in dataset:
    gradients = compute_gradients(batch)
    m = beta1 * m + (1 - beta1) * gradients
    v = beta2 * v + (1 - beta2) * gradients**2
    
    m_hat = m / (1 - beta1**t)  # Bias correction
    v_hat = v / (1 - beta2**t)
    
    weights -= learning_rate * m_hat / (sqrt(v_hat) + epsilon)
```

**Default hyperparameters:**
- learning_rate = 0.001
- beta1 = 0.9
- beta2 = 0.999
- epsilon = 1e-8

**Benefits:**
- ✅ Adaptive learning rates per parameter
- ✅ Works well with minimal tuning
- ✅ Efficient for large datasets

#### Others

- **AdamW**: Adam with better weight decay
- **RMSprop**: Good for RNNs
- **AdaGrad**: Adapts learning rate based on parameter frequency

---

## Training Process

### Complete Training Loop

```python
import torch
import torch.nn as nn
import torch.optim as optim

# 1. Define model
model = NeuralNetwork()

# 2. Define loss function
criterion = nn.CrossEntropyLoss()

# 3. Define optimizer
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. Training loop
num_epochs = 10
for epoch in range(num_epochs):
    for batch_x, batch_y in train_loader:
        # Forward pass
        predictions = model(batch_x)
        loss = criterion(predictions, batch_y)
        
        # Backward pass
        optimizer.zero_grad()  # Clear previous gradients
        loss.backward()         # Compute gradients
        optimizer.step()        # Update weights
    
    # Validation
    val_loss = evaluate(model, val_loader)
    print(f"Epoch {epoch}: Train Loss={loss:.4f}, Val Loss={val_loss:.4f}")
```

### Training Best Practices

#### 1. Train/Validation/Test Split

```
Dataset → 70% Training (optimize weights)
       → 15% Validation (tune hyperparameters)
       → 15% Test (final evaluation)
```

#### 2. Normalization

```python
# Normalize inputs to zero mean, unit variance
X = (X - X.mean()) / X.std()
```

**Why:** Helps optimization converge faster

#### 3. Weight Initialization

```python
# Xavier/Glorot initialization for tanh
W = np.random.randn(n_in, n_out) * np.sqrt(1 / n_in)

# He initialization for ReLU
W = np.random.randn(n_in, n_out) * np.sqrt(2 / n_in)
```

#### 4. Learning Rate Scheduling

```python
# Reduce learning rate when validation loss plateaus
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=5)
scheduler.step(val_loss)
```

#### 5. Early Stopping

```python
# Stop training if validation loss doesn't improve
best_val_loss = float('inf')
patience_counter = 0

if val_loss < best_val_loss:
    best_val_loss = val_loss
    patience_counter = 0
else:
    patience_counter += 1
    if patience_counter >= patience:
        print("Early stopping!")
        break
```

#### 6. Regularization

**Dropout:**
```python
# Randomly disable neurons during training
layer = nn.Linear(128, 64)
dropout = nn.Dropout(p=0.5)  # Disable 50% of neurons
```

**Weight Decay (L2 regularization):**
```python
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=0.01)
```

---

## Common Architectures

### 1. Feedforward Neural Network (FNN)

```
Input → Dense → ReLU → Dense → ReLU → Dense → Output
```

**Use cases:** Tabular data, simple classification

### 2. Convolutional Neural Network (CNN)

```
Image → Conv → ReLU → Pool → Conv → ReLU → Pool → Flatten → Dense → Output
```

**Use cases:** Image classification, object detection, computer vision

**Key innovation:** Learns spatial hierarchies (edges → shapes → objects)

### 3. Recurrent Neural Network (RNN)

```
Word₁ → [RNN] → Hidden State → Word₂ → [RNN] → ...
           ↓                      ↓
        Output₁                Output₂
```

**Use cases:** Time series, text, sequential data

**Problem:** Vanishing gradients on long sequences

### 4. LSTM (Long Short-Term Memory)

Improved RNN with gates to control information flow:
- **Forget gate**: What to forget from memory
- **Input gate**: What new information to add
- **Output gate**: What to output

**Use cases:** Machine translation, speech recognition

---

## From RNNs to Transformers

### The Sequential Processing Problem

**RNNs must process one token at a time:**

```
"The cat sat on the mat"

Step 1: Process "The"      → hidden_state₁
Step 2: Process "cat"      → hidden_state₂ (depends on step 1)
Step 3: Process "sat"      → hidden_state₃ (depends on step 2)
...

❌ Cannot parallelize
❌ Long-range dependencies fade
❌ Slow training
```

### The Attention Revolution

**Key insight:** What if we could look at ALL words simultaneously?

```
"The cat sat on the mat"

For predicting next word:
- Look at all positions at once
- Compute relevance scores (attention weights)
- Focus more on important words
- Process in parallel

✅ Parallelizable
✅ Long-range dependencies preserved
✅ Fast training
```

### Transformer Benefits

1. **Parallel Processing**: All positions computed simultaneously
2. **Long Context**: No vanishing gradients over distance
3. **Flexibility**: Same architecture for many tasks
4. **Scalability**: Can train on massive datasets
5. **Transfer Learning**: Pre-train once, fine-tune for many tasks

This is why transformers have become the dominant architecture for:
- Natural Language Processing (GPT, BERT, T5)
- Computer Vision (Vision Transformer)
- Multi-modal models (CLIP, GPT-4)
- Audio (Whisper)
- Code generation (Codex, GitHub Copilot)

---

## Next Steps

Now that you understand neural network basics, proceed to:

1. **`attention_explained.md`** - Deep dive into attention mechanism
2. **`transformer_architecture.md`** - Complete transformer breakdown
3. **Run the Python examples** - Hands-on implementation

The journey continues! 🚀
