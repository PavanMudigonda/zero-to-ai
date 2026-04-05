# Phase 12: LLM Fine-Tuning

This module is strongest when approached as decision-making, not just training mechanics. The real question is when fine-tuning is the right tool, how to prepare data well enough for it to matter, and how to evaluate whether the resulting model is actually better than prompting or RAG.

## Actual Module Contents

1. [00_START_HERE.ipynb](00_START_HERE.ipynb)
2. [01_dataset_preparation.ipynb](01_dataset_preparation.ipynb)
3. [02_supervised_finetuning.ipynb](02_supervised_finetuning.ipynb)
4. [03_lora_basics.ipynb](03_lora_basics.ipynb)
5. [04_qlora_efficient.ipynb](04_qlora_efficient.ipynb)
6. [05_dpo_alignment.ipynb](05_dpo_alignment.ipynb)
7. [06_evaluation.ipynb](06_evaluation.ipynb)
8. [07_deployment.ipynb](07_deployment.ipynb)
9. [08_grpo_reasoning_training.ipynb](08_grpo_reasoning_training.ipynb)
10. [09_unsloth_fast_finetuning.ipynb](09_unsloth_fast_finetuning.ipynb)
11. [10_quantization_gptq_awq.ipynb](10_quantization_gptq_awq.ipynb)
12. [11_rlhf_constitutional_ai.ipynb](11_rlhf_constitutional_ai.ipynb)

## Recommended Order

- First pass: `00 -> 01 -> 02 -> 03 -> 04 -> 06 -> 07`
- Second pass for alignment: `05 -> 08 -> 11`
- Deployment and efficiency depth: `09 -> 10`

## What To Learn Here

- When fine-tuning beats prompting
- Why dataset quality dominates training quality
- How LoRA and QLoRA reduce hardware needs
- Why evaluation must be task-specific
- The distinction between SFT, preference optimization, and RL-style alignment

## Study Advice

- Do not start with RLHF terminology if SFT data formatting is still fuzzy.
- Treat [06_evaluation.ipynb](06_evaluation.ipynb) as a required notebook, not an optional one.
- Compare every fine-tuning idea against a prompting baseline and a RAG baseline.

## Practical Outcomes

After this module, you should be able to:

- Prepare instruction-format data
- Run an adapter-based fine-tune
- Evaluate whether the tuned model improved on a concrete task
- Package or deploy the result without confusing training success for production readiness
