# Contributing to Zero to AI

Thank you for contributing to this repository. The goal of this project is to make AI/ML learning structured, practical, and maintainable for self-learners.

**Live site:** [https://zero-to-ai.dev](https://zero-to-ai.dev)

## What Contributions Help Most

- Fix broken links, stale APIs, and outdated instructions
- Improve explanations in notebooks and READMEs
- Add exercises, assignments, and challenge prompts
- Add or improve `00_START_HERE.ipynb` guidance in modules
- Contribute new notebooks only when they clearly fit the existing curriculum

## Before You Start

1. Read [README.md](README.md) for the repo overview
2. Read [MASTER_STUDY_GUIDE.md](MASTER_STUDY_GUIDE.md) to understand the intended learning flow
3. Check [checklist.md](checklist.md) if your change affects the curriculum path
4. Search existing issues and pull requests before starting overlapping work

## Repo Structure

This repo uses numbered folders for the learning path:

- `00-course-setup/`
- `01-python/`
- `02-data-science/`
- `03-maths/`
- `04-token/`
- `05-embeddings/`
- `06-neural-networks/`
- `07-vector-databases/`
- `08-rag/`
- `09-mlops/`
- `10-specializations/`
- `11-prompt-engineering/`
- `12-llm-finetuning/`
- `13-multimodal/`
- `14-local-llms/`
- `15-ai-agents/`
- `16-model-evaluation/`
- `17-debugging-troubleshooting/`
- `18-low-code-ai-tools/`
- `19-ai-safety-redteaming/`
- `20-real-time-streaming/`
- `21-quizzes/`
- `22-references/`
- `23-glossary/`
- `24-advanced-deep-learning/`
- `25-reinforcement-learning/`
- `26-time-series-analysis/`
- `27-causal-inference/`
- `28-practical-data-science/`
- `29-ai-hardware-llm-validation/`
- `30-inference-optimization/`

## Getting Started

### Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/zero-to-ai.git
cd zero-to-ai
```

### Set Up the Environment

Use the repo’s current setup docs:

- [00-course-setup/README.md](00-course-setup/README.md)
- [setup.md](setup.md)

Fast path:

```bash
./install_dependencies.sh
source .venv/bin/activate
```

### Create a Branch

```bash
git checkout -b docs/fix-rag-links
```

## Standards for Curriculum Changes

### Prefer curriculum consistency over novelty

A smaller, coherent learning path is better than a larger repo with overlapping or stale material.

### If you add a notebook

- Place it in the correct numbered module
- Add or update that module’s `README.md`
- Update [checklist.md](checklist.md) if it becomes part of the intended path
- Update [MASTER_STUDY_GUIDE.md](MASTER_STUDY_GUIDE.md) only if it changes the recommended flow

### If you update documentation

- Check local links
- Remove stale file references
- Avoid exact counts unless you have verified them
- Prefer “first pass / optional depth” guidance when a module is large

### If you update code in notebooks

- Make sure the notebook still runs top-to-bottom when practical
- Keep explanations beginner-readable
- Explain why a technique is used, not just what the code does

## Pull Request Checklist

Before opening a PR:

- Run the changed notebook or verify the changed doc paths
- Check for broken local links in edited markdown
- Confirm you did not introduce old folder names or stale file references
- Keep unrelated cleanup out of the PR unless it is obviously generated clutter

## Commit Style

Use clear, narrow commit messages:

```bash
git commit -m "docs: fix root setup instructions"
git commit -m "fix: update checklist paths for cs229 notebooks"
git commit -m "docs: refresh vector database module README"
```

## Reporting Bugs or Content Issues

When opening an issue, include:

- file path
- what is wrong
- expected behavior
- reproduction steps if code is involved

## License

By contributing, you agree that your contributions will be licensed under the MIT License in [LICENSE.md](LICENSE.md).
