# Contributing to Zero to AI

Thank you for considering a contribution. This is an open-source AI/ML curriculum aimed at learners around the world, so contributions that improve **clarity, accessibility, and accuracy** are especially welcome.

You do not need to be an expert. Fixing a typo, clarifying a paragraph, or translating one notebook is a real contribution.

## Ways to Contribute

- **Fix a typo or broken link** — open a PR directly, no issue needed.
- **Report a bug** — open an [issue](https://github.com/PavanMudigonda/zero-to-ai/issues) using the bug report template.
- **Suggest a notebook or topic** — open an [issue](https://github.com/PavanMudigonda/zero-to-ai/issues) using the notebook suggestion template.
- **Improve an explanation** — open a PR with the change.
- **Add a translation** — see [Translations](#translations) below.
- **Add or improve a notebook** — please open an issue first for anything larger than a small edit, so we can align on scope.

## Repository Layout

The curriculum lives in two parallel trees, kept in sync:

- `jupyter-notebooks/<phase>/` — source of truth for runnable notebooks.
- `next-docs/src/app/<phase>/` — auto-generated MDX wrappers that render notebooks on [zero-to-ai.dev](https://zero-to-ai.dev/).

Always edit notebooks under `jupyter-notebooks/`, then run:

```bash
python3 scripts/sync_notebooks.py
python3 scripts/generate_meta_sequential.py
```

These regenerate the MDX wrappers and the Nextra sidebar.

## Setup

```bash
git clone https://github.com/<your-username>/zero-to-ai.git
cd zero-to-ai
./install_dependencies.sh
```

If you only need to edit text or docs, you can skip the install — Markdown and MDX changes don't need a Python environment.

## Making a Change

1. Create a branch: `git checkout -b fix/<short-description>`.
2. Make your change. For notebooks, **clear outputs before committing** unless the output is part of the lesson:
   ```bash
   jupyter nbconvert --clear-output --inplace <notebook>.ipynb
   ```
3. If you edited a notebook, run the sync scripts above.
4. Commit with a short, descriptive message:
   - `fix: clarify backprop step in 06-neural-networks/02_backprop`
   - `docs: add note about Kaggle phone verification in README`
   - `feat: new notebook on RAG evaluation in 08-rag`
5. Push and open a PR.

## What Makes a Good PR

- **One topic per PR.** A typo fix and a new notebook are two PRs.
- **No huge formatting reflows.** Touch only what you need to.
- **Beginner-friendly explanations.** Assume the reader is a global learner, sometimes reading in their second or third language. Avoid jargon when a plain word works.
- **Working code.** Cells should execute top-to-bottom without errors. If a cell needs an API key, mark it clearly and don't put your own key in.
- **No tracked outputs over 1 MB** unless the output is the lesson (e.g. a generated image).

## Translations

We welcome translations into any language. A few principles:

- Translate the **explanations and headings**, keep the **code** unchanged (variable names, library calls, etc.).
- Put translated notebooks alongside the original with a language suffix, e.g. `02_basic_prompting.es.ipynb` for Spanish.
- If you'd like to translate a whole phase, open an issue first so we can track the effort and avoid duplicates.

## Code of Conduct

By participating you agree to our [Code of Conduct](CODE_OF_CONDUCT.md). Be kind, be patient, and assume good faith.

## Questions?

Open a [discussion](https://github.com/PavanMudigonda/zero-to-ai/discussions) or an [issue](https://github.com/PavanMudigonda/zero-to-ai/issues). For larger ideas, drafting an issue before a PR saves everyone time.
