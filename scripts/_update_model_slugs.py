#!/usr/bin/env python3
"""Update claude-opus-4-6 → claude-opus-4-7 across affected notebooks."""
import json

FILES = [
    'jupyter-notebooks/31-ai-powered-dev-tools/03_ai_dev_tools_2026/03_ai_dev_tools_2026.ipynb',
    'jupyter-notebooks/15-ai-agents/10_autonomous_agents_2026/10_autonomous_agents_2026.ipynb',
]

OLD = 'claude-opus-4-6'
NEW = 'claude-opus-4-7'

for path in FILES:
    with open(path) as f:
        nb = json.load(f)
    count = 0
    for cell in nb['cells']:
        src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        if OLD in src:
            new_src = src.replace(OLD, NEW)
            cell['source'] = new_src.splitlines(keepends=True)
            count += src.count(OLD)
    with open(path, 'w') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print(f"Updated {count} occurrence(s) in {path.split('/')[-1]}")

print("Done.")
