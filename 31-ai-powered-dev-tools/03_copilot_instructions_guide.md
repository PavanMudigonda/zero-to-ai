# GitHub Copilot Customization Guide

Seven configuration primitives control how Copilot behaves in your project. They persist across sessions, apply to every team member, and are committed to version control.

---

## Quick Reference

| # | Primitive | File | Location | Scope |
|---|-----------|------|----------|-------|
| 1 | [Workspace instructions](#1-workspace-instructions) | `copilot-instructions.md` | `.github/` | Every interaction in this repo |
| 2 | [AGENTS.md](#2-agentsmd) | `AGENTS.md` | Root or subfolders | Every interaction (monorepo-friendly) |
| 3 | [Scoped instructions](#3-scoped-instructions) | `*.instructions.md` | `.github/instructions/` | Files matching `applyTo` glob |
| 4 | [Prompt files](#4-prompt-files) | `*.prompt.md` | `.github/prompts/` | On-demand via prompt picker |
| 5 | [Custom agents](#5-custom-agents) | `*.agent.md` | `.github/agents/` | Agent picker or subagent delegation |
| 6 | [Skills](#6-skills) | `SKILL.md` + assets | `.github/skills/<name>/` | On-demand via `/` picker or auto-discovery |
| 7 | [Hooks](#7-hooks) | `*.json` | `.github/hooks/` | Deterministic lifecycle events |

**Rule:** Use `copilot-instructions.md` OR `AGENTS.md` for workspace instructions - not both.

---

## 1. Workspace Instructions

Create `.github/copilot-instructions.md` in your repo root. Automatically included in every Copilot interaction.

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

## Testing
- pytest for all tests
- Run with: pytest tests/ -v

## What NOT to Do
- Do not add API keys or secrets to any file
- Do not install packages globally; use .venv
- Do not use print() for debugging; use logging
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

## Build Commands
- Install: pip install -e ".[dev]"
- Test: pytest tests/ -v --timeout=30
- Lint: ruff check src/
- Format: ruff format src/
```

---

## 2. AGENTS.md

An alternative to `copilot-instructions.md` with **monorepo hierarchy support**. Place `AGENTS.md` at the repo root or in subfolders - the closest file in the directory tree wins.

```
/AGENTS.md                  # Root defaults
/frontend/AGENTS.md         # Frontend-specific (overrides root for frontend/)
/backend/AGENTS.md          # Backend-specific (overrides root for backend/)
```

### When to use AGENTS.md vs copilot-instructions.md

| Scenario | Use |
|----------|-----|
| Single-project repo | `copilot-instructions.md` |
| Monorepo with different stacks per folder | `AGENTS.md` (one per subfolder) |
| Want cross-editor compatibility | `AGENTS.md` (open standard) |

**Important:** Use one or the other - never both in the same repo.

### Example

```markdown
# Backend Guidelines

## Architecture
- FastAPI + SQLAlchemy 2.0
- Service layer pattern: never put business logic in route handlers

## Build and Test
- Install: pip install -e ".[dev]"
- Test: pytest tests/ -v
- Lint: ruff check src/

## Conventions
- Use async def everywhere
- Environment variables via pydantic-settings
```

---

## 3. Scoped Instructions

For rules that apply only to specific files or directories. Place `*.instructions.md` files in `.github/instructions/` with YAML frontmatter.

### Frontmatter

```yaml
---
description: "Use when writing database migrations"   # For on-demand discovery
applyTo: "**/*.py"                                     # Auto-attach for matching files
---
```

### Discovery Modes

| Mode | Trigger | Use case |
|------|---------|----------|
| **On-demand** (`description`) | Agent detects task relevance | Task-based rules: migrations, refactoring |
| **Explicit** (`applyTo`) | Files matching glob in context | File-based rules: language standards |
| **Manual** | `Add Context` → `Instructions` | Ad-hoc attachment |

### Example: Test Rules

```markdown
---
applyTo: "tests/**"
---
# Test Rules

- Use pytest.mark.asyncio for all async tests
- Use the `client` fixture (defined in conftest.py) for HTTP tests
- Assert specific error messages, not just status codes
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
```

### Glob Patterns

```yaml
applyTo: "**"                      # Always included (use with caution - burns context)
applyTo: "**/*.py"                 # All Python files
applyTo: ["src/**", "lib/**"]      # Multiple patterns (OR)
applyTo: "src/api/**/*.ts"         # Specific folder + extension
```

---

## 4. Prompt Files

Reusable workflow templates that appear in Copilot's prompt picker (`/`). Save in `.github/prompts/`.

### Frontmatter

```yaml
---
mode: agent                              # agent or ask
tools: ["terminal", "codebase"]          # tools the agent can use
description: "Add evaluation metrics"    # shown in the picker
---
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
```

The `${input:name}` syntax prompts the user for values when the prompt is selected.

### Example: Security Review

```markdown
---
mode: agent
tools: ["codebase"]
description: "Review code for security issues"
---
# Security Review

Review the current file for:
1. SQL injection vulnerabilities
2. Hardcoded secrets or credentials
3. Missing input validation
4. Insecure deserialization
5. Path traversal risks

For each issue found, explain the risk and provide a fix.
```

---

## 5. Custom Agents

Custom personas with specific tools, instructions, and behaviors. Create `*.agent.md` files in `.github/agents/`.

### Frontmatter

```yaml
---
description: "Use when running database migrations"  # Required: for discovery
tools: [read, search, execute]                        # Tool aliases
model: "Claude Sonnet 4"                              # Optional: override default
user-invocable: true                                  # Show in agent picker
---
```

### Tool Aliases

| Alias | Purpose |
|-------|---------|
| `execute` | Run shell commands |
| `read` | Read file contents |
| `edit` | Edit files |
| `search` | Search files or text |
| `agent` | Invoke other agents as subagents |
| `web` | Fetch URLs and web search |
| `todo` | Manage task lists |

### Example: Read-Only Researcher

```markdown
---
description: "Research codebase questions without making changes"
tools: [read, search]
---
You are a read-only research agent. Your job is to answer questions about the codebase.

## Constraints
- DO NOT edit any files
- DO NOT run terminal commands
- ONLY read and search

## Output Format
Provide a concise answer with file paths and line numbers as evidence.
```

### Example: Test Writer

```markdown
---
description: "Generate tests for Python modules following project conventions"
tools: [read, search, edit, execute]
---
You are a test specialist. Generate comprehensive pytest tests.

## Approach
1. Read the target module to understand its API
2. Read existing tests in tests/ for conventions
3. Write tests covering: happy path, edge cases, error cases
4. Run pytest to verify all tests pass

## Constraints
- Follow patterns in conftest.py
- Use factory_boy for test data
- Never mock the function under test
```

### Subagent Pattern

A parent agent can delegate to specialized subagents:

```yaml
---
description: "Coordinate feature implementation"
tools: [read, search, edit, execute, agent]
agents: [researcher, test-writer]
---
```

Set `user-invocable: false` on helper agents you only want accessible as subagents.

---

## 6. Skills

On-demand workflow packages with bundled scripts, templates, and reference docs. The agent loads them when relevant based on the `description`.

### Directory Structure

```
.github/skills/webapp-testing/
├── SKILL.md              # Required - must match folder name
├── scripts/
│   └── run-tests.sh
├── references/
│   └── test-patterns.md
└── assets/
    └── config-template.json
```

### SKILL.md Format

```yaml
---
name: webapp-testing
description: "Test web applications using Playwright. Use for verifying frontend, debugging UI, capturing screenshots."
argument-hint: "Describe what to test"
---
```

### Body

```markdown
# Web Application Testing

## When to Use
- Verify frontend functionality after changes
- Debug UI behavior with screenshots
- Run end-to-end tests

## Procedure
1. Start the dev server: `npm run dev`
2. Run [test script](./scripts/run-tests.sh)
3. Review screenshots in `./screenshots/`
4. Report failures with specific selectors
```

### How Skills Differ from Prompts

| Feature | Prompt (`.prompt.md`) | Skill (`SKILL.md`) |
|---------|----------------------|---------------------|
| Bundled assets | No | Yes (scripts, templates, references) |
| Auto-discovery | No (manual `/` picker) | Yes (agent reads `description`) |
| Progressive loading | No (full content sent) | Yes (description → body → assets) |
| Best for | Single focused task | Multi-step workflow with assets |

Both appear when you type `/` in chat.

---

## 7. Hooks

Deterministic lifecycle automation. Unlike instructions (which guide behavior), hooks **enforce** behavior via shell commands at specific events.

### Location

```
.github/hooks/*.json      # Workspace (team-shared)
```

### Hook Events

| Event | When it fires |
|-------|--------------|
| `SessionStart` | First prompt of a new agent session |
| `PreToolUse` | Before a tool is invoked |
| `PostToolUse` | After a tool succeeds |
| `UserPromptSubmit` | User submits a prompt |
| `Stop` | Agent session ends |

### Example: Auto-format After Edits

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "type": "command",
        "command": "ruff format --quiet .",
        "timeout": 10
      }
    ]
  }
}
```

### Example: Block Dangerous Commands

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/validate-tool.sh",
        "timeout": 15
      }
    ]
  }
}
```

The script receives JSON on stdin describing the tool call. It can return:
- `"permissionDecision": "allow"` - proceed
- `"permissionDecision": "ask"` - ask user for confirmation
- `"permissionDecision": "deny"` - block the action

### When to Use Hooks vs Instructions

| Need | Use |
|------|-----|
| Guide coding style | Instructions |
| Auto-run formatter after every edit | Hook (`PostToolUse`) |
| Prevent `rm -rf` or `DROP TABLE` | Hook (`PreToolUse`) |
| Inject runtime context | Hook (`SessionStart`) |

---

## 8. Decision Flowchart

```
Is this a project-wide coding standard?
├── Yes → copilot-instructions.md or AGENTS.md
│         (monorepo with subfolder differences? → AGENTS.md)
└── No
    ├── Does it apply only to specific files?
    │   └── Yes → .instructions.md with applyTo
    ├── Is it a reusable one-shot task?
    │   └── Yes → .prompt.md
    ├── Is it a multi-step workflow with scripts/templates?
    │   └── Yes → SKILL.md
    ├── Is it a specialized persona with tool restrictions?
    │   └── Yes → .agent.md
    └── Must it be enforced deterministically (not just guided)?
        └── Yes → Hook (.json)
```

---

## 9. Best Practices

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

Negative instructions prevent common AI mistakes:
```
## Do NOT
- Do not use os.getenv() - use pydantic-settings
- Do not hardcode secrets - use environment variables
- Do not add print() for debugging - use logging
```

### Write Keyword-Rich Descriptions

The `description` field is how Copilot discovers skills, agents, and on-demand instructions. If trigger words aren't in the description, the agent won't find it.

Bad: `"A helpful skill for testing"`

Good: `"Test web applications using Playwright. Use for verifying frontend, debugging UI, capturing screenshots."`

### Commit Everything to Version Control

All customization files should be committed to git - instructions, prompts, agents, skills, and hooks. This ensures every team member gets the same Copilot behavior.

---

## 10. Troubleshooting

| Problem | Fix |
|---------|-----|
| Copilot ignores instructions | Verify file is at `.github/copilot-instructions.md` (exact path) |
| Using both AGENTS.md and copilot-instructions.md | Pick one - having both causes conflicts |
| Scoped instructions not applying | Check `applyTo` glob matches the file you're editing |
| Prompt files not appearing | Ensure they're in `.github/prompts/` with `.prompt.md` extension |
| Agent not appearing in picker | Check `user-invocable` isn't `false` and `description` is present |
| Skill not auto-loading | Verify `name` in frontmatter matches folder name exactly |
| Hooks not firing | Check JSON syntax, `type: "command"`, and file is in `.github/hooks/` |
| `applyTo: "**"` slowing things down | Too broad - loads on every interaction. Use specific globs |
| Too much instruction text | Keep under ~2000 words total; Copilot has context limits |

---

*Next: [04_copilot_workflows.md](04_copilot_workflows.md) - real VS Code + Copilot workflows*
