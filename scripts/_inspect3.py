#!/usr/bin/env python3
import json, re
arrow = re.compile('[↓↑]')

for path, ci in [
    ("jupyter-notebooks/03-maths/cs229-course/course/08_learning_theory/08_learning_theory.ipynb", 0),
    ("jupyter-notebooks/03-maths/cs229-course/course/15_reinforcement_learning/15_reinforcement_learning.ipynb", 9),
]:
    with open(path) as f: nb = json.load(f)
    cell = nb['cells'][ci]
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    blocks = re.findall(r'```[\s\S]*?```', src)
    arrow_blocks = [b for b in blocks if arrow.search(b)]
    print(f"\n== {path.split('/')[-1]} cell {ci} ({cell['cell_type']}) ==")
    if arrow_blocks:
        for b in arrow_blocks:
            print(b[:600])
    else:
        lines = src.splitlines()
        hits = [j for j,l in enumerate(lines) if arrow.search(l)]
        for j in hits[:3]:
            s=max(0,j-2); e=min(len(lines),j+3)
            print('\n'.join(lines[s:e])); print("---")
