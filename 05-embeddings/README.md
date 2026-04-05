# Phase 5: Embeddings

Embeddings are the bridge between raw text and everything that follows in this repo: semantic search, vector databases, RAG, clustering, retrieval evaluation, and recommendation-style systems.

## What To Learn Here

- How text is mapped into dense vectors
- Why cosine similarity is the default comparison metric
- The difference between word, token, sentence, and sparse embeddings
- When to use local models vs hosted APIs
- How embeddings become a practical search pipeline

## Recommended Order

1. [00_START_HERE.ipynb](00_START_HERE.ipynb)
2. [embeddings_intro.ipynb](embeddings_intro.ipynb)
3. [semantic_similarity.ipynb](semantic_similarity.ipynb)
4. [sentence_transformer_intro.ipynb](sentence_transformer_intro.ipynb)
5. [huggingface_embeddings.ipynb](huggingface_embeddings.ipynb)
6. [openai_embeddings.ipynb](openai_embeddings.ipynb)
7. [semantic_search_intro.ipynb](semantic_search_intro.ipynb)
8. [vector_database_demo.ipynb](vector_database_demo.ipynb)
9. [embedding_comparison.md](embedding_comparison.md)

Optional depth:

- [semantic_textual_similarity_intro.ipynb](semantic_textual_similarity_intro.ipynb)
- [paraphrase_mining_intro.ipynb](paraphrase_mining_intro.ipynb)
- [sparse_encoder_intro.ipynb](sparse_encoder_intro.ipynb)

## Learning Goals

By the end of this phase, you should be able to:

- Explain why embeddings make semantic retrieval possible
- Generate embeddings with both local and API-based workflows
- Compare pooling strategies at a high level
- Build a minimal semantic search flow
- Choose an embedding approach based on quality, latency, and cost constraints

## Prerequisites

- Tokenization fundamentals from [04-token/](../04-token/)
- Basic linear algebra intuition from [03-maths/](../03-maths/)
- Enough Python to run notebooks and inspect arrays

## Good Study Strategy

- Do not treat every notebook as mandatory on the first pass.
- Focus first on concept transfer: similarity, search, and trade-offs.
- Return later for sparse retrieval and model-comparison detail when you start Phase 6 and Phase 7.

## What To Build After This

- A semantic FAQ search system
- A duplicate-detection tool for documents
- A chunk-and-retrieve pipeline that feeds Phase 7 RAG work

## Companion Files

- [QUICKSTART.md](QUICKSTART.md): fast setup and notebook entry points
- [WHATS_NEW.md](WHATS_NEW.md): recent additions in this module
- [embedding_comparison.md](embedding_comparison.md): decision support for local vs hosted embedding stacks
