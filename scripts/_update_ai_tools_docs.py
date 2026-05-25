#!/usr/bin/env python3
"""
Update AI coding tools content in course notebooks based on May 2026 docs.
Targets: 03_ai_dev_tools_2026.ipynb and 10_autonomous_agents_2026.ipynb
"""
import json

NB1 = "jupyter-notebooks/31-ai-powered-dev-tools/03_ai_dev_tools_2026/03_ai_dev_tools_2026.ipynb"
NB2 = "jupyter-notebooks/15-ai-agents/10_autonomous_agents_2026/10_autonomous_agents_2026.ipynb"

def load(path):
    with open(path) as f:
        return json.load(f)

def save(nb, path):
    with open(path, "w") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"Saved {path}")

def get_src(cell):
    s = cell["source"]
    return "".join(s) if isinstance(s, list) else s

def set_src(cell, text):
    cell["source"] = text

# ──────────────────────────────────────────────────────────────────────────────
# Notebook 1: 03_ai_dev_tools_2026.ipynb
# ──────────────────────────────────────────────────────────────────────────────
nb1 = load(NB1)
cells = nb1["cells"]

# ── Cell 0: ToC / title ──────────────────────────────────────────────────────
src0 = get_src(cells[0])
src0 = src0.replace(
    "# AI Coding Tools for ML Engineers (March 2026)",
    "# AI Coding Tools for ML Engineers (May 2026)"
)
src0 = src0.replace(
    "2. [Windsurf (by Codeium, acquired by OpenAI)](#2-windsurf-by-codeium-acquired-by-openai)",
    "2. [Windsurf (by Codeium, acquired by Cognition AI)](#2-windsurf-by-codeium-acquired-by-cognition-ai)"
)
src0 = src0.replace(
    "## March 6, 2026 Update Snapshot",
    "## May 2026 Update Snapshot"
)
set_src(cells[0], src0)
print("Cell 0: updated title, ToC Windsurf line, snapshot date")

# ── Cell 8: Windsurf pricing + Aider models list ─────────────────────────────
src8 = get_src(cells[8])

# Fix Windsurf pricing table
src8 = src8.replace(
    """### Pricing

| Plan | Price | Notes |
|---|---|---|
| Free | $0 | 5 Cascade requests/day, basic autocomplete |
| Pro | $15/month | 75 Cascade requests/day, all models |
| Teams | $35/user/month | Enterprise features, admin dashboard |

**Best for**: Teams who want truly autonomous multi-step coding workflows. If you want to say "implement this feature" and come back when it's done, Windsurf Cascade is the best current option. Also excellent for enterprise teams due to its OpenAI backing and enterprise security posture.""",
    """### Pricing

| Plan | Price | Includes |
|---|---|---|
| Free | $0 | Light Cascade quota (refreshes daily/weekly), unlimited Tab completions |
| Pro | $20/month | Standard quota + all frontier models (Claude, OpenAI, Gemini) + SWE-1.6 + Devin Cloud access |
| Max | $200/month | Heavy quota, same features as Pro |
| Teams | $40/user/month | Pro features + centralized billing + admin dashboard + automated zero-data-retention |
| Enterprise | Custom | SSO, RBAC, hybrid deployment, dedicated account management |

> **Note**: Windsurf was acquired by Cognition AI (makers of Devin) in 2026. The Pro plan now includes access to Devin Cloud agents and Cognition's SWE-1.6 model. Pricing changed significantly from the prior Codeium-era plans.

**Best for**: Teams who want truly autonomous multi-step coding workflows. If you want to say "implement this feature" and come back when it's done, Windsurf Cascade is the best current option. Also excellent for enterprise teams due to its Cognition AI backing (Devin Cloud integration) and enterprise security posture."""
)

# Fix Aider models list (Opus 4.6 → 4.7)
src8 = src8.replace(
    "- Anthropic Claude (Opus 4.6, Sonnet 4.6, Haiku 4.5)",
    "- Anthropic Claude (Opus 4.7, Sonnet 4.6, Haiku 4.5)"
)

set_src(cells[8], src8)
print("Cell 8: updated Windsurf pricing, added Cognition AI note, fixed Opus version")

# ── Cell 9: Aider install ─────────────────────────────────────────────────────
src9 = get_src(cells[9])
src9 = src9.replace(
    """# Install
pip install aider-chat

# Start with Claude Opus 4 (recommended for complex tasks)
aider --model claude-opus-4-7

# Start with a specific file
aider src/training/trainer.py --model claude-opus-4-7

# Use with OpenAI
aider --model gpt-4o

# Use with a local model via Ollama
aider --model ollama/llama3.3""",
    """# Recommended: one-liner installer (installs Python 3.12 if needed)
curl -LsSf https://aider.chat/install.sh | sh   # macOS / Linux
# powershell -ExecutionPolicy ByPass -c "irm https://aider.chat/install.ps1 | iex"  # Windows

# Alternative: aider-install (pip-based)
pip install aider-install && aider-install

# Or plain pip (use a virtualenv)
pip install -U aider-chat

# ── Start aider ──
# Claude Opus 4.7 (recommended for complex tasks)
aider --model claude-opus-4-7

# Shorthand aliases work too
aider --model sonnet --api-key anthropic=<key>    # Claude Sonnet
aider --model o3-mini --api-key openai=<key>       # o3-mini

# Start on a specific file
aider src/training/trainer.py --model claude-opus-4-7

# Use with OpenAI
aider --model gpt-4o

# Use with a local model via Ollama
aider --model ollama/llama3.3"""
)
set_src(cells[9], src9)
print("Cell 9: updated aider install to recommend one-liner")

# ── After cell 10 (Key Aider Commands): add chat modes cell if not present ───
# Check if chat modes are already covered
modes_present = any(
    "/ask" in get_src(c) and "architect" in get_src(c)
    for c in cells[9:16]
)
if not modes_present:
    # Insert a new markdown cell after cell 10 explaining chat modes
    modes_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": (
            "\n"
            "### Chat Modes\n\n"
            "Aider has four interactive chat modes you can switch between at any time:\n\n"
            "| Mode | Command | Purpose |\n"
            "|---|---|---|\n"
            "| `code` | `/code` | Default — Aider edits your files |\n"
            "| `ask` | `/ask` | Discuss and plan without making changes |\n"
            "| `architect` | `/architect` | Two-model mode: one plans, one edits — best for reasoning models (o3, R1) |\n"
            "| `help` | `/help` | Answer questions about aider itself |\n\n"
            "Switch modes mid-session: `/chat-mode architect`  \n"
            "Or launch in a mode: `aider --architect` (same as `--chat-mode architect`)\n\n"
            "**Recommended workflow**: Use `/ask` to agree on the plan, then `/code` or plain "
            "`go ahead` to execute it.\n"
        )
    }
    # Insert after cell 10 (index 10 → insert at 11)
    cells.insert(11, modes_cell)
    print("Inserted new cell 11: Aider chat modes")
else:
    print("Cell 9-15: chat modes already covered, skipping")

# Re-index cells after potential insert
cells = nb1["cells"]

# ── Find and fix OpenHands cell ───────────────────────────────────────────────
for ci, cell in enumerate(cells):
    src = get_src(cell)
    if "install.openhands.dev" in src or "uv tool install openhands" in src:
        src = src.replace(
            "# Dedicated Python 3.12+ tool environment recommended\nuv tool install openhands --python 3.12\n\n# Or standalone binary\ncurl -fsSL https://install.openhands.dev/install.sh | sh",
            "# Option 1: Cloud (no install)\n# Visit https://app.all-hands.dev  — sign in and create a task\n\n# Option 2: Self-hosted via uv (Python 3.12 tool env)\nuv tool install openhands --python 3.12\n\n# Option 3: Docker\ndocker pull docker.all-hands.dev/all-hands-ai/openhands:latest\n\n# Docs: https://docs.openhands.dev"
        )
        set_src(cell, src)
        print(f"Cell {ci}: updated OpenHands install options + new docs URL")
        break

# ── Find and fix OpenCode install cell ───────────────────────────────────────
for ci, cell in enumerate(cells):
    src = get_src(cell)
    if cell["cell_type"] == "code" and "brew install anomalyco/tap/opencode" in src and "curl" not in src:
        src = src.replace(
            "# macOS and Linux\nbrew install anomalyco/tap/opencode\n\n# npm\nnpm i -g opencode-ai@latest",
            "# Recommended: one-liner install\ncurl -fsSL https://opencode.ai/install | bash\n\n# macOS / Linux (Homebrew)\nbrew install anomalyco/tap/opencode\n\n# npm / pnpm\nnpm install -g opencode-ai\n\n# Then run in your project directory\nopencode"
        )
        set_src(cell, src)
        print(f"Cell {ci}: updated OpenCode install with one-liner")
        break

# ── Find and fix OpenCode description cell (Plan mode, /init) ────────────────
for ci, cell in enumerate(cells):
    src = get_src(cell)
    if "Terminal-first UX with built-in planning and execution agents" in src:
        src = src.replace(
            "**Why teams use it**:\n- Terminal-first UX with built-in planning and execution agents\n- Provider-agnostic model support instead of being tied to one vendor\n- Strong fit for SSH, remote dev boxes, and neovim/TUI-heavy workflows\n\n**Good use cases**:\n- Developers who do most work over SSH or in tmux\n- Teams that want open-source Claude-Code-like workflows\n- Multi-provider setups using Claude, OpenAI, Gemini, or local models",
            "**Key features**:\n- **Plan mode** (press `Tab`): disables file edits so the agent only proposes a plan you can review before switching back to Build mode\n- **`/init` command**: analyzes your project and creates an `AGENTS.md` file — commit this to help OpenCode understand your project\n- **`/connect` command**: configure LLM providers from inside the TUI\n- **`/undo` / `/redo`**: revert or redo agent changes mid-session\n- **`/share`**: create a shareable link to the current conversation\n- **OpenCode Zen**: curated list of verified models at [opencode.ai/docs/zen](https://opencode.ai/docs/zen)\n\n**Why teams use it**:\n- Terminal-first TUI with built-in Plan/Build mode separation\n- Provider-agnostic: Claude, OpenAI, Gemini, local models via any API-compatible provider\n- Strong fit for SSH, remote dev boxes, and neovim/TUI-heavy workflows\n\n**Good use cases**:\n- Developers who do most work over SSH or in tmux\n- Teams that want open-source Claude-Code-like workflows\n- Multi-provider setups using Claude, OpenAI, Gemini, or local models"
        )
        set_src(cell, src)
        print(f"Cell {ci}: updated OpenCode description with Plan mode, /init, /connect, /undo, Zen")
        break

# ── Find and fix mini-swe-agent install cell ─────────────────────────────────
for ci, cell in enumerate(cells):
    src = get_src(cell)
    if cell["cell_type"] == "code" and "pip install mini-swe-agent" in src and "uvx mini-swe-agent" in src:
        src = src.replace(
            "pip install mini-swe-agent\n\n# Or ephemeral CLI execution\nuvx mini-swe-agent",
            "# Option 1: Ephemeral (no install, try it now)\npip install uv && uvx mini-swe-agent\n\n# Option 2: Install in current environment\npip install mini-swe-agent\nmini   # launch the CLI (v2+)\n\n# Option 3: Install with pipx (PATH-safe)\npip install pipx && pipx ensurepath && pipx run mini-swe-agent"
        )
        set_src(cell, src)
        print(f"Cell {ci}: updated mini-swe-agent install to uvx-first + mini CLI")
        break

# ── Find and fix mini-swe-agent description cell ─────────────────────────────
for ci, cell in enumerate(cells):
    src = get_src(cell)
    if "Very small, understandable architecture" in src and "swe-bench-style tasks" in src:
        src = src.replace(
            "**Why teams use it**:\n- Very small, understandable architecture\n- Excellent for experiments, swe-bench-style tasks, and research baselines\n- Easy to script and reason about compared with larger agent frameworks\n\n**Good use cases**:\n- Benchmarking coding-agent performance\n- Research environments comparing prompts, models, and policies\n- Small teams that want a simple CLI agent instead of a full IDE workflow",
            "**mini-swe-agent v2** (`mini` CLI) — now scoring **>74% on SWE-bench Verified**, with Gemini 3 Pro reaching 74% using this agent.\n\n**New in v2**: migration from v1; faster startup than Claude Code; new benchmark [ProgramBench](https://mini-swe-agent.com/latest/usage/programbench/) (extremely challenging).\n\n**Adopted by**: Meta, NVIDIA, IBM, Essential AI, Nebius, Anyscale, Princeton University, Stanford University.\n\n**Why teams use it**:\n- ~100 lines of Python for the core agent — fully auditable architecture\n- Excellent for experiments, SWE-bench-style tasks, and research baselines\n- Compatible with all models via litellm, OpenRouter, and Portkey\n- Supports local envs, Docker/Podman, Singularity, bubblewrap, and more\n\n**Good use cases**:\n- Benchmarking coding-agent performance\n- Research environments comparing prompts, models, and policies\n- Small teams that want a simple CLI agent instead of a full IDE workflow"
        )
        set_src(cell, src)
        print(f"Cell {ci}: updated mini-swe-agent description with v2, >74%, Gemini 3, ProgramBench")
        break

# ── Fix final setup cell (cell near end) ─────────────────────────────────────
for ci, cell in enumerate(cells):
    src = get_src(cell)
    if "pip install aider-chat mini-swe-agent" in src and "# Install Python CLI tools" in src:
        src = src.replace(
            "# Install Python CLI tools\npip install aider-chat mini-swe-agent",
            "# Install aider (one-liner, includes Python 3.12 if needed)\ncurl -LsSf https://aider.chat/install.sh | sh\n\n# Install mini-swe-agent v2\npip install mini-swe-agent  # then run: mini"
        )
        # Fix OpenCode line
        src = src.replace("npm i -g opencode-ai@latest", "curl -fsSL https://opencode.ai/install | bash  # or: npm install -g opencode-ai")
        # Fix the `mini` CLI comment
        src = src.replace(
            "# Try mini-swe-agent quickly\nmini",
            "# mini-swe-agent v2 CLI\nmini  # after: pip install mini-swe-agent"
        )
        set_src(cell, src)
        print(f"Cell {ci}: updated final setup cell install commands")
        break

# ── Fix footer date ───────────────────────────────────────────────────────────
for ci, cell in enumerate(cells):
    src = get_src(cell)
    if "Last updated: March 6, 2026" in src:
        set_src(cell, src.replace("Last updated: March 6, 2026", "Last updated: May 2026"))
        print(f"Cell {ci}: updated footer date to May 2026")
        break

save(nb1, NB1)

# ──────────────────────────────────────────────────────────────────────────────
# Notebook 2: 10_autonomous_agents_2026.ipynb
# ──────────────────────────────────────────────────────────────────────────────
nb2 = load(NB2)
cells2 = nb2["cells"]

for ci, cell in enumerate(cells2):
    src = get_src(cell)

    # Fix Devin pricing (Cognition AI standalone was $500/month, but Windsurf now includes Devin Cloud at $20/month)
    if "Cognition AI's proprietary coding agent that costs $500/month" in src:
        src = src.replace(
            "OpenHands (formerly OpenDevin) is an open-source autonomous software engineering agent. It is the community's answer to Devin, Cognition AI's proprietary coding agent that costs $500/month.",
            "OpenHands (formerly OpenDevin) is an open-source autonomous software engineering agent. It is the community's answer to Devin — Cognition AI's autonomous coding product. Devin Cloud is now accessible via the Windsurf Pro plan ($20/month) after Cognition AI acquired Windsurf."
        )
        set_src(cell, src)
        print(f"NB2 Cell {ci}: updated OpenHands/Devin description to reflect Windsurf acquisition")

save(nb2, NB2)
print("\nDone.")
