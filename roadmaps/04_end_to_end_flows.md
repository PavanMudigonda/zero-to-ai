# Visual Roadmap - Part 4: End-to-End Flows

> Complete pipelines from raw data to production: project flow, RAG pipeline, document ingestion, LLM training, agentic RAG, idea-to-production, and multimodal.

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

## 16. Docs + Query → Chunks → Embeddings → RAG → Answer

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

## 17. Document Ingestion Pipeline

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

## 18. Training an LLM (Pre-train → Fine-tune → Deploy)

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

## 19. Agentic RAG (Question → Tools → Search → Synthesize)

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

## 20. From Idea to Production AI App

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

## 21. Multimodal - Image + Text → Understanding → Generation

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

[← Previous: Advanced Topics](03_advanced_topics.md)
