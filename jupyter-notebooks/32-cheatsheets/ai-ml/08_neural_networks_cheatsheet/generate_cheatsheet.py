"""
Neural Networks Cheat Sheet — Matplotlib Generator
Produces: neural_networks_cheatsheet.png  (same layout as the reference image)
Run:  python generate_cheatsheet.py
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.gridspec import GridSpec

# ── Palette ──────────────────────────────────────────────────────────────────
C = {
    "neuron":   "#d6eaf8",   # blue
    "activ":    "#d5f5e3",   # green
    "arch":     "#fde8d8",   # orange
    "loss":     "#fdf2e9",   # peach
    "train":    "#eaf0fb",   # lavender
    "optim":    "#fff9c4",   # yellow
    "reg":      "#fce4ec",   # pink
    "init":     "#f3e5f5",   # purple-light
    "conv":     "#e8f5e9",   # mint
    "pool":     "#e3f2fd",   # sky
    "rnn":      "#fff3e0",   # amber
    "lstm":     "#fce4ec",   # rose
    "trans":    "#ede7f6",   # deep-purple-light
    "attn":     "#e0f7fa",   # cyan
    "layers":   "#f9fbe7",   # lime
    "eval":     "#fbe9e7",   # deep-orange-light
    "best":     "#e8eaf6",   # indigo-light
    "workflow": "#e0f2f1",   # teal
    "header":   "#1a237e",   # dark navy
    "border":   "#37474f",   # dark grey
    "text":     "#212121",
    "subtext":  "#424242",
    "code":     "#1565c0",
    "formula":  "#b71c1c",
}

def section(ax, title, color, num=None):
    """Draw the coloured box + bold section title."""
    ax.set_facecolor(color)
    for sp in ax.spines.values():
        sp.set_color(C["border"]); sp.set_linewidth(1.2)
    ax.set_xticks([]); ax.set_yticks([])
    nums = ['(1)','(2)','(3)','(4)','(5)','(6)','(7)','(8)',
             '(9)','(10)','(11)','(12)','(13)','(14)','(15)','(16)']
    label = f"{nums[num-1]} {title}" if num else title
    ax.set_title(label, fontsize=8.5, fontweight="bold", color=C["header"],
                 pad=4, loc="left")

def txt(ax, x, y, s, **kw):
    kw.setdefault("fontsize", 6.8); kw.setdefault("va", "top")
    kw.setdefault("color", C["text"]); kw.setdefault("wrap", True)
    ax.text(x, y, s, transform=ax.transAxes, **kw)

def rule(ax, y, color="#bdbdbd"):
    ax.axhline(y, color=color, linewidth=0.5)

# ── Figure layout ─────────────────────────────────────────────────────────────
FIG_W, FIG_H = 22, 30
fig = plt.figure(figsize=(FIG_W, FIG_H), facecolor="white")

# Title
fig.text(0.5, 0.977, "NEURAL NETWORKS", fontsize=34, fontweight="black",
         ha="center", va="top", color=C["header"])
fig.text(0.5, 0.968, "CHEAT SHEET  ·  The Ultimate Quick Reference Guide",
         fontsize=13, ha="center", va="top", color="#455a64")
fig.text(0.5, 0.961, "FROM BASICS TO ADVANCED IN ONE SHEET",
         fontsize=9, ha="center", va="top", color="#78909c", style="italic")

# 6 rows × 4 cols grid (top title + bottom banner consume the rest)
gs = GridSpec(6, 4, figure=fig,
              top=0.955, bottom=0.075,
              left=0.01, right=0.99,
              hspace=0.38, wspace=0.18)

# ── Row 0 ────────────────────────────────────────────────────────────────────

# ① Neuron Basics
ax1 = fig.add_subplot(gs[0, 0])
section(ax1, "NEURON BASICS", C["neuron"], 1)
txt(ax1, 0.05, 0.88, "The building block", fontsize=6.5, color="#546e7a")
txt(ax1, 0.05, 0.78, "• Inputs  x₁, x₂, …, xₙ  (features)", fontsize=6.5)
txt(ax1, 0.05, 0.68, "• Weights  w₁, w₂, …, wₙ  (learned)", fontsize=6.5)
txt(ax1, 0.05, 0.58, "• Bias  b  (learned offset)", fontsize=6.5)
txt(ax1, 0.05, 0.48, "• Activation  f(·)  (non-linearity)", fontsize=6.5)
rule(ax1, 0.42)
txt(ax1, 0.05, 0.38, "y = f(Σ wᵢxᵢ + b)", fontsize=8, fontweight="bold",
    color=C["formula"])
txt(ax1, 0.05, 0.24,
    "inputs → weights → activation → output", fontsize=6.3, color="#546e7a")

# ② Activation Functions
ax2 = fig.add_subplot(gs[0, 1])
section(ax2, "ACTIVATION FUNCTIONS", C["activ"], 2)
txt(ax2, 0.05, 0.88, "Add non-linearity!", fontsize=6.5, color="#546e7a")
rows = [
    ("ReLU",      "f(x) = max(0, x)"),
    ("Sigmoid",   "f(x) = 1 / (1 + e⁻ˣ)"),
    ("Tanh",      "f(x) = tanh(x)"),
    ("Leaky ReLU","f(x) = max(αx, x)"),
    ("ELU",       "f(x) = x  if x>0 else α(eˣ−1)"),
]
y = 0.77
for name, formula in rows:
    txt(ax2, 0.05, y, f"• {name}", fontsize=6.5, fontweight="bold")
    txt(ax2, 0.38, y, formula, fontsize=6.3, color=C["formula"])
    y -= 0.135

# ③ Network Architectures
ax3 = fig.add_subplot(gs[0, 2])
section(ax3, "NETWORK ARCHITECTURES", C["arch"], 3)
txt(ax3, 0.05, 0.88, "Common types", fontsize=6.5, color="#546e7a")
archs = [
    ("MLP",         "Feedforward — fully connected layers"),
    ("CNN",         "Convolutional — spatial feature extraction"),
    ("RNN",         "Recurrent — sequential / time-series data"),
    ("Transformer", "Attention — parallel, long-range context"),
]
y = 0.77
for arch, desc in archs:
    txt(ax3, 0.05, y, arch, fontsize=7, fontweight="bold", color=C["code"])
    txt(ax3, 0.05, y - 0.09, f"  {desc}", fontsize=6.3)
    y -= 0.195

# ④ Loss Functions
ax4 = fig.add_subplot(gs[0, 3])
section(ax4, "LOSS FUNCTIONS", C["loss"], 4)
txt(ax4, 0.05, 0.90, "Measure prediction error", fontsize=6.5, color="#546e7a")
txt(ax4, 0.05, 0.81, "Regression:", fontsize=7, fontweight="bold")
txt(ax4, 0.05, 0.72, "  MSE = (1/n) Σ(yᵢ − ŷᵢ)²", fontsize=6.5, color=C["formula"])
txt(ax4, 0.05, 0.63, "  MAE = (1/n) Σ|yᵢ − ŷᵢ|", fontsize=6.5, color=C["formula"])
rule(ax4, 0.57)
txt(ax4, 0.05, 0.54, "Classification:", fontsize=7, fontweight="bold")
txt(ax4, 0.05, 0.45,
    "  Binary CE = −(y log ŷ + (1−y) log(1−ŷ))",
    fontsize=6.3, color=C["formula"])
txt(ax4, 0.05, 0.35,
    "  Multi-class CE = −Σ yₖ log(ŷₖ)",
    fontsize=6.3, color=C["formula"])
rule(ax4, 0.28)
txt(ax4, 0.05, 0.24,
    "Huber: MSE near 0, MAE for outliers",
    fontsize=6.3, color="#546e7a")

# ── Row 1 ────────────────────────────────────────────────────────────────────

# ⑤ Training Process
ax5 = fig.add_subplot(gs[1, 0])
section(ax5, "TRAINING PROCESS", C["train"], 5)
txt(ax5, 0.05, 0.88, "How networks learn", fontsize=6.5, color="#546e7a")
steps = ["1  Forward Pass — compute predictions",
         "2  Loss Calculation — compare to targets",
         "3  Backward Pass — compute gradients",
         "4  Update Weights — optimizer step",
         "5  Repeat — until convergence"]
y = 0.78
for s in steps:
    txt(ax5, 0.05, y, s, fontsize=6.5)
    y -= 0.13
rule(ax5, 0.14)
txt(ax5, 0.05, 0.10, "w ← w − α · ∇L", fontsize=8,
    fontweight="bold", color=C["formula"])

# ⑥ Optimizers
ax6 = fig.add_subplot(gs[1, 1])
section(ax6, "OPTIMIZERS", C["optim"], 6)
txt(ax6, 0.05, 0.88, "Update weights efficiently", fontsize=6.5, color="#546e7a")
opts = [
    ("SGD",       "Simple stochastic updates"),
    ("Momentum",  "Accumulates past gradients"),
    ("RMSprop",   "Adaptive per-param LR"),
    ("Adam",      "Momentum + adaptive LR"),
    ("AdamW",     "Adam + decoupled weight decay"),
]
y = 0.78
for name, desc in opts:
    txt(ax6, 0.05, y, f"▸ {name}", fontsize=6.8, fontweight="bold", color=C["code"])
    txt(ax6, 0.35, y, desc, fontsize=6.3)
    y -= 0.13
rule(ax6, 0.14)
txt(ax6, 0.05, 0.10, "Default: AdamW (lr=3e-4, wd=0.01)",
    fontsize=6.3, color="#546e7a", style="italic")

# ⑦ Regularization
ax7 = fig.add_subplot(gs[1, 2])
section(ax7, "REGULARIZATION", C["reg"], 7)
txt(ax7, 0.05, 0.88, "Prevent overfitting", fontsize=6.5, color="#546e7a")
regs = [
    ("Dropout",          "Randomly zeroes p% of neurons"),
    ("L2 / Weight Decay","λ Σw² penalty — shrinks weights"),
    ("Early Stopping",   "Stop when val loss stops improving"),
    ("Batch Norm",       "(x−μ)/√(σ²+ε) — stabilises training"),
]
y = 0.78
for name, desc in regs:
    txt(ax7, 0.05, y, f"• {name}", fontsize=6.8, fontweight="bold")
    txt(ax7, 0.05, y - 0.09, f"  {desc}", fontsize=6.3, color="#546e7a")
    y -= 0.20

# ⑧ Initialization
ax8 = fig.add_subplot(gs[1, 3])
section(ax8, "INITIALIZATION", C["init"], 8)
txt(ax8, 0.05, 0.88, "Start with good weights", fontsize=6.5, color="#546e7a")
txt(ax8, 0.05, 0.79, "Xavier / Glorot  (tanh, sigmoid):", fontsize=7, fontweight="bold")
txt(ax8, 0.05, 0.70,
    "  W ~ N(0,  2 / (nᵢₙ + nₒᵤₜ))",
    fontsize=6.5, color=C["formula"])
rule(ax8, 0.63)
txt(ax8, 0.05, 0.59, "He Initialization  (ReLU):", fontsize=7, fontweight="bold")
txt(ax8, 0.05, 0.50,
    "  W ~ N(0,  2 / nᵢₙ)",
    fontsize=6.5, color=C["formula"])
rule(ax8, 0.43)
txt(ax8, 0.05, 0.39, "Orthogonal:", fontsize=7, fontweight="bold")
txt(ax8, 0.05, 0.30,
    "  WᵀW = I  — preserves variance",
    fontsize=6.5, color=C["formula"])
rule(ax8, 0.22)
txt(ax8, 0.05, 0.17, "Bad init → vanishing / exploding gradients",
    fontsize=6.3, color="#b71c1c")

# ── Row 2 ────────────────────────────────────────────────────────────────────

# ⑨ Convolution (CNN)
ax9 = fig.add_subplot(gs[2, 0])
section(ax9, "CONVOLUTION (CNN)", C["conv"], 9)
txt(ax9, 0.05, 0.88, "Extract spatial features", fontsize=6.5, color="#546e7a")

# Draw a tiny conv diagram
for r in range(3):
    for c_ in range(3):
        rect = FancyBboxPatch((0.08 + c_*0.10, 0.54 - r*0.10), 0.09, 0.09,
                              boxstyle="round,pad=0.01",
                              fc="#bbdefb", ec="#1976d2", lw=0.7,
                              transform=ax9.transAxes, clip_on=False)
        ax9.add_patch(rect)
txt(ax9, 0.08, 0.41, "Input", fontsize=5.5, color="#546e7a")

txt(ax9, 0.42, 0.72, "✕", fontsize=14, color="#555")

for r in range(2):
    for c_ in range(2):
        rect = FancyBboxPatch((0.52 + c_*0.10, 0.58 - r*0.10), 0.09, 0.09,
                              boxstyle="round,pad=0.01",
                              fc="#c8e6c9", ec="#388e3c", lw=0.7,
                              transform=ax9.transAxes, clip_on=False)
        ax9.add_patch(rect)
txt(ax9, 0.52, 0.45, "Filter", fontsize=5.5, color="#546e7a")

txt(ax9, 0.73, 0.72, "=", fontsize=14, color="#555")
for r in range(2):
    for c_ in range(2):
        rect = FancyBboxPatch((0.80 + c_*0.08, 0.58 - r*0.08), 0.07, 0.07,
                              boxstyle="round,pad=0.01",
                              fc="#fff9c4", ec="#f9a825", lw=0.7,
                              transform=ax9.transAxes, clip_on=False)
        ax9.add_patch(rect)
txt(ax9, 0.80, 0.45, "Output", fontsize=5.5, color="#546e7a")

rule(ax9, 0.38)
txt(ax9, 0.05, 0.34,
    "Out = ⌊(W − F + 2P) / S⌋ + 1",
    fontsize=6.5, color=C["formula"])
txt(ax9, 0.05, 0.22, "• Slides filter over input", fontsize=6.3)
txt(ax9, 0.05, 0.13, "• Detects edges, textures, shapes", fontsize=6.3)
txt(ax9, 0.05, 0.04, "• Parameter sharing → fewer params", fontsize=6.3)

# ⑩ Pooling (CNN)
ax10 = fig.add_subplot(gs[2, 1])
section(ax10, "POOLING (CNN)", C["pool"], 10)
txt(ax10, 0.05, 0.88, "Downsample feature maps", fontsize=6.5, color="#546e7a")
txt(ax10, 0.05, 0.79, "Max Pooling — takes max in window:",
    fontsize=7, fontweight="bold")

# 4×4 input grid
grid_vals = [[1,3,2,4],[5,6,0,1],[2,1,3,2],[4,0,1,5]]
for r in range(4):
    for c_ in range(4):
        fc = "#bbdefb" if (r < 2 and c_ < 2) else \
             "#c8e6c9" if (r < 2 and c_ >= 2) else \
             "#fff9c4" if (r >= 2 and c_ < 2) else "#fce4ec"
        rect = FancyBboxPatch((0.05 + c_*0.11, 0.35 + (3-r)*0.10), 0.10, 0.09,
                              boxstyle="square,pad=0",
                              fc=fc, ec="#90a4ae", lw=0.5,
                              transform=ax10.transAxes)
        ax10.add_patch(rect)
        ax10.text(0.10 + c_*0.11, 0.395 + (3-r)*0.10,
                  str(grid_vals[r][c_]),
                  transform=ax10.transAxes, ha="center", va="center",
                  fontsize=6, fontweight="bold")

txt(ax10, 0.52, 0.70, "→", fontsize=14, color="#555")

mp_vals = [[6,4],[4,5]]
for r in range(2):
    for c_ in range(2):
        fc = ["#bbdefb","#c8e6c9","#fff9c4","#fce4ec"][r*2+c_]
        rect = FancyBboxPatch((0.60 + c_*0.14, 0.45 + (1-r)*0.13), 0.13, 0.12,
                              boxstyle="square,pad=0",
                              fc=fc, ec="#90a4ae", lw=0.5,
                              transform=ax10.transAxes)
        ax10.add_patch(rect)
        ax10.text(0.665 + c_*0.14, 0.52 + (1-r)*0.13,
                  str(mp_vals[r][c_]),
                  transform=ax10.transAxes, ha="center", va="center",
                  fontsize=7, fontweight="bold")

rule(ax10, 0.32)
txt(ax10, 0.05, 0.27, "Avg Pooling — takes mean in window:",
    fontsize=7, fontweight="bold")
txt(ax10, 0.05, 0.17,
    "  Same as above but mean instead of max",
    fontsize=6.3, color="#546e7a")
txt(ax10, 0.05, 0.07,
    "  Reduces spatial size, keeps channel count",
    fontsize=6.3, color="#546e7a")

# ⑪ Recurrent Neural Network
ax11 = fig.add_subplot(gs[2, 2])
section(ax11, "RECURRENT NN (RNN)", C["rnn"], 11)
txt(ax11, 0.05, 0.88, "Handle sequential data", fontsize=6.5, color="#546e7a")
txt(ax11, 0.05, 0.79, "Unrolled over time:", fontsize=6.5)

# Draw unrolled RNN boxes
for i, label in enumerate(["h₀","h₁","h₂","…","hₜ"]):
    x = 0.05 + i * 0.19
    if label != "…":
        rect = FancyBboxPatch((x, 0.50), 0.13, 0.18,
                              boxstyle="round,pad=0.02",
                              fc="#fff3e0", ec="#ef6c00", lw=1,
                              transform=ax11.transAxes)
        ax11.add_patch(rect)
        ax11.text(x + 0.065, 0.59, label, transform=ax11.transAxes,
                  ha="center", va="center", fontsize=6.5, fontweight="bold")
        ax11.text(x + 0.065, 0.46, f"x{i if i<4 else 't'}",
                  transform=ax11.transAxes, ha="center", fontsize=6,
                  color="#546e7a")
    else:
        ax11.text(x + 0.03, 0.59, "…", transform=ax11.transAxes,
                  fontsize=14, va="center")
    if i < 4 and label != "…":
        ax11.annotate("", xy=(x+0.19, 0.59), xytext=(x+0.13, 0.59),
                      xycoords="axes fraction", textcoords="axes fraction",
                      arrowprops=dict(arrowstyle="->", color="#ef6c00", lw=1))

rule(ax11, 0.40)
txt(ax11, 0.05, 0.36,
    "hₜ = tanh(Wₕhₜ₋₁ + Wₓxₜ + b)",
    fontsize=7, color=C["formula"])
txt(ax11, 0.05, 0.26,
    "⚠ Vanishing gradient over long sequences",
    fontsize=6.3, color="#b71c1c")
txt(ax11, 0.05, 0.16, "• Time series, speech, NLP", fontsize=6.3)
txt(ax11, 0.05, 0.07, "• Solved by LSTM / GRU / Transformer", fontsize=6.3)

# ⑫ LSTM
ax12 = fig.add_subplot(gs[2, 3])
section(ax12, "LONG SHORT-TERM MEMORY", C["lstm"], 12)
txt(ax12, 0.05, 0.88, "Remember long-term info", fontsize=6.5, color="#546e7a")
gates = [
    ("Forget gate  fₜ",  "σ(Wf·[hₜ₋₁,xₜ]+bf)", "Keep/discard cell state"),
    ("Input gate   iₜ",  "σ(Wᵢ·[hₜ₋₁,xₜ]+bᵢ)", "What new info to write"),
    ("Cell cand.   c̃ₜ",  "tanh(Wc·[hₜ₋₁,xₜ]+bc)", "Candidate cell values"),
    ("Output gate  oₜ",  "σ(Wo·[hₜ₋₁,xₜ]+bo)", "What to expose as hₜ"),
]
y = 0.79
for name, eq, desc in gates:
    txt(ax12, 0.05, y, name, fontsize=6.3, fontweight="bold", color=C["code"])
    txt(ax12, 0.05, y-0.08, f"  {eq}", fontsize=5.8, color=C["formula"])
    y -= 0.17
rule(ax12, 0.11)
txt(ax12, 0.05, 0.07,
    "cₜ = fₜ⊙cₜ₋₁ + iₜ⊙c̃ₜ   hₜ = oₜ⊙tanh(cₜ)",
    fontsize=6.5, color=C["formula"])

# ── Row 3 ────────────────────────────────────────────────────────────────────

# ⑬ Transformer Architecture
ax13 = fig.add_subplot(gs[3, 0])
section(ax13, "TRANSFORMER ARCHITECTURE", C["trans"], 13)
txt(ax13, 0.05, 0.88, "Powerful for sequence modelling", fontsize=6.5, color="#546e7a")

for label, x, col in [("ENCODER",0.05,"#3f51b5"),("DECODER",0.52,"#7b1fa2")]:
    rect = FancyBboxPatch((x, 0.28), 0.40, 0.52,
                          boxstyle="round,pad=0.02",
                          fc="white", ec=col, lw=1.5,
                          transform=ax13.transAxes)
    ax13.add_patch(rect)
    ax13.text(x+0.20, 0.77, label, transform=ax13.transAxes, ha="center",
              fontsize=6.5, fontweight="bold", color=col)
    for i, sub in enumerate(["Multi-Head Self-Attn", "Feed Forward", "+ Residual/LN"]):
        ry = 0.60 - i * 0.115
        srect = FancyBboxPatch((x+0.03, ry), 0.34, 0.09,
                               boxstyle="round,pad=0.01",
                               fc="#e8eaf6", ec=col, lw=0.8,
                               transform=ax13.transAxes)
        ax13.add_patch(srect)
        ax13.text(x+0.20, ry+0.045, sub, transform=ax13.transAxes,
                  ha="center", va="center", fontsize=5.2)

ax13.annotate("", xy=(0.52, 0.52), xytext=(0.45, 0.52),
              xycoords="axes fraction", textcoords="axes fraction",
              arrowprops=dict(arrowstyle="->", color="#555", lw=1))

rule(ax13, 0.26)
txt(ax13, 0.05, 0.22, "• Positional Encoding added to embeddings", fontsize=6.3)
txt(ax13, 0.05, 0.14, "• Parallelisable — no sequential bottleneck", fontsize=6.3)
txt(ax13, 0.05, 0.06, "• Powers BERT, GPT, T5, ViT …", fontsize=6.3)

# ⑭ Attention Mechanism
ax14 = fig.add_subplot(gs[3, 1])
section(ax14, "ATTENTION MECHANISM", C["attn"], 14)
txt(ax14, 0.05, 0.88, "Focus on relevant parts", fontsize=6.5, color="#546e7a")

for label, x, col in [("Query\nQ",0.08,"#0288d1"),
                       ("Key\nK",0.38,"#00838f"),
                       ("Value\nV",0.68,"#2e7d32")]:
    rect = FancyBboxPatch((x, 0.55), 0.22, 0.25,
                          boxstyle="round,pad=0.02",
                          fc="white", ec=col, lw=1.2,
                          transform=ax14.transAxes)
    ax14.add_patch(rect)
    ax14.text(x+0.11, 0.675, label, transform=ax14.transAxes, ha="center",
              fontsize=7, fontweight="bold", color=col)

rule(ax14, 0.50)
txt(ax14, 0.05, 0.46,
    "Attention(Q,K,V) = softmax(QKᵀ / √dₖ) V",
    fontsize=7, color=C["formula"], fontweight="bold")
rule(ax14, 0.38)
txt(ax14, 0.05, 0.33, "Multi-Head: run h parallel attention heads,", fontsize=6.3)
txt(ax14, 0.05, 0.25, "  concatenate and project outputs.", fontsize=6.3)
rule(ax14, 0.18)
txt(ax14, 0.05, 0.13, "Causal (masked): decoder prevents", fontsize=6.3)
txt(ax14, 0.05, 0.05, "  attending to future tokens.", fontsize=6.3)

# ⑮ Common Layers
ax15 = fig.add_subplot(gs[3, 2])
section(ax15, "COMMON LAYERS", C["layers"], 15)
txt(ax15, 0.05, 0.88, "Building blocks", fontsize=6.5, color="#546e7a")
layers_info = [
    ("Dense / Linear",    "nn.Linear(in, out)"),
    ("Conv2D",            "nn.Conv2d(in_ch, out_ch, k)"),
    ("MaxPooling2D",      "nn.MaxPool2d(kernel)"),
    ("BatchNormalization","nn.BatchNorm1d / 2d(features)"),
    ("Dropout",           "nn.Dropout(p=0.5)"),
    ("Embedding",         "nn.Embedding(vocab, dim)"),
]
y = 0.79
for name, api in layers_info:
    txt(ax15, 0.05, y, f"• {name}", fontsize=6.3, fontweight="bold")
    txt(ax15, 0.05, y-0.08, f"  {api}", fontsize=5.8, color=C["code"])
    y -= 0.16

# ⑯ Evaluation Metrics
ax16 = fig.add_subplot(gs[3, 3])
section(ax16, "EVALUATION METRICS", C["eval"], 16)
txt(ax16, 0.05, 0.88, "Measure performance", fontsize=6.5, color="#546e7a")
txt(ax16, 0.05, 0.80, "Classification:", fontsize=7, fontweight="bold")
cls_metrics = [
    "Accuracy  = correct / total",
    "Precision = TP / (TP+FP)",
    "Recall    = TP / (TP+FN)",
    "F1        = 2·P·R / (P+R)",
    "ROC-AUC   = area under ROC curve",
]
y = 0.72
for m in cls_metrics:
    txt(ax16, 0.07, y, m, fontsize=6.3, color=C["formula"])
    y -= 0.10
rule(ax16, 0.22)
txt(ax16, 0.05, 0.19, "Regression:", fontsize=7, fontweight="bold")
for m in ["MAE  = (1/n)Σ|yᵢ−ŷᵢ|",
          "RMSE = √MSE",
          "R²   = 1 − SSres/SStot"]:
    txt(ax16, 0.07, y, m, fontsize=6.3, color=C["formula"])
    y -= 0.10

# ── Row 4 ────────────────────────────────────────────────────────────────────

# Best Practices (wide — spans 2 cols)
ax_bp = fig.add_subplot(gs[4, :2])
section(ax_bp, "BEST PRACTICES", C["best"])
practices = [
    ("[1] Normalise Data",     "Zero-mean / unit-std inputs -> stable gradients"),
    ("[2] Start Simple",       "Overfit one batch first; then regularise"),
    ("[3] Monitor Val Loss",   "Diverging train/val = overfitting"),
    ("[4] Use Callbacks",      "Early stopping, LR scheduler, checkpointing"),
    ("[5] Save & Version",     "torch.save(model.state_dict(), path)"),
    ("[6] Reproduce",          "Set all random seeds; log experiments"),
]
y = 0.82
for i, (title, desc) in enumerate(practices):
    col = 0 if i < 3 else 0.5
    row = i if i < 3 else i - 3
    txt(ax_bp, col+0.02, y - row*0.22,
        title, fontsize=6.8, fontweight="bold")
    txt(ax_bp, col+0.02, y - row*0.22 - 0.10,
        f"  {desc}", fontsize=6.3, color="#546e7a")

txt(ax_bp, 0.02, 0.08,
    "KEY TIPS: Understand the problem · Visualise data · Iterate fast",
    fontsize=6.5, color="#b71c1c", fontweight="bold")

# Common Workflow (wide — spans 2 cols)
ax_wf = fig.add_subplot(gs[4, 2:])
section(ax_wf, "COMMON WORKFLOW", C["workflow"])

steps_wf = ["Data", "Preprocess", "Model", "Train", "Evaluate", "Deploy"]
colors_wf = ["#1e88e5","#43a047","#8e24aa","#fb8c00","#e53935","#00897b"]
x_pos = [0.07, 0.22, 0.37, 0.52, 0.67, 0.82]

for x, label, col in zip(x_pos, steps_wf, colors_wf):
    circle = plt.Circle((x, 0.55), 0.055, color=col,
                         transform=ax_wf.transAxes, zorder=3)
    ax_wf.add_patch(circle)
    ax_wf.text(x, 0.55, label[:4], transform=ax_wf.transAxes,
               ha="center", va="center", fontsize=5.5,
               color="white", fontweight="bold", zorder=4)
    ax_wf.text(x, 0.30, label, transform=ax_wf.transAxes,
               ha="center", va="center", fontsize=6.3,
               color=col, fontweight="bold")

for i in range(len(x_pos)-1):
    ax_wf.annotate("", xy=(x_pos[i+1]-0.055, 0.55),
                   xytext=(x_pos[i]+0.055, 0.55),
                   xycoords="axes fraction", textcoords="axes fraction",
                   arrowprops=dict(arrowstyle="->", color="#37474f", lw=1.5))

rule(ax_wf, 0.18)
workflow_details = [
    "Data: collect, label, split (train/val/test)",
    "Preprocess: normalise, augment, batch",
    "Model: choose architecture, loss, optimiser",
    "Train: forward → loss → backward → step",
    "Evaluate: metrics on held-out test set",
    "Deploy: export (ONNX / TorchScript), serve",
]
txt(ax_wf, 0.02, 0.14,
    "   ·   ".join(workflow_details[:3]),
    fontsize=5.8, color="#546e7a")
txt(ax_wf, 0.02, 0.06,
    "   ·   ".join(workflow_details[3:]),
    fontsize=5.8, color="#546e7a")

# ── Row 5 — bottom banner ────────────────────────────────────────────────────
ax_bot = fig.add_subplot(gs[5, :])
ax_bot.set_facecolor("#1a237e")
for sp in ax_bot.spines.values(): sp.set_visible(False)
ax_bot.set_xticks([]); ax_bot.set_yticks([])
ax_bot.text(0.5, 0.65,
            "PRACTICE + PATIENCE = MASTERY",
            transform=ax_bot.transAxes, ha="center", va="center",
            fontsize=14, fontweight="black", color="white")
ax_bot.text(0.5, 0.25,
            "Neural networks are powerful, but YOU make them intelligent.  "
            "Good data → Good model → Great results.",
            transform=ax_bot.transAxes, ha="center", va="center",
            fontsize=9, color="#90caf9")

# ── Save ──────────────────────────────────────────────────────────────────────
out = "neural_networks_cheatsheet.png"
fig.savefig(out, dpi=180, bbox_inches="tight", facecolor="white")
print(f"✅  Saved → {out}")
plt.close(fig)
