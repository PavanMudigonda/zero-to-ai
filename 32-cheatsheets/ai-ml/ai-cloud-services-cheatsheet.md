# AI/ML Cloud Services Cheatsheet

> CLI commands and patterns for AWS SageMaker, Azure Machine Learning, and GCP Vertex AI.

---

## Table of Contents

- [AWS SageMaker](#aws-sagemaker)
- [Azure Machine Learning](#azure-machine-learning)
- [GCP Vertex AI](#gcp-vertex-ai)
- [Cloud Comparison Matrix](#cloud-comparison-matrix)
- [Cost Optimization Tips](#cost-optimization-tips)
- [Interview Scenarios](#interview-scenarios)

---

## AWS SageMaker

### Setup

```bash
# Install SageMaker CLI/SDK
pip install sagemaker boto3

# Configure AWS credentials
aws configure
```

### Training Jobs

```bash
# Create a training job
aws sagemaker create-training-job \
  --training-job-name "my-training-$(date +%Y%m%d)" \
  --algorithm-specification '{
    "TrainingImage": "763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:2.0-gpu-py310",
    "TrainingInputMode": "File"
  }' \
  --role-arn "arn:aws:iam::123456789:role/SageMakerRole" \
  --input-data-config '[{
    "ChannelName": "training",
    "DataSource": {
      "S3DataSource": {
        "S3DataType": "S3Prefix",
        "S3Uri": "s3://my-bucket/data/train/",
        "S3DataDistributionType": "FullyReplicated"
      }
    }
  }]' \
  --output-data-config '{
    "S3OutputPath": "s3://my-bucket/output/"
  }' \
  --resource-config '{
    "InstanceCount": 1,
    "InstanceType": "ml.p3.2xlarge",
    "VolumeSizeInGB": 50
  }' \
  --stopping-condition '{"MaxRuntimeInSeconds": 86400}'

# Check training job status
aws sagemaker describe-training-job \
  --training-job-name "my-training-20240101"

# List training jobs
aws sagemaker list-training-jobs \
  --sort-by CreationTime --sort-order Descending --max-results 10
```

### SageMaker Python SDK (Higher-Level)

```python
import sagemaker
from sagemaker.pytorch import PyTorch

session = sagemaker.Session()
role = sagemaker.get_execution_role()

# Define estimator
estimator = PyTorch(
    entry_point="train.py",
    source_dir="src/",
    role=role,
    instance_count=1,
    instance_type="ml.p3.2xlarge",
    framework_version="2.0",
    py_version="py310",
    hyperparameters={
        "epochs": 10,
        "batch-size": 64,
        "learning-rate": 0.001,
    },
    use_spot_instances=True,            # Save up to 90% cost
    max_wait=7200,                       # Max wait for spot
    max_run=3600,                        # Max training time
    checkpoint_s3_uri="s3://bucket/checkpoints/",
)

# Start training
estimator.fit({
    "training": "s3://my-bucket/data/train/",
    "validation": "s3://my-bucket/data/val/",
})
```

### Endpoints

```bash
# Create a model
aws sagemaker create-model \
  --model-name "my-model" \
  --primary-container '{
    "Image": "763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:2.0-gpu-py310",
    "ModelDataUrl": "s3://my-bucket/output/model.tar.gz"
  }' \
  --execution-role-arn "arn:aws:iam::123456789:role/SageMakerRole"

# Create endpoint config
aws sagemaker create-endpoint-config \
  --endpoint-config-name "my-endpoint-config" \
  --production-variants '[{
    "VariantName": "primary",
    "ModelName": "my-model",
    "InstanceType": "ml.g4dn.xlarge",
    "InitialInstanceCount": 1,
    "InitialVariantWeight": 1.0
  }]'

# Create endpoint
aws sagemaker create-endpoint \
  --endpoint-name "my-endpoint" \
  --endpoint-config-name "my-endpoint-config"

# Invoke endpoint
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name "my-endpoint" \
  --content-type "application/json" \
  --body '{"instances": [[1.0, 2.0, 3.0, 4.0]]}' \
  output.json

# Delete endpoint (stop billing)
aws sagemaker delete-endpoint --endpoint-name "my-endpoint"
```

### SageMaker Processing Jobs (Data Processing)

```bash
aws sagemaker create-processing-job \
  --processing-job-name "data-processing-$(date +%Y%m%d)" \
  --processing-resources '{
    "ClusterConfig": {
      "InstanceCount": 1,
      "InstanceType": "ml.m5.xlarge",
      "VolumeSizeInGB": 30
    }
  }' \
  --app-specification '{
    "ImageUri": "763104351884.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn:1.2-1-cpu-py3",
    "ContainerEntrypoint": ["python3", "/opt/ml/processing/code/preprocess.py"]
  }' \
  --processing-inputs '[{
    "InputName": "raw-data",
    "S3Input": {
      "S3Uri": "s3://bucket/raw/",
      "LocalPath": "/opt/ml/processing/input",
      "S3DataType": "S3Prefix"
    }
  }]' \
  --processing-output-config '{
    "Outputs": [{
      "OutputName": "processed-data",
      "S3Output": {
        "S3Uri": "s3://bucket/processed/",
        "LocalPath": "/opt/ml/processing/output",
        "S3UploadMode": "EndOfJob"
      }
    }]
  }' \
  --role-arn "arn:aws:iam::123456789:role/SageMakerRole"
```

---

## Azure Machine Learning

### Setup

```bash
# Install Azure ML CLI extension
az extension add -n ml

# Create workspace
az ml workspace create \
  --name my-ml-workspace \
  --resource-group my-rg \
  --location eastus

# Set defaults
az configure --defaults group=my-rg workspace=my-ml-workspace
```

### Compute

```bash
# Create compute cluster (for training)
az ml compute create \
  --name gpu-cluster \
  --type AmlCompute \
  --size Standard_NC6s_v3 \
  --min-instances 0 \
  --max-instances 4 \
  --idle-time-before-scale-down 300

# Create compute instance (for development)
az ml compute create \
  --name dev-instance \
  --type ComputeInstance \
  --size Standard_DS3_v2

# List compute resources
az ml compute list -o table

# Stop compute instance (save costs)
az ml compute stop --name dev-instance
```

### Training Jobs

```yaml
# job.yml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: python train.py --epochs ${{inputs.epochs}} --lr ${{inputs.learning_rate}}
environment:
  image: mcr.microsoft.com/azureml/openmpi4.1.0-cuda11.8-cudnn8-ubuntu22.04
  conda_file: conda.yml
compute: azureml:gpu-cluster
inputs:
  epochs: 10
  learning_rate: 0.001
  training_data:
    type: uri_folder
    path: azureml:training-data@latest
code: ./src
experiment_name: my-experiment
```

```bash
# Submit a training job
az ml job create -f job.yml

# Submit a sweep job (hyperparameter tuning)
az ml job create -f sweep.yml

# Monitor job
az ml job show --name <job-name> -o table

# Stream job logs
az ml job stream --name <job-name>

# Download job outputs
az ml job download --name <job-name> --output-name model

# List recent jobs
az ml job list --max-results 10 -o table

# Cancel a job
az ml job cancel --name <job-name>
```

### Hyperparameter Sweep

```yaml
# sweep.yml
$schema: https://azuremlschemas.azureedge.net/latest/sweepJob.schema.json
type: sweep
trial:
  command: python train.py --lr ${{search_space.lr}} --batch-size ${{search_space.batch_size}}
  environment:
    image: mcr.microsoft.com/azureml/openmpi4.1.0-cuda11.8-cudnn8-ubuntu22.04
  code: ./src
  compute: azureml:gpu-cluster
search_space:
  lr:
    type: loguniform
    min_value: -5
    max_value: -1
  batch_size:
    type: choice
    values: [16, 32, 64, 128]
objective:
  primary_metric: val_accuracy
  goal: maximize
sampling_algorithm: bayesian
limits:
  max_total_trials: 20
  max_concurrent_trials: 4
  timeout: 7200
```

### Endpoints (Online Inference)

```yaml
# endpoint.yml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
name: fraud-endpoint
auth_mode: key
```

```yaml
# deployment.yml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: blue
endpoint_name: fraud-endpoint
model: azureml:fraud-model@latest
code_configuration:
  code: ./src
  scoring_script: score.py
environment:
  image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu22.04
  conda_file: conda.yml
instance_type: Standard_DS3_v2
instance_count: 1
```

```bash
# Create endpoint
az ml online-endpoint create -f endpoint.yml

# Create deployment
az ml online-deployment create -f deployment.yml --all-traffic

# Test endpoint
az ml online-endpoint invoke \
  --name fraud-endpoint \
  --request-file sample-request.json

# Scale deployment
az ml online-deployment update \
  --name blue \
  --endpoint fraud-endpoint \
  --instance-count 3

# Get endpoint scoring URI and key
az ml online-endpoint show --name fraud-endpoint
az ml online-endpoint get-credentials --name fraud-endpoint

# Delete endpoint (stop billing)
az ml online-endpoint delete --name fraud-endpoint --yes
```

### Data Assets

```bash
# Register a data asset
az ml data create \
  --name training-data \
  --version 1 \
  --type uri_folder \
  --path "https://mystorageaccount.blob.core.windows.net/data/train/"

# List data assets
az ml data list -o table
```

---

## GCP Vertex AI

### Setup

```bash
# Install Vertex AI SDK
pip install google-cloud-aiplatform

# Authenticate
gcloud auth application-default login

# Set project
gcloud config set project my-project-id
```

### Training (Custom)

```bash
# Submit a custom training job
gcloud ai custom-jobs create \
  --region=us-central1 \
  --display-name="my-training-job" \
  --worker-pool-spec=machine-type=n1-standard-8,accelerator-type=NVIDIA_TESLA_V100,accelerator-count=1,replica-count=1,container-image-uri=us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-0:latest \
  --args="--epochs=10,--lr=0.001"

# List training jobs
gcloud ai custom-jobs list --region=us-central1

# Describe a job
gcloud ai custom-jobs describe JOB_ID --region=us-central1
```

### Vertex AI Python SDK

```python
from google.cloud import aiplatform

aiplatform.init(project="my-project", location="us-central1")

# Custom training job
job = aiplatform.CustomTrainingJob(
    display_name="my-training",
    script_path="train.py",
    container_uri="us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-0:latest",
    requirements=["transformers", "datasets"],
)

model = job.run(
    replica_count=1,
    machine_type="n1-standard-8",
    accelerator_type="NVIDIA_TESLA_V100",
    accelerator_count=1,
)
```

### Endpoints

```bash
# Upload model
gcloud ai models upload \
  --region=us-central1 \
  --display-name="fraud-model" \
  --container-image-uri="us-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.2-0:latest" \
  --artifact-uri="gs://my-bucket/model/"

# Create endpoint
gcloud ai endpoints create \
  --region=us-central1 \
  --display-name="fraud-endpoint"

# Deploy model to endpoint
gcloud ai endpoints deploy-model ENDPOINT_ID \
  --region=us-central1 \
  --model=MODEL_ID \
  --display-name="fraud-v1" \
  --machine-type=n1-standard-4 \
  --accelerator-type=NVIDIA_TESLA_T4 \
  --accelerator-count=1 \
  --min-replica-count=1 \
  --max-replica-count=3

# Predict
gcloud ai endpoints predict ENDPOINT_ID \
  --region=us-central1 \
  --json-request=request.json

# Undeploy (stop billing)
gcloud ai endpoints undeploy-model ENDPOINT_ID \
  --region=us-central1 \
  --deployed-model-id=DEPLOYED_MODEL_ID
```

### Vertex AI Pipelines

```python
from kfp import dsl
from google.cloud import aiplatform

@dsl.pipeline(name="vertex-ml-pipeline")
def ml_pipeline(project: str, region: str):
    from google_cloud_pipeline_components.v1.custom_job import CustomTrainingJobOp
    from google_cloud_pipeline_components.v1.endpoint import (
        EndpointCreateOp,
        ModelDeployOp,
    )

    training_op = CustomTrainingJobOp(
        display_name="train",
        project=project,
        location=region,
        worker_pool_specs=[{
            "machine_spec": {
                "machine_type": "n1-standard-8",
                "accelerator_type": "NVIDIA_TESLA_V100",
                "accelerator_count": 1,
            },
            "replica_count": 1,
            "container_spec": {
                "image_uri": "gcr.io/my-project/training:latest",
            },
        }],
    )

aiplatform.init(project="my-project", location="us-central1")
job = aiplatform.PipelineJob(
    display_name="ml-pipeline",
    template_path="pipeline.json",
)
job.run()
```

---

## Cloud Comparison Matrix

| Feature | AWS SageMaker | Azure ML | GCP Vertex AI |
|---------|--------------|----------|---------------|
| **Managed Notebooks** | SageMaker Studio | Compute Instances | Workbench |
| **Training** | Training Jobs | Command Jobs | Custom Jobs |
| **HPO** | Automatic Model Tuning | Sweep Jobs | Vizier |
| **Model Registry** | Model Registry | Model Registry | Model Registry |
| **Real-time Inference** | Endpoints | Online Endpoints | Endpoints |
| **Batch Inference** | Batch Transform | Batch Endpoints | Batch Prediction |
| **Pipelines** | SageMaker Pipelines | Azure ML Pipelines | Vertex Pipelines |
| **Feature Store** | Feature Store | Managed Feature Store | Feature Store |
| **AutoML** | Autopilot | AutoML | AutoML |
| **GPU Cheapest** | ml.g4dn.xlarge (~$0.53/hr) | Standard_NC4as_T4_v3 (~$0.53/hr) | n1-standard-4 + T4 (~$0.55/hr) |

---

## Cost Optimization Tips

```bash
# AWS: Use spot instances (up to 90% savings)
# Set use_spot_instances=True in SageMaker estimator

# Azure: Use low-priority VMs
az ml compute create --name gpu-cluster --type AmlCompute \
  --size Standard_NC6s_v3 --tier low_priority

# GCP: Use preemptible VMs
gcloud ai custom-jobs create \
  --worker-pool-spec=machine-type=n1-standard-8,accelerator-type=NVIDIA_TESLA_V100,accelerator-count=1 \
  --enable-web-access

# All clouds: Auto-scale to zero when idle
# Set min-instances 0 for compute clusters

# All clouds: Right-size your instances
# Don't use A100 for fine-tuning small models
# Use T4 for inference, V100/A100 for training
```

---

## Interview Scenarios

**Q: How would you choose between AWS SageMaker, Azure ML, and GCP Vertex AI?**
> Consider: (1) existing cloud investment and team expertise, (2) specific features needed (e.g., Azure ML has best MLflow integration, SageMaker has broadest instance selection, Vertex AI has best AutoML), (3) pricing for your workload pattern, (4) compliance requirements, (5) integration with other services you use.

**Q: How do you manage costs for ML workloads in the cloud?**
> Key strategies: spot/preemptible instances for training (with checkpointing), auto-scale to zero for compute clusters, right-size GPU selection, reserved instances for steady-state inference, batch inference instead of real-time where possible, and use cloud cost monitoring tools (AWS Cost Explorer, Azure Cost Management, GCP Billing).
