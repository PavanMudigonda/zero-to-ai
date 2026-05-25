#!/usr/bin/env python3
import json, re

def load(p):
    with open(p) as f: return json.load(f)
def save(p, nb):
    with open(p, 'w') as f: json.dump(nb, f, ensure_ascii=False, indent=1)

arrow = re.compile('[↓↑]')

# ── 1. 08_learning_theory cell 0 ───────────────────────────────────────────────
path = "jupyter-notebooks/03-maths/cs229-course/course/08_learning_theory/08_learning_theory.ipynb"
nb = load(path)
cell = nb['cells'][0]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
blocks = re.findall(r'```[\s\S]*?```', src)
arrow_blocks = [b for b in blocks if arrow.search(b)]
if arrow_blocks:
    NEW = """```mermaid
flowchart TD
    S["Training Set S\n{(x⁽¹⁾,y⁽¹⁾), ..., (x⁽ᵐ⁾,y⁽ᵐ⁾)}"] --> A["Learning Algorithm A\n(deterministic)"]
    A --> H["Hypothesis ĥ (or θ̂)"]
```"""
    cell['source'] = src.replace(arrow_blocks[0], NEW).splitlines(keepends=True)
    print("UPDATED 08_learning_theory cell 0")
else:
    print("NO MATCH 08_learning_theory cell 0")
save(path, nb)

# ── 2. 15_reinforcement_learning cell 9 — two blocks ───────────────────────────
path = "jupyter-notebooks/03-maths/cs229-course/course/15_reinforcement_learning/15_reinforcement_learning.ipynb"
nb = load(path)
cell = nb['cells'][9]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
blocks = re.findall(r'```[\s\S]*?```', src)
arrow_blocks = [b for b in blocks if arrow.search(b)]

NEW_DUEL = """```mermaid
flowchart TD
    IS([Input state s]) --> SL["CNN/FC layers (shared)"]
    SL --> VS["V(s)"]
    SL --> A1["A(s,a₁)"]
    SL --> A2["A(s,a₂) ..."]
    VS & A1 & A2 --> Q["Q(s,a) = V + (A - mean(A))"]
```"""

NEW_CNN = """```mermaid
flowchart TD
    I(["Input: 84×84×4 (stacked frames)"]) --> C1["Conv1: 32 filters, 8×8, stride 4, ReLU"]
    C1 --> C2["Conv2: 64 filters, 4×4, stride 2, ReLU"]
    C2 --> C3["Conv3: 64 filters, 3×3, stride 1, ReLU"]
    C3 --> FC["Flatten → FC: 512 units, ReLU"]
    FC --> O(["Output: |A| Q-values (linear)"])
```"""

news = [NEW_DUEL, NEW_CNN]
for old, new in zip(arrow_blocks, news):
    src = src.replace(old, new)
if arrow_blocks:
    cell['source'] = src.splitlines(keepends=True)
    print(f"UPDATED 15_reinforcement_learning cell 9 ({len(arrow_blocks)} blocks)")
else:
    print("NO MATCH 15_reinforcement_learning cell 9")
save(path, nb)

print("\nDone.")
