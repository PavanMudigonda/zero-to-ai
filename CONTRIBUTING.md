# Contributing to AI/ML Learning Repository

Thank you for your interest in contributing to this comprehensive AI/ML learning repository! This project contains 732 notebooks across 14 phases, designed to take learners from Python fundamentals to advanced topics like local LLMs and multimodal AI.

## 🎯 What Contributions Are Welcome

We welcome all contributions that enhance the learning experience:

- **New Notebooks**: Add tutorials on emerging AI/ML topics (December 2025 models and beyond)
- **Bug Fixes**: Correct errors in code, fix broken dependencies, or update deprecated APIs
- **Documentation**: Improve explanations, add diagrams, clarify concepts
- **Exercises**: Add practice problems or solutions to existing notebooks
- **Code Quality**: Refactor notebooks for clarity, add type hints, improve comments
- **Resources**: Add relevant papers, articles, or external learning materials
- **Translations**: Help make content accessible in other languages

## 📚 Repository Structure

Our learning path follows 14 phases:

```
0-python/              # Python fundamentals
1-data-science/        # NumPy, Pandas, Matplotlib, Scikit-learn
2-maths/               # Mathematical foundations (Linear Algebra, Calculus, Statistics)
3-token/               # Tokenization (BPE, WordPiece, SentencePiece)
4-embeddings/          # Word and sentence embeddings
5-neural-networks/     # Deep learning fundamentals, PyTorch
6-vector-databases/    # ChromaDB, Qdrant, Weaviate, Pinecone
7-rag/                 # Retrieval-Augmented Generation
8-mlops/               # ML Operations and deployment
9-specializations/     # Domain-specific applications
10-prompt-engineering/ # Advanced prompting techniques
11-llm-finetuning/     # LoRA, QLoRA, PEFT methods
12-multimodal/         # Vision-language models, image generation
13-local-llms/         # Ollama, local model deployment
```

## 🛠️ Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/aiml-repo.git
cd aiml-repo/aiml
```

### 2. Set Up Your Environment

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Create a Branch

```bash
# Create a descriptive branch name
git checkout -b add-diffusion-models-notebook
# or
git checkout -b fix-embedding-dimension-error
```

## 📝 Notebook Standards

### Notebook Structure Template

Every notebook should follow this structure:

````markdown
# [Topic Name]: [Specific Focus]

## 📋 Learning Objectives

By the end of this notebook, you will be able to:
- Objective 1 (action-oriented)
- Objective 2 (measurable outcome)
- Objective 3 (practical skill)

## 🎯 Prerequisites

- **Required Knowledge**: [Previous topics/concepts needed]
- **Recommended Notebooks**: [Links to prerequisite notebooks]
- **Required Packages**: `package1`, `package2`, `package3`

## 🔧 Setup and Imports

```python
# Standard imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ML/AI specific imports
import torch
from transformers import AutoModel, AutoTokenizer

# Configuration
%matplotlib inline
plt.style.use('seaborn-v0_8')
```

## 📖 Theory and Concepts

[Clear explanations with mathematical foundations when needed]

**Key Concepts:**
- **Concept 1**: Definition and intuition
- **Concept 2**: Why it matters in practice

## 💻 Implementation

### Step 1: [First Major Step]

```python
# Well-commented, production-quality code
def example_function(input_data):
    """
    Brief description of what this function does.
    
    Args:
        input_data: Description of parameter
        
    Returns:
        Description of return value
    """
    # Implementation
    pass
```

### Step 2: [Next Major Step]

[Continue with logical progression]

## 🧪 Practical Exercises

**Exercise 1**: [Description]
```python
# Your code here
```

**Exercise 2**: [Description with hints]
```python
# Hint: Consider using X approach
```

## 🎓 Key Takeaways

- ✅ Takeaway 1
- ✅ Takeaway 2
- ✅ Takeaway 3

## 📚 Next Steps

- **Next Notebook**: [Link to logical next topic]
- **Advanced Topics**: [Related advanced concepts]
- **Further Reading**: [Papers, articles, documentation]

## 🔗 References

1. [Paper/Article Title](URL) - Brief description
2. [Documentation](URL)
````

### Code Quality Standards

1. **Clarity Over Cleverness**: Write code that teaches, not code that impresses
   ```python
   # Good: Clear and educational
   attention_scores = torch.matmul(query, key.transpose(-2, -1))
   attention_scores = attention_scores / math.sqrt(d_k)
   
   # Avoid: Too condensed for learning
   attn = torch.matmul(q, k.T) / math.sqrt(d_k)
   ```

2. **Type Hints**: Use type hints for clarity
   ```python
   def calculate_embedding_similarity(
       emb1: np.ndarray, 
       emb2: np.ndarray
   ) -> float:
       return np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
   ```

3. **Docstrings**: Include docstrings for all functions and classes
   ```python
   def train_lora_model(model, dataset, rank=8):
       """
       Fine-tune a model using LoRA (Low-Rank Adaptation).
       
       Args:
           model: Pre-trained transformer model
           dataset: Training dataset with 'text' and 'label' columns
           rank: LoRA rank parameter (lower = fewer trainable params)
           
       Returns:
           Trained model with LoRA adapters attached
       """
   ```

4. **Comments**: Explain "why", not just "what"
   ```python
   # Use fp16 to reduce memory footprint and enable larger batch sizes
   model = model.half()
   ```

5. **Error Handling**: Show learners how to handle common issues
   ```python
   try:
       tokenizer = AutoTokenizer.from_pretrained(model_name)
   except OSError:
       print(f"Model {model_name} not found. Downloading...")
       tokenizer = AutoTokenizer.from_pretrained(model_name, force_download=True)
   ```

6. **Dependencies**: Pin versions when critical
   ```python
   # requirements.txt
   torch>=2.0.0,<3.0.0
   transformers>=4.36.0
   sentence-transformers>=2.2.2
   ```

## 🎨 Educational Philosophy

Our notebooks prioritize:

1. **Learning Over Brevity**: Verbose explanations are better than terse code
2. **Practical Over Theoretical**: Show real-world applications alongside theory
3. **Modern Best Practices**: Use current tools (as of December 2025)
4. **Progressive Complexity**: Build from fundamentals to advanced topics
5. **Hands-On Learning**: Include exercises and experiments
6. **MDTP Framework**: Focus on Mastery through Deliberate, Thoughtful Practice

### Good Example: Teaching Attention

```python
"""
Attention Mechanism: The Core of Transformers

The attention mechanism allows models to focus on relevant parts of the input.
Think of it like highlighting important words when reading a passage.
"""

def scaled_dot_product_attention(query, key, value, mask=None):
    """
    Compute scaled dot-product attention.
    
    Intuition: 
    1. Compare query with all keys (how relevant is each position?)
    2. Scale down to prevent large values
    3. Apply softmax to get probabilities
    4. Use these probabilities to weight the values
    
    Args:
        query: What we're looking for [batch, seq_len, d_k]
        key: What we're comparing against [batch, seq_len, d_k]
        value: What we return if we find a match [batch, seq_len, d_v]
        mask: Optional mask to prevent attention to certain positions
        
    Returns:
        Weighted sum of values [batch, seq_len, d_v]
        Attention weights [batch, seq_len, seq_len]
    """
    d_k = query.size(-1)
    
    # Step 1: Compute attention scores (similarity between query and keys)
    scores = torch.matmul(query, key.transpose(-2, -1))  # [batch, seq_len, seq_len]
    
    # Step 2: Scale by sqrt(d_k) to prevent vanishing gradients with large d_k
    scores = scores / math.sqrt(d_k)
    
    # Step 3: Apply mask (for padding or causal attention)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    
    # Step 4: Convert to probabilities
    attention_weights = F.softmax(scores, dim=-1)
    
    # Step 5: Apply attention to values
    output = torch.matmul(attention_weights, value)
    
    return output, attention_weights
```

## 🔄 Pull Request Process

### 1. Commit Your Changes

Use [Conventional Commits](https://www.conventionalcommits.org/):

```bash
# For new notebooks
git commit -m "feat: add stable diffusion XL tutorial"

# For bug fixes
git commit -m "fix: correct embedding dimension in semantic search"

# For documentation
git commit -m "docs: clarify tokenizer training process"

# For updates to existing content
git commit -m "refactor: improve LoRA fine-tuning code readability"
```

### 2. Test Your Notebook

Before submitting, ensure:
- ✅ All cells execute without errors (Run All Cells)
- ✅ Output is included and demonstrates the concepts
- ✅ Required packages are listed in the notebook
- ✅ Code follows our style guidelines
- ✅ Explanations are clear and beginner-friendly
- ✅ Links and references work

### 3. Update Documentation

If you added a new notebook:
- Update the relevant phase README.md
- Add entry to the main checklist.md
- Update setup.md if new dependencies are needed

### 4. Submit Pull Request

```bash
git push origin your-branch-name
```

Then create a PR on GitHub with:
- Clear title describing the change
- Description of what was added/fixed
- Screenshots if relevant (visualizations, outputs)
- Related issue numbers (if applicable)

### 5. Code Review

- Maintainers will review within 5-7 days
- Address feedback and push updates
- Once approved, your contribution will be merged!

## 🐛 Reporting Issues

Found a bug? Have a suggestion? Please:

1. Check existing issues first
2. Use the appropriate issue template
3. Include:
   - Notebook name and phase
   - Python version and OS
   - Complete error message
   - Steps to reproduce

## 💡 Suggesting New Topics

We're always looking to expand! For new notebook suggestions:

1. Check if the topic exists in another phase
2. Use the "Notebook Suggestion" template
3. Explain:
   - Why this topic is important
   - Where it fits in the learning path
   - Prerequisites needed
   - Potential outline

## 🤝 Community

- Be respectful and welcoming to learners at all levels
- Provide constructive feedback
- Help others in discussions
- Share your learning journey

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

- Open a discussion on GitHub
- Check existing documentation
- Review similar notebooks for patterns

---

Thank you for helping make AI/ML education more accessible! 🚀
