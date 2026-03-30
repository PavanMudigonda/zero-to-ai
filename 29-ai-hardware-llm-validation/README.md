# Phase 29: AI Silicon Validation & Hardware-Software Co-Validation

## Overview

Master the end-to-end validation stack for AI accelerators — from bare-metal hardware bring-up to datacenter-scale deployment. 

**Duration:** 45–65 hours (9 sections, 9 detailed guides + exercises)

**Target Roles:**
- AI/ML Silicon Validation Engineer
- GPU/NPU/TPU Validation Engineer
- ML Performance Engineer
- AI Infra / Platform Validation Engineer
- AI Compiler & Runtime QA Engineer

---

## Learning Objectives

By the end of this phase, you will be able to:

- ✅ Validate power, thermals, memory, and stability of AI accelerators
- ✅ Write and run correctness tests for compute kernels (GEMM, conv, attention, softmax, layernorm)
- ✅ Validate ML framework integration (PyTorch, TensorFlow, ONNX Runtime) against hardware backends
- ✅ Benchmark and validate model performance for LLMs, CV, and speech workloads
- ✅ Design end-to-end pipeline validation (data ingestion → inference → postprocessing)
- ✅ Test distributed training across multi-GPU and multi-node setups (NCCL, RCCL)
- ✅ Validate AI workloads in datacenter environments (Kubernetes, scheduling, observability)
- ✅ Build regression suites, golden baselines, and cross-version release validation
- ✅ Understand industry benchmarks (AA-SLT, AA-AgentPerf, MLPerf, LMSys Arena) and how internal validation feeds them

---

## Prerequisites

- Solid Python programming skills
- Basic understanding of neural networks and deep learning (Phase 6)
- Familiarity with PyTorch or TensorFlow
- Linux command-line proficiency
- Helpful: C/C++, CUDA or HIP basics

---

## Module Structure

| # | Section | File | Duration |
|---|---------|------|----------|
| 1 | Hardware Validation | `01_hardware_validation.ipynb` | 5 hrs |
| 2 | Kernel Validation | `02_kernel_validation.ipynb` | 6 hrs |
| 3 | Framework Validation | `03_framework_validation.ipynb` | 5 hrs |
| 4 | Model Performance Validation | `04_model_performance_validation.ipynb` | 5 hrs |
| 5 | End-to-End Pipeline Validation | `05_e2e_pipeline_validation.ipynb` | 5 hrs |
| 6 | Distributed Training Validation | `06_distributed_training_validation.ipynb` | 5 hrs |
| 7 | Datacenter Validation | `07_datacenter_validation.ipynb` | 5 hrs |
| 8 | Regression & Release Validation | `08_regression_release_validation.ipynb` | 4 hrs |
| 9 | Industry Benchmarking & Performance Analysis | `09_benchmarking_industry.ipynb` | 4 hrs |

### Hands-On Labs

| # | Lab | File | Covers |
|---|-----|------|--------|
| 1 | Hardware Validation Lab | `lab_01_hardware_validation.ipynb` | GPU monitoring, thermal throttle detection, memory integrity |
| 2 | Kernel Validation Lab | `lab_02_kernel_validation.ipynb` | GEMM, softmax, LayerNorm, attention correctness testing |
| 3 | Model Performance Lab | `lab_03_model_performance.ipynb` | Throughput benchmarking, profiling, prefill vs decode |
| 4 | Regression Suite Lab | `lab_04_regression_suite.ipynb` | Golden baselines, version matrix, release gates |
| 5 | Distributed Training Lab | `lab_05_distributed_training.ipynb` | AllReduce simulation, scaling efficiency, health checks |
| 6 | Framework Validation Lab | `lab_06_framework_validation.ipynb` | PyTorch ops, ONNX export, torch.compile, execution modes |
| 7 | GPGPU Backends Lab | `lab_07_gpgpu_backends.ipynb` | CoreML, DirectML, Vulkan backend validation |
| 8 | Benchmarking Lab | `lab_08_benchmarking.ipynb` | AA-SLT simulation, SLO binary search, statistical testing |

---

## Learning Path

### Week 1–2: Hardware & Kernel Foundations
- [ ] Read `01_hardware_validation.ipynb` — power, thermals, memory, stability
- [ ] Complete `lab_01_hardware_validation.ipynb`
- [ ] Read `02_kernel_validation.ipynb` — GEMM, conv, attention, softmax, layernorm
- [ ] Complete `lab_02_kernel_validation.ipynb`
- [ ] Run stress tests on available GPU (nvidia-smi, rocm-smi)
- [ ] Write a simple GEMM correctness test comparing GPU vs CPU output

### Week 3: Framework & Model Validation
- [ ] Read `03_framework_validation.ipynb` — PyTorch, TensorFlow, ONNX Runtime backends
- [ ] Complete `lab_06_framework_validation.ipynb`
- [ ] Read `04_model_performance_validation.ipynb` — LLMs, CV, speech
- [ ] Complete `lab_03_model_performance.ipynb`
- [ ] Profile a model with `torch.profiler` and compare to baselines
- [ ] Export a model to ONNX and validate numerical parity

### Week 4: Pipeline, Distributed & Datacenter
- [ ] Read `05_e2e_pipeline_validation.ipynb` — data → model → postprocessing
- [ ] Read `06_distributed_training_validation.ipynb` — NCCL/RCCL, multi-GPU
- [ ] Complete `lab_05_distributed_training.ipynb`
- [ ] Read `07_datacenter_validation.ipynb` — Kubernetes, scheduling, monitoring
- [ ] Complete `lab_07_gpgpu_backends.ipynb`
- [ ] Run a multi-GPU training job and validate loss convergence

### Week 5: Regression, Release & Industry Benchmarks
- [ ] Read `08_regression_release_validation.ipynb` — baselines, cross-version testing
- [ ] Complete `lab_04_regression_suite.ipynb`
- [ ] Build a mini regression suite for a model + driver version matrix
- [ ] Read `09_benchmarking_industry.ipynb` — AA-SLT, AA-AgentPerf, MLPerf, LMSys Arena
- [ ] Complete `lab_08_benchmarking.ipynb` — build your own SLT and capacity planner
- [ ] Review the interview questions section and practice answers

---

## Company-Specific Focus Areas

| Company | Hardware | Key Validation Focus |
|---------|----------|---------------------|
| **AMD** | MI300X, MI325X, Instinct GPUs | ROCm stack, HIP kernels, RCCL, PyTorch/ROCm |
| **NVIDIA** | H100, H200, B100/B200, Grace Hopper | CUDA, cuDNN, NCCL, TensorRT, Triton |
| **Qualcomm** | Cloud AI 100, Snapdragon NPU | ONNX Runtime, QNN SDK, on-device inference |
| **Amazon Annapurna** | Trainium, Inferentia (trn1, inf2) | Neuron SDK, NeuronX Distributed, custom compiler |
| **Intel** | Gaudi 2/3, Ponte Vecchio | Habana SynapseAI, oneAPI, OpenVINO |
| **Google** | TPU v5e, v6e (Trillium) | JAX, XLA compiler, TPU runtime |
| **Apple** | M-series Neural Engine, ANE | Core ML, MLX framework |
| **Microsoft** | Maia 100 AI Accelerator | Custom silicon + Azure integration |

---

## Tools & Technologies

```bash
# GPU monitoring & stress testing
pip install gpustat pynvml

# Profiling & benchmarking
pip install torch torchvision torchaudio  # PyTorch ecosystem
pip install tensorflow                     # TensorFlow
pip install onnx onnxruntime               # ONNX
pip install triton                         # OpenAI Triton compiler

# Distributed training
pip install deepspeed                      # DeepSpeed
pip install fairscale                      # FairScale

# Datacenter / orchestration
pip install kubernetes                     # K8s Python client
pip install prometheus-client              # Metrics export
```

**System Tools (installed via package manager):**
- `nvidia-smi`, `rocm-smi` — GPU monitoring
- `nvprof`, `nsys`, `ncu` — NVIDIA profilers
- `rocprof`, `omniperf`, `omnitrace` — AMD profilers
- `stress-ng`, `memtester` — Hardware stress testing
- `docker`, `kubectl`, `helm` — Container orchestration

## Notebook Quality Checks

Before committing changes in this phase, run a lightweight structural check:

```bash
python validate_notebooks.py
```

This verifies that every notebook:
- parses as valid JSON
- uses `nbformat` 4+
- contains the expected code-cell fields
- has Python code cells that compile cleanly with `ast.parse`

It will catch notebook corruption and broken f-strings before they land in the repo.

---

## Interview Questions (All Sections)

### Hardware Validation
1. How do you validate that a GPU stays within its thermal design power (TDP) under sustained ML workloads?
2. Explain the difference between HBM bandwidth validation and PCIe bandwidth validation.
3. What is the role of ECC memory in AI accelerator validation?
4. How would you design a stress test that exercises all SMs/CUs simultaneously?

### Kernel Validation
5. How do you validate GEMM correctness when floating-point is non-associative?
6. Explain tolerance thresholds for FP16, BF16, FP8, and INT8 validation.
7. What is the difference between `atol` (absolute tolerance) and `rtol` (relative tolerance)?
8. How would you test a fused attention kernel for numerical correctness?

### Framework Validation
9. How do you validate that a PyTorch custom backend produces bit-accurate results?
10. Explain the ONNX opset versioning challenge for hardware vendors.
11. What are common failure modes when running TensorFlow models on non-NVIDIA hardware?

### Distributed Training
12. How do you validate NCCL/RCCL all-reduce correctness across 8 GPUs?
13. What metrics indicate a communication bottleneck in distributed training?
14. How would you debug a hang in a multi-node training job?

### Release & Regression
15. How do you build golden baselines for regression testing across driver versions?
16. Explain the concept of "performance regression" vs "correctness regression."
17. How would you design a CI/CD pipeline for validating a new GPU driver release?

### Industry Benchmarking
18. Explain the difference between TTFT and TTFAT. Why does it matter for reasoning models?
19. How does Artificial Analysis's AA-SLT benchmark detect throughput plateau?
20. What is the difference between AA-SLT (uniform workload) and AA-AgentPerf (real agent trajectories)?
21. Why does AA-AgentPerf use P25 output speed rather than median for SLO compliance?
22. How does MLPerf Inference's "Server" scenario differ from AA-AgentPerf's binary search approach?
23. Why is token normalization (to OpenAI tokens) necessary for fair cross-model speed comparison?
24. How do per-kW and per-$/hr normalizations help compare MI300X vs H100 for datacenter deployment?

---

## Real-World Applications

1. **New GPU Bring-Up**: Validating an MI300X from first silicon through production readiness
2. **Driver Release Testing**: Running 10,000+ test cases across CUDA/ROCm driver versions
3. **LLM Inference Serving**: Validating that Llama 3 produces correct output on Inferentia2
4. **Multi-Node Training**: Ensuring GPT-scale training converges identically on 256 GPUs vs 512 GPUs

---

## External Resources

### Courses & Documentation
- [AMD ROCm Documentation](https://rocm.docs.amd.com/)
- [NVIDIA CUDA Toolkit Documentation](https://docs.nvidia.com/cuda/)
- [AWS Neuron SDK Documentation](https://awsdocs-neuron.readthedocs-hosted.com/)
- [ONNX Runtime Documentation](https://onnxruntime.ai/docs/)
- [DeepSpeed Documentation](https://www.deepspeed.ai/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

### Papers & Talks
- "Dissecting Batched Group GEMM Kernels on GPUs" — AMD Research
- "Megatron-LM: Training Multi-Billion Parameter Language Models" — NVIDIA
- "Mixed Precision Training" — Micikevicius et al. (ICLR 2018)
- "An Empirical Study of Distributed Training" — Google Brain

### Community
- [AMD ROCm GitHub](https://github.com/ROCm)
- [NVIDIA Developer Forums](https://forums.developer.nvidia.com/)
- [PyTorch Forums — Hardware](https://discuss.pytorch.org/)

---

## Next Steps

- **Want to go deeper into MLOps?** → [09-mlops/](../09-mlops/)
- **Interested in LLM fine-tuning validation?** → [12-llm-finetuning/](../12-llm-finetuning/)
- **Need local GPU optimization?** → [14-local-llms/](../14-local-llms/)
- **Looking for model evaluation metrics?** → [16-model-evaluation/](../16-model-evaluation/)
