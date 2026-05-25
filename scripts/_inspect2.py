#!/usr/bin/env python3
import json, re

path = "jupyter-notebooks/32-cheatsheets/ai-ml/02_mlops_cheatsheet/02_mlops_cheatsheet.ipynb"
with open(path) as f:
    nb = json.load(f)

cell = nb['cells'][1]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
print(f"cell_type: {cell['cell_type']}")
print("---")
print(repr(src[:1500]))
