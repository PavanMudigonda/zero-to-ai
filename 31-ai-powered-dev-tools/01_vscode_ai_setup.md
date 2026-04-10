# VS Code AI Setup Guide

A hands-on guide to configuring VS Code as a fully AI-powered development environment.

---

## 1. GitHub Copilot: The Three Modes

GitHub Copilot in VS Code operates in three progressively more capable modes:

### 1.1 Completions (Inline)

The default experience. Copilot suggests code as you type, shown as ghost text.

**Key settings** (`settings.json`):
```json
{
  "github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": true,
    "scminput": false
  },
  "editor.inlineSuggest.enabled": true
}
```

**Tips:**
- Press `Tab` to accept, `Esc` to dismiss
- Press `Alt+]` / `Alt+[` to cycle through alternative suggestions
- Write a comment describing what you want, then let Copilot complete the code

### 1.2 Chat (Panel and Inline)

Open the chat panel (`Ctrl+Shift+I` or `Cmd+Shift+I` on macOS) to ask questions, explain code, or request changes.

**Key chat participants:**
| Participant | What it does |
|-------------|-------------|
| `@workspace` | Searches your entire codebase for context |
| `@terminal` | References terminal output |
| `@vscode` | Asks about VS Code settings and commands |

**Slash commands in chat:**
| Command | Effect |
|---------|--------|
| `/explain` | Explain the selected code |
| `/fix` | Fix problems in the selected code |
| `/tests` | Generate tests for the selected code |
| `/doc` | Generate documentation |
| `/new` | Scaffold a new file or project |

### 1.3 Agent Mode

The most powerful mode. Agent mode can:
- Read and edit multiple files
- Run terminal commands and react to output
- Search the codebase for context
- Call MCP tools (databases, APIs, web browsers)
- Iterate until tests pass

**How to use it:**
1. Open Copilot Chat (`Ctrl+Shift+I`)
2. Switch to Agent mode using the mode picker (dropdown at top of chat)
3. Describe your task in natural language
4. Agent proposes edits, runs commands, and iterates

**What makes agent mode different from chat:**
- Chat gives you *suggestions*. Agent mode *executes* changes.
- Agent can run terminal commands and read their output.
- Agent can call MCP tools you've configured.
- Agent iterates: if a test fails, it reads the error and tries again.

---

## 2. Custom Instructions

Custom instructions tell Copilot how to behave in your project. They persist across sessions and apply to every team member who clones the repo.

### 2.1 Repository-Level Instructions

Create `.github/copilot-instructions.md` in your repo root:

```markdown
# Project: Zero to AI Curriculum

## Code Style
- Python 3.12+, use type hints on all function signatures
- Prefer f-strings over .format() or %
- Use pathlib.Path instead of os.path
- Docstrings in Google format

## Project Structure
- Each phase is a numbered directory (00-course-setup/, 01-python/, etc.)
- Notebooks are ordered: 00_START_HERE.ipynb, 01_*, 02_*, ...
- Each directory has a README.md as the chapter entrypoint

## Testing
- Use pytest for all tests
- Run tests with: pytest tests/ -v
- Self-contained notebooks should use toy data, no API keys required

## What NOT to do
- Do not add API keys or secrets to any file
- Do not install packages globally; use .venv
- Do not modify notebooks that have execution outputs without re-running them
```

### 2.2 File-Scoped Instructions (`.instructions.md`)

For instructions that only apply to specific files or directories, create `.instructions.md` files with YAML frontmatter:

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

Place this file anywhere in your repo. The `applyTo` glob pattern controls which files it affects.

### 2.3 Prompt Files (`.prompt.md`)

Reusable prompt templates that appear in the chat's prompt picker:

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

Save as `.github/prompts/add-evaluation.prompt.md`. It will appear in the Copilot chat prompt picker.

---

## 3. Model Selection

Copilot supports multiple models. Switch per conversation using the model picker in the chat panel.

| Model | Best for | Speed |
|-------|----------|-------|
| **GPT-4o** | General coding, fast iteration | Fast |
| **Claude Sonnet 4** | Complex reasoning, long contexts | Medium |
| **o3** | Algorithmic problems, math, hard bugs | Slow |
| **Gemini 2.0 Flash** | Quick questions, simple edits | Fastest |

**Routing strategy:**
- Start with GPT-4o or Gemini Flash for exploration
- Switch to Claude Sonnet 4 or o3 when you hit a hard problem
- Use the same model throughout a multi-step agent task (avoid switching mid-task)

---

## 4. MCP in VS Code

MCP (Model Context Protocol) connects Copilot agent mode to external tools: databases, browsers, APIs, file systems, and custom servers.

### 4.1 Configuration

MCP servers are configured in `.vscode/mcp.json` (workspace-scoped) or your user `settings.json` (global):

**Workspace-scoped** (`.vscode/mcp.json`):
```json
{
  "servers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y", "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/directory"
      ]
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${input:pgConnectionString}"
      }
    }
  }
}
```

**Project-root** (`.mcp.json`) — also supported by Claude Code:
```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["scripts/my_mcp_server.py"]
    }
  }
}
```

### 4.2 Popular MCP Servers

| Server | What it does | Install |
|--------|-------------|---------|
| **Playwright** | Browser automation, screenshots, web scraping | `npx @playwright/mcp@latest` |
| **Filesystem** | Read/write files outside workspace | `npx @modelcontextprotocol/server-filesystem` |
| **PostgreSQL** | Query database, inspect schema | `npx @modelcontextprotocol/server-postgres` |
| **SQLite** | Local database access | `npx @modelcontextprotocol/server-sqlite` |
| **GitHub** | Issues, PRs, repository data | `npx @modelcontextprotocol/server-github` |
| **Memory** | Persistent key-value store across sessions | `npx @modelcontextprotocol/server-memory` |
| **Brave Search** | Web search from agent mode | `npx @modelcontextprotocol/server-brave-search` |
| **Azure** | Azure resource management | VS Code Azure MCP extension |

### 4.3 Using MCP Tools in Agent Mode

Once configured, MCP tools appear automatically in agent mode. When the agent needs to browse a web page, query a database, or read a file, it calls the appropriate MCP tool.

Example agent prompt:
```
Check the current schema of the users table in our Postgres database,
then update the User model in src/models/user.py to match.
Add any missing fields and update the migration file.
```

The agent will:
1. Call the Postgres MCP server to inspect the schema
2. Read `src/models/user.py`
3. Compare and update the model
4. Generate a migration

### 4.4 Verifying MCP Servers

To check if your MCP servers are running:
1. Open the Command Palette (`Ctrl+Shift+P`)
2. Search "MCP: List Servers"
3. Each server should show a green status

If a server fails to start, check:
- Is the command installed? (`npx`, `python`, etc.)
- Are environment variables set?
- Check the Output panel → "MCP" channel for error logs

---

## 5. Extensions That Complement Copilot

| Extension | Purpose |
|-----------|---------|
| **GitHub Copilot** | Core AI assistant |
| **GitHub Copilot Chat** | Chat panel and agent mode |
| **Pylance** | Python language server (provides Copilot with type info) |
| **Jupyter** | Notebook support |
| **Error Lens** | Inline error display (helps agent see errors faster) |
| **GitLens** | Git blame and history (useful context for agent) |

---

## 6. Recommended `settings.json` for AI-Powered Development

```json
{
  // Copilot
  "github.copilot.enable": { "*": true },
  "chat.agent.enabled": true,

  // Python
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,

  // Terminal (helps agent mode read output)
  "terminal.integrated.scrollback": 10000,

  // Editor (helps Copilot understand your code)
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "ms-python.black-formatter",

  // Files (reduce noise in @workspace searches)
  "files.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true,
    "**/node_modules": true,
    "**/*.egg-info": true
  }
}
```

---

## 7. Troubleshooting

| Problem | Fix |
|---------|-----|
| Agent mode not available | Update VS Code and Copilot extension to latest version |
| MCP server won't start | Check Output → MCP channel; verify command is installed |
| Agent doesn't use MCP tools | Ensure you're in Agent mode (not Chat mode); check server status |
| Copilot ignores instructions | Verify `.github/copilot-instructions.md` path is exact; check file is UTF-8 |
| Model picker not showing | Requires Copilot Pro or Business plan |
| Slow responses | Switch to a faster model (GPT-4o or Gemini Flash) |

---

*Next: [02_mcp_deep_dive.md](02_mcp_deep_dive.md) — the MCP protocol in depth*
