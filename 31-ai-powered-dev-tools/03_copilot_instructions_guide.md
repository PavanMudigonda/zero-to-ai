# GitHub Copilot Custom Instructions Guide

Custom instructions tell Copilot how to behave in your project. They persist across sessions, apply to every team member, and are committed to version control.

---

## 1. Why Instructions Matter

Without instructions, Copilot:
- Doesn't know your project conventions
- Generates code in a generic style
- Misses project-specific constraints (e.g., "always use Hydra for config")
- Repeats mistakes you've already corrected

With good instructions, Copilot:
- Follows your team's coding standards automatically
- Knows which frameworks and patterns to use
- Avoids anti-patterns specific to your project
- Produces code that passes your linter and tests on the first try

---

## 2. The Three Instruction Types

| Type | File | Scope | When to use |
|------|------|-------|-------------|
| **Repository instructions** | `.github/copilot-instructions.md` | Every Copilot interaction in this repo | Project-wide conventions |
| **Scoped instructions** | Any `.instructions.md` with `applyTo` frontmatter | Only files matching the glob | Directory-specific rules |
| **Prompt files** | `.github/prompts/*.prompt.md` | On-demand via prompt picker | Reusable agent workflows |

---

## 3. Repository Instructions

Create `.github/copilot-instructions.md` in your repo root. This is automatically included in every Copilot interaction.

### Example: Python ML Project

```markdown
# Project: Zero to AI Curriculum

## Stack
- Python 3.12+, scikit-learn, pandas, PyTorch
- Jupyter notebooks for tutorials, pytest for tests
- Sphinx for documentation

## Code Style
- Type hints on all function signatures
- f-strings over .format() or %
- pathlib.Path instead of os.path
- Google-style docstrings (Args, Returns, Raises)

## Project Structure
- Each phase is a numbered directory (00-course-setup/, 01-python/, etc.)
- Notebooks are ordered: 00_START_HERE.ipynb, 01_*, 02_*, ...
- Each directory has a README.md as the chapter entrypoint

## Notebook Rules
- Self-contained: no API keys required, use toy data and TF-IDF
- Every notebook must include a benchmark or comparison table
- All code cells must execute without errors

## Testing
- pytest for all tests
- Run with: pytest tests/ -v

## What NOT to Do
- Do not add API keys or secrets to any file
- Do not install packages globally; use .venv
- Do not use print() for debugging; use logging
- Do not modify notebooks with saved outputs without re-running them
```

### Example: FastAPI Backend

```markdown
# Project: E-Commerce API

## Stack
- Python 3.12, FastAPI, SQLAlchemy 2.0, Alembic, PostgreSQL 16
- pytest + httpx for testing, pydantic-settings for config

## Conventions
- All endpoints return Pydantic v2 models
- Use async def everywhere, not sync def
- Dependency injection for database sessions (src/api/deps.py)
- Environment variables via pydantic-settings, never os.getenv()

## File Organization
- src/api/routes/ — one file per resource
- src/models/ — SQLAlchemy models
- src/schemas/ — Pydantic request/response schemas
- src/services/ — business logic (never in route handlers)

## Testing
- Every endpoint needs: happy path, 401, and 422 tests
- Use factory_boy for test data
- Mock external APIs with respx

## Build Commands
- Install: pip install -e ".[dev]"
- Test: pytest tests/ -v --timeout=30
- Lint: ruff check src/
- Format: ruff format src/
```

---

## 4. Scoped Instructions (`.instructions.md`)

For rules that only apply to certain files or directories. Place `.instructions.md` files anywhere in your repo with `applyTo` YAML frontmatter.

### Example: Test-Specific Rules

```markdown
---
applyTo: "tests/**"
---
# Test Rules

- Use pytest.mark.asyncio for all async tests
- Use the `client` fixture (defined in conftest.py) for HTTP tests
- Assert specific error messages, not just status codes
- Clean up test data in fixtures, not in test functions
```

### Example: RAG Notebook Rules

```markdown
---
applyTo: "08-rag/**"
---
# RAG Notebook Rules

- All RAG notebooks must be self-contained (no API keys)
- Use TF-IDF or sklearn for retrieval in toy examples
- Every notebook must include a benchmark comparison table
- Link to 08_rag_technique_selection.md for technique context
```

### Example: API Route Rules

```markdown
---
applyTo: "src/api/routes/**"
---
# API Route Rules

- Every route function must have a docstring
- Use status_code parameter on the decorator
- Always include response_model on the decorator
- Rate limit all public endpoints with slowapi
```

### How Scoping Works

- `applyTo` uses glob patterns (same as `.gitignore` syntax)
- Multiple `.instructions.md` files can coexist — all matching ones apply
- More specific scopes override general ones when they conflict
- Files are found in any directory, not just `.github/`

---

## 5. Prompt Files (`.prompt.md`)

Reusable agent workflow templates that appear in Copilot's prompt picker. Save them in `.github/prompts/`.

### Example: Add Evaluation Metrics

```markdown
---
mode: agent
tools: ["terminal", "codebase"]
description: "Add evaluation metrics to a notebook"
---
# Add Evaluation Metrics

Add precision@k, recall@k, MRR, and NDCG metrics to the selected notebook.
Create a benchmark set with at least 3 test queries across categories.
Compare at least 2 retrieval variants in a summary table.
Run all cells to verify they execute without errors.
```

### Example: New API Endpoint

```markdown
---
mode: agent
tools: ["terminal", "codebase"]
description: "Scaffold a new API endpoint with tests"
---
# New API Endpoint

Create a new endpoint for the ${input:resource} resource:

1. Create the route in src/api/routes/${input:resource}.py
2. Create request/response schemas in src/schemas/${input:resource}.py
3. Create the SQLAlchemy model if needed
4. Write tests in tests/api/test_${input:resource}.py
5. Run tests: pytest tests/api/test_${input:resource}.py -v

Follow all conventions in .github/copilot-instructions.md.
```

### Example: Security Review

```markdown
---
mode: agent
tools: ["codebase"]
description: "Review code for security issues"
---
# Security Review

Review the current file or selection for:
1. SQL injection vulnerabilities
2. Hardcoded secrets or credentials
3. Missing input validation
4. Insecure deserialization
5. Path traversal risks

For each issue found, explain the risk and provide a fix.
```

### How to Use Prompt Files

1. Save `.prompt.md` files in `.github/prompts/`
2. Open Copilot Chat
3. Click the prompt picker (or type `/`) to see available prompts
4. Select a prompt — it pre-fills the chat with the template
5. The `${input:name}` syntax prompts you for values

---

## 6. Model Selection

Copilot supports multiple models. Switch per conversation using the model picker dropdown.

| Model | Best for | Speed | Cost tier |
|-------|----------|-------|-----------|
| **GPT-4o** | General coding, fast iteration | Fast | Standard |
| **Claude Sonnet 4** | Complex reasoning, long contexts | Medium | Premium |
| **o3** | Algorithmic problems, math, hard bugs | Slow | Premium |
| **Gemini 2.0 Flash** | Quick questions, simple edits | Fastest | Standard |

### Model Routing Strategy

| Task | Recommended model |
|------|-------------------|
| Fast edits, boilerplate, docstrings | GPT-4o or Gemini Flash |
| Multi-file feature implementation | Claude Sonnet 4 |
| Hard debugging, algorithm design | o3 |
| Code review and explanation | GPT-4o |
| Large refactor | Claude Sonnet 4 |

**Rule of thumb:** Start with GPT-4o. Escalate to Claude Sonnet 4 or o3 only when the output quality isn't sufficient.

---

## 7. Copilot Chat Participants and Slash Commands

### Participants

| Participant | What it does |
|-------------|-------------|
| `@workspace` | Searches your entire codebase for context |
| `@terminal` | References terminal output |
| `@vscode` | Asks about VS Code settings and commands |

### Slash Commands

| Command | Effect |
|---------|--------|
| `/explain` | Explain the selected code |
| `/fix` | Fix problems in the selected code |
| `/tests` | Generate tests for the selection |
| `/doc` | Generate documentation |
| `/new` | Scaffold a new file or project |

---

## 8. Best Practices

### Keep Instructions Short and Specific

Bad: `Write clean, well-documented code following best practices.`

Good:
```
- Type hints on all function signatures
- Google-style docstrings (Args, Returns, Raises)
- Max line length: 100 characters
- Use ruff for linting and formatting
```

### Include Build/Test Commands

The agent can only run tests if you tell it how:
```
## Build & Test
- Install: pip install -e ".[dev]"
- Test: pytest tests/ -v
- Lint: ruff check src/
```

### List What NOT to Do

Negative instructions are effective at preventing common AI mistakes:
```
## Do NOT
- Do not use os.getenv() — use pydantic-settings
- Do not hardcode secrets — use environment variables
- Do not add print() for debugging — use logging
- Do not modify alembic/env.py without discussing first
```

### Commit Instructions to Version Control

All instruction files should be committed to git. This ensures every team member and CI job gets the same Copilot behavior.

---

## 9. Troubleshooting

| Problem | Fix |
|---------|-----|
| Copilot ignores instructions | Verify file is at `.github/copilot-instructions.md` (exact path), UTF-8 encoding |
| Scoped instructions not applying | Check `applyTo` glob matches the file you're editing |
| Prompt files not appearing | Ensure they're in `.github/prompts/` and have `.prompt.md` extension |
| Instructions conflict | More specific scopes win; check for overlapping `.instructions.md` files |
| Too much instruction text | Keep under ~2000 words total; Copilot has context limits |

---

*Next: [04_copilot_workflows.md](04_copilot_workflows.md) — real VS Code + Copilot workflows*
