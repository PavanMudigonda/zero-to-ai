# VS Code + GitHub Copilot Workflows

Practical workflow patterns for real development tasks using Copilot's three modes: **completions**, **chat**, and **agent**.

---

## 1. Understanding the Three Modes

| Mode | Trigger | Best for |
|------|---------|----------|
| **Completions** | Just type — suggestions appear inline | Boilerplate, repetitive patterns, line-by-line edits |
| **Chat** | Open Copilot Chat panel (⌘⇧I) | Questions, explanations, planning, code review |
| **Agent** | @workspace in chat, or agent mode toggle | Multi-file features, refactoring, test generation, debugging |

### When to Use Each

```
Simple rename / one-liner    → Completions
"How does this function work?" → Chat
"Add auth middleware to all routes" → Agent
```

---

## 2. Feature Implementation Workflow

**Scenario:** Add a new "Parent-Child Retrieval" notebook to the RAG chapter.

### Step 1: Plan with Chat

Open Copilot Chat and ask:

```
@workspace What RAG notebooks exist in 08-rag/? What numbering scheme do they use?
I want to add a parent-child retrieval notebook.
```

Copilot scans the workspace and returns the existing notebook list and naming convention.

### Step 2: Build with Agent Mode

Switch to agent mode and describe the full task:

```
Create 08-rag/12_parent_child_retrieval.ipynb following the existing notebook
conventions in 08-rag/. The notebook should:
1. Explain parent-child retrieval with a diagram
2. Implement chunking with parent references
3. Show retrieval that expands from child chunks to parent docs
4. Compare against flat retrieval with precision and recall metrics
5. Include a summary comparison table

Use self-contained code with TF-IDF (no API keys).
Run all cells to verify they execute.
```

Agent mode will:
- Read existing notebooks to learn the conventions
- Create the notebook with proper structure
- Execute cells and fix any errors
- Report back with results

### Step 3: Review with Chat

Select the generated code and ask:

```
/explain this retrieval implementation — are there edge cases I'm missing?
```

---

## 3. Debugging Workflow

**Scenario:** Tests are failing after a refactor.

### Step 1: Get Context

```
@terminal What are the test failures?
```

Or paste the error directly into chat.

### Step 2: Fix with Agent

```
The tests in tests/api/test_users.py are failing with a 422 error.
The endpoint was recently refactored. Fix the failing tests to match
the new endpoint signatures.
```

Agent reads the test file, the route file, the schemas, and the error — then fixes the mismatch.

### Step 3: Verify

Agent mode runs the tests automatically. If they still fail, it iterates.

---

## 4. Code Review Workflow

### Quick Explanation

Select code, then:
```
/explain
```

### Targeted Review

```
@workspace Review src/services/payment.py for:
1. SQL injection risks
2. Missing error handling
3. Race conditions in the checkout flow
```

### Review a Diff

Open the Source Control panel, select changed files, and ask:

```
Review these changes. Flag any breaking changes, missing tests,
or security issues.
```

---

## 5. Test Generation Workflow

### Basic Test Generation

Select a function, then:
```
/tests
```

### Comprehensive Test Suite

Use agent mode for thorough coverage:

```
Generate tests for src/api/routes/orders.py.
Include:
- Happy path for each endpoint
- 401 unauthorized
- 422 validation errors
- 404 not found
- Edge cases (empty list, max pagination)

Use the existing conftest.py fixtures and follow the test patterns
in tests/api/test_users.py.
```

---

## 6. MCP-Connected Workflows

MCP servers give Copilot access to external tools. Here are workflows that combine Copilot with MCP.

### Database → Code Workflow

With a PostgreSQL MCP server connected:

```
@workspace Look at the database schema for the orders table.
Generate a SQLAlchemy model, Pydantic schemas, and CRUD routes
that match the actual table structure.
```

Copilot reads the live schema via MCP and generates code that matches exactly.

### Browser Testing Workflow

With the Playwright MCP server connected:

```
Navigate to http://localhost:3000/checkout and fill in the form
with test data. Take a screenshot after each step.
Then verify the order appears in the database.
```

### Documentation Workflow

With a fetch/web MCP server:

```
Fetch the API documentation from https://api.example.com/docs
and generate TypeScript types that match the response schemas.
```

---

## 7. Refactoring Workflow

### Extract and Reorganize

```
@workspace The file src/services/orders.py is 800 lines long.
Split it into:
- src/services/orders/create.py
- src/services/orders/search.py
- src/services/orders/fulfillment.py

Update all imports across the codebase. Run tests after to verify
nothing broke.
```

### Migrate a Pattern

```
@workspace Find all uses of os.getenv() in src/ and replace them
with pydantic-settings. The settings class is in src/config.py.
```

---

## 8. Documentation Workflow

### Generate Docs for Existing Code

Select a module and use:
```
/doc
```

### Generate a Full README

```
@workspace Generate a README.md for the 08-rag/ directory.
Include:
- Chapter overview
- Prerequisites
- List of all notebooks with one-line descriptions
- Suggested study order
- Link to the technique selection guide
```

---

## 9. Workflow Cheat Sheet

| Task | Mode | Example prompt |
|------|------|----------------|
| Quick fix | Completions | Just type the fix — Copilot suggests the rest |
| Explain code | Chat | `/explain` on selection |
| Find a function | Chat | `@workspace Where is the retry logic?` |
| New feature | Agent | `Add rate limiting to all /api/ routes...` |
| Fix failing tests | Agent | `@terminal Fix these test failures` |
| Generate tests | Agent | `/tests` or detailed prompt |
| Refactor | Agent | `Split this 500-line file into modules...` |
| Code review | Chat | `Review this for security issues` |
| Documentation | Chat/Agent | `/doc` or `Generate README for...` |
| Database → code | Agent + MCP | `Read the users table schema and generate models` |

---

## 10. Tips for Effective Prompts

### Be Specific

Bad: `Make this better`

Good: `Refactor this function to use async/await instead of callbacks. Keep the same function signature.`

### Provide Context

Bad: `Fix the bug`

Good: `The /api/orders endpoint returns 500 when the cart is empty. The error is in the calculate_total function.`

### Reference Files

Bad: `Update the tests`

Good: `Update tests/api/test_orders.py to cover the new discount_code parameter added in src/api/routes/orders.py`

### Iterate

Don't expect perfection on the first try. Review the output and follow up:

```
Good start, but:
1. Use the existing `create_test_order` fixture instead of inline setup
2. Add a test for the edge case where discount > total
```

---

*Previous: [03_copilot_instructions_guide.md](03_copilot_instructions_guide.md) — custom instructions for Copilot*
*Next: [05_build_mcp_server.ipynb](05_build_mcp_server.ipynb) — hands-on: build your own MCP server*
