# Interview Preparation

15 core ML questions, coding problems, 3 system design walkthroughs, and LLM/GenAI questions. Use after building at least one project.

---

## Part 1: Core ML Concepts (15 Questions)

### Q1: Bias-variance tradeoff?
Bias = underfitting (too simple). Variance = overfitting (too sensitive to training data). Goal: find the sweet spot. Diagnose: high train + val error = bias; low train, high val = variance.

### Q2: L1 vs L2 regularization?
**L1 (Lasso)**: Drives some weights to exactly zero. Good for feature selection.
**L2 (Ridge)**: Shrinks all weights toward zero. More stable with correlated features.
**Elastic Net**: Both combined.

### Q3: Gradient descent?
Iteratively adjust parameters to minimize loss. `w = w - lr * gradient`. Variants: Batch (full dataset), SGD (one sample), Mini-batch (best of both), Adam (adaptive per-parameter, most common).

### Q4: Class imbalance?
1. Collect more minority data. 2. Use precision/recall/F1 instead of accuracy. 3. Resample (SMOTE / undersample). 4. Class weights. 5. If extreme (99.9%+), treat as anomaly detection.

### Q5: Precision, recall, F1?
- **Precision**: TP / (TP + FP) — optimize when false positives are costly
- **Recall**: TP / (TP + FN) — optimize when false negatives are costly
- **F1**: Harmonic mean of both

### Q6: Cross-validation?
Split data into K folds, train on K-1, validate on remaining, rotate K times. Use stratified K-fold for classification. Time series: use temporal splits. Never cross-validate on the test set.

### Q7: Transformer architecture?
Processes sequences in parallel via self-attention (not sequential like RNNs).
Key components: token embeddings → positional encoding → multi-head self-attention → feed-forward → layer norm + residuals.
`Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V`
Encoder (BERT) = bidirectional. Decoder (GPT) = causal/masked.

### Q8: Overfitting prevention?
More data, regularization (L1/L2/dropout), early stopping, data augmentation, simpler model, cross-validation, ensembles.

### Q9: Bagging vs boosting?
**Bagging** (Random Forest): parallel training on random subsets, reduces variance.
**Boosting** (XGBoost): sequential, each model corrects previous errors, reduces bias.

### Q10: Random Forest?
Multiple decision trees on bootstrap samples with random feature subsets. Average predictions. Works because averaging decorrelated trees reduces variance without increasing bias.

### Q11: ROC curve and AUC?
ROC: TPR vs FPR at various thresholds. AUC: area under ROC (0.5 = random, >0.9 = outstanding). For imbalanced data, use precision-recall curves instead.

### Q12: Supervised vs unsupervised vs reinforcement?
**Supervised**: labeled data (classification, regression). **Unsupervised**: find patterns (clustering, PCA). **Reinforcement**: learn from rewards/penalties. **Self-supervised**: create own labels (BERT masking, GPT next-token).

### Q13: PCA?
Finds directions of maximum variance, projects data onto them. Use for dimensionality reduction, visualization, noise reduction. Assumes linear relationships — use t-SNE/UMAP for non-linear.

### Q14: Backpropagation?
Forward pass → compute loss → backward pass (chain rule to compute gradients) → update weights. Each layer needs only the gradient from above and its own local gradient.

### Q15: Loss functions?
**MSE**: regression, penalizes large errors. **Cross-entropy**: classification, measures probability divergence. **Binary cross-entropy**: binary classification. Others: Huber, hinge, focal, triplet, contrastive.

---

## Part 2: Coding Problems

### Problem 1: Data Cleaning
Given a messy DataFrame: handle missing values, remove duplicates, compute stats, find correlations. (20 min)

### Problem 2: Train a Classifier
Iris dataset: split, train 2+ models, cross-validate, compare metrics, select best. (20 min)

### Problem 3: Simple RAG Pipeline
Chunk docs → embed with SentenceTransformer → store in ChromaDB → retrieve → construct LLM prompt. (30 min)

### Problem 4: Feature Engineering
Raw transactions → aggregated user features (count, sum, mean, max, std, unique categories, days active). (15 min)

---

## Part 3: System Design Walkthroughs

### Design 1: RAG Document Q&A (10K+ PDFs)

```
Ingestion → Chunk + Embed → Vector DB (Qdrant) → FastAPI → Retrieval + LLM → Streamlit
```

Key decisions: 512-token chunks with 50-token overlap. Hybrid search (dense + BM25) with reranking. GPT-4.1-mini or Claude Haiku 4.5 for cost. Redis caching. RAGAS evaluation.

### Design 2: Recommendation System (10M users, 1M products)

Two-stage: candidate generation (ANN via FAISS/Qdrant) → ranking (XGBoost on features). Real-time features from last 10 interactions. Cold start via content-based features. A/B test with 5% traffic. Latency budget: <100ms.

### Design 3: LLM Customer Support Agent

LangGraph orchestrator with tools: `lookup_order`, `process_return`, `search_faq`, `escalate_to_human`. Guardrails: content moderation, PII redaction, rate limiting. GPT-4.1-mini for high volume, Claude Sonnet 4.6 for complex reasoning. Human-in-the-loop for high-stakes actions.

---

## Part 4: LLM & GenAI Questions

**Q1: RAG vs fine-tuning vs prompting?**
Try prompting → add RAG if hallucinations → fine-tune if style/format still wrong.

**Q2: RAG pipeline end-to-end?**
Document → Chunk → Embed → Store → Query → Retrieve → Rerank → Augment prompt → Generate → Return with citations.

**Q3: What is LoRA?**
Freeze pre-trained weights, inject small trainable adapter matrices. Train ~2-5% of parameters. QLoRA: 4-bit base model + LoRA = 7B model on 4-6GB VRAM.

**Q4: How to evaluate RAG?**
RAGAS: faithfulness, answer relevancy, context precision, context recall. Also: latency, cost/query, user satisfaction.

**Q5: AI agents — what makes them reliable?**
Structured outputs, explicit error handling per tool, retry with backoff, human-in-the-loop for high stakes, comprehensive logging, test scenarios.

---

## Part 5: Behavioral Questions

**"Tell me about a challenging ML project."** Use STAR: Situation, Task, Action, Result (quantify).

**"How do you stay current?"** Follow key researchers, read papers, participate in communities, build prototypes of new tools.

**"Technical disagreements?"** Define metrics, run experiment, let data decide.

**"Explain ML to non-technical audience?"** Use analogies. RAG = "smart student with an open-book exam."

---

## Study Plan

- **Week 1**: Review 15 concept questions + solve coding problems
- **Week 2**: Walk through 3 system designs (35 min each: 5 requirements, 10 high-level, 15 deep dive, 5 scaling)
- **Week 3**: Mock interviews, record yourself, practice on shared screen

---

## Related Files

| Need | File |
|------|------|
| Career strategy | [CAREER_ROADMAP.md](CAREER_ROADMAP.md) |
| Learning plan | [MASTER_STUDY_GUIDE.md](MASTER_STUDY_GUIDE.md) |
| Tool comparisons | [COMPARISON_MATRICES.md](COMPARISON_MATRICES.md) |

*Last Updated: April 2026*
