#!/usr/bin/env python3
"""Scan all notebooks for ASCII v-arrow and branch-arrow diagram patterns."""
import json, os, re

v_arrow = re.compile(r'^\s{2,}\bv\b\s*$', re.MULTILINE)
branch  = re.compile(r'\+--+>')

results = []
for root, dirs, files in os.walk('jupyter-notebooks'):
    dirs[:] = [d for d in dirs if d != '.ipynb_checkpoints']
    for fn in files:
        if not fn.endswith('.ipynb'):
            continue
        path = os.path.join(root, fn)
        try:
            with open(path) as f:
                nb = json.load(f)
        except Exception:
            continue
        for i, cell in enumerate(nb['cells']):
            src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
            if v_arrow.search(src) or branch.search(src):
                lines = src.splitlines()
                hits = [j for j, l in enumerate(lines) if v_arrow.match(l) or branch.search(l)]
                snippet_start = max(0, hits[0] - 3)
                snippet_end   = min(len(lines), hits[-1] + 4)
                snippet = '\n'.join(lines[snippet_start:snippet_end])
                results.append((path, i, cell['cell_type'], snippet))

for path, i, ct, snippet in results:
    print(f"\n{'='*60}")
    print(f"  {path}  cell {i} ({ct})")
    print(snippet)

print(f"\nTotal: {len(results)} cell(s)")
