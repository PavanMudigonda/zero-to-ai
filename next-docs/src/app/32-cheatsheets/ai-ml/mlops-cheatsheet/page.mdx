# MLOps Fundamentals Cheatsheet

> The practices, tools, and patterns for taking ML models from notebook to production.

---

## Table of Contents

- [ML Lifecycle Overview](#ml-lifecycle-overview)
- [CI/CD for ML](#cicd-for-ml)
- [Model Registry](#model-registry)
- [Data Versioning](#data-versioning)
- [Feature Stores](#feature-stores)
- [ML Pipeline Orchestration](#ml-pipeline-orchestration)
- [Model Monitoring](#model-monitoring)
- [MLOps Maturity Levels](#mlops-maturity-levels)
- [Interview Scenarios](#interview-scenarios)

---

## ML Lifecycle Overview

```
Data Collection → Data Validation → Feature Engineering → Model Training
      ↓                                                        ↓
Data Versioning                                         Experiment Tracking
                                                               ↓
                                                      Model Evaluation
                                                               ↓
                                                      Model Registry
                                                               ↓
                                                      Model Deployment
                                                               ↓
                                                      Model Monitoring
                                                               ↓
                                                      Retrain (loop back)
```

---

## CI/CD for ML

### GitHub Actions: ML Pipeline Example

```yaml
# .github/workflows/ml-pipeline.yml
name: ML Pipeline

on:
  push:
    paths:
      - 'src/**'
      - 'data/**'
      - 'configs/**'

jobs:
  data-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate data schema
        run: python scripts/validate_data.py

  train:
    needs: data-validation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Train model
        run: |
          pip install -r requirements.txt
          python train.py --config configs/prod.yaml
      - name: Upload model artifact
        uses: actions/upload-artifact@v4
        with:
          name: model
          path: outputs/model/

  evaluate:
    needs: train
    runs-on: ubuntu-latest
    steps:
      - name: Download model
        uses: actions/download-artifact@v4
        with:
          name: model
      - name: Evaluate against baseline
        run: python evaluate.py --model model/ --threshold 0.85

  register:
    needs: evaluate
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Register model
        run: |
          mlflow models register \
            --model-uri runs:/$RUN_ID/model \
            --name production-model
```

### Azure DevOps: ML Pipeline

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include: [main]
  paths:
    include: [src/*, data/*, configs/*]

stages:
  - stage: Train
    jobs:
      - job: TrainModel
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: '3.11'
          - script: |
              pip install -r requirements.txt
              python train.py
          - publish: $(System.DefaultWorkingDirectory)/outputs
            artifact: model

  - stage: Deploy
    dependsOn: Train
    condition: succeeded()
    jobs:
      - deployment: DeployModel
        environment: 'production'
        strategy:
          runOnce:
            deploy:
              steps:
                - script: |
                    az ml online-deployment create \
                      --name blue \
                      --endpoint prod-endpoint \
                      -f deployment.yml
```

---

## Model Registry

### MLflow Model Registry

```bash
# Register a model
mlflow models register \
  --model-uri "runs:/abc123/model" \
  --name "fraud-detector"

# Transition model stage
mlflow models transition-stage \
  --name "fraud-detector" \
  --version 3 \
  --stage "Production"

# List models
mlflow models list --name "fraud-detector"

# Download a model
mlflow models download \
  --model-uri "models:/fraud-detector/Production" \
  --dst-path ./model
```

### Azure ML Model Registry

```bash
# Register a model
az ml model create \
  --name fraud-detector \
  --version 1 \
  --path ./model \
  --type mlflow_model

# List model versions
az ml model list --name fraud-detector

# Show model details
az ml model show --name fraud-detector --version 1
```

### AWS SageMaker Model Registry

```bash
# Create model package group
aws sagemaker create-model-package-group \
  --model-package-group-name "fraud-detector"

# Register model
aws sagemaker create-model-package \
  --model-package-group-name "fraud-detector" \
  --model-approval-status "PendingManualApproval" \
  --inference-specification '{
    "Containers": [{
      "Image": "123456789.dkr.ecr.us-east-1.amazonaws.com/model:latest",
      "ModelDataUrl": "s3://bucket/model.tar.gz"
    }],
    "SupportedContentTypes": ["application/json"],
    "SupportedResponseMIMETypes": ["application/json"]
  }'

# Approve model
aws sagemaker update-model-package \
  --model-package-arn "arn:aws:sagemaker:..." \
  --model-approval-status "Approved"
```

---

## Data Versioning

### DVC (Data Version Control)

```bash
# Initialize DVC in a Git repo
dvc init

# Track a large dataset
dvc add data/training_data.csv
git add data/training_data.csv.dvc data/.gitignore
git commit -m "Track training data v1"

# Configure remote storage
dvc remote add -d myremote s3://my-bucket/dvc-store

# Push data to remote
dvc push

# Pull data from remote
dvc pull

# Switch to a different data version
git checkout v2.0
dvc checkout

# Compare metrics across experiments
dvc metrics diff

# Create a reproducible pipeline
dvc run -n train \
  -d src/train.py -d data/train.csv \
  -o model/model.pkl \
  -m metrics.json \
  python src/train.py
```

### DVC Pipeline (dvc.yaml)

```yaml
stages:
  prepare:
    cmd: python src/prepare.py
    deps:
      - src/prepare.py
      - data/raw/
    outs:
      - data/processed/

  train:
    cmd: python src/train.py
    deps:
      - src/train.py
      - data/processed/
    outs:
      - model/
    metrics:
      - metrics.json:
          cache: false
    plots:
      - plots/training_loss.csv:
          x: epoch
          y: loss

  evaluate:
    cmd: python src/evaluate.py
    deps:
      - src/evaluate.py
      - model/
      - data/test/
    metrics:
      - eval_metrics.json:
          cache: false
```

---

## Feature Stores

### Feast (Open Source Feature Store)

```python
# feature_store.yaml
project: fraud_detection
registry: data/registry.db
provider: local
online_store:
  type: sqlite
  path: data/online_store.db
```

```python
# feature_repo/features.py
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64
from datetime import timedelta

# Define entity
customer = Entity(name="customer_id", join_keys=["customer_id"])

# Define data source
customer_stats_source = FileSource(
    path="data/customer_stats.parquet",
    timestamp_field="event_timestamp",
)

# Define feature view
customer_stats_fv = FeatureView(
    name="customer_stats",
    entities=[customer],
    ttl=timedelta(days=1),
    schema=[
        Field(name="total_transactions", dtype=Int64),
        Field(name="avg_transaction_amount", dtype=Float32),
        Field(name="days_since_last_transaction", dtype=Int64),
    ],
    source=customer_stats_source,
)
```

```bash
# Apply feature definitions
feast apply

# Materialize features to online store
feast materialize-incremental $(date -u +"%Y-%m-%dT%H:%M:%S")
```

```python
# Retrieve features for training
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo/")

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "customer_stats:total_transactions",
        "customer_stats:avg_transaction_amount",
    ],
).to_df()

# Retrieve features for inference (online)
feature_vector = store.get_online_features(
    features=[
        "customer_stats:total_transactions",
        "customer_stats:avg_transaction_amount",
    ],
    entity_rows=[{"customer_id": 1001}],
).to_dict()
```

---

## ML Pipeline Orchestration

### Kubeflow Pipelines

```python
from kfp import dsl, compiler

@dsl.component(base_image="python:3.11")
def preprocess(data_path: str) -> str:
    # Preprocess data
    import pandas as pd
    df = pd.read_csv(data_path)
    processed_path = "/tmp/processed.csv"
    df.dropna().to_csv(processed_path, index=False)
    return processed_path

@dsl.component(base_image="python:3.11-slim",
               packages_to_install=["scikit-learn"])
def train(data_path: str) -> str:
    from sklearn.ensemble import RandomForestClassifier
    import joblib, pandas as pd
    df = pd.read_csv(data_path)
    X, y = df.drop("target", axis=1), df["target"]
    model = RandomForestClassifier().fit(X, y)
    model_path = "/tmp/model.joblib"
    joblib.dump(model, model_path)
    return model_path

@dsl.pipeline(name="ml-training-pipeline")
def ml_pipeline(data_path: str = "gs://bucket/data.csv"):
    preprocess_task = preprocess(data_path=data_path)
    train_task = train(data_path=preprocess_task.output)

compiler.Compiler().compile(ml_pipeline, "pipeline.yaml")
```

### Apache Airflow for ML

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "ml-team",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "ml_training_dag",
    default_args=default_args,
    schedule_interval="@weekly",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    def validate_data(**kwargs):
        import great_expectations as gx
        context = gx.get_context()
        result = context.run_checkpoint("data_quality")
        if not result.success:
            raise ValueError("Data validation failed")

    def train_model(**kwargs):
        import mlflow
        with mlflow.start_run():
            # Training logic here
            mlflow.log_metric("accuracy", 0.95)
            mlflow.sklearn.log_model(model, "model")

    def deploy_model(**kwargs):
        import subprocess
        subprocess.run([
            "az", "ml", "online-deployment", "create",
            "--name", "blue", "--endpoint", "prod",
            "-f", "deployment.yml"
        ], check=True)

    validate = PythonOperator(task_id="validate_data", python_callable=validate_data)
    train = PythonOperator(task_id="train_model", python_callable=train_model)
    deploy = PythonOperator(task_id="deploy_model", python_callable=deploy_model)

    validate >> train >> deploy
```

---

## Model Monitoring

### Data Drift Detection (Evidently)

```python
import evidently
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset

# Compare training data vs. production data
report = Report(metrics=[
    DataDriftPreset(),
    DataQualityPreset(),
])

report.run(reference_data=train_df, current_data=prod_df)
report.save_html("drift_report.html")
```

### Prometheus Metrics for ML Models

```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Define ML-specific metrics
PREDICTION_COUNT = Counter(
    "model_predictions_total",
    "Total predictions made",
    ["model_name", "model_version"]
)

PREDICTION_LATENCY = Histogram(
    "model_prediction_latency_seconds",
    "Time to generate prediction",
    ["model_name"]
)

PREDICTION_CONFIDENCE = Histogram(
    "model_prediction_confidence",
    "Prediction confidence scores",
    ["model_name"],
    buckets=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
)

DATA_DRIFT_SCORE = Gauge(
    "model_data_drift_score",
    "Data drift score (0=no drift, 1=full drift)",
    ["model_name", "feature_name"]
)

# Use in prediction endpoint
import time

def predict(request):
    start = time.time()
    result = model.predict(request.data)
    latency = time.time() - start

    PREDICTION_COUNT.labels(model_name="fraud", model_version="v3").inc()
    PREDICTION_LATENCY.labels(model_name="fraud").observe(latency)
    PREDICTION_CONFIDENCE.labels(model_name="fraud").observe(result.confidence)

    return result
```

### Grafana Dashboard Queries (PromQL for ML)

```promql
# Prediction throughput (requests/sec)
rate(model_predictions_total[5m])

# P99 latency
histogram_quantile(0.99, rate(model_prediction_latency_seconds_bucket[5m]))

# Average confidence score
histogram_quantile(0.5, rate(model_prediction_confidence_bucket[5m]))

# Drift alert (threshold > 0.3)
model_data_drift_score > 0.3
```

---

## MLOps Maturity Levels

| Level | Description | Characteristics |
|-------|------------|-----------------|
| **0 - No MLOps** | Manual everything | Jupyter notebooks, manual deployment, no monitoring |
| **1 - DevOps (no MLOps)** | Basic CI/CD | Automated tests, container builds, but manual ML steps |
| **2 - Automated Training** | ML pipeline | Automated training, experiment tracking, model registry |
| **3 - Automated Deployment** | Full CI/CD for ML | Auto-deploy on model approval, A/B testing, canary releases |
| **4 - Full MLOps** | Closed loop | Auto-retrain on drift, feature store, full observability |

---

## Essential Tools Comparison

| Category | Tools |
|----------|-------|
| **Experiment Tracking** | MLflow, Weights & Biases, Neptune, Comet |
| **Pipeline Orchestration** | Kubeflow, Airflow, Prefect, Dagster, ZenML |
| **Feature Store** | Feast, Tecton, Hopsworks |
| **Model Registry** | MLflow, Azure ML, SageMaker, Vertex AI |
| **Data Versioning** | DVC, LakeFS, Delta Lake |
| **Model Serving** | TorchServe, TF Serving, Triton, BentoML, Seldon |
| **Monitoring** | Evidently, WhyLabs, Arize, Fiddler |
| **Data Validation** | Great Expectations, Pandera, TFX Data Validation |

---

## Interview Scenarios

**Q: Walk me through how you would set up MLOps for a new ML project.**
> Start with Level 1: version control (Git), experiment tracking (MLflow), reproducible environments (Docker). Then Level 2: automate training pipelines (Airflow/Kubeflow), set up model registry. Level 3: CI/CD for models (GitHub Actions), automated deployment with A/B testing. Level 4: monitoring (Evidently for drift, Prometheus/Grafana for metrics), automated retraining triggers.

**Q: How do you handle model versioning?**
> Three things need versioning: (1) Code via Git, (2) Data via DVC or Delta Lake, (3) Model artifacts via MLflow/cloud model registry. Each training run should log: code commit hash, data version, hyperparameters, metrics, and the model artifact. Use semantic versioning for production models (major = breaking changes, minor = improvements, patch = bug fixes).

**Q: How do you detect and handle data drift in production?**
> Monitor input feature distributions using statistical tests (KS test, PSI, chi-squared). Set up Evidently or WhyLabs to compare production data against training data reference. Alert when drift score exceeds threshold. Response: investigate root cause, retrain with recent data if needed, update feature preprocessing if schema changed.
