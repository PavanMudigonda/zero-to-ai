# Challenges: Neural Networks

> **Hands-on challenges to deepen your understanding of neural networks**

## 🚀 Challenge 1: Gradient Vanishing Detective

**Difficulty:** ⭐⭐ Beginner-Intermediate  
**Time:** 30-45 minutes  
**Concepts:** Activation functions, gradient flow, deep networks

### The Problem
Build a very deep neural network (10+ layers) and observe the gradient vanishing problem in action.

### Your Task
1. Create a 15-layer network with sigmoid activations
2. Train on MNIST dataset
3. Track gradient magnitudes at each layer during training
4. Visualize the gradients - notice how they get smaller in early layers?
5. Fix it by switching to ReLU - observe the difference!

### Starter Code
```python
class DeepNetwork:
    def __init__(self, n_layers=15, activation='sigmoid'):
        self.n_layers = n_layers
        self.activation = activation
        # TODO: Initialize layers
    
    def track_gradients(self):
        """Return gradient magnitudes for each layer."""
        # TODO: Track gradient norms
        pass
```

### Success Criteria
- [ ] Demonstrate gradient vanishing with sigmoid
- [ ] Show improvement with ReLU
- [ ] Create visualization comparing both
- [ ] Explain why this happens mathematically

<details>
<summary>💡 Hint</summary>
Sigmoid derivative: max value is 0.25. If you chain 15 layers: 0.25^15 ≈ 0 (vanishing!)
ReLU derivative: either 0 or 1, so gradients flow better.
</details>

---

## 🚀 Challenge 2: Architecture Search

**Difficulty:** ⭐⭐⭐ Intermediate  
**Time:** 1-2 hours  
**Concepts:** Hyperparameter tuning, model selection, experimental design

### The Problem
Find the best neural network architecture for CIFAR-10 image classification.

### Your Task
Experiment with:
- Number of layers (2, 4, 6, 8)
- Layer sizes (32, 64, 128, 256)
- Activation functions (ReLU, LeakyReLU, ELU)
- Dropout rates (0, 0.2, 0.5)
- Batch sizes (32, 64, 128)

### Requirements
1. Test at least 20 different architectures
2. Track accuracy, training time, and parameter count
3. Create visualization showing tradeoffs
4. Identify Pareto-optimal architectures
5. Present your findings

### Deliverable
```
results/
├── experiment_log.csv      # All experiments
├── best_models.json        # Top 5 configurations
├── tradeoff_plot.png      # Accuracy vs params vs time
└── recommendations.md      # Your analysis
```

<details>
<summary>💡 Hint</summary>
Use a grid search or random search. Track experiments in a DataFrame. 
Consider accuracy/params ratio as a metric.
</details>

---

## 🚀 Challenge 3: Attention Visualization

**Difficulty:** ⭐⭐⭐ Intermediate-Advanced  
**Time:** 2-3 hours  
**Concepts:** Attention mechanism, visualization, interpretability

### The Problem
Implement and visualize a simple attention mechanism for sequence classification.

### Your Task
1. Build attention layer from scratch
2. Train on text sentiment classification
3. Visualize attention weights for sample inputs
4. Show which words the model focuses on
5. Compare with/without attention

### Example Output
```
Input: "This movie was absolutely terrible and boring"
Attention weights:
- "terrible": 0.45 ██████████
- "boring": 0.38   ████████
- "absolutely": 0.10 ██
- Other words: <0.05
Prediction: Negative (0.92 confidence)
```

### Success Criteria
- [ ] Working attention implementation
- [ ] Heatmap visualization of attention
- [ ] Interpretable results
- [ ] Performance comparison

<details>
<summary>💡 Hint</summary>
Attention formula: α = softmax(score(h_i, query))
Output = Σ α_i * h_i
Start with simple dot-product attention.
</details>

---

## 🚀 Challenge 4: Transfer Learning Master

**Difficulty:** ⭐⭐⭐⭐ Advanced  
**Time:** 3-4 hours  
**Concepts:** Transfer learning, fine-tuning, domain adaptation

### The Problem
Use a pre-trained ImageNet model for a custom classification task with limited data.

### Your Task
1. Choose a small custom dataset (100-500 images, 5-10 classes)
2. Load pre-trained ResNet/VGG/MobileNet
3. Try 3 approaches:
   - Feature extraction (freeze all layers)
   - Fine-tuning (unfreeze last few layers)
   - Full training (train entire network)
4. Compare results and training time
5. Analyze which layers learn what

### Dataset Suggestions
- Food classification
- Dog breed recognition
- Flower species
- Medical images
- Your own photos

### Analysis Required
- Learning curves for each approach
- Confusion matrices
- Layer-wise feature visualization
- Recommendations for when to use each approach

<details>
<summary>💡 Hint</summary>
Feature extraction works well with <1000 images.
Fine-tuning helps when task is somewhat different from ImageNet.
Full training needs lots of data.
</details>

---

## 🚀 Challenge 5: Neural Network Debugger

**Difficulty:** ⭐⭐⭐ Intermediate  
**Time:** 1-2 hours  
**Concepts:** Debugging, troubleshooting, systematic diagnosis

### The Problem
You're given 5 broken neural network implementations. Find and fix the bugs!

### Scenarios

**Bug 1: The Never-Learning Network**
```python
# Network trains but loss doesn't decrease
# What's wrong?
for epoch in range(100):
    loss = compute_loss(model(X), y)
    gradients = backprop(loss)
    # weights stay the same! Why?
```

**Bug 2: The Exploding Loss**
```python
# Loss goes to infinity after a few batches
# What's the issue?
def train_step(X, y):
    pred = model(X)
    loss = mse_loss(pred, y)
    # loss = 1e+10 after iteration 3
```

**Bug 3: The Plateauing Network**
```python
# Accuracy stuck at 10% on MNIST (10 classes)
# Red flag! What's happening?
```

**Bug 4: The Slow Learner**
```python
# Training takes 10x longer than expected
# Same architecture, same data
# Where's the bottleneck?
```

**Bug 5: The Overfitting Champion**
```python
# Training accuracy: 99%
# Validation accuracy: 45%
# How do you fix this?
```

### Your Task
- Identify each bug
- Explain why it happens
- Provide the fix
- Share prevention strategies

<details>
<summary>💡 Hint 1</summary>
Bug 1: Are you actually updating the weights?
Bug 2: Check learning rate and weight initialization
Bug 3: Is your model predicting all one class?
Bug 4: Profile your code - is it the data loading?
Bug 5: Classic overfitting - what's missing?
</details>

---

## 🌟 Meta Challenge: Build Your Own Framework

**Difficulty:** ⭐⭐⭐⭐⭐ Expert  
**Time:** 8-12 hours  
**Concepts:** Software engineering, API design, comprehensive understanding

### The Ultimate Challenge
Build a mini deep learning framework (like PyTorch, but simpler).

### Requirements
Your framework should support:
- [ ] Automatic differentiation (autograd)
- [ ] Common layers (Linear, Conv2D, ReLU, etc.)
- [ ] Loss functions (MSE, CrossEntropy)
- [ ] Optimizers (SGD, Adam)
- [ ] Model save/load
- [ ] GPU support (optional but impressive!)

### Example Usage
```python
from your_framework import Module, Linear, ReLU, CrossEntropyLoss, Adam

class MyModel(Module):
    def __init__(self):
        self.fc1 = Linear(784, 128)
        self.relu = ReLU()
        self.fc2 = Linear(128, 10)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

model = MyModel()
optimizer = Adam(model.parameters(), lr=0.001)
criterion = CrossEntropyLoss()

# Training loop works just like PyTorch!
```

### Bonus Points
- Clean, documented API
- Comprehensive tests
- Tutorial notebooks
- Performance benchmarks
- PyTorch compatibility layer

---

## 📊 Challenge Completion Tracker

Mark off challenges as you complete them:

- [ ] Challenge 1: Gradient Vanishing Detective
- [ ] Challenge 2: Architecture Search
- [ ] Challenge 3: Attention Visualization
- [ ] Challenge 4: Transfer Learning Master
- [ ] Challenge 5: Neural Network Debugger
- [ ] Meta Challenge: Build Your Own Framework

---

## 🏆 Share Your Solutions!

Completed a challenge? Share your solution:

1. **GitHub:** Create a repo with your solution
2. **Discussions:** Post in [Challenges Section](https://github.com/zero-to-ai/discussions/categories/challenges)
3. **Tag:** Use `#ZeroToAI` and `#NNChallenge`
4. **Help Others:** Comment on others' solutions

---

## 💡 Learning Tips

- **Start small:** Don't try all challenges at once
- **Debug systematically:** Print intermediate values, visualize data
- **Compare with libraries:** Check your implementation against PyTorch
- **Read papers:** Many challenges have research papers behind them
- **Ask for help:** Post in Discussions if stuck

---

**Happy challenging! 🚀**

Remember: The goal is to learn, not to complete everything perfectly. Each challenge deepens your understanding!
