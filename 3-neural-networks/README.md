# Phase 3: Neural Networks & Transformers

**Learning Time:** 4-6 weeks | **Difficulty:** Intermediate

## What You'll Learn

By the end of this module, you will understand:

- ✅ How neural networks learn from data
- ✅ Forward and backward propagation
- ✅ The attention mechanism (core innovation of transformers)
- ✅ Transformer architecture (the "T" in ChatGPT)
- ✅ How modern LLMs process and generate text
- ✅ Practical implementation with PyTorch

## Quick Start

```bash
# Install required packages
pip install torch torchvision numpy matplotlib transformers

# Run examples in order
python 1_neural_network_basics.py      # 10-15 min
python 2_backpropagation_demo.py       # 15-20 min
python 3_attention_mechanism.py        # 20-25 min
python 4_transformer_basics.py         # 25-30 min
python 5_fine_tune_transformer.py      # 30-40 min
```

## Files in This Module

| File | Description | Run Time |
|------|-------------|----------|
| `intro.md` | Comprehensive theory and concepts | Read: 30-40 min |
| `attention_explained.md` | Deep dive into attention mechanism | Read: 20-30 min |
| `transformer_architecture.md` | Transformer explained step-by-step | Read: 25-35 min |
| `1_neural_network_basics.py` | Build neural network from scratch | 10-15 min |
| `2_backpropagation_demo.py` | Understand how networks learn | 15-20 min |
| `3_attention_mechanism.py` | Implement attention from scratch | 20-25 min |
| `4_transformer_basics.py` | Transformer components | 25-30 min |
| `5_fine_tune_transformer.py` | Practical fine-tuning example | 30-40 min |
| `exercises.py` | Interactive practice problems | 20-30 min |

## Learning Path

### The Journey So Far

```
Phase 1: Tokenization ✅
    ↓ (Text → Token IDs)
Phase 2: Embeddings ✅
    ↓ (Token IDs → Dense Vectors)
Phase 3: Neural Networks ← YOU ARE HERE
    ↓ (Vectors → Intelligence)
```

### Step 1: Understand Neural Network Basics (Week 1)

**Read:** `intro.md` - Neural network fundamentals

**Watch:** 
- [3Blue1Brown Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) (ESSENTIAL)
- Focus on: neurons, activation functions, layers

**Practice:**
```bash
python 1_neural_network_basics.py
```
Build a simple neural network from scratch using only NumPy.

### Step 2: Master Backpropagation (Week 1-2)

**Read:** Section on backpropagation in `intro.md`

**Watch:**
- [3Blue1Brown Backpropagation](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
- [Andrej Karpathy: Micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0)

**Practice:**
```bash
python 2_backpropagation_demo.py
```
Implement gradient descent and see how networks learn.

### Step 3: Learn PyTorch/TensorFlow (Week 2-3)

**Read:** PyTorch sections in examples

**Resources:**
- [PyTorch 60min Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
- [PyTorch for Deep Learning](https://www.learnpytorch.io/)

**Practice:**
- Reimplement previous examples using PyTorch
- Train on MNIST or similar datasets

### Step 4: Understand Attention Mechanism (Week 3-4)

**Read:** `attention_explained.md` - The breakthrough innovation

**Watch:**
- [Illustrated Attention](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)
- [StatQuest Attention](https://www.youtube.com/watch?v=PSs6nxngL6k)

**Practice:**
```bash
python 3_attention_mechanism.py
```
Implement self-attention from scratch and visualize attention weights.

### Step 5: Master Transformer Architecture (Week 4-5)

**Read:** `transformer_architecture.md` - Complete architecture breakdown

**Watch:**
- [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [Andrej Karpathy: Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY)

**Practice:**
```bash
python 4_transformer_basics.py
```
Build transformer components and understand the complete architecture.

### Step 6: Practical Application (Week 5-6)

**Practice:**
```bash
python 5_fine_tune_transformer.py
```
Fine-tune a pre-trained transformer on a real task.

**Projects:**
- Text classification with BERT
- Sentiment analysis
- Named entity recognition
- Simple text generation

## Key Concepts

### Neural Network Fundamentals

**What is a Neural Network?**

A neural network is a mathematical function that learns patterns from data:

```
Input → [Hidden Layers] → Output
  x   →  [Weights & Biases] →  ŷ
```

**Components:**
- **Neurons**: Basic computation units
- **Weights**: Learnable parameters (the "knowledge")
- **Biases**: Learnable offsets
- **Activation Functions**: Non-linearity (ReLU, Sigmoid, Tanh)
- **Loss Function**: Measures prediction error
- **Optimizer**: Updates weights (SGD, Adam)

### The Learning Process

```python
for epoch in range(num_epochs):
    # 1. Forward Pass
    predictions = model(inputs)
    
    # 2. Calculate Loss
    loss = loss_function(predictions, targets)
    
    # 3. Backward Pass (compute gradients)
    loss.backward()
    
    # 4. Update Weights
    optimizer.step()
    optimizer.zero_grad()
```

### Attention Mechanism ⭐

**The Game Changer**

Before attention: Models struggled with long sequences
After attention: Models can focus on relevant parts of input

**Key Innovation:**
Instead of compressing entire sequence into fixed vector, attention allows model to "look at" different parts with different weights.

```
"The cat sat on the mat"

When predicting "sat":
- High attention to: "cat" (subject)
- Medium attention to: "The", "on", "the", "mat"
- This context helps understand the sentence
```

**Self-Attention Formula:**

```
Attention(Q, K, V) = softmax(QK^T / √d_k) V

Where:
- Q = Query (what am I looking for?)
- K = Key (what do I contain?)
- V = Value (what do I output?)
```

### Transformer Architecture

**Core Components:**

1. **Multi-Head Attention**: Multiple attention mechanisms in parallel
2. **Feed-Forward Networks**: Process attention output
3. **Layer Normalization**: Stabilize training
4. **Residual Connections**: Help gradients flow
5. **Positional Encoding**: Add sequence position information

**Three Types:**

| Type | Architecture | Examples | Use Case |
|------|-------------|----------|----------|
| Encoder-only | Stacked encoders | BERT, RoBERTa | Understanding (classification, NER) |
| Decoder-only | Stacked decoders | GPT, LLaMA | Generation (text completion, chat) |
| Encoder-Decoder | Both | T5, BART | Translation, summarization |

## Common Pitfalls

### ❌ Mistake 1: Not understanding backpropagation
**Problem:** Treating neural networks as black boxes

**Solution:** Implement backpropagation from scratch at least once. Understand how gradients flow through the network.

### ❌ Mistake 2: Skipping attention mechanism
**Problem:** Jumping straight to using transformers without understanding attention

**Solution:** Study attention mechanism in isolation. Implement it from scratch. Visualize attention weights.

### ❌ Mistake 3: Overfitting on small datasets
**Problem:** Model memorizes training data, fails on new data

**Solution:**
- Use regularization (dropout, weight decay)
- Early stopping
- Data augmentation
- Start with pre-trained models

### ❌ Mistake 4: Wrong learning rate
**Problem:** Too high = unstable training, Too low = slow/stuck

**Solution:**
- Start with 1e-3 or 3e-4
- Use learning rate schedulers
- Monitor loss curves

### ❌ Mistake 5: Ignoring computational costs
**Problem:** Training huge models without considering resources

**Solution:**
- Start small, scale up gradually
- Use gradient accumulation for large batches
- Consider model size vs. available GPU memory

## Architecture Evolution

### Timeline of Key Innovations

```
2012: AlexNet → Deep learning revolution begins
2014: GRU/LSTM → Handle sequential data
2015: ResNet → Very deep networks (residual connections)
2017: Transformer → "Attention is All You Need" ⭐
2018: BERT → Bidirectional transformers
2018: GPT → Generative pre-training
2019: GPT-2 → Scaled up language models
2020: GPT-3 → 175B parameters
2022: ChatGPT → Conversational AI
2023: GPT-4 → Multimodal transformers
2024+: Mixture of Experts, Efficient transformers
```

### Why Transformers Won

**Problems with RNNs/LSTMs:**
- ❌ Sequential processing (slow)
- ❌ Vanishing gradients on long sequences
- ❌ Can't parallelize training
- ❌ Limited context window

**Transformers' Advantages:**
- ✅ Parallel processing (fast training)
- ✅ Long-range dependencies via attention
- ✅ Scales to massive datasets
- ✅ Transfer learning (pre-train once, fine-tune for many tasks)

## Practical Applications

### 1. Text Classification
```python
from transformers import pipeline

classifier = pipeline("text-classification", 
                     model="distilbert-base-uncased-finetuned-sst-2-english")
result = classifier("I love this tutorial!")
# Output: [{'label': 'POSITIVE', 'score': 0.9998}]
```

### 2. Named Entity Recognition (NER)
```python
ner = pipeline("ner", model="dslim/bert-base-NER")
result = ner("Apple Inc. is located in Cupertino, California.")
# Identifies: Apple Inc. (ORG), Cupertino (LOC), California (LOC)
```

### 3. Question Answering
```python
qa = pipeline("question-answering")
result = qa(question="What is the capital of France?",
           context="Paris is the capital and largest city of France.")
# Output: "Paris"
```

### 4. Text Generation
```python
generator = pipeline("text-generation", model="gpt2")
result = generator("Once upon a time", max_length=50)
```

## Practice Exercises

Work through `exercises.py` to test your understanding:

1. **Implement XOR Gate** - Build network that learns XOR function
2. **Gradient Descent Visualization** - See how optimization works
3. **Attention Weight Analysis** - Visualize what model focuses on
4. **Build Mini-Transformer** - Implement simplified transformer
5. **Fine-tune for Classification** - Real-world task

## Verification Checklist

Before moving to Phase 4 (LLMs & Applications), ensure you can:

- [ ] Explain forward and backward propagation
- [ ] Implement a simple neural network from scratch
- [ ] Understand gradient descent and optimization
- [ ] Explain the attention mechanism in your own words
- [ ] Describe transformer architecture components
- [ ] Use PyTorch to build and train models
- [ ] Fine-tune a pre-trained transformer
- [ ] Visualize attention weights
- [ ] Understand positional encoding
- [ ] Know the difference between encoder-only, decoder-only, and encoder-decoder models

## Deep Dive Resources

### Essential Reading

**Papers (Read in this order):**
1. [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Original transformer paper
2. [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805)
3. [GPT-3: Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)

**Blogs:**
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html)
- [Attention? Attention!](https://lilianweng.github.io/posts/2018-06-24-attention/)

### Video Courses

**Must Watch:**
- [3Blue1Brown: Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) ⭐⭐⭐
- [Andrej Karpathy: Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
- [Stanford CS224N: NLP with Deep Learning](https://www.youtube.com/playlist?list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ)

**Supplementary:**
- [StatQuest: Neural Networks](https://www.youtube.com/watch?v=CqOfi41LfDw&list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1)
- [FastAI: Practical Deep Learning](https://course.fast.ai/)

### Interactive Tools

- [TensorFlow Playground](https://playground.tensorflow.org/) - Visualize neural networks
- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) - Interactive transformer
- [Attention Visualizer](https://github.com/jessevig/bertviz) - BertViz tool

## Common Questions

**Q: Do I need to implement everything from scratch?**  
A: Implement basics (simple network, backprop, attention) from scratch once to understand. Then use PyTorch/TensorFlow for real work.

**Q: Should I learn PyTorch or TensorFlow?**  
A: PyTorch is more popular in research and has better community support. Start with PyTorch.

**Q: How much math do I need?**  
A: Basics: linear algebra (matrix multiplication), calculus (derivatives), probability. You don't need to be a math expert, but understand the concepts.

**Q: Can I train transformers on my laptop?**  
A: Small models (BERT-tiny, DistilBERT) yes. Large models (GPT-3) no - use cloud platforms (Colab, AWS, Hugging Face).

**Q: What's the difference between BERT and GPT?**  
A: BERT (encoder) is for understanding tasks (classification, NER). GPT (decoder) is for generation (text completion, chat).

**Q: How do I choose model size?**  
A: Start small, scale up if needed. Base models (110M-340M params) work for most tasks. Large models (>1B) for complex tasks or when you have lots of data.

## Project Ideas

### Beginner Projects

1. **Digit Classifier** - MNIST with simple neural network
2. **Sentiment Analyzer** - Fine-tune BERT on movie reviews
3. **Name Classifier** - Predict nationality from name

### Intermediate Projects

4. **Text Summarizer** - Fine-tune T5 or BART
5. **Question Answering System** - Fine-tune on SQuAD dataset
6. **Code Completion** - Fine-tune GPT on code dataset
7. **Spam Detector** - Classification with transformers

### Advanced Projects

8. **Multi-label Classifier** - Classify news into multiple categories
9. **Named Entity Recognition** - Build custom NER for specific domain
10. **Translation System** - Fine-tune encoder-decoder transformer
11. **Chatbot** - Build retrieval-based or generative chatbot

## Next Steps

Once you're comfortable with neural networks and transformers, move to **Phase 4: LLMs & Modern AI**:

```bash
cd ../4-llms-modern-ai
cat README.md
```

**Phase 4 Preview:** 
- GPT architecture deep dive
- Prompt engineering techniques
- Fine-tuning strategies (LoRA, QLoRA)
- RAG (Retrieval-Augmented Generation)
- LangChain and LlamaIndex
- Building production LLM applications
- Vector databases for LLMs
- Agent frameworks

---

**Need Help?**
- Review markdown files for detailed theory
- Run examples with different parameters
- Complete interactive exercises
- Join communities: r/MachineLearning, Hugging Face forums
- Ask questions in Discord servers: FastAI, PyTorch

**Study Tips:**
- Don't rush - understanding > speed
- Implement concepts yourself before using libraries
- Visualize what's happening (attention weights, gradients)
- Build projects - best way to learn
- Review Phase 1 & 2 if concepts feel unclear
