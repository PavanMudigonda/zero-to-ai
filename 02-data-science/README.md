# Phase 1: Data Science Foundations

This folder is the practical base layer for the rest of the repo. If you are not yet comfortable with arrays, DataFrames, plots, train/test splits, and the `fit/predict/transform` workflow, later LLM and deep learning phases will feel harder than they need to.

## What This Phase Covers

- NumPy for numerical thinking
- pandas for messy real-world data
- matplotlib for basic visualization
- scikit-learn for classical ML workflows
- broader data science examples for exploratory and applied practice

## Folder Map

- `1-numpy-examples/`: array operations, broadcasting, indexing, exercises
- `2-pandas-examples/`: cleaning, joins, grouping, time-series handling, projects
- `3-data-science-examples/`: broader learning material and reference notebooks
- `4-matplotlib/`: plotting fundamentals
- `5-scikit-learn/`: a very large example library across major model families

## Recommended First Pass

1. Work through `1-numpy-examples/`
2. Move to `2-pandas-examples/`
3. Use `4-matplotlib/` for core plotting habits
4. In `5-scikit-learn/`, focus first on:
   - `linear_model/`
   - `model_selection/`
   - `preprocessing/`
   - `ensemble/`
   - `cluster/`
5. Use `3-data-science-examples/` as breadth and reinforcement, not as a strict sequential course

## Study Advice

- Do not try to complete every scikit-learn notebook on the first pass.
- Prefer one full workflow over broad shallow browsing:
  data loading -> cleaning -> feature work -> split -> train -> evaluate -> explain results.
- Keep notes on leakage, validation mistakes, and metric choice. Those habits matter more than memorizing APIs.

## Suggested Projects

- Iris or wine classification with proper validation
- Housing-price regression with feature engineering
- Customer segmentation with clustering and a short business write-up

## What Comes Next

After this phase, move to:

1. [03-maths/README.md](../03-maths/README.md)
2. [04-token/](../04-token/)
3. [05-embeddings/](../05-embeddings/)
