# AI / ML Visual Roadmap

> Interactive Mermaid diagrams covering the full AI & ML landscape — from fundamentals to production systems. Every box maps to a phase in the **Zero to AI** curriculum.

## Jump To

**Overview**

- [1. The Big Picture](#the-big-picture)
- [2. Machine Learning Paradigms](#machine-learning-paradigms)
- [3. Deep Learning Architecture Tree](#deep-learning-architecture-tree)
- [4. NLP & LLM Pipeline](#nlp-llm-pipeline)

**Core Systems**

- [5. The LLM Model Landscape (2026)](#the-llm-model-landscape-2026)
- [6. Embeddings & Vector Search](#embeddings-vector-search)
- [7. RAG (Retrieval-Augmented Generation)](#rag-retrieval-augmented-generation)
- [8. AI Agents Architecture](#ai-agents-architecture)
- [9. Multi-Agent Systems](#multi-agent-systems)
- [10. MLOps Lifecycle](#mlops-lifecycle)

**Advanced Topics**

- [11. Fine-tuning Decision Tree](#fine-tuning-decision-tree)
- [12. Multimodal AI](#multimodal-ai)
- [13. Inference Optimization](#inference-optimization)
- [14. AI Safety & Guardrails](#ai-safety-guardrails)

**Cross-Topic Flows**

- [15. End-to-End Project Flow](#end-to-end-project-flow)
- [16. Docs + Query → Chunks → Embeddings → RAG → Answer](#end-to-end-docs-query-chunks-embeddings-rag-answer)
- [17. Document Ingestion Pipeline](#end-to-end-document-ingestion-pipeline)
- [18. Training an LLM (Pre-train → Fine-tune → Deploy)](#end-to-end-training-an-llm-pre-train-fine-tune-deploy)
- [19. Agentic RAG (Question → Tools → Search → Synthesize)](#end-to-end-agentic-rag-question-tools-search-synthesize)
- [20. From Idea to Production AI App](#end-to-end-from-idea-to-production-ai-app)
- [21. Multimodal — Image + Text → Understanding → Generation](#end-to-end-multimodal-image-text-understanding-generation)

## Suggested Reading Paths

**If you are new to AI/ML**

Start with [1. The Big Picture](#the-big-picture), then read [2. Machine Learning Paradigms](#machine-learning-paradigms), [3. Deep Learning Architecture Tree](#deep-learning-architecture-tree), and [15. End-to-End Project Flow](#end-to-end-project-flow).

**If you want to build LLM applications**

Start with [4. NLP & LLM Pipeline](#nlp-llm-pipeline), then move to [6. Embeddings & Vector Search](#embeddings-vector-search), [7. RAG (Retrieval-Augmented Generation)](#rag-retrieval-augmented-generation), [8. AI Agents Architecture](#ai-agents-architecture), and [20. From Idea to Production AI App](#end-to-end-from-idea-to-production-ai-app).

**If you care about production systems**

Start with [10. MLOps Lifecycle](#mlops-lifecycle), then read [13. Inference Optimization](#inference-optimization), [14. AI Safety & Guardrails](#ai-safety-guardrails), [19. Agentic RAG (Question → Tools → Search → Synthesize)](#end-to-end-agentic-rag-question-tools-search-synthesize), and [20. From Idea to Production AI App](#end-to-end-from-idea-to-production-ai-app).

**If you want model internals**

Start with [3. Deep Learning Architecture Tree](#deep-learning-architecture-tree), then read [4. NLP & LLM Pipeline](#nlp-llm-pipeline), [11. Fine-tuning Decision Tree](#fine-tuning-decision-tree), [12. Multimodal AI](#multimodal-ai), and [18. Training an LLM (Pre-train → Fine-tune → Deploy)](#end-to-end-training-an-llm-pre-train-fine-tune-deploy).

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
        I --> J[Prompt Engineering]
        J --> K[LLM Fine-tuning]
        K --> L[Multimodal AI]
        L --> M[Local LLMs]
        M --> N[AI Agents]
    end

    subgraph Production
        N --> O[Model Evaluation]
        O --> P[Inference Optimization]
        P --> Q[AI Safety & Red-teaming]
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

## 5. The LLM Model Landscape (2026)

```{mermaid}
flowchart TD
    subgraph Proprietary
        GPT[GPT-5.4 / o3 / o4-mini]
        CLAUDE[Claude Sonnet 4.6 / Opus 4.6]
        GEMINI[Gemini 3.1 Pro / Flash]
    end

    subgraph Open-Weight
        LLAMA[Llama 4 Scout / Maverick]
        QWEN[Qwen 3 0.6B-235B]
        DS[DeepSeek V3.2 / R1]
        PHI[Phi-4 14B]
        MISTRAL[Mistral / Mixtral]
    end

    subgraph Reasoning
        O3[OpenAI o3 / o4-mini]
        R1[DeepSeek R1 671B]
        CT[Claude Extended Thinking]
    end

    subgraph Local Running
        OLLAMA[Ollama]
        LLAMACPP[llama.cpp]
        MLX[Apple MLX]
        OLLAMA --- PHI
        LLAMACPP --- QWEN
        MLX --- LLAMA
    end
```

---

## 6. Embeddings & Vector Search

```{mermaid}
flowchart TD
    subgraph Embedding Models
        OAI_E["OpenAI text-embedding-3"]
        ST["Sentence Transformers"]
        COHERE_E["Cohere embed-v4"]
        NOM["nomic-embed-text"]
    end

    subgraph Vector Databases
        CHROMA[ChromaDB]
        QDRANT[Qdrant]
        PINECONE[Pinecone]
        WEAVIATE[Weaviate]
        PGVEC[pgvector]
        FAISS[FAISS]
    end

    DOC[Documents] --> CHUNK[Chunk] --> EMB[Embed]
    EMB --> OAI_E
    EMB --> ST
    OAI_E --> STORE[Store]
    ST --> STORE
    STORE --> CHROMA
    STORE --> QDRANT
    STORE --> PINECONE

    QUERY[Query] --> Q_EMB[Embed Query]
    Q_EMB --> SIM[Similarity Search]
    CHROMA --> SIM
    QDRANT --> SIM
    PINECONE --> SIM
    SIM --> RESULTS[Top-K Results]
```

---

## 7. RAG (Retrieval-Augmented Generation)

```{mermaid}
flowchart TD
    subgraph Indexing Pipeline
        A[Documents] --> B[Chunk]
        B --> C[Embed]
        C --> D[Vector Store]
    end

    subgraph Query Pipeline
        E[User Question] --> F[Embed Query]
        F --> G[Retrieve Top-K]
        D --> G
        G --> H["Context + Question"]
    end

    subgraph Generation
        H --> I[LLM]
        I --> J[Answer with Citations]
    end

    subgraph Advanced RAG
        K[Re-ranking] --> G
        L[Query Expansion] --> F
        M[Hybrid Search BM25 + Dense] --> G
        N[Agentic RAG] --> I
    end
```

---

## 8. AI Agents Architecture

```{mermaid}
flowchart TD
    USER[User Request] --> AGENT[Agent - LLM Brain]

    AGENT --> PLAN[Plan / Reason]
    PLAN --> ACT[Select Tool]
    ACT --> TOOL1["🔧 Web Search"]
    ACT --> TOOL2["🔧 Code Executor"]
    ACT --> TOOL3["🔧 Database Query"]
    ACT --> TOOL4["🔧 API Call"]

    TOOL1 --> OBS[Observation]
    TOOL2 --> OBS
    TOOL3 --> OBS
    TOOL4 --> OBS

    OBS --> REFLECT{Done?}
    REFLECT -->|No| PLAN
    REFLECT -->|Yes| ANSWER[Final Answer]

    subgraph Protocols
        MCP["MCP - Tool Connectivity"]
        A2A["A2A - Agent Delegation"]
    end

    subgraph Frameworks
        LC[LangChain / LangGraph]
        OAI_SDK[OpenAI Agents SDK]
        CREW[CrewAI]
        ADK[Google ADK]
        SK[Semantic Kernel]
    end
```

---

## 9. Multi-Agent Systems

```{mermaid}
flowchart TD
    USER[User Task] --> COORD[Coordinator Agent]

    COORD --> R[Researcher]
    COORD --> W[Writer]
    COORD --> C[Critic]

    R -->|findings| COORD
    W -->|draft| COORD
    C -->|feedback| COORD

    COORD --> FINAL[Final Output]

    subgraph Patterns
        P1[Coordinator / Delegate]
        P2[Pipeline - Sequential]
        P3[Debate - Adversarial]
        P4[Voting - Consensus]
    end
```

---

## 10. MLOps Lifecycle

```{mermaid}
flowchart TD
    A[Data Collection] --> B[Data Validation]
    B --> C[Feature Engineering]
    C --> D[Model Training]
    D --> E[Experiment Tracking - MLflow]
    E --> F[Model Evaluation]
    F --> G[Model Registry]
    G --> H[CI/CD Pipeline]
    H --> I[Deployment]
    I --> J[Monitoring & Observability]
    J --> K{Drift Detected?}
    K -->|Yes| A
    K -->|No| J

    subgraph Serving
        I --> S1[REST API - FastAPI]
        I --> S2[vLLM / TGI]
        I --> S3[Triton Inference Server]
        I --> S4[Managed APIs - Bedrock / Vertex AI / Azure AI Foundry]
        I --> S5[Edge Runtime - ONNX Runtime]
        I --> S6[Open Source - Ollama / llama.cpp / SGLang]
    end
```

---

## 11. Fine-tuning Decision Tree

```{mermaid}
flowchart TD
    START{Can a good prompt solve it?}
    START -->|Yes| PE[Prompt Engineering]
    START -->|No| DOCS{Need private/current docs?}
    DOCS -->|Yes| RAG_FT[RAG]
    DOCS -->|No| STYLE{Need consistent style/format?}
    STYLE -->|Yes| FT[Fine-tuning]
    STYLE -->|No| PRIV{Data privacy critical?}
    PRIV -->|Yes| FT
    PRIV -->|No| COST{Inference cost a concern?}
    COST -->|Yes| FT_SMALL["Fine-tune smaller model"]
    COST -->|No| PE

    subgraph Fine-tuning Methods
        FULL[Full Fine-tuning >40GB VRAM]
        LORA["LoRA / DoRA (8-12GB)"]
        QLORA["QLoRA 4-bit (4-6GB)"]
        PT["Prompt Tuning (<1GB)"]
    end
```

---

## 12. Multimodal AI

```{mermaid}
flowchart TD
    subgraph Vision Language
        IMG[Image] --> VIT_M[ViT Encoder]
        VIT_M --> PROJ[Projection Layer]
        TXT[Text Prompt] --> LLM_M[LLM]
        PROJ --> LLM_M
        LLM_M --> RESP[Text Response]
    end

    subgraph Image Generation
        PROMPT[Text Prompt] --> CLIP_M[CLIP Encoder]
        CLIP_M --> UNET["U-Net (Denoising)"]
        UNET --> VAE[VAE Decoder]
        VAE --> IMAGE[Generated Image]
    end

    subgraph Models
        GPT5[GPT-5.4 Vision]
        GEM[Gemini 3.1 Pro]
        CL[Claude Sonnet 4.6]
        FLUX_M[FLUX 1.1]
        SD35[Stable Diffusion 3.5]
    end
```

---

## 13. Inference Optimization

```{mermaid}
flowchart LR
    MODEL[Trained Model] --> Q[Quantization]
    MODEL --> KV[KV-Cache Optimization]
    MODEL --> SPEC[Speculative Decoding]
    MODEL --> BATCH[Continuous Batching]

    Q --> Q4["4-bit (GPTQ / AWQ)"]
    Q --> Q8["8-bit (bitsandbytes)"]
    KV --> PAGED[PagedAttention - vLLM]
    KV --> PREFIX[Prefix Caching]
    SPEC --> DRAFT[Draft Model + Verify]
    BATCH --> VLLM[vLLM / SGLang / TGI]

    VLLM --> DEPLOY[Production Deployment]
    DEPLOY --> GPU["NVIDIA A100/H100"]
    DEPLOY --> APPLE[Apple Silicon - MLX]
    DEPLOY --> EDGE["Edge - Phi-4 / Qwen3-0.6B"]
```

---

## 14. AI Safety & Guardrails

```{mermaid}
flowchart TD
    INPUT[User Input] --> V["Layer 1: Input Validation"]
    V --> PI["Layer 2: Prompt Injection Detection"]
    PI --> MOD["Layer 3: Content Moderation"]
    MOD --> PII["Layer 4: PII Detection"]
    PII --> LLM_S["Layer 5: LLM Processing"]
    LLM_S --> OUT["Layer 6: Output Validation"]
    OUT --> LOG["Layer 7: Monitoring & Logging"]
    LOG --> RESP_S[Safe Response]

    subgraph Red Teaming
        RT1[Prompt Injection Attacks]
        RT2[Jailbreak Attempts]
        RT3[Data Extraction Probes]
        RT4[Bias & Fairness Testing]
    end
```

---

## 15. End-to-End Project Flow

```{mermaid}
flowchart LR
    subgraph "Phase 1 - Learn"
        P[Python] --> DS[Data Science]
        DS --> MATH[Math & Stats]
        MATH --> NN[Neural Networks]
    end

    subgraph "Phase 2 - Build"
        NN --> TOK[Tokenization]
        TOK --> EMB_P[Embeddings]
        EMB_P --> VDB[Vector DB]
        VDB --> RAG_P[RAG System]
    end

    subgraph "Phase 3 - Ship"
        RAG_P --> AGENT_P[AI Agent]
        AGENT_P --> EVAL[Evaluation]
        EVAL --> OPT[Optimization]
        OPT --> DEPLOY_P[Deploy to Production]
    end
```

---

## 16. End-to-End: Docs + Query → Chunks → Embeddings → RAG → Answer

Traces both sides of the RAG system: document ingestion and query-time retrieval.

```{mermaid}
flowchart LR
    subgraph "Corpus Side"
        DOCS[Source Documents] --> SPLIT[Chunking]
        SPLIT --> CHUNKS[Text Chunks]
        CHUNKS --> DOC_EMB[Embedding Model]
        DOC_EMB --> DOCVEC["Stored Chunk Vectors"]
    end

    subgraph "Phase 4 · Tokenization"
        RAW["'What causes<br/>Northern Lights?'"] --> TOK[Tokenizer - BPE]
        TOK --> IDS["Token IDs<br/>[2061, 5765, 4249, ...]"]
    end

    subgraph "Phase 5 · Embeddings"
        IDS --> EMB_MODEL["Embedding Model<br/>text-embedding-3-small"]
        EMB_MODEL --> QVEC["Query Vector<br/>[0.021, -0.14, ..., 0.087]<br/>1536 dims"]
    end

    subgraph "Phase 7 · Vector DB"
        QVEC --> SIM["Cosine Similarity<br/>Search"]
        DOCVEC --> SIM
        SIM --> TOPK["Top-K Chunks<br/>k=5"]
    end

    subgraph "Phase 8 · RAG"
        TOPK --> CTX["Context Assembly<br/>System + Retrieved Chunks + Question"]
        CTX --> LLM["LLM<br/>GPT-4o / Claude"]
        LLM --> ANS["'The Northern Lights are caused<br/>by charged solar particles...'"]
    end
```

---

## 17. End-to-End: Document Ingestion Pipeline

How a PDF becomes searchable knowledge in a RAG system.

```{mermaid}
flowchart TD
    subgraph "Ingestion"
        PDF[PDF / Web Page / Markdown] --> PARSE[Parse & Extract Text]
        PARSE --> CLEAN[Clean & Normalize]
    end

    subgraph "Phase 4 · Chunking"
        CLEAN --> SPLIT{"Splitting Strategy"}
        SPLIT -->|Fixed size| FIX["512 tokens<br/>50-token overlap"]
        SPLIT -->|Semantic| SEM["By paragraph /<br/>section boundary"]
        SPLIT -->|Recursive| REC["Try \\n\\n → \\n → . → space"]
        FIX --> CHUNKS["Chunks[]"]
        SEM --> CHUNKS
        REC --> CHUNKS
    end

    subgraph "Phase 5 · Embedding"
        CHUNKS --> BATCH["Batch Embed<br/>(1000 chunks at a time)"]
        BATCH --> VECS["Float32 vectors<br/>1 per chunk"]
    end

    subgraph "Phase 7 · Storage"
        VECS --> DB["Vector DB<br/>ChromaDB / Qdrant / pgvector"]
        CHUNKS -->|metadata| DB
    end
```

---

## 18. End-to-End: Training an LLM (Pre-train → Fine-tune → Deploy)

How a language model goes from raw text to a production API.

```{mermaid}
flowchart LR
    subgraph "Pre-training"
        CORPUS["Internet-scale Corpus<br/>trillions of tokens"] --> TOK_T[Tokenizer Training - BPE]
        TOK_T --> PT["Pre-training<br/>Next-token prediction<br/>1000s of GPUs, weeks"]
        PT --> BASE["Base Model<br/>(completes text, no instructions)"]
    end

    subgraph "Alignment"
        BASE --> SFT["Supervised Fine-tuning<br/>(instruction / chat pairs)"]
        SFT --> POST_ALIGN{Post-training method}
        POST_ALIGN --> RLHF_T["RLHF<br/>Reward model + PPO"]
        POST_ALIGN --> GRPO_T["GRPO<br/>Group-relative rewards"]
        RLHF_T --> CHAT["Chat Model<br/>(follows instructions)"]
        GRPO_T --> CHAT
    end

    subgraph "Customization"
        CHAT --> LORA["LoRA / QLoRA<br/>Your domain data"]
        LORA --> CUSTOM["Custom Model"]
    end

    subgraph "Serving"
        CUSTOM --> QUANT["Quantize<br/>4-bit / 8-bit"]
        QUANT --> SERVE["vLLM / TGI<br/>Continuous Batching"]
        SERVE --> API["REST API<br/>FastAPI"]
    end
```

---

## 19. End-to-End: Agentic RAG (Question → Tools → Search → Synthesize)

An AI agent answering a complex question that requires multiple tool calls.

```{mermaid}
flowchart TD
    Q["User: 'Compare Q1 revenue<br/>of AAPL and MSFT'"] --> AGENT["Agent (LLM Brain)<br/>Plans: need 2 data lookups"]

    AGENT -->|"Step 1"| TOOL_A["🔧 Financial API<br/>get_revenue('AAPL', 'Q1')"]
    AGENT -->|"Step 2"| TOOL_B["🔧 Financial API<br/>get_revenue('MSFT', 'Q1')"]

    TOOL_A --> OBS_A["Observation: $94.9B"]
    TOOL_B --> OBS_B["Observation: $61.9B"]

    OBS_A --> THINK["Agent Reflects:<br/>'I have both numbers, can compare'"]
    OBS_B --> THINK

    THINK --> SYNTH["Generate Answer:<br/>'AAPL Q1 revenue ($94.9B)<br/>exceeded MSFT ($61.9B) by 53%'"]

    subgraph "Under the Hood (per tool call)"
        CALL[Tool Schema - JSON] --> FC[Function Calling API]
        FC --> EXEC[Execute Function]
        EXEC --> PARSE[Parse Result]
        PARSE --> FEED[Feed back to LLM]
    end
```

---

## 20. End-to-End: From Idea to Production AI App

The complete lifecycle from first line of code to users in production.

```{mermaid}
flowchart TD
    subgraph "Prototype"
        IDEA[Idea / Use Case] --> PROMPT["Prompt Engineering<br/>Test in Playground"]
        PROMPT --> EVAL_P{Good enough?}
        EVAL_P -->|No| RAG_Q["Add RAG<br/>(retrieve domain docs)"]
        RAG_Q --> EVAL_P
        EVAL_P -->|Still No| FT_Q["Fine-tune<br/>(LoRA on your data)"]
        FT_Q --> EVAL_P
        EVAL_P -->|Yes| MVP["Working Prototype"]
    end

    subgraph "Harden"
        MVP --> GUARD["Add Guardrails<br/>Input validation, PII filter"]
        GUARD --> TEST["Eval Suite<br/>50+ test cases, LLM-as-Judge"]
        TEST --> OBS["Observability<br/>LangSmith / Arize tracing"]
    end

    subgraph "Ship"
        OBS --> API_P["Wrap in API<br/>FastAPI + auth"]
        API_P --> DOCKER["Containerize<br/>Docker"]
        DOCKER --> DEPLOY_Q["Deploy<br/>Cloud / Kubernetes"]
        DEPLOY_Q --> MONITOR["Monitor<br/>Latency, cost, drift"]
        MONITOR -->|Drift| RETRAIN["Retrain / Re-index"]
        RETRAIN --> TEST
    end
```

---

## 21. End-to-End: Multimodal — Image + Text → Understanding → Generation

How multimodal models process and generate across modalities.

```{mermaid}
flowchart LR
    subgraph "Understanding (Vision-Language)"
        IMG["📷 Photo of a dog<br/>on a beach"] --> VIT["ViT Encoder<br/>Patch embeddings"]
        VIT --> PROJ["Projection Layer<br/>Align to LLM space"]
        TXT_Q["'What breed is this?'"] --> TOK_M[Tokenizer]
        TOK_M --> LLM_EMB["LLM Token Embeddings"]
        PROJ --> MERGE["Merge: image + text<br/>tokens"]
        LLM_EMB --> MERGE
        MERGE --> LLM_M["LLM Decoder<br/>GPT-5.4 / Gemini"]
        LLM_M --> ANS_M["'Golden Retriever,<br/>adult, sandy beach'"]
    end

    subgraph "Generation (Diffusion)"
        PROMPT_G["'Golden Retriever<br/>running on Mars'"] --> CLIP_E["CLIP Text Encoder"]
        CLIP_E --> NOISE["Start from Noise<br/>Gaussian random"]
        NOISE --> DENOISE["U-Net Denoising<br/>50 steps"]
        DENOISE --> VAE_D["VAE Decoder"]
        VAE_D --> IMG_OUT["🖼️ Generated Image"]
    end
```

---

## How to Read These Diagrams

| Symbol | Meaning |
|--------|---------|
| `[Box]` | Concept, tool, or technique |
| `-->` | Leads to / depends on |
| `-.->` | Weak or optional dependency |
| `{Diamond}` | Decision point |
| `subgraph` | Grouping of related concepts |

Each box roughly corresponds to a topic covered in one of the **31 phases** of the Zero to AI curriculum. Follow the arrows to find a natural learning path.

---

*Generated for the Zero to AI curriculum — April 2026*
