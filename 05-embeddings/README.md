# Embeddings

Dense vector representations are the bridge between raw text and everything that follows in this repo: semantic search, vector databases, RAG, clustering, retrieval evaluation, and recommendation-style systems.

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

## Recent 2026 Topics To Keep In View

This phase is centered on text embeddings, but production retrieval systems in 2026 also depend on:

- Multimodal embeddings such as CLIP and SigLIP for image-text retrieval
- Dense + sparse + reranker pipelines instead of dense-only retrieval
- Late-interaction retrieval patterns such as ColBERT-style reranking
- Local embedding stacks for privacy-sensitive workflows alongside hosted APIs
- Embedding versioning, drift tracking, and compression for large-scale vector systems

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
- A chunk-and-retrieve pipeline that feeds Phase 8 RAG work
- An image-text search prototype using multimodal embeddings
- A hybrid retrieval stack with a reranker on top of dense retrieval

## Companion Files

- [QUICKSTART.md](QUICKSTART.md): fast setup and notebook entry points
- [embedding_comparison.md](embedding_comparison.md): decision support for local vs hosted embedding stacks

## What Comes Next

- Continue to [../07-vector-databases/README.md](../07-vector-databases/README.md) to learn how embeddings become retrievable infrastructure.
- Continue to [../08-rag/README.md](../08-rag/README.md) to use embeddings inside full retrieval systems.
- Continue to [../13-multimodal/README.md](../13-multimodal/README.md) later if you want image-text and cross-modal embedding systems.
