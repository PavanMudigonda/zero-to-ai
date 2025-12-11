# learning path
## 🎯 Your Current Position

**Phase 1 - Foundation** [ ] (You've completed tokenization basics)  
**Phase 2 - Embeddings & Vectors** 🎯 (You are here - working on embeddings)  
**Phase 3 - Neural Networks & Transformers** ⏭️ (Coming next)  
**Phase 4 - LLMs & Applications** 🔜 (Advanced topics)

---

## 📚 Phase 1: Foundation (2-3 months | 200-300 hours)

> **Goal**: Build mathematical and programming foundations essential for ML
> **Prerequisites**: Basic programming knowledge
> **Outcome**: Ready to understand ML algorithms and implement them

### Core Topics Checklist

**Core Concepts**

- [ ] Artificial Intelligence (AI)
- [ ] Machine Learning (ML)
- [ ] Supervised / Unsupervised / Semi‑Supervised Learning
- [ ] Reinforcement Learning (RL)
- [ ] Offline vs Online Machine Learning
- [ ] Overfitting, Underfitting, Bias, Variance

**Math & Statistics Basics**

- [ ] Loss Functions (Cross‑Entropy, Mean Squared Error)
- [ ] Optimization (gradients, backpropagation basics)
- [ ] L1 Norm, L2 Norm, Regularisation
- [ ] Probability (Naïve Bayes, distributions)

**Data Fundamentals**

- [ ] Features, Labels, Annotation
- [ ] Training/Validation/Testing Sets
- [ ] Feature Engineering & Feature Extraction
- [ ] Normalisation

### 📖 Required Resources (Phase 1)

**Mathematics (80-120 hours)**

- [ ] **[3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)** (~8 hours) ⭐ ESSENTIAL
  - Visual intuition for vectors, matrices, transformations
- [ ] **[3Blue1Brown - Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)** (~6 hours) ⭐ ESSENTIAL
  - Derivatives, integrals, chain rule
- [ ] **[Gilbert Strang - MIT Linear Algebra 18.06](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8)** (~35 hours)
  - Deep dive into linear algebra theory
- [ ] **[Khan Academy](https://www.khanacademy.org/)** - Statistics, Probability, Calculus (30-50 hours)
  - Fill gaps in mathematical knowledge

**Programming (40-60 hours)**

- [ ] **[Python for Beginners - Microsoft](https://github.com/microsoft/c9-python-getting-started)** (10-15 hours)
- [ ] **NumPy, Pandas basics** (20-30 hours)
  - [NumPy Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
  - [Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
- [ ] **Matplotlib/Seaborn for visualization** (10-15 hours)

**ML Fundamentals (80-120 hours)**

- [ ] **[Andrew Ng - Machine Learning Specialization](https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)** (60-80 hours) ⭐ ESSENTIAL
  - Course 1: Supervised ML (Regression, Classification)
  - Course 2: Advanced Learning Algorithms
  - Course 3: Unsupervised Learning, Recommenders, RL
- [ ] **[ISLP Book](https://www.statlearning.com/)** - Introduction to Statistical Learning with Python (40-60 hours)
  - Read chapters 1-8 (linear regression through tree-based methods)

### 🎯 Phase 1 Projects

- [ ] **Project 1**: Linear regression on housing prices (Boston/California dataset)
- [ ] **Project 2**: Classification with logistic regression (Iris/Titanic)
- [ ] **Project 3**: K-means clustering on customer segmentation
- [ ] **Project 4**: Decision tree for loan approval prediction

### ✅ Phase 1 Completion Criteria

Before moving to Phase 2, you should be able to:

- [ ] Explain gradient descent and backpropagation conceptually
- [ ] Implement linear/logistic regression from scratch in NumPy
- [ ] Use scikit-learn for basic ML tasks
- [ ] Understand train/validation/test splits and cross-validation
- [ ] Read and understand mathematical notation in ML papers (basic level)

---

## 📚 Phase 2: Embeddings & Vectors (3-4 weeks | 60-80 hours)

> **Goal**: Understand vector representations and semantic search
> **Prerequisites**: Phase 1 complete
> **Outcome**: Build RAG systems and work with embeddings

### Core Topics Checklist

**Tokenization**

- [ ] Tokens - Text broken into processable units
- [ ] Tokenization algorithms (BPE, WordPiece, SentencePiece)
- [ ] Subword tokenization concepts

**Embeddings** 🔥

- [ ] Embeddings - Dense vector representations
- [ ] Word2Vec, fastText, Doc2Vec
- [ ] Semantic meaning in vector space
- [ ] Cosine Similarity - Measuring semantic similarity
- [ ] Vector operations (addition, subtraction, distance)

**Vector Storage & Retrieval**

- [ ] Vector Database (Pinecone, Weaviate, ChromaDB)
- [ ] Semantic search vs keyword search
- [ ] Nearest neighbor search (FAISS, HNSW)
- [ ] Dimensionality (384, 768, 1536 dimensions)

**Text Representations (Classical)**

- [ ] Bag of Words, N‑grams (Bigrams, Trigrams)
- [ ] TF (Term Frequency), IDF (Inverse Document Frequency)
- [ ] TF‑IDF weighting

### 📖 Required Resources (Phase 2)

**Core Learning (30-40 hours)**

- [ ] **[Word2Vec Paper](https://arxiv.org/abs/1301.3781)** - Original embeddings paper (3-4 hours)
- [ ] **[Jay Alammar - Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/)** (1 hour)
- [ ] **[Sentence Transformers Documentation](https://www.sbert.net/)** (5-10 hours)
  - Learn modern embedding models
- [ ] **Hugging Face - [Embeddings Course](https://huggingface.co/learn/nlp-course/)** (Chapter 5) (10-15 hours)

**Vector Databases (15-20 hours)**

- [ ] **[Pinecone Documentation](https://docs.pinecone.io/)** (5-8 hours)
- [ ] **[ChromaDB Tutorial](https://docs.trychroma.com/)** (3-5 hours)
- [ ] **[FAISS Tutorial](https://github.com/facebookresearch/faiss/wiki)** (5-7 hours)

**Practical Implementation (15-20 hours)**

- [ ] Build semantic search engine with sentence-transformers
- [ ] Create vector database with ChromaDB or Pinecone
- [ ] Implement similarity search and ranking

### 🎯 Phase 2 Projects

- [ ] **Project 1**: Semantic search engine for your documents
- [ ] **Project 2**: Question-answering with document retrieval
- [ ] **Project 3**: Duplicate detection using embeddings
- [ ] **Project 4**: Text clustering and visualization with t-SNE/UMAP

### ✅ Phase 2 Completion Criteria

- [ ] Generate embeddings using sentence-transformers
- [ ] Build and query a vector database
- [ ] Implement semantic search from scratch
- [ ] Understand cosine similarity vs. Euclidean distance
- [ ] Explain difference between sparse (TF-IDF) and dense (embeddings) representations

---

## 📚 Phase 3: Neural Networks & Architecture (2-3 months | 200-300 hours)

**Neural Network Basics**

- [ ] Neural Networks, Hidden Layers
- [ ] Activation Functions (ReLU, sigmoid, tanh)
- [ ] Backpropagation (in depth)
- [ ] Gradient descent & optimization
- [ ] Epoch, Batch Size, Learning rate
- [ ] Dropout, Regularization techniques

**Deep Learning Architectures**

- [ ] Deep Learning fundamentals
- [ ] CNNs (Convolutional Neural Networks) - for images
- [ ] RNNs (Recurrent Neural Networks) - for sequences
- [ ] LSTMs (Long Short-Term Memory) - for long sequences
- [ ] Autoencoders - dimensionality reduction

**Attention & Transformers** 🌟

- [ ] Attention Mechanism - focusing on relevant parts
- [ ] Self-Attention - all tokens attend to each other
- [ ] Multi-Head Attention - multiple attention in parallel
- [ ] Transformer Architecture - the foundation of modern NLP
- [ ] Encoder-Decoder Architecture
- [ ] Positional Encoding

---

## Phase 4: LLMs & Modern AI 🚀

**Large Language Models**

- [ ] LLMs (Large Language Models) - GPT, Claude, LLaMA
- [ ] GPT (Generative Pre-trained Transformer)
- [ ] BERT (Bidirectional Encoder Representations)
- [ ] Foundation Models - pre-trained models
- [ ] Context Window - token limits
- [ ] Perplexity - model evaluation

**Working with LLMs**

- [ ] Prompt Engineering - crafting effective prompts
- [ ] Temperature - controlling randomness
- [ ] Few-Shot / One-Shot / Zero-Shot Learning
- [ ] In-Context Learning
- [ ] Chain-of-Thought (CoT) prompting
- [ ] Instruction Tuning

**Fine-tuning & Optimization**

- [ ] Transfer Learning
- [ ] Fine-tuning pre-trained models
- [ ] LoRA (Low-Rank Adaptation) - efficient fine-tuning
- [ ] Quantization - 4-bit, 8-bit model compression
- [ ] Distillation - creating smaller models
- [ ] RLHF (Reinforcement Learning from Human Feedback)

**RAG & Knowledge Systems**

- [ ] RAG (Retrieval Augmented Generation) 🔥
- [ ] Information Retrieval (IR)
- [ ] Semantic search with embeddings
- [ ] Combining retrieval + generation
- [ ] Knowledge Graphs

---

## Phase 5: Specialized Domains

**Natural Language Processing (NLP)**

- [ ] NLP fundamentals
- [ ] Named Entity Recognition (NER)
- [ ] Sentiment Classification
- [ ] Machine Translation (MT)
- [ ] Sequence‑to‑Sequence (Seq2Seq)
- [ ] Abstractive vs Extractive Summarisation
- [ ] Natural Language Generation (NLG)
- [ ] Chatbots & conversational AI

**Computer Vision (CV)**

- [ ] Computer Vision concepts
- [ ] CNN applications (classification, detection)
- [ ] Image embeddings (CLIP)
- [ ] Stable Diffusion - text-to-image
- [ ] Diffusion Models
- [ ] GANs (Generative Adversarial Networks)
- [ ] Multimodal AI - text + vision

**Advanced Topics**

- [ ] AI Agents - autonomous decision-making
- [ ] Mixture of Experts (MoE)
- [ ] Active Learning
- [ ] Recommender Systems
- [ ] Anomaly Detection
- [ ] Human in the Loop (HITL) systems

---

## Phase 6: ML Engineering & Production

**Model Evaluation**

- [ ] Accuracy, Precision, Recall, F1 Score
- [ ] Cross‑Validation
- [ ] Confusion Matrix
- [ ] BLEU, ROUGE (for generation tasks)

**Data Engineering**

- [ ] Data pipelines
- [ ] ETL (Extract, Transform, Load)
- [ ] Data versioning
- [ ] Batch vs streaming processing

**ML Tools & Libraries**

- [ ] NumPy - numerical computing
- [ ] Pandas - data manipulation
- [ ] Scikit‑Learn - classical ML
- [ ] PyTorch / TensorFlow / Keras - deep learning
- [ ] Hugging Face Transformers
- [ ] LangChain - LLM applications

**MLOps & Deployment**

- [ ] ML Pipelines (Kedro, Airflow)
- [ ] Model versioning & monitoring
- [ ] Cloud platforms (AWS SageMaker, Azure ML, GCP)
- [ ] API deployment (FastAPI, Flask)
- [ ] Model serving & inference optimization
- [ ] A/B testing

---

## Phase 7: Ethics, Safety & Advanced Concepts

**AI Safety & Alignment**

- [ ] Hallucination - factual accuracy issues
- [ ] Alignment - matching human values
- [ ] Constitutional AI
- [ ] Prompt Injection - security concerns
- [ ] Bias & fairness in AI
- [ ] Explainability & interpretability

**Model Types Comparison**

- [ ] Generative vs Discriminative models
- [ ] Supervised vs Unsupervised vs RL
- [ ] Rules‑Based vs ML-based systems
- [ ] Classical ML vs Deep Learning tradeoffs

---

## 📚 Learning Resources by Phase

**Phase 1-2 (Foundation + Embeddings):**

- [ ] Start with your current examples: `tiktoken_example.py`, `embeddings_intro.py`
- [ ] Practice: Create embeddings for different texts, compare similarities
- [ ] Build: Simple semantic search with your own documents

**Phase 3 (Neural Networks):**

- [ ] Implement: Simple neural network from scratch
- [ ] Study: 3Blue1Brown neural network series
- [ ] Practice: MNIST digit classification with PyTorch

**Phase 4 (LLMs):**

- [ ] Use: OpenAI API, Anthropic Claude, or local LLMs
- [ ] Build: RAG system with your own knowledge base
- [ ] Practice: Prompt engineering for different tasks

**Phase 5+ (Specialization):**

- [ ] Choose your focus: NLP, CV, or multimodal
- [ ] Build end-to-end projects
- [ ] Contribute to open source (Hugging Face, LangChain)
