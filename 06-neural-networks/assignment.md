# Assignment: Build a Neural Network from Scratch

## 🎯 Objective

Build a complete neural network from scratch (without PyTorch/TensorFlow) to classify the MNIST handwritten digits dataset. This assignment will solidify your understanding of how neural networks actually work under the hood.

**Estimated Time:** 6-8 hours  
**Difficulty:** ⭐⭐⭐ Intermediate  
**Suggested Pace:** 1-2 weeks if you are moving through the course sequentially

---

## 📋 Requirements

### Part 1: Network Architecture

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

### Part 2: Training Loop

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

### Part 3: Evaluation & Analysis

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

### Part 4: Experimentation & Documentation

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

## 📊 Self-Review Guide

| Criteria | Strong | Working | Emerging | Needs revision |
|----------|--------|---------|----------|----------------|
| **Implementation** | Clean, efficient, understandable code; all functions work correctly | Mostly correct with minor bugs | Basic implementation with several bugs | Broken or incomplete |
| **Architecture** | Proper layer sizes, activations, and initialization with clear rationale | Correct structure with minor inefficiencies | Basic structure but suboptimal choices | Incorrect architecture |
| **Training** | Smooth convergence, validation tracking, clear learning curves | Good training process with minor issues | Training works but is inefficient | Poor training or does not converge |
| **Evaluation** | Comprehensive analysis, strong visualizations, and target accuracy reached | Good analysis with clear results | Basic evaluation with partial analysis | Incomplete evaluation or very weak results |
| **Experiments** | Four or more experiments with clear insights | Three to four experiments with good documentation | Two to three experiments with basic documentation | Fewer than two experiments or poor analysis |
| **Documentation** | Clear, professional, and reflective | Well organized and readable | Adequate but could be clearer | Poor or missing documentation |

### Suggested Interpretation
- If all core requirements work and your analysis is clear, the project is in strong shape.
- If the model trains but some experiments or analysis are thin, strengthen the documentation before moving on.
- If the implementation is unstable, focus first on correctness, then on accuracy improvements.

---

## 🌟 Optional Extensions

### Optional Extension 1: Advanced Optimizers
- [ ] Implement momentum optimization
- [ ] Implement Adam optimizer
- [ ] Compare SGD vs Momentum vs Adam with plots

### Optional Extension 2: Regularization
- [ ] Add L2 regularization
- [ ] Implement dropout
- [ ] Show impact on overfitting with plots

### Optional Extension 3: Advanced Analysis
- [ ] Visualize activation patterns in hidden layers
- [ ] Implement and visualize attention/saliency maps
- [ ] Create interactive demo with matplotlib widgets

### Optional Extension 4: Performance Optimization
- [ ] Vectorize all operations (no Python loops)
- [ ] Compare training time: original vs optimized
- [ ] Profile code and show bottleneck analysis

---

## 📦 Deliverables

### What to Prepare

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

### Suggested Project Structure

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

**Recommended packaging:**
- Keep the project in a public or private GitHub repository
- Include all files listed above
- Ensure the code runs with: `pip install -r requirements.txt && python train.py`

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
A: 85-89% is still a solid result for a first from-scratch implementation. Document what you tried and why it likely plateaued.

**Q: Can I work with a partner?**  
A: Discuss concepts together if helpful, but build and understand your own implementation.

**Q: How long should the report be?**  
A: Quality over quantity. 2-4 pages of clear analysis is better than 10 pages of fluff.

**Q: Can I use a different dataset?**  
A: Stick with MNIST for the first pass so your results stay comparable with the rest of the assignment.

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

- **Discussion Forum:** [GitHub Discussions](https://github.com/zero-to-ai/discussions)
- **Stuck?** Post the bug, the exact error, and what you already tried.
- **Best workflow:** Finish the core phase notebooks first, then come back to this assignment if your fundamentals still feel shaky.

---

**Good luck! You've got this! 🚀**

Remember: This assignment is designed to be challenging but doable. Start early, test often, and don't hesitate to ask for help.
