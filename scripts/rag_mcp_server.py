#!/usr/bin/env python3
"""MCP server that provides RAG search over the zero-to-ai repo using ChromaDB."""

import json
from pathlib import Path

import chromadb
from mcp.server.fastmcp import FastMCP
from sentence_transformers import SentenceTransformer

REPO_ROOT = Path(__file__).resolve().parent.parent
DB_DIR = REPO_ROOT / ".vectordb"
COLLECTION_NAME = "zero_to_ai_repo"

# Initialize MCP server
mcp = FastMCP(
    "zero-to-ai-rag",
    instructions="RAG search over the zero-to-ai repository using a local ChromaDB vector database",
)

# Lazy-loaded globals
_model = None
_collection = None


def _get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def _get_collection():
    global _collection
    if _collection is None:
        client = chromadb.PersistentClient(path=str(DB_DIR))
        _collection = client.get_collection(COLLECTION_NAME)
    return _collection


@mcp.tool()
def search_repo(query: str, n_results: int = 10) -> str:
    """Search the zero-to-ai repository for content related to your query.

    Use this to find relevant code examples, explanations, configurations,
    and documentation from the repository's notebooks, scripts, and markdown files.

    Args:
        query: Natural language search query (e.g., "how to use ChromaDB", "tokenizer training")
        n_results: Number of results to return (default: 10, max: 30)
    """
    n_results = min(max(1, n_results), 30)

    model = _get_model()
    collection = _get_collection()

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )

    if not results["documents"] or not results["documents"][0]:
        return "No results found for your query."

    output_parts = []
    for i, (doc, meta, dist) in enumerate(
        zip(results["documents"][0], results["metadatas"][0], results["distances"][0])
    ):
        similarity = 1 - dist  # cosine distance -> similarity
        filepath = meta.get("filepath", "unknown")
        chunk_idx = meta.get("chunk_index", 0)
        output_parts.append(
            f"### Result {i + 1} - {filepath} (chunk {chunk_idx}, similarity: {similarity:.3f})\n\n{doc}\n"
        )

    header = f"Found {len(output_parts)} results for: \"{query}\"\n\n"
    return header + "\n---\n\n".join(output_parts)


@mcp.tool()
def search_repo_by_file(query: str, file_pattern: str, n_results: int = 10) -> str:
    """Search the repo filtered to files matching a pattern.

    Args:
        query: Natural language search query
        file_pattern: Substring to match in file paths (e.g., "07-vector", ".py", "README")
        n_results: Number of results to return (default: 10)
    """
    n_results = min(max(1, n_results), 30)

    model = _get_model()
    collection = _get_collection()

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(n_results * 5, 100),  # fetch more to filter
        include=["documents", "metadatas", "distances"],
    )

    if not results["documents"] or not results["documents"][0]:
        return "No results found."

    output_parts = []
    for doc, meta, dist in zip(
        results["documents"][0], results["metadatas"][0], results["distances"][0]
    ):
        filepath = meta.get("filepath", "")
        if file_pattern.lower() not in filepath.lower():
            continue
        similarity = 1 - dist
        chunk_idx = meta.get("chunk_index", 0)
        output_parts.append(
            f"### {filepath} (chunk {chunk_idx}, similarity: {similarity:.3f})\n\n{doc}\n"
        )
        if len(output_parts) >= n_results:
            break

    if not output_parts:
        return f"No results matching file pattern '{file_pattern}'."

    header = f"Found {len(output_parts)} results for \"{query}\" in files matching \"{file_pattern}\"\n\n"
    return header + "\n---\n\n".join(output_parts)


@mcp.tool()
def list_indexed_files() -> str:
    """List all files that have been indexed in the vector database.

    Returns a summary of all indexed files grouped by directory.
    """
    collection = _get_collection()

    # Get all metadatas
    all_data = collection.get(include=["metadatas"])
    filepaths = set()
    for meta in all_data["metadatas"]:
        filepaths.add(meta.get("filepath", "unknown"))

    # Group by top-level directory
    by_dir: dict[str, list[str]] = {}
    for fp in sorted(filepaths):
        parts = fp.split("/")
        top_dir = parts[0] if len(parts) > 1 else "."
        by_dir.setdefault(top_dir, []).append(fp)

    output = f"**{len(filepaths)} files indexed across {len(by_dir)} directories**\n\n"
    for dir_name, files in sorted(by_dir.items()):
        output += f"### {dir_name}/ ({len(files)} files)\n"
        for f in files[:10]:  # Show first 10 per directory
            output += f"- {f}\n"
        if len(files) > 10:
            output += f"- ... and {len(files) - 10} more\n"
        output += "\n"

    return output


@mcp.tool()
def get_db_stats() -> str:
    """Get statistics about the vector database.

    Returns the number of chunks, files, and database size.
    """
    collection = _get_collection()
    count = collection.count()

    all_data = collection.get(include=["metadatas"])
    filepaths = set(meta.get("filepath", "") for meta in all_data["metadatas"])

    db_size = sum(f.stat().st_size for f in DB_DIR.rglob("*") if f.is_file())
    db_size_mb = db_size / (1024 * 1024)

    return (
        f"**Vector Database Stats**\n"
        f"- Total chunks: {count}\n"
        f"- Total files indexed: {len(filepaths)}\n"
        f"- Database size: {db_size_mb:.1f} MB\n"
        f"- Location: {DB_DIR}\n"
        f"- Collection: {COLLECTION_NAME}\n"
        f"- Embedding model: all-MiniLM-L6-v2 (384 dimensions)\n"
    )


if __name__ == "__main__":
    mcp.run()
