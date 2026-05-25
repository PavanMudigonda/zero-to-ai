#!/usr/bin/env python3
import json

# Fix 1: cell 11 of 13_agentic_coding_ides — stale URL in Resources section
PATH1 = "jupyter-notebooks/15-ai-agents/13_agentic_coding_ides/13_agentic_coding_ides.ipynb"
with open(PATH1) as f:
    nb1 = json.load(f)
cell = nb1['cells'][11]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
if 'antigravity.google/docs/get-started' in src:
    src = src.replace('antigravity.google/docs/get-started', 'antigravity.google/docs/getting-started')
    cell['source'] = src.splitlines(keepends=True)
    print("FIXED 13_agentic_coding_ides cell 11 URL")
with open(PATH1, 'w') as f:
    json.dump(nb1, f, ensure_ascii=False, indent=1)

# Fix 2: 09_reasoning_models cell 29 — Grok 4.20 → Grok 4.3
PATH2 = "jupyter-notebooks/15-ai-agents/09_reasoning_models/09_reasoning_models.ipynb"
with open(PATH2) as f:
    nb2 = json.load(f)
cell = nb2['cells'][29]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
if 'Grok 4.20' in src:
    src = src.replace('Grok 4.20', 'Grok 4.3')
    cell['source'] = src.splitlines(keepends=True)
    print("FIXED 09_reasoning_models cell 29: Grok 4.20 → Grok 4.3")
with open(PATH2, 'w') as f:
    json.dump(nb2, f, ensure_ascii=False, indent=1)

print("Done.")
