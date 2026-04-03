#!/bin/bash
# Copy phase READMEs into docs/curriculum/ for MkDocs build
set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CURRICULUM_DIR="$REPO_ROOT/docs/curriculum"

rm -rf "$CURRICULUM_DIR"
mkdir -p "$CURRICULUM_DIR"

count=0

copy_phase() {
  local src="$1" target="$2"
  if [ -f "$REPO_ROOT/$src/README.md" ]; then
    cp "$REPO_ROOT/$src/README.md" "$CURRICULUM_DIR/$target.md"
    count=$((count + 1))
  fi
}

copy_phase "00-course-setup"              "00-course-setup"
copy_phase "01-python"                    "01-python"
copy_phase "02-data-science"              "02-data-science"
copy_phase "03-maths"                     "03-maths"
copy_phase "04-token"                     "04-token"
copy_phase "05-embeddings"                "05-embeddings"
copy_phase "06-neural-networks"           "06-neural-networks"
copy_phase "07-vector-databases"          "07-vector-databases"
copy_phase "08-rag"                       "08-rag"
copy_phase "09-mlops"                     "09-mlops"
copy_phase "10-specializations"           "10-specializations"
copy_phase "11-prompt-engineering"        "11-prompt-engineering"
copy_phase "12-llm-finetuning"            "12-llm-finetuning"
copy_phase "13-multimodal"                "13-multimodal"
copy_phase "14-local-llms"                "14-local-llms"
copy_phase "15-ai-agents"                 "15-ai-agents"
copy_phase "16-model-evaluation"          "16-model-evaluation"
copy_phase "17-debugging-troubleshooting" "17-debugging"
copy_phase "18-low-code-ai-tools"         "18-low-code"
copy_phase "19-ai-safety-redteaming"      "19-ai-safety"
copy_phase "20-real-time-streaming"       "20-streaming"
copy_phase "21-quizzes"                   "21-quizzes"
copy_phase "22-references"                "22-references"
copy_phase "23-glossary"                  "23-glossary"
copy_phase "24-advanced-deep-learning"    "24-advanced-dl"
copy_phase "25-reinforcement-learning"    "25-rl"
copy_phase "26-time-series-analysis"      "26-time-series"
copy_phase "27-causal-inference"          "27-causal-inference"
copy_phase "28-practical-data-science"    "28-practical-ds"
copy_phase "29-ai-hardware-llm-validation" "29-ai-hardware"
copy_phase "30-inference-optimization"    "30-inference-opt"

echo "Copied $count phase READMEs to docs/curriculum/"
