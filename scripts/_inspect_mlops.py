#!/usr/bin/env python3
import json, re

path = "jupyter-notebooks/32-cheatsheets/ai-ml/mlops-cheatsheet/mlops-cheatsheet.ipynb"
with open(path) as f:
    nb = json.load(f)

cell = nb['cells'][1]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
print(f"cell_type: {cell['cell_type']}")
print("---source---")
print(repr(src[:2000]))
