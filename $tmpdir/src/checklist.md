---
orphan: true
---

# AI/ML Learning Checklist ✅

> Use this as a progress tracker after you read `MASTER_STUDY_GUIDE.md`.
> This checklist is broader than the current quiz system, and some advanced items are intentionally marked as planned.

## START HERE — Essential Reading (Do This First)

- [ ] Done  **[MASTER_STUDY_GUIDE.md](MASTER_STUDY_GUIDE.md)** — Phase-by-phase learning notes, text explanations, and study schedule. Start here.
- [ ] Done  **[REFERENCES.md](REFERENCES.md)** — All videos, GitHub repos, courses, papers, and tools organized by phase.

## 📋 How to Use This Checklist

1. Read [MASTER_STUDY_GUIDE.md](MASTER_STUDY_GUIDE.md) first and choose a track before checking anything off.
2. Use this file as a progress tracker, not as a replacement for the study guide or the phase READMEs.
3. Mark an item done only when you have actually run the material, understood the core idea, and can reuse or explain it.
4. Skip optional depth when needed. Follow your track priorities first, then come back later for breadth.

<div class="checklist-track-focus" data-checklist-track-focus>
<div>
  <span class="checklist-track-focus__eyebrow">Track-aware checklist</span>
  <p class="checklist-track-focus__title">No saved learning path found yet.</p>
  <p class="checklist-track-focus__copy" data-checklist-track-copy>Pick a path on the homepage and this checklist will prioritize the phases that matter most for that track.</p>
</div>
<div class="checklist-track-focus__actions">
  <a class="checklist-track-focus__link" href="index.html#choose-your-track">Choose a path</a>
  <a class="checklist-track-focus__link" href="MASTER_STUDY_GUIDE.html" data-study-guide-link>Open study guide</a>
  <button type="button" class="checklist-track-focus__button" data-reset-checklist-progress>Reset saved progress</button>
  <button type="button" class="checklist-track-focus__button" data-export-checklist-progress>Export progress</button>
  <button type="button" class="checklist-track-focus__button" data-import-checklist-progress>Import progress</button>
  <button type="button" class="checklist-track-focus__button" data-clear-learning-data>Clear all local data</button>
  <input type="file" accept="application/json" data-import-checklist-file hidden>
</div>
<p class="checklist-track-focus__progress" data-checklist-progress-summary>Progress is stored only on this device.</p>
<div class="checklist-track-focus__grid">
  <div class="checklist-track-focus__panel">
    <h3>Core phases</h3>
    <ul data-track-core-list>
      <li>Saved path recommendations will appear here.</li>
    </ul>
  </div>
  <div class="checklist-track-focus__panel">
    <h3>Optional depth</h3>
    <ul data-track-optional-list>
      <li>Stretch topics will appear here after you choose a path.</li>
    </ul>
  </div>
</div>
</div>

## Phase 0: Glossary & Foundations

- [ ] Done  [23-glossary/GLOSSARY.md](../23-glossary/GLOSSARY.md)
- [ ] Done  [00-course-setup/2026_model_landscape.md](../00-course-setup/2026_model_landscape.md) — frontier models, open-weight models, benchmarks as of 2026
- [ ] Done  [31-ai-powered-dev-tools/00_ai_dev_tools_2026.md](../31-ai-powered-dev-tools/00_ai_dev_tools_2026.md) — Cursor, Windsurf, Aider, GitHub Copilot comparison
- [ ] Familiarize yourself with basic ML concepts
- [ ] Understand the difference between supervised/unsupervised learning
- [ ] Done  [MASTER_STUDY_GUIDE.md](MASTER_STUDY_GUIDE.md) — choose your learning track (AI Engineer / ML Engineer / Data Scientist)


## Phase 1: Python & Machine Learning (278 notebooks)

### Python Foundations
- [ ] Done  NumPy tutorials in [02-data-science/1-numpy-examples/](../02-data-science/1-numpy-examples/)
- [ ] Done  pandas tutorials in [02-data-science/2-pandas-examples/](../02-data-science/2-pandas-examples/)
- [ ] Done  data science examples in [02-data-science/3-data-science-examples/](../02-data-science/3-data-science-examples/)

### Scikit-learn Mastery (278 notebooks)
- [ ] Done  [02-data-science/5-scikit-learn/](../02-data-science/5-scikit-learn/) - 278 example notebooks
- [ ] Practice linear regression examples
- [ ] Practice classification examples (SVM, Random Forest, etc.)
- [ ] Practice clustering examples (K-means, DBSCAN, etc.)
- [ ] Practice dimensionality reduction (PCA, t-SNE, etc.)

### Microsoft Labs
- [ ] Done  [Machine Learning for Beginners](https://github.com/microsoft/ML-For-Beginners) (26 lessons)
- [ ] Done  [Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) (20 lessons)

### Projects
- [ ] Build a classification model (e.g., Iris dataset)
- [ ] Build a regression model (e.g., housing prices)
- [ ] Build a clustering project (e.g., customer segmentation)


## Phase 2: Mathematics for ML


### Linear Algebra
- [ ] Done  [03-maths/mml-book/course/01_linear_algebra.ipynb](../03-maths/mml-book/course/01_linear_algebra.ipynb)
- [ ] Done  [03-maths/foundational/01_linear_algebra_fundamentals.ipynb](../03-maths/foundational/01_linear_algebra_fundamentals.ipynb)
- [ ] Done  3Blue1Brown - Essence of Linear Algebra (see [REFERENCES.md](REFERENCES.md))

### Calculus & Derivatives
- [ ] Done  [03-maths/foundational/02_calculus_derivatives.ipynb](../03-maths/foundational/02_calculus_derivatives.ipynb)
- [ ] Done  [03-maths/mml-book/course/04_vector_calculus.ipynb](../03-maths/mml-book/course/04_vector_calculus.ipynb)
- [ ] Watch 3Blue1Brown - Essence of Calculus

### Probability & Statistics
- [ ] Done  [03-maths/foundational/03_probability_statistics.ipynb](../03-maths/foundational/03_probability_statistics.ipynb)
- [ ] Done  [03-maths/mml-book/course/05_probability.ipynb](../03-maths/mml-book/course/05_probability.ipynb)
- [ ] Done  [03-maths/foundational/06_statistical_inference.ipynb](../03-maths/foundational/06_statistical_inference.ipynb)

### Optimization & Gradient Descent
- [ ] Done  [03-maths/foundational/04_gradient_descent.ipynb](../03-maths/foundational/04_gradient_descent.ipynb)
- [ ] Done  [03-maths/mml-book/course/06_optimization.ipynb](../03-maths/mml-book/course/06_optimization.ipynb)

### ISLP Book (13 notebooks)
- [ ] Done  [01_introduction.ipynb](../03-maths/islp-book/01_introduction.ipynb)
- [ ] Done  [02_statistical_learning.ipynb](../03-maths/islp-book/02_statistical_learning.ipynb)
- [ ] Done  [03_linear_regression.ipynb](../03-maths/islp-book/03_linear_regression.ipynb)
- [ ] Done  [04_classification.ipynb](../03-maths/islp-book/04_classification.ipynb)
- [ ] Done  [05_resampling_methods.ipynb](../03-maths/islp-book/05_resampling_methods.ipynb)
- [ ] Done  [06_regularization.ipynb](../03-maths/islp-book/06_regularization.ipynb)
- [ ] Done  [07_nonlinearity.ipynb](../03-maths/islp-book/07_nonlinearity.ipynb)
- [ ] Done  [08_tree_methods.ipynb](../03-maths/islp-book/08_tree_methods.ipynb)
- [ ] Done  [09_support_vector_machines.ipynb](../03-maths/islp-book/09_support_vector_machines.ipynb)
- [ ] Done  [10_deep_learning.ipynb](../03-maths/islp-book/10_deep_learning.ipynb)
- [ ] Done  [11_survival_analysis.ipynb](../03-maths/islp-book/11_survival_analysis.ipynb)
- [ ] Done  [12_unsupervised_learning.ipynb](../03-maths/islp-book/12_unsupervised_learning.ipynb)
- [ ] Done  [13_multiple_testing.ipynb](../03-maths/islp-book/13_multiple_testing.ipynb)

### CS229 Course Notebooks
- [ ] Done  [01_linear_regression.ipynb](../03-maths/cs229-course/course/01_linear_regression.ipynb)
- [ ] Done  [04_logistic_regression.ipynb](../03-maths/cs229-course/course/04_logistic_regression.ipynb)
- [ ] Done  [07_regularization.ipynb](../03-maths/cs229-course/course/07_regularization.ipynb)
- [ ] Done  [06_svm.ipynb](../03-maths/cs229-course/course/06_svm.ipynb)
- [ ] Done  [10_neural_networks_basics.ipynb](../03-maths/cs229-course/course/10_neural_networks_basics.ipynb)

### Video Courses
- [ ] Done  Stanford CS229 (first 10 lectures) - see [22-references/videos/](../22-references/videos/)
- [ ] Watch StatQuest ML fundamentals


## Phase 3: Tokenization (8 notebooks)


### Tokenizer Notebooks
- [ ] Done  [01_tokenizers_quickstart.ipynb](../04-token/01_tokenizers_quickstart.ipynb)
- [ ] Done  [02_tokenizers_training.ipynb](../04-token/02_tokenizers_training.ipynb)
- [ ] Done  [03_advanced_training_methods.ipynb](../04-token/03_advanced_training_methods.ipynb)
- [ ] Done  [06_pipeline_components.ipynb](../04-token/06_pipeline_components.ipynb)
- [ ] Done  [sentencepiece_example.ipynb](../04-token/sentencepiece_example.ipynb)
- [ ] Done  [tiktoken_example.ipynb](../04-token/tiktoken_example.ipynb)
- [ ] Done  [token_exercises.ipynb](../04-token/token_exercises.ipynb)
- [ ] Done  [token_exploration.ipynb](../04-token/token_exploration.ipynb)

### Documentation
- [ ] Done  [README_TOKENIZERS.md](../04-token/README_TOKENIZERS.md)
- [ ] Done  [README_TIKTOKEN.md](../04-token/README_TIKTOKEN.md)
- [ ] Done  [huggingface_tokenizers_guide.md](../04-token/huggingface_tokenizers_guide.md)


## Phase 4: Embeddings (10 notebooks)


### Core Embedding Notebooks
- [ ] Done  [embeddings_intro.ipynb](../05-embeddings/embeddings_intro.ipynb)
- [ ] Done  [sentence_transformer_intro.ipynb](../05-embeddings/sentence_transformer_intro.ipynb)
- [ ] Done  [huggingface_embeddings.ipynb](../05-embeddings/huggingface_embeddings.ipynb)
- [ ] Done  [openai_embeddings.ipynb](../05-embeddings/openai_embeddings.ipynb)

### Similarity & Search
- [ ] Done  [semantic_similarity.ipynb](../05-embeddings/semantic_similarity.ipynb)
- [ ] Done  [semantic_textual_similarity_intro.ipynb](../05-embeddings/semantic_textual_similarity_intro.ipynb)
- [ ] Done  [semantic_search_intro.ipynb](../05-embeddings/semantic_search_intro.ipynb)
- [ ] Done  [paraphrase_mining_intro.ipynb](../05-embeddings/paraphrase_mining_intro.ipynb)

### Advanced Topics
- [ ] Done  [sparse_encoder_intro.ipynb](../05-embeddings/sparse_encoder_intro.ipynb)
- [ ] Done  [vector_database_demo.ipynb](../05-embeddings/vector_database_demo.ipynb)

### Documentation
- [ ] Done  [README.md](../05-embeddings/README.md)
- [ ] Done  [QUICKSTART.md](../05-embeddings/QUICKSTART.md)


## Phase 5: Neural Networks


### Core Notebooks
- [ ] Done  [00_START_HERE.ipynb](../06-neural-networks/00_START_HERE.ipynb) - Overview and learning path
- [ ] Done  [01_neural_network_basics.ipynb](../06-neural-networks/01_neural_network_basics.ipynb) - Neurons, layers, activations, forward pass
- [ ] Done  [02_backpropagation_explained.ipynb](../06-neural-networks/02_backpropagation_explained.ipynb) - Backprop from scratch with NumPy
- [ ] Done  [03_pytorch_fundamentals.ipynb](../06-neural-networks/03_pytorch_fundamentals.ipynb) - Tensors, autograd, training loop in PyTorch
- [ ] Done  [04_attention_mechanism.ipynb](../06-neural-networks/04_attention_mechanism.ipynb) - Self-attention, multi-head attention from scratch
- [ ] Done  [05_transformer_architecture.ipynb](../06-neural-networks/05_transformer_architecture.ipynb) - Full transformer: encoder, decoder, positional encoding

### Math Foundation
- [ ] Done  [03-maths/foundational/07_neural_network_math.ipynb](../03-maths/foundational/07_neural_network_math.ipynb)

### Microsoft Labs
- [ ] Done  [AI for Beginners](https://github.com/microsoft/AI-For-Beginners) (24 lessons)

### Video Courses
- [ ] Done  3Blue1Brown - Neural Networks series (see [REFERENCES.md](REFERENCES.md))
- [ ] Done  Andrej Karpathy - Neural Networks: Zero to Hero (see [REFERENCES.md](REFERENCES.md))
- [ ] Done  MIT 6.S191 - Intro to Deep Learning (see [REFERENCES.md](REFERENCES.md))

### Projects
- [ ] Build a neural network from scratch using only NumPy (no PyTorch)
- [ ] Implement backpropagation by hand for a 2-layer network
- [ ] Train a transformer on a character-level language modeling task


## Phase 6: Vector Databases (7 notebooks)


### Core Notebooks
- [ ] Done  [00_START_HERE.ipynb](../07-vector-databases/00_START_HERE.ipynb)
- [ ] Done  [01_vector_db_basics.ipynb](../07-vector-databases/01_vector_db_basics.ipynb)
- [ ] Done  [02_chroma_guide.ipynb](../07-vector-databases/02_chroma_guide.ipynb)
- [ ] Done  [03_qdrant_guide.ipynb](../07-vector-databases/03_qdrant_guide.ipynb)
- [ ] Done  [04_weaviate_guide.ipynb](../07-vector-databases/04_weaviate_guide.ipynb)
- [ ] Done  [05_milvus_guide.ipynb](../07-vector-databases/05_milvus_guide.ipynb)
- [ ] Done  [06_aurora_pgvector_guide.ipynb](../07-vector-databases/06_aurora_pgvector_guide.ipynb)

### Documentation
- [ ] Done  [README.md](../07-vector-databases/README.md)

### Projects
- [ ] Build a semantic search engine with Chroma
- [ ] Deploy a vector database locally
- [ ] Benchmark different vector databases


## Phase 7: RAG Systems


### Core RAG Notebooks
- [ ] Done  [00_START_HERE.ipynb](../08-rag/00_START_HERE.ipynb) - RAG overview and pipeline architecture
- [ ] Done  [01_basic_rag.ipynb](../08-rag/01_basic_rag.ipynb) - Minimal RAG from scratch
- [ ] Done  [02_document_processing.ipynb](../08-rag/02_document_processing.ipynb) - Chunking strategies and document loaders
- [ ] Done  [03_langchain_rag.ipynb](../08-rag/03_langchain_rag.ipynb) - RAG with LangChain LCEL
- [ ] Done  [04_llamaindex_rag.ipynb](../08-rag/04_llamaindex_rag.ipynb) - RAG with LlamaIndex
- [ ] Done  [05_advanced_retrieval.ipynb](../08-rag/05_advanced_retrieval.ipynb) - HyDE, query expansion, reranking
- [ ] Done  [06_conversation_rag.ipynb](../08-rag/06_conversation_rag.ipynb) - Multi-turn conversational RAG
- [ ] Done  [07_evaluation.ipynb](../08-rag/07_evaluation.ipynb) - RAGAS metrics: faithfulness, relevancy, precision
- [ ] Done  [09_advanced_retrieval.ipynb](../08-rag/09_advanced_retrieval.ipynb) - Parent-child retrieval, multi-vector, ensemble
- [ ] Done  [10_graphrag_visual_rag.ipynb](../08-rag/10_graphrag_visual_rag.ipynb) - GraphRAG and multimodal RAG

### Documentation
- [ ] Done  [08-rag/README.md](../08-rag/README.md)

### Microsoft Labs
- [ ] Done  [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) (18 lessons)
- [ ] Done  [LangChain for Beginners](https://github.com/microsoft/langchain-for-beginners) (6 lessons)

### Projects
- [ ] Build a basic RAG chatbot over a PDF
- [ ] Build a document Q&A system with hybrid search + reranking
- [ ] Implement RAG with RAGAS evaluation metrics
- [ ] Build a fully local RAG (Ollama + ChromaDB, no cloud APIs)


## Phase 8: MLOps


### Core Notebooks
- [ ] Done  [00_START_HERE.ipynb](../09-mlops/00_START_HERE.ipynb) - MLOps lifecycle overview
- [ ] Done  [01_experiment_tracking.ipynb](../09-mlops/01_experiment_tracking.ipynb) - MLflow: log params, metrics, artifacts
- [ ] Done  [02_fastapi_basics.ipynb](../09-mlops/02_fastapi_basics.ipynb) - Build REST API for model serving
- [ ] Done  [03_model_deployment.ipynb](../09-mlops/03_model_deployment.ipynb) - Package and deploy end-to-end
- [ ] Done  [04_docker_ml.ipynb](../09-mlops/04_docker_ml.ipynb) - Containerize ML models with Docker
- [ ] Done  [05_monitoring.ipynb](../09-mlops/05_monitoring.ipynb) - Detect data drift and model degradation
- [ ] Done  [06_ci_cd_pipeline.ipynb](../09-mlops/06_ci_cd_pipeline.ipynb) - GitHub Actions for ML CI/CD
- [ ] Done  [07_cloud_deployment.ipynb](../09-mlops/07_cloud_deployment.ipynb) - Deploy to AWS/GCP/Azure
- [ ] Done  [09_llm_infrastructure.ipynb](../09-mlops/09_llm_infrastructure.ipynb) - vLLM, TGI, LLM serving at scale

### Documentation
- [ ] Done  [09-mlops/README.md](../09-mlops/README.md)

### Video Courses
- [ ] Watch Made With ML - MLOps (free at madewithml.com)
- [ ] Watch Weights & Biases tutorials for experiment tracking

### Projects
- [ ] Deploy a classifier with FastAPI + Docker + GitHub Actions CI/CD
- [ ] Set up MLflow experiment tracking for any training run
- [ ] Deploy a local LLM server with vLLM (OpenAI-compatible endpoint)


## Phase 9: Specializations


- [ ] Done  [10-specializations/README.md](../10-specializations/README.md) for guidance on choosing your path

### Path A: Computer Vision (best for CV Engineer / Multimodal AI roles)
- [ ] Done  [00_START_HERE.ipynb](../10-specializations/computer-vision/00_START_HERE.ipynb) - CV overview and roadmap
- [ ] Done  [01_image_classification.ipynb](../10-specializations/computer-vision/01_image_classification.ipynb) - CNNs, ResNet, EfficientNet with PyTorch
- [ ] Done  [02_object_detection.ipynb](../10-specializations/computer-vision/02_object_detection.ipynb) - YOLO, Faster R-CNN, bounding boxes
- [ ] Done  [03_clip_embeddings.ipynb](../10-specializations/computer-vision/03_clip_embeddings.ipynb) - CLIP for zero-shot image classification + search
- [ ] Done  [04_stable_diffusion.ipynb](../10-specializations/computer-vision/04_stable_diffusion.ipynb) - Diffusion models and image generation
- [ ] Done  [05_multimodal_rag.ipynb](../10-specializations/computer-vision/05_multimodal_rag.ipynb) - RAG over images + text

### Path B: NLP (best for NLP Engineer / Text AI roles)
- [ ] Done  [00_START_HERE.ipynb](../10-specializations/nlp/00_START_HERE.ipynb) - NLP overview
- [ ] Done  [01_ner.ipynb](../10-specializations/nlp/01_ner.ipynb) - Named Entity Recognition with transformers
- [ ] Done  [02_translation.ipynb](../10-specializations/nlp/02_translation.ipynb) - Sequence-to-sequence translation (MarianMT, Helsinki-NLP)
- [ ] Done  [03_summarization.ipynb](../10-specializations/nlp/03_summarization.ipynb) - Abstractive summarization with BART/T5
- [ ] Done  [04_sentiment_analysis.ipynb](../10-specializations/nlp/04_sentiment_analysis.ipynb) - BERT fine-tuning for sentiment
- [ ] Done  [05_information_extraction.ipynb](../10-specializations/nlp/05_information_extraction.ipynb) - Structured extraction from text

### Path C: AI Agents Specialization (best for AI Engineer roles — pairs with Phase 14)
- [ ] Done  [00_START_HERE.ipynb](../10-specializations/ai-agents/00_START_HERE.ipynb) - Agents specialization overview
- [ ] Done  [01_function_calling.ipynb](../10-specializations/ai-agents/01_function_calling.ipynb) - Advanced tool/function calling patterns
- [ ] Done  [02_react_pattern.ipynb](../10-specializations/ai-agents/02_react_pattern.ipynb) - ReAct implementation deep dive
- [ ] Done  [03_langgraph_agents.ipynb](../10-specializations/ai-agents/03_langgraph_agents.ipynb) - Stateful agents with LangGraph
- [ ] Done  [04_multi_agent_systems.ipynb](../10-specializations/ai-agents/04_multi_agent_systems.ipynb) - Multi-agent orchestration patterns
- [ ] Done  [05_memory_state.ipynb](../10-specializations/ai-agents/05_memory_state.ipynb) - Agent memory: short-term, long-term, episodic
- [ ] Done  [06_production.ipynb](../10-specializations/ai-agents/06_production.ipynb) - Production agent: reliability, cost, monitoring

### Microsoft Labs
- [ ] Done  [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)


## Phase 10: Prompt Engineering (6 notebooks) 🔥


### Core Notebooks
- [ ] Done  [00_START_HERE.ipynb](../11-prompt-engineering/00_START_HERE.ipynb)
- [ ] Done  [01_basic_prompting.ipynb](../11-prompt-engineering/01_basic_prompting.ipynb)
- [ ] Done  [02_chain_of_thought.ipynb](../11-prompt-engineering/02_chain_of_thought.ipynb)
- [ ] Done  [03_react_prompting.ipynb](../11-prompt-engineering/03_react_prompting.ipynb)
- [ ] Done  [05_structured_outputs_dspy.ipynb](../11-prompt-engineering/05_structured_outputs_dspy.ipynb) - DSPy: programmatic prompt optimization and structured outputs
- [ ] Done  [06_long_context_strategies.ipynb](../11-prompt-engineering/06_long_context_strategies.ipynb) - long-context prompting, chunking, and retrieval-aware strategies

### Documentation
- [ ] Done  [README.md](../11-prompt-engineering/README.md)

### Video Courses
- [ ] DeepLearning.AI - ChatGPT Prompt Engineering
- [ ] Google Prompting Essentials

### Projects
- [ ] Build a ReAct agent with tools
- [ ] Create a prompt optimization system
- [ ] Build a multi-step reasoning chain


## Phase 11: LLM Fine-tuning (12 notebooks) 🔥


### Core Notebooks
- [ ] Done  [00_START_HERE.ipynb](../12-llm-finetuning/00_START_HERE.ipynb) - Overview, decision framework, hardware guide
- [ ] Done  [01_dataset_preparation.ipynb](../12-llm-finetuning/01_dataset_preparation.ipynb) - Data cleaning, formatting, augmentation
- [ ] Done  [02_supervised_finetuning.ipynb](../12-llm-finetuning/02_supervised_finetuning.ipynb) - SFT with SFTTrainer, Flash Attention 2
- [ ] Done  [03_lora_basics.ipynb](../12-llm-finetuning/03_lora_basics.ipynb) - LoRA fundamentals and configuration
- [ ] Done  [04_qlora_efficient.ipynb](../12-llm-finetuning/04_qlora_efficient.ipynb) - QLoRA, DoRA, RSLoRA deep dive
- [ ] Done  [05_dpo_alignment.ipynb](../12-llm-finetuning/05_dpo_alignment.ipynb) - DPO, RLHF, alignment techniques
- [ ] Done  [06_evaluation.ipynb](../12-llm-finetuning/06_evaluation.ipynb) - BLEU, BERTScore, LLM-as-judge, benchmarks
- [ ] Done  [07_deployment.ipynb](../12-llm-finetuning/07_deployment.ipynb) - vLLM, Ollama, Docker, production serving
- [ ] Done  [08_grpo_reasoning_training.ipynb](../12-llm-finetuning/08_grpo_reasoning_training.ipynb) - GRPO: training reasoning models (DeepSeek-style)
- [ ] Done  [09_unsloth_fast_finetuning.ipynb](../12-llm-finetuning/09_unsloth_fast_finetuning.ipynb) - 2-4x faster fine-tuning with Unsloth
- [ ] Done  [10_quantization_gptq_awq.ipynb](../12-llm-finetuning/10_quantization_gptq_awq.ipynb) - quantization for deployment efficiency
- [ ] Done  [11_rlhf_constitutional_ai.ipynb](../12-llm-finetuning/11_rlhf_constitutional_ai.ipynb) - RLHF, constitutional AI, and alignment framing

### Documentation
- [ ] Done  [README.md](../12-llm-finetuning/README.md)

### Video Courses
- [ ] DeepLearning.AI - Finetuning Large Language Models
- [ ] Hugging Face - Transformers Course

### Projects
- [ ] Fine-tune a model with LoRA on a custom dataset
- [ ] Apply DPO alignment to improve helpfulness
- [ ] Deploy a fine-tuned model with vLLM
- [ ] Compare QLoRA vs DoRA quality vs memory tradeoffs


## Phase 12: Multimodal AI 🔥


### Vision-Language Models
- [ ] Done  [vision-language/01_clip_basics.ipynb](../13-multimodal/vision-language/01_clip_basics.ipynb) - CLIP: aligning image and text embeddings, zero-shot classification

### Image Generation
- [ ] Done  [image-generation/01_stable_diffusion.ipynb](../13-multimodal/image-generation/01_stable_diffusion.ipynb) - Stable Diffusion: latent diffusion, text-to-image, img2img

### Documentation
- [ ] Done  [README.md](../13-multimodal/README.md)


### Projects
- [ ] Build an image search engine: embed images with CLIP, query by text
- [ ] Create a text-to-image generator with custom prompts and negative prompts
- [ ] Build a multimodal chatbot that can describe and discuss images (use GPT-5.4, Gemini 3.1, or Qwen2.5-VL locally)


## Phase 13: Local LLMs (6 notebooks) 🔥


### Core Notebooks
- [ ] Done  [00_START_HERE.ipynb](../14-local-llms/00_START_HERE.ipynb) - local LLM setup overview and learning path
- [ ] Done  [01_ollama_quickstart.ipynb](../14-local-llms/01_ollama_quickstart.ipynb) - Ollama setup and first models
- [ ] Done  [02_open_source_models_overview.ipynb](../14-local-llms/02_open_source_models_overview.ipynb) - Model landscape comparison
- [ ] Done  [03_local_rag_with_ollama.ipynb](../14-local-llms/03_local_rag_with_ollama.ipynb) - Fully local RAG (Ollama + ChromaDB)
- [ ] Done  [04_llm_server_and_api.ipynb](../14-local-llms/04_llm_server_and_api.ipynb) - vLLM, llama.cpp, OpenAI-compatible servers
- [ ] Done  [05_speculative_decoding.ipynb](../14-local-llms/05_speculative_decoding.ipynb) - latency reduction and local inference optimization concepts

### Documentation
- [ ] Done  [README.md](../14-local-llms/README.md)

### Video Courses
- [ ] Matthew Berman - Local LLMs

### Projects
- [ ] Set up Ollama and run Qwen 3 / Llama 4 locally
- [ ] Build a fully local private RAG system over your documents
- [ ] Deploy a local LLM server with OpenAI-compatible API

## Phase 14: AI Agents (9 notebooks) 🔥 HOT TOPIC



### Core Notebooks
- [ ] Done  [01_intro_to_agents.ipynb](../15-ai-agents/01_intro_to_agents.ipynb) - What agents are, ReAct loop, agent anatomy
- [ ] Done  [02_function_calling.ipynb](../15-ai-agents/02_function_calling.ipynb) - Tool/function calling with OpenAI and Anthropic APIs
- [ ] Done  [03_react_pattern.ipynb](../15-ai-agents/03_react_pattern.ipynb) - Reasoning + Acting loop implementation
- [ ] Done  [04_agent_frameworks.ipynb](../15-ai-agents/04_agent_frameworks.ipynb) - LangChain Agents, LangGraph overview
- [ ] Done  [05_multi_agent_systems.ipynb](../15-ai-agents/05_multi_agent_systems.ipynb) - Orchestrator + worker agents, CrewAI, AutoGen
- [ ] Done  [06_mcp_model_context_protocol.ipynb](../15-ai-agents/06_mcp_model_context_protocol.ipynb) - MCP: new standard for AI tool integration (2026)
- [ ] Done  [07_openai_agents_sdk_langgraph.ipynb](../15-ai-agents/07_openai_agents_sdk_langgraph.ipynb) - OpenAI Agents SDK and LangGraph stateful agents
- [ ] Done  [08_reasoning_models.ipynb](../15-ai-agents/08_reasoning_models.ipynb) - o1, o3, DeepSeek R1 - using reasoning models in agents
- [ ] Done  [09_autonomous_agents_2026.ipynb](../15-ai-agents/09_autonomous_agents_2026.ipynb) - State of the art: autonomous agents in 2026

### Documentation
- [ ] Done  [15-ai-agents/README.md](../15-ai-agents/README.md)

### Pre/Post Assessment
- [ ] Done  [pre-quiz.md](../15-ai-agents/pre-quiz.md) before starting
- [ ] Done  [post-quiz.md](../15-ai-agents/post-quiz.md) after finishing

### Projects
- [ ] Build a research agent with web search + calculator + code execution tools
- [ ] Build a multi-agent pipeline: planner → executor → reviewer
- [ ] Build an MCP-powered agent connected to your own data sources
- [ ] Create a LangGraph stateful agent with persistent memory


## Phase 15: Real-Time Streaming AI (4 notebooks) 🔥


### Core Notebooks
- [ ] Done  [01_streaming_responses.ipynb](../20-real-time-streaming/01_streaming_responses.ipynb) - SSE, OpenAI/Anthropic streaming, TTFT/TPS metrics
- [ ] Done  [02_websocket_connections.ipynb](../20-real-time-streaming/02_websocket_connections.ipynb) - WebSocket protocol, connection management, auth
- [ ] Done  [03_real_time_rag.ipynb](../20-real-time-streaming/03_real_time_rag.ipynb) - Streaming RAG, progressive context, citation tracking
- [ ] Done  [04_production_streaming.ipynb](../20-real-time-streaming/04_production_streaming.ipynb) - Rate limiting, circuit breakers, Prometheus, load testing

### Documentation
- [ ] Done  [README.md](../20-real-time-streaming/README.md)

### Projects
- [ ] Build a ChatGPT-style streaming chat interface with FastAPI + SSE
- [ ] Create a real-time RAG system that streams sources then answers
- [ ] Deploy a production streaming server with monitoring dashboards


## Supplementary Phases (Do These Alongside or After Core Track)


### Model Evaluation — [16-model-evaluation/](../16-model-evaluation/)


- [ ] Done  [01_classification_metrics.ipynb](../16-model-evaluation/01_classification_metrics.ipynb) - Precision, recall, F1, ROC-AUC, confusion matrices
- [ ] Done  [02_regression_metrics.ipynb](../16-model-evaluation/02_regression_metrics.ipynb) - RMSE, MAE, R², residual analysis
- [ ] Done  [03_llm_evaluation.ipynb](../16-model-evaluation/03_llm_evaluation.ipynb) - BLEU, BERTScore, RAGAS, LLM-as-judge
- [ ] Done  [04_bias_fairness.ipynb](../16-model-evaluation/04_bias_fairness.ipynb) - Demographic parity, equal opportunity, disparate impact
- [ ] Done  [05_model_comparison.ipynb](../16-model-evaluation/05_model_comparison.ipynb) - Statistical tests for model comparison (paired t-test, McNemar)
- [ ] Done  [16-model-evaluation/README.md](../16-model-evaluation/README.md)
- [ ] Done  [16-model-evaluation/assignment.md](../16-model-evaluation/assignment.md)


### Debugging & Troubleshooting — [17-debugging-troubleshooting/](../17-debugging-troubleshooting/)


- [ ] Done  [01_debugging_workflow.ipynb](../17-debugging-troubleshooting/01_debugging_workflow.ipynb) - Systematic debugging: data → model → serving
- [ ] Done  [02_data_issues.ipynb](../17-debugging-troubleshooting/02_data_issues.ipynb) - Missing values, class imbalance, label noise, distribution shift
- [ ] Done  [03_performance_profiling.ipynb](../17-debugging-troubleshooting/03_performance_profiling.ipynb) - CPU/GPU profiling, memory leaks, training speed bottlenecks
- [ ] Done  [04_model_debugging.ipynb](../17-debugging-troubleshooting/04_model_debugging.ipynb) - Loss curves, gradient issues, overfitting diagnosis
- [ ] Done  [05_error_analysis.ipynb](../17-debugging-troubleshooting/05_error_analysis.ipynb) - Confusion matrix deep dive, error slicing, failure mode analysis
- [ ] Done  [17-debugging-troubleshooting/README.md](../17-debugging-troubleshooting/README.md)


### Low-Code AI Tools — [18-low-code-ai-tools/](../18-low-code-ai-tools/)



- [ ] Done  [01_gradio_basics.ipynb](../18-low-code-ai-tools/01_gradio_basics.ipynb) - Build ML demos in minutes with Gradio
- [ ] Done  [02_streamlit_apps.ipynb](../18-low-code-ai-tools/02_streamlit_apps.ipynb) - Data apps with Streamlit
- [ ] Done  [03_huggingface_spaces.ipynb](../18-low-code-ai-tools/03_huggingface_spaces.ipynb) - Deploy your demo for free on HuggingFace Spaces
- [ ] Done  [04_automl_platforms.ipynb](../18-low-code-ai-tools/04_automl_platforms.ipynb) - AutoML with H2O, AutoSklearn, TPOT
- [ ] Done  [05_end_to_end_project.ipynb](../18-low-code-ai-tools/05_end_to_end_project.ipynb) - Full project: model → Gradio → HF Spaces deployment
- [ ] Done  [18-low-code-ai-tools/README.md](../18-low-code-ai-tools/README.md)



### AI Safety & Red Teaming — [19-ai-safety-redteaming/](../19-ai-safety-redteaming/)



- [ ] Done  [01_prompt_security.ipynb](../19-ai-safety-redteaming/01_prompt_security.ipynb) - Prompt injection attacks and defenses
- [ ] Done  [02_content_moderation.ipynb](../19-ai-safety-redteaming/02_content_moderation.ipynb) - Filtering harmful content with classifiers and LLM guards
- [ ] Done  [03_pii_privacy.ipynb](../19-ai-safety-redteaming/03_pii_privacy.ipynb) - PII detection, redaction, and privacy-preserving ML
- [ ] Done  [04_bias_fairness.ipynb](../19-ai-safety-redteaming/04_bias_fairness.ipynb) - Bias detection in LLM outputs, debiasing techniques
- [ ] Done  [05_red_teaming.ipynb](../19-ai-safety-redteaming/05_red_teaming.ipynb) - Systematic red teaming: jailbreaks, adversarial prompts, evaluation
- [ ] Done  [19-ai-safety-redteaming/README.md](../19-ai-safety-redteaming/README.md)
- [ ] Done  [19-ai-safety-redteaming/quiz.md](../19-ai-safety-redteaming/quiz.md)


## 🧪 Hands-On Labs

### Microsoft Labs (100+ lessons)
- [ ] Done  [22-references/microsoft-labs/](../22-references/microsoft-labs/)
- [ ] Complete at least 3 full courses
- [ ] Build all course projects

### Video Courses (50+ channels)
- [ ] Done  [22-references/videos/](../22-references/videos/)
- [ ] Done  Stanford CS229 (full course) — see [REFERENCES.md](REFERENCES.md) for direct links
- [ ] Done  Andrej Karpathy - Build GPT from scratch — see [REFERENCES.md](REFERENCES.md)
- [ ] Done  3Blue1Brown neural network series — see [REFERENCES.md](REFERENCES.md)

### Cloud Platforms
- [ ] Done  [22-references/cloud-platforms/](../22-references/cloud-platforms/)
- [ ] Complete AWS SageMaker tutorials
- [ ] Try Google Cloud AI Studio
- [ ] Deploy a model on cloud


## 🎓 MDTP Framework - Comprehensive Knowledge Map


### M - Models

#### M0. Statistical Thinking & Intuition
- [ ] Probability, random variables, distributions
- [ ] Model vs. reality, digital twins
- [ ] Structure and causality
- [ ] Inference vs generalization (Breiman's "Two Cultures")
- [ ] Observation, experiment and experiment design
- [ ] Treatment and treatment effects
- [ ] Measurement errors and missing data

#### M1. Statistical Inference
- [ ] Data generating process, sample vs population
- [ ] Sampling techniques and inference
- [ ] Frequentist and Bayesian views
- [ ] Measuring model quality and performance
- [ ] Model lifecycle, data and model drift

#### M2. Econometrics
- [ ] Cross-section, time series, panel and spatial data
- [ ] Linear regression and OLS
- [ ] Violation of OLS assumptions (Peter Kennedy's 10 Commandments)
- [ ] Estimation techniques: OLS, GMM, maximum likelihood, Bayesian

#### M4. Classic Machine Learning
- [ ] Classification, regression, clustering
- [ ] Dimensionality reduction, decision trees
- [ ] Support vector machines and discriminant analysis
- [ ] Model selection and performance evaluation

#### M5. Neural Networks & Deep Learning
- [ ] Simple perceptron and NN construction
- [ ] Gradient descent, backpropagation, regularization
- [ ] Traditional architectures (feed-forward, CNN, RNN, GAN, transformers)
- [ ] **Embeddings and vector representations** (word2vec, sentence-transformers)
- [ ] **Tokenization** (BPE, WordPiece, SentencePiece)
- [ ] **Attention mechanism** (self-attention, multi-head attention)
- [ ] **Mixture of Experts (MoE)** architecture

#### M6. NLP, CV and Advanced Subfields
- [ ] Classic NLP (Jurafsky and Martin)
- [ ] **Large Language Models** (GPT-4, Claude, LLaMA, Gemini)
- [ ] Transformer architecture, prompt engineering
- [ ] RAGs and fine-tuning
- [ ] **Instruction tuning and alignment** (RLHF, DPO, constitutional AI)
- [ ] **In-context learning** (few-shot, zero-shot, chain-of-thought)
- [ ] **Model compression** (quantization: 4-bit, 8-bit; distillation; LoRA/QLoRA)
- [ ] **Hallucination detection and mitigation**
- [ ] Computer vision fundamentals
- [ ] **Multimodal models** (CLIP, GPT-4V, vision-language)
- [ ] **Diffusion models** (Stable Diffusion, DALL-E, Midjourney)

#### M9. Modern AI Architectures (2020-2025)
- [ ] **Transformer variants** (BERT, GPT, T5)
- [ ] **Vision Transformers (ViT)** for image understanding
- [ ] **State Space Models** (Mamba, structured state spaces)
- [ ] **Retrieval-augmented architectures** (RAG systems)
- [ ] **Sparse models and efficient transformers** (Sparse Transformers, Longformer)

### D - Data

#### D1. Data Sources
- [ ] Data collection, observation vs experiment
- [ ] Physical sensors
- [ ] Proprietary vs open data, official statistics
- [ ] Data distribution and providers
- [ ] Data protection and privacy

#### D2. Data Analysis
- [ ] EDA and descriptive statistics
- [ ] Graphs, visualizations, dashboards
- [ ] Analysis as a DAG
- [ ] Reproducible research

#### D3. Data Engineering
- [ ] Structured data, serialization formats (CSV, JSON, XML)
- [ ] SQL for tabular data
- [ ] Dataframes (pandas, polars)
- [ ] Processing large datasets (MapReduce, Hadoop, Spark)
- [ ] Everything as a vector: text, images, sound, video
- [ ] Data ingestion, transform, storage, retrieval
- [ ] **Vector databases** (Pinecone, Weaviate, ChromaDB, pgvector)
- [ ] **Embedding storage and retrieval** (semantic search, HNSW, FAISS)
- [ ] **Real-time data streaming** (Kafka, Flink)
- [ ] **Data versioning** (DVC, LakeFS)

#### D4. Pipelines & Orchestration
- [ ] Modelling pipelines (Airflow)
- [ ] Model delivery (FastAPI)
- [ ] **MLOps platforms** (MLflow, Weights & Biases, Kubeflow, Neptune)
- [ ] **Feature stores** (Feast, Tecton)
- [ ] **A/B testing and experimentation frameworks**
- [ ] **Model versioning and registry**

#### D5. Data Management
- [ ] Data quality assurance
- [ ] Corporate data governance (DMBOK)

### T - Tools (Code & Infrastructure)

#### T0. Writing Code
- [ ] Linux and command line (local and remote)
- [ ] Software development practices (version control, unit testing, APIs)
- [ ] DevOps, product thinking and metrics
- [ ] Python, R, Julia ecosystems

#### T1. Software Tools
- [ ] Statistical packages and documentation
- [ ] R for statistics, scikit-learn for ML
- [ ] PyTorch, TensorFlow, Keras for neural networks
- [ ] **LLM frameworks** (LangChain, LlamaIndex, Haystack)
- [ ] **Hugging Face ecosystem** (Transformers, Datasets, Accelerate, PEFT)
- [ ] **Vector database libraries** (FAISS, Annoy, hnswlib)
- [ ] **Modern ML frameworks** (JAX, XGBoost, LightGBM, CatBoost)

#### T2. Cloud & Computing Infrastructure
- [ ] Cloud services and infrastructure provisioning
- [ ] **GPU computing** (CUDA, distributed training, multi-GPU)
- [ ] **Container orchestration** (Docker, Kubernetes for ML)
- [ ] **Serverless ML** (AWS Lambda, Modal, Banana, Replicate)
- [ ] **Edge deployment** (TensorFlow Lite, ONNX Runtime)
- [ ] **LLM hosting** (vLLM, TGI, Ollama for local models)

#### T2.1. Understanding the Cloud (Business Perspective)
- [ ] Client-server foundation and architecture
- [ ] Virtualization and resource efficiency
- [ ] Storage solutions (S3, block, object storage)
- [ ] Containerization and orchestration (Kubernetes)
- [ ] PaaS and serverless (Lambda)
- [ ] Networking: zones, CDNs, load balancing
- [ ] On-premise vs cloud tradeoffs
- [ ] Economics of cloud computing
- [ ] Cloud providers: AWS, GCP, Azure
- [ ] Data center energy efficiency

#### T2.2. Databases & Storage
- [ ] HDD vs SSD vs Cloud (S3) tradeoffs
- [ ] File systems (HDFS)
- [ ] **Relational databases** (PostgreSQL, MySQL)
- [ ] **NoSQL types**: Key-Value, Document, Column, Graph
- [ ] **Vector databases** (Pinecone, Weaviate, ChromaDB)
- [ ] Time series databases (InfluxDB, TimescaleDB)
- [ ] Large data processing (MapReduce, Hadoop, Spark)
- [ ] Search databases (ElasticSearch, Solr)
- [ ] Data warehouses (Snowflake, Databricks, BigQuery)
- [ ] Database theory: ACID, CAP theorem, BASE
- [ ] OLAP vs OLTP

#### T2.3. Data Engineering Tools
- [ ] Data engineering lifecycle: Generation → Storage → Ingestion → Transformation → Serving
- [ ] **Workflow orchestration** (Airflow, Prefect, Dagster)
- [ ] **MLFlow** for ML lifecycle management
- [ ] Modern data stack components
- [ ] Ingestion: Fivetran, Airbyte, Stitch
- [ ] Transform: dbt, Spark
- [ ] BI tools: Looker, Tableau, PowerBI

#### T3. Development Tools & Environment
- [ ] **Jupyter ecosystem** (JupyterLab, notebooks, extensions)
- [ ] **IDEs and AI coding assistants** (VS Code, Cursor, GitHub Copilot)
- [ ] **Experiment tracking** (Weights & Biases, Neptune, Comet)
- [ ] **Data labeling tools** (Label Studio, Prodigy, Scale AI)

### P - Productisation

#### P1. Productisation & Business Value
- [ ] Risk, learning and experimentation in business context
- [ ] Modelling hypothesis and expected outcomes
- [ ] Data-model-action workflows
- [ ] Team roles and hiring
- [ ] Measuring business outcomes and ML impact
- [ ] **RAG systems** architecture and implementation
- [ ] **Prompt engineering** as systematic discipline
- [ ] **AI agent frameworks** (AutoGPT, LangChain agents, function calling)
- [ ] **Model monitoring** (drift detection, performance tracking)
- [ ] **Cost optimization** (token usage, caching, batch processing)

#### P1.1. ML Project Lifecycle Framework
- [ ] **A. Identify Business Case** - Hypothesis and expected ROI
- [ ] **B. Create Adequate Model** - Value chain representation
- [ ] **C. State Proposed Change** - Why, what, how, success criteria
- [ ] **D. Prove with Experiments** - Run controlled tests
- [ ] **E. Scale or Pivot** - Based on results
- [ ] **F. Continuous Improvement** - Feedback loops

#### P1.2. Data Team Roles & Responsibilities
- [ ] Understand different role functions:
  - [ ] Full-Stack Data Scientist
  - [ ] Data Scientist/Modeler
  - [ ] Data Engineer/Architect
  - [ ] Machine Learning Engineer
  - [ ] Research Scientist
  - [ ] Business Analyst
  - [ ] Product Manager

#### P1.3. Production Challenges
- [ ] Technical: Data quality, model drift, infrastructure failures
- [ ] Organizational: Silos, unclear responsibilities
- [ ] Business: Unclear success criteria, ROI validation

#### P2. Applications, Domains & Cases
- [ ] Recommender systems (RecSys)
- [ ] Clinical trials
- [ ] Quality control and industrial automation
- [ ] Finance applications
- [ ] **Conversational AI and chatbots**
- [ ] **Code generation** (GitHub Copilot, code assistants)
- [ ] **Document intelligence** (Q&A, summarization, extraction)
- [ ] **Search and information retrieval** (semantic search, hybrid search)

#### P3. Society Impacts & Regulation
- [ ] Fairness, biases, equity, ethics
- [ ] Grounds for AI regulation and policy
- [ ] **AI safety and alignment** (value alignment, red teaming)
- [ ] **Prompt injection and security vulnerabilities**
- [ ] **Environmental impact** (carbon footprint of training)
- [ ] **AI watermarking and detection**
- [ ] **Copyright and IP issues** with generative AI


## 📚 Documentation & Resources

- [ ] Done  [22-references/README.md](../22-references/README.md) - All hands-on labs
- [ ] Done  [REFERENCES.md](REFERENCES.md) - Full curated video, repo, and paper list


## 🎯 Final Projects (Build Your Portfolio)

### Beginner Projects
- [ ] Iris classification (scikit-learn)
- [ ] House price prediction (regression)
- [ ] Customer segmentation (clustering)

### Intermediate Projects
- [ ] Sentiment analysis (NLP)
- [ ] Image classifier (CNN)
- [ ] Recommendation system (collaborative filtering)

### Advanced Projects
- [ ] RAG chatbot for your documents
- [ ] Fine-tuned LLM for specific domain
- [ ] Multimodal AI application (vision + language)

### Production Projects
- [ ] Deploy ML model with FastAPI + Docker
- [ ] Build CI/CD pipeline for ML
- [ ] Create monitoring dashboard for ML models


## ⭐ Completion Milestones


- [ ] **Foundation Complete** - Phases 0-2 done (Python, Math, ML basics)
- [ ] **Modern AI Stack** - Phases 3-6 done (Tokenization, Embeddings, Neural Nets, Vector DBs)
- [ ] **Production Ready** - Phases 7-9 done (RAG, MLOps, Specializations)
- [ ] **Cutting-Edge AI** - Phases 10-13 done (Prompt Engineering, Fine-tuning, Multimodal, Local LLMs)
- [ ] **Advanced Research** - Phases 24-25 done (Advanced Math, Deep Learning Research)
- [ ] **Portfolio Built** - 5+ projects deployed and documented
- [ ] **Certified** - At least 1 ML certification (AWS, Google, Azure, or DeepLearning.AI)


## Phase 24: Advanced Deep Learning (RESEARCH LEVEL) 🔬



### Generative Models - Advanced
- [ ] Done  [01_gan_mathematics.ipynb](../24-advanced-deep-learning/01_gan_mathematics.ipynb) - GAN theory and vanilla implementation
- [ ] Done  [02_wgan_theory_implementation.ipynb](../24-advanced-deep-learning/02_wgan_theory_implementation.ipynb) - Wasserstein GAN with gradient penalty
- [ ] Done  [03_variational_autoencoders_advanced.ipynb](../24-advanced-deep-learning/03_variational_autoencoders_advanced.ipynb) - VAE theory, ELBO, β-VAE
- [ ] Done  [04_neural_ode.ipynb](../24-advanced-deep-learning/04_neural_ode.ipynb) - Neural ODEs and continuous normalizing flows

### Advanced Topics (To Be Implemented)
- [ ] Info-GAN and Conditional GANs
- [ ] Bayesian GANs
- [ ] Advanced VAE architectures
- [ ] 3D Vision and NeRF
- [ ] Vision Transformers (ViT)
- [ ] Advanced Transformer architectures



## Phase 25: Reinforcement Learning (7 notebooks)


### Core Notebooks
- [ ] Done  [00_START_HERE.ipynb](../25-reinforcement-learning/00_START_HERE.ipynb) - RL fundamentals and overview
- [ ] Done  [01_markov_decision_processes.ipynb](../25-reinforcement-learning/01_markov_decision_processes.ipynb) - MDP theory and Bellman equations
- [ ] Done  [02_q_learning.ipynb](../25-reinforcement-learning/02_q_learning.ipynb) - tabular RL and temporal-difference learning
- [ ] Done  [03_deep_q_networks.ipynb](../25-reinforcement-learning/03_deep_q_networks.ipynb) - function approximation with deep networks
- [ ] Done  [04_policy_based_methods.ipynb](../25-reinforcement-learning/04_policy_based_methods.ipynb) - policy gradients and actor-critic ideas
- [ ] Done  [05_advanced_topics_applications.ipynb](../25-reinforcement-learning/05_advanced_topics_applications.ipynb) - broader RL applications and advanced concepts
- [ ] Done  [06_practical_exercises.ipynb](../25-reinforcement-learning/06_practical_exercises.ipynb) - hands-on RL practice

### Advanced Topics
- [ ] Policy gradients and actor-critic methods (planned)
- [ ] Deep reinforcement learning (planned)
- [ ] Multi-agent reinforcement learning (planned)



## Phase 26: Time Series Analysis & Forecasting (7 notebooks)


### Core Notebooks
- [ ] Done  [00_START_HERE.ipynb](../26-time-series-analysis/00_START_HERE.ipynb) - Time series fundamentals
- [ ] Done  [01_time_series_fundamentals.ipynb](../26-time-series-analysis/01_time_series_fundamentals.ipynb) - decomposition, autocorrelation, and forecasting basics
- [ ] Done  [02_classical_statistical_methods.ipynb](../26-time-series-analysis/02_classical_statistical_methods.ipynb) - ARIMA-style and statistical forecasting methods
- [ ] Done  [03_facebook_prophet.ipynb](../26-time-series-analysis/03_facebook_prophet.ipynb) - Prophet for business forecasting workflows
- [ ] Done  [04_deep_learning_time_series.ipynb](../26-time-series-analysis/04_deep_learning_time_series.ipynb) - deep learning approaches for forecasting
- [ ] Done  [05_advanced_techniques_applications.ipynb](../26-time-series-analysis/05_advanced_techniques_applications.ipynb) - advanced forecasting and applied scenarios
- [ ] Done  [06_practical_applications_exercises.ipynb](../26-time-series-analysis/06_practical_applications_exercises.ipynb) - hands-on forecasting exercises

### Advanced Topics
- [ ] GARCH models for volatility (planned)
- [ ] State space models (planned)
- [ ] Bayesian time series (planned)



## Phase 27: Causal Inference & Experimental Design (7 notebooks)


### Core Notebooks
- [ ] Done  [00_START_HERE.ipynb](../27-causal-inference/00_START_HERE.ipynb) - Causal inference overview
- [ ] Done  [01_causal_fundamentals.ipynb](../27-causal-inference/01_causal_fundamentals.ipynb) - causal questions, estimands, and foundational ideas
- [ ] Done  [02_causal_graphs_dags.ipynb](../27-causal-inference/02_causal_graphs_dags.ipynb) - DAGs and causal graphs
- [ ] Done  [03_experimental_design.ipynb](../27-causal-inference/03_experimental_design.ipynb) - RCT design and analysis
- [ ] Done  [04_observational_methods.ipynb](../27-causal-inference/04_observational_methods.ipynb) - Propensity scores, matching
- [ ] Done  [05_advanced_topics_applications.ipynb](../27-causal-inference/05_advanced_topics_applications.ipynb) - advanced topics, confounding, and applied causal analysis
- [ ] Done  [06_quasi_experimental_designs.ipynb](../27-causal-inference/06_quasi_experimental_designs.ipynb) - RDD, DiD, IV methods

### Advanced Topics
- [ ] Mediation analysis (planned)
- [ ] Causal discovery (planned)
- [ ] Difference-in-differences with multiple periods (planned)



## 🏆 Completion Milestones

- [ ] **Foundation Complete** - Phases 0-2 done (Python, Math, ML basics)
- [ ] **Modern AI Stack** - Phases 3-6 done (Tokenization, Embeddings, Neural Nets, Vector DBs)
- [ ] **Production Ready** - Phases 7-9 done (RAG, MLOps, Specializations)
- [ ] **Cutting-Edge AI** - Phases 10-13 done (Prompt Engineering, Fine-tuning, Multimodal, Local LLMs)
- [ ] **Research Mastery** - Phases 24-27 done (Advanced Deep Learning, Reinforcement Learning, Time Series, Causal Inference)
- [ ] **Portfolio Built** - 5+ projects deployed and documented
- [ ] **Certified** - At least 1 ML certification (AWS, Google, Azure, or DeepLearning.AI)


## 🎓 Next Steps After Completion

- [ ] Contribute to open-source ML projects (start with docs/issues on popular repos)
- [ ] Write blog posts about what you built (1 post per major project)
- [ ] Mentor others in AI/ML
- [ ] Build your own AI product
- [ ] Apply for ML/AI jobs or research positions
- [ ] Continue learning (AI never stops evolving!)
- [ ] Read and implement papers from top conferences (NeurIPS, ICML, ICLR)
- [ ] Contribute to ML research


## Career Readiness Milestones


- [ ] **Resume Updated** — AI/ML skills section added, projects listed
- [ ] **LinkedIn Updated** — Headline reflects AI/ML focus, summary updated
- [ ] **GitHub Polished** — 4+ repos pinned, each with README + demo
- [ ] **Project 1 Live** — RAG chatbot deployed (HF Spaces / Render)
- [ ] **Project 2 Live** — Fine-tuned model with evaluation results documented
- [ ] **Project 3 Live** — MLOps pipeline or AI agent
- [ ] **Interview Prep** — Practiced 10 core ML concept questions
- [ ] **Coding Practice** — Solved 20+ pandas/sklearn coding problems
- [ ] **System Design** — Practiced 3 ML system design scenarios
- [ ] **Networking** — Connected with 10+ AI engineers on LinkedIn
- [ ] **Applications Sent** — Applied to 20+ positions


## Key Resources Quick Links





