#!/usr/bin/env python3
"""Replace the remaining ASCII arrow diagrams in mlops notebooks + cheatsheet."""
import json, re

def load(p):
    with open(p) as f: return json.load(f)
def save(p, nb):
    with open(p, 'w') as f: json.dump(nb, f, ensure_ascii=False, indent=1)

arrow = re.compile('[↓↑│]')


def replace_block(cell, old, new):
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    if old in src:
        cell['source'] = src.replace(old, new).splitlines(keepends=True)
        return True
    # try regex fallback using first non-backtick line
    first_line = old[4:old.index('\n', 4)]
    m = re.search(r'```\n' + re.escape(first_line) + r'[\s\S]*?```', src)
    if m:
        cell['source'] = src.replace(m.group(), new).splitlines(keepends=True)
        return True
    return False


# ── 1. 04_model_deployment cell 0 — Blue/Green ─────────────────────────────────
path = "jupyter-notebooks/09-mlops/04_model_deployment/04_model_deployment.ipynb"
nb = load(path)
cell = nb['cells'][0]
blocks = re.findall(r'```[\s\S]*?```', ''.join(cell['source']) if isinstance(cell['source'],list) else cell['source'])
arrow_blocks = [b for b in blocks if arrow.search(b)]
if arrow_blocks:
    NEW = """```mermaid
flowchart LR
    BL["Blue (v1)"] --> LB[Load Balancer]
    GR["Green (v2)"] --> LB
    LB --> U([Users])
    LB -.->|switch traffic| GR
```"""
    if replace_block(cell, arrow_blocks[0], NEW):
        print("UPDATED 04_model_deployment cell 0")
    else:
        print("NO MATCH 04_model_deployment cell 0")
else:
    print("NO ARROW BLOCKS in 04_model_deployment cell 0")
save(path, nb)


# ── 2. 07_ci_cd_pipeline cell 1 ────────────────────────────────────────────────
path = "jupyter-notebooks/09-mlops/07_ci_cd_pipeline/07_ci_cd_pipeline.ipynb"
nb = load(path)
cell = nb['cells'][1]
blocks = re.findall(r'```[\s\S]*?```', ''.join(cell['source']) if isinstance(cell['source'],list) else cell['source'])
arrow_blocks = [b for b in blocks if arrow.search(b)]
if arrow_blocks:
    NEW = """```mermaid
flowchart LR
    CC["Code Change\\nLinting, Type Check"] --> TE["Test\\nUnit, Data Validation"]
    TE --> TR["Train\\nModel Validation, Schema"]
    TR --> EV["Evaluate\\nMetrics, A/B Test"]
    EV --> DP["Deploy\\nRegistry, Version, Package"]
    DP --> MO["Monitor\\nAlerts, Dashboard"]
```"""
    if replace_block(cell, arrow_blocks[0], NEW):
        print("UPDATED 07_ci_cd_pipeline cell 1")
    else:
        print("NO MATCH 07_ci_cd_pipeline cell 1")
else:
    print("NO ARROW BLOCKS in 07_ci_cd_pipeline cell 1")
save(path, nb)


# ── 3. 01_START_HERE (mlops) cell 1 — ML Lifecycle ─────────────────────────────
path = "jupyter-notebooks/09-mlops/01_START_HERE/01_START_HERE.ipynb"
nb = load(path)
cell = nb['cells'][1]
blocks = re.findall(r'```[\s\S]*?```', ''.join(cell['source']) if isinstance(cell['source'],list) else cell['source'])
arrow_blocks = [b for b in blocks if arrow.search(b)]
if arrow_blocks:
    NEW = """```mermaid
flowchart LR
    D([Data]) --> EXP[Experiment]
    EXP --> TR[Train]
    TR --> EV[Evaluate]
    EV --> DP[Deploy]
    DP --> MO["Monitor & Retrain"]
    MO -.->|feedback| D
```"""
    if replace_block(cell, arrow_blocks[0], NEW):
        print("UPDATED 01_START_HERE (mlops) cell 1")
    else:
        print("NO MATCH 01_START_HERE (mlops) cell 1")
else:
    print("NO ARROW BLOCKS in 01_START_HERE (mlops) cell 1")
save(path, nb)


# ── 4. mlops-cheatsheet cell 1 (code → markdown) ───────────────────────────────
path = "jupyter-notebooks/32-cheatsheets/ai-ml/mlops-cheatsheet/mlops-cheatsheet.ipynb"
nb = load(path)
cell = nb['cells'][1]
# This is a plain-text code cell — convert to markdown
NEW_SRC = """## MLOps Pipeline

```mermaid
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
```
"""
cell['cell_type'] = 'markdown'
cell['source'] = NEW_SRC.splitlines(keepends=True)
if 'outputs' in cell:
    del cell['outputs']
if 'execution_count' in cell:
    del cell['execution_count']
print("UPDATED mlops-cheatsheet cell 1 (code→markdown)")
save(path, nb)

print("\nDone.")
