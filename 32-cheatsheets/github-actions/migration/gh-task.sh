#!/bin/bash

export $OWNER=PavanMudigondaTR
export $REPO=

gh agent-task create --base main --follow --repo $OWNER/$REPO "$(cat <<'PROMPT'  
You are a senior DevOps engineer. Goal: finish migrating our CI/CD to GitHub Actions to reach 100% functional parity, using best practices and maximizing reusability/maintainability.

Context:  
- We already ran GitHub Actions Importer. About ~60% is converted.  
- The remaining ~40% includes missing jobs/steps, platform-specific features that didn't convert cleanly, and refactors needed for reusable patterns.

Hard requirements:  
1) Preserve behavior: match original pipeline semantics (triggers, conditions, approvals, artifacts, test reports, deployments, notifications).  
2) Reusability: avoid duplicating logic across workflows. Prefer:  
   - reusable workflows via `workflow_call` for shared pipelines (build/test/release/deploy)  
   - composite actions for repeated step sequences (setup, auth, build, publish)  
3) Security best practices:  
   - least-privilege `permissions:` per workflow/job  
   - use OIDC for cloud auth where possible (avoid long-lived secrets)  
   - never print secrets; redact tokens; don't add plaintext secrets to repo  
   - pin third-party actions to a full commit SHA when practical  
4) Reliability & speed:  
   - caching (setup language deps, build caches) where safe  
   - concurrency controls to prevent overlapping deploys  
   - robust retries/timeouts where appropriate  
   - use artifacts consistently (upload/download) for multi-job flows  
5) Documentation: update/author concise docs so the team can operate the new workflows.

Deliverables (in ONE draft PR):  
A) Complete/fix all workflows under `.github/workflows/` so they cover all pipelines (100% migration).  
B) Introduce a reusable structure, for example:  
   - `.github/workflows/_reusable-*.yml` (workflow_call) for shared pipelines  
   - `.github/actions/<name>/action.yml` composite actions for repeated step sets  
C) Add/update documentation:  
   - `docs/ci-cd.md` (or README section) explaining workflows, how to run manually, required secrets/vars, environments, and release/deploy process.  
D) Add guardrails:  
   - environment protection rules usage (where relevant)  
   - required checks names stable and meaningful  
   - clear job names and step names

Step-by-step tasks:  
1) Inventory:  
   - Enumerate existing workflows in `.github/workflows/` and identify what's incomplete/duplicated/incorrect.  
   - Find references to the old CI system (configs/scripts) and map them to GitHub Actions equivalents.  
2) Parity fixes:  
   - Implement missing triggers: push/pull_request/schedule/workflow_dispatch/release/tags as needed.  
   - Implement conditional execution (branch filters, path filters, labels, etc.).  
   - Ensure artifacts/test reports are produced the same way (e.g., junit, coverage, build outputs).  
   - Ensure deployments match environments (dev/stage/prod) and include approvals if needed.  
3) Reusability refactor:  
   - Extract common build/test logic into reusable workflows (`workflow_call`) and/or composite actions.  
   - Standardize setup steps (checkout, toolchain setup, dependency install, cache) into reusable components.  
4) Secrets/vars:  
   - Replace any hardcoded tokens/URLs with `secrets.*` or `vars.*`.  
   - Create a clear list of required secrets/variables in docs (names only; no values).  
5) Quality:  
   - Add `shell: bash`/`pwsh` explicitly where necessary for portability.  
   - Use `set -euo pipefail` where appropriate.  
   - Add `timeout-minutes` for long-running jobs.  
6) Validation:  
   - Ensure workflows are syntactically valid and logically consistent.  
   - If you add new composite actions/reusable workflows, update callers accordingly.  
   - Add minimal smoke workflows or a "CI self-check" job if useful (lint YAML, validate actions).

Constraints:  
- Do not introduce paid third-party SaaS dependencies.  
- Prefer GitHub-native features and official actions.  
- Keep changes focused on migration + necessary refactors.  
- If anything is ambiguous, choose the most conservative behavior that preserves original intent and document assumptions in the PR description.

Output format:  
- Make code changes directly.  
- Open a draft PR with a detailed description including:  
  - What pipelines are now covered  
  - Reusable components added and how to use them  
  - Secrets/vars required  
  - Any behavior changes/assumptions  
  - Follow-up recommendations (optional)

Now proceed with the implementation.  
PROMPT  
)"  