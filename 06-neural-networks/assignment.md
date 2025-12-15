# Assignment: Build a Neural Network from Scratch

## 🎯 Objective

Build a complete neural network from scratch (without PyTorch/TensorFlow) to classify the MNIST handwritten digits dataset. This assignment will solidify your understanding of how neural networks actually work under the hood.

**Estimated Time:** 6-8 hours  
**Difficulty:** ⭐⭐⭐ Intermediate  
**Due Date:** 2 weeks from assignment

---

## 📋 Requirements

### Part 1: Network Architecture (25 points)

Implement a 3-layer neural network with:

- [ ] **Input layer:** 784 neurons (28x28 flattened images)
- [ ] **Hidden layer 1:** 128 neurons with ReLU activation
- [ ] **Hidden layer 2:** 64 neurons with ReLU activation
- [ ] **Output layer:** 10 neurons with Softmax activation (digits 0-9)

**Required Implementation:**
```python
class NeuralNetwork:
    def __init__(self, layer_sizes):
        """
        Initialize network with given layer sizes.
        
        Args:
            layer_sizes: List of layer sizes, e.g., [784, 128, 64, 10]
        """
        # TODO: Initialize weights and biases
        pass
    
    def forward(self, X):
        """Forward pass through the network."""
        # TODO: Implement forward propagation
        pass
    
    def backward(self, X, y):
        """Backward pass - compute gradients."""
        # TODO: Implement backpropagation
        pass
    
    def update_weights(self, learning_rate):
        """Update weights using computed gradients."""
        # TODO: Implement gradient descent update
        pass
```

### Part 2: Training Loop (25 points)

Implement the training process:

- [ ] Load and preprocess MNIST dataset
- [ ] Implement mini-batch gradient descent
- [ ] Use categorical cross-entropy loss
- [ ] Train for at least 10 epochs
- [ ] Track training and validation loss per epoch
- [ ] Plot learning curves

**Training Requirements:**
- Batch size: 32-128 (your choice)
- Learning rate: 0.001-0.01 (experiment)
- Validation split: 20% of training data
- Save best model based on validation accuracy

### Part 3: Evaluation & Analysis (25 points)

Evaluate your trained model:

- [ ] Calculate final test accuracy (target: >90%)
- [ ] Create confusion matrix
- [ ] Show examples of misclassified digits
- [ ] Analyze which digits are most confused
- [ ] Visualize learned weights from first layer

**Required Metrics:**
```python
# Calculate and report:
- Test Accuracy
- Precision per class
- Recall per class
- F1-Score per class
- Overall confusion matrix
```

### Part 4: Experimentation & Documentation (25 points)

Experiment and document your findings:

- [ ] **Experiment 1:** Try 3 different learning rates - which works best?
- [ ] **Experiment 2:** Compare 2-layer vs 3-layer networks
- [ ] **Experiment 3:** Try different activation functions (sigmoid, tanh, ReLU)
- [ ] **Experiment 4:** Test different weight initialization strategies

**Documentation Requirements:**
- Create a markdown report with:
  - Introduction and approach
  - Architecture decisions and rationale
  - Training process description
  - Results table comparing experiments
  - Conclusions and lessons learned

---

## 📊 Grading Rubric

| Criteria | Exemplary (A: 90-100%) | Proficient (B: 80-89%) | Adequate (C: 70-79%) | Needs Work (D/F: <70%) |
|----------|----------------------|---------------------|-------------------|---------------------|
| **Implementation** | Clean, efficient, well-commented code; all functions work correctly | Mostly correct, minor bugs; adequate comments | Basic implementation with several bugs | Broken or incomplete code |
| **Architecture** | Proper layer sizes, activations, and initialization; optimized design | Correct structure with minor inefficiencies | Basic structure but suboptimal choices | Incorrect architecture |
| **Training** | Smooth convergence, proper validation, excellent learning curves | Good training process with minor issues | Training works but inefficient | Poor training or doesn't converge |
| **Evaluation** | Comprehensive analysis, insightful visualizations, >92% accuracy | Good analysis, clear results, >90% accuracy | Basic evaluation, >85% accuracy | Incomplete evaluation or <85% accuracy |
| **Experiments** | 4+ experiments, thorough analysis, clear insights | 3-4 experiments with good documentation | 2-3 experiments, basic documentation | <2 experiments or poor analysis |
| **Documentation** | Exceptionally clear, professional, insightful | Well-written and organized | Adequate but could be clearer | Poor or missing documentation |

### Grade Breakdown
- **A (90-100):** All requirements met + bonus challenges + exceptional documentation
- **B (80-89):** All core requirements met with good quality
- **C (70-79):** Most requirements met, basic functionality
- **D/F (<70):** Major requirements missing or not working

---

## 🌟 Bonus Challenges (+10 points each, max +30)

### Bonus 1: Advanced Optimizers (+10 points)
- [ ] Implement momentum optimization
- [ ] Implement Adam optimizer
- [ ] Compare SGD vs Momentum vs Adam with plots

### Bonus 2: Regularization (+10 points)
- [ ] Add L2 regularization
- [ ] Implement dropout
- [ ] Show impact on overfitting with plots

### Bonus 3: Advanced Analysis (+10 points)
- [ ] Visualize activation patterns in hidden layers
- [ ] Implement and visualize attention/saliency maps
- [ ] Create interactive demo with matplotlib widgets

### Bonus 4: Performance Optimization (+10 points)
- [ ] Vectorize all operations (no Python loops)
- [ ] Compare training time: original vs optimized
- [ ] Profile code and show bottleneck analysis

---

## 📦 Submission Requirements

### What to Submit

1. **Code Files:**
   - `neural_network.py` - Your NN class implementation
   - `train.py` - Training script
   - `evaluate.py` - Evaluation script
   - `requirements.txt` - Dependencies

2. **Jupyter Notebook:**
   - `analysis.ipynb` - Complete analysis with:
     - Training process
     - Visualizations
     - Experiments
     - Results discussion

3. **Report:**
   - `REPORT.md` - Markdown report with:
     - Methodology
     - Results tables
     - Conclusions
     - Lessons learned

4. **Assets:**
   - `models/` - Saved model weights
   - `plots/` - All generated visualizations
   - `results/` - Experiment results (CSV/JSON)

### Submission Format

**GitHub Repository:**
```
your-name-mnist-nn/
├── README.md              # Setup and run instructions
├── requirements.txt       # Dependencies
├── neural_network.py      # Core implementation
├── train.py              # Training script
├── evaluate.py           # Evaluation script
├── analysis.ipynb        # Analysis notebook
├── REPORT.md             # Written report
├── models/
│   └── best_model.npz    # Saved weights
├── plots/
│   ├── learning_curves.png
│   ├── confusion_matrix.png
│   └── ...
└── results/
    └── experiments.csv
```

**Submit:**
- GitHub repository link (make it public)
- Include all files listed above
- Ensure code runs with: `pip install -r requirements.txt && python train.py`

---

## 💡 Hints & Tips

<details>
<summary>Hint 1: Weight Initialization</summary>

Use Xavier/He initialization to prevent gradient vanishing:
```python
# Xavier initialization for layers with sigmoid/tanh
W = np.random.randn(n_in, n_out) * np.sqrt(2.0 / (n_in + n_out))

# He initialization for layers with ReLU
W = np.random.randn(n_in, n_out) * np.sqrt(2.0 / n_in)
```
</details>

<details>
<summary>Hint 2: Debugging Gradients</summary>

Implement gradient checking to verify backpropagation:
```python
def numerical_gradient(f, x, eps=1e-5):
    """Compute gradient numerically for verification."""
    grad = np.zeros_like(x)
    for i in range(x.size):
        old_val = x.flat[i]
        x.flat[i] = old_val + eps
        pos = f(x)
        x.flat[i] = old_val - eps
        neg = f(x)
        x.flat[i] = old_val
        grad.flat[i] = (pos - neg) / (2 * eps)
    return grad
```
</details>

<details>
<summary>Hint 3: Vectorization</summary>

Avoid loops! Process entire batches at once:
```python
# Bad: Loop through samples
for i in range(batch_size):
    output[i] = np.dot(W, X[i]) + b

# Good: Vectorized
output = np.dot(X, W.T) + b  # Entire batch at once
```
</details>

<details>
<summary>Hint 4: Debugging Low Accuracy</summary>

If accuracy is low, check:
1. Data normalization (scale to 0-1)
2. Learning rate (try 0.001, 0.01, 0.1)
3. Weight initialization
4. Gradient flow (print gradient magnitudes)
5. Loss decreasing? (plot loss curve)
</details>

---

## 📚 Resources

### Essential Reading
- [Backpropagation Calculus (3Blue1Brown)](https://www.youtube.com/watch?v=tIeHLnjs5U8)
- [CS231n: Backpropagation Notes](http://cs231n.github.io/optimization-2/)
- [Neural Networks from Scratch in Python](https://nnfs.io/)

### Code References
- [NumPy Broadcasting Guide](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [MNIST Dataset Documentation](http://yann.lecun.com/exdb/mnist/)
- [Gradient Checking Guide](https://cs231n.github.io/neural-networks-3/#gradcheck)

### Optional Deep Dives
- [Why Momentum Works](https://distill.pub/2017/momentum/)
- [Visualizing Neural Networks](https://cs.stanford.edu/people/karpathy/convnetjs/)
- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

---

## ❓ FAQ

**Q: Can I use PyTorch/TensorFlow for parts of it?**  
A: No - the point is to implement from scratch. You can use NumPy, but not ML frameworks.

**Q: What if I can't reach 90% accuracy?**  
A: 85-89% is still acceptable for a passing grade. Document what you tried and why you think it didn't work better.

**Q: Can I work with a partner?**  
A: Discuss concepts together, but write your own code. No shared code submissions.

**Q: How long should the report be?**  
A: Quality over quantity. 2-4 pages of clear analysis is better than 10 pages of fluff.

**Q: Can I use a different dataset?**  
A: No - use MNIST so we can fairly compare submissions.

---

## 🎓 Learning Objectives

After completing this assignment, you will be able to:

- ✅ Implement forward and backward propagation from scratch
- ✅ Understand the mathematical foundations of neural networks
- ✅ Debug gradient computation issues
- ✅ Choose appropriate hyperparameters
- ✅ Evaluate model performance comprehensively
- ✅ Communicate technical results clearly

---

## 🚀 Getting Started

1. **Fork the starter repository:** [github.com/zero-to-ai/nn-assignment-starter](https://github.com/zero-to-ai/nn-assignment-starter)
2. **Set up your environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install numpy matplotlib scikit-learn jupyter
   ```
3. **Download MNIST:**
   ```python
   from sklearn.datasets import fetch_openml
   mnist = fetch_openml('mnist_784', version=1)
   ```
4. **Start coding!** Begin with the `neural_network.py` skeleton

---

## 💬 Questions & Support

- **Office Hours:** Tuesdays 2-4 PM, Thursdays 3-5 PM
- **Discussion Forum:** [GitHub Discussions](https://github.com/zero-to-ai/discussions)
- **Email:** instructor@zero-to-ai.com (response within 24 hours)
- **Stuck?** Post your question in Discussions - help others by answering too!

---

**Good luck! You've got this! 🚀**

Remember: This assignment is designed to be challenging but doable. Start early, test often, and don't hesitate to ask for help.
