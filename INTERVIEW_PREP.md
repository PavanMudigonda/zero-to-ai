# Interview Preparation Guide — AI/ML Engineering

> Answers included. Study the answer, then practice explaining it in your own words out loud. That's the real test.

---

## Part 1: ML Concepts — Questions with Answers

### Foundations

**Q1: Explain the bias-variance tradeoff.**

> A high-bias model (underfit) is too simple — it misses patterns in training data and performs poorly everywhere. A high-variance model (overfit) learns the noise — it performs great on training data but poorly on new data. The goal is to find the sweet spot. In practice: start simple (linear model), then add complexity only if needed. Regularization (L1/L2) reduces variance. More data reduces variance. Better features reduce bias.

**Q2: What is the difference between L1 and L2 regularization?**

> Both penalize large weights to reduce overfitting. L2 (Ridge) adds the sum of squared weights to the loss — it pushes all weights toward zero but rarely to exactly zero. L1 (Lasso) adds the sum of absolute weights — it tends to push some weights to exactly zero, effectively doing feature selection. Use L1 when you suspect many features are irrelevant. Use L2 otherwise. ElasticNet combines both.

**Q3: Explain precision, recall, and F1. When would you optimize for precision vs recall?**

> - **Precision** = of all positive predictions, how many were actually positive. Minimize false positives.
> - **Recall** = of all actual positives, how many did we catch. Minimize false negatives.
> - **F1** = harmonic mean of precision and recall. Use when you care about both equally.
>
> Optimize for **precision** when false positives are costly: spam detection (don't block real emails), fraud detection in a high-value system (don't block real transactions).
>
> Optimize for **recall** when false negatives are costly: cancer screening (don't miss sick patients), security threat detection (don't miss attacks).

**Q4: What is gradient descent and why does learning rate matter?**

> Gradient descent minimizes the loss function by iteratively moving in the direction of the negative gradient (steepest descent). The learning rate controls step size. Too high: overshoots the minimum, training diverges. Too low: takes forever, may get stuck in local minima. In practice, use learning rate schedulers (cosine decay, warmup) or adaptive optimizers (Adam, AdamW) which adjust the learning rate per parameter.

**Q5: Explain cross-validation. Why is it better than a single train/test split?**

> Cross-validation (k-fold) divides data into k parts, trains on k-1 parts, tests on the remaining 1, and repeats k times. Average the results. This gives a more reliable estimate of model performance because every data point is used for both training and testing. A single train/test split is noisy — you might get lucky or unlucky with your split. Use k=5 or k=10 in practice.

---

### Models

**Q6: How does a Random Forest work? Why is it better than a single decision tree?**

> A Random Forest trains many decision trees, each on a random subset of the training data (bagging) and using a random subset of features at each split. Final prediction is the majority vote (classification) or average (regression). It's better because: (1) individual trees overfit, but averaging many overfit trees cancels out the variance, (2) random feature subsets make the trees uncorrelated, maximizing the benefit of averaging.

**Q7: What is gradient boosting and how does it differ from Random Forest?**

> Gradient boosting also builds an ensemble of trees, but sequentially — each tree corrects the errors of the previous one. It fits each new tree to the residuals (errors) of the ensemble so far. XGBoost, LightGBM, CatBoost are implementations. RF trains trees in parallel, GB trains them sequentially. GB usually achieves higher accuracy but is slower to train and more prone to overfitting without tuning.

**Q8: Explain the Transformer architecture in plain terms.**

> Input text is tokenized. Each token is converted to an embedding (learned vector). Positional encodings are added (so the model knows token order). The sequence passes through N transformer blocks. Each block has two parts: (1) **Multi-head self-attention** — each token looks at all other tokens and decides how much attention to pay to each; (2) **Feed-forward network** — a simple MLP applied to each token independently. After N blocks, the output is projected to vocabulary size and softmax gives probabilities for the next token.

**Q9: What is self-attention and why is it powerful?**

> Self-attention allows each token to "look at" all other tokens in the sequence when computing its representation. For each token, it computes a query (what am I looking for?), a key (what do I contain?), and a value (what should I contribute?). Attention scores are dot products of queries and keys, normalized by softmax. The output is a weighted sum of values. This lets the model capture long-range dependencies regardless of distance — unlike RNNs that struggled with long sequences.

---

### LLMs and RAG

**Q10: What is the difference between RAG and fine-tuning? When would you use each?**

> **RAG** (Retrieval-Augmented Generation): at inference time, retrieve relevant context from a knowledge base and include it in the prompt. The model itself is unchanged. Use RAG when: data changes frequently, you need factual accuracy with sources, data is too large to fit in context, or you want to avoid the cost/complexity of fine-tuning.
>
> **Fine-tuning**: update the model weights on new data. The model internalizes the knowledge. Use fine-tuning when: you need a specific style or format the base model doesn't have, the task is very domain-specific and consistent, or you need the model to behave differently (not just know different facts).
>
> **Rule of thumb**: try prompting → then RAG → then fine-tune. Each step adds cost and complexity.

**Q11: How does LoRA fine-tuning work?**

> LoRA (Low-Rank Adaptation) freezes the original model weights and adds small, trainable adapter matrices to specific layers (usually attention projection layers). Instead of updating a W (d×d) matrix, it learns two small matrices A (d×r) and B (r×d) where r << d (r is the "rank", typically 4-64). The update is W + AB. Only A and B are trained — typically 0.1-1% of the original parameters. QLoRA additionally quantizes the frozen base model to 4-bit, drastically reducing GPU memory while maintaining quality.

**Q12: How would you evaluate a RAG system?**

> Use the **RAGAS** framework which measures:
> - **Faithfulness**: is the answer grounded in the retrieved context? (no hallucinations)
> - **Answer Relevancy**: does the answer address the actual question?
> - **Context Precision**: are the retrieved chunks actually relevant to the question?
> - **Context Recall**: did we retrieve all the relevant information?
>
> In practice: build a test set of 50-100 question-answer-context triples, run RAGAS metrics, and use an LLM-as-judge for qualitative assessment. Track these metrics before/after each system change.

**Q13: What chunking strategy would you use for a RAG system?**

> Depends on the document type:
> - **Fixed-size chunking** (512-1024 tokens, 10-20% overlap): simple, works for most cases
> - **Semantic chunking**: split at natural boundaries (sentences, paragraphs) — better for narrative text
> - **Recursive character splitting**: LangChain's default; tries paragraphs → sentences → words progressively
> - **Document structure-aware**: for PDFs/HTML, respect headers, tables, code blocks
> - **Parent-child**: store large chunks for context, index small chunks for retrieval
>
> Always experiment: chunk size is a hyperparameter. Start with 512 tokens + 10% overlap.

---

### AI Agents

**Q14: Explain the ReAct pattern for AI agents.**

> ReAct (Reasoning + Acting) interleaves thinking and acting: the LLM first outputs a **Thought** (reasoning about what to do), then an **Action** (calling a tool), then observes the **Observation** (tool output), then reasons again. This loop continues until the task is complete. It outperforms pure reasoning (no tools) or pure acting (no reasoning) because the LLM can correct its own errors based on tool feedback.

**Q15: What are the main challenges in building reliable AI agents?**

> 1. **Error accumulation**: mistakes in early steps compound. Mitigation: add validation at each step, retry logic, human checkpoints.
> 2. **Tool reliability**: external APIs fail or return unexpected formats. Mitigation: structured outputs, explicit error handling.
> 3. **Context overflow**: long chains fill the context window. Mitigation: summarization, memory management.
> 4. **Evaluation**: hard to measure "agent success" vs model quality. Mitigation: define clear task success criteria upfront.
> 5. **Cost**: many LLM calls = expensive. Mitigation: cache tool results, use smaller models for simple steps.

---

## Part 2: Coding Practice — Specific Problems

### Data Manipulation (Always Tested)

Practice these patterns until automatic. These come up in every DS/ML interview screen.

**Python/Pandas — do these on StrataScratch:**

| # | Problem | Skill | Platform |
|---|---------|-------|----------|
| 1 | Facebook: Average Sessions per Day | groupby + aggregation | StrataScratch |
| 2 | Airbnb: Number of Bathrooms and Bedrooms | basic filtering + stats | StrataScratch |
| 3 | Spotify: Find the top-ranking songs | ranking functions | StrataScratch |
| 4 | Amazon: Finding User Purchases | self-join logic in pandas | StrataScratch |
| 5 | Google: Host Popularity Scoring | complex aggregations | StrataScratch |
| 6 | Twitter: Find Users Sending Most Spam | groupby + sort | StrataScratch |

**SQL — do these on LeetCode and StrataScratch:**

| # | Problem | Skill | Platform |
|---|---------|-------|----------|
| LC 175 | Combine Two Tables | LEFT JOIN | LeetCode |
| LC 176 | Second Highest Salary | LIMIT + OFFSET or subquery | LeetCode |
| LC 177 | Nth Highest Salary | window functions | LeetCode |
| LC 178 | Rank Scores | DENSE_RANK() | LeetCode |
| LC 180 | Consecutive Numbers | self-join | LeetCode |
| LC 184 | Department Highest Salary | GROUP BY + JOIN | LeetCode |
| LC 185 | Top 3 salaries | window function + rank | LeetCode |
| LC 196 | Delete Duplicate Emails | DELETE + subquery | LeetCode |
| LC 197 | Rising Temperature | date functions + self-join | LeetCode |
| LC 262 | Trips and Users | complex joins + filtering | LeetCode |

**scikit-learn patterns — implement these from scratch:**

```python
# Pattern 1: Full ML pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])
scores = cross_val_score(pipe, X, y, cv=5, scoring='f1_weighted')

# Pattern 2: Hyperparameter tuning
from sklearn.model_selection import GridSearchCV
params = {'clf__n_estimators': [50, 100, 200], 'clf__max_depth': [None, 5, 10]}
grid = GridSearchCV(pipe, params, cv=3, scoring='f1_weighted', n_jobs=-1)
grid.fit(X_train, y_train)

# Pattern 3: Handling imbalanced data
from sklearn.utils.class_weight import compute_class_weight
weights = compute_class_weight('balanced', classes=np.unique(y), y=y)

# Pattern 4: Feature importance
importances = grid.best_estimator_.named_steps['clf'].feature_importances_
feat_df = pd.DataFrame({'feature': feature_names, 'importance': importances})
    .sort_values('importance', ascending=False)
```

**LLM/RAG patterns — build these from scratch:**

```python
# Pattern 1: Minimal RAG
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

# Load → Split → Embed → Store → Query
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)
vectorstore = Chroma.from_documents(chunks, OpenAIEmbeddings())
qa = RetrievalQA.from_chain_type(ChatOpenAI(), retriever=vectorstore.as_retriever())

# Pattern 2: Streaming response
from openai import OpenAI
client = OpenAI()
stream = client.chat.completions.create(
    model="gpt-4o", messages=[{"role": "user", "content": prompt}], stream=True
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)

# Pattern 3: Function calling
tools = [{"type": "function", "function": {
    "name": "get_weather", "description": "Get weather for a city",
    "parameters": {"type": "object", "properties": {
        "city": {"type": "string"}}, "required": ["city"]}}}]
response = client.chat.completions.create(
    model="gpt-4o", messages=messages, tools=tools, tool_choice="auto")
```

---

## Part 3: System Design — Worked Examples

### Example 1: Design a RAG-based Customer Support Chatbot

**Step 1: Clarify requirements**
- Scale: 10k conversations/day, <3s latency
- Data: 50k support articles, updated weekly
- Accuracy: must cite sources, no hallucinations allowed

**Step 2: Architecture**

```
User Query
    ↓
Query Preprocessing (spell check, intent detection)
    ↓
Hybrid Retrieval (dense + BM25 sparse)
    ↓
Reranking (cross-encoder)
    ↓
Context Assembly (top 3-5 chunks)
    ↓
LLM Generation (GPT-4o or Claude 3.5)
    ↓
Output + Citations
    ↓
Guardrails (PII check, toxicity filter)
    ↓
Response to User
```

**Step 3: Key decisions**
- **Embedding model**: `text-embedding-3-large` (OpenAI) for quality; or `bge-m3` for cost savings
- **Vector store**: Pinecone (managed) or pgvector (if already on Postgres)
- **Retrieval**: Hybrid (dense + BM25) with `reciprocal rank fusion` to merge results
- **Reranking**: `cross-encoder/ms-marco-MiniLM-L6-v2` to reorder top 20 → top 5
- **LLM**: GPT-4o with `temperature=0` for factual, citation-required answers
- **Chunking**: 512 tokens, 10% overlap, document-structure-aware

**Step 4: Monitoring**
- RAGAS metrics on random 2% of conversations (faithfulness, context precision)
- Thumbs up/down feedback per conversation
- Latency: P50, P95, P99 per pipeline stage
- Unanswered rate: when retrieval fails to find relevant context

---

### Example 2: Design a Fraud Detection System

**Step 1: Clarify requirements**
- Volume: 1M transactions/day, must decide in <100ms
- Labels: 0.1% fraud rate (highly imbalanced)
- Action: flag for review or auto-block

**Step 2: Architecture**

```
Transaction Event (Kafka stream)
    ↓
Feature Engineering (real-time + historical)
    ↓
ML Model (XGBoost ensemble)
    ↓
Risk Score (0-1)
    ↓
Rules Engine (hard rules + model score)
    ↓
Decision: Approve / Flag / Block
```

**Step 3: Key decisions**
- **Model**: XGBoost (tabular data, interpretable, fast inference). Ensemble with LightGBM.
- **Imbalanced data**: SMOTE for oversampling + `scale_pos_weight` in XGBoost
- **Metric**: F1 at threshold + AUC-ROC. NOT accuracy (useless at 0.1% fraud rate).
- **Threshold**: tune based on cost matrix (cost of missed fraud >> cost of false positive)
- **Features**: transaction amount, velocity (# transactions last hour/day), merchant category, device fingerprint, behavioral features (typing speed, mouse movement)
- **Drift monitoring**: monitor feature distributions weekly; retrain monthly

**Step 4: Interview follow-ups to prepare for**
- "How do you handle concept drift?" → Monitor model performance on labeled data weekly; retrain when F1 drops 5%+
- "How do you explain a fraud decision to a customer?" → SHAP values; top 3 contributing features
- "How do you avoid discriminatory models?" → Fairness metrics by protected class; EEOC compliance testing

---

### Example 3: Design a Recommendation System

**Step 1: Clarify requirements**
- Scale: 10M users, 1M items, real-time recommendations
- Latency: <50ms for serving
- Goal: maximize click-through rate (CTR)

**Step 2: Two-stage architecture (industry standard)**

```
Stage 1: RETRIEVAL (Candidate Generation)
    ↓ (from 1M items → 500 candidates fast)

Matrix Factorization or Two-Tower Neural Net
User → User Embedding
Item → Item Embedding
ANN (Approximate Nearest Neighbor) search

Stage 2: RANKING (Scoring)
    ↓ (from 500 → top 20 to show)

XGBoost or Deep & Cross Network
Rich features: user history, item metadata, context
Predict P(click | user, item)
```

**Step 3: Key decisions**
- **Retrieval**: Two-Tower model (separate user/item towers) trained with contrastive loss
- **ANN index**: FAISS IVFFlat for billion-scale, or ScaNN for highest accuracy
- **Ranking**: feature-rich model with interaction features (user × item)
- **Cold start**: for new items, use content-based features; for new users, use demographics + popular items
- **A/B testing**: always test ranking changes with proper experimentation

---

## Part 4: Behavioral Questions — STAR Stories

Structure every answer: **S**ituation → **T**ask → **A**ction → **R**esult

**Prepare one strong story for each of these:**

**1. "Tell me about a time you used data to challenge an assumption."**
> *Template*: "We assumed [X was true]. I analyzed [data source] and found [unexpected insight]. I presented this to [stakeholders] and we changed [decision], which led to [outcome]."

**2. "Describe a time you had to learn something quickly."**
> *Template*: "We needed [technology/skill] for [project] in [timeframe]. I [specific learning actions — read docs, built a prototype, paired with expert]. Within [time], I was able to [deliverable], which [outcome]."

**3. "Tell me about a technical project you're most proud of."**
> *Key elements*: What problem you solved, what you built, technical decisions you made and why, what you learned, measurable outcome.

**4. "How do you handle disagreement with a technical decision?"**
> *Template*: "I first try to understand the other perspective by [asking specific questions]. Then I share my concern with [data/reasoning]. If we still disagree, I [defer to senior/propose a test/escalate appropriately]. In [specific case], I did this and [outcome]."

**5. "Tell me about a project that failed."**
> *Key elements*: What went wrong (be specific, not vague), what you did when you realized it, what you'd do differently, what you learned. Interviewers want to see self-awareness and growth, not blame.

---

## Part 5: Pre-Interview Checklist

### 48 Hours Before
- [ ] Review your portfolio projects — can you explain every line of code?
- [ ] Practice saying your projects aloud (2-minute version, 5-minute version)
- [ ] Review the company's AI/ML blog or recent papers — know what they're working on
- [ ] Refresh on the 15 concept questions above

### Day Before
- [ ] Set up your coding environment (no setup errors during the interview)
- [ ] Prepare your IDE and Jupyter — test that you can import pandas, sklearn, torch
- [ ] Review your STAR stories — say them aloud
- [ ] Sleep 8 hours. Seriously.

### Interview Day
- [ ] Have your GitHub open in a browser tab — they will ask to see projects
- [ ] Have a blank notebook ready for live coding
- [ ] For system design: draw diagrams on screen share (use excalidraw.com)
- [ ] Ask clarifying questions before diving into any answer

### Questions to Ask the Interviewer
- "What does a typical week look like for this role?"
- "What's the biggest technical challenge the team is working through right now?"
- "How does the team decide what to build vs. buy vs. use open source?"
- "What would make someone in this role really successful in the first 6 months?"
- "How does the team handle model failures in production?"

---

## Part 6: Role-Specific Study Focus

### If Applying for AI Engineer
Deep focus on: RAG evaluation, streaming, tool calling, LangGraph, vLLM deployment

### If Applying for ML Engineer
Deep focus on: PyTorch training loops, distributed training basics, MLflow, Docker/K8s basics

### If Applying for Data Scientist
Deep focus on: SQL (must be fluent), A/B testing, causal inference, statsmodels, Bayesian thinking

### If Applying for MLOps
Deep focus on: CI/CD for ML, Kubernetes, Prometheus/Grafana, feature stores, model registries
