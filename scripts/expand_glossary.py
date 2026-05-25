#!/usr/bin/env python3
"""
Add missing terms to 01_GLOSSARY.ipynb.
Run from repo root: python3 scripts/expand_glossary.py
"""
import json
import os
import re

GLOSSARY_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "jupyter-notebooks",
    "23-glossary",
    "01_GLOSSARY",
    "01_GLOSSARY.ipynb",
)

# New terms to add: (letter_section, term_header, definition)
NEW_TERMS = [
    (
        "A",
        "Agent Orchestration",
        "Agent orchestration is the coordination layer in multi-agent systems that routes "
        "tasks, manages context handoff between agents, enforces execution order, and "
        "handles retries and failures. Orchestration frameworks include LangGraph, AutoGen, "
        "and the OpenAI Agents SDK.",
    ),
    (
        "C",
        "Compound AI System",
        "A compound AI system is an architecture that combines multiple components — such as "
        "LLMs, retrievers, tools, code executors, and memory stores — to handle tasks that "
        "no single model call can accomplish alone. Examples include RAG pipelines, "
        "tool-using agents, and multi-agent systems.",
    ),
    (
        "C",
        "Context Length",
        "Context length is the maximum number of tokens a language model can process in a "
        "single forward pass, including both the input prompt and the generated output. "
        "Also referred to as context window size. Modern models range from 8K to 1M+ "
        "tokens.",
    ),
    (
        "F",
        "Flash Attention",
        "Flash Attention is a memory-efficient, IO-aware implementation of the attention "
        "mechanism that avoids materializing the full N×N attention matrix in GPU HBM. "
        "By tiling and fusing operations, it achieves O(N) memory complexity and "
        "significantly faster training and inference, enabling much longer context windows.",
    ),
    (
        "F",
        "Function Calling",
        "Function calling (also called tool use) is a capability in LLM APIs that allows "
        "models to request the execution of predefined functions with structured JSON "
        "arguments. The model decides when to call a tool, the host application executes "
        "it, and the result is fed back to the model — enabling API integration, database "
        "queries, and code execution.",
    ),
    (
        "G",
        "GGUF (GPT-Generated Unified Format)",
        "GGUF is a binary file format for storing quantized LLM weights optimized for "
        "CPU and GPU inference. It replaced the GGML format and is the primary format "
        "used by llama.cpp, Ollama, and LM Studio for local model loading. Supports "
        "embedded metadata, tokenizer information, and multiple quantization levels "
        "(Q4_K_M, Q8_0, etc.).",
    ),
    (
        "G",
        "GRPO (Group Relative Policy Optimization)",
        "GRPO is a reinforcement learning alignment algorithm that improves upon PPO by "
        "eliminating the value network. It computes advantages by comparing rewards across "
        "a group of responses to the same prompt, reducing memory requirements. GRPO was "
        "popularized by DeepSeek-R1 and is increasingly used for reasoning model training.",
    ),
    (
        "G",
        "Guardrail",
        "A guardrail is a safety mechanism applied to AI system inputs or outputs to detect, "
        "filter, or block harmful, sensitive, or policy-violating content. Input guardrails "
        "check for prompt injection, jailbreaks, and off-topic requests. Output guardrails "
        "check for hallucinations, PII leakage, toxicity, and format violations. Libraries "
        "include NVIDIA NeMo Guardrails, Guardrails AI, and LlamaGuard.",
    ),
    (
        "H",
        "HyDE (Hypothetical Document Embeddings)",
        "HyDE is an advanced RAG retrieval technique where the LLM first generates a "
        "hypothetical ideal answer to a query, which is then embedded and used to search "
        "the vector store instead of the original query. This bridges the semantic gap "
        "between sparse user questions and dense document representations.",
    ),
    (
        "L",
        "Logit",
        "A logit is the raw, unnormalized output score produced by a model's final linear "
        "layer before applying softmax. In language models, logits over the entire "
        "vocabulary determine the probability distribution for the next token after "
        "softmax normalisation. Manipulating logits (e.g., temperature scaling, top-k/top-p "
        "filtering) controls generation diversity.",
    ),
    (
        "M",
        "Model Card",
        "A model card is a standardised documentation artifact for ML models that describes "
        "intended use cases, training data, evaluation results across subgroups, known "
        "limitations, and responsible AI considerations. First proposed by Google and "
        "popularized on Hugging Face's model hub as a prerequisite for responsible "
        "model sharing.",
    ),
    (
        "N",
        "Nucleus Sampling",
        "Nucleus sampling (also called top-p sampling) is a text generation strategy that "
        "samples from the smallest subset of tokens whose cumulative probability mass "
        "exceeds a threshold p. Unlike fixed top-k, nucleus sampling dynamically adjusts "
        "the candidate pool size based on the probability distribution, balancing diversity "
        "and coherence. Typical values: p=0.9 or p=0.95.",
    ),
    (
        "R",
        "Reranking",
        "Reranking is a second-stage retrieval step that reorders an initial set of "
        "retrieved documents using a more powerful cross-encoder model (rather than the "
        "bi-encoder used for fast retrieval). Cross-encoders jointly encode the query and "
        "document to produce a relevance score, improving precision at the cost of "
        "additional latency. Common rerankers: Cohere Rerank, BGE-Reranker, Jina Reranker.",
    ),
    (
        "S",
        "System Prompt",
        "The system prompt is the instruction block passed to a language model in the "
        "'system' role before the user conversation begins. It sets the model's persona, "
        "defines behavioral constraints, specifies output format, and establishes safety "
        "guidelines for the session. Distinct from user and assistant turns in the "
        "conversation history. Critical for reliable production behavior.",
    ),
    (
        "T",
        "Tokenizer",
        "A tokenizer is the component responsible for converting raw text into a sequence "
        "of integer token IDs that the model processes, and for decoding model output IDs "
        "back to text. Common algorithms include BPE (GPT family), WordPiece (BERT), and "
        "SentencePiece (T5, LLaMA). Each model has a fixed vocabulary and paired tokenizer "
        "that must be used together.",
    ),
    (
        "T",
        "Top-p Sampling",
        "Top-p sampling (also called nucleus sampling) is a text generation strategy that "
        "samples from the smallest set of most probable tokens whose cumulative probability "
        "exceeds p. This dynamically adjusts the candidate pool size: for peaked "
        "distributions, few tokens are considered; for flat distributions, many are "
        "included. Often combined with temperature scaling.",
    ),
    (
        "U",
        "Unsloth",
        "Unsloth is an open-source library that accelerates LLM fine-tuning by 2–5x and "
        "reduces GPU memory usage by up to 80% compared to standard HuggingFace training. "
        "It achieves this through custom CUDA kernels and manual backpropagation, and is "
        "compatible with HuggingFace TRL and PEFT for LoRA and QLoRA fine-tuning workflows.",
    ),
    (
        "V",
        "VLM (Vision-Language Model)",
        "A vision-language model (VLM) is a multimodal AI model that jointly processes "
        "visual inputs (images or video) and natural language. VLMs use an image encoder "
        "(e.g., ViT) and a projection layer to align visual tokens with a language model's "
        "embedding space. Examples: LLaVA, GPT-4V, Gemini Vision, Claude 3 Opus, "
        "Qwen-VL.",
    ),
    (
        "Y",
        "YAML (YAML Ain't Markup Language)",
        "YAML is a human-readable data serialisation format commonly used for configuration "
        "files in ML systems. In the AI/ML ecosystem it appears in GitHub Actions workflows, "
        "Kubernetes and Helm manifests, MLflow experiment configs, Hugging Face model "
        "metadata (model cards), and agent configuration files.",
    ),
]


def insert_term_into_section(text: str, letter: str, term: str, definition: str) -> str:
    """Insert a new **Term**\\n\\nDefinition block into the correct letter section."""
    section_marker = f"\n## {letter}\n"
    term_block = f"\n**{term}**\n\n{definition}\n"

    if term.lower() in text.lower():
        print(f"  SKIP (already present): {term}")
        return text

    # Find the section
    section_pos = text.find(section_marker)
    if section_pos == -1:
        # Section doesn't exist — create it before ## Z or at end
        # Find where to insert the new section
        # Look for the first section marker that sorts after this letter
        for next_letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if next_letter <= letter:
                continue
            next_marker = f"\n## {next_letter}\n"
            next_pos = text.find(next_marker)
            if next_pos != -1:
                new_section = f"\n## {letter}\n{term_block}"
                text = text[:next_pos] + new_section + text[next_pos:]
                print(f"  ADDED (new section {letter}): {term}")
                return text
        # Append at end
        text = text.rstrip() + f"\n\n## {letter}\n{term_block}"
        print(f"  ADDED (appended section {letter}): {term}")
        return text

    # Find next section start after this one
    next_section_pos = len(text)
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch <= letter:
            continue
        nxt = text.find(f"\n## {ch}\n", section_pos + 1)
        if nxt != -1 and nxt < next_section_pos:
            next_section_pos = nxt

    # Find alphabetically correct insertion point within the section
    section_text = text[section_pos:next_section_pos]
    # Find all **Term** positions in the section
    term_positions = list(re.finditer(r'\n\*\*([^*]+)\*\*\n', section_text))

    insert_pos_in_section = len(section_text)  # default: append to section
    for m in term_positions:
        existing_term = m.group(1).lower()
        if term.lower() < existing_term:
            insert_pos_in_section = m.start()
            break

    # Insert after the section marker if no terms yet
    if not term_positions:
        insert_pos_in_section = len(section_marker)

    absolute_pos = section_pos + insert_pos_in_section
    text = text[:absolute_pos] + term_block + text[absolute_pos:]
    print(f"  ADDED: {term}")
    return text


def main():
    with open(GLOSSARY_PATH, encoding="utf-8") as f:
        nb = json.load(f)

    cell = nb["cells"][0]
    src = "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]

    print(f"Glossary source length before: {len(src)} chars")

    for letter, term, definition in NEW_TERMS:
        src = insert_term_into_section(src, letter, term, definition)

    print(f"Glossary source length after: {len(src)} chars")

    # Write back preserving original format
    if isinstance(cell["source"], list):
        lines = src.split("\n")
        cell["source"] = [
            (line + "\n") if i < len(lines) - 1 else line
            for i, line in enumerate(lines)
        ]
    else:
        cell["source"] = src

    with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    print(f"\nDone — glossary saved to {GLOSSARY_PATH}")


if __name__ == "__main__":
    main()
