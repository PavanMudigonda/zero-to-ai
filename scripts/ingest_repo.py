#!/usr/bin/env python3
"""Ingest the entire zero-to-ai repo into a local ChromaDB vector database."""

import json
import os
import sys
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

REPO_ROOT = Path(__file__).resolve().parent.parent
DB_DIR = REPO_ROOT / ".vectordb"
COLLECTION_NAME = "zero_to_ai_repo"

# File extensions to index
EXTENSIONS = {".py", ".md", ".ipynb", ".txt", ".yml", ".yaml", ".toml", ".sh", ".nix", ".cfg"}

# Directories to skip
SKIP_DIRS = {".venv", ".git", "node_modules", "__pycache__", "zero_to_ai.egg-info", ".vectordb"}

# Max chunk size in characters (~500 tokens ≈ 2000 chars)
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 200


def extract_notebook_text(filepath: Path) -> str:
    """Extract text content from a Jupyter notebook."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            nb = json.load(f)
        parts = []
        for cell in nb.get("cells", []):
            source = cell.get("source", "")
            if isinstance(source, list):
                source = "".join(source)
            cell_type = cell.get("cell_type", "code")
            if cell_type == "markdown":
                parts.append(source)
            elif cell_type == "code":
                parts.append(f"```python\n{source}\n```")
        return "\n\n".join(parts)
    except (json.JSONDecodeError, KeyError):
        return ""


def read_file_text(filepath: Path) -> str:
    """Read text from a file, handling notebooks specially."""
    if filepath.suffix == ".ipynb":
        return extract_notebook_text(filepath)
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception:
        return ""


def chunk_text(text: str, filepath: str) -> list[dict]:
    """Split text into overlapping chunks with metadata."""
    if not text.strip():
        return []

    chunks = []
    lines = text.split("\n")
    current_chunk = []
    current_len = 0

    for i, line in enumerate(lines):
        current_chunk.append(line)
        current_len += len(line) + 1  # +1 for newline

        if current_len >= CHUNK_SIZE:
            chunk_text_str = "\n".join(current_chunk)
            chunks.append({
                "text": chunk_text_str,
                "filepath": filepath,
                "chunk_index": len(chunks),
            })
            # Keep overlap
            overlap_chars = 0
            overlap_start = len(current_chunk)
            for j in range(len(current_chunk) - 1, -1, -1):
                overlap_chars += len(current_chunk[j]) + 1
                if overlap_chars >= CHUNK_OVERLAP:
                    overlap_start = j
                    break
            current_chunk = current_chunk[overlap_start:]
            current_len = sum(len(l) + 1 for l in current_chunk)

    # Don't forget the last chunk
    if current_chunk:
        chunk_text_str = "\n".join(current_chunk)
        if chunk_text_str.strip():
            chunks.append({
                "text": chunk_text_str,
                "filepath": filepath,
                "chunk_index": len(chunks),
            })

    return chunks


def collect_files() -> list[Path]:
    """Collect all indexable files from the repo."""
    files = []
    for root, dirs, filenames in os.walk(REPO_ROOT):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fname in filenames:
            fpath = Path(root) / fname
            if fpath.suffix in EXTENSIONS:
                files.append(fpath)
    return sorted(files)


def main():
    print(f"📁 Repo root: {REPO_ROOT}")
    print(f"💾 Database dir: {DB_DIR}")

    # Collect files
    files = collect_files()
    print(f"📄 Found {len(files)} files to index")

    # Build chunks
    all_chunks = []
    for fpath in files:
        rel_path = str(fpath.relative_to(REPO_ROOT))
        text = read_file_text(fpath)
        chunks = chunk_text(text, rel_path)
        all_chunks.extend(chunks)

    print(f"🧩 Created {len(all_chunks)} chunks")

    if not all_chunks:
        print("❌ No chunks to index!")
        sys.exit(1)

    # Load embedding model
    print("🤖 Loading embedding model (all-MiniLM-L6-v2)...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Initialize ChromaDB
    DB_DIR.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(DB_DIR))

    # Delete existing collection if it exists
    try:
        client.delete_collection(COLLECTION_NAME)
        print("🗑️  Deleted existing collection")
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    # Process in batches
    BATCH_SIZE = 100
    total = len(all_chunks)

    for batch_start in range(0, total, BATCH_SIZE):
        batch_end = min(batch_start + BATCH_SIZE, total)
        batch = all_chunks[batch_start:batch_end]

        texts = [c["text"] for c in batch]
        ids = [f"chunk_{batch_start + i}" for i in range(len(batch))]
        metadatas = [{"filepath": c["filepath"], "chunk_index": c["chunk_index"]} for c in batch]

        # Embed
        embeddings = model.encode(texts, show_progress_bar=False).tolist()

        # Add to ChromaDB
        collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        pct = int(batch_end / total * 100)
        print(f"  ✅ Indexed {batch_end}/{total} chunks ({pct}%)")

    print(f"\n🎉 Done! {total} chunks indexed into ChromaDB at {DB_DIR}")
    print(f"   Collection: {COLLECTION_NAME}")
    print(f"   You can now use the MCP server for RAG queries.")


if __name__ == "__main__":
    main()
