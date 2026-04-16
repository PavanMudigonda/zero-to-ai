#!/bin/bash
# Build the Sphinx curriculum tree and site-specific support pages.
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
  "31-ai-powered-dev-tools:31-ai-dev-tools"
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

# Copy LLM discovery files into _extras so they appear at site root
cp -f "$REPO_ROOT/llms.txt" "$DOCS_DIR/_extras/llms.txt" 2>/dev/null || true
cp -f "$REPO_ROOT/llms-full.txt" "$DOCS_DIR/_extras/llms-full.txt" 2>/dev/null || true

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
from typing import Optional
from urllib.parse import urlsplit

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

target_to_source = {target: source for source, target in source_to_target.items()}
phase_output_dirs = {
    "00-course-setup": "00-course-setup",
    "01-python": "01-python",
    "02-data-science": "02-data-science",
    "03-maths": "03-maths",
    "04-token": "04-token",
    "05-embeddings": "05-embeddings",
    "06-neural-networks": "06-neural-networks",
    "07-vector-databases": "07-vector-databases",
    "08-rag": "08-rag",
    "09-mlops": "09-mlops",
    "10-specializations": "10-specializations",
    "11-prompt-engineering": "11-prompt-engineering",
    "12-llm-finetuning": "12-llm-finetuning",
    "13-multimodal": "13-multimodal",
    "14-local-llms": "14-local-llms",
    "15-ai-agents": "15-ai-agents",
    "16-model-evaluation": "16-model-evaluation",
    "17-debugging-troubleshooting": "17-debugging",
    "18-low-code-ai-tools": "18-low-code",
    "19-ai-safety-redteaming": "19-ai-safety",
    "20-real-time-streaming": "20-streaming",
    "21-quizzes": "21-quizzes",
    "22-references": "22-references",
    "23-glossary": "23-glossary",
    "24-advanced-deep-learning": "24-advanced-dl",
    "25-reinforcement-learning": "25-rl",
    "26-time-series-analysis": "26-time-series",
    "27-causal-inference": "27-causal-inference",
    "28-practical-data-science": "28-practical-ds",
    "29-ai-hardware-llm-validation": "29-ai-hardware",
    "30-inference-optimization": "30-inference-opt",
    "31-ai-powered-dev-tools": "31-ai-dev-tools",
}

site_doc_outputs = {
}

roadmap_files = [
    "roadmaps/01_overview.md",
    "roadmaps/02_core_systems.md",
    "roadmaps/03_advanced_topics.md",
    "roadmaps/04_end_to_end_flows.md",
]

link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

def map_source_rel_to_site(rel_path: Path) -> Optional[Path]:
    if rel_path == Path("README.md"):
        return Path("index.md")
    if rel_path == Path("docs/README.md") or rel_path == Path("docs/index.md"):
        return Path("index.md")
    if rel_path.parts and rel_path.parts[0] == "docs":
        name = rel_path.name
        if name in site_doc_outputs:
            return Path(site_doc_outputs[name])
        return rel_path.relative_to("docs")
    if rel_path.parts and rel_path.parts[0] in phase_output_dirs:
        mapped_first = phase_output_dirs[rel_path.parts[0]]
        rest = rel_path.parts[1:]
        return Path("curriculum", mapped_first, *rest)
    return None

def original_path_for_curriculum_output(md_file: Path) -> Path:
    rel = md_file.relative_to(curriculum_dir)
    parts = list(rel.parts)
    parts[0] = target_to_source.get(parts[0], parts[0])
    return repo_root / Path(*parts)

def make_relative_link(current_output_rel: Path, destination_rel: Path) -> str:
    return Path(os.path.relpath(destination_rel, start=current_output_rel.parent)).as_posix()

def rewrite_links(text: str, current_source_path: Path, current_output_rel: Path) -> str:
    def repl(match):
        label, target = match.groups()
        if target.startswith(("#", "mailto:", "tel:", "javascript:")):
            return match.group(0)

        parts = urlsplit(target)
        if parts.scheme or parts.netloc:
            return match.group(0)

        fragment = f"#{parts.fragment}" if parts.fragment else ""
        target_path = parts.path
        if not target_path:
            return match.group(0)

        resolved = (current_source_path.parent / target_path).resolve(strict=False)
        try:
            rel_to_repo = resolved.relative_to(repo_root)
        except ValueError:
            if current_source_path.parent == repo_root and target_path.startswith("../"):
                normalized_target = target_path
                while normalized_target.startswith("../"):
                    normalized_target = normalized_target[3:]
                resolved = (repo_root / normalized_target).resolve(strict=False)
                try:
                    rel_to_repo = resolved.relative_to(repo_root)
                except ValueError:
                    return match.group(0)
            else:
                return match.group(0)

        destination_rel = map_source_rel_to_site(rel_to_repo)
        if destination_rel is None:
            basename = Path(target_path).name
            if basename in site_doc_outputs:
                destination_rel = Path(site_doc_outputs[basename])
            else:
                return match.group(0)

        if target_path.endswith("/") and destination_rel.suffix == "":
            destination_rel = destination_rel / "README.md"

        rewritten_target = make_relative_link(current_output_rel, destination_rel) + fragment
        return f"[{label}]({rewritten_target})"

    return link_pattern.sub(repl, text)

for md_file in curriculum_dir.rglob("*.md"):
    current_output_rel = md_file.relative_to(docs_dir)
    current_source_path = original_path_for_curriculum_output(md_file)
    text = md_file.read_text(encoding="utf-8")
    rewritten = rewrite_links(text, current_source_path, current_output_rel)
    md_file.write_text(rewritten, encoding="utf-8")


# ---------------------------------------------------------------------------
# Inject toctree directives so Sphinx discovers sub-sections in the sidebar.
# ---------------------------------------------------------------------------

def _collect_toctree_entries(directory: Path):
    """Return a list of toctree entry strings for documents inside *directory*."""
    seen = set()
    entries = []

    def _add(entry: str):
        if entry not in seen:
            seen.add(entry)
            entries.append(entry)

    # Root-level markdown files (skip README, it's structural)
    for md in sorted(directory.glob("*.md")):
        if md.name == "README.md":
            continue
        _add(md.stem)

    # Root-level notebooks (deduplicated against .md stems above)
    for nb in sorted(directory.glob("*.ipynb")):
        _add(nb.stem)

    # Sub-directories
    for subdir in sorted(p for p in directory.iterdir() if p.is_dir()):
        sub_readme = subdir / "README.md"
        if sub_readme.exists():
            _add(f"{subdir.name}/README")
        else:
            # Pick the first discoverable document as the entry point
            first = (
                next(iter(sorted(subdir.glob("*.ipynb"))), None)
                or next(iter(sorted(subdir.glob("*.md"))), None)
            )
            if first:
                _add(f"{subdir.name}/{first.stem}")

    return entries


def inject_toctree(directory: Path):
    """Append a hidden toctree to the README.md in *directory* (if any docs exist)."""
    readme = directory / "README.md"
    entries = _collect_toctree_entries(directory)
    if not entries:
        return

    toctree_block = "\n```{toctree}\n:hidden:\n\n"
    for entry in entries:
        toctree_block += entry + "\n"
    toctree_block += "```\n"

    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if "```{toctree}" in text:
            return  # already has a toctree
        readme.write_text(text.rstrip() + "\n" + toctree_block, encoding="utf-8")
    else:
        # Look-up table for directory names that don't title-case well
        _title_overrides = {
            "mml-book": "Mathematics for Machine Learning (MML)",
            "cs229-course": "Stanford CS229 Machine Learning",
            "islp-book": "Introduction to Statistical Learning (ISLP)",
            "mlpp-book": "ML: A Probabilistic Perspective (MLPP)",
            "3blue1brown": "3Blue1Brown Visual Mathematics",
        }
        title = _title_overrides.get(
            directory.name,
            directory.name.replace("_", " ").replace("-", " ").title(),
        )
        # Create a minimal README so Sphinx has a document to attach children to
        readme.write_text(f"# {title}\n{toctree_block}", encoding="utf-8")


def inject_toctrees_recursive(directory: Path):
    """Walk *directory* depth-first, injecting toctrees at every level."""
    for subdir in sorted(p for p in directory.iterdir() if p.is_dir()):
        inject_toctrees_recursive(subdir)
    inject_toctree(directory)


for phase_dir in sorted(p for p in curriculum_dir.iterdir() if p.is_dir()):
    inject_toctrees_recursive(phase_dir)


for source_name, output_rel in site_doc_outputs.items():
    source_path = docs_dir / source_name
    current_source_path = repo_root / source_name
    output_path = docs_dir / output_rel
    current_output_rel = Path(output_rel)

    if current_source_path.exists():
        actual_source_path = current_source_path
    elif source_path.exists():
        actual_source_path = source_path
    else:
        raise FileNotFoundError(
            f"Missing source document: checked {current_source_path} and {source_path}"
        )

    text = actual_source_path.read_text(encoding="utf-8")
    rewritten = rewrite_links(text, actual_source_path, current_output_rel)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rewritten, encoding="utf-8")

# Copy roadmap files into docs/generated/roadmaps/
for rm_rel in roadmap_files:
    rm_source = repo_root / rm_rel
    rm_output = docs_dir / "generated" / rm_rel
    rm_output_rel = Path("generated") / rm_rel
    if rm_source.exists():
        text = rm_source.read_text(encoding="utf-8")
        rewritten = rewrite_links(text, rm_source, rm_output_rel)
        rm_output.parent.mkdir(parents=True, exist_ok=True)
        rm_output.write_text(rewritten, encoding="utf-8")
    else:
        print(f"WARNING: roadmap source not found: {rm_source}")
PY

phase_count=$(find "$CURRICULUM_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
readme_count=$(find "$CURRICULUM_DIR" -type f -name 'README.md' | wc -l | tr -d ' ')
nb_count=$(find "$CURRICULUM_DIR" -type f -name '*.ipynb' | wc -l | tr -d ' ')

# ---------------------------------------------------------------------------
# Normalize notebooks: add missing cell IDs (required by nbformat >= 5.5)
# ---------------------------------------------------------------------------
python3 -c "
import json, glob, uuid, sys

fixed = 0
for path in glob.glob('$CURRICULUM_DIR/**/*.ipynb', recursive=True):
    try:
        with open(path) as f:
            nb = json.load(f)
    except Exception:
        continue
    changed = False
    for cell in nb.get('cells', []):
        if 'id' not in cell:
            cell['id'] = uuid.uuid4().hex[:8]
            changed = True
    # Ensure nbformat_minor >= 5 when cells have id fields (required by schema)
    if nb.get('nbformat') == 4 and nb.get('nbformat_minor', 0) < 5:
        has_ids = any('id' in cell for cell in nb.get('cells', []))
        if has_ids:
            nb['nbformat_minor'] = 5
            changed = True
    if changed:
        with open(path, 'w') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
            f.write('\n')
        fixed += 1
print(f'Normalized {fixed} notebooks (added missing cell IDs, ensured nbformat_minor >= 5).')
"

echo "Published $phase_count phases, $readme_count README files, and $nb_count notebooks."
