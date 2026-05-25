"""
Course-wide Cheat Sheet Generator
Generates one PNG per major course module using Matplotlib.
Run from any directory:
    python generate_all_cheatsheets.py
All PNGs are written to:
    jupyter-notebooks/32-cheatsheets/ai-ml/<module>_cheatsheet/<module>_cheatsheet.png
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.gridspec import GridSpec

# ── Repo root (two levels up from this file) ─────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# SCRIPT_DIR is already  …/jupyter-notebooks/32-cheatsheets/ai-ml
OUT_BASE    = SCRIPT_DIR

# ── Shared drawing helpers ────────────────────────────────────────────────────
PALETTE = {
    "h1": "#1a237e", "h2": "#283593", "border": "#37474f",
    "text": "#212121", "sub": "#546e7a", "code": "#1565c0",
    "formula": "#b71c1c", "warn": "#e65100",
    # section bg colours
    "blue":   "#d6eaf8", "green":  "#d5f5e3", "orange": "#fde8d8",
    "peach":  "#fdf2e9", "lav":    "#eaf0fb", "yellow": "#fff9c4",
    "pink":   "#fce4ec", "purple": "#f3e5f5", "mint":   "#e8f5e9",
    "sky":    "#e3f2fd", "amber":  "#fff3e0", "rose":   "#fce4ec",
    "indigo": "#e8eaf6", "cyan":   "#e0f7fa", "lime":   "#f9fbe7",
    "teal":   "#e0f2f1", "navy":   "#1a237e", "white":  "#ffffff",
}

def make_fig(nrows, ncols, title, subtitle="",
             w=22, h_per_row=4.8, top_pad=0.055):
    h = nrows * h_per_row + 1.2
    fig = plt.figure(figsize=(w, h), facecolor="white")
    fig.text(0.5, 1 - 0.012,  title,    fontsize=28, fontweight="black",
             ha="center", va="top", color=PALETTE["h1"])
    fig.text(0.5, 1 - 0.038, subtitle,  fontsize=11, ha="center", va="top",
             color="#455a64")
    gs = GridSpec(nrows, ncols, figure=fig,
                  top=1 - top_pad, bottom=0.04,
                  left=0.01, right=0.99,
                  hspace=0.42, wspace=0.18)
    return fig, gs

def section_ax(ax, title, bg, title_size=8.5):
    ax.set_facecolor(bg)
    for sp in ax.spines.values():
        sp.set_color(PALETTE["border"]); sp.set_linewidth(1.1)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(title, fontsize=title_size, fontweight="bold",
                 color=PALETTE["h1"], pad=4, loc="left")

def t(ax, x, y, s, size=6.8, color=None, bold=False, italic=False, **kw):
    style = "italic" if italic else "normal"
    weight = "bold" if bold else "normal"
    ax.text(x, y, s, transform=ax.transAxes,
            fontsize=size, color=color or PALETTE["text"],
            fontweight=weight, fontstyle=style, va="top", **kw)

def rule(ax, y, c="#bdbdbd", lw=0.5):
    ax.axhline(y, color=c, linewidth=lw)

def bullet(ax, items, start_y=0.88, dy=0.12, indent=0.05,
           key_color=None, val_sep=None, size=6.5):
    y = start_y
    for item in items:
        if isinstance(item, tuple) and val_sep is not None:
            key, val = item
            t(ax, indent, y, key, size=size, bold=True,
              color=key_color or PALETTE["code"])
            t(ax, indent + val_sep, y, val, size=size-0.3)
        elif isinstance(item, tuple):
            key, val = item
            t(ax, indent, y, f"* {key}", size=size, bold=True)
            t(ax, indent, y - dy*0.65, f"  {val}", size=size-0.3,
              color=PALETTE["sub"])
            y -= dy * 1.5
            continue
        else:
            t(ax, indent, y, item, size=size)
        y -= dy

def save(fig, name, dpi=160):
    out_dir = os.path.join(OUT_BASE, f"{name}_cheatsheet")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{name}_cheatsheet.png")
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  saved -> {path}")

def banner(fig, msg, sub=""):
    """Dark footer banner."""
    ax = fig.add_axes([0, 0, 1, 0.032])
    ax.set_facecolor(PALETTE["navy"])
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.text(0.5, 0.65, msg,  ha="center", va="center",
            fontsize=10, fontweight="black", color="white",
            transform=ax.transAxes)
    if sub:
        ax.text(0.5, 0.20, sub, ha="center", va="center",
                fontsize=7, color="#90caf9", transform=ax.transAxes)


# ════════════════════════════════════════════════════════════════════════════
# 1. PYTHON BASICS
# ════════════════════════════════════════════════════════════════════════════
def gen_python():
    print("Generating: python_basics ...")
    fig, gs = make_fig(3, 4, "PYTHON BASICS CHEAT SHEET",
                       "Core language reference for AI/ML development")

    sections = [
        # row 0
        ("Data Types", PALETTE["blue"],
         [("int / float", "1, 3.14, 1_000"),
          ("str",         '"hello", f"x={x}"'),
          ("bool",        "True, False"),
          ("list",        "[1, 2, 3]  — mutable"),
          ("tuple",       "(1, 2)     — immutable"),
          ("dict",        '{"k": v}   — key-value'),
          ("set",         "{1, 2, 3}  — unique"),
          ("None",        "null / missing value")]),
        ("String Methods", PALETTE["green"],
         ["s.upper() / s.lower()",
          's.strip() / s.split(",")',
          "s.replace(old, new)",
          "s.startswith(p) / endswith(p)",
          's.join(["a","b"]) -> "a,b"',
          "f-string:  f'x={x:.2f}'",
          "len(s) / s[start:stop:step]",
          'str.format(): "{0}".format(v)']),
        ("List & Dict Ops", PALETTE["orange"],
         ["lst.append(x) / lst.extend(it)",
          "lst.pop(i) / lst.remove(x)",
          "sorted(lst) / lst.sort()",
          "lst[::-1]  — reverse",
          "d.get(k, default)",
          "d.keys() / d.values() / d.items()",
          "dict comprehension: {k:v for k,v in …}",
          "list comprehension: [f(x) for x in …]"]),
        ("Control Flow", PALETTE["peach"],
         ["if x > 0:          # elif / else",
          "for i in range(n): # enumerate",
          "while cond:  break / continue",
          "try: … except E as e: …",
          "finally: …  # always runs",
          "with open(f) as fh: …  # context mgr",
          "match x:            # Python 3.10+",
          "  case 1: …  case _: …"]),
        # row 1
        ("Functions", PALETTE["lav"],
         ["def f(x, y=0, *args, **kw): …",
          "return multiple: return a, b",
          "lambda x: x**2",
          "@decorator  — wraps function",
          "Closures: inner fn captures outer vars",
          "*args = positional varargs",
          "**kwargs = keyword varargs",
          "type hints: def f(x: int) -> str:"]),
        ("Classes & OOP", PALETTE["yellow"],
         ["class Dog(Animal):",
          "  def __init__(self, name):",
          "    super().__init__()",
          "    self.name = name",
          "  def __repr__(self): …",
          "  @property / @setter",
          "  @classmethod / @staticmethod",
          "  __eq__, __lt__, __hash__"]),
        ("Comprehensions & Generators", PALETTE["pink"],
         ["[x**2 for x in range(10)]",
          "{x: x**2 for x in range(5)}",
          "{x for x in lst if x > 0}",
          "(x**2 for x in range(10))  # lazy",
          "yield / yield from  # generator fn",
          "next(gen) — pull one value",
          "itertools.chain, islice, product",
          "map(f, it) / filter(pred, it)"]),
        ("File & Path I/O", PALETTE["purple"],
         ['open("f","r/w/a/rb")',
          "json.load(fh) / json.dump(obj, fh)",
          "csv.reader / csv.DictReader",
          "pathlib.Path('dir') / 'file.txt'",
          "p.read_text() / p.write_text(s)",
          "p.glob('*.py') / p.rglob('**')",
          "os.environ.get('KEY','default')",
          "shutil.copy / shutil.rmtree"]),
        # row 2
        ("Virtual Envs & Packages", PALETTE["mint"],
         ["python -m venv .venv",
          "source .venv/bin/activate",
          "pip install pkg / pip freeze",
          "pip install -r requirements.txt",
          "pyproject.toml / setup.cfg",
          "conda env create -f env.yml",
          "importlib.import_module(name)",
          "__all__ = ['pub_fn'] # exports"]),
        ("Error Handling", PALETTE["sky"],
         ["try: … except (A, B) as e:",
          "raise ValueError('msg')",
          "raise from e  # chain exceptions",
          "assert cond, 'msg'",
          "logging.basicConfig(level=…)",
          "logging.info / warning / error",
          "warnings.warn('msg')",
          "traceback.format_exc()"]),
        ("Useful Stdlib", PALETTE["amber"],
         ["collections: Counter, defaultdict, deque",
          "itertools: chain, product, combinations",
          "functools: lru_cache, partial, reduce",
          "typing: List, Dict, Optional, Union",
          "datetime: date, timedelta, strftime",
          "re: re.compile, search, findall, sub",
          "sys.argv / sys.path / sys.exit(code)",
          "subprocess.run(['cmd'], capture_output=True)"]),
        ("Testing & Debug", PALETTE["rose"],
         ["pytest test_file.py -v",
          "assert f(x) == expected",
          "pytest.fixture / parametrize",
          "unittest.mock.patch",
          "breakpoint()  # Python 3.7+ pdb",
          "pdb.set_trace()  # breakpoint",
          "cProfile.run('f()') — profiling",
          "timeit.timeit('expr', number=N)"]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            t(ax, 0.04, y, item, size=6.3)
            y -= 0.105

    banner(fig,
           "PYTHON  *  The language of AI/ML",
           "PEP 8 style  *  type hints  *  virtual envs  *  test everything")
    save(fig, "python_basics")


# ════════════════════════════════════════════════════════════════════════════
# 2. DATA SCIENCE (NumPy / Pandas / Matplotlib / Sklearn)
# ════════════════════════════════════════════════════════════════════════════
def gen_data_science():
    print("Generating: data_science ...")
    fig, gs = make_fig(3, 4, "DATA SCIENCE CHEAT SHEET",
                       "NumPy · Pandas · Matplotlib · Scikit-learn")

    sections = [
        ("NumPy Arrays", PALETTE["blue"],
         ["np.array([1,2,3]) / np.zeros((m,n))",
          "np.ones / np.eye / np.random.randn",
          "a.shape / a.dtype / a.ndim",
          "a.reshape(m,n) / a.flatten()",
          "a[::2] / a[:, 1] / a[a>0]",
          "np.concatenate / np.stack / np.vstack",
          "np.dot(a,b) / a @ b / np.linalg.inv",
          "np.mean/std/sum(axis=0 or 1)"]),
        ("Pandas Series & DataFrame", PALETTE["green"],
         ["pd.Series([1,2,3], index=['a','b','c'])",
          "pd.DataFrame({'col': [1,2,3]})",
          "df.head() / df.info() / df.describe()",
          "df['col'] / df[['a','b']] / df.loc[r,c]",
          "df.iloc[0:3, 1:4]  — positional slice",
          "df.dropna() / df.fillna(val)",
          "df.rename(columns={'old':'new'})",
          "pd.read_csv / pd.read_parquet"]),
        ("Pandas Wrangling", PALETTE["orange"],
         ["df.merge(df2, on='key', how='left')",
          "df.groupby('col').agg({'v':'mean'})",
          "df.sort_values('col', ascending=False)",
          "df.apply(fn) / df['col'].map(fn)",
          "df.pivot_table(values, index, columns)",
          "pd.melt(df, id_vars, value_vars)",
          "df.query('age > 30 & salary > 50k')",
          "df.astype({'col': int}) / pd.to_datetime"]),
        ("Matplotlib Basics", PALETTE["peach"],
         ["fig, ax = plt.subplots(figsize=(w,h))",
          "ax.plot(x,y,'b-',linewidth=2,label='s')",
          "ax.scatter(x,y,c=z,cmap='viridis')",
          "ax.bar(x, height) / ax.hist(data,bins)",
          "ax.set_xlabel/ylabel/title",
          "ax.legend() / ax.grid(alpha=0.3)",
          "plt.tight_layout(); plt.savefig('f.png')",
          "ax.axhline(y) / ax.axvline(x)"]),
        ("EDA Workflow", PALETTE["lav"],
         ["1. df.shape, df.dtypes, df.isnull().sum()",
          "2. Histograms / boxplots for distributions",
          "3. Correlation: df.corr(); sns.heatmap",
          "4. Categorical: value_counts, bar chart",
          "5. Outliers: IQR or z-score filter",
          "6. Missing: heatmap or msno.matrix",
          "7. Feature relationships: pairplot",
          "8. Target distribution: check imbalance"]),
        ("Seaborn Quick Ref", PALETTE["yellow"],
         ["sns.histplot(df, x='col', hue='grp')",
          "sns.boxplot(x='cat', y='num', data=df)",
          "sns.scatterplot(x, y, hue, size)",
          "sns.heatmap(df.corr(), annot=True)",
          "sns.pairplot(df, hue='target')",
          "sns.catplot(kind='strip/swarm/bar')",
          "sns.lineplot(x, y, ci=95) — CI ribbon",
          "plt.style.use('seaborn-v0_8')"]),
        ("Scikit-learn Pipeline", PALETTE["pink"],
         ["from sklearn.pipeline import Pipeline",
          "from sklearn.preprocessing import StandardScaler",
          "pipe = Pipeline([('sc', StandardScaler()),",
          "                 ('clf', LogisticRegression())])",
          "pipe.fit(X_train, y_train)",
          "pipe.predict(X_test)",
          "pipe.score(X_test, y_test)",
          "GridSearchCV(pipe, params, cv=5)"]),
        ("Preprocessing", PALETTE["purple"],
         ["StandardScaler: zero-mean unit-var",
          "MinMaxScaler: [0,1] range",
          "RobustScaler: median + IQR (outliers)",
          "OrdinalEncoder / LabelEncoder",
          "OneHotEncoder / pd.get_dummies",
          "SimpleImputer(strategy='mean')",
          "PolynomialFeatures(degree=2)",
          "train_test_split(X,y,test_size=0.2)"]),
        ("Classic ML Models", PALETTE["mint"],
         ["LogisticRegression (classification)",
          "LinearRegression / Ridge / Lasso",
          "DecisionTreeClassifier/Regressor",
          "RandomForestClassifier (ensemble)",
          "GradientBoostingClassifier / XGBoost",
          "SVC(kernel='rbf') / SVR",
          "KNeighborsClassifier(n_neighbors=5)",
          "KMeans(n_clusters=k) — unsupervised"]),
        ("Cross-Validation", PALETTE["sky"],
         ["KFold(n_splits=5, shuffle=True)",
          "StratifiedKFold — preserves class ratio",
          "cross_val_score(model, X, y, cv=5)",
          "cross_validate — multiple metrics",
          "LeaveOneOut — small dataset",
          "TimeSeriesSplit — temporal data",
          "Nested CV: outer=eval, inner=tune",
          "RepeatedKFold(n_splits=5, n_repeats=3)"]),
        ("Metrics Quick Ref", PALETTE["amber"],
         ["accuracy_score / balanced_accuracy",
          "precision_score / recall_score / f1",
          "roc_auc_score / average_precision",
          "confusion_matrix — TP/FP/TN/FN",
          "mean_squared_error(squared=False) = RMSE",
          "mean_absolute_error / r2_score",
          "classification_report — full table",
          "cohen_kappa_score — inter-rater"]),
        ("Feature Engineering", PALETTE["rose"],
         ["SelectKBest(f_classif, k=10)",
          "RFE(estimator, n_features_to_select)",
          "PCA(n_components=0.95) — variance kept",
          "TSNE / UMAP — 2D visualisation",
          "feature_importances_ (tree models)",
          "permutation_importance (model-agnostic)",
          "VarianceThreshold — drop near-zero var",
          "Log / sqrt / box-cox transforms"]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            t(ax, 0.04, y, item, size=6.3)
            y -= 0.105

    banner(fig,
           "DATA SCIENCE  *  Explore * Clean * Model * Evaluate",
           "NumPy  *  Pandas  *  Matplotlib  *  Seaborn  *  Scikit-learn")
    save(fig, "data_science")


# ════════════════════════════════════════════════════════════════════════════
# 3. MATHEMATICS FOR ML
# ════════════════════════════════════════════════════════════════════════════
def gen_maths():
    print("Generating: maths_for_ml ...")
    fig, gs = make_fig(3, 4, "MATHEMATICS FOR ML CHEAT SHEET",
                       "Linear Algebra · Calculus · Probability · Statistics")

    sections = [
        ("Vectors & Dot Product", PALETTE["blue"],
         ["v = [v1, v2, ..., vn]  (1-D array)",
          "||v|| = sqrt(sum vi^2)  — L2 norm",
          "u . v = sum(ui*vi) = ||u|| ||v|| cos(θ)",
          "cos similarity = u.v / (||u|| ||v||)",
          "Orthogonal: u.v = 0",
          "Unit vector: v / ||v||",
          "np.dot(a,b) / np.linalg.norm(v)",
          "Outer product: np.outer(u,v) -> matrix"]),
        ("Matrix Operations", PALETTE["green"],
         ["A (m×n) * B (n×p) = C (m×p)",
          "Transpose: A^T  — rows <-> cols",
          "Symmetric: A = A^T",
          "Inverse: A^-1  s.t. A A^-1 = I",
          "Det: np.linalg.det(A)",
          "Rank: np.linalg.matrix_rank(A)",
          "SVD: A = U Σ V^T",
          "Eigenvalues: Av = λv"]),
        ("Derivatives & Gradients", PALETTE["orange"],
         ["f'(x) = lim h->0 [f(x+h)-f(x)] / h",
          "Chain rule: d/dx[f(g(x))] = f'(g)g'",
          "Product rule: (fg)' = f'g + fg'",
          "Gradient ∇f = [∂f/∂x1, ..., ∂f/∂xn]",
          "∂(Wx+b)/∂W = x^T  (matrix deriv)",
          "Jacobian: matrix of partial derivatives",
          "Hessian: matrix of 2nd derivatives",
          "Automatic diff: PyTorch autograd"]),
        ("Probability Basics", PALETTE["peach"],
         ["P(A) ∈ [0,1],  P(Ω) = 1",
          "P(A or B) = P(A)+P(B)-P(A and B)",
          "P(A|B) = P(A,B) / P(B)  — conditional",
          "Independence: P(A,B) = P(A)P(B)",
          "Bayes: P(A|B) = P(B|A)P(A) / P(B)",
          "Total prob: P(B) = Σ P(B|Ai)P(Ai)",
          "Joint -> Marginal: sum/integrate out",
          "MLE: argmax P(data | θ)"]),
        ("Common Distributions", PALETTE["lav"],
         ["Bernoulli(p): P(1)=p, P(0)=1-p",
          "Binomial(n,p): k successes in n trials",
          "Gaussian N(μ,σ²): bell curve",
          "Uniform U(a,b): flat density",
          "Categorical: multi-class discrete",
          "Exponential: time between events",
          "Dirichlet: distribution over distributions",
          "KL divergence: D_KL(P||Q)=Σ P log P/Q"]),
        ("Statistics Essentials", PALETTE["yellow"],
         ["Mean μ = (1/n) Σ xi",
          "Variance σ² = E[(X-μ)²]",
          "Std dev σ = sqrt(σ²)",
          "Covariance Cov(X,Y) = E[(X-μx)(Y-μy)]",
          "Pearson r = Cov(X,Y)/(σx σy)",
          "Median: middle value (robust)",
          "Skewness / Kurtosis — shape of dist",
          "Central Limit Theorem: means -> Normal"]),
        ("Optimisation", PALETTE["pink"],
         ["Gradient descent: θ -= α ∇L(θ)",
          "Convex: single global minimum",
          "Saddle points: zero grad, not minimum",
          "Learning rate α: too high=diverge",
          "Momentum: exponential moving avg grad",
          "Adam: adaptive per-param step size",
          "L-BFGS: second-order, small data",
          "Constrained: Lagrange multipliers"]),
        ("Information Theory", PALETTE["purple"],
         ["Entropy H(X) = -Σ p log p  (bits)",
          "Cross-entropy H(p,q) = -Σ p log q",
          "KL(p||q) = Σ p log(p/q) >= 0",
          "Mutual Info I(X;Y) = H(X)-H(X|Y)",
          "Log loss = cross-entropy loss",
          "Maximum entropy principle",
          "Bits per token = entropy of LLM",
          "Perplexity = 2^H  (language models)"]),
        ("Eigenvalues & PCA", PALETTE["mint"],
         ["Av = λv  — eigenvalue equation",
          "Characteristic poly: det(A-λI)=0",
          "SVD: A = U Σ V^T",
          "PCA: eigenvectors of cov matrix",
          "Explained variance ratio: λi/Σλ",
          "Low-rank approx: keep top-k sing. vals",
          "Whitening: decorrelate + normalise",
          "np.linalg.eig / np.linalg.svd"]),
        ("Norms & Distances", PALETTE["sky"],
         ["L1 norm: Σ|xi|  — Manhattan",
          "L2 norm: sqrt(Σxi²) — Euclidean",
          "Lp norm: (Σ|xi|^p)^(1/p)",
          "Frobenius: sqrt(Σ aij²) — matrix",
          "Cosine dist = 1 - cosine similarity",
          "KL divergence: asymmetric",
          "Wasserstein: optimal transport",
          "Hamming: # positions that differ"]),
        ("Activation Derivatives", PALETTE["amber"],
         ["σ(x) = 1/(1+e^-x)",
          "σ'(x) = σ(x)(1-σ(x))",
          "tanh'(x) = 1 - tanh²(x)",
          "ReLU'(x) = 1 if x>0 else 0",
          "Softmax: p_i = e^xi / Σe^xj",
          "log softmax + NLL = cross-entropy",
          "GELU: x Φ(x)  — used in GPT",
          "SwiGLU: split + gate — LLaMA"]),
        ("Matrix Calculus for NN", PALETTE["rose"],
         ["dL/dW = dL/dy * dy/dW",
          "Linear layer: y = Wx + b",
          "  dL/dW = δ x^T   (outer product)",
          "  dL/dx = W^T δ",
          "  dL/db = δ",
          "Softmax + CE gradient: ŷ - y",
          "Batch: average gradients over batch",
          "Backprop = chain rule recursively"]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            t(ax, 0.04, y, item, size=6.3)
            y -= 0.105

    banner(fig,
           "MATHS FOR ML  *  LA + Calculus + Probability + Stats",
           "Master the fundamentals that power every model")
    save(fig, "maths_for_ml")


# ════════════════════════════════════════════════════════════════════════════
# 4. TOKENIZATION
# ════════════════════════════════════════════════════════════════════════════
def gen_tokenization():
    print("Generating: tokenization ...")
    fig, gs = make_fig(2, 4, "TOKENIZATION CHEAT SHEET",
                       "How text is converted to numbers for LLMs")

    sections = [
        ("Why Tokenization?", PALETTE["blue"],
         ["LLMs work with token IDs, not raw text",
          "Token = word piece / sub-word / char",
          "Vocabulary size: ~32k-200k tokens",
          "Same word -> same token ID (usually)",
          "Unknown words -> split into sub-tokens",
          'Example: "tokenization"',
          '  -> ["token","iz","ation"]',
          "  -> [  3,    22,   811  ]"]),
        ("Tokenizer Types", PALETTE["green"],
         [("BPE", "Byte-Pair Encoding — merge frequent pairs"),
          ("WordPiece", "Google BERT — prefix ## for sub-words"),
          ("SentencePiece", "Language-agnostic, Unicode-safe"),
          ("Unigram", "Probabilistic vocab pruning"),
          ("Char-level", "One token per character (rare)"),
          ("Byte-level", "GPT-2/Llama — raw UTF-8 bytes"),
          ("Tiktoken", "OpenAI fast BPE tokenizer"),
          ("AutoTokenizer", "HuggingFace auto-select")]),
        ("HuggingFace API", PALETTE["orange"],
         ['from transformers import AutoTokenizer',
          'tok = AutoTokenizer.from_pretrained("model")',
          'enc = tok("Hello world!")',
          '# enc.input_ids, enc.attention_mask',
          'tok.decode(ids)  # ids -> string',
          'tok.batch_encode_plus(texts,',
          '  padding=True, truncation=True)',
          'tok.convert_tokens_to_ids(tokens)']),
        ("Special Tokens", PALETTE["peach"],
         ["[CLS] — sequence start (BERT)",
          "[SEP] — separator / end (BERT)",
          "[PAD] — padding to equal length",
          "[MASK] — masked language model",
          "<s> / </s> — start/end of sequence",
          "<unk> — unknown token",
          "<|endoftext|> — GPT end token",
          "add_special_tokens=True (default)"]),
        ("Byte-Pair Encoding (BPE)", PALETTE["lav"],
         ["1. Start: each char is a token",
          "2. Count all adjacent pair frequencies",
          "3. Merge most frequent pair -> new token",
          "4. Repeat until vocab size reached",
          "Ex: 'aab aab ab' -> merge 'aa'='Z'",
          "-> 'Zb Zb ab'  vocab grows",
          "Greedy & deterministic at inference",
          "Used by GPT-2/3/4, RoBERTa, LLaMA"]),
        ("Attention Mask & Padding", PALETTE["yellow"],
         ["Padding: short seqs padded to max len",
          "attention_mask=1 for real tokens",
          "attention_mask=0 for [PAD] tokens",
          "Model ignores PAD in self-attention",
          "max_length=512 (BERT) / 4096+ (LLaMA)",
          "truncation=True — cuts long inputs",
          "stride — sliding window long docs",
          "position_ids tracks true positions"]),
        ("Token Statistics", PALETTE["pink"],
         ["1 token ≈ 4 chars  (English prose)",
          "1 token ≈ 0.75 words",
          "Code: more tokens / fewer chars",
          "Non-English: often more tokens/word",
          "Rare words split into many sub-tokens",
          "Perplexity = 2^(cross-entropy in bits)",
          "OOV (Out-of-Vocab) rate near 0 w/ BPE",
          "tokenizer.vocab_size  — query vocab"]),
        ("Common Model Vocabularies", PALETTE["purple"],
         [("BERT-base", "30,522 WordPiece tokens"),
          ("GPT-2",     "50,257 BPE tokens"),
          ("GPT-4",     "~100,000 tiktoken"),
          ("LLaMA-3",   "128,000 SentencePiece"),
          ("T5",        "32,100 SentencePiece"),
          ("mBERT",     "119,547 multilingual"),
          ("Llama-2",   "32,000 SentencePiece"),
          ("Falcon",    "65,024 BPE")]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            if isinstance(item, tuple):
                key, val = item
                t(ax, 0.04, y, key, size=6.5, bold=True, color=PALETTE["code"])
                t(ax, 0.38, y, val, size=6.3)
            else:
                t(ax, 0.04, y, item, size=6.3)
            y -= 0.115

    banner(fig,
           "TOKENIZATION  *  Text -> Tokens -> IDs -> Embeddings",
           "BPE * WordPiece * SentencePiece * HuggingFace Tokenizers")
    save(fig, "tokenization")


# ════════════════════════════════════════════════════════════════════════════
# 5. EMBEDDINGS
# ════════════════════════════════════════════════════════════════════════════
def gen_embeddings():
    print("Generating: embeddings ...")
    fig, gs = make_fig(2, 4, "EMBEDDINGS CHEAT SHEET",
                       "Dense vector representations for semantic AI")

    sections = [
        ("What Are Embeddings?", PALETTE["blue"],
         ["Embed text/image/code in dense vector",
          "Similar meaning -> close in vector space",
          "Typical dims: 384, 768, 1536, 3072",
          "float32 or float16 values",
          "Dot product / cosine -> similarity",
          "Algebraic: king - man + woman ≈ queen",
          "Learned via self-supervised pretraining",
          "Frozen or fine-tuned for downstream"]),
        ("Embedding Models", PALETTE["green"],
         [("text-emb-3-small", "OpenAI 1536-dim"),
          ("text-emb-3-large", "OpenAI 3072-dim"),
          ("nomic-embed",      "8192-ctx open"),
          ("gte-large",        "Alibaba 1024-dim"),
          ("bge-m3",           "BAAI multilingual"),
          ("all-MiniLM-L6",    "384-dim fast"),
          ("e5-mistral-7b",    "LLM-backed embed"),
          ("colbert-v2",       "Late-interaction")]),
        ("Similarity Metrics", PALETTE["orange"],
         ["Cosine:  u.v / (||u|| ||v||)  [range -1,1]",
          "Dot prod: u.v  [unbounded]",
          "Euclidean: ||u - v||  [0,∞)",
          "Manhattan: Σ|ui-vi|  [0,∞)",
          "Cosine best for normalized embeddings",
          "Dot prod fast when same magnitude",
          "L2 if scale carries meaning",
          "np.dot / scipy.spatial.distance"]),
        ("Sentence Transformers", PALETTE["peach"],
         ['from sentence_transformers import SentenceTransformer',
          'model = SentenceTransformer("all-MiniLM-L6-v2")',
          'embs = model.encode(sentences)',
          '# embs.shape: (N, 384)',
          'util.cos_sim(emb1, emb2)',
          'model.encode(texts, batch_size=32)',
          'normalize_embeddings=True',
          'prompt_name="query"  (asymmetric)']),
        ("OpenAI Embeddings API", PALETTE["lav"],
         ['from openai import OpenAI',
          'client = OpenAI()',
          'resp = client.embeddings.create(',
          '  input=["text..."],',
          '  model="text-embedding-3-small")',
          'vec = resp.data[0].embedding',
          'Batch: pass list of strings',
          'Max tokens: 8191 (ada-v2)']),
        ("Chunking Strategies", PALETTE["yellow"],
         ["Fixed size: chunk_size=512, overlap=50",
          "Sentence: split on . ! ? boundaries",
          "Paragraph: double-newline split",
          "Recursive: try larger then smaller",
          "Semantic: embed then cluster similar",
          "Document: whole doc (short docs only)",
          "Parent-child: store large, retrieve small",
          "Sliding window: stride < chunk_size"]),
        ("Fine-tuning Embeddings", PALETTE["pink"],
         ["Contrastive learning: pull same, push diff",
          "Triplet loss: anchor, pos, neg",
          "MultipleNegativesRankingLoss (MNRL)",
          "SBERT: siamese network architecture",
          "Matryoshka: nested dimensions",
          "Adapter layers: lightweight fine-tune",
          "Hard negative mining improves quality",
          "MTEB benchmark: compare models"]),
        ("Multimodal Embeddings", PALETTE["purple"],
         ["CLIP: image + text in shared space",
          "ImageBind: 6 modalities unified",
          "Stable Diffusion uses CLIP text embs",
          "DALL-E uses CLIP-like text encoder",
          "ColPali: PDF pages as image patches",
          "whisper-emb: audio -> dense vector",
          "Code: CodeBERT, CodeT5+, StarEncoder",
          "Graph: GraphSAGE, Node2Vec"]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            if isinstance(item, tuple):
                key, val = item
                t(ax, 0.04, y, key, size=6.5, bold=True, color=PALETTE["code"])
                t(ax, 0.44, y, val, size=6.3)
            else:
                t(ax, 0.04, y, item, size=6.3)
            y -= 0.115

    banner(fig,
           "EMBEDDINGS  *  The Language of Semantic Similarity",
           "Sentence Transformers * OpenAI * CLIP * Fine-tuning * MTEB")
    save(fig, "embeddings")


# ════════════════════════════════════════════════════════════════════════════
# 6. VECTOR DATABASES
# ════════════════════════════════════════════════════════════════════════════
def gen_vector_db():
    print("Generating: vector_databases ...")
    fig, gs = make_fig(2, 4, "VECTOR DATABASES CHEAT SHEET",
                       "Approximate Nearest Neighbor search at scale")

    sections = [
        ("Why Vector DBs?", PALETTE["blue"],
         ["Store millions of dense embeddings",
          "Fast approximate nearest-neighbor (ANN)",
          "Supports metadata filtering",
          "Scales to billions of vectors",
          "Persistent (survives restarts)",
          "Powers RAG, semantic search, rec sys",
          "CRUD: insert, query, update, delete",
          "vs numpy: no RAM limit, indexed"]),
        ("ANN Algorithms", PALETTE["green"],
         [("HNSW",      "Hierarchical Navigable Small World"),
          ("IVF",       "Inverted File — cluster-based"),
          ("PQ",        "Product Quantization — compress"),
          ("ANNOY",     "Random projection trees"),
          ("ScaNN",     "Google — space-efficient"),
          ("DiskANN",   "SSD-based billion-scale"),
          ("LSH",       "Locality Sensitive Hashing"),
          ("Flat",      "Exact brute-force (small N)")]),
        ("Chroma", PALETTE["orange"],
         ['import chromadb',
          'client = chromadb.Client()  # in-memory',
          '# or chromadb.PersistentClient(path)',
          'col = client.create_collection("mydb")',
          'col.add(ids=["1"], embeddings=[v],',
          '        documents=["text"],',
          '        metadatas=[{"src":"wiki"}])',
          'col.query(query_embeddings=[q], n_results=5)']),
        ("Qdrant", PALETTE["peach"],
         ['from qdrant_client import QdrantClient',
          'client = QdrantClient(":memory:")',
          'client.recreate_collection("name",',
          '  vectors_config=VectorParams(',
          '    size=768, distance=Distance.COSINE))',
          'client.upsert("name",',
          '  points=[PointStruct(id=1, vector=v,',
          '                      payload=meta)])',
          'client.search("name", q, limit=5)']),
        ("Pinecone", PALETTE["lav"],
         ['import pinecone',
          'pc = pinecone.Pinecone(api_key=KEY)',
          'idx = pc.Index("my-index")',
          'idx.upsert(vectors=[',
          '  ("id1", emb, {"meta": "val"})])',
          'results = idx.query(',
          '  vector=q_emb, top_k=10,',
          '  filter={"meta": {"$eq":"val"}})',
          'idx.describe_index_stats()']),
        ("Weaviate", PALETTE["yellow"],
         ['import weaviate',
          'client = weaviate.connect_to_local()',
          'col = client.collections.create("Docs",',
          '  vectorizer_config=Configure.',
          '    Vectorizer.text2vec_openai())',
          'col.data.insert(properties={',
          '  "content": "text..."})',
          'col.query.near_text(query="…", limit=5)']),
        ("Key Concepts", PALETTE["pink"],
         [("Collection/Index", "Namespace for vectors"),
          ("Vector",           "Dense float array (embedding)"),
          ("Payload/Metadata", "JSON attached to each vector"),
          ("n_results/top_k",  "How many neighbors to return"),
          ("Score threshold",  "Min similarity to include"),
          ("Namespace",        "Logical partition (Pinecone)"),
          ("HNSW ef",          "Search-time accuracy vs speed"),
          ("Quantization",     "Compress to int8 / binary")]),
        ("Comparison Table", PALETTE["purple"],
         [("Chroma",    "Local / cloud, great for dev"),
          ("Qdrant",    "Rust, self-host, production"),
          ("Pinecone",  "Managed cloud, easiest setup"),
          ("Weaviate",  "Multi-modal, GraphQL API"),
          ("Milvus",    "Open-source, Kubernetes-ready"),
          ("pgvector",  "Postgres extension, SQL+ANN"),
          ("FAISS",     "Meta, library (no server)"),
          ("Redis",     "In-memory + vector search")]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            if isinstance(item, tuple):
                key, val = item
                t(ax, 0.04, y, key, size=6.5, bold=True, color=PALETTE["code"])
                t(ax, 0.44, y, val, size=6.3)
            else:
                t(ax, 0.04, y, item, size=6.3)
            y -= 0.115

    banner(fig,
           "VECTOR DATABASES  *  Semantic Search at Scale",
           "Chroma * Qdrant * Pinecone * Weaviate * Milvus * pgvector")
    save(fig, "vector_databases")


# ════════════════════════════════════════════════════════════════════════════
# 7. RAG (Retrieval-Augmented Generation)
# ════════════════════════════════════════════════════════════════════════════
def gen_rag():
    print("Generating: rag ...")
    fig, gs = make_fig(2, 4, "RAG CHEAT SHEET",
                       "Retrieval-Augmented Generation — grounded LLM answers")

    sections = [
        ("RAG Architecture", PALETTE["blue"],
         ["1. Index: embed docs -> vector store",
          "2. Retrieve: embed query, ANN search",
          "3. Augment: inject context into prompt",
          "4. Generate: LLM answers with context",
          "Reduces hallucination significantly",
          "No re-training needed (plug-and-play)",
          "Context window = limiting factor",
          "Retriever + Generator = RAG pipeline"]),
        ("Document Processing", PALETTE["green"],
         ["Load: PDFLoader, WebBaseLoader, CSVLoader",
          "Split: RecursiveCharacterTextSplitter",
          "  chunk_size=512, overlap=64",
          "Clean: strip HTML, deduplicate",
          "Enrich: add source/page metadata",
          "Embed: model.encode(chunks)",
          "Store: vectorstore.add_documents(docs)",
          "Re-index: detect and update stale docs"]),
        ("LangChain RAG", PALETTE["orange"],
         ['from langchain_community.vectorstores',
          '  import Chroma',
          'from langchain.chains import',
          '  RetrievalQA',
          'retriever = db.as_retriever(',
          '  search_kwargs={"k": 5})',
          'chain = RetrievalQA.from_chain_type(',
          '  llm=llm, retriever=retriever)']),
        ("LlamaIndex RAG", PALETTE["peach"],
         ['from llama_index.core import',
          '  VectorStoreIndex, SimpleDirectoryReader',
          'docs = SimpleDirectoryReader("data/").load()',
          'idx  = VectorStoreIndex.from_documents(docs)',
          'engine = idx.as_query_engine()',
          'resp = engine.query("What is…?")',
          '# resp.response, resp.source_nodes',
          'idx.storage_context.persist("store/")']),
        ("Advanced Retrieval", PALETTE["lav"],
         [("HyDE",         "Hypothetical doc embedding"),
          ("MMR",          "Max marginal relevance"),
          ("Multi-query",  "Generate 3 query variants"),
          ("Parent-child", "Store large, index small"),
          ("BM25 hybrid",  "Sparse + dense fusion"),
          ("Re-ranker",    "Cross-encoder re-rank top-k"),
          ("Self-query",   "LLM generates metadata filter"),
          ("FLARE",        "Retrieve during generation")]),
        ("Evaluation", PALETTE["yellow"],
         [("Faithfulness", "Is answer grounded in context?"),
          ("Answer relev.", "Does it answer the question?"),
          ("Context prec.", "Are retrieved docs relevant?"),
          ("Context recall","Are all needed docs retrieved?"),
          ("RAGAS",         "End-to-end RAG evaluation"),
          ("TruLens",       "Triad: relevance+grounds+answer"),
          ("DeepEval",      "LLM-based judge metrics"),
          ("Human eval",    "Gold standard — expensive")]),
        ("Prompt Template", PALETTE["pink"],
         ["System:",
          "  You are a helpful assistant.",
          "  Answer ONLY using the context below.",
          "  If unsure, say 'I don't know'.",
          "Context: {retrieved_chunks}",
          "Question: {user_query}",
          "Answer:",
          "  (Cite sources as [doc_id])"]),
        ("Common Failure Modes", PALETTE["purple"],
         [("Wrong chunks", "Bad embedding / chunk size"),
          ("Lost in middle","Context > 4k tokens"),
          ("Hallucination", "LLM ignores context"),
          ("Stale index",   "Data not re-indexed"),
          ("Low precision", "Too many irrelevant docs"),
          ("Low recall",    "Relevant docs not found"),
          ("Latency",       "Large k or slow retriever"),
          ("No metadata",   "Can't filter by date/source")]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            if isinstance(item, tuple):
                key, val = item
                t(ax, 0.04, y, key, size=6.5, bold=True, color=PALETTE["code"])
                t(ax, 0.40, y, val, size=6.3)
            else:
                t(ax, 0.04, y, item, size=6.3)
            y -= 0.115

    banner(fig,
           "RAG  *  Retrieval-Augmented Generation",
           "Index * Retrieve * Augment * Generate * Evaluate")
    save(fig, "rag")


# ════════════════════════════════════════════════════════════════════════════
# 8. MLOps
# ════════════════════════════════════════════════════════════════════════════
def gen_mlops():
    print("Generating: mlops ...")
    fig, gs = make_fig(3, 4, "MLOps CHEAT SHEET",
                       "Experiment Tracking * Deployment * Monitoring * CI/CD")

    sections = [
        ("MLOps Maturity Levels", PALETTE["blue"],
         ["L0: Manual — notebooks, no automation",
          "L1: Pipeline — automated training runs",
          "L2: CI/CD — auto trigger on new data",
          "L3: Full — online learning, A/B tests",
          "Goal: reduce time-to-production",
          "Version: data + code + model + config",
          "Reproducibility: fix all random seeds",
          "Monitoring: data drift + model decay"]),
        ("MLflow", PALETTE["green"],
         ['import mlflow',
          'mlflow.set_experiment("my-exp")',
          'with mlflow.start_run():',
          '  mlflow.log_param("lr", 0.01)',
          '  mlflow.log_metric("acc", 0.95)',
          '  mlflow.log_artifact("model.pkl")',
          '  mlflow.sklearn.log_model(model,"clf")',
          'mlflow ui  # launch local dashboard']),
        ("Weights & Biases", PALETTE["orange"],
         ['import wandb',
          'wandb.init(project="my-project")',
          'wandb.config.update({"lr": 0.01})',
          'wandb.log({"loss": loss,',
          '           "acc": acc})',
          'wandb.save("model.pt")',
          'wandb.watch(model)  # gradients',
          'wandb.finish()']),
        ("FastAPI Model Serving", PALETTE["peach"],
         ['from fastapi import FastAPI',
          'from pydantic import BaseModel',
          'app = FastAPI()',
          'class Input(BaseModel):',
          '  text: str',
          '@app.post("/predict")',
          'def predict(inp: Input):',
          '  return {"label": model(inp.text)}']),
        ("Docker for ML", PALETTE["lav"],
         ['# Dockerfile',
          'FROM python:3.11-slim',
          'WORKDIR /app',
          'COPY requirements.txt .',
          'RUN pip install -r requirements.txt',
          'COPY . .',
          'CMD ["uvicorn", "app:app",',
          '     "--host","0.0.0.0","--port","8000"]']),
        ("DVC (Data Version Control)", PALETTE["yellow"],
         ["dvc init  — init in git repo",
          "dvc add data/train.csv  — track file",
          "dvc push  — upload to remote (S3/GCS)",
          "dvc pull  — download tracked files",
          "dvc repro  — run pipeline stages",
          "dvc dag   — show pipeline graph",
          "dvc params diff  — compare runs",
          "dvc metrics show  — compare metrics"]),
        ("CI/CD for ML", PALETTE["pink"],
         ["GitHub Actions / GitLab CI",
          "Trigger: push to main or new data",
          "Steps: lint -> test -> train -> eval",
          "Gate: fail if metric < threshold",
          "Register: push model to registry",
          "Deploy: update serving endpoint",
          "Rollback: keep previous version",
          "Notify: Slack/email on failure"]),
        ("Model Registry", PALETTE["purple"],
         [("MLflow",     "Built-in registry + stages"),
          ("W&B",        "Artifacts + lineage"),
          ("HuggingFace","push_to_hub + model cards"),
          ("Vertex AI",  "Google managed registry"),
          ("Sagemaker",  "AWS model registry"),
          ("BentoML",    "Bentos = model + deps"),
          ("Stages",     "Staging -> Production"),
          ("Tags",       "metadata: team, version, task")]),
        ("Feature Store", PALETTE["mint"],
         [("Feast",    "Open-source offline+online"),
          ("Tecton",   "Managed feature platform"),
          ("Hopsworks","Open-source + Flink"),
          ("Vertex",   "Google managed features"),
          ("Benefits", "No training-serving skew"),
          ("Offline",  "Parquet / DeltaLake store"),
          ("Online",   "Redis / DynamoDB for <10ms"),
          ("Point-in-time","Correct historical labels")]),
        ("Monitoring", PALETTE["sky"],
         [("Data drift",    "PSI / KS test on input dist"),
          ("Label drift",   "Output distribution shifts"),
          ("Concept drift", "P(y|x) changes over time"),
          ("Prometheus",    "Metrics scraping & alerts"),
          ("Grafana",       "Dashboard visualization"),
          ("Evidently AI",  "ML monitoring reports"),
          ("Latency p99",   "99th percentile latency"),
          ("Error rate",    "5xx / prediction failures")]),
        ("Kubernetes for ML", PALETTE["amber"],
         ["kubectl apply -f deployment.yaml",
          "resources: limits.cpu/memory/nvidia.com/gpu",
          "HPA: auto-scale on CPU/custom metric",
          "Kserve: model serving on K8s",
          "Seldon Core: multi-model serving",
          "Kubeflow: ML pipelines on K8s",
          "PVC: persistent storage for models",
          "Istio: traffic routing for A/B tests"]),
        ("A/B Testing Models", PALETTE["rose"],
         ["Shadow mode: log but don't serve",
          "Canary: route 5% traffic to new model",
          "Blue-green: instant switchover",
          "Multi-armed bandit: adaptive allocation",
          "Statistical test: t-test / chi-square",
          "Sample size: power analysis",
          "Minimum detectable effect (MDE)",
          "Ramp up: 1% -> 5% -> 25% -> 100%"]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            if isinstance(item, tuple):
                key, val = item
                t(ax, 0.04, y, key, size=6.5, bold=True, color=PALETTE["code"])
                t(ax, 0.40, y, val, size=6.3)
            else:
                t(ax, 0.04, y, item, size=6.3)
            y -= 0.105

    banner(fig,
           "MLOps  *  Ship models reliably and repeatably",
           "MLflow * W&B * DVC * Docker * FastAPI * Kubernetes * Monitoring")
    save(fig, "mlops")


# ════════════════════════════════════════════════════════════════════════════
# 9. PROMPT ENGINEERING
# ════════════════════════════════════════════════════════════════════════════
def gen_prompt_eng():
    print("Generating: prompt_engineering ...")
    fig, gs = make_fig(2, 4, "PROMPT ENGINEERING CHEAT SHEET",
                       "Techniques to get the best out of LLMs")

    sections = [
        ("Core Principles", PALETTE["blue"],
         ["Be specific and explicit",
          "Provide context and examples",
          "Specify output format (JSON, markdown)",
          "Set the persona/role in system prompt",
          "Break complex tasks into steps",
          "Iterate: test, observe, refine",
          "Avoid negations: say DO not DON'T",
          "Temperature: 0=deterministic, 1=creative"]),
        ("Zero/Few-Shot", PALETTE["green"],
         ["Zero-shot: just ask directly",
          '  "Classify as positive/negative: {text}"',
          "One-shot: provide one example",
          "Few-shot: provide 3-5 examples",
          "Examples should cover edge cases",
          "Format examples = desired output fmt",
          "Order matters: last example biases",
          "Dynamic: retrieve relevant examples"]),
        ("Chain-of-Thought (CoT)", PALETTE["orange"],
         ['"Think step by step"',
          '"Let\'s reason through this carefully"',
          "Zero-shot CoT: just add the phrase",
          "Few-shot CoT: show worked examples",
          "Self-consistency: sample N paths, vote",
          "Tree-of-Thought: explore branches",
          "Scratchpad: <thinking> tags (Claude)",
          "Best for math, logic, multi-step tasks"]),
        ("System Prompt Template", PALETTE["peach"],
         ["You are a {persona}.",
          "Your goal is to {task}.",
          "Always {constraint_1}.",
          "Never {constraint_2}.",
          "Format your response as {format}.",
          "If unsure, {fallback_behavior}.",
          "Tone: {professional/friendly/concise}.",
          "Language: {English/same as user}."]),
        ("ReAct Pattern", PALETTE["lav"],
         ["Thought: I need to find the population…",
          "Action: search('Paris population')",
          "Observation: 2.1 million (city proper)",
          "Thought: Now I can calculate…",
          "Action: calculator('2.1M * 0.02')",
          "Observation: 42,000",
          "Thought: I have enough info.",
          "Answer: The result is 42,000"]),
        ("Output Formatting", PALETTE["yellow"],
         ['"Return JSON: {"field": value}"',
          '"Use markdown headers and bullets"',
          '"Limit to 3 bullet points"',
          '"Reply in exactly 2 sentences"',
          'Pydantic: model.with_structured_output()',
          '"Start directly, no preamble"',
          '"End with a confidence score 0-10"',
          "JSON mode: OpenAI response_format"]),
        ("Advanced Techniques", PALETTE["pink"],
         [("RAG prompt",  "Inject retrieved context"),
          ("Least-to-most","Decompose then solve"),
          ("Generated KB", "Ask model to recall facts"),
          ("Maieutic",     "Explain then verify"),
          ("COSTAR",       "Context/Objective/Style/Tone"),
          ("Neg prompting", "State what NOT to do"),
          ("Prompt chaining","Pipe output -> next prompt"),
          ("DSPy",          "Programmatic prompt optim.")]),
        ("Common Pitfalls", PALETTE["purple"],
         [("Prompt injection","User overrides system"),
          ("Jailbreaks",     "Role-play / hypotheticals"),
          ("Hallucination",  "Confident wrong answers"),
          ("Sycophancy",     "Agrees with user's claim"),
          ("Lost in middle", "Context > 4k tokens"),
          ("Verbosity",      "Too long = ignore later"),
          ("Ambiguity",      "Vague -> varied outputs"),
          ("Overthinking",   "Chain too long -> drift")]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            if isinstance(item, tuple):
                key, val = item
                t(ax, 0.04, y, key, size=6.5, bold=True, color=PALETTE["code"])
                t(ax, 0.40, y, val, size=6.3)
            else:
                t(ax, 0.04, y, item, size=6.3)
            y -= 0.115

    banner(fig,
           "PROMPT ENGINEERING  *  The Art of Talking to LLMs",
           "Zero-shot * Few-shot * CoT * ReAct * RAG * DSPy")
    save(fig, "prompt_engineering")


# ════════════════════════════════════════════════════════════════════════════
# 10. LLM FINE-TUNING
# ════════════════════════════════════════════════════════════════════════════
def gen_finetuning():
    print("Generating: llm_finetuning ...")
    fig, gs = make_fig(2, 4, "LLM FINE-TUNING CHEAT SHEET",
                       "Adapt pre-trained models to your task")

    sections = [
        ("When to Fine-tune?", PALETTE["blue"],
         ["Consistent format / style needed",
          "Domain-specific vocabulary",
          "Latency: smaller fine-tuned > big LLM",
          "Privacy: no data leaves your infra",
          "Cost: fewer tokens per call",
          "NOT needed if few-shot works",
          "NOT needed if RAG is sufficient",
          "Start with prompting, then fine-tune"]),
        ("Fine-tuning Methods", PALETTE["green"],
         [("Full FT",    "All weights updated — expensive"),
          ("LoRA",       "Low-rank adapters — efficient"),
          ("QLoRA",      "LoRA + 4-bit quantization"),
          ("IA3",        "Rescale activations only"),
          ("Prefix",     "Prepend learnable tokens"),
          ("Adapter",    "Small bottleneck layers"),
          ("RLHF",       "Reward model + PPO"),
          ("DPO",        "Direct Preference Optimization")]),
        ("LoRA Explained", PALETTE["orange"],
         ["W' = W + BA  where rank(B,A) = r",
          "r = 8 or 16  (rank, very small)",
          "alpha = 16   (scaling factor)",
          "Only B and A are trained",
          "Params: r*(d_in+d_out) vs d_in*d_out",
          "Merge at inference: W_new = W + BA",
          "target_modules: q,k,v,o projections",
          "PEFT library: get_peft_model(model)"]),
        ("QLoRA Setup", PALETTE["peach"],
         ['from transformers import BitsAndBytesConfig',
          'bnb = BitsAndBytesConfig(',
          '  load_in_4bit=True,',
          '  bnb_4bit_quant_type="nf4",',
          '  bnb_4bit_compute_dtype=bfloat16)',
          'model = AutoModelForCausalLM.from_pretrained(',
          '  model_id, quantization_config=bnb)',
          'model = prepare_model_for_kbit_training(m)']),
        ("Dataset Format (Instruct)", PALETTE["lav"],
         ['{"messages": [',
          '  {"role":"system","content":"You are…"},',
          '  {"role":"user","content":"Question?"},',
          '  {"role":"assistant","content":"Answer"}',
          ']}',
          "# Alpaca format:",
          '{"instruction":"...","input":"...","output":"…"}',
          "datasets.load_dataset / from_list"]),
        ("Training with Trl", PALETTE["yellow"],
         ['from trl import SFTTrainer',
          'trainer = SFTTrainer(',
          '  model=model,',
          '  train_dataset=dataset,',
          '  peft_config=lora_config,',
          '  dataset_text_field="text",',
          '  max_seq_length=2048,',
          '  args=TrainingArguments(...))']),
        ("Hyperparameters", PALETTE["pink"],
         [("lr",           "2e-4 to 1e-5 (LoRA)"),
          ("batch_size",   "4-16 (gradient accumulate)"),
          ("epochs",       "1-3 (small datasets)"),
          ("warmup_ratio", "0.03-0.05"),
          ("scheduler",    "cosine with warmup"),
          ("max_grad_norm","1.0 — clip gradients"),
          ("weight_decay", "0.01"),
          ("bf16/fp16",    "Mixed precision training")]),
        ("Evaluation & Merging", PALETTE["purple"],
         ['# Evaluate perplexity',
          'trainer.evaluate()',
          '# Save adapter',
          'model.save_pretrained("adapter/")',
          '# Merge LoRA into base model',
          'model = model.merge_and_unload()',
          'model.save_pretrained("merged/")',
          '# Push to HuggingFace Hub',
          'model.push_to_hub("user/model-ft")']),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            if isinstance(item, tuple):
                key, val = item
                t(ax, 0.04, y, key, size=6.5, bold=True, color=PALETTE["code"])
                t(ax, 0.38, y, val, size=6.3)
            else:
                t(ax, 0.04, y, item, size=6.3)
            y -= 0.115

    banner(fig,
           "LLM FINE-TUNING  *  From General to Specialist",
           "LoRA * QLoRA * SFT * DPO * RLHF * PEFT * TRL")
    save(fig, "llm_finetuning")


# ════════════════════════════════════════════════════════════════════════════
# 11. AI AGENTS
# ════════════════════════════════════════════════════════════════════════════
def gen_ai_agents():
    print("Generating: ai_agents ...")
    fig, gs = make_fig(2, 4, "AI AGENTS CHEAT SHEET",
                       "LLM-powered autonomous agents and multi-agent systems")

    sections = [
        ("What is an Agent?", PALETTE["blue"],
         ["LLM + Tools + Memory + Planning",
          "Perceive environment via observations",
          "Decide actions based on goal",
          "Execute: call tools, APIs, code",
          "Observe: receive tool results",
          "Repeat until goal achieved",
          "vs chatbot: takes real-world actions",
          "vs pipeline: dynamic, not pre-scripted"]),
        ("Agent Loop (ReAct)", PALETTE["green"],
         ["Thought: Reason about current state",
          "Action: Choose tool & arguments",
          "Observation: Receive tool output",
          "... repeat N times ...",
          "Final Answer: Synthesise result",
          "Max iterations to prevent loops",
          "Streaming: token-by-token thinking",
          "Interrupt: human-in-the-loop"]),
        ("Common Tools", PALETTE["orange"],
         [("Search",     "web_search(query) -> snippets"),
          ("Calculator", "eval(expr) -> number"),
          ("Code exec",  "python_repl(code) -> output"),
          ("File I/O",   "read/write files"),
          ("API calls",  "requests.get/post"),
          ("Browser",    "playwright screenshot+interact"),
          ("DB query",   "sql_query(query) -> rows"),
          ("Memory",     "store/retrieve past context")]),
        ("Function Calling", PALETTE["peach"],
         ['tools = [{"type":"function","function":{',
          '  "name": "get_weather",',
          '  "description": "Get current weather",',
          '  "parameters": {"type":"object",',
          '    "properties": {"city":{"type":"string"}},',
          '    "required":["city"]}}}]',
          'resp = client.chat.completions.create(',
          '  tools=tools, tool_choice="auto")']),
        ("LangChain Agents", PALETTE["lav"],
         ['from langchain.agents import',
          '  create_react_agent, AgentExecutor',
          'from langchain.tools import DuckDuckGoSearchRun',
          'tools = [DuckDuckGoSearchRun()]',
          'agent = create_react_agent(llm, tools, prompt)',
          'executor = AgentExecutor(',
          '  agent=agent, tools=tools, verbose=True)',
          'executor.invoke({"input":"What is…?"})']),
        ("Memory Types", PALETTE["yellow"],
         [("In-context",  "Recent messages in window"),
          ("Summary",     "Compress old turns -> summary"),
          ("Entity",      "Track people/places/facts"),
          ("Vector",      "Embed + retrieve past turns"),
          ("External DB", "SQL / KV store persistence"),
          ("Episodic",    "Store action/outcome pairs"),
          ("Semantic",    "Background world knowledge"),
          ("Working mem", "Current reasoning scratchpad")]),
        ("Multi-Agent Systems", PALETTE["pink"],
         [("Orchestrator","Directs sub-agents"),
          ("Specialist",  "Focused single-task agent"),
          ("Critic",      "Reviews other agent output"),
          ("Planner",     "Breaks goal into sub-tasks"),
          ("AutoGen",     "Microsoft multi-agent lib"),
          ("CrewAI",      "Role-based agent crews"),
          ("LangGraph",   "Graph of agent nodes"),
          ("OpenAI Swarm","Lightweight handoffs")]),
        ("Safety & Control", PALETTE["purple"],
         ["Human-in-the-loop for irreversible actions",
          "Max iterations / token budget",
          "Tool allowlist: only permitted tools",
          "Sandbox code execution (Docker)",
          "Prompt injection defense",
          "Log all tool calls for audit",
          "Rate limiting: avoid runaway API costs",
          "Graceful degradation on tool failure"]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            if isinstance(item, tuple):
                key, val = item
                t(ax, 0.04, y, key, size=6.5, bold=True, color=PALETTE["code"])
                t(ax, 0.38, y, val, size=6.3)
            else:
                t(ax, 0.04, y, item, size=6.3)
            y -= 0.115

    banner(fig,
           "AI AGENTS  *  LLM + Tools + Memory + Planning",
           "ReAct * Function Calling * LangChain * AutoGen * CrewAI * LangGraph")
    save(fig, "ai_agents")


# ════════════════════════════════════════════════════════════════════════════
# 12. MODEL EVALUATION
# ════════════════════════════════════════════════════════════════════════════
def gen_model_eval():
    print("Generating: model_evaluation ...")
    fig, gs = make_fig(2, 4, "MODEL EVALUATION CHEAT SHEET",
                       "Classification * Regression * LLM * Fairness")

    sections = [
        ("Classification Metrics", PALETTE["blue"],
         ["Accuracy  = (TP+TN) / N",
          "Precision = TP / (TP+FP)  — quality",
          "Recall    = TP / (TP+FN)  — coverage",
          "F1 = 2*P*R/(P+R)  — harmonic mean",
          "F-beta: beta>1 weights recall more",
          "ROC-AUC: discrimination ability",
          "PR-AUC: better for class imbalance",
          "Cohen Kappa: adjust for chance"]),
        ("Confusion Matrix", PALETTE["green"],
         ["         Pred Pos  Pred Neg",
          "Act Pos  TP        FN  <- False Neg",
          "Act Neg  FP        TN  <- True Neg",
          "         ^FP: Type I error",
          "         FN: Type II error",
          "Sensitivity = Recall = TPR",
          "Specificity = TNR = TN/(TN+FP)",
          "sklearn.metrics.confusion_matrix"]),
        ("Regression Metrics", PALETTE["orange"],
         ["MAE  = (1/n) Σ|y-ŷ|  — robust",
          "MSE  = (1/n) Σ(y-ŷ)²  — penalise large",
          "RMSE = sqrt(MSE)  — same units as y",
          "MAPE = (1/n) Σ|y-ŷ|/|y| * 100%",
          "R²   = 1 - SSres/SStot  — variance expl.",
          "Adj R²: penalise extra features",
          "Residual plots: check assumptions",
          "Prediction interval vs conf interval"]),
        ("LLM Evaluation", PALETTE["peach"],
         [("BLEU",     "n-gram precision vs reference"),
          ("ROUGE-L",  "Longest common subsequence"),
          ("BERTScore","Contextual embedding sim"),
          ("BLEURT",   "Learned regression on human"),
          ("G-Eval",   "GPT-4 as judge (1-5 scale)"),
          ("MT-Bench", "Multi-turn instruction eval"),
          ("MMLU",     "57 academic subject MCQs"),
          ("HumanEval","Code generation pass@k")]),
        ("Benchmarks", PALETTE["lav"],
         [("MMLU",      "Knowledge breadth"),
          ("HellaSwag", "Commonsense reasoning"),
          ("TruthfulQA","Avoid falsehoods"),
          ("GSM8K",     "Grade school math"),
          ("HumanEval", "Python code gen"),
          ("MATH",      "Competition math"),
          ("ARC",       "Science QA"),
          ("GPQA",      "PhD-level questions")]),
        ("Cross-Validation", PALETTE["yellow"],
         ["KFold(k=5): standard for tabular",
          "StratifiedKFold: preserve class ratio",
          "GroupKFold: no data leakage by group",
          "TimeSeriesSplit: temporal order",
          "Nested CV: unbiased model selection",
          "Leave-One-Out: very small datasets",
          "Shuffle: shuffle=True for i.i.d. data",
          "Report: mean ± std across folds"]),
        ("Calibration & Uncertainty", PALETTE["pink"],
         ["Calibration: predicted prob = true freq",
          "Reliability diagram: predicted vs actual",
          "Expected Calibration Error (ECE)",
          "Temperature scaling: T>1 = less confident",
          "Platt scaling: sigmoid on raw scores",
          "Isotonic regression: monotone mapping",
          "Bayesian: posterior predictive interval",
          "MC Dropout: stochastic forward passes"]),
        ("Fairness Metrics", PALETTE["purple"],
         [("Demographic parity","Equal pred rate per group"),
          ("Equalised odds",  "Equal TPR+FPR per group"),
          ("Predictive parity","Equal PPV per group"),
          ("Individual fair.", "Similar inputs -> similar out"),
          ("SHAP / LIME",     "Local explanation per pred"),
          ("AIF360",          "IBM fairness toolkit"),
          ("Fairlearn",       "Microsoft mitigation"),
          ("Disparate impact","0.8 rule threshold")]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            if isinstance(item, tuple):
                key, val = item
                t(ax, 0.04, y, key, size=6.5, bold=True, color=PALETTE["code"])
                t(ax, 0.40, y, val, size=6.3)
            else:
                t(ax, 0.04, y, item, size=6.3)
            y -= 0.115

    banner(fig,
           "MODEL EVALUATION  *  Trust your metrics, question your assumptions",
           "Accuracy * Precision * Recall * F1 * ROC-AUC * BLEU * BERTScore * Fairness")
    save(fig, "model_evaluation")


# ════════════════════════════════════════════════════════════════════════════
# 13. REINFORCEMENT LEARNING
# ════════════════════════════════════════════════════════════════════════════
def gen_rl():
    print("Generating: reinforcement_learning ...")
    fig, gs = make_fig(2, 4, "REINFORCEMENT LEARNING CHEAT SHEET",
                       "Agent * Environment * Reward * Policy * Value")

    sections = [
        ("Core Concepts", PALETTE["blue"],
         ["Agent: learner & decision maker",
          "Environment: world agent acts in",
          "State s: current situation",
          "Action a: choice available to agent",
          "Reward r: scalar feedback signal",
          "Policy π(a|s): maps state to action",
          "Episode: sequence until terminal state",
          "Return G_t = Σ γ^k r_{t+k}  (discounted)"]),
        ("Markov Decision Process", PALETTE["green"],
         ["MDP = (S, A, P, R, γ)",
          "S: state space",
          "A: action space",
          "P(s'|s,a): transition probability",
          "R(s,a): expected reward",
          "γ ∈ [0,1]: discount factor",
          "Markov property: future ⊥ past | present",
          "Goal: maximize E[Σ γ^t r_t]"]),
        ("Value Functions", PALETTE["orange"],
         ["V^π(s) = E_π[G_t | S_t=s]",
          "  Expected return from state s under π",
          "Q^π(s,a) = E_π[G_t | S_t=s, A_t=a]",
          "  Expected return from (s,a) under π",
          "Advantage A(s,a) = Q(s,a) - V(s)",
          "Bellman: V(s)=Σ π(a|s)[R+γ V(s')]",
          "Optimal V*: max over all policies",
          "Q-table: tabular Q for small spaces"]),
        ("Q-Learning", PALETTE["peach"],
         ["Off-policy TD control",
          "Q(s,a) += α[r + γ max Q(s',a') - Q(s,a)]",
          "α: learning rate (0.1-0.5)",
          "ε-greedy: explore with prob ε",
          "Decay ε: 1.0 -> 0.01 over training",
          "Tabular: 2D array Q[s][a]",
          "Converges to Q* with sufficient visits",
          "Gym: env.reset() / step(action)"]),
        ("Deep Q-Network (DQN)", PALETTE["lav"],
         ["Q(s,a;θ) — neural network approx",
          "Experience Replay: store (s,a,r,s')",
          "  Sample random minibatch each step",
          "Target Network: θ- updated slowly",
          "  TD target: r + γ max Q(s';θ-)",
          "Loss: (TD target - Q(s,a;θ))²",
          "Double DQN: decouple action select",
          "Dueling: V(s) + A(s,a) heads"]),
        ("Policy Gradient", PALETTE["yellow"],
         ["REINFORCE: θ += α G_t ∇log π(a|s)",
          "Baseline: subtract V(s) to reduce var",
          "Actor-Critic: actor π, critic V",
          "A2C: synchronous advantage AC",
          "A3C: async parallel workers",
          "PPO: clip ratio to trust region",
          "  L = min(r_t A_t, clip(r_t,1-ε,1+ε)A_t)",
          "SAC: entropy-regularised (off-policy)"]),
        ("RLHF for LLMs", PALETTE["pink"],
         ["1. SFT: supervised fine-tune on demos",
          "2. Reward Model: rank human prefs",
          "   RM trained on (chosen, rejected) pairs",
          "3. RL: PPO maximise reward model score",
          "   KL penalty: stay close to SFT model",
          "DPO: skip reward model entirely",
          "  L = -log σ(β log π/π_ref on chosen",
          "             - β log π/π_ref on rejected)"]),
        ("Key Libraries", PALETTE["purple"],
         [("Gymnasium", "Standard RL environment API"),
          ("Stable-SB3","Off-shelf PPO/SAC/TD3 agents"),
          ("TRL",        "RLHF for LLMs — PPO/DPO"),
          ("RLlib",      "Distributed RL — Ray"),
          ("CleanRL",    "Single-file clean impl."),
          ("PettingZoo", "Multi-agent environments"),
          ("MuJoCo",     "Physics simulation envs"),
          ("Atari",      "Classic game benchmarks")]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            if isinstance(item, tuple):
                key, val = item
                t(ax, 0.04, y, key, size=6.5, bold=True, color=PALETTE["code"])
                t(ax, 0.40, y, val, size=6.3)
            else:
                t(ax, 0.04, y, item, size=6.3)
            y -= 0.115

    banner(fig,
           "REINFORCEMENT LEARNING  *  Learn from Rewards",
           "MDP * Q-Learning * DQN * PPO * SAC * RLHF * DPO")
    save(fig, "reinforcement_learning")


# ════════════════════════════════════════════════════════════════════════════
# 14. TIME SERIES
# ════════════════════════════════════════════════════════════════════════════
def gen_time_series():
    print("Generating: time_series ...")
    fig, gs = make_fig(2, 4, "TIME SERIES ANALYSIS CHEAT SHEET",
                       "Classical * Statistical * Deep Learning forecasting")

    sections = [
        ("Core Concepts", PALETTE["blue"],
         ["Time series: ordered sequence over time",
          "Trend: long-term increase/decrease",
          "Seasonality: periodic pattern (weekly…)",
          "Cyclical: non-fixed multi-year waves",
          "Noise / residual: random fluctuation",
          "Stationarity: constant mean/var over t",
          "Autocorrelation: corr(x_t, x_{t-k})",
          "Lag: past value used as feature"]),
        ("Stationarity Tests", PALETTE["green"],
         ["ADF test: H0 = unit root (non-stationary)",
          "  p < 0.05 -> reject H0 -> stationary",
          "KPSS test: H0 = stationary",
          "  p < 0.05 -> reject H0 -> non-stationary",
          "Differencing: y_t' = y_t - y_t-1",
          "Log transform: log(y_t) for exp growth",
          "Seasonal diff: y_t - y_{t-m}",
          "statsmodels: adfuller / kpss"]),
        ("ARIMA Family", PALETTE["orange"],
         ["AR(p): y_t = c + Σ φ_i y_{t-i} + ε_t",
          "MA(q): y_t = c + Σ θ_i ε_{t-i} + ε_t",
          "ARIMA(p,d,q): AR+diff+MA combined",
          "SARIMA(p,d,q)(P,D,Q,m): seasonal",
          "ARIMAX: + exogenous variables",
          "ACF: choose q (MA order)",
          "PACF: choose p (AR order)",
          "AIC/BIC: model selection criterion"]),
        ("Prophet (Facebook/Meta)", PALETTE["peach"],
         ['from prophet import Prophet',
          'df = pd.DataFrame({"ds":dates,"y":vals})',
          'm = Prophet(seasonality_mode="multiplicative",',
          '            yearly_seasonality=True)',
          'm.add_country_holidays(country_name="US")',
          'm.fit(df)',
          'future = m.make_future_dataframe(periods=30)',
          'forecast = m.predict(future)']),
        ("Deep Learning Models", PALETTE["lav"],
         [("LSTM/GRU",   "Sequence-to-sequence RNN"),
          ("TCN",        "Temporal Convolutional Net"),
          ("WaveNet",    "Dilated causal convolutions"),
          ("Transformer","Temporal fusion transformer"),
          ("TFT",        "Multi-horizon prob forecast"),
          ("N-BEATS",    "Pure DL, interpretable"),
          ("PatchTST",   "Transformer with patches"),
          ("TimesFM",    "Google foundation model")]),
        ("Feature Engineering", PALETTE["yellow"],
         ["lag_1, lag_7, lag_30 — past values",
          "rolling_mean(7), rolling_std(30)",
          "diff_1, diff_7 — first differences",
          "hour, day_of_week, month, quarter",
          "is_holiday, is_weekend flags",
          "Fourier features: sin/cos pairs",
          "EWM: exponentially weighted mean",
          "Target encode categorical features"]),
        ("Evaluation Metrics", PALETTE["pink"],
         [("MAE",    "Mean Absolute Error — intuitive"),
          ("RMSE",   "Root MSE — penalise large errs"),
          ("MAPE",   "Mean Abs % Error — scale-free"),
          ("sMAPE",  "Symmetric MAPE [0,200%]"),
          ("MASE",   "vs naive forecast — M4 winner"),
          ("Winkler","Prediction interval scoring"),
          ("CRPS",   "Continuous ranked prob score"),
          ("Walk-forward","Rolling origin evaluation")]),
        ("Libraries", PALETTE["purple"],
         [("statsmodels", "ARIMA, SARIMAX, VAR"),
          ("Prophet",     "Facebook trend+season"),
          ("skforecast",  "sklearn API for time series"),
          ("darts",       "Multiple models unified API"),
          ("NeuralForecast","LSTM/TFT/NHITS"),
          ("GluonTS",     "Amazon probabilistic"),
          ("tslearn",     "Time series ML/clustering"),
          ("tsfresh",     "Automated feature extract")]),
    ]

    for idx, (title, bg, items) in enumerate(sections):
        row, col = divmod(idx, 4)
        ax = fig.add_subplot(gs[row, col])
        section_ax(ax, title, bg)
        y = 0.88
        for item in items:
            if isinstance(item, tuple):
                key, val = item
                t(ax, 0.04, y, key, size=6.5, bold=True, color=PALETTE["code"])
                t(ax, 0.38, y, val, size=6.3)
            else:
                t(ax, 0.04, y, item, size=6.3)
            y -= 0.115

    banner(fig,
           "TIME SERIES  *  Forecast the Future from the Past",
           "ARIMA * Prophet * LSTM * TFT * N-BEATS * skforecast * darts")
    save(fig, "time_series")


# ════════════════════════════════════════════════════════════════════════════
# MAIN — run all generators
# ════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    generators = [
        gen_python,
        gen_data_science,
        gen_maths,
        gen_tokenization,
        gen_embeddings,
        gen_vector_db,
        gen_rag,
        gen_mlops,
        gen_prompt_eng,
        gen_finetuning,
        gen_ai_agents,
        gen_model_eval,
        gen_rl,
        gen_time_series,
    ]

    # Allow filtering: python generate_all_cheatsheets.py python rag mlops
    if len(sys.argv) > 1:
        names = set(sys.argv[1:])
        generators = [g for g in generators if g.__name__.replace("gen_","") in names]

    print(f"\nGenerating {len(generators)} cheat sheet(s)...\n")
    for gen in generators:
        try:
            gen()
        except Exception as e:
            print(f"  ERROR in {gen.__name__}: {e}")

    print(f"\nDone! All PNGs written to:\n  {OUT_BASE}/*/\n")
