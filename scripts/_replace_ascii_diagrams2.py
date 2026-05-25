#!/usr/bin/env python3
"""Replace the final remaining ASCII arrow diagrams with Mermaid."""
import json, re

def load(p):
    with open(p) as f: return json.load(f)
def save(p, nb):
    with open(p, 'w') as f: json.dump(nb, f, ensure_ascii=False, indent=1)
def set_src(cell, text):
    cell['source'] = text.splitlines(keepends=True)

def replace_in_cell(cell, old, new):
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    if old in src:
        set_src(cell, src.replace(old, new))
        return True
    return False

# ── 1. 02_object_detection cell 3 — three blocks ──────────────────────────────
path = "jupyter-notebooks/10-specializations/computer-vision/02_object_detection/02_object_detection.ipynb"
nb = load(path)
cell = nb['cells'][3]

OLD_RCNN = "```\nImage → CNN (entire image) → RoI Pooling → FC layers → {cls, bbox}\n          ↓\n      Feature Map\n          ↑\n    Region Proposals (Selective Search)\n```"
NEW_RCNN = """```mermaid
flowchart TD
    I([Image]) --> CNN[CNN entire image]
    CNN --> FM[Feature Map]
    I --> SS["Region Proposals\\n(Selective Search)"]
    FM --> ROI[RoI Pooling]
    SS --> ROI
    ROI --> FC[FC layers]
    FC --> OUT(["{cls, bbox}"])
```"""

OLD_YOLO = "```\nInput (640×640)\n    ↓\nCSPDarknet Backbone (feature extraction)\n    ↓\nC2f modules (faster C3)\n    ↓\nPAN-FPN Neck (multi-scale fusion)\n    ↓\nDecoupled Head (separate cls/box branches)\n    ↓\n{bbox, objectness, class} predictions\n```"
NEW_YOLO = """```mermaid
flowchart TD
    A([Input 640×640]) --> B["CSPDarknet Backbone\\nfeature extraction"]
    B --> C["C2f modules\\n(faster C3)"]
    C --> D["PAN-FPN Neck\\nmulti-scale fusion"]
    D --> E["Decoupled Head\\nseparate cls/box branches"]
    E --> F(["bbox / objectness / class"])
```"""

OLD_FPN = "```\nBottom-up: C2 → C3 → C4 → C5\n             ↓    ↓    ↓    ↓\nTop-down:   P2 ← P3 ← P4 ← P5\n```"
NEW_FPN = """```mermaid
flowchart TB
    subgraph BU["Bottom-up (backbone)"]
        C2 --> C3 --> C4 --> C5
    end
    subgraph TD["Top-down (FPN)"]
        P5 --> P4 --> P3 --> P2
    end
    C5 --> P5
    C4 --> P4
    C3 --> P3
    C2 --> P2
```"""

updated = 0
for old, new, label in [(OLD_RCNN, NEW_RCNN, "R-CNN"), (OLD_YOLO, NEW_YOLO, "YOLOv8"), (OLD_FPN, NEW_FPN, "FPN")]:
    if replace_in_cell(cell, old, new):
        print(f"UPDATED 02_object_detection {label}")
        updated += 1
if updated == 0:
    print("WARNING: no blocks matched in 02_object_detection")
save(path, nb)

# ── 2. 04_framework_validation cell 0 ─────────────────────────────────────────
path = "jupyter-notebooks/29-ai-hardware-llm-validation/04_framework_validation/04_framework_validation.ipynb"
nb = load(path)
cell = nb['cells'][0]
OLD = "```\nUser's PyTorch Code\n       ↓\nPyTorch Frontend (ATen ops)\n       ↓\nBackend Dispatch (CUDA / ROCm / XLA / Neuron / QNN)\n       ↓\nHardware-Specific Kernels\n       ↓\nGPU / NPU / TPU silicon\n```"
NEW = """```mermaid
flowchart TD
    A["User's PyTorch Code"] --> B["PyTorch Frontend\\n(ATen ops)"]
    B --> C["Backend Dispatch\\n(CUDA / ROCm / XLA / Neuron / QNN)"]
    C --> D[Hardware-Specific Kernels]
    D --> E([GPU / NPU / TPU silicon])
```"""
if replace_in_cell(cell, OLD, NEW):
    print("UPDATED 04_framework_validation cell 0")
else:
    print("WARNING: no match in 04_framework_validation")
save(path, nb)

# ── 3. 06_e2e_pipeline_validation cell 0 ──────────────────────────────────────
path = "jupyter-notebooks/29-ai-hardware-llm-validation/06_e2e_pipeline_validation/06_e2e_pipeline_validation.ipynb"
nb = load(path)
cell = nb['cells'][0]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
# Use regex since spacing may vary
m = re.search(r'```\nRaw Data[\s\S]*?```', src)
if m:
    OLD = m.group()
    NEW = """```mermaid
flowchart LR
    A([Raw Data]) --> B[Preprocessing]
    B --> C["Tokenization / Transforms"]
    C --> D[Model Inference]
    D --> E[Postprocessing]
    E --> F([Output])
    F --> G["API / UI Client"]
    H["Storage / Streaming"] -->|feed| A
    E -.->|store| H
```"""
    set_src(cell, src.replace(OLD, NEW))
    print("UPDATED 06_e2e_pipeline_validation cell 0")
else:
    print("WARNING: no match in 06_e2e_pipeline_validation")
save(path, nb)

# ── 4. 20_stylegan cell 15 ────────────────────────────────────────────────────
path = "jupyter-notebooks/24-advanced-deep-learning/20_stylegan/20_stylegan.ipynb"
nb = load(path)
cell = nb['cells'][15]
src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
m = re.search(r'```\nz \(512\)[\s\S]*?```', src)
if m:
    OLD = m.group()
    NEW = """```mermaid
flowchart TD
    Z([z 512]) --> M[Mapping Network]
    M --> W[w 512]
    W -->|"duplicate 18 times"| WS["w_1, w_2, ..., w_18"]
    subgraph SYN["Synthesis Network"]
        C0["Const 4×4×512"]
        C0 -->|"AdaIN w_1,w_2"| C1["Conv 4×4"]
        C1 -->|"AdaIN w_3,w_4"| U1["Upsample → 8×8"]
        U1 -->|"AdaIN w_5,w_6"| C2["Conv 8×8"]
        C2 -->|"... (7 more layers)"| CN["Conv 1024×1024"]
    end
    WS --> SYN
    CN --> O([RGB output])
```"""
    set_src(cell, src.replace(OLD, NEW))
    print("UPDATED 20_stylegan cell 15")
else:
    print("WARNING: no match in 20_stylegan")
save(path, nb)

print("\nDone.")
