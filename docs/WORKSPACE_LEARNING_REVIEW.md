# Workspace Learning Review

Audit of the repo as a learning system. Main risks at this scale: navigation drift, stale guidance, uneven scaffolding.

## Key Findings

1. Several phase READMEs described wrong file layouts or old phase numbering.
2. Root-level entry point pushed learners toward a weak or nonexistent orientation flow.
3. `23-glossary/` and `28-practical-data-science/` were missing usable landing pages.
4. `28-practical-data-science/00_START_HERE.ipynb` was empty.
5. Broken markdown links in top-level and phase-level guides.

## Folder Priority

| Priority | Folders |
|----------|---------|
| **High** | `00-course-setup`, `01-python`, `05-embeddings`, `06-neural-networks`, `11-prompt-engineering`, `12-llm-finetuning`, `14-local-llms`, `23-glossary`, `28-practical-data-science` |
| **Medium** | `02-data-science`, `03-maths`, `04-token`, `07-vector-databases`, `08-rag`, `09-mlops`, `10-specializations`, `20-real-time-streaming`, `21-quizzes`, `24-advanced-deep-learning`, `25-reinforcement-learning`, `26-time-series`, `27-causal-inference` |
| **Low** | `15-ai-agents`, `16-model-evaluation`, `17-debugging`, `18-low-code`, `19-ai-safety`, `22-references`, `scripts` |

## Fixes Applied

- Corrected repo entry-point guidance in main README and setup docs
- Fixed stale links in `01-python/README.md`
- Rewrote phase READMEs for embeddings, neural networks, prompt engineering, fine-tuning, and local LLMs to match actual notebooks
- Added landing pages for `23-glossary/` and `28-practical-data-science/`
- Added real start notebook for `28-practical-data-science/`

## Recommended Next Pass

1. Repair broken links in `checklist.md` to match current folder structure
2. Refresh `07-vector-databases/README.md`, `02-data-science/README.md`, `03-maths/README.md` with stronger curation
3. Add "first pass / second pass / optional" guidance to every advanced phase (24+)
