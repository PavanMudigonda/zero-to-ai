# MLOps

> **Goal**: Learn to deploy, monitor, and maintain ML models as production systems. This is what separates a data scientist from a machine learning engineer.

This phase is one of the main bridges from learning notebooks to building production-ready systems. If you want hiring leverage, this is one of the most important folders in the repo.

---

## Why MLOps Matters for Your Career

80% of ML projects never reach production. The ones that do succeed because of solid MLOps practices. Employers specifically look for:

- Can you deploy a model beyond a Jupyter notebook?
- Can you reproduce an experiment from 3 months ago?
- Do you know how to detect when a model starts degrading?
- Can you build a CI/CD pipeline for ML?

MLOps is consistently one of the top hiring criteria for ML Engineer roles.

---

## Notebooks - Work in This Order

| # | Notebook | What You Learn | Time |
|---|----------|----------------|------|
| 1 | [01_START_HERE.ipynb](01_START_HERE.ipynb) | MLOps overview and the full lifecycle | 30 min |
| 2 | [02_experiment_tracking.ipynb](02_experiment_tracking.ipynb) | MLflow: log metrics, params, artifacts | 60 min |
| 3 | [03_fastapi_basics.ipynb](03_fastapi_basics.ipynb) | Build REST API endpoints for model serving | 60 min |
| 4 | [04_model_deployment.ipynb](04_model_deployment.ipynb) | Package and deploy a model end-to-end | 90 min |
| 5 | [05_docker_ml.ipynb](05_docker_ml.ipynb) | Containerize ML models with Docker | 90 min |
| 6 | [06_monitoring.ipynb](06_monitoring.ipynb) | Detect data drift and model degradation | 60 min |
| 7 | [07_ci_cd_pipeline.ipynb](07_ci_cd_pipeline.ipynb) | GitHub Actions for automated ML testing | 60 min |
| 8 | [08_cloud_deployment.ipynb](08_cloud_deployment.ipynb) | Deploy to AWS/GCP/Azure | 90 min |
| 9 | [09_llm_infrastructure.ipynb](09_llm_infrastructure.ipynb) | vLLM, TGI, and LLM serving at scale | 60 min |

## How To Use This Phase Well

- Complete at least one full path: experiment tracking -> serving -> containerization -> monitoring.
- Build one deployable project instead of only reading notebook examples.
- Treat monitoring and reproducibility as part of the product, not as post-launch cleanup.
- Pair this phase with a model-building phase you already care about so the operational work stays concrete.

---

## Key Concepts

### The ML Lifecycle (What MLOps Manages)

```{mermaid}
flowchart TD
    A[Data Collection] --> B[Data Validation]
    B --> C[Feature Engineering]
    C --> D[Model Training]
    D --> E[Experiment Tracking]
    E --> F[Model Evaluation]
    F --> G[Model Registry]
    G --> H[CI/CD]
    H --> I[Deployment]
    I --> J[Monitoring]
    J --> K[Retraining]
    K --> A
```

### Experiment Tracking (MLflow)

Every training run should be tracked. Track:
- **Parameters**: learning rate, batch size, model architecture choices
- **Metrics**: loss, accuracy, F1, AUC - over time, not just final values
- **Artifacts**: the trained model file, tokenizer, feature scaler
- **Environment**: Python version, library versions (requirements.txt)

**MLflow quick start:**
```python
import mlflow

mlflow.start_run()
mlflow.log_param("learning_rate", 0.001)
mlflow.log_metric("accuracy", 0.94)
mlflow.log_artifact("model.pkl")
mlflow.end_run()
```

### Model Serving Patterns

| Pattern | Tool | When to Use |
|---------|------|-------------|
| REST API | FastAPI | Standard models, <100ms latency needed |
| Batch inference | Celery/Ray | Large datasets, overnight jobs |
| Streaming | vLLM + SSE | LLM text generation |
| Managed foundation model API | Bedrock / Vertex AI / Azure AI Foundry | Fastest path to production without running GPUs |
| GPU inference server | Triton / vLLM / TGI | High-throughput production serving |
| Edge deployment | ONNX Runtime | Mobile/embedded devices |

### The MLOps Stack (What to Learn)

| Category | Tool | Priority |
|----------|------|----------|
| Experiment tracking | MLflow or W&B | Must know |
| Model serving | FastAPI | Must know |
| Containerization | Docker | Must know |
| CI/CD | GitHub Actions | Must know |
| Monitoring | Prometheus + Grafana | Know basics |
| LLM serving | vLLM | Know if doing LLM work |
| Orchestration | Kubeflow / Airflow | Nice to have |
| Cloud ML | SageMaker / Azure ML / Vertex AI | Nice to have |

### Deployment Matrix: AWS, Azure, Google, and Open Source

Different deployment targets solve different problems. `ONNX Runtime` is a runtime and model format choice. `Bedrock`, `Vertex AI`, and `Azure AI Foundry` are managed platforms. `vLLM`, `TGI`, `Triton`, `Ollama`, and `llama.cpp` are open-source serving stacks.

| Need | AWS | Azure | Google Cloud | Open Source | Best Fit |
|------|-----|-------|--------------|-------------|----------|
| Managed LLM API | Bedrock | Azure AI Foundry / Azure OpenAI | Vertex AI Gemini | OpenAI-compatible gateway over hosted OSS is possible, but not truly managed | Teams that want minimal infra |
| Train and deploy custom ML model | SageMaker | Azure ML | Vertex AI | FastAPI + Docker + Kubernetes | Classical ML and custom DL models |
| Self-host open-weight LLMs on GPU | EKS/ECS + vLLM or TGI | AKS + vLLM or TGI | GKE + vLLM or TGI | vLLM / TGI / Triton / SGLang | High-volume LLM inference |
| Multi-model inference server | SageMaker endpoints or ECS/EKS + Triton | Azure ML managed endpoints or AKS + Triton | Vertex endpoints or GKE + Triton | Triton Inference Server | Mixed PyTorch / TensorRT / ONNX workloads |
| Edge or mobile deployment | Greengrass + ONNX Runtime | Azure IoT Edge + ONNX Runtime | Edge TPU / Vertex Edge + ONNX Runtime | ONNX Runtime / TensorFlow Lite / llama.cpp | Low-latency local inference |
| Local developer workflow | Bedrock local emulation is limited | Azure-hosted only | Vertex-hosted only | Ollama / llama.cpp / LM Studio | Fast iteration and privacy |

### How to Choose a Deployment Path

1. **Use ONNX Runtime** when you own the model artifact and want portable, optimized inference across CPU, GPU, and edge devices.
2. **Use Bedrock / Azure AI Foundry / Vertex AI** when you want managed foundation model access and do not want to run your own inference cluster.
3. **Use SageMaker / Azure ML / Vertex AI custom endpoints** when you need managed training plus deployment for your own models.
4. **Use vLLM / TGI / Triton / SGLang** when you want open-source control, custom batching, lower cost at scale, or open-weight LLM hosting.
5. **Use Ollama or llama.cpp** for local development, offline demos, CPU-friendly inference, or privacy-sensitive prototyping.

### Practical Defaults

| Scenario | Recommended Path |
|----------|------------------|
| MVP chatbot with lowest ops burden | Bedrock, Azure AI Foundry, Vertex AI, or OpenAI/Anthropic API |
| Enterprise app with strict cloud standard | Match the platform to your cloud: Bedrock, Azure AI Foundry, or Vertex AI |
| Open-weight LLM in production | vLLM or TGI on Kubernetes / cloud GPU |
| Mixed model fleet with TensorRT/ONNX/PyTorch | Triton Inference Server |
| Mobile / embedded / offline | ONNX Runtime or TensorFlow Lite |
| Local-first development | Ollama or llama.cpp |

### Docker for ML - The Essential Pattern

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Model Monitoring - What to Watch

- **Data drift**: Input feature distributions shift from training distribution
- **Concept drift**: The relationship between features and labels changes
- **Performance degradation**: Accuracy/F1 drops on recent data
- **Latency**: Response time increases (often due to memory pressure)
- **Error rates**: HTTP 5xx errors in your API

---

## LLM Infrastructure (09_llm_infrastructure.ipynb)

This newer notebook covers production LLM serving:

- **vLLM**: PagedAttention for high-throughput LLM inference (10-30x faster than naive serving)
- **TGI (Text Generation Inference)**: HuggingFace's production LLM server
- **Ollama**: Easy local LLM serving with OpenAI-compatible API
- **llama.cpp**: CPU inference for quantized models

**When to use what:**

| Scenario | Tool |
|----------|------|
| Local development | Ollama |
| Production, high throughput | vLLM |
| HuggingFace models in prod | TGI |
| CPU-only inference | llama.cpp |
| Managed cloud FM access | Bedrock / Azure AI Foundry / Vertex AI |

### Bedrock vs ONNX vs vLLM in One Sentence

- **Bedrock**: managed API for foundation models.
- **ONNX Runtime**: portable runtime for your own exported model.
- **vLLM**: high-throughput open-source LLM server for self-hosting.

---

## Practice Projects (Put These on GitHub)

**Project 1: Model API with Full MLOps**
- Train any classifier (e.g., sentiment analysis)
- Track experiment with MLflow
- Serve with FastAPI
- Containerize with Docker
- Add GitHub Actions to run tests on every push

**Project 2: LLM Serving Setup**
- Set up vLLM with a small model (Qwen2.5-1.5B)
- Create OpenAI-compatible endpoints
- Load test with Locust
- Monitor with basic Prometheus metrics

**Project 3: Model Monitoring Pipeline**
- Deploy a model
- Generate artificial drift in incoming data
- Detect and alert on drift
- Trigger retraining pipeline

---

## Interview Questions for MLOps

1. How do you detect data drift? What would you do when you detect it?
2. What's the difference between a model registry and an artifact store?
3. How does vLLM's PagedAttention improve throughput?
4. Walk me through how you'd deploy a new model version with zero downtime.
5. What's the difference between online and batch inference? When would you use each?

---

## External Resources

| Resource | Type | Link |
|----------|------|-------|
| Made With ML | Free Course | https://madewithml.com |
| Full Stack Deep Learning | Free Course | https://fullstackdeeplearning.com |
| MLflow Docs | Docs | https://mlflow.org/docs/latest/index.html |
| vLLM Docs | Docs | https://docs.vllm.ai |
| FastAPI Docs | Docs | https://fastapi.tiangolo.com |
| mlflow/mlflow | GitHub | https://github.com/mlflow/mlflow |
| vllm-project/vllm | GitHub | https://github.com/vllm-project/vllm |

---

## What to Learn Next

After MLOps, choose your specialization path:
- **AI Agents** → [15-ai-agents/](../15-ai-agents/)
- **LLM Fine-tuning** → [12-llm-finetuning/](../12-llm-finetuning/)
- **Computer Vision** → [10-specializations/computer-vision/](../10-specializations/computer-vision/)
- **Model Evaluation** → [16-model-evaluation/README.md](../16-model-evaluation/README.md) if you want stronger measurement and regression testing habits
- **Local LLMs** → [14-local-llms/README.md](../14-local-llms/README.md) if you want to own inference infrastructure directly
