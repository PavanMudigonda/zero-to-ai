#!/bin/bash
# Build the MkDocs curriculum tree from the source phase folders.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DOCS_DIR="$REPO_ROOT/docs"
CURRICULUM_DIR="$DOCS_DIR/curriculum"

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

rm -rf "$CURRICULUM_DIR"
mkdir -p "$CURRICULUM_DIR"

for phase in "${PHASES[@]}"; do
  src="${phase%%:*}"
  target="${phase##*:}"
  copy_phase "$src" "$target"
done

phase_count=$(find "$CURRICULUM_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
readme_count=$(find "$CURRICULUM_DIR" -type f -name 'README.md' | wc -l | tr -d ' ')
nb_count=$(find "$CURRICULUM_DIR" -type f -name '*.ipynb' | wc -l | tr -d ' ')

echo "Published $phase_count phases, $readme_count README files, and $nb_count notebooks to docs/curriculum/"
