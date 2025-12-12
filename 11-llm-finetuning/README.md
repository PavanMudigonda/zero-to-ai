# Phase 11: LLM Fine-tuning & Training

## 🎯 Overview

Learn to customize and train Large Language Models for your specific needs. Master cost-effective fine-tuning techniques like LoRA, QLoRA, and PEFT to adapt powerful models without massive compute.

**Prerequisites:**
- ✅ Neural Networks (Phase 5)
- ✅ Transformers understanding
- ✅ Python & PyTorch basics
- ✅ Prompt Engineering (Phase 10)

**Time:** 3-4 weeks | 60-80 hours  
**Outcome:** Fine-tune models for custom tasks, understand RLHF, deploy specialized LLMs

---

## 📚 What You'll Learn

### Fine-tuning Fundamentals

- [ ] When to fine-tune vs. prompt engineer
- [ ] Full fine-tuning vs. parameter-efficient methods
- [ ] Dataset preparation and formatting
- [ ] Supervised fine-tuning (SFT)
- [ ] Instruction tuning
- [ ] Evaluation and benchmarking

### Parameter-Efficient Fine-Tuning (PEFT)

- [ ] LoRA (Low-Rank Adaptation)
- [ ] QLoRA (Quantized LoRA)
- [ ] Adapter layers
- [ ] Prefix tuning
- [ ] P-tuning and prompt tuning
- [ ] IA3 (Infused Adapter by Inhibiting and Amplifying)

### Advanced Techniques

- [ ] RLHF (Reinforcement Learning from Human Feedback)
- [ ] DPO (Direct Preference Optimization)
- [ ] Constitutional AI principles
- [ ] Multi-task fine-tuning
- [ ] Continual learning and catastrophic forgetting
- [ ] Merging fine-tuned models

### Production Deployment

- [ ] Model quantization (4-bit, 8-bit)
- [ ] Model compression and distillation
- [ ] Serving fine-tuned models
- [ ] Cost optimization strategies
- [ ] Monitoring and evaluation

---

## 🗂️ Module Structure

```
11-llm-finetuning/
├── 00_START_HERE.ipynb                    # Overview & decision tree
├── 01_dataset_preparation.ipynb           # Data formatting
├── 02_supervised_finetuning.ipynb         # Basic SFT
├── 03_lora_basics.ipynb                   # LoRA fundamentals
├── 04_qlora_efficient.ipynb               # QLoRA for consumer GPUs
├── 05_instruction_tuning.ipynb            # Instruction datasets
├── 06_evaluation.ipynb                    # Testing fine-tuned models
├── 07_rlhf_dpo.ipynb                      # Alignment techniques
├── 08_deployment.ipynb                    # Production deployment
├── projects/
│   ├── custom_chatbot.py                  # Domain-specific assistant
│   ├── code_completion.py                 # Code model fine-tune
│   ├── sentiment_classifier.py            # Classification task
│   └── summarization_model.py             # Summarization fine-tune
├── datasets/
│   ├── instruction_examples.jsonl
│   ├── conversational_data.jsonl
│   └── task_specific_examples.jsonl
└── scripts/
    ├── prepare_data.py
    ├── train_lora.py
    ├── merge_adapters.py
    └── quantize_model.py
```

---

## 🚀 Quick Start

### Decision Tree: Should You Fine-tune?

```python
def should_fine_tune(task):
    """Decide if fine-tuning is needed."""
    
    # Try this first:
    if can_solve_with_prompting(task):
        return "Use prompt engineering (cheaper, faster)"
    
    # If you have labeled data:
    if have_labeled_data(task) and need_consistent_format(task):
        return "Fine-tune (better accuracy, lower latency)"
    
    # If you need domain expertise:
    if need_specialized_knowledge(task):
        return "RAG + Fine-tuning (best of both)"
    
    # If you want behavior change:
    if need_different_behavior(task):
        return "RLHF or DPO (alignment)"
    
    return "Start with prompting, fine-tune if needed"
```

### LoRA Fine-tuning Example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset

# Load base model (4-bit quantized)
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    load_in_4bit=True,
    device_map="auto"
)

# Configure LoRA
lora_config = LoraConfig(
    r=16,                    # Rank
    lora_alpha=32,           # Scaling factor
    target_modules=["q_proj", "v_proj"],  # Which layers
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# Apply LoRA
model = prepare_model_for_kbit_training(model)
model = get_peft_model(model, lora_config)

# Train (only LoRA parameters update!)
# ~1% of parameters, 10x faster, same GPU
```

---

## 📋 Learning Path

### Week 1: Fundamentals & Data

- [ ] Complete `00_START_HERE.ipynb`
- [ ] Learn data prep in `01_dataset_preparation.ipynb`
- [ ] Basic fine-tuning in `02_supervised_finetuning.ipynb`
- [ ] **Project:** Prepare your own dataset

### Week 2: Efficient Fine-tuning

- [ ] Master LoRA in `03_lora_basics.ipynb`
- [ ] QLoRA techniques in `04_qlora_efficient.ipynb`
- [ ] Instruction tuning in `05_instruction_tuning.ipynb`
- [ ] **Project:** Fine-tune Llama-2 with LoRA

### Week 3: Evaluation & Alignment

- [ ] Evaluation methods in `06_evaluation.ipynb`
- [ ] RLHF/DPO in `07_rlhf_dpo.ipynb`
- [ ] Compare different techniques
- [ ] **Project:** Build aligned chatbot

### Week 4: Production

- [ ] Deployment in `08_deployment.ipynb`
- [ ] Optimize and quantize models
- [ ] Monitor performance
- [ ] **Capstone:** Production-ready custom model

---

## 🛠️ Technologies You'll Use

**Frameworks:**
- Hugging Face Transformers
- PEFT (Parameter-Efficient Fine-Tuning)
- TRL (Transformer Reinforcement Learning)
- Axolotl (fine-tuning framework)

**Training Infrastructure:**
- PyTorch / PyTorch Lightning
- Accelerate (distributed training)
- DeepSpeed / FSDP
- bitsandbytes (quantization)

**Models to Fine-tune:**
- Llama 2/3 (7B, 13B, 70B)
- Mistral 7B
- Phi-3
- Gemma
- Qwen

**Hardware:**
- Google Colab (free T4 GPU)
- Kaggle Notebooks (P100/T4)
- RunPod / Vast.ai (paid)
- Local GPU (8GB+ VRAM with QLoRA)

---

## 📊 Key Concepts Explained

### LoRA (Low-Rank Adaptation)

Instead of updating all 7 billion parameters, LoRA adds small trainable matrices to attention layers:

```
Original: W (large, frozen)
LoRA: W + B·A (small, trainable)

Where B·A is rank-r decomposition (r << d)
Only train B and A (~1% of parameters)
```

**Benefits:**
- 10-100x fewer parameters to train
- 3-10x faster training
- Multiple adapters for one base model
- Easy to merge or swap

### QLoRA (Quantized LoRA)

LoRA + 4-bit quantization = Fine-tune 70B models on consumer GPUs!

```
1. Quantize base model to 4-bit (NF4 format)
2. Add LoRA adapters (16-bit)
3. Train only adapters
4. Use paged optimizers for large models
```

**Enables:**
- 70B model on 24GB GPU
- 13B model on 8GB GPU
- 7B model on 4GB GPU

### RLHF vs DPO

**RLHF (Reinforcement Learning from Human Feedback):**
```
1. SFT: Supervised fine-tuning
2. RM: Train reward model from preferences
3. RL: Optimize policy with PPO
```

**DPO (Direct Preference Optimization):**
```
1. SFT: Supervised fine-tuning
2. DPO: Directly optimize from preferences
   (No separate reward model needed!)
```

DPO is simpler and often works just as well.

---

## 🎯 Projects

### 1. Custom Domain Chatbot

Fine-tune for medical, legal, or technical domain.

**Skills:** Instruction tuning, evaluation, deployment

### 2. Code Completion Model

Adapt model for your codebase and style.

**Skills:** Code datasets, fill-in-middle training

### 3. Sentiment Classifier

Classification with efficient fine-tuning.

**Skills:** Task-specific heads, evaluation metrics

### 4. Summarization Model

Custom summarization for your document types.

**Skills:** Seq2seq tuning, ROUGE metrics

---

## 📈 Evaluation Metrics

### Generation Quality

- **Perplexity:** Lower is better (language modeling)
- **BLEU/ROUGE:** Translation/summarization
- **Human eval:** Gold standard
- **GPT-4 as judge:** Scalable alternative

### Task Performance

- **Accuracy:** Classification tasks
- **F1 Score:** Balanced precision/recall
- **Exact Match:** QA tasks
- **Pass@k:** Code generation

### Efficiency

- **Training time:** Hours to convergence
- **Memory usage:** Peak VRAM
- **Inference latency:** Response time
- **Cost per sample:** Training + inference

---

## 💡 Best Practices

### DO ✅

- Start with small model (7B) before big (70B)
- Use QLoRA for consumer GPUs
- Prepare high-quality data (quality > quantity)
- Evaluate on held-out test set
- Monitor for catastrophic forgetting
- Version control your models and data
- Use Flash Attention for speed
- Quantize for inference

### DON'T ❌

- Fine-tune without trying prompting first
- Use dirty/unformatted data
- Overtrain (watch validation loss)
- Ignore eval metrics
- Train on evaluation data
- Skip data filtering
- Use default hyperparameters blindly
- Forget to save checkpoints

### Training Tips

```python
# Good hyperparameters for LoRA
config = {
    "r": 16,                      # Higher r = more capacity
    "lora_alpha": 32,             # Usually 2x rank
    "lora_dropout": 0.05,
    "learning_rate": 2e-4,        # Higher than full fine-tuning
    "batch_size": 4,              # With gradient accumulation
    "gradient_accumulation": 8,   # Effective batch = 32
    "warmup_steps": 100,
    "max_steps": 1000,            # Or epochs
    "save_steps": 100
}
```

---

## 🔗 Resources

### Courses

- [Hugging Face Fine-tuning Course](https://huggingface.co/learn/nlp-course/chapter3/1)
- [DeepLearning.AI - Fine-tuning LLMs](https://www.deeplearning.ai/short-courses/finetuning-large-language-models/)
- [Fast.ai - Practical Deep Learning](https://course.fast.ai/)

### Papers

- [LoRA: Low-Rank Adaptation](https://arxiv.org/abs/2106.09685)
- [QLoRA: Efficient Finetuning](https://arxiv.org/abs/2305.14314)
- [RLHF: Training language models](https://arxiv.org/abs/2203.02155)
- [DPO: Direct Preference Optimization](https://arxiv.org/abs/2305.18290)

### Tools & Frameworks

- [Hugging Face PEFT](https://github.com/huggingface/peft)
- [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl)
- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)
- [Unsloth](https://github.com/unslothai/unsloth) - 2x faster training

### Datasets

- [Alpaca Dataset](https://github.com/tatsu-lab/stanford_alpaca)
- [OpenAssistant Conversations](https://huggingface.co/datasets/OpenAssistant/oasst1)
- [Dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k)
- [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered)

---

## ✅ Completion Checklist

Before moving forward, you should be able to:

- [ ] Decide when fine-tuning is appropriate
- [ ] Prepare datasets in correct format
- [ ] Perform supervised fine-tuning
- [ ] Use LoRA for efficient training
- [ ] Apply QLoRA on consumer hardware
- [ ] Understand RLHF and DPO
- [ ] Evaluate fine-tuned models
- [ ] Quantize models for deployment
- [ ] Merge and swap LoRA adapters
- [ ] Deploy custom models in production

---

## 🎓 What's Next?

**Phase 13: Local LLMs** →
- Run your fine-tuned models locally
- Privacy and full control
- Optimize for inference

**Phase 8: MLOps** →
- CI/CD for model training
- Experiment tracking
- Production monitoring

**Phase 12: Multimodal AI** →
- Fine-tune vision-language models
- Image + text tasks
- Audio models

---

**Ready to customize your own LLM?** → Start with `00_START_HERE.ipynb`

**Questions?** → Check the projects/ folder for complete examples

**🚀 Remember: Fine-tuning is cheaper than you think with QLoRA!**
