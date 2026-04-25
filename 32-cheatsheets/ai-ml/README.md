# Cloud DevOps for AI/ML Engineers

> Everything an AI/ML learner needs to deploy, scale, and operate machine learning workloads in the cloud.

## Why This Chapter?

Most AI/ML courses teach you to build models in Jupyter notebooks—but shipping models to production requires **cloud infrastructure, MLOps pipelines, GPU management, and DevOps practices** tailored for ML workloads. This chapter bridges that gap.

---

## Table of Contents

| # | Cheatsheet | What You'll Learn |
|---|-----------|-------------------|
| 1 | [MLOps Fundamentals](mlops-cheatsheet.md) | ML lifecycle, CI/CD for ML, model registries, feature stores, versioning |
| 2 | [AI/ML Cloud Services](ai-cloud-services-cheatsheet.md) | AWS SageMaker, Azure ML, GCP Vertex AI, managed endpoints |
| 3 | [GPU & Compute Infrastructure](gpu-compute-cheatsheet.md) | GPU instances, CUDA, spot/preemptible instances, cost optimization |
| 4 | [ML Model Serving & Deployment](ml-model-serving-cheatsheet.md) | TorchServe, TF Serving, Triton, BentoML, FastAPI, scaling inference |
| 5 | [Experiment Tracking & Reproducibility](experiment-tracking-cheatsheet.md) | MLflow, Weights & Biases, DVC, experiment management |
| 6 | [Data Pipelines for ML](data-pipelines-cheatsheet.md) | Airflow, data lakes, ETL/ELT, streaming for ML, feature engineering |

---

## Learning Path

```
                    ┌──────────────────────┐
                    │  1. MLOps Fundamentals│
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                 ▼
   ┌──────────────┐  ┌────────────────┐  ┌────────────────┐
   │ 2. Cloud     │  │ 3. GPU &       │  │ 5. Experiment  │
   │    Services  │  │    Compute     │  │    Tracking    │
   └──────┬───────┘  └───────┬────────┘  └───────┬────────┘
          │                  │                    │
          └──────────────────┼────────────────────┘
                             ▼
              ┌──────────────────────────┐
              │ 4. Model Serving &       │
              │    Deployment            │
              └──────────┬───────────────┘
                         ▼
              ┌──────────────────────────┐
              │ 6. Data Pipelines for ML │
              └──────────────────────────┘
```

---

## Prerequisites

Before diving in, make sure you're comfortable with:

- **Docker** → See [Docker Cheatsheet](../docker/docker-commands-cheatsheet.md)
- **Kubernetes** → See [kubectl Cheatsheet](../k8s/kubectl-commands-cheatsheet.md)
- **Cloud CLIs** → See [AWS](../cloud/aws-cli-cheatsheet.md) / [Azure](../cloud/azure-cli-cheatsheet.md) / [GCP](../cloud/gcp-gcloud-cheatsheet.md)
- **Terraform** → See [Terraform Cheatsheet](../cloud/terraform-commands-cheatsheet.md)
- **CI/CD** → See [GitHub Actions](../github-actions/github-actions-cheatsheet.md)

---

## Key Differences: Traditional DevOps vs. ML DevOps

| Aspect | Traditional DevOps | ML DevOps (MLOps) |
|--------|-------------------|-------------------|
| **Artifacts** | Code packages, containers | Models, datasets, configs |
| **Testing** | Unit/integration tests | Data validation, model quality tests |
| **Versioning** | Code (Git) | Code + Data + Model + Params |
| **CI/CD** | Build → Test → Deploy | Train → Validate → Register → Deploy |
| **Monitoring** | Latency, errors, uptime | Data drift, model accuracy, prediction quality |
| **Compute** | CPU-focused | GPU/TPU-heavy, burst training |
| **Cost** | Predictable | Highly variable (training spikes) |

---

## Quick Start: Your First ML Deployment

```bash
# 1. Train a model locally
python train.py --epochs 10 --output model/

# 2. Track the experiment
mlflow run . --experiment-name my-first-model

# 3. Package in a container
docker build -t my-ml-model:v1 .

# 4. Push to a registry
docker push myregistry.azurecr.io/my-ml-model:v1

# 5. Deploy to cloud (Azure ML example)
az ml online-endpoint create --name my-endpoint -f endpoint.yml
az ml online-deployment create --name blue --endpoint my-endpoint -f deployment.yml

# 6. Test the endpoint
curl -X POST https://my-endpoint.region.inference.ml.azure.com/score \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"data": [[1.0, 2.0, 3.0, 4.0]]}'
```

---

## Interview Scenarios

**Q: How would you set up CI/CD for a machine learning project?**
> Use GitHub Actions / Azure DevOps to: (1) trigger on code or data changes, (2) run data validation and unit tests, (3) train the model in a cloud compute cluster, (4) evaluate against baseline metrics, (5) register the model if it passes, (6) deploy to a staging endpoint, (7) run integration tests, (8) promote to production with canary/blue-green strategy.

**Q: How do you handle GPU costs for ML training?**
> Use spot/preemptible instances for fault-tolerant training (with checkpointing), right-size GPU selection (don't use A100 for small models), auto-shutdown idle instances, reserved instances for predictable workloads, and multi-GPU training to reduce wall-clock time.

**Q: What's the difference between batch and real-time inference?**
> Batch: process large datasets on schedule (cost-efficient, high-throughput). Real-time: single predictions via API with low latency (< 100ms). Choose based on business requirements—recommendation engines often use batch, chatbots need real-time.
