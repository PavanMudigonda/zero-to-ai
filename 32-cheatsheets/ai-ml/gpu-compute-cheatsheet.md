# GPU & Compute Infrastructure Cheatsheet

> Managing GPUs, CUDA, and compute resources for ML training and inference.

---

## Table of Contents

- [GPU Types & Selection Guide](#gpu-types--selection-guide)
- [CUDA & NVIDIA Tools](#cuda--nvidia-tools)
- [Docker with GPU Support](#docker-with-gpu-support)
- [Kubernetes GPU Scheduling](#kubernetes-gpu-scheduling)
- [Spot/Preemptible Instances](#spotpreemptible-instances)
- [Multi-GPU & Distributed Training](#multi-gpu--distributed-training)
- [Cost Optimization](#cost-optimization)
- [Interview Scenarios](#interview-scenarios)

---

## GPU Types & Selection Guide

### Common GPU Instances

| GPU | VRAM | Use Case | AWS | Azure | GCP |
|-----|------|----------|-----|-------|-----|
| **T4** | 16 GB | Inference, small training | g4dn.xlarge | NC4as_T4_v3 | n1-standard-4 + T4 |
| **V100** | 16/32 GB | Training medium models | p3.2xlarge | NC6s_v3 | n1-standard-8 + V100 |
| **A10G** | 24 GB | Training + inference | g5.xlarge | NV36ads_A10_v5 | a2-highgpu-1g |
| **A100** | 40/80 GB | Large model training, LLMs | p4d.24xlarge | NC24ads_A100_v4 | a2-highgpu-1g |
| **H100** | 80 GB | LLM training, frontier models | p5.48xlarge | NC40ads_H100_v5 | a3-highgpu-1g |

### How to Choose

```
Small models (< 1B params):     T4 or V100 (16GB)
Medium models (1B-7B params):   A10G or V100 (32GB)
Large models (7B-30B params):   A100 (40/80GB)
Frontier models (30B+ params):  H100 or multi-A100
Inference only:                 T4 (best price/performance)
```

---

## CUDA & NVIDIA Tools

### Check GPU Status

```bash
# GPU info and utilization
nvidia-smi

# Watch GPU usage in real-time (refresh every 1 second)
nvidia-smi -l 1
# or
watch -n 1 nvidia-smi

# Detailed GPU info
nvidia-smi -q

# Check CUDA version
nvcc --version

# Check cuDNN version
cat /usr/local/cuda/include/cudnn_version.h | grep CUDNN_MAJOR -A 2

# List available GPUs (PyTorch)
python -c "import torch; print(torch.cuda.device_count()); print(torch.cuda.get_device_name(0))"

# Check GPU memory (PyTorch)
python -c "
import torch
for i in range(torch.cuda.device_count()):
    print(f'GPU {i}: {torch.cuda.get_device_name(i)}')
    print(f'  Memory: {torch.cuda.get_device_properties(i).total_mem / 1e9:.1f} GB')
"
```

### CUDA Toolkit Installation

```bash
# Ubuntu 22.04 - CUDA 12.x
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-4

# Add to PATH
echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

### GPU Memory Management (PyTorch)

```python
import torch

# Clear GPU cache
torch.cuda.empty_cache()

# Check memory usage
print(f"Allocated: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
print(f"Cached: {torch.cuda.memory_reserved() / 1e9:.2f} GB")

# Enable memory-efficient attention (for transformers)
# Use Flash Attention 2
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b",
    torch_dtype=torch.float16,
    attn_implementation="flash_attention_2",
)

# Gradient checkpointing (trade compute for memory)
model.gradient_checkpointing_enable()

# Mixed precision training
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()

for batch in dataloader:
    optimizer.zero_grad()
    with autocast():
        output = model(batch)
        loss = criterion(output, targets)
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

---

## Docker with GPU Support

### NVIDIA Container Toolkit Setup

```bash
# Install NVIDIA Container Toolkit
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | \
  sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

### Running GPU Containers

```bash
# Run with GPU access
docker run --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi

# Run with specific GPU(s)
docker run --gpus '"device=0"' my-ml-image:latest
docker run --gpus '"device=0,1"' my-ml-image:latest

# Run with shared memory (needed for PyTorch DataLoader)
docker run --gpus all --shm-size=8g my-ml-image:latest

# Full ML training container
docker run --gpus all \
  --shm-size=16g \
  -v $(pwd)/data:/data \
  -v $(pwd)/model:/model \
  -e CUDA_VISIBLE_DEVICES=0,1 \
  my-training-image:latest \
  python train.py --epochs 10
```

### GPU Dockerfile

```dockerfile
FROM nvidia/cuda:12.4.0-cudnn-runtime-ubuntu22.04

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install ML dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy code
COPY src/ /app/src/
WORKDIR /app

CMD ["python3", "src/train.py"]
```

---

## Kubernetes GPU Scheduling

### GPU Node Pool (AKS)

```bash
# Create GPU node pool
az aks nodepool add \
  --resource-group my-rg \
  --cluster-name my-cluster \
  --name gpupool \
  --node-count 2 \
  --node-vm-size Standard_NC6s_v3 \
  --node-taints sku=gpu:NoSchedule

# Install NVIDIA device plugin
kubectl apply -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.15.0/deployments/static/nvidia-device-plugin.yml
```

### GPU Pod Spec

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ml-training
spec:
  containers:
    - name: trainer
      image: my-training-image:latest
      resources:
        limits:
          nvidia.com/gpu: 1       # Request 1 GPU
        requests:
          memory: "16Gi"
          cpu: "4"
      volumeMounts:
        - name: shm
          mountPath: /dev/shm
  volumes:
    - name: shm                    # Shared memory for PyTorch
      emptyDir:
        medium: Memory
        sizeLimit: "8Gi"
  tolerations:
    - key: "sku"
      operator: "Equal"
      value: "gpu"
      effect: "NoSchedule"
  nodeSelector:
    accelerator: nvidia-tesla-v100
```

### GPU Training Job (Kubernetes)

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: model-training
spec:
  backoffLimit: 3
  template:
    spec:
      restartPolicy: OnFailure
      containers:
        - name: trainer
          image: myregistry.azurecr.io/ml-trainer:v1
          command: ["python", "train.py", "--epochs", "50"]
          resources:
            limits:
              nvidia.com/gpu: 2
            requests:
              memory: "32Gi"
              cpu: "8"
          env:
            - name: CUDA_VISIBLE_DEVICES
              value: "0,1"
            - name: NCCL_DEBUG
              value: "INFO"
          volumeMounts:
            - name: data
              mountPath: /data
            - name: shm
              mountPath: /dev/shm
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: training-data-pvc
        - name: shm
          emptyDir:
            medium: Memory
            sizeLimit: "16Gi"
```

---

## Spot/Preemptible Instances

### AWS Spot Instances

```bash
# Request spot instance
aws ec2 request-spot-instances \
  --spot-price "1.50" \
  --instance-count 1 \
  --type "one-time" \
  --launch-specification '{
    "ImageId": "ami-0abcdef1234567890",
    "InstanceType": "p3.2xlarge",
    "KeyName": "my-key"
  }'

# SageMaker with spot (in Python SDK)
# use_spot_instances=True, max_wait=7200
# Always implement checkpointing!
```

### Azure Low-Priority VMs

```bash
# Spot VM
az vm create \
  --name ml-spot-vm \
  --resource-group my-rg \
  --image Ubuntu2204 \
  --size Standard_NC6s_v3 \
  --priority Spot \
  --eviction-policy Deallocate \
  --max-price 0.50

# AKS Spot Node Pool
az aks nodepool add \
  --resource-group my-rg \
  --cluster-name my-cluster \
  --name spotgpu \
  --priority Spot \
  --eviction-policy Delete \
  --spot-max-price -1 \
  --node-vm-size Standard_NC6s_v3 \
  --node-count 3
```

### GCP Preemptible VMs

```bash
# Create preemptible GPU instance
gcloud compute instances create ml-training-vm \
  --zone=us-central1-a \
  --machine-type=n1-standard-8 \
  --accelerator=type=nvidia-tesla-v100,count=1 \
  --preemptible \
  --maintenance-policy=TERMINATE \
  --image-family=pytorch-latest-gpu \
  --image-project=deeplearning-platform-release \
  --boot-disk-size=200GB
```

### Checkpointing Pattern (Essential for Spot)

```python
import torch
import os

def save_checkpoint(model, optimizer, epoch, loss, path="checkpoint.pt"):
    torch.save({
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
        "loss": loss,
    }, path)

def load_checkpoint(model, optimizer, path="checkpoint.pt"):
    if os.path.exists(path):
        checkpoint = torch.load(path)
        model.load_state_dict(checkpoint["model_state_dict"])
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        return checkpoint["epoch"], checkpoint["loss"]
    return 0, float("inf")

# Training loop with checkpointing
start_epoch, best_loss = load_checkpoint(model, optimizer)
for epoch in range(start_epoch, num_epochs):
    loss = train_one_epoch(model, dataloader, optimizer)
    if loss < best_loss:
        best_loss = loss
        save_checkpoint(model, optimizer, epoch, loss)
    # Save every N epochs regardless
    if epoch % 5 == 0:
        save_checkpoint(model, optimizer, epoch, loss,
                       f"checkpoint_epoch_{epoch}.pt")
```

---

## Multi-GPU & Distributed Training

### PyTorch Distributed Data Parallel (DDP)

```python
import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

def setup(rank, world_size):
    dist.init_process_group("nccl", rank=rank, world_size=world_size)
    torch.cuda.set_device(rank)

def train(rank, world_size):
    setup(rank, world_size)
    model = MyModel().to(rank)
    model = DDP(model, device_ids=[rank])

    sampler = torch.utils.data.distributed.DistributedSampler(
        dataset, num_replicas=world_size, rank=rank
    )
    dataloader = torch.utils.data.DataLoader(
        dataset, sampler=sampler, batch_size=32
    )

    for epoch in range(num_epochs):
        sampler.set_epoch(epoch)
        for batch in dataloader:
            loss = model(batch.to(rank))
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

    dist.destroy_process_group()

# Launch distributed training
# torchrun --nproc_per_node=4 train.py
```

### DeepSpeed (for Large Models)

```python
import deepspeed

model, optimizer, _, _ = deepspeed.initialize(
    model=model,
    model_parameters=model.parameters(),
    config={
        "train_batch_size": 64,
        "gradient_accumulation_steps": 4,
        "fp16": {"enabled": True},
        "zero_optimization": {
            "stage": 2,        # ZeRO Stage 2
            "offload_optimizer": {
                "device": "cpu"  # Offload to CPU to save GPU memory
            }
        },
    }
)

for batch in dataloader:
    loss = model(batch)
    model.backward(loss)
    model.step()
```

```bash
# Launch with DeepSpeed
deepspeed --num_gpus=4 train.py --deepspeed_config ds_config.json

# Multi-node training
deepspeed --hostfile=hostfile --num_gpus=8 train.py
```

---

## Cost Optimization

### Quick Reference

| Strategy | Savings | Risk |
|----------|---------|------|
| **Spot/Preemptible** | 60-90% | Instance can be terminated |
| **Reserved Instances** | 30-60% | Upfront commitment |
| **Auto-scale to zero** | Variable | Cold start latency |
| **Right-size GPU** | 20-50% | May need testing |
| **Mixed precision (FP16)** | 2x throughput | Slight accuracy change |
| **Gradient accumulation** | Use smaller GPUs | Slower training |
| **Distillation** | Smaller model for inference | Some accuracy loss |

### Monitoring GPU Costs

```bash
# AWS: Check GPU instance costs
aws ce get-cost-and-usage \
  --time-period Start=2024-01-01,End=2024-02-01 \
  --granularity MONTHLY \
  --metrics BlendedCost \
  --filter '{"Dimensions":{"Key":"INSTANCE_TYPE","Values":["p3.2xlarge","g4dn.xlarge"]}}'

# Azure: Check ML workspace costs
az consumption usage list \
  --start-date 2024-01-01 --end-date 2024-02-01 \
  --query "[?contains(instanceName,'gpu')]"

# GCP: Check compute costs
gcloud billing accounts list
gcloud beta billing budgets list --billing-account=ACCOUNT_ID
```

---

## Interview Scenarios

**Q: How do you handle GPU out-of-memory errors during training?**
> Progressive approach: (1) reduce batch size, (2) enable mixed precision (FP16/BF16), (3) enable gradient checkpointing, (4) use gradient accumulation, (5) use DeepSpeed ZeRO, (6) use model parallelism, (7) switch to a larger GPU.

**Q: How do you decide between single-GPU and multi-GPU training?**
> Consider: dataset size, model size, and time budget. If training fits in one GPU's memory and completes in acceptable time, single GPU is simpler. Use multi-GPU when: model doesn't fit in one GPU (model parallelism), or you need to reduce training time (data parallelism). Use distributed training across nodes for very large models.

**Q: How do you optimize inference costs for a deployed ML model?**
> Use T4 GPUs for inference (best price/performance), enable model quantization (FP16 or INT8), batch requests when possible, auto-scale based on traffic (scale to zero during off-hours), use spot instances for non-latency-critical inference, and consider model distillation to create a smaller, faster model.
