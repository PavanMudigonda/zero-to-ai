# AI-Powered Development with VS Code & GitHub Copilot

## Overview

This chapter teaches you how to turn VS Code into a fully AI-native development environment. We go deep on the three systems that make Copilot truly powerful: **agent mode**, **MCP (Model Context Protocol)**, and **custom instructions**.

For a surface-level comparison of all AI coding tools, see [00_ai_dev_tools_2026.md](00_ai_dev_tools_2026.md). This chapter focuses exclusively on VS Code + GitHub Copilot.

**Prerequisites:**
- Comfortable with Python and VS Code
- Familiarity with git basics
- Completed at least Phases 0-8 of the curriculum

**Time:** 1 week | 10-15 hours
**Outcome:** A fully configured VS Code environment with Copilot agent mode, MCP servers, custom instructions, and model routing

This phase is optional but useful much earlier than Phase 31 for many learners. If AI-assisted development helps you move faster, you can study it in parallel once you are comfortable with Python, git, and the basic repo structure.

---

## What You'll Learn

- [ ] How Copilot's three modes work: completions, chat, and agent mode
- [ ] How to configure and use MCP servers to connect Copilot to databases, browsers, and APIs
- [ ] How to write custom instructions (`.github/copilot-instructions.md`, `.instructions.md`, `.prompt.md`)
- [ ] How to select and route between models (GPT-4o, Claude, o3, Gemini)
- [ ] How to build your own MCP server in Python
- [ ] Real VS Code workflows for multi-file editing, debugging, testing, and code review

---

## Module Structure

```
31-ai-powered-dev-tools/
├── README.md                           # This file
├── 01_vscode_ai_setup.md               # Copilot modes, model selection, settings
├── 02_mcp_deep_dive.md                 # MCP protocol, server catalog, configuration
├── 03_copilot_instructions_guide.md    # All 7 customization primitives
├── 04_copilot_workflows.md             # Real VS Code + Copilot workflows
└── 05_build_mcp_server.ipynb           # Hands-on: build an MCP server in Python
```

---

## Learning Path

Suggested timing:
- Study early if you actively code every day and want tooling leverage.
- Study later if you prefer to first understand the core AI concepts before customizing your dev environment.

### Day 1-2: VS Code AI Setup
- [ ] Read `01_vscode_ai_setup.md`
- [ ] Configure Copilot agent mode and model selection
- [ ] Set up at least one MCP server in your workspace
- [ ] **Exercise:** Use agent mode to refactor a file, run tests, and fix failures

### Day 3-4: MCP Deep Dive
- [ ] Read `02_mcp_deep_dive.md`
- [ ] Understand the MCP protocol: tools, resources, prompts
- [ ] Configure Playwright MCP, a database MCP, or a filesystem MCP
- [ ] Run through `05_build_mcp_server.ipynb` to build your own
- [ ] **Exercise:** Build an MCP server that exposes your project's test results

### Day 5: Custom Instructions and Workflows
- [ ] Read `03_copilot_instructions_guide.md`
- [ ] Create a `.github/copilot-instructions.md` for this repo
- [ ] Create at least one scoped `.instructions.md` file
- [ ] Read `04_copilot_workflows.md`
- [ ] **Exercise:** Create a `.prompt.md` file for a common task in your project

---

## Key Concepts

### The Three Layers of AI-Assisted Development

```
┌─────────────────────────────────────────────┐
│  Layer 3: Agent Mode                        │
│  (multi-file edits, test-run-fix loops,     │
│   autonomous task completion)               │
├─────────────────────────────────────────────┤
│  Layer 2: MCP Tools                         │
│  (database access, web search, file system, │
│   API calls, custom tools)                  │
├─────────────────────────────────────────────┤
│  Layer 1: Custom Instructions               │
│  (copilot-instructions.md,                  │
│   .instructions.md, .prompt.md)             │
└─────────────────────────────────────────────┘
```

Most developers only use Layer 3 (the chat). The 10x productivity gain comes from configuring Layers 1 and 2 properly.

### Why This Chapter Exists

Copilot in 2026 is not autocomplete. It is:
- An **agent** that reads your codebase, runs commands, and iterates on errors
- **Protocol-connected** via MCP to databases, APIs, browsers, and cloud services
- **Instruction-driven** by project-level config files that shape every response
- **Multi-model** with routing between GPT-4o, Claude, o3, and Gemini per task

Understanding how to configure these systems is as important as understanding the models themselves.

---

## How This Chapter Relates to Other Phases

| Phase | Connection |
|-------|-----------|
| **00 - AI Dev Tools** | `00_ai_dev_tools_2026.md` compares all AI coding tools; this chapter goes deep on VS Code |
| **08 - RAG** | MCP servers can expose your RAG pipeline as a tool Copilot can call |
| **15 - AI Agents** | The agent patterns (plan → act → observe → reflect) are exactly what Copilot agent mode does |
| **18 - Low-Code AI Tools** | Gradio/Streamlit build UIs; this chapter builds developer workflows |

## What Comes Next

- Apply these workflows while working through the rest of the curriculum.
- Pair this phase with [../15-ai-agents/README.md](../15-ai-agents/README.md) if you want to understand coding agents more deeply.
- Pair this phase with [../09-mlops/README.md](../09-mlops/README.md) if you want practical repo automation and deployment workflows.

---

## Quick Reference: Copilot Configuration Files

| File | Purpose | Scope |
|------|---------|-------|
| `.github/copilot-instructions.md` | Project-wide coding rules | All Copilot interactions in this repo |
| `.instructions.md` (with `applyTo` frontmatter) | Scoped rules for specific files/dirs | Files matching the glob pattern |
| `.prompt.md` files (in `.github/prompts/`) | Reusable agent workflow templates | Available in the prompt picker |
| `.vscode/mcp.json` | MCP server configuration | This workspace |
| `.mcp.json` (project root) | MCP server configuration (shared) | This project, also Claude Code |

---

*Part of the [Zero to AI](../README.md) curriculum - Phase 31*
