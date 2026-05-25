#!/usr/bin/env python3
import json, re

path = "jupyter-notebooks/06-neural-networks/06_attention_mechanism/06_attention_mechanism.ipynb"
with open(path) as f:
    nb = json.load(f)

cell = nb['cells'][1]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']

blocks = re.findall(r'```[\s\S]*?```', src)
arrow_blocks = [(i, b) for i, b in enumerate(blocks) if any(c in b for c in ['↓','↑','↘','↙'])]

NEW_RNN = """```mermaid
flowchart TD
    T[The] --> H1; C[cat] --> H2; S[sat] --> H3
    O[on]  --> H4; TH[the] --> H5; M[mat] --> H6
    H1 --> H2 --> H3 --> H4 --> H5 --> H6
    H6 --> BN(["Bottleneck! (Final hidden state)"])
```"""

NEW_ATT = """```mermaid
flowchart TD
    T[The] --> H1; C[cat] --> H2; S[sat] --> H3
    O[on]  --> H4; TH[the] --> H5; M[mat] --> H6
    H1 & H2 & H3 & H4 & H5 & H6 --> ATT[Attention]
    ATT --> WS(["Weighted sum of ALL inputs!"])
```"""

news = [NEW_RNN, NEW_ATT]
for (i, old), new in zip(arrow_blocks, news):
    src = src.replace(old, new)
    print(f"Replaced block {i}")

cell['source'] = src.splitlines(keepends=True)
with open(path, 'w') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)
print("Saved.")
