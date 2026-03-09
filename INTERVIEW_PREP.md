# Interview Preparation — Zero to AI

> **15 Core ML Questions with Answers, Coding Problems, and 3 System Design Walkthroughs**

---

## Table of Contents

- [Part 1: Core ML Concept Questions (15 Q&A)](#part-1-core-ml-concept-questions)
- [Part 2: Coding Problems](#part-2-coding-problems)
- [Part 3: System Design Walkthroughs](#part-3-system-design-walkthroughs)
- [Part 4: LLM & GenAI Interview Questions](#part-4-llm--genai-interview-questions)
- [Part 5: Behavioral Questions for AI Roles](#part-5-behavioral-questions-for-ai-roles)

---

## Part 1: Core ML Concept Questions

### Q1: What is the bias-variance tradeoff?

**Answer**: Bias is error from overly simple assumptions (underfitting). Variance is error from sensitivity to training data fluctuations (overfitting). The tradeoff: reducing bias increases variance and vice versa. The goal is to find the sweet spot — a model complex enough to capture patterns but not so complex it memorizes noise.

**Follow-up**: How do you diagnose it?
- High bias: both training and validation error are high
- High variance: training error is low but validation error is high
- Fix high bias: more features, more complex model
- Fix high variance: more data, regularization, simpler model

---

### Q2: Explain the difference between L1 and L2 regularization.

**Answer**:
- **L1 (Lasso)**: Adds sum of absolute values of weights to the loss. Encourages sparsity — some weights become exactly zero. Good for feature selection.
- **L2 (Ridge)**: Adds sum of squared weights to the loss. Shrinks all weights toward zero but doesn't eliminate any. More stable when features are correlated.
- **Elastic Net**: Combines both L1 and L2.

**When to use**: L1 when you suspect many irrelevant features. L2 when most features are relevant. Elastic Net when uncertain.

---

### Q3: What is gradient descent and how does it work?

**Answer**: Gradient descent is an optimization algorithm that iteratively adjusts model parameters to minimize the loss function. It computes the gradient (partial derivatives) of the loss with respect to each parameter, then updates parameters in the opposite direction of the gradient.

**Update rule**: `w = w - learning_rate * gradient`

**Variants**:
- **Batch GD**: Uses entire dataset per step — stable but slow
- **Stochastic GD (SGD)**: Uses one sample per step — noisy but fast
- **Mini-batch GD**: Uses small batches (32-256) — best of both worlds
- **Adam**: Adaptive learning rate per parameter — most commonly used in deep learning

---

### Q4: How do you handle class imbalance?

**Answer** (in priority order):
1. **Collect more data** for minority class (if possible)
2. **Change the evaluation metric**: Use precision, recall, F1, AUC-ROC instead of accuracy
3. **Resampling**: Oversample minority (SMOTE) or undersample majority
4. **Class weights**: Tell the model to penalize misclassifying minority class more
5. **Anomaly detection**: If extreme imbalance (99.9%+), treat as anomaly detection
6. **Ensemble methods**: Bagging with balanced subsets

---

### Q5: Explain precision, recall, and F1 score.

**Answer**:
- **Precision**: Of all predicted positives, how many are actually positive? `TP / (TP + FP)`
- **Recall**: Of all actual positives, how many did we catch? `TP / (TP + FN)`
- **F1 Score**: Harmonic mean of precision and recall: `2 * (P * R) / (P + R)`

**When to prioritize**:
- Precision: When false positives are costly (spam filter — don't block real email)
- Recall: When false negatives are costly (cancer detection — don't miss a case)
- F1: When you need a balance between both

---

### Q6: What is cross-validation and why use it?

**Answer**: Cross-validation splits data into K folds, trains on K-1 folds and validates on the remaining fold, rotating K times. It gives a more robust estimate of model performance than a single train/test split.

**Types**:
- **K-Fold** (typically K=5 or 10): Standard approach
- **Stratified K-Fold**: Preserves class distribution in each fold
- **Leave-One-Out**: K = N (each sample is a fold) — expensive, low bias
- **Time Series Split**: Respects temporal order — no future data leakage

**Key point**: Never use cross-validation on the test set. Cross-validation is for model selection; the test set is for final evaluation only.

---

### Q7: Explain the Transformer architecture.

**Answer**: The Transformer processes sequences in parallel using self-attention rather than sequential processing (unlike RNNs).

**Key components**:
1. **Token embeddings**: Convert tokens to vectors
2. **Positional encoding**: Inject position information (since attention has no inherent order)
3. **Multi-head self-attention**: Each token attends to all other tokens. Multiple heads learn different relationships. Scaled dot-product: `Attention(Q,K,V) = softmax(QK^T / √d_k) V`
4. **Feed-forward network**: Two linear layers with activation (applied per position)
5. **Layer normalization + residual connections**: Stabilize training
6. **Encoder** (BERT-style): Bidirectional attention, good for understanding
7. **Decoder** (GPT-style): Causal (masked) attention, good for generation

**Why it matters**: Every modern LLM (GPT-4, Claude, Llama, Gemini) is based on Transformers.

---

### Q8: What is overfitting and how do you prevent it?

**Answer**: Overfitting occurs when a model learns noise in the training data rather than the underlying pattern. It performs well on training data but poorly on unseen data.

**Prevention techniques**:
1. **More training data** — most effective solution
2. **Regularization** — L1, L2, dropout
3. **Early stopping** — stop training when validation loss starts increasing
4. **Data augmentation** — create variations of training data
5. **Simpler model** — fewer parameters, fewer layers
6. **Cross-validation** — for more robust model selection
7. **Ensemble methods** — combine multiple models

---

### Q9: What is the difference between bagging and boosting?

**Answer**:
- **Bagging** (e.g., Random Forest): Train multiple models on random subsets of data *in parallel*. Average their predictions. Reduces variance.
- **Boosting** (e.g., XGBoost, AdaBoost): Train models *sequentially*, where each model focuses on correcting errors of the previous model. Reduces bias.

| Aspect | Bagging | Boosting |
|--------|---------|----------|
| Training | Parallel | Sequential |
| Focus | Reduce variance | Reduce bias |
| Overfitting risk | Low | Higher |
| Example | Random Forest | XGBoost, LightGBM |

---

### Q10: Explain how a Random Forest works.

**Answer**: Random Forest builds multiple decision trees and averages their predictions (regression) or takes majority vote (classification).

**Key mechanisms**:
1. **Bootstrap sampling**: Each tree gets a random subset of the training data (with replacement)
2. **Random feature selection**: At each split, only a random subset of features is considered
3. **Aggregation**: Combine predictions from all trees

**Why it works**: Individual trees overfit, but averaging many decorrelated trees reduces variance without increasing bias. Feature randomness ensures trees are different from each other.

**Hyperparameters to tune**: `n_estimators` (number of trees), `max_depth`, `min_samples_split`, `max_features`.

---

### Q11: What is a ROC curve and AUC?

**Answer**:
- **ROC curve**: Plots True Positive Rate (recall) vs. False Positive Rate at various classification thresholds
- **AUC (Area Under Curve)**: Single number summarizing the ROC curve. Ranges from 0 to 1.
  - 0.5 = random guessing
  - 0.7-0.8 = acceptable
  - 0.8-0.9 = excellent
  - >0.9 = outstanding

**When to use**: Binary classification problems, especially when you want to compare models across all possible thresholds. Not ideal for heavily imbalanced datasets (use Precision-Recall curve instead).

---

### Q12: What is the difference between supervised, unsupervised, and reinforcement learning?

**Answer**:
- **Supervised**: Learn from labeled data (input → output pairs). Examples: classification, regression.
- **Unsupervised**: Find patterns in unlabeled data. Examples: clustering, dimensionality reduction, anomaly detection.
- **Reinforcement**: Learn by taking actions in an environment and receiving rewards/penalties. Examples: game playing, robotics, recommendation tuning.

**Self-supervised** (bonus): A subset of unsupervised where the model creates its own labels from the data. Example: masked language modeling in BERT (predict masked tokens), next-token prediction in GPT.

---

### Q13: What is PCA and when would you use it?

**Answer**: Principal Component Analysis finds the directions (principal components) of maximum variance in the data and projects data onto these directions.

**When to use**:
- Dimensionality reduction (100 features → 10 components)
- Visualization (reduce to 2D or 3D)
- Noise reduction (keep only top components)
- When features are highly correlated
- Speed up training (fewer features)

**Key considerations**: PCA assumes linear relationships. For non-linear data, consider t-SNE or UMAP for visualization, or autoencoders for reduction.

---

### Q14: How does backpropagation work?

**Answer**: Backpropagation computes the gradient of the loss with respect to each weight in the network using the chain rule of calculus.

**Steps**:
1. **Forward pass**: Input flows through the network to produce a prediction
2. **Compute loss**: Compare prediction to true label
3. **Backward pass**: Compute gradients layer by layer from output to input using the chain rule
4. **Update weights**: `w = w - lr * ∂L/∂w`

**Key insight**: The chain rule allows us to efficiently compute gradients for deep networks. Each layer only needs the gradient from the layer above and its own local gradient.

---

### Q15: What is a loss function and name three common ones?

**Answer**: A loss function measures how far the model's predictions are from the true values. It's what the model optimizes during training.

**Common loss functions**:
1. **MSE (Mean Squared Error)**: For regression. Penalizes large errors more.
2. **Cross-Entropy Loss**: For classification. Measures divergence between predicted and true probability distributions.
3. **Binary Cross-Entropy**: For binary classification. Special case of cross-entropy.

**Others**: Huber Loss (robust regression), Hinge Loss (SVMs), Focal Loss (imbalanced classification), Triplet Loss (embeddings), Contrastive Loss (self-supervised learning).

---

## Part 2: Coding Problems

### Problem 1: Data Cleaning & EDA

```python
"""
Given a messy DataFrame, clean it and compute basic statistics.
Time limit: 20 minutes

Tasks:
1. Load the data
2. Handle missing values
3. Remove duplicates
4. Compute summary statistics
5. Find correlations
"""
import pandas as pd
import numpy as np

# Sample data
data = {
    'age': [25, 30, np.nan, 35, 30, 40, 25, np.nan, 50, 35],
    'salary': [50000, 60000, 70000, np.nan, 60000, 80000, 50000, 65000, 90000, np.nan],
    'department': ['eng', 'eng', 'sales', 'eng', 'eng', 'sales', 'eng', 'hr', 'sales', 'eng'],
    'rating': [4.5, 3.8, 4.2, 4.0, 3.8, 4.5, 4.5, 3.9, 4.1, 4.0]
}
df = pd.DataFrame(data)

# Solution:

# 1. Check missing values
print(df.isnull().sum())

# 2. Fill missing values
df['age'] = df['age'].fillna(df['age'].median())
df['salary'] = df['salary'].fillna(df.groupby('department')['salary'].transform('median'))

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Summary statistics
print(df.describe())
print(df.groupby('department')['salary'].agg(['mean', 'median', 'count']))

# 5. Correlation
print(df[['age', 'salary', 'rating']].corr())
```

---

### Problem 2: Train a Classifier

```python
"""
Train a classifier on the Iris dataset. Evaluate properly.
Time limit: 20 minutes

Tasks:
1. Load data, split into train/test
2. Train at least 2 models
3. Compare using appropriate metrics
4. Select the best model
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Solution:

# 1. Load and split
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 2. Train models
models = {
    'Logistic Regression': LogisticRegression(max_iter=200),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

# 3. Evaluate with cross-validation
for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    print(f"{name}: CV Accuracy = {scores.mean():.3f} (+/- {scores.std():.3f})")

# 4. Final evaluation on test set
best_model = RandomForestClassifier(n_estimators=100, random_state=42)
best_model.fit(X_train, y_train)
y_pred = best_model.predict(X_test)
print(classification_report(y_test, y_pred))
```

---

### Problem 3: Implement a Simple RAG Pipeline

```python
"""
Build a minimal RAG system (pseudocode / conceptual).
Time limit: 30 minutes

Tasks:
1. Chunk documents
2. Create embeddings
3. Store in a vector database
4. Retrieve relevant chunks for a query
5. Generate an answer using an LLM
"""
from sentence_transformers import SentenceTransformer
import chromadb

# Solution:

# 1. Prepare documents
documents = [
    "RAG combines retrieval with generation for grounded AI responses.",
    "Vector databases store embeddings for fast similarity search.",
    "Chunking strategies affect RAG quality significantly.",
    "Hybrid search combines dense and sparse retrieval.",
    "Reranking improves retrieval precision using cross-encoders.",
]

# 2. Create embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# 3. Store in ChromaDB
client = chromadb.Client()
collection = client.create_collection("demo")
collection.add(
    documents=documents,
    ids=[f"doc_{i}" for i in range(len(documents))],
)

# 4. Retrieve
query = "How does hybrid search work?"
results = collection.query(query_texts=[query], n_results=3)
context = "\n".join(results['documents'][0])

# 5. Generate (using OpenAI or any LLM)
prompt = f"""Based on the following context, answer the question.

Context:
{context}

Question: {query}

Answer:"""

# response = openai.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": prompt}]
# )
print(f"Prompt ready:\n{prompt}")
```

---

### Problem 4: Feature Engineering

```python
"""
Given raw data, create meaningful features.
Time limit: 15 minutes
"""
import pandas as pd
import numpy as np

# Raw transaction data
transactions = pd.DataFrame({
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 3, 3],
    'amount': [50, 200, 30, 500, 100, 20, 30, 40, 50, 60],
    'timestamp': pd.date_range('2026-01-01', periods=10, freq='D'),
    'category': ['food', 'electronics', 'food', 'electronics', 'food',
                 'food', 'food', 'transport', 'transport', 'food']
})

# Solution: Create aggregated user features
user_features = transactions.groupby('user_id').agg(
    total_transactions=('amount', 'count'),
    total_spent=('amount', 'sum'),
    avg_transaction=('amount', 'mean'),
    max_transaction=('amount', 'max'),
    std_transaction=('amount', 'std'),
    unique_categories=('category', 'nunique'),
    most_common_category=('category', lambda x: x.mode()[0]),
    days_active=('timestamp', lambda x: (x.max() - x.min()).days),
).reset_index()

user_features['std_transaction'] = user_features['std_transaction'].fillna(0)
print(user_features)
```

---

## Part 3: System Design Walkthroughs

### Design 1: RAG-based Document Q&A System

**Problem**: Design a system where employees can ask questions about company documents (10,000+ PDFs, wikis, Slack messages).

**Architecture**:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Ingestion   │────▶│  Processing  │────▶│   Storage    │
│  Pipeline    │     │  Pipeline    │     │              │
│              │     │              │     │  Vector DB   │
│ PDF, Wiki,   │     │ Chunk, Clean │     │  (Qdrant)    │
│ Slack export │     │ Embed        │     │              │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                  │
                                                  ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Frontend   │────▶│   API Layer  │────▶│  Retrieval + │
│  (Streamlit) │     │  (FastAPI)   │     │  Generation  │
│              │◀────│              │◀────│  (LLM)       │
└──────────────┘     └──────────────┘     └──────────────┘
```

**Key decisions**:
1. **Chunking**: Recursive text splitter, 512 tokens, 50-token overlap. Preserve document metadata.
2. **Embedding model**: `text-embedding-3-small` (API) or `all-mpnet-base-v2` (local). Choice depends on privacy requirements.
3. **Vector DB**: Qdrant for production (fast, scalable). ChromaDB for prototype.
4. **Retrieval**: Hybrid search (dense + BM25) with cross-encoder reranking. Top 5 chunks.
5. **LLM**: GPT-4o-mini for cost efficiency. Instruct it to cite sources.
6. **Caching**: Cache frequent queries + responses in Redis. Cache embeddings.
7. **Evaluation**: RAGAS metrics (faithfulness, answer relevancy, context precision).

**Scaling considerations**:
- Batch embedding jobs for new documents (async queue)
- Rate limiting on LLM API calls
- Incremental indexing (don't re-embed unchanged documents)

---

### Design 2: Real-time Recommendation System

**Problem**: Design a recommendation engine for an e-commerce platform with 10M users and 1M products.

**Architecture**:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Data Layer  │     │  Training    │     │  Serving     │
│              │     │  Pipeline    │     │  Layer       │
│ Clickstream  │────▶│              │────▶│              │
│ Purchases    │     │ Collaborative│     │ FastAPI +    │
│ User profile │     │ Filtering    │     │ Redis Cache  │
└──────────────┘     └──────────────┘     └──────────────┘
```

**Key decisions**:
1. **Two-stage approach**: Candidate generation (fast, broad) → Ranking (slower, precise)
2. **Candidate generation**: Approximate nearest neighbors using user/item embeddings (FAISS or Qdrant)
3. **Ranking model**: Gradient boosted trees (XGBoost) on features: user history, item features, context
4. **Real-time features**: Last 10 interactions, session context, time of day
5. **Cold start**: Content-based features for new users/items; popular items as fallback
6. **A/B testing**: Route 5% traffic to new model, measure CTR and conversion
7. **Infrastructure**: Feature store (Feast), model registry (MLflow), serving (FastAPI + Redis)

**Latency budget**: < 100ms total (50ms candidate retrieval, 30ms ranking, 20ms overhead)

---

### Design 3: LLM-powered Customer Support Agent

**Problem**: Build an AI agent that handles customer support queries, can look up orders, process returns, and escalate to humans.

**Architecture**:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Customer   │────▶│  Agent       │────▶│   Tools      │
│   Interface  │     │  Orchestrator│     │              │
│  (Chat UI)   │◀────│  (LangGraph) │◀────│ Order DB     │
│              │     │              │     │ Return API   │
└──────────────┘     └──────────────┘     │ FAQ RAG      │
                                          │ Escalation   │
                                          └──────────────┘
```

**Key decisions**:
1. **Agent framework**: LangGraph for stateful workflow with explicit state transitions
2. **Tools**: `lookup_order(order_id)`, `process_return(order_id, reason)`, `search_faq(query)`, `escalate_to_human(reason)`
3. **Memory**: Conversation history in context (last 10 turns) + user profile from DB
4. **Guardrails**: Content moderation filter on input/output. PII detection and redaction. Rate limiting.
5. **Escalation triggers**: User requests human, agent confidence low, sensitive topics, 3+ failed tool calls
6. **Evaluation**: Track resolution rate, escalation rate, customer satisfaction, average handle time
7. **LLM choice**: GPT-4o-mini for cost (high volume). Claude 3.5 Sonnet for complex reasoning cases.

**Safety considerations**:
- Never expose internal system details in responses
- Confirm destructive actions (refunds, cancellations) before executing
- Log all agent actions for audit trail
- Human-in-the-loop for actions above $X threshold

---

## Part 4: LLM & GenAI Interview Questions

### Q1: When would you use RAG vs. fine-tuning vs. prompt engineering?

**Answer**:
- **Prompt engineering first**: When the model already knows the domain. Cheapest and fastest.
- **RAG**: When you need factual accuracy from specific documents. The model needs access to your data.
- **Fine-tuning**: When you need the model to learn a specific style, format, or behavior that can't be achieved with prompting or RAG. Most expensive and slowest.

**Decision flow**: Try prompting → add RAG if hallucinations → fine-tune if style/format still wrong.

### Q2: Explain the RAG pipeline end-to-end.

**Answer**: Document → Chunk → Embed → Store in vector DB → User query → Embed query → Retrieve similar chunks → Rerank → Construct prompt with context → LLM generates answer → Return with citations.

**Key failure points**: Bad chunking, wrong embedding model, too many/few retrieved chunks, no reranking, poor prompt construction.

### Q3: What is LoRA and why is it useful?

**Answer**: Low-Rank Adaptation freezes the pre-trained model weights and injects small trainable matrices (adapters) into each layer. Instead of training all N billion parameters, you train only ~2-5% of parameters.

**Benefits**: Much less GPU memory (QLoRA: 4-bit base model + LoRA = 4-6GB for 7B model), faster training, easy to swap adapters for different tasks, same base model can serve multiple use cases.

### Q4: How do you evaluate a RAG system?

**Answer**: Use the RAGAS framework:
- **Faithfulness**: Is the answer grounded in the retrieved context?
- **Answer relevancy**: Does the answer address the question?
- **Context precision**: Are the retrieved documents relevant?
- **Context recall**: Did we retrieve all the necessary documents?

Also measure: latency, cost per query, and user satisfaction.

### Q5: What are AI agents and what makes them reliable?

**Answer**: AI agents are LLM-based systems that can plan, use tools, and take multi-step actions. They use the ReAct pattern (Reasoning → Action → Observation → Repeat).

**Reliability strategies**: Structured outputs (JSON schemas), explicit error handling per tool, retry with backoff, human-in-the-loop for high-stakes actions, comprehensive logging, evaluation on test scenarios.

---

## Part 5: Behavioral Questions for AI Roles

### "Tell me about a challenging ML project."

**Framework** (STAR method):
- **Situation**: What was the business problem?
- **Task**: What was your role?
- **Action**: What did you build? What technical decisions did you make?
- **Result**: What was the outcome? Quantify if possible.

### "How do you stay current in AI?"

**Good answer**: "I follow key researchers on Twitter/X (Andrej Karpathy, Lilian Weng), read papers from NeurIPS/ICML, participate in r/MachineLearning and r/LocalLLaMA, and build small projects to test new tools. For example, when MCP was released, I built a prototype agent using it within a week."

### "How do you handle disagreements about technical approach?"

**Good answer**: "I focus on data and experiments. If someone prefers approach A and I prefer approach B, I suggest we define success metrics upfront and run a quick experiment to compare. The data decides, not opinions."

### "Describe a time you had to explain a complex ML concept to a non-technical audience."

**Good answer**: Use the Feynman technique — explain in simple analogies. Example: "I explained RAG to our product team by comparing it to a student taking an open-book exam. The student (LLM) is smart but might misremember facts. The textbook (retrieved documents) provides accurate reference material. RAG = smart student + open book."

---

## Study Plan for Interviews

### Week 1: Foundations
- [ ] Review all 15 concept questions above
- [ ] Solve coding problems 1-4
- [ ] Practice explaining Transformers in 2 minutes

### Week 2: System Design
- [ ] Walk through all 3 system designs
- [ ] Practice drawing architecture diagrams
- [ ] Time yourself: 35 minutes per design (5 min requirements, 10 min high-level, 15 min deep dive, 5 min scaling)

### Week 3: Mock Practice
- [ ] Do a mock interview with a friend or AI
- [ ] Record yourself answering behavioral questions
- [ ] Practice coding on a shared screen (no IDE autocomplete)

---

## Key Resources

| Need | Go To |
|------|-------|
| Career strategy | [CAREER_ROADMAP.md](CAREER_ROADMAP.md) |
| Learning plan | [MASTER_STUDY_GUIDE.md](MASTER_STUDY_GUIDE.md) |
| Tool comparisons | [COMPARISON_MATRICES.md](COMPARISON_MATRICES.md) |
| Practice notebooks | [28-practical-data-science/](28-practical-data-science/) |

---

*Last Updated: March 2026*
*Repository: [zero-to-ai](https://github.com/PavanMudigonda/zero-to-ai)*