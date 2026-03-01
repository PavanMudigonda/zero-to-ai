# AI Coding Tools for ML Engineers (2026)

A practical guide to the tools that are reshaping how ML engineers write, debug, and ship code. This covers the four major AI coding assistants, a head-to-head comparison, ML-specific workflows, and AI-assisted research tools.

---

## Table of Contents

1. [Cursor AI](#1-cursor-ai)
2. [Windsurf (by Codeium, acquired by OpenAI)](#2-windsurf-by-codeium-acquired-by-openai)
3. [Aider — Terminal-Native AI Pair Programmer](#3-aider--terminal-native-ai-pair-programmer)
4. [GitHub Copilot 2025](#4-github-copilot-2025)
5. [Comparison Table](#5-comparison-table)
6. [For ML Engineers Specifically](#6-for-ml-engineers-specifically)
7. [AI-Assisted Research Tools](#7-ai-assisted-research-tools)

---

## 1. Cursor AI

**What it is**: A fork of VS Code built around AI as a first-class feature, not a plugin. Cursor replaces the entire editor experience — everything from autocomplete to multi-file editing is AI-native.

**Valuation**: $9B (Series B, 2025). One of the fastest-growing developer tools companies ever.

**Website**: [cursor.com](https://cursor.com)

### Key Features

#### Composer (Multi-File Editing)
Cursor's flagship feature. Describe a change in natural language and Composer edits multiple files simultaneously with a diff view you can accept, reject, or edit. This is the key differentiator from GitHub Copilot's single-file approach.

```
Example Composer prompts:
- "Add input validation to all API endpoints in src/routes/"
- "Refactor the DataLoader class to support async loading"
- "Add type hints to all functions in training/trainer.py"
```

#### Tab Autocomplete
Context-aware autocomplete that understands your entire codebase, not just the current file. Learns your patterns and coding style. Significantly more accurate than GitHub Copilot for large codebases because of the full codebase indexing.

#### Bug Finder
Run `Ctrl+Shift+P → Find bugs` to get a structured analysis of potential issues in the current file or selection. Identifies logical errors, edge cases, and security vulnerabilities.

#### Codebase Context (@ symbols)
Reference specific parts of your codebase in any prompt:
- `@codebase` — entire indexed codebase
- `@filename.py` — specific file
- `@folder/` — entire directory
- `@web` — search the web
- `@docs` — reference indexed documentation

### Setup for ML/AI Projects

**1. Create a `.cursorignore` file** to exclude large binary files and unnecessary directories from indexing:

```gitignore
# .cursorignore
data/
datasets/
*.pkl
*.h5
*.hdf5
*.ckpt
*.safetensors
wandb/
mlruns/
__pycache__/
.venv/
node_modules/
*.egg-info/
dist/
build/
```

**2. Create `.cursor/rules` for project-specific AI behavior:**

```markdown
# .cursor/rules

## Project Context
This is a PyTorch ML training codebase using Hydra for configuration and WandB for experiment tracking.

## Code Style
- Use type hints for all function signatures
- Docstrings in Google format
- Follow PEP8 with 100-character line limit

## ML-Specific Rules
- Always use torch.no_grad() in evaluation loops
- Use DataLoader with num_workers=4 unless specified
- Log metrics with wandb.log(), not print()
- Configuration changes go in conf/config.yaml, not hardcoded

## Testing
- Write pytest tests for all utility functions
- Use pytest fixtures for expensive setup (model loading)
- Mock external APIs and file I/O in tests
```

**3. Index your documentation** for framework-specific help:
- Go to Settings → Features → Docs
- Add: PyTorch docs, HuggingFace docs, your internal confluence/notion

**4. Useful keyboard shortcuts for ML work**:
- `Ctrl+K` — inline edit (great for modifying a training loop in place)
- `Ctrl+L` — chat with codebase context
- `Ctrl+Shift+I` — Composer for multi-file changes
- `Ctrl+Shift+L` — add current selection to chat

### Pricing

| Plan | Price | Key Limits |
|---|---|---|
| Free (Hobby) | $0 | 2,000 completions/month, 50 slow premium requests |
| Pro | $20/month | Unlimited completions, 500 fast premium requests |
| Business | $40/user/month | SSO, privacy mode, audit logs |

**Best for**: Individual developers and small teams doing complex multi-file Python/ML work. The codebase indexing and Composer feature make it significantly faster for large-scale refactors.

---

## 2. Windsurf (by Codeium, acquired by OpenAI)

**What it is**: An AI IDE (VS Code-based) built by Codeium. OpenAI acquired Codeium in early 2026, making Windsurf the first IDE directly owned by a frontier lab. Known for its **Cascade** autonomous agent and exceptional context-building speed.

**Website**: [codeium.com/windsurf](https://codeium.com/windsurf)

### Key Features

#### Cascade Agent
Windsurf's core differentiator. Cascade is a fully autonomous coding agent that can complete multi-step tasks without asking for approval at each step. Unlike Cursor's Composer (which shows diffs and waits), Cascade:

1. Reads the relevant files
2. Plans the changes
3. Executes all edits
4. Runs tests to verify
5. Fixes any introduced errors
6. Reports when done

This is closer to the OpenHands/Devin model but embedded directly in your IDE.

#### Fast Context (8 Parallel Tool Calls)
Windsurf's context-building engine runs up to 8 tool calls in parallel, making it ~10x faster than sequential context gathering. When you ask about a bug, Windsurf reads all relevant files simultaneously rather than one at a time.

#### Arena Mode (February 2026)
Windsurf's Arena Mode presents completions from two different models side-by-side (anonymized) and asks you to choose the better one. Your preferences fine-tune the models over time, creating a personalized coding assistant that improves with use.

#### Supercomplete
Predictive multi-line completions that predict entire code blocks, not just the next line. Trained specifically on Codeium's 70B+ parameter model.

### Cascade: Autonomous Workflow Example

```
You: "Our API endpoints don't have rate limiting. Add rate limiting to all
     endpoints in src/api/ using slowapi. Use Redis as the backend.
     Add tests."

Cascade:
1. Reads all files in src/api/
2. Identifies all FastAPI route handlers
3. Installs slowapi (updates requirements.txt)
4. Adds rate limit decorators to each endpoint
5. Creates Redis configuration in config/
6. Writes tests in tests/test_rate_limiting.py
7. Runs pytest — finds one failure
8. Fixes the failure
9. Reports: "Added rate limiting to 12 endpoints. All 47 tests passing."
```

### Pricing

| Plan | Price | Notes |
|---|---|---|
| Free | $0 | 5 Cascade requests/day, basic autocomplete |
| Pro | $15/month | 75 Cascade requests/day, all models |
| Teams | $35/user/month | Enterprise features, admin dashboard |

**Best for**: Teams who want truly autonomous multi-step coding workflows. If you want to say "implement this feature" and come back when it's done, Windsurf Cascade is the best current option. Also excellent for enterprise teams due to its OpenAI backing and enterprise security posture.

---

## 3. Aider — Terminal-Native AI Pair Programmer

**What it is**: A command-line AI coding assistant that works directly with your git repository. It is the tool of choice for developers who live in the terminal, work on remote servers via SSH, or need to integrate AI coding into CI/CD pipelines.

**GitHub**: [github.com/Aider-AI/aider](https://github.com/Aider-AI/aider) (~20K stars)

### Why Aider Is Different

Aider is **git-native**: every change it makes is immediately committed with a descriptive commit message. This gives you a complete history of every AI-generated change, making it trivial to revert, audit, or cherry-pick.

It also supports the widest model range of any tool:
- Anthropic Claude (Opus 4, Sonnet 4, Haiku)
- OpenAI (o3, o4-mini, GPT-4o)
- Google Gemini (2.0 Flash, 2.5 Pro)
- DeepSeek (R1, V3)
- Any OpenAI-compatible local model (Ollama, LM Studio)

### Installation and Basic Usage

```bash
# Install
pip install aider-chat

# Start with Claude Opus 4 (recommended for complex tasks)
aider --model claude-opus-4-6

# Start with a specific file
aider src/training/trainer.py --model claude-opus-4-6

# Use with OpenAI
aider --model gpt-4o

# Use with a local model via Ollama
aider --model ollama/llama3.3
```

### Key Aider Commands

```bash
# In the aider REPL:
> /add src/model.py tests/test_model.py    # Add files to context
> /drop src/old_file.py                    # Remove from context
> /git log --oneline -10                   # Check recent commits
> /undo                                    # Undo last AI commit
> /diff                                    # Show uncommitted changes
> /run pytest tests/                       # Run a command and add output to context
> /ask What does the forward() method do?  # Ask without making changes
```

### Non-Interactive / Scripted Usage

```bash
# Fix a specific bug (single command)
aider --message "Fix the KeyError in data_loader.py line 42" \
      src/data/data_loader.py \
      --model claude-opus-4-6 \
      --yes  # Auto-confirm all changes

# Implement a feature from a description
aider --message "Add learning rate warmup to the training loop. \
                 Use linear warmup for the first 10% of steps." \
      src/training/trainer.py \
      --model claude-opus-4-6 \
      --yes

# Batch refactor: add type hints to multiple files
for f in src/**/*.py; do
    aider --message "Add type hints to all function signatures in this file" \
          "$f" --model claude-opus-4-6 --yes
done
```

### CI/CD Integration

```yaml
# .github/workflows/auto-fix-tests.yml
name: Auto-fix failing tests with Aider

on:
  workflow_dispatch:
    inputs:
      branch:
        description: 'Branch to fix'
        required: true

jobs:
  auto-fix:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ inputs.branch }}

      - name: Run tests and capture failures
        run: pytest tests/ --tb=short 2>&1 | tee test_output.txt || true

      - name: Fix failures with Aider
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          pip install aider-chat pytest
          aider --message "$(cat test_output.txt) Fix all failing tests." \
                --model claude-opus-4-6 \
                --yes \
                $(find src/ -name "*.py" | head -20)

      - name: Push fixes
        run: |
          git push origin ${{ inputs.branch }}
```

### Cost Estimates

Since Aider uses pay-per-use API pricing, the cost per task is predictable:

| Task Type | Typical Files in Context | Estimated Cost |
|---|---|---|
| Fix a single bug | 1-3 files | $0.01 - $0.05 |
| Implement a small feature | 3-8 files | $0.05 - $0.20 |
| Add tests for a module | 2-5 files | $0.02 - $0.10 |
| Large refactor (one module) | 10-20 files | $0.20 - $1.00 |

**Best for**: CLI-native developers, remote server work (SSH sessions), CI/CD automation, scripted batch processing of codebases, and anyone who wants fine-grained control over cost via model selection.

---

## 4. GitHub Copilot 2025

**What it is**: Microsoft and GitHub's AI coding assistant, now the enterprise standard. Embedded in VS Code, JetBrains IDEs, and the GitHub web UI. Used by over 1.8 million developers.

**Docs**: [docs.github.com/copilot](https://docs.github.com/en/copilot)

### Key Features (2025 Updates)

#### Copilot Workspace
The highest-level Copilot feature: given a GitHub issue, Copilot Workspace plans, implements, and opens a PR — all from the GitHub web interface.

```
Workflow:
1. Go to any GitHub issue
2. Click "Open in Copilot Workspace"
3. Copilot analyzes the issue and proposes a plan (editable)
4. Approve the plan → Copilot generates code changes
5. Review diffs in browser
6. Click "Create PR" → done
```

#### Agent Mode in VS Code
Copilot's response to Cursor Composer. Activated with `Ctrl+Shift+I` in VS Code, Agent Mode can:
- Edit multiple files simultaneously
- Run terminal commands and respond to output
- Search the codebase to understand context
- Iterate until tests pass

#### Multi-Model Support
GitHub Copilot now lets you choose your underlying model:
- **GPT-4o** — fast, good for everyday coding
- **Claude Sonnet 4** — best for complex reasoning and long contexts
- **Gemini 2.0 Flash** — fastest option
- **o3** — best for algorithmic and math-heavy problems

Switch models per conversation with the model picker in the chat panel.

#### Copilot Extensions
Third-party tools can be added to Copilot as extensions. Current popular ones:
- **Datadog** — ask about production alerts and logs
- **Sentry** — diagnose errors directly in VS Code
- **Docker** — get containerization help
- **Pieces** — personal code snippet management

### Enterprise Features

| Feature | Details |
|---|---|
| **Privacy** | Code never used for training; SOC2 Type II compliant |
| **Policy management** | Admins can enable/disable features, restrict models |
| **Audit logs** | Full log of all Copilot interactions |
| **IP indemnification** | GitHub covers IP claims for Enterprise customers |
| **SAML SSO** | Integrates with Okta, Azure AD, Google Workspace |

### Pricing

| Plan | Price | Notes |
|---|---|---|
| Free | $0 | 2,000 completions/month, 50 chat requests |
| Pro | $10/month | Unlimited completions, all models |
| Business | $19/user/month | Admin controls, policy enforcement |
| Enterprise | $39/user/month | Fine-tuning on your codebase, advanced security |

**Best for**: Enterprise teams already on GitHub. The deep GitHub integration (issues → workspace → PR) is unmatched. Also the safest choice for regulated industries due to compliance certifications.

---

## 5. Comparison Table

| Feature | Cursor | Windsurf | Aider | GitHub Copilot |
|---|---|---|---|---|
| **Base IDE** | VS Code fork | VS Code fork | Terminal/any editor | VS Code, JetBrains, web |
| **Autonomy level** | Medium (Composer with diffs) | High (Cascade, auto-executes) | High (with --yes flag) | Medium (Agent Mode) |
| **Multi-file editing** | Yes (Composer) | Yes (Cascade) | Yes | Yes (Agent Mode) |
| **Git integration** | Manual | Manual | Native (auto-commits) | Via Copilot Workspace |
| **Codebase indexing** | Yes (full codebase) | Yes | Context window only | Yes (via @workspace) |
| **CI/CD integration** | No | No | Yes (CLI, scriptable) | Yes (Copilot Workspace API) |
| **Model flexibility** | Multiple (Claude, GPT-4o, etc.) | Multiple (various) | Any (widest selection) | Multiple (GPT-4o, Claude, Gemini) |
| **Local/offline models** | No | No | Yes (via Ollama) | No |
| **Enterprise features** | Limited | Good | None | Excellent |
| **Pricing** | $20/month | $15/month | Pay-per-use API | $10-$39/month |
| **Best use case** | Complex multi-file refactors | Fully autonomous tasks | CLI, CI/CD, scripted automation | Enterprise, PR-level tasks |
| **Learning curve** | Low | Low | Medium | Very low |

---

## 6. For ML Engineers Specifically

### Setting Up Cursor for Jupyter/Python ML Workflows

Cursor handles `.ipynb` files natively. Key tips:

**1. Use Composer for notebook restructuring:**
```
Cursor Composer prompt:
"Refactor this notebook into a proper Python package:
- Extract the preprocessing code into src/data/preprocessing.py
- Extract model definition into src/models/cnn.py
- Keep the notebook as an experiment script that imports from src/
- Add __init__.py files where needed"
```

**2. Cursor rules for ML projects (`.cursor/rules`):**
```
## ML Project Rules

- All experiments must log to WandB with wandb.init()
- Use hydra @hydra.main() for all training scripts
- DataLoader workers: use cpu_count() // 2
- Always seed: torch.manual_seed, numpy.random.seed, random.seed
- Model checkpoints go in checkpoints/{run_name}/
- Never hardcode learning rates or batch sizes - use config
- Evaluation always uses torch.no_grad() context manager
- For HuggingFace models, always specify trust_remote_code=False
```

**3. Context files to always include:**
- `pyproject.toml` or `setup.py` — so Cursor knows your dependencies
- `conf/config.yaml` — so it knows your Hydra configuration schema
- `src/__init__.py` — project structure overview

### Using Aider to Refactor Training Scripts

Aider excels at systematic, git-tracked refactoring:

```bash
# Add experiment tracking to a training script
aider --message \
  "Add WandB experiment tracking to train.py:
   - wandb.init() at the start with project='my-project'
   - Log train/val loss and accuracy every epoch
   - Log model architecture summary
   - Save best model checkpoint with wandb.save()
   - wandb.finish() at the end" \
  src/train.py \
  --model claude-opus-4-6 \
  --yes

# Convert training script to use Hydra config
aider --message \
  "Convert hardcoded hyperparameters to Hydra configuration:
   - Create conf/config.yaml with all current hyperparams
   - Add @hydra.main decorator to main()
   - Replace all hardcoded values with cfg.field references" \
  src/train.py conf/ \
  --model claude-opus-4-6 \
  --yes

# Add type hints to entire src directory
find src/ -name "*.py" | while read f; do
  aider --message "Add complete type hints to all functions. Import from typing as needed." \
        "$f" --model claude-sonnet-4-6 --yes
done
```

### Windsurf Cascade for Updating Multiple Notebooks

When you have a series of tutorial notebooks that all need updating (e.g., updating from PyTorch 2.0 to 2.4 API changes):

```
Windsurf Cascade prompt:
"Update all Jupyter notebooks in 05-transformers/ to use the PyTorch 2.4 API:
 - Replace deprecated torch.nn.functional.scaled_dot_product_attention
   calls with the new torch.nn.attention module
 - Update any torch.cuda.amp.autocast() calls to use torch.amp.autocast()
 - Fix any deprecation warnings visible in the cell outputs
 - Run each notebook to verify it executes without errors"
```

Cascade will open each notebook, make the changes, attempt to run cells, and fix any errors it introduces — all without step-by-step approval.

### Custom Rules for AI Development Workflow

Create a project-level `.aider.conf.yml` for Aider settings:

```yaml
# .aider.conf.yml
model: claude-opus-4-6
auto-commits: true
commit-prompt: |
  Write a concise commit message for this change.
  Use the format: <type>(<scope>): <description>
  Types: feat, fix, refactor, test, docs, chore
map-tokens: 2048    # Increase for large codebases
```

Create a Cursor-specific system prompt file at `.cursor/system_prompt.md`:

```markdown
You are an expert ML engineer helping with a PyTorch training codebase.

Key facts about this project:
- Framework: PyTorch 2.4 with torch.compile()
- Config: Hydra 1.3
- Experiment tracking: Weights & Biases
- Testing: pytest with hypothesis for property-based tests
- Data: stored in data/ (never commit this directory)
- Models: checkpointed in checkpoints/ (never commit this directory)

When writing code:
1. Prefer vectorized operations over Python loops
2. Use torch.compile() for performance-critical code paths
3. Always add gradient clipping (max_norm=1.0) in training loops
4. Use bfloat16 for mixed precision, not float16
5. Profile before optimizing — use torch.profiler
```

### Recommended Tool Combination for ML Teams

| Scenario | Recommended Tool |
|---|---|
| Daily coding, notebook work | Cursor (codebase context + Tab autocomplete) |
| Large autonomous tasks ("implement this feature") | Windsurf Cascade |
| Refactoring training scripts, adding type hints | Aider (batch, git-tracked) |
| CI/CD: auto-fix failing tests | Aider (headless --yes mode) |
| PR review and issue → code → PR | GitHub Copilot Workspace |
| New developer onboarding | GitHub Copilot (lowest learning curve) |

---

## 7. AI-Assisted Research Tools

For ML engineers who need to stay current with research papers, three tools stand out.

### Perplexity AI

**Website**: [perplexity.ai](https://perplexity.ai)
**Use**: Fast research and fact-checking with citations

Perplexity is a search engine powered by LLMs that always cites its sources. Unlike ChatGPT, every answer links to the actual papers, blog posts, or documentation it used.

**ML use cases**:
- "What is the current state-of-the-art for long-context language models?"
- "What are the main differences between DPO and RLHF?"
- "Find recent papers on synthetic data generation for language models"
- "What changed in PyTorch 2.4 vs 2.3?"

**Pro tips**:
- Use **Perplexity Pro** ($20/month) for access to Claude and GPT-4o models
- Enable **Focus: Academic** to prioritize arxiv and peer-reviewed sources
- Use **Collections** to organize research by topic
- The **Spaces** feature (like Notion + Perplexity) is useful for ongoing research projects

### Elicit

**Website**: [elicit.org](https://elicit.org)
**Use**: Structured paper reading and literature synthesis

Elicit is purpose-built for research workflows. It searches over 125M papers and can:
- Answer questions from across multiple papers simultaneously
- Extract specific data (datasets used, evaluation metrics, model sizes) into tables
- Find papers that cite a specific method or dataset
- Summarize the abstract, methods, and results of multiple papers side by side

**ML use cases**:
```
Example Elicit queries:
- "What benchmarks are used to evaluate code generation models?"
- "How do RLHF and constitutional AI compare for reducing model hallucination?"
- "What methods exist for efficient fine-tuning of large language models?"
- "What are the reported training compute costs for GPT-4 class models?"
```

**Key feature**: The **Notebook** feature lets you extract structured data from papers into columns. For example, you can create a table of "paper | model size | training data | MMLU score" across 50 papers automatically.

**Pricing**: Free tier (limited queries), Pro $12/month for researchers.

### Connected Papers

**Website**: [connectedpapers.com](https://connectedpapers.com)
**Use**: Visual literature review and finding related work

Connected Papers builds a graph visualization of papers related to any seed paper. Nodes are papers, edges represent citation relationships and co-citation similarity. Papers that are frequently cited together cluster together.

**When to use it**:
- Starting research in a new subfield — find the 10-15 most important papers quickly
- Writing the related work section of a paper — see what you might have missed
- Finding derivative works of a seminal paper
- Understanding how a field has evolved (visualized as a "derivative" graph)

**Workflow for ML engineers**:
1. Find a key paper on arxiv (e.g., "Attention Is All You Need")
2. Paste the arxiv URL into Connected Papers
3. Explore the graph — larger nodes = more influential
4. Switch to "Prior Works" view to see foundational papers
5. Switch to "Derivative Works" view to see what built on this paper
6. Export the graph as a citation list for your notes

**Pricing**: Free (5 graphs/month), Academic $3/month (unlimited).

### Bonus: Other Research Tools Worth Knowing

| Tool | Purpose | URL |
|---|---|---|
| **Semantic Scholar** | Paper search with AI-generated summaries | semanticscholar.org |
| **Papers With Code** | Find papers + their official code implementations | paperswithcode.com |
| **Arxiv Sanity** | Better arxiv search and filtering | arxiv-sanity-lite.com |
| **Litmaps** | Alternative to Connected Papers with timeline view | litmaps.com |
| **ResearchRabbit** | Automated literature review and alerts | researchrabbitapp.com |
| **Consensus** | Consensus-based answers from scientific literature | consensus.app |

---

## Quick Reference: Getting Started Today

```bash
# Install all CLI tools
pip install aider-chat cursor-cli  # cursor-cli for command-line access

# Set up Aider with Claude
export ANTHROPIC_API_KEY=your_key_here
aider --model claude-opus-4-6

# Install Cursor
# Download from cursor.com (replaces your current VS Code)

# Install Windsurf
# Download from codeium.com/windsurf (separate install from VS Code)

# GitHub Copilot
# VS Code: Extensions → search "GitHub Copilot" → Install
# Then: gh auth login && gh extension install github/gh-copilot
```

---

*Last updated: February 2026. Tool features and pricing change frequently — check the official documentation for the latest information.*
