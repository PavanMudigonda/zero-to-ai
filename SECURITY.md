# Security Policy

Zero to AI is an educational repository made up of Jupyter notebooks, course
content, a documentation website (`next-docs/`), and Python maintenance tooling
(`scripts/`). It is not a deployed product, but we still take security seriously
for the build pipeline, dependencies, and the public documentation site at
[zero-to-ai.dev](https://zero-to-ai.dev/).

## Supported Versions

This project is rolling-release. Only the latest state of the `main` branch is
supported. Please make sure you are on the most recent commit before reporting an
issue.

## Reporting a Vulnerability

Please **do not** open a public GitHub issue for security vulnerabilities.

Instead, report privately using one of the following:

- Open a [GitHub Security Advisory](https://github.com/PavanMudigonda/zero-to-ai/security/advisories/new)
  (preferred), or
- Email the maintainer at **mnpawan@gmail.com** with the subject line
  `SECURITY: zero-to-ai`.

When reporting, please include:

- A description of the vulnerability and its potential impact.
- Steps to reproduce, or a proof of concept.
- The affected file(s), workflow(s), or dependency.

We aim to acknowledge new reports within a few days. Once a fix is available,
we will coordinate a disclosure timeline with you.

## Scope

In scope:

- The GitHub Actions workflows in `.github/workflows/`.
- The documentation site build and runtime in `next-docs/`.
- Python tooling in `scripts/`.
- Declared dependencies in `pyproject.toml`, `requirements*.txt`,
  `environment.yml`, and the `package.json` files.

Out of scope:

- Vulnerabilities in third-party services (Cloudflare, Supabase, Google
  Colab, Kaggle, Replit) — report those to the respective vendor.
- Issues that require a user to run untrusted notebook code they authored
  themselves.

## Dependency and Code Scanning

This repository uses:

- **Dependabot** (`.github/dependabot.yml`) for automated dependency updates
  across pip, npm, and GitHub Actions.
- **Snyk** scanning for first-party code, per the contribution guidelines.

When contributing, please run available security scans on new or modified code
and fix reported issues before opening a pull request.
