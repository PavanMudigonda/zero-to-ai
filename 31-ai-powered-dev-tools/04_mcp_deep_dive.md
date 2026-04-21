# MCP Deep Dive: Model Context Protocol

MCP is what turns a chatbot into an agent. Without MCP, your coding assistant can only read files in your workspace and run terminal commands. With MCP, it can browse the web, query databases, call APIs, manage cloud resources, and use any custom tool you build.

This guide focuses on MCP as used in **VS Code + GitHub Copilot**.

---

## 1. What MCP Actually Is

MCP (Model Context Protocol) is an **open standard** created by Anthropic that defines how AI applications connect to external data sources and tools. Think of it as USB-C for AI tools: a single protocol that any AI client (VS Code Copilot, Claude Code, Cursor, etc.) can use to connect to any MCP server. We focus on the VS Code integration here.

### The Three MCP Primitives

| Primitive | Direction | What it does | Example |
|-----------|-----------|-------------|---------|
| **Tools** | Client → Server | Actions the AI can take | `query_database`, `take_screenshot`, `create_issue` |
| **Resources** | Server → Client | Data the AI can read | Database schema, file contents, API documentation |
| **Prompts** | Server → Client | Pre-written prompt templates | "Analyze this SQL query for performance issues" |

In practice, **tools** are the most commonly used primitive. When the agent decides it needs to query a database, it calls the `query` tool on the database MCP server.

### Architecture

```
┌──────────────┐     JSON-RPC      ┌──────────────┐     Native     ┌──────────────┐
│  AI Client   │ ◄──── stdio ────► │  MCP Server  │ ◄───────────► │  Data Source  │
│  (VS Code,   │   or HTTP/SSE     │  (Python,    │   protocol    │  (Postgres,   │
│   Claude)    │                   │   Node.js)   │               │   Web, API)   │
└──────────────┘                   └──────────────┘               └──────────────┘
```

- The **client** is your AI tool (VS Code Copilot, Claude Code, etc.)
- The **server** is a lightweight process that translates between MCP and the data source's native protocol
- Communication uses **JSON-RPC 2.0** over either stdio (local) or HTTP with Server-Sent Events (remote)

---

## 2. Transport: stdio vs HTTP/SSE

### stdio (Local Servers)

The client spawns the server as a child process. Communication happens over stdin/stdout.

```json
{
  "servers": {
    "my-server": {
      "command": "python",
      "args": ["server.py"],
      "env": { "DB_URL": "postgresql://..." }
    }
  }
}
```

**Pros:** Simple, no auth needed, fast
**Cons:** Must run on the same machine as the client

### HTTP/SSE (Remote Servers)

The server runs as a web service. The client connects over HTTP.

```json
{
  "servers": {
    "remote-db": {
      "url": "https://mcp.example.com/db",
      "headers": {
        "Authorization": "Bearer ${input:apiToken}"
      }
    }
  }
}
```

**Pros:** Server can run anywhere (cloud, shared team server)
**Cons:** Requires auth, network latency, more setup

---

## 3. MCP Server Catalog

### Official Servers (by Anthropic / ModelContextProtocol org)

| Server | Package | What it does |
|--------|---------|-------------|
| **Filesystem** | `@modelcontextprotocol/server-filesystem` | Read/write files, search by glob |
| **PostgreSQL** | `@modelcontextprotocol/server-postgres` | Query, inspect schema, run SQL |
| **SQLite** | `@modelcontextprotocol/server-sqlite` | Local database access |
| **GitHub** | `@modelcontextprotocol/server-github` | Repos, issues, PRs, actions |
| **Git** | `@modelcontextprotocol/server-git` | Log, diff, blame, branch |
| **Brave Search** | `@modelcontextprotocol/server-brave-search` | Web search |
| **Memory** | `@modelcontextprotocol/server-memory` | Persistent key-value memory |
| **Fetch** | `@modelcontextprotocol/server-fetch` | HTTP requests to any URL |
| **Puppeteer** | `@modelcontextprotocol/server-puppeteer` | Browser automation |

### Community & Vendor Servers

| Server | What it does |
|--------|-------------|
| **Playwright MCP** | Browser automation, screenshots, form filling, navigation |
| **Azure MCP** | Azure resource management, deployment, monitoring |
| **Supabase MCP** | Supabase database and auth |
| **Notion MCP** | Read/write Notion pages and databases |
| **Slack MCP** | Read/send messages, search channels |
| **Linear MCP** | Issue tracking, project management |
| **Sentry MCP** | Error tracking, issue analysis |
| **Docker MCP** | Container management |

### Finding More Servers

- **Official registry:** [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- **Community list:** [mcpservers.org](https://mcpservers.org)
- **npm search:** `npx @modelcontextprotocol/server-*`
- **pip search:** `pip install mcp-server-*`

---

## 4. Configuration in Detail

### VS Code (`.vscode/mcp.json`)

```json
{
  "servers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${input:pgConnectionString}"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:githubToken}"
      }
    }
  }
}
```

The `${input:name}` syntax prompts you for the value when the server starts, so you never commit secrets.

### Project Root (`.mcp.json`)

You can also place MCP config at the project root as `.mcp.json`. This format is also recognized by other MCP-compatible tools:

```json
{
  "mcpServers": {
    "rag-server": {
      "command": "python",
      "args": ["scripts/rag_mcp_server.py"]
    }
  }
}
```

---

## 5. Security Considerations

MCP servers can execute arbitrary code. Treat them like any other dependency:

### Do

- Pin server versions in `package.json` or requirements files
- Use `${input:...}` for secrets - never hardcode tokens
- Scope filesystem servers to specific directories (not `/`)
- Review server source code before using in production
- Use read-only database credentials when possible

### Don't

- Run MCP servers as root
- Give filesystem servers access to `~/.ssh`, `~/.aws`, or credential directories
- Use MCP servers from untrusted sources without reviewing the code
- Commit `.env` files with MCP credentials

### Principle of Least Privilege

```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y", "@modelcontextprotocol/server-filesystem",
        "/Users/you/project/data"
      ]
    }
  }
}
```

This restricts the filesystem server to only the `data/` directory. The agent cannot read your SSH keys or other sensitive files.

---

## 6. Debugging MCP Servers

### VS Code

1. Open Command Palette → "MCP: List Servers" - check status
2. Open Output Panel → select "MCP" from the dropdown - see logs
3. If a server is red, click it to see the error message

### Common Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Server shows "not started" | Command not found | Verify `npx`, `python`, etc. are on PATH |
| Server starts but agent doesn't use it | Not in Agent mode | Switch from Chat to Agent mode |
| "Connection refused" for HTTP server | Server not running | Start the server process manually first |
| Tools work but are slow | Large response payloads | Limit query results, paginate |
| `ENOENT` error | Wrong path to server script | Use absolute path or verify relative path |

### Testing a Server Manually

You can test any stdio MCP server directly:

```bash
# Start the server and send a JSON-RPC request
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | \
  npx @modelcontextprotocol/server-filesystem /tmp
```

This prints the list of tools the server exposes.

---

## 7. Building Your Own MCP Server

See [07_build_mcp_server.ipynb](07_build_mcp_server.ipynb) for a hands-on walkthrough. The key steps:

1. **Install the MCP SDK:**
   ```bash
   pip install mcp
   ```

2. **Define your tools** as Python functions with type annotations
3. **Register them** with the MCP server framework
4. **Configure** the server in `.vscode/mcp.json` or `.mcp.json`
5. **Test** by starting the server and calling tools from agent mode

### When to Build a Custom Server

Build your own when:
- You need to expose an internal API or database that no existing server covers
- You want to give the agent access to your ML experiment tracker (W&B, MLflow)
- You need custom business logic (e.g., "lookup customer by account ID")
- You want to wrap a command-line tool as an MCP server

Don't build your own when:
- An existing server already does what you need (check the catalog first)
- A simple terminal command would suffice (agent mode can already run commands)

---

## 8. MCP vs. Function Calling vs. Tool Use

| Concept | What it is | Scope |
|---------|-----------|-------|
| **Function calling** | LLM API feature: model outputs structured JSON to call a function | Single API call |
| **Tool use** | Agent pattern: model decides which tool to call in a loop | Single agent |
| **MCP** | Protocol standard: any client can connect to any server | Cross-tool, cross-vendor |

MCP builds on function calling and tool use but adds:
- **Discoverability** - servers advertise their tools, resources, and prompts
- **Standardization** - same protocol works in VS Code and any MCP-compatible client
- **Composability** - connect multiple servers simultaneously

---

*Next: [05_copilot_instructions_guide.md](05_copilot_instructions_guide.md) - custom instructions for Copilot*
