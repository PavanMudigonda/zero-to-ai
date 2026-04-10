# Visual Roadmap — Part 1: Overview

> Foundational diagrams: the big picture, ML paradigms, deep learning architectures, and the NLP/LLM pipeline.

---

## 1. The Big Picture

```{mermaid}
flowchart TD
    subgraph Foundations
        A[Python & NumPy] --> B[Data Science & Pandas]
        B --> C[Mathematics & Statistics]
    end

    subgraph Core ML
        C --> D[Tokenization]
        D --> E[Embeddings]
        E --> F[Neural Networks & Deep Learning]
    end

    subgraph Applied AI
        F --> G[Vector Databases]
        G --> H[RAG Systems]
        H --> I[MLOps & Deployment]
    end

    subgraph Advanced
        I --> J[Specializations]
        J --> K[Prompt Engineering]
        K --> L[LLM Fine-tuning]
        L --> M[Multimodal AI]
        M --> N[Local LLMs]
        N --> O[AI Agents]
    end

    subgraph Production
        O --> P[Model Evaluation]
        P --> Q[Inference Optimization]
        Q --> R[AI Safety & Red-teaming]
    end

    subgraph Developer Tools
        R --> S[VS Code & GitHub Copilot]
        S --> T[MCP Servers]
        T --> U[Custom Instructions & Agent Config]
    end
```

---

## 2. Machine Learning Paradigms

```{mermaid}
flowchart TD
    ML[Machine Learning] --> SUP[Supervised Learning]
    ML --> UNSUP[Unsupervised Learning]
    ML --> RL[Reinforcement Learning]
    ML --> SSL[Self-Supervised Learning]

    SUP --> CLS[Classification]
    SUP --> REG[Regression]
    CLS --> LR[Logistic Regression]
    CLS --> SVM[SVM]
    CLS --> RF[Random Forest]
    CLS --> XGB[XGBoost / LightGBM]
    REG --> LINR[Linear Regression]
    REG --> LASSO[Lasso / Ridge]

    UNSUP --> CLUST[Clustering]
    UNSUP --> DR[Dimensionality Reduction]
    CLUST --> KM[K-Means]
    CLUST --> DBSCAN[DBSCAN]
    DR --> PCA[PCA]
    DR --> TSNE[t-SNE / UMAP]

    RL --> MAB[Multi-Armed Bandits]
    RL --> PG[Policy Gradient]
    RL --> LLM_RL[RL for LLM Post-Training]
    LLM_RL --> RLHF[RLHF]
    LLM_RL --> GRPO[GRPO]

    SSL --> MASK[Masked Language Modeling]
    SSL --> CLIP_SSL[Contrastive Learning - CLIP]
```

---

## 3. Deep Learning Architecture Tree

```{mermaid}
flowchart TD
    DL[Deep Learning] --> FNN[Feed-forward Networks]
    DL --> CNN[CNNs - Convolutional]
    DL --> RNN_GRP[RNNs - Recurrent]
    DL --> TF[Transformers]
    DL --> GAN[GANs - Generative]
    DL --> DIFF[Diffusion Models]

    FNN --> MLP[MLP / Autoencoders]
    CNN --> IMGCLS[Image Classification]
    CNN --> OBJ[Object Detection - YOLO]
    CNN --> SEG[Segmentation - SAM]

    RNN_GRP --> LSTM[LSTM / GRU]
    RNN_GRP --> TS[Time-Series Forecasting]

    TF --> ENC[Encoder-only - BERT]
    TF --> DEC[Decoder-only - GPT]
    TF --> ENCDEC[Encoder-Decoder - T5]
    TF --> VIT[Vision Transformer - ViT]
    TF --> MOE[Mixture of Experts - Mixtral]

    GAN --> STYLEGAN[StyleGAN]
    DIFF --> SD[Stable Diffusion / FLUX]
    DIFF --> SORA[Video Generation - Sora]
```

---

## 4. NLP & LLM Pipeline

```{mermaid}
flowchart LR
    A[Raw Text] --> B[Tokenization]
    B --> C[Embeddings]
    C --> D[Transformer Layers]
    D --> E{Task?}

    E -->|Generation| F[Decoder - GPT / Llama]
    E -->|Classification| G[Encoder - BERT]
    E -->|Translation| H[Encoder-Decoder - T5]
    E -->|Reasoning| I[Reasoning Model - o3 / R1]

    F --> J[Prompt Engineering]
    J --> K[Fine-tuning - LoRA / QLoRA]
    K --> L[Evaluation - MMLU / HumanEval]
    L --> M[Deployment - vLLM / TGI]
```

---

[Next: Core Systems →](02_core_systems.md)
