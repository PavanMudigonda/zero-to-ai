#!/usr/bin/env python3
"""
Add > **Status:** badges to hub notebooks that don't have one.
Run from repo root: python3 scripts/add_status_badges.py
"""
import json
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "jupyter-notebooks")

# (dir, hub_file, status_message)
HUB_STATUS = [
    (
        "00-course-setup",
        "00-course-setup.ipynb",
        "Complete — environment setup guide is fully available. Quick-start in 5 minutes, "
        "or follow the detailed setup walkthrough below.",
    ),
    (
        "01-python",
        "01-python.ipynb",
        "Developing — this is a lightweight bridge module, not a full Python course. "
        "Use the referenced external resources and return when you can comfortably write "
        "basic Python before moving into Phase 2.",
    ),
    (
        "02-data-science",
        "02-data-science.ipynb",
        "Complete — comprehensive NumPy, pandas, matplotlib, and scikit-learn coverage. "
        "Start with the recommended first pass in this notebook.",
    ),
    (
        "03-maths",
        "03-maths.ipynb",
        "Complete — 153 notebooks across 10 learning tracks. See the folder map and "
        "learning paths below to choose the right track for your background.",
    ),
    (
        "04-token",
        "04-token.ipynb",
        "Complete — all planned tokenization notebooks are available. Start from "
        "`01_START_HERE.ipynb`.",
    ),
    (
        "05-embeddings",
        "05-embeddings.ipynb",
        "Complete — covers embedding models, semantic search, paraphrase mining, and "
        "vector integration. Start from `01_START_HERE.ipynb`.",
    ),
    (
        "06-neural-networks",
        "06-neural-networks.ipynb",
        "Complete — covers backpropagation, PyTorch fundamentals, attention, and "
        "transformers. Start from `01_START_HERE.ipynb`.",
    ),
    (
        "07-vector-databases",
        "07-vector-databases.ipynb",
        "Complete — covers FAISS, Chroma, Pinecone, Weaviate, Qdrant, and ANN algorithms. "
        "Start from `01_START_HERE.ipynb`.",
    ),
    (
        "08-rag",
        "08-rag.ipynb",
        "Complete — covers basic to advanced RAG, LangChain, LlamaIndex, and RAG "
        "evaluation. Start from `01_START_HERE.ipynb`.",
    ),
    (
        "09-mlops",
        "09-mlops.ipynb",
        "Complete — covers experiment tracking, model serving, Docker, CI/CD, and cloud "
        "deployment. Work through the notebooks in order.",
    ),
    (
        "10-specializations",
        "10-specializations.ipynb",
        "Developing — the hub and all three sub-tracks (Computer Vision, Advanced NLP, "
        "AI Agents) have content; additional depth is planned. Treat this as a selective "
        "deep-dive elective after the core phases.",
    ),
    (
        "11-prompt-engineering",
        "11-prompt-engineering.ipynb",
        "Complete — all planned notebooks are available. Start from "
        "`01_START_HERE.ipynb`.",
    ),
    (
        "12-llm-finetuning",
        "12-llm-finetuning.ipynb",
        "Complete — covers SFT, LoRA, QLoRA, DPO, GRPO, quantisation, and evaluation. "
        "Start from `01_START_HERE.ipynb`.",
    ),
    (
        "13-multimodal",
        "13-multimodal.ipynb",
        "Developing — vision-language models, image generation, and audio AI have solid "
        "coverage; video generation and live omnimodal assistants are planned for a later "
        "update.",
    ),
    (
        "15-ai-agents",
        "15-ai-agents.ipynb",
        "Complete — covers function calling, ReAct, multi-agent frameworks, MCP, "
        "autonomous agents, and agentic evaluation. Start from `01_START_HERE.ipynb`.",
    ),
    (
        "16-model-evaluation",
        "16-model-evaluation.ipynb",
        "Complete — all planned notebooks are available. Start from "
        "`01_START_HERE.ipynb`.",
    ),
    (
        "17-debugging-troubleshooting",
        "17-debugging-troubleshooting.ipynb",
        "Developing — core debugging notebooks are available; additional content is "
        "planned. Work through what is here alongside your other phases.",
    ),
    (
        "18-low-code-ai-tools",
        "18-low-code-ai-tools.ipynb",
        "Complete — covers Gradio, Streamlit, Hugging Face Spaces, and AutoML. Start "
        "from `02_gradio_basics.ipynb`.",
    ),
    (
        "19-ai-safety-redteaming",
        "19-ai-safety-redteaming.ipynb",
        "Complete — all planned notebooks are available. Start from "
        "`01_START_HERE.ipynb`.",
    ),
    (
        "21-quizzes",
        "21-quizzes.ipynb",
        "Developing — quizzes for Phases 15–18 are available; full curriculum coverage "
        "is still being built out.",
    ),
    (
        "22-references",
        "22-references.ipynb",
        "Complete — curated resource shelf with Microsoft Labs, Stanford courses, "
        "YouTube educators, and cloud platform guides.",
    ),
    (
        "23-glossary",
        "23-glossary.ipynb",
        "Complete — A–Z reference for AI/ML terminology. Read "
        "`01_GLOSSARY/01_GLOSSARY.ipynb` at any time during the curriculum.",
    ),
    (
        "24-advanced-deep-learning",
        "24-advanced-deep-learning.ipynb",
        "Complete — 39+ sub-topics across advanced architectures and techniques. Start "
        "from `01_START_HERE.ipynb`.",
    ),
    (
        "25-reinforcement-learning",
        "25-reinforcement-learning.ipynb",
        "Complete — covers MDPs, Q-learning, DQN, policy gradients, and multi-agent RL.",
    ),
    (
        "26-time-series-analysis",
        "26-time-series-analysis.ipynb",
        "Complete — covers ARIMA, Prophet, LSTM, and transformer-based forecasting.",
    ),
    (
        "27-causal-inference",
        "27-causal-inference.ipynb",
        "Developing — foundational causal inference notebooks are available; causal ML "
        "and advanced heterogeneous treatment effect notebooks are planned.",
    ),
    (
        "28-practical-data-science",
        "28-practical-data-science.ipynb",
        "Complete — 12 applied tracks across interview prep, CV, NLP, ML, SQL, and "
        "time series.",
    ),
    (
        "29-ai-hardware-llm-validation",
        "29-ai-hardware-llm-validation.ipynb",
        "Complete — 9 theory sections and 8 hands-on labs. This is a specialised "
        "elective for silicon validation, ML infra, and AI platform engineering roles.",
    ),
    (
        "31-ai-powered-dev-tools",
        "31-ai-powered-dev-tools.ipynb",
        "Complete — covers Copilot agent mode, MCP servers, custom instructions, and "
        "AI-native VS Code workflows. Optional but useful much earlier than Phase 31 "
        "for many learners.",
    ),
    (
        "32-cheatsheets",
        "32-cheatsheets.ipynb",
        "Complete — quick-reference guides for Docker, Kubernetes, Git, GitHub Actions, "
        "cloud CLIs, Linux, and AI/ML DevOps.",
    ),
]

SKIP_IF_CONTAINS = "**Status:**"


def get_source_text(source_field) -> str:
    if isinstance(source_field, list):
        return "".join(source_field)
    return source_field


def set_source_field(original, new_text: str):
    """Return source in the same format (list or string) as the original."""
    if isinstance(original, list):
        return list(new_text)  # each char — no, better to split by lines
    return new_text


def insert_status(source, status_msg: str):
    """Insert > **Status:** line after the first heading line."""
    lines = source.split("\n")
    # Find first line that starts with '#'
    insert_after = 0
    for i, line in enumerate(lines):
        if line.startswith("#"):
            insert_after = i
            break
    status_lines = [
        "",
        f"> **Status:** {status_msg}",
        "",
    ]
    new_lines = lines[: insert_after + 1] + status_lines + lines[insert_after + 1 :]
    return "\n".join(new_lines)


def patch_notebook(path: str, status_msg: str) -> bool:
    with open(path, encoding="utf-8") as f:
        nb = json.load(f)

    first_cell = nb["cells"][0]
    if first_cell.get("cell_type") != "markdown":
        print(f"  SKIP — first cell is not markdown in {path}")
        return False

    src = get_source_text(first_cell["source"])
    if SKIP_IF_CONTAINS in src:
        return False  # already has Status

    new_src = insert_status(src, status_msg)

    # Preserve original format (list vs string)
    if isinstance(first_cell["source"], list):
        # Store as list of lines with \n at end (standard Jupyter format)
        new_lines = new_src.split("\n")
        new_source = [
            (line + "\n") if i < len(new_lines) - 1 else line
            for i, line in enumerate(new_lines)
        ]
        first_cell["source"] = new_source
    else:
        first_cell["source"] = new_src

    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    return True


def main():
    updated = 0
    skipped = 0
    for dir_name, hub_file, status_msg in HUB_STATUS:
        path = os.path.join(BASE, dir_name, hub_file)
        if not os.path.exists(path):
            print(f"MISSING {dir_name}/{hub_file}")
            continue
        changed = patch_notebook(path, status_msg)
        if changed:
            print(f"UPDATED {dir_name}/{hub_file}")
            updated += 1
        else:
            print(f"SKIP    {dir_name}/{hub_file} (already has Status or non-markdown first cell)")
            skipped += 1

    print(f"\nDone — {updated} updated, {skipped} skipped.")


if __name__ == "__main__":
    main()
