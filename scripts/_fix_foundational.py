#!/usr/bin/env python3
import json, re

def load(p):
    with open(p) as f: return json.load(f)
def save(p, nb):
    with open(p, 'w') as f: json.dump(nb, f, ensure_ascii=False, indent=1)

arrow = re.compile('[↓↑│▼]')

# ── 1. 11_markov_models_hmm cell 5 ─────────────────────────────────────────────
path = "jupyter-notebooks/03-maths/foundational/11_markov_models_hmm/11_markov_models_hmm.ipynb"
nb = load(path)
cell = nb['cells'][5]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
blocks = re.findall(r'```[\s\S]*?```', src)
ab = [b for b in blocks if arrow.search(b)]
if ab:
    NEW = """```mermaid
flowchart LR
    subgraph H["Hidden States"]
        Z1["Z₁"] --> Z2["Z₂"] --> Z3["Z₃"] --> Zn["... Zₙ"]
    end
    Z1 --> X1["X₁"]
    Z2 --> X2["X₂"]
    Z3 --> X3["X₃"]
    Zn --> Xn["Xₙ"]
    subgraph O["Observations"]
        X1; X2; X3; Xn
    end
```"""
    cell['source'] = src.replace(ab[0], NEW).splitlines(keepends=True)
    print("UPDATED 11_markov_models_hmm cell 5")
else:
    print("NO MATCH 11_markov_models_hmm cell 5")
save(path, nb)

# ── 2. 10_ai_foundations_control_theory cell 6 ─────────────────────────────────
path = "jupyter-notebooks/03-maths/foundational/10_ai_foundations_control_theory/10_ai_foundations_control_theory.ipynb"
nb = load(path)
cell = nb['cells'][6]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
blocks = re.findall(r'```[\s\S]*?```', src)
ab = [b for b in blocks if arrow.search(b)]
if ab:
    NEW = """```mermaid
flowchart LR
    G(["Goal (setpoint)"]) --> C[Controller]
    C --> P["System / Plant"]
    P --> O([Output])
    O --> SN[Sensor]
    SN -.->|"Error (Feedback)"| C
```"""
    cell['source'] = src.replace(ab[0], NEW).splitlines(keepends=True)
    print("UPDATED 10_ai_foundations_control_theory cell 6")
else:
    print("NO MATCH 10_ai_foundations_control_theory cell 6")
save(path, nb)

print("Done.")
