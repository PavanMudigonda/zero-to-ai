#!/usr/bin/env python3
"""
Update 13_agentic_coding_ides.ipynb with the latest official docs:
  - VS Code Copilot: add Agents Window (Preview), pricing pause note
  - Cursor: update model names to match current docs
  - Claude Code: add Essential CLI Commands table
  - OpenAI Codex: URL fix in table
  - Google Antigravity: fix get-started URL, add slash commands + agent modes + navigation
"""
import json

PATH = "jupyter-notebooks/15-ai-agents/13_agentic_coding_ides/13_agentic_coding_ides.ipynb"

with open(PATH) as f:
    nb = json.load(f)

def get_src(cell):
    return ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']

def set_src(cell, text):
    cell['source'] = text.splitlines(keepends=True)

changes = []

# ─────────────────────────────────────────────────────────────────────────────
# Cell 2 — The Five Major Agentic IDEs table
# ─────────────────────────────────────────────────────────────────────────────
cell = nb['cells'][2]
src = get_src(cell)

# Fix Antigravity URL: get-started → getting-started
OLD = "**[Google Antigravity](https://antigravity.google/docs/get-started)**"
NEW = "**[Google Antigravity](https://antigravity.google/docs/getting-started)**"
if OLD in src:
    src = src.replace(OLD, NEW)
    changes.append("Cell 2: fixed Antigravity URL")
else:
    print("WARNING Cell 2: Antigravity URL not found (may already be correct)")

# Update Cursor model: Composer 2 → Composer 2.5
OLD = "Claude, GPT, Gemini, Composer 2 | 2023 (editor), 2025 (agent)"
NEW = "Claude, GPT, Gemini, Composer 2.5 | 2023 (editor), 2025 (agent)"
if OLD in src:
    src = src.replace(OLD, NEW)
    changes.append("Cell 2: updated Cursor Composer 2 → 2.5")

set_src(cell, src)


# ─────────────────────────────────────────────────────────────────────────────
# Cell 4 — GitHub Copilot deep dive
# ─────────────────────────────────────────────────────────────────────────────
cell = nb['cells'][4]
src = get_src(cell)

# Add Agents Window to Key Features list
OLD = "- **Browser Testing** - (Experimental) Ask agents to open and verify web apps"
NEW = (
    "- **Browser Testing** - (Experimental) Ask agents to open and verify web apps\n"
    "- **Agents Window** (Preview) - Agent-first surface with a Changes panel for reviewing edits; "
    "connect to remote machines via SSH or dev tunnel; "
    "monitor all sessions from any browser at [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents)"
)
if OLD in src:
    src = src.replace(OLD, NEW)
    changes.append("Cell 4: added Agents Window to Key Features")

# Update Pricing section with April 2026 pause notice
OLD = (
    "### Pricing\n\n"
    "- **Free tier** - Limited monthly completions and chat\n"
    "- **Pro / Pro+** - More usage, premium models\n"
    "- **Enterprise** - Org-wide policies, SSO, IP indemnity"
)
NEW = (
    "### Pricing\n\n"
    "- **Free tier** - Limited monthly completions and chat\n"
    "- **Pro / Pro+** - More usage, premium models\n"
    "- **Enterprise** - Org-wide policies, SSO, IP indemnity\n\n"
    "> **Note (April 2026):** New sign-ups for Copilot Pro and Pro+ plans are temporarily paused; "
    "weekly usage limits have been tightened. "
    "See [GitHub Copilot plans](https://docs.github.com/en/copilot/get-started/plans) for current availability."
)
if OLD in src:
    src = src.replace(OLD, NEW)
    changes.append("Cell 4: added April 2026 pricing pause note")

set_src(cell, src)


# ─────────────────────────────────────────────────────────────────────────────
# Cell 5 — Cursor deep dive
# ─────────────────────────────────────────────────────────────────────────────
cell = nb['cells'][5]
src = get_src(cell)

# Update model names to match current cursor.com/docs
OLD = "- **Models** - Claude 4.6/4.7, GPT-5.3/5.5, Gemini 3.1, Grok 4.20, Composer 2 (custom)"
NEW = "- **Models** - Claude 4.6 Sonnet / 4.7 Opus, GPT-5.3 Codex / 5.5, Gemini 3.1 Pro / 3.5 Flash, Grok 4.3, Composer 2.5 (custom)"
if OLD in src:
    src = src.replace(OLD, NEW)
    changes.append("Cell 5: updated Cursor model names")

set_src(cell, src)


# ─────────────────────────────────────────────────────────────────────────────
# Cell 6 — Claude Code deep dive
# ─────────────────────────────────────────────────────────────────────────────
cell = nb['cells'][6]
src = get_src(cell)

# Add Essential CLI Commands section before Pricing
OLD = "### Pricing\n\n- Requires a **Claude subscription**"
NEW = (
    "### Essential CLI Commands\n\n"
    "| Command | Description | Example |\n"
    "|---------|-------------|---------|\n"
    "| `claude` | Start interactive mode | `claude` |\n"
    "| `claude \"task\"` | Run a one-time task | `claude \"fix the build error\"` |\n"
    "| `claude -p \"query\"` | One-off query, then exit | `claude -p \"explain this function\"` |\n"
    "| `claude -c` | Continue most recent conversation | `claude -c` |\n"
    "| `claude -r` | Resume a previous conversation | `claude -r` |\n"
    "| `/clear` | Clear conversation history | `/clear` |\n"
    "| `/help` | Show available commands | `/help` |\n"
    "| `exit` / `Ctrl+D` | Exit Claude Code | `exit` |\n\n"
    "### Pricing\n\n- Requires a **Claude subscription**"
)
if OLD in src:
    src = src.replace(OLD, NEW)
    changes.append("Cell 6: added Essential CLI Commands section")

set_src(cell, src)


# ─────────────────────────────────────────────────────────────────────────────
# Cell 8 — Google Antigravity deep dive
# ─────────────────────────────────────────────────────────────────────────────
cell = nb['cells'][8]
src = get_src(cell)

# Add Agent Modes (starting a session) between Architecture and Core Components
OLD = "### Core Components"
NEW = (
    "### Agent Modes (Starting a Session)\n\n"
    "When spawning an agent in a Project, choose a mode:\n\n"
    "| Mode | Description |\n"
    "|------|-------------|\n"
    "| **Local Mode** | Agent operates directly in your active project folders |\n"
    "| **New Worktree Mode** | Agent operates in an isolated Git worktree (safe parallel experimentation) |\n\n"
    "### Core Components"
)
if OLD in src:
    src = src.replace(OLD, NEW)
    changes.append("Cell 8: added Agent Modes section")

# Add Slash Commands + Basic Navigation before Platform Support
OLD = "### Platform Support"
NEW = (
    "### Slash Commands\n\n"
    "| Command | Description |\n"
    "|---------|-------------|\n"
    "| `/goal` | Run until the task is fully finished — no intermediate input from user |\n"
    "| `/grill-me` | Agent asks clarifying questions before starting to implement |\n"
    "| `/schedule` | Run an instruction as a one-time or recurring scheduled task |\n"
    "| `/browser` | Explicitly enable browser primitives for the session (requires Chrome permission) |\n\n"
    "### Basic Navigation\n\n"
    "| Action | macOS | Windows |\n"
    "|--------|-------|---------|\n"
    "| Open Conversation Picker | `⌘K` | `Ctrl+K` |\n"
    "| Open File Search | `⌘P` | `Ctrl+P` |\n"
    "| Focus Input | `⌘L` | `Ctrl+L` |\n"
    "| New Conversation | `⌘N` | `Ctrl+N` |\n"
    "| Next / Previous Conversation | `⌥↑` / `⌥↓` | `Alt+↑` / `Alt+↓` |\n\n"
    "### Platform Support"
)
if OLD in src:
    src = src.replace(OLD, NEW)
    changes.append("Cell 8: added Slash Commands + Basic Navigation")

set_src(cell, src)


# ─────────────────────────────────────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────────────────────────────────────
with open(PATH, 'w') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print(f"\nApplied {len(changes)} change(s):")
for c in changes:
    print(f"  ✓ {c}")
print("\nSaved:", PATH)
