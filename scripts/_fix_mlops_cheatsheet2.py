#!/usr/bin/env python3
import json, re

path = "jupyter-notebooks/32-cheatsheets/ai-ml/02_mlops_cheatsheet/02_mlops_cheatsheet.ipynb"
with open(path) as f:
    nb = json.load(f)

cell = nb['cells'][1]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']

# Find the fenced code block with arrows
blocks = re.findall(r'```[\s\S]*?```', src)
arrow_blocks = [b for b in blocks if '↓' in b or '↑' in b]

NEW = """```mermaid
flowchart TD
    DC[Data Collection] --> DV[Data Validation]
    DV --> FE[Feature Engineering]
    FE --> MT[Model Training]
    DC --> DVR[Data Versioning]
    MT --> ET[Experiment Tracking]
    ET --> ME[Model Evaluation]
    ME --> MR[Model Registry]
    MR --> MD[Model Deployment]
    MD --> MM[Model Monitoring]
    MM --> RT([Retrain])
    RT -.->|loop back| DC
```"""

if arrow_blocks:
    new_src = src.replace(arrow_blocks[0], NEW)
    cell['source'] = new_src.splitlines(keepends=True)
    with open(path, 'w') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print("UPDATED 02_mlops_cheatsheet cell 1")
else:
    print("NO MATCH")
