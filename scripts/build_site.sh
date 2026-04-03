#!/bin/bash
# Build the MkDocs curriculum tree and site-specific support pages.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DOCS_DIR="$REPO_ROOT/docs"
CURRICULUM_DIR="$DOCS_DIR/curriculum"
GENERATED_DIR="$DOCS_DIR/generated"

PHASES=(
  "00-course-setup:00-course-setup"
  "01-python:01-python"
  "02-data-science:02-data-science"
  "03-maths:03-maths"
  "04-token:04-token"
  "05-embeddings:05-embeddings"
  "06-neural-networks:06-neural-networks"
  "07-vector-databases:07-vector-databases"
  "08-rag:08-rag"
  "09-mlops:09-mlops"
  "10-specializations:10-specializations"
  "11-prompt-engineering:11-prompt-engineering"
  "12-llm-finetuning:12-llm-finetuning"
  "13-multimodal:13-multimodal"
  "14-local-llms:14-local-llms"
  "15-ai-agents:15-ai-agents"
  "16-model-evaluation:16-model-evaluation"
  "17-debugging-troubleshooting:17-debugging"
  "18-low-code-ai-tools:18-low-code"
  "19-ai-safety-redteaming:19-ai-safety"
  "20-real-time-streaming:20-streaming"
  "21-quizzes:21-quizzes"
  "22-references:22-references"
  "23-glossary:23-glossary"
  "24-advanced-deep-learning:24-advanced-dl"
  "25-reinforcement-learning:25-rl"
  "26-time-series-analysis:26-time-series"
  "27-causal-inference:27-causal-inference"
  "28-practical-data-science:28-practical-ds"
  "29-ai-hardware-llm-validation:29-ai-hardware"
  "30-inference-optimization:30-inference-opt"
)

copy_phase() {
  local src="$1"
  local target="$2"
  local src_dir="$REPO_ROOT/$src"
  local target_dir="$CURRICULUM_DIR/$target"

  if [ ! -d "$src_dir" ]; then
    return
  fi

  mkdir -p "$target_dir"

  # Copy the browsable learning material and supporting assets, while leaving
  # out generated caches and oversized files that bloat the Pages artifact.
  rsync -a --prune-empty-dirs --max-size=10m \
    --exclude '.ipynb_checkpoints/' \
    --exclude '__pycache__/' \
    --exclude '*.pyc' \
    --exclude '.DS_Store' \
    --include '*/' \
    --include '*.ipynb' \
    --include '*.md' \
    --include '*.png' \
    --include '*.PNG' \
    --include '*.jpg' \
    --include '*.jpeg' \
    --include '*.gif' \
    --include '*.svg' \
    --include '*.pdf' \
    --include '*.csv' \
    --include '*.tsv' \
    --include '*.txt' \
    --include '*.json' \
    --include '*.yml' \
    --include '*.yaml' \
    --include '*.py' \
    --include '*.js' \
    --include '*.css' \
    --include '*.html' \
    --include '*.vue' \
    --include '*.sql' \
    --include '*.R' \
    --include '*.r' \
    --include '*.xlsx' \
    --exclude '*' \
    "$src_dir"/ "$target_dir"/
}

rm -rf "$CURRICULUM_DIR" "$GENERATED_DIR"
mkdir -p "$CURRICULUM_DIR" "$GENERATED_DIR"

for phase in "${PHASES[@]}"; do
  src="${phase%%:*}"
  target="${phase##*:}"
  copy_phase "$src" "$target"
done

export REPO_ROOT DOCS_DIR CURRICULUM_DIR GENERATED_DIR

python - <<'PY'
from pathlib import Path
import os
import re

repo_root = Path(os.environ["REPO_ROOT"])
docs_dir = Path(os.environ["DOCS_DIR"])
curriculum_dir = Path(os.environ["CURRICULUM_DIR"])
generated_dir = Path(os.environ["GENERATED_DIR"])

source_to_target = {
    "17-debugging-troubleshooting": "17-debugging",
    "18-low-code-ai-tools": "18-low-code",
    "19-ai-safety-redteaming": "19-ai-safety",
    "20-real-time-streaming": "20-streaming",
    "24-advanced-deep-learning": "24-advanced-dl",
    "25-reinforcement-learning": "25-rl",
    "26-time-series-analysis": "26-time-series",
    "28-practical-data-science": "28-practical-ds",
    "29-ai-hardware-llm-validation": "29-ai-hardware",
    "30-inference-optimization": "30-inference-opt",
}

phase_prefixes = {
    *(f"{i:02d}-{name}" for i, name in []),
}
phase_roots = {
    "00-course-setup", "01-python", "02-data-science", "03-maths", "04-token",
    "05-embeddings", "06-neural-networks", "07-vector-databases", "08-rag",
    "09-mlops", "10-specializations", "11-prompt-engineering",
    "12-llm-finetuning", "13-multimodal", "14-local-llms", "15-ai-agents",
    "16-model-evaluation", "17-debugging", "17-debugging-troubleshooting",
    "18-low-code", "18-low-code-ai-tools", "19-ai-safety",
    "19-ai-safety-redteaming", "20-streaming", "20-real-time-streaming",
    "21-quizzes", "22-references", "23-glossary", "24-advanced-dl",
    "24-advanced-deep-learning", "25-rl", "25-reinforcement-learning",
    "26-time-series", "26-time-series-analysis", "27-causal-inference",
    "28-practical-ds", "28-practical-data-science", "29-ai-hardware",
    "29-ai-hardware-llm-validation", "30-inference-opt",
    "30-inference-optimization",
}

site_doc_outputs = {
    "setup.md": "generated/setup.md",
    "checklist.md": "generated/checklist.md",
}

root_doc_targets = {
    "README.md": "../../index.md",
    "setup.md": "../../generated/setup.md",
    "checklist.md": "../../generated/checklist.md",
    "MASTER_STUDY_GUIDE.md": "../../MASTER_STUDY_GUIDE.md",
    "CAREER_ROADMAP.md": "../../CAREER_ROADMAP.md",
    "INTERVIEW_PREP.md": "../../INTERVIEW_PREP.md",
    "REFERENCES.md": "../../REFERENCES.md",
    "CHANGELOG.md": "../../CHANGELOG.md",
    "CONTRIBUTING.md": "../../CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md": "../../CODE_OF_CONDUCT.md",
    "SUPPORT.md": "../../SUPPORT.md",
    "COMPARISON_MATRICES.md": "../../COMPARISON_MATRICES.md",
    "LICENSE.md": "../../LICENSE.md",
    "WORKSPACE_LEARNING_REVIEW.md": "../../WORKSPACE_LEARNING_REVIEW.md",
}

link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

def map_phase_prefix(path: str) -> str:
    for source, target in source_to_target.items():
        if path.startswith(source + "/"):
            return target + path[len(source):]
        if path == source:
            return target
    return path

def rewrite_site_root_target(target: str) -> str:
    if "://" in target or target.startswith(("#", "mailto:", "tel:")):
        return target
    if target.startswith("curriculum/"):
        return map_phase_prefix(target)
    if target in site_doc_outputs:
        return site_doc_outputs[target]
    head = target.split("/", 1)[0]
    if head in phase_roots:
        return "curriculum/" + map_phase_prefix(target)
    return target

def rewrite_curriculum_target(target: str) -> str:
    if "://" in target or target.startswith(("#", "mailto:", "tel:")):
        return target

    for root_doc, replacement in root_doc_targets.items():
        if target == f"../{root_doc}":
            return replacement

    if target.startswith("../"):
        sibling = target[3:]
        sibling = map_phase_prefix(sibling)
        if sibling.endswith("/"):
            return "../" + sibling + "README.md"
        return "../" + sibling

    return map_phase_prefix(target)

def rewrite_links(text: str, target_rewriter) -> str:
    def repl(match):
        label, target = match.groups()
        return f"[{label}]({target_rewriter(target)})"
    return link_pattern.sub(repl, text)

def write_phase_catalog(phase_dir: Path):
    readme_path = phase_dir / "README.md"
    title = phase_dir.name.replace("-", " ").title()
    if readme_path.exists():
        heading_match = re.search(r"^#\s+(.+)$", readme_path.read_text(encoding="utf-8"), re.MULTILINE)
        if heading_match:
            title = heading_match.group(1).strip()

    root_notebooks = sorted(p for p in phase_dir.glob("*.ipynb"))
    top_sections = sorted(p for p in phase_dir.iterdir() if p.is_dir())
    total_notebooks = len(list(phase_dir.rglob("*.ipynb")))
    total_markdown = len(list(phase_dir.rglob("*.md")))

    lines = [
        f"# {title} Catalog",
        "",
        f"- Total notebooks: **{total_notebooks}**",
        f"- Markdown guides: **{total_markdown}**",
        "",
        "Use this page to jump into the main sections of the phase.",
        "",
    ]

    if root_notebooks:
        lines.extend(["## Root Notebooks", ""])
        for notebook in root_notebooks:
            lines.append(f"- [{notebook.name}]({notebook.name})")
        lines.append("")

    if top_sections:
        lines.extend(["## Sections", ""])
        for section in top_sections:
            section_notebooks = len(list(section.rglob("*.ipynb")))
            section_markdown = len(list(section.rglob("*.md")))
            preferred = None
            for candidate in ("README.md", "START_HERE.ipynb", "00_START_HERE.ipynb"):
                candidate_path = section / candidate
                if candidate_path.exists():
                    preferred = candidate_path
                    break
            if preferred is None:
                first_notebook = sorted(section.rglob("*.ipynb"))
                if first_notebook:
                    preferred = first_notebook[0]
                else:
                    first_markdown = sorted(section.rglob("*.md"))
                    if first_markdown:
                        preferred = first_markdown[0]

            summary = f"{section_notebooks} notebooks"
            if section_markdown:
                summary += f", {section_markdown} markdown files"

            if preferred is not None:
                rel = preferred.relative_to(phase_dir).as_posix()
                lines.append(f"- [{section.name}]({rel}) — {summary}")
            else:
                lines.append(f"- `{section.name}` — {summary}")
        lines.append("")

    catalog_path = phase_dir / "CATALOG.md"
    catalog_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    if readme_path.exists():
        readme = readme_path.read_text(encoding="utf-8")
        marker = "## Site Navigation"
        block = "\n## Site Navigation\n\n- [Browse the phase catalog](CATALOG.md)\n"
        if marker not in readme:
            readme_path.write_text(readme.rstrip() + block + "\n", encoding="utf-8")

for md_file in curriculum_dir.rglob("*.md"):
    text = md_file.read_text(encoding="utf-8")
    rewritten = rewrite_links(text, rewrite_curriculum_target)
    md_file.write_text(rewritten, encoding="utf-8")

for phase_dir in sorted(p for p in curriculum_dir.iterdir() if p.is_dir()):
    write_phase_catalog(phase_dir)

for source_name, output_rel in site_doc_outputs.items():
    source_path = docs_dir / source_name
    output_path = docs_dir / output_rel
    text = source_path.read_text(encoding="utf-8")
    rewritten = rewrite_links(text, rewrite_site_root_target)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rewritten, encoding="utf-8")
PY

phase_count=$(find "$CURRICULUM_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
readme_count=$(find "$CURRICULUM_DIR" -type f -name 'README.md' | wc -l | tr -d ' ')
nb_count=$(find "$CURRICULUM_DIR" -type f -name '*.ipynb' | wc -l | tr -d ' ')
catalog_count=$(find "$CURRICULUM_DIR" -type f -name 'CATALOG.md' | wc -l | tr -d ' ')

echo "Published $phase_count phases, $readme_count README files, $catalog_count catalogs, and $nb_count notebooks."
