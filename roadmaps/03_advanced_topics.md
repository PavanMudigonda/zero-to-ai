# Visual Roadmap — Part 3: Advanced Topics

> Fine-tuning decisions, multimodal AI, inference optimization, and AI safety.

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

[← Previous: Core Systems](02_core_systems.md) | [Next: End-to-End Flows →](04_end_to_end_flows.md)
