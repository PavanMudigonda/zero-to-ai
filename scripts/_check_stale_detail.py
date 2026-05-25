#!/usr/bin/env python3
import json, re

STALE = [
    (re.compile(r'Grok 4\.20'),           'Grok 4.20 → 4.3'),
    (re.compile(r'Composer 2[^.\d5]'),    'Composer 2 → 2.5'),
    (re.compile(r'antigravity\.google/docs/get-started(?!ing)'), 'old Antigravity URL'),
    (re.compile(r'Gemini 3\.1[^. P]'),    'Gemini 3.1 missing suffix'),
    (re.compile(r'GPT-5\.3[^ C/]'),       'GPT-5.3 missing Codex suffix'),
    (re.compile(r'claude-opus-4-6\b'),    'old model slug'),
    (re.compile(r'claude-sonnet-4-6\b'),  'old model slug'),
]

FILES = [
    'jupyter-notebooks/31-ai-powered-dev-tools/03_ai_dev_tools_2026/03_ai_dev_tools_2026.ipynb',
    'jupyter-notebooks/15-ai-agents/10_autonomous_agents_2026/10_autonomous_agents_2026.ipynb',
    'jupyter-notebooks/31-ai-powered-dev-tools/02_vscode_ai_setup/02_vscode_ai_setup.ipynb',
    'jupyter-notebooks/31-ai-powered-dev-tools/04_mcp_deep_dive/04_mcp_deep_dive.ipynb',
    'jupyter-notebooks/31-ai-powered-dev-tools/05_copilot_instructions_guide/05_copilot_instructions_guide.ipynb',
    'jupyter-notebooks/31-ai-powered-dev-tools/06_copilot_workflows/06_copilot_workflows.ipynb',
    'jupyter-notebooks/31-ai-powered-dev-tools/31-ai-powered-dev-tools.ipynb',
]

for path in FILES:
    try:
        with open(path) as f:
            nb = json.load(f)
    except Exception as e:
        print(f"ERROR {path}: {e}"); continue

    found_any = False
    for ci, cell in enumerate(nb.get('cells', [])):
        src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        for pattern, note in STALE:
            m = pattern.search(src)
            if m:
                if not found_any:
                    print(f"\n{path}")
                    found_any = True
                line = next((l for l in src.splitlines() if pattern.search(l)), '')
                print(f"  cell {ci} [{note}]: {line.strip()[:100]}")

    if not found_any:
        print(f"OK  {path}")
