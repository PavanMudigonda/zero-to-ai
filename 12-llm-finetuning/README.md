# LLM Fine-Tuning

This module is strongest when approached as decision-making, not just training mechanics. The real question is when fine-tuning is the right tool, how to prepare data well enough for it to matter, and how to evaluate whether the resulting model is actually better than prompting or RAG.

This phase should be treated as a selective tool, not a default answer. Most learners get more value when they first understand prompting, retrieval, evaluation, and deployment tradeoffs before deciding to tune a model.

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

## How To Use This Phase Well

- Start with SFT, LoRA, and evaluation before moving into alignment-heavy notebooks.
- Keep a baseline model and task benchmark so you can measure whether tuning actually helped.
- Focus on data quality and task framing before spending time on training tricks.
- Pair deployment and monitoring work here with [../09-mlops/README.md](../09-mlops/README.md) once you have a model worth serving.

## Practical Outcomes

After this module, you should be able to:

- Prepare instruction-format data
- Run an adapter-based fine-tune
- Evaluate whether the tuned model improved on a concrete task
- Package or deploy the result without confusing training success for production readiness
- Use coding agents (OpenHands, OpenCode, Aider) to accelerate script writing, debugging, and evaluation

## Agent-Assisted Fine-tuning

Notebook `00_START_HERE.ipynb` (Section 10) covers how coding agents like **OpenHands**, **OpenCode**, and **mini-swe-agent** can automate the engineering side of the fine-tuning pipeline — scaffolding training scripts, debugging OOM errors, generating hyperparameter sweep configs, and writing evaluation harnesses.

Dataset curation and alignment decisions remain human work. The agents accelerate everything around those decisions.

**Cross-references:**
- **Phase 15** — [09_autonomous_agents_2026.ipynb](../15-ai-agents/09_autonomous_agents_2026.ipynb) for full coverage of OpenHands, OpenCode, Lingxi, and mini-swe-agent
- **Phase 31** — [00_ai_dev_tools_2026.md](../31-ai-powered-dev-tools/00_ai_dev_tools_2026.md) for installation, comparison, and ML-specific workflows

## What Comes Next

- Continue to [../16-model-evaluation/README.md](../16-model-evaluation/README.md) if you want stronger task-specific measurement and regression tracking.
- Continue to [../14-local-llms/README.md](../14-local-llms/README.md) or [../30-inference-optimization/README.md](../30-inference-optimization/README.md) if your focus shifts toward serving tuned models efficiently.
- Continue to [../09-mlops/README.md](../09-mlops/README.md) if you want to package, deploy, and monitor fine-tuned systems in production.
