#!/usr/bin/env python3
import json, os, re
arrow = re.compile('[↓↑]')
for root, dirs, files in os.walk('jupyter-notebooks'):
    dirs[:] = [d for d in dirs if d != '.ipynb_checkpoints']
    for fn in files:
        if not fn.endswith('.ipynb'):
            continue
        with open(os.path.join(root, fn)) as f:
            nb = json.load(f)
        for i, cell in enumerate(nb['cells']):
            src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
            if arrow.search(src) and '```mermaid' not in src:
                # show the matching lines
                for line in src.splitlines():
                    if arrow.search(line):
                        print(f"{os.path.join(root, fn)} cell {i}: {line.strip()[:100]}")
