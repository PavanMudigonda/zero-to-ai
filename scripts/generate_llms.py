#!/usr/bin/env python3
"""
Generate llms.txt, llms-full.txt, and update sitemap.xml lastmod dates.
Usage: python3 scripts/generate_llms.py
"""
import re, glob, json, os
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP = ROOT / "next-docs" / "src" / "app"
SITEMAP = ROOT / "next-docs" / "out" / "sitemap.xml"
BASE = "https://zero-to-ai.dev"
TODAY = date.today().isoformat()  # e.g. 2026-05-24

# ─── 1. Build slug → title map from all _meta.ts files ───────────────────────
def parse_meta(path: str) -> dict[str, str]:
    """Extract {slug: title} from a _meta.ts export default { ... } block."""
    text = open(path).read()
    out = {}
    # Match "key": "Title" or key: "Title"
    for m in re.finditer(r'"?([\w\-]+)"?\s*:\s*(?:"([^"]+)"|{[^}]*"title"\s*:\s*"([^"]+)"})', text):
        slug, t1, t2 = m.group(1), m.group(2), m.group(3)
        title = t1 or t2
        if title:
            out[slug] = title
    return out

# Map: relative_path_from_app → title
slug_title: dict[str, str] = {}
for meta_path in glob.glob(str(APP / "**" / "_meta.ts"), recursive=True):
    rel_dir = Path(meta_path).parent.relative_to(APP)
    titles = parse_meta(meta_path)
    for slug, title in titles.items():
        key = str(rel_dir / slug) if str(rel_dir) != "." else slug
        slug_title[key] = title

def url_to_title(url: str) -> str:
    """Convert a URL to a human-readable title using meta data or slug."""
    path = url.replace(BASE, "").strip("/")
    if not path:
        return "Home"
    segs = path.split("/")
    # Try progressively shorter paths for a meta match
    for end in range(len(segs), 0, -1):
        key = "/".join(segs[:end])
        if key in slug_title:
            return slug_title[key]
    # Fallback: clean up the last slug
    last = segs[-1]
    last = re.sub(r"^\d+[-_]", "", last)   # strip leading numbers
    last = last.replace("_", " ").replace("-", " ")
    return last.title()

# ─── 2. Load all sitemap URLs, grouped by phase ──────────────────────────────
if not SITEMAP.exists():
    print(f"WARNING: {SITEMAP} not found — run `cd next-docs && npm run build` first")
    all_urls = []
else:
    raw = SITEMAP.read_text()
    all_urls = re.findall(r"<loc>(" + re.escape(BASE) + r"[^<]*)</loc>", raw)

# Group: top_segment → [urls in order]
from collections import defaultdict
grouped: dict[str, list[str]] = defaultdict(list)
for u in all_urls:
    seg = u.replace(BASE, "").strip("/").split("/")[0] or "/"
    grouped[seg].append(u)

# Canonical phase order
TOP_META = parse_meta(str(APP / "_meta.ts"))
PHASE_ORDER = [k for k in TOP_META if k not in {"index", "auth"}]

# Phase descriptions
PHASE_DESC = {
    "00-course-setup":            "Environment setup, 2026 model landscape overview, troubleshooting guide.",
    "01-python":                  "Python crash course covering syntax, data structures, functions, OOP, and libraries.",
    "02-data-science":            "NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn — 278 hands-on notebooks including Microsoft DS curriculum, Kaggle, and real-world projects.",
    "03-maths":                   "Linear algebra, calculus, probability, statistics, and optimization. Implements MML, ISLP, Stanford CS229, 3Blue1Brown, and more.",
    "04-token":                   "How text becomes numbers: tiktoken, SentencePiece, HuggingFace Tokenizers. BPE, WordPiece, Unigram, production pipelines.",
    "05-embeddings":              "Text embeddings with OpenAI, Sentence-Transformers, Cohere. Semantic search, similarity, evaluation.",
    "06-neural-networks":         "Build neural nets from scratch: perceptrons, backprop, CNNs, RNNs, LSTMs, attention, and the full Transformer architecture.",
    "07-vector-databases":        "ChromaDB, Qdrant, Weaviate, Milvus, pgvector. Indexing, hybrid search, metadata filtering, production patterns.",
    "08-rag":                     "End-to-end RAG pipelines: chunking, retrieval, reranking, corrective RAG, self-RAG, graph RAG.",
    "09-mlops":                   "Model deployment, monitoring, CI/CD for ML, experiment tracking, model registries, serving infrastructure.",
    "10-specializations":         "Domain tracks: computer vision, NLP, AI agents — each with dedicated notebook sequences.",
    "11-prompt-engineering":      "Chain-of-thought, few-shot, structured outputs with Instructor and DSPy. Production LLM prompt patterns.",
    "12-llm-finetuning":          "LoRA, QLoRA, PEFT, full fine-tuning. DPO, GRPO alignment. Fine-tuning on custom datasets with mini-swe-agent and OpenHands.",
    "13-multimodal":              "Vision-language models, audio processing, video understanding, real-time multimodal pipelines.",
    "14-local-llms":              "Run models locally: Ollama, llama.cpp, MLX. Local RAG, model serving, hardware optimization.",
    "15-ai-agents":               "Function calling, tool use, MCP (Model Context Protocol), OpenAI Agents SDK, LangGraph, multi-agent systems, memory, and agent evaluation.",
    "16-model-evaluation":        "Classification/regression metrics, LLM evaluation, LLM-as-judge, fairness metrics, bias detection, agent evaluation frameworks.",
    "17-debugging-troubleshooting": "Systematic debugging of AI systems: profiling, data quality, model behavior diagnosis.",
    "18-low-code-ai-tools":       "Gradio, Streamlit, HuggingFace Spaces, Flowise, Langflow, Dify, AutoML platforms.",
    "19-ai-safety-redteaming":    "Adversarial testing, content moderation, PII protection, bias mitigation, jailbreak prevention.",
    "20-real-time-streaming":     "Token streaming, WebSockets, WebRTC, real-time RAG, live voice AI.",
    "21-quizzes":                 "Self-assessment questions for each phase of the curriculum.",
    "22-references":              "Curated external resources: papers, videos, courses, and tools organized by phase.",
    "23-glossary":                "Comprehensive AI/ML terminology reference with 500+ definitions.",
    "24-advanced-deep-learning":  "GANs, VAEs, normalizing flows, diffusion models, NeRF, neural ODEs, Bayesian NNs, graph neural networks — 39 notebooks.",
    "25-reinforcement-learning":  "MDP, Q-learning, deep Q-networks, policy gradients, actor-critic, PPO. RLHF foundations.",
    "26-time-series-analysis":    "ARIMA, Prophet, LSTM forecasting, Transformer-based forecasting, anomaly detection.",
    "27-causal-inference":        "DAGs, do-calculus, A/B testing, difference-in-differences, instrumental variables, regression discontinuity.",
    "28-practical-data-science":  "Interview prep, end-to-end projects, SQL, data engineering, recommender systems — 65 notebooks.",
    "29-ai-hardware-llm-validation": "Silicon validation for AMD, NVIDIA, Qualcomm, TPU, Apple Silicon. Datacenter benchmarking.",
    "30-inference-optimization":  "KV cache, PagedAttention, vLLM, TensorRT-LLM, quantization (AWQ, GPTQ, INT4/INT8), speculative decoding.",
    "31-ai-powered-dev-tools":    "VS Code AI setup, MCP deep dive, custom instructions, Cursor, Windsurf, Aider, Claude Code, GitHub Copilot, OpenCode, mini-swe-agent.",
    "32-cheatsheets":             "Quick references: AI/ML, MLOps, cloud (AWS/GCP/Azure), DevOps, and model comparison tables.",
    "33-roadmaps":                "Curated learning roadmaps by role: AI engineer, ML engineer, data scientist, researcher.",
}

# ─── 3. Generate llms.txt (compact — hub page + key notebooks per phase) ─────
def make_compact_lines(phase_urls: list[str], max_items: int = 12) -> list[str]:
    """Return formatted link lines for the compact llms.txt."""
    lines = []
    for u in phase_urls[:max_items]:
        title = url_to_title(u)
        lines.append(f"- [{title}]({u})")
    if len(phase_urls) > max_items:
        lines.append(f"- *…and {len(phase_urls) - max_items} more notebooks — see [llms-full.txt]({BASE}/llms-full.txt)*")
    return lines

compact_lines = [
    "# Zero to AI",
    "",
    "> The ultimate free, open-source AI learning course with 950+ Jupyter notebooks — from Python basics to production AI agents.",
    "",
    "Zero to AI is a self-paced curriculum organized into 34 phases covering machine learning, deep learning, NLP, computer vision, LLMs, RAG, AI agents, MLOps, fine-tuning, and more. Three learning tracks: AI Engineer (4–6 months), ML Engineer (8–10 months), Research (10–12 months).",
    "",
    f"- Website: {BASE}/",
    "- GitHub: https://github.com/PavanMudigonda/zero-to-ai",
    "- License: MIT",
    f"- Full index: [{BASE}/llms-full.txt]({BASE}/llms-full.txt)",
    "",
    "## Curriculum",
    "",
]

for phase in PHASE_ORDER:
    title = TOP_META.get(phase, phase)
    desc  = PHASE_DESC.get(phase, "")
    urls  = grouped.get(phase, [])
    if not urls:
        continue
    compact_lines.append(f"## {title}")
    if desc:
        compact_lines.append(desc)
    compact_lines.append("")
    compact_lines.extend(make_compact_lines(urls))
    compact_lines.append("")

llms_txt = "\n".join(compact_lines)
(ROOT / "llms.txt").write_text(llms_txt)
print(f"Written llms.txt  ({len(compact_lines)} lines)")

# ─── 4. Generate llms-full.txt (every canonical page) ────────────────────────
full_lines = [
    "# Zero to AI — Complete Page Index",
    "",
    "> Every page in the Zero to AI curriculum at https://zero-to-ai.dev/",
    "",
    "Zero to AI is a comprehensive, self-paced learning path with 950+ Jupyter notebooks covering the full AI/ML stack.",
    "",
    f"- Website: {BASE}/",
    "- GitHub: https://github.com/PavanMudigonda/zero-to-ai",
    f"- Compact index: [{BASE}/llms.txt]({BASE}/llms.txt)",
    f"- Last updated: {TODAY}",
    "",
]

for phase in PHASE_ORDER:
    title = TOP_META.get(phase, phase)
    desc  = PHASE_DESC.get(phase, "")
    urls  = grouped.get(phase, [])
    if not urls:
        continue
    full_lines.append(f"## {title}")
    if desc:
        full_lines.append(desc)
    full_lines.append("")
    for u in urls:
        pg_title = url_to_title(u)
        full_lines.append(f"- [{pg_title}]({u})")
    full_lines.append("")

llms_full_txt = "\n".join(full_lines)
(ROOT / "llms-full.txt").write_text(llms_full_txt)
print(f"Written llms-full.txt  ({len(full_lines)} lines, {len(all_urls)} URLs)")

# ─── 5. Update sitemap.xml lastmod to today ───────────────────────────────────
if SITEMAP.exists():
    xml = SITEMAP.read_text()
    updated = re.sub(r"<lastmod>[^<]+</lastmod>", f"<lastmod>{TODAY}</lastmod>", xml)
    SITEMAP.write_text(updated)
    count = xml.count("<lastmod>")
    print(f"Updated sitemap.xml  ({count} lastmod dates → {TODAY})")
else:
    print("Skipped sitemap.xml (file not found — run next build first)")
