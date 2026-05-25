#!/usr/bin/env python3
"""
1. Add VS Code Extensions comparison section to 02_vscode_ai_setup.ipynb
2. Add VS Code extension install step to Claude Code deep dive (cell 6)
3. Add VS Code extension install step to Codex deep dive (cell 7)
   in 13_agentic_coding_ides.ipynb
"""
import json

# ─────────────────────────────────────────────────────────────────
# 1. 02_vscode_ai_setup.ipynb — insert new section before cell 16 (Troubleshooting)
# ─────────────────────────────────────────────────────────────────
PATH1 = "jupyter-notebooks/31-ai-powered-dev-tools/02_vscode_ai_setup/02_vscode_ai_setup.ipynb"
with open(PATH1) as f:
    nb1 = json.load(f)

NEW_MD_SRC = """\

---

## 5. VS Code Extensions: All Three Agents Side-by-Side

You can run **GitHub Copilot, Claude Code, and OpenAI Codex** directly inside VS Code — no separate app needed.

| Extension | Publisher ID | Marketplace |
|-----------|-------------|-------------|
| **GitHub Copilot** | `GitHub.copilot` + `GitHub.copilot-chat` | [Install](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) |
| **Claude Code** | `Anthropic.claude-code` | [Install](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code) |
| **OpenAI Codex** | `openai.codex` | [Install](https://marketplace.visualstudio.com/items?itemName=openai.codex) |

### Install from the Command Line

```bash
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
code --install-extension Anthropic.claude-code
code --install-extension openai.codex
```

### What Each Extension Adds

| Feature | GitHub Copilot | Claude Code | OpenAI Codex |
|---------|---------------|-------------|-------------|
| **Sidebar panel** | ✅ Chat + Sessions | ✅ Claude Code panel | ✅ Codex panel |
| **Inline chat** (`⌘I`) | ✅ | ✅ | ✅ |
| **Agent mode** | ✅ (full — local, background, cloud) | ✅ (same engine as CLI) | ✅ (same engine as desktop app) |
| **MCP support** | ✅ (`.vscode/mcp.json`) | ✅ (`.mcp.json`) | ✅ |
| **Free tier** | ✅ (limited monthly) | ❌ (requires Claude subscription) | ✅ (ChatGPT Plus/Pro plan) |
| **Project rules file** | `*.instructions.md` | `CLAUDE.md` | `AGENTS.md` |

> **Tip:** All three extensions work in the same workspace and can share MCP servers. Switch between them depending on the task or model you prefer.

---

## 6. Recommended Settings (`settings.json`) for All Three\
"""

NEW_CELL = {
    "cell_type": "markdown",
    "metadata": {},
    "source": NEW_MD_SRC.splitlines(keepends=True)
}

# Insert before the existing cell 15 (recommended settings JSON) and cell 16 (Troubleshooting)
# Current cell 15 is a settings.json code cell — relabel it as section 6 content
# Insert the new markdown cell at position 15 (before current cells 15 & 16)
nb1['cells'].insert(15, NEW_CELL)
print(f"02_vscode_ai_setup: inserted new cell at position 15 (total now: {len(nb1['cells'])})")

with open(PATH1, 'w') as f:
    json.dump(nb1, f, ensure_ascii=False, indent=1)


# ─────────────────────────────────────────────────────────────────
# 2 & 3. 13_agentic_coding_ides.ipynb
# ─────────────────────────────────────────────────────────────────
PATH2 = "jupyter-notebooks/15-ai-agents/13_agentic_coding_ides/13_agentic_coding_ides.ipynb"
with open(PATH2) as f:
    nb2 = json.load(f)

# Cell 6: Claude Code — add VS Code extension to Installation section
cell6 = nb2['cells'][6]
src = ''.join(cell6['source']) if isinstance(cell6['source'], list) else cell6['source']

OLD_INSTALL = (
    "### Installation\n\n"
    "```bash\n"
    "# macOS / Linux / WSL\n"
    "curl -fsSL https://claude.ai/install.sh | bash\n\n"
    "# Then use it\n"
    "cd your-project\n"
    "claude\n"
    "```"
)
NEW_INSTALL = (
    "### Installation\n\n"
    "```bash\n"
    "# macOS / Linux / WSL (CLI)\n"
    "curl -fsSL https://claude.ai/install.sh | bash\n\n"
    "# VS Code extension\n"
    "code --install-extension Anthropic.claude-code\n\n"
    "# Then use the CLI\n"
    "cd your-project\n"
    "claude\n"
    "```\n\n"
    "> **Marketplace:** [marketplace.visualstudio.com/items?itemName=Anthropic.claude-code](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code)"
)
if OLD_INSTALL in src:
    src = src.replace(OLD_INSTALL, NEW_INSTALL)
    cell6['source'] = src.splitlines(keepends=True)
    print("13_agentic_coding_ides cell 6: added VS Code extension install")
else:
    print("WARNING: cell 6 install section not matched")

# Cell 7: OpenAI Codex — add VS Code extension install section
cell7 = nb2['cells'][7]
src7 = ''.join(cell7['source']) if isinstance(cell7['source'], list) else cell7['source']

OLD_PRICING7 = "### Pricing\n\n- Included with **ChatGPT Plus, Pro, Business, Edu, Enterprise** plans"
NEW_PRICING7 = (
    "### Installation\n\n"
    "```bash\n"
    "# VS Code extension\n"
    "code --install-extension openai.codex\n"
    "```\n\n"
    "> **Marketplace:** [marketplace.visualstudio.com/items?itemName=openai.codex](https://marketplace.visualstudio.com/items?itemName=openai.codex)\n\n"
    "### Pricing\n\n- Included with **ChatGPT Plus, Pro, Business, Edu, Enterprise** plans"
)
if OLD_PRICING7 in src7:
    src7 = src7.replace(OLD_PRICING7, NEW_PRICING7)
    cell7['source'] = src7.splitlines(keepends=True)
    print("13_agentic_coding_ides cell 7: added VS Code extension install")
else:
    print("WARNING: cell 7 pricing section not matched")

with open(PATH2, 'w') as f:
    json.dump(nb2, f, ensure_ascii=False, indent=1)

print("Done.")
