"""Sphinx configuration for Zero to AI documentation."""

import os

# -- Project information -----------------------------------------------------
project = "Zero to AI"
copyright = "MIT License 2026, Pavan Mudigonda"
author = "Pavan Mudigonda"
release = "0.1.0"

html_baseurl = "https://zero-to-ai.dev/"

# -- SEO / discoverability --------------------------------------------------
# Site-wide <meta> tags injected into every page <head>
html_meta = {
    "description": (
        "Zero to AI: free open-source AI/ML course with 950+ Jupyter notebooks. "
        "Learn Python, deep learning, LLMs, RAG, AI agents, prompt engineering, "
        "fine-tuning, MLOps, and more — from scratch to production."
    ),
    "keywords": (
        "AI course, machine learning tutorial, deep learning, LLM, RAG, "
        "AI agents, prompt engineering, embeddings, vector database, "
        "fine-tuning, MLOps, Python, PyTorch, Transformers, free AI course, "
        "open source AI curriculum, learn AI, Jupyter notebooks"
    ),
    "author": "Pavan Mudigonda",
    "robots": "index, follow",
    # OpenGraph
    "og:title": "Zero to AI — Free AI/ML Course with 950+ Notebooks",
    "og:description": (
        "Self-paced open-source curriculum: Python, deep learning, LLMs, RAG, "
        "AI agents, MLOps, evaluation, and more. 31 phases, 3 tracks."
    ),
    "og:type": "website",
    "og:url": "https://zero-to-ai.dev/",
    "og:site_name": "Zero to AI",
    # Twitter Card
    "twitter:card": "summary_large_image",
    "twitter:title": "Zero to AI — Free AI/ML Course with 950+ Notebooks",
    "twitter:description": (
        "Open-source AI/ML curriculum from Python basics to production agents. "
        "950+ hands-on Jupyter notebooks."
    ),
}

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "sphinx_sitemap",
]

# Mermaid diagram settings — render client-side via CDN (no mmdc binary needed)
mermaid_version = "11"
mermaid_init_js = "mermaid.initialize({startOnLoad:true});"

# MyST parser settings
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_dmath_allow_digits = False
myst_heading_anchors = 3

# Notebook execution settings
nb_execution_mode = "off"
nb_execution_allow_errors = True
suppress_warnings = [
    "mystnb.unknown_mime_type",
    "mystnb.lexer",
    "myst-nb.lexer",
    "myst.header",
    "myst.xref_missing",
    "toc.not_readable",
    "image.not_readable",
    "misc.highlighting_failure",
]

# Treat unknown Pygments lexer names as plain text instead of warning
highlight_language = "python3"

# Source suffix configuration
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst-nb",
    ".ipynb": "myst-nb",
}

# Templates and exclusions
templates_path = ["_templates"]
html_extra_path = ["_extras"]

# Suppress "document not in any toctree" for curriculum notebooks/sub-pages
# that are reachable via links but not explicitly listed in toctrees.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/.ipynb_checkpoints",
    "**/__pycache__",
    # Title-less documents that generate thousands of warnings
    "**/_sidebar.md",
    "**/Untitled.ipynb",
    "**/Test.ipynb",
    # Duplicate .md/.ipynb pairs — keep the notebook, drop the markdown
    "curriculum/02-data-science/3-data-science-examples/01-microsoft-course/1-Introduction/04-stats-and-probability/assignment.md",
    "curriculum/02-data-science/3-data-science-examples/01-microsoft-course/2-Working-With-Data/08-data-preparation/assignment.md",
    "curriculum/02-data-science/3-data-science-examples/01-microsoft-course/4-Data-Science-Lifecycle/15-analyzing/assignment.md",
    # Translation directories — non-English content with broken relative image paths
    "**/translations",
    # Source markdown files that are copied into generated/ by build_site.sh
    # Orphaned docs/ copies of deleted root files
    "COMPARISON_MATRICES.md",
    "CONTRIBUTING.md",
    "LICENSE.md",
    "REFERENCES.md",
    "SUPPORT.md",
    "checklist.md",
    "setup.md",
]

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_title = "Zero to AI"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["sidebar-scroll.js", "sidebar-toggle.js", "scroll-progress.js"]
html_favicon = "assets/favicon.svg"
html_logo = "assets/logo.svg"

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#3f51b5",
        "color-brand-content": "#3f51b5",
    },
    "dark_css_variables": {
        "color-brand-primary": "#7986cb",
        "color-brand-content": "#7986cb",
    },
    "source_repository": "https://github.com/PavanMudigonda/zero-to-ai",
    "source_branch": "main",
    "source_directory": "docs/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/PavanMudigonda/zero-to-ai",
            "html": '<svg stroke="currentColor" fill="currentColor" stroke-width="0" '
            'viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 '
            "3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-"
            "2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 "
            "1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-"
            "3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 "
            ".67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 "
            "2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-"
            '3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 '
            '8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>',
            "class": "",
        },
    ],
}

# Google Analytics — inject via Furo's analytics slot (no extra extension needed)
_ga_id = os.environ.get("GOOGLE_ANALYTICS_ID", "")
if _ga_id:
    html_context = {
        "analytics_id": _ga_id,
    }

# -- Intersphinx mapping -----------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
}


# ---------------------------------------------------------------------------
# Workaround: docutils asserts that <transition> (``---``) nodes live
# directly under the document root.  Notebook markdown cells parsed by
# myst-nb can produce transitions nested inside sections/containers,
# which triggers an AssertionError in docutils ≤ 0.21.  The transform
# below silently removes those offending nodes before docutils checks.
# ---------------------------------------------------------------------------
from docutils import nodes, transforms  # noqa: E402


class _FixNestedTransitions(transforms.Transform):
    """Remove transition nodes that are not direct children of the document."""

    default_priority = 1  # run before docutils.transforms.misc.Transitions (820)

    def apply(self):
        for node in list(self.document.traverse(nodes.transition)):
            if not isinstance(node.parent, nodes.document):
                node.replace_self(nodes.comment("", "(horizontal rule removed)"))


# ---------------------------------------------------------------------------
# Notebook launcher buttons (Colab / Kaggle) for .ipynb pages
# ---------------------------------------------------------------------------
_REPO_NAME = "PavanMudigonda/zero-to-ai"
_REPO_URL = "https://github.com/" + _REPO_NAME

# Short docs-dir names → actual repo directory names
_PHASE_ALIASES = {
    "17-debugging/": "17-debugging-troubleshooting/",
    "18-low-code/": "18-low-code-ai-tools/",
    "19-ai-safety/": "19-ai-safety-redteaming/",
    "20-streaming/": "20-real-time-streaming/",
    "24-advanced-dl/": "24-advanced-deep-learning/",
    "25-rl/": "25-reinforcement-learning/",
    "26-time-series/": "26-time-series-analysis/",
    "28-practical-ds/": "28-practical-data-science/",
    "29-ai-hardware/": "29-ai-hardware-llm-validation/",
    "30-inference-opt/": "30-inference-optimization/",
}


def _notebook_page_context(app, pagename, templatename, context, doctree):
    """Inject Colab / Kaggle URLs into the template context for .ipynb pages."""
    src = context.get("page_source_suffix", "")
    if src != ".ipynb":
        context["notebook_launchers"] = None
        return

    # Map from docs-relative path back to the repo-root path
    repo_path = pagename + ".ipynb"
    if repo_path.startswith("curriculum/"):
        repo_path = repo_path[len("curriculum/"):]
    for short, full in _PHASE_ALIASES.items():
        if repo_path.startswith(short):
            repo_path = full + repo_path[len(short):]
            break

    blob_url = _REPO_URL + "/blob/main/" + repo_path
    colab_url = (
        "https://colab.research.google.com/github/"
        + _REPO_NAME + "/blob/main/" + repo_path
    )
    kaggle_url = "https://kaggle.com/kernels/welcome?src=" + blob_url

    context["notebook_launchers"] = {
        "colab_url": colab_url,
        "kaggle_url": kaggle_url,
    }


def setup(app):
    app.add_transform(_FixNestedTransitions)
    app.connect("html-page-context", _notebook_page_context)
