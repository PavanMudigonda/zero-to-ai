**Machine Learning (ML) Topic Guide: Statistical Models, Data, Tools and Productisation (MDTP)**  
© Evgeny Pogrebnyak ([e.pogrebnyak@gmail.com](mailto:e.pogrebnyak@gmail.com)), October 2024, v1.2.0 (draft).

This guide takes a broad view of methods applicable in statistical modelling followed by ways to manage the data and create data-driven computing systems that are useful in business. 

* In modeling space we get to hear about the AI hype cycle a lot but much less about other models (not deep learning and not targeting human cognitive ability) that are still very practical and even more reliable in solving real-world problems.   
* It is not only the model choice that matters but also how you obtain and process the data – for example is it just an fixed dataset of observations or the data may come from a controlled experiment; are you happy with data quality and can you work witht the data respecting privacy restrictions.  
* The computer systems, both hardware and software, that allow to process the data and run a model vary in size and complexity.   
* Lastly, superb data, model and pipelines do not guarantee where the modelling results will be applied meaningfully – is just someone taking a look at the dashboard or there are “actuators” – the people, business processes, machinery or robots that are controlled by the model outcome.


Using this topic guide you can probably touch upon what an  experienced statistic modeller, a data engineer, a software developper and a product manager or domain expert would collectively know and apply in a machine learning or a data modelling project.   
This stack of skills can be explored in several directions. On a direction from theory to practice you can pose a question “What are the capabilities or theortic limits of predictions and forecasts that we can possibly make? Is this computation really possible or we will be lying to ourselves when attempting it?”  
On a direction from pracitcal questions to methodology there is a question “Can we identify a business case that is well answered by the model and the data that we can obtain?” In the middle of a skill stack there sits a question “How can we make an affordable and maintainable computer system for this computation project or task?” 

The guide has a modular structure that should help cherry pick and proritise learning areas for three groups of readers (a) the [new learners](https://trics.me/beginner.html) at the start of a career journey; (b) reviewers – people with longer previous careers, that are related to modelling or not; and (c) carreer switchers who have expertise in one domain and would want to migrate to another, eg from econometrics to productisation or from software engineering to machine learning.  
The topic list is organised into sections below:

* M (models): probability, statistics, econometrics, machine learning, deep learning and other modelling areas.  
* D (data): data engineering, data management and data governance.  
* T (tools): software tools, databases and computing infrastructure.  
* P (productisation): ok, now you have the data, a model and a server running, but what’s the benefit?

The author would be grateful to comments about the structure, the contents and usefulness of this guide to the readers as well as ideas for corrections and improvements. This guide is accompanied with another list of notes called [MLMW (Machine Learning My Way](https://docs.google.com/document/d/e/2PACX-1vT9ZkQJDDimZuPgBb7_hUJ40lm8LhqzL45HwIcYRYHw0AQkwA7pcqg0AIE7Gwf3QpAnZ34-BrFrWovO/pub)) that also exists as a draft. In the future releases MLMW would be a more dense guide exclusively for machine learning concepts and modelling techniques while MDTP will cover data, code and productisation in more detail. 

The table below summarises steps in the extended modelling process, starting from a modelling idea to finalising the business or society benefits.  

| Section / steps | Typical questions | An example |
| :---- | :---- | :---- |
| Idea | Why bother collecting data and modelling in this area? | Everyone else is doing this (usually bad). Space for improvements (good). |
| Models | What kind formulas do I need? What are their limitations? | Linear regression and OLS. |
| Data – provenance | How is the data collected? Does this reflect what we need to know?  | Some said the data is valid. |
| Data – artifacts and datasets | Do we have the data? Can we store and manage this data?  | There is a CSV file or a database that allows a SQL query. |
| Software | What software should I use?  | Python pandas and statmodels libraries. |
|  | How do I write my own code? | In a Jupyter notebook. |
| Infrastructure | Where do I put my code and data? | Laptop or Google Colab. |
| Teams and roles | Who is working on a project?  | Just myself.  |
| Business value | Does the modlling result provide any improvements for the business? | Adjust goods purchases to seasonality. |
| Society benefits | Are there any gains for everyone not just a specific company? | Rise in productivity in agrofood sector. Improved food security. |

# 

# **M. Models** {#m.-models}

~~Non-essential topics are strike-through~~

## **M0. Statistical thinking and intuition**	 {#m0.-statistical-thinking-and-intuition}

- [ ] Probability, random variables, distributions.  
- [ ] Model vs. reality. Digital twins.   
- [ ] Structure and causality.   
- [ ] Inference (econometrics) vs generalisation (machine learning). Breiman's *[Two Cultures](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full)* (2001) and rebuttals.  
- [ ] Observation, experiment and experiment design.  
- [ ] Treatment and treatment effects.   
- [ ] Measurement errors and missing data.

## **M1. Statistical inference** {#m1.-statistical-inference}

- [ ] Data generating process, sample vs population.  
- [ ] Sampling techniques and inference. Statistical model.   
- [ ] Frequentist and Bayesian views of a statistical model.  
- [x] ~~Modelling tradeoffs and “no free lunch”.~~  
- [ ] Measuring model quality and performance.  
- [ ] Model lifecyle, data and model drift.

## **M2. Econometrics** {#m2.-econometrics}

- [ ] Cross-section, time series, panel and spatial data.   
- [ ] Linear regression and ordinary least squares (OLS).  
- [ ] Violation of OLS assumptions. [*Peter Kennedy*](https://en.wikipedia.org/wiki/Peter_Kennedy_\(economist\)) textbook and the [*10 Commandments*](https://www.principlesofeconometrics.com/poe5/writing/kennedy.pdf).  
- [x] ~~Difference-in-differences, instrumental variables, regression discontinuity.~~  
- [x] ~~Time series. Seasonal adjustment, smoothing, filtering.~~  
- [x] ~~Systems of equations.~~  
- [ ] Estimation techniques: OLS and varieties, GMM, maximum likelihood, Bayesian estimates.

## **M3. Bayesian modeling and causal inference.** {#m3.-bayesian-modeling-and-causal-inference.}

- [x] ~~Bayesian modeling and probabilistic programming.~~  
- [x] ~~Causal inference and do-notation.~~

## **M4. Classic machine learning.** {#m4.-classic-machine-learning.}

- [ ] Tasks: classification, regression, clustering, dimensionality reduction, decision trees, support vector machines and discriminant analysis.  
- [ ] Criteria for model selection and performance evaluation.   
- [x] ~~Statistical learning theory (loss, theoretical and empirical risk, PAC-Bayes)~~  
- [x] ~~Forecast combination, choosing forecasts and AutoML.~~ 

## **M5. Neural nets (NN) and deep learning.** {#m5.-neural-nets-(nn)-and-deep-learning.}

- [ ] Simple perceptron and NN construction (gradient descent, backpropagation, regularization).  
- [ ] Traditional NN architectures (feed-forward, convolutional, recurrent, generative аdversarial, transformers).  
- [ ] **Embeddings and vector representations** (word2vec, sentence-transformers, dense vectors for semantic meaning).  
- [ ] **Tokenization** (BPE, WordPiece, SentencePiece for modern LLMs).  
- [ ] **Attention mechanism** (self-attention, multi-head attention - foundational for transformers).  
- [ ] **Mixture of Experts (MoE)** architecture for efficient scaling.  
- [ ] Artificial general intelligence (AGI) and tests for intelligence.

## **M6. NLP, CV and RL subfields.** {#m6.-nlp,-cv-and-rl-subfields.}

- [ ] Text and speech – classic NLP. [*Jurafsky and Martin*](https://web.stanford.edu/~jurafsky/slp3/)*.* 
- [ ] **Large Language Models (LLMs)** - GPT-4, Claude, LLaMA, Gemini architecture and capabilities.  
- [ ] Transformer architecture, prompt engineering, RAGs and fine-tuning.  
- [ ] **Instruction tuning and alignment** (RLHF, DPO, constitutional AI).  
- [ ] **In-context learning** (few-shot, zero-shot, chain-of-thought prompting).  
- [ ] **Model compression** (quantization: 4-bit, 8-bit; distillation; LoRA/QLoRA).  
- [ ] **Hallucination detection and mitigation** in generative models.  
- [ ] Computer vision (CV).  
- [ ] **Multimodal models** (CLIP, GPT-4V, vision-language integration).  
- [ ] **Diffusion models** (Stable Diffusion, DALL-E, Midjourney for image generation).  
- [x] ~~Reinforcement learning (RL). [*Sutton and Barto*](http://www.incompleteideas.net/book/the-book-2nd.html)*.*~~  
- [x] ~~Robotics. [*Underactuated Robotics*](https://underactuated.csail.mit.edu/) *course notes by [Russ Tedrake](http://people.csail.mit.edu/russt/).*~~

## **M7. Other modelling techniques.** {#m7.-other-modelling-techniques.}

- [x] ~~Graphs and networks. [*NetworkX bibliography.*](https://networkx.org/documentation/stable/#bibliography)~~  
- [x] ~~Agent-based modeling (ABM).~~   
- [x] ~~Game theory and auction design.~~  
- [x] ~~Optimisation and linear programming (LP). [*MOSEK and*](https://docs.mosek.com/modeling-cookbook/zbiblio.html#id181)~~   
      [*JuMP*](https://jump.dev/JuMP.jl/stable/background/bibliography/) *[bibliographies.](https://docs.mosek.com/modeling-cookbook/zbiblio.html#id181) [Stephen Boyd](https://web.stanford.edu/~boyd) books and classes.*  
- [x] ~~System dynamics (SD). [*Jay Forrester.*](https://systemdynamics.org/news/memorial/jay-w-forrester/)~~  
- [x] ~~Control theory. [*r/ControlTheory wiki*](https://www.reddit.com/r/ControlTheory/wiki/index/) *and [Feedback Systems by Aström and Murray](https://www.cds.caltech.edu/~murray/books/AM08/pdf/am08-complete_28Sep12.pdf)*.~~

## **M9. Modern AI Architectures (2020-2025).** {#m9.-modern-ai-architectures}

- [ ] **Transformer variants** (encoder-only: BERT; decoder-only: GPT; encoder-decoder: T5).  
- [ ] **Vision Transformers (ViT)** for image understanding.  
- [ ] **State Space Models** (Mamba, structured state spaces for efficient sequence modeling).  
- [ ] **Retrieval-augmented architectures** (RAG systems combining retrieval and generation).  
- [ ] **Sparse models and efficient transformers** (Sparse Transformers, Longformer, sliding window attention).

## **M8. Additional topics (harder or less exciting)** {#m8.-additional-topics-(harder-or-less-exciting)}

- [x] ~~Combinatorics… *[is hard.](https://www.reddit.com/r/mathematics/comments/17e0h2h/combinatorics_destroying_my_ego_the_strangest_of/)*~~  
- [x] ~~Mathematical statistics (point estimation, confidence bands, hypothesis testing).~~  
- [x] ~~Central limit theorems, asymptotics and convergence.~~  
- [x] ~~Non-parametric statistics. [*All of Nonparametric Statistics*](https://link.springer.com/book/10.1007/0-387-30623-4)*.*~~  
- [x] ~~Entropy, cross-entropy and information theory.~~  
- [x] ~~Differential equations and random processes.~~  
- [x] ~~Probability as part of measure theory.~~

# **D. Data** {#d.-data}

## **D1. Data sources.** {#d1.-data-sources.}

- [ ] Data collection, observation vs experiment, registration protocols.   
- [ ] Physical sensors.  
- [ ] Proprietary vs open data, disclosure requirements, official statistics.  
- [ ] Data distribution and providers. Data markets.  
- [ ] Data protection and privacy.

## **D2. Data analysis.** {#d2.-data-analysis.}

- [ ] EDA and descriptive statistics.  
- [ ] Graphs, visualizations, dashboards.  
- [ ] Analysis as a DAG.   
- [ ] Reproducible research.

## **D3. Data engineering.** {#d3.-data-engineering.}

- [ ] Structured data. Serialization formats (CSV, JSON, XML). Binary data formats.  
- [ ] SQL for tabular data. Dataframes (pandas, polars) and dataframe backends.  
- [ ] Processing large datasets (MapReduce, Hadoop, Spark).  
- [ ] Everything as a vector: text, images, sound and video.   
- [ ] Data ingestion, transform, storage, retrieval.  
- [ ] **Vector databases** (Pinecone, Weaviate, ChromaDB, pgvector for embedding storage).  
- [ ] **Embedding storage and retrieval** (semantic search, nearest neighbor, HNSW, FAISS).  
- [ ] **Real-time data streaming** (Kafka, Flink, event-driven architectures).  
- [ ] **Data versioning** (DVC, LakeFS for reproducibility).

## **D4. Pipelines and orchestration.** {#d4.-pipelines-and-orchestration.}

- [ ] Modelling pipelines (Airflow and similar).  
- [ ] Model delivery (eg FastAPI).  
- [ ] **MLOps platforms** (MLflow, Weights & Biases, Kubeflow, Neptune).  
- [ ] **Feature stores** (Feast, Tecton for feature management).  
- [ ] **A/B testing and experimentation frameworks** for production ML.  
- [ ] **Model versioning and registry** (tracking model lineage and artifacts).  
      

## **D5. Data management**  {#d5.-data-management}

- [ ] Data quality  
- [ ] Corporate data governance (DMBOK).

# **T. Tools – Code and Infrastructure** {#t.-tools-–-code-and-infrastructure}

## **T0. Writing code** {#t0.-writing-code}

- [ ] Linux and command line on a local and remote machine.  
- [ ] Software development practices for data modelling (version control, unit testing, APIs, DevOps, product thinking and metrics, architecture).  
- [ ] Python, R, Julia ecosystems for machine learning.

## **T1. Software tools.**  {#t1.-software-tools.}

- [ ] Proprietary statistical packages and their documentation.  
- [ ] Open software for statistics (R), machine learning (scikit-learn) and neural networks (pytorch, tensorflow and keras).  
- [ ] Managed services for machine learning (H20, DataRobot, etc).  
- [ ] **LLM frameworks** (LangChain, LlamaIndex, Haystack for LLM applications).  
- [ ] **Hugging Face ecosystem** (Transformers, Datasets, Accelerate, PEFT for model training).  
- [ ] **Vector database libraries** (FAISS, Annoy, hnswlib for similarity search).  
- [ ] **Modern ML frameworks** (JAX, XGBoost, LightGBM, CatBoost for gradient boosting).

## **T2. Cloud and computing infrastructure.** {#t2.-cloud-and-computing-infrastructure.}

- [ ] Cloud services and infrastructure provisioning.  
- [ ] **GPU computing** (CUDA, distributed training, multi-GPU setups).  
- [ ] **Container orchestration** (Docker, Kubernetes for ML workloads).  
- [ ] **Serverless ML** (AWS Lambda for inference, Modal, Banana, Replicate).  
- [ ] **Edge deployment** (TensorFlow Lite, ONNX Runtime, model optimization for edge devices).  
- [ ] **LLM hosting** (vLLM, TGI Text Generation Inference, Ollama for local models).

## **T3. Development Tools and Environment.** {#t3.-development-tools}

- [ ] **Jupyter ecosystem** (JupyterLab, Jupyter notebooks, extensions, interactive computing).  
- [ ] **IDEs and AI coding assistants** (VS Code, Cursor, GitHub Copilot, Windsurf).  
- [ ] **Experiment tracking** (Weights & Biases, Neptune, Comet for reproducibility).  
- [ ] **Data labeling tools** (Label Studio, Prodigy, Scale AI for annotation).

# 

# **P. Productisation** {#p.-productisation}

Delivering value for users, business stakeholders and society from data and models.

Note: “model producisation” usually means two things – taking a model out of a single author usage to a workable system – thus making a pipeline, or designing a task ina  way that is likely to serve a business purpose   

## **P1. Productisation and business value.** {#p1.-productisation-and-business-value.}

- [ ] Risk, learning and experimentation in business context.  
- [ ] Modelling hypothesis and expected outcomes.  
- [ ] Data-model-action workflows.  
- [ ] Team roles, rationale for these roles and hiring.  
- [ ] Measuring business outcomes and business impact of ML.  
- [ ] **RAG systems** (Retrieval Augmented Generation architecture and implementation).  
- [ ] **Prompt engineering** as a systematic discipline for LLM applications.  
- [ ] **AI agent frameworks** (AutoGPT, LangChain agents, function calling for autonomous agents).  
- [ ] **Model monitoring** (drift detection, performance tracking in production).  
- [ ] **Cost optimization** (token usage tracking, caching strategies, batch processing).

## **P2. Applications, domains and cases.** {#p2.-applications,-domains-and-cases.}

- [ ] Recommender systems (RecSys).  
- [ ] Clinical trials.  
- [ ] Quality control and industrial automation.  
- [ ] Finance.  
- [ ] **Conversational AI and chatbots** (customer service, virtual assistants).  
- [ ] **Code generation** (GitHub Copilot, code assistants, automated programming).  
- [ ] **Document intelligence** (Q&A over documents, summarization, extraction).  
- [ ] **Search and information retrieval** (semantic search, hybrid search systems).

## **P3. Society impacts and regulation.** {#p3.-society-impacts-and-regulation.}

- [ ] Fairness, biases, equity, human loop and ethics.  
- [ ] Grounds for AI regulation and policy.   
- [ ] Generation-scale and wicked problems.  
- [ ] **AI safety and alignment** (value alignment, red teaming, adversarial testing).  
- [ ] **Prompt injection and security** vulnerabilities in LLM systems.  
- [ ] **Environmental impact** (carbon footprint of training large models).  
- [ ] **AI watermarking and detection** (synthetic content identification).  
- [ ] **Copyright and intellectual property** issues with generative AI.

# **E. Extra topics** {#e.-extra-topics}

## **E1. Companies** {#e1.-companies}

- [x] ~~Academic vs corporate research.~~  
- [x] ~~Company valuations.~~  
- [x] ~~Data ownership.~~ 

---

# **Personalized Learning Roadmap** {#personalized-learning-roadmap}

This section provides a structured, phase-based approach to learning AI/ML, tailored for progressive skill building from foundations to advanced applications.

## 🎯 Your Current Position

**Phase 1 - Foundation** ✅ (You've completed tokenization basics)  
**Phase 2 - Embeddings & Vectors** 🎯 (You are here - working on embeddings)  
**Phase 3 - Neural Networks & Transformers** ⏭️ (Coming next)  
**Phase 4 - LLMs & Applications** 🔜 (Advanced topics)

---

## Phase 1: Foundation ✅

**Core Concepts**

- ✅ Artificial Intelligence (AI)
- ✅ Machine Learning (ML)
- ✅ Supervised / Unsupervised / Semi‑Supervised Learning
- Reinforcement Learning (RL)
- Offline vs Online Machine Learning
- Overfitting, Underfitting, Bias, Variance

**Math & Statistics Basics**

- Loss Functions (Cross‑Entropy, Mean Squared Error)
- Optimization (gradients, backpropagation basics)
- L1 Norm, L2 Norm, Regularisation
- Probability (Naïve Bayes, distributions)

**Data Fundamentals**

- Features, Labels, Annotation
- Training/Validation/Testing Sets
- Feature Engineering & Feature Extraction
- Normalisation

---

## Phase 2: Embeddings & Vectors 🎯 (Current Focus)

**Tokenization** ✅

- ✅ Tokens - Text broken into processable units
- ✅ Tokenization algorithms (BPE, WordPiece)
- ✅ Subword tokenization concepts

**Embeddings** 🔥 (Learn next)

- Embeddings - Dense vector representations
- Word2Vec, fastText, Doc2Vec
- Semantic meaning in vector space
- Cosine Similarity - Measuring semantic similarity
- Vector operations (addition, subtraction, distance)

**Vector Storage & Retrieval**

- Vector Database (Pinecone, Weaviate, ChromaDB)
- Semantic search vs keyword search
- Nearest neighbor search
- Dimensionality (384, 768, 1536 dimensions)

**Text Representations (Classical)**

- Bag of Words, N‑grams (Bigrams, Trigrams)
- TF (Term Frequency), IDF (Inverse Document Frequency)
- TF‑IDF weighting

---

## Phase 3: Neural Networks & Architecture

**Neural Network Basics**

- Neural Networks, Hidden Layers
- Activation Functions (ReLU, sigmoid, tanh)
- Backpropagation (in depth)
- Gradient descent & optimization
- Epoch, Batch Size, Learning rate
- Dropout, Regularization techniques

**Deep Learning Architectures**

- Deep Learning fundamentals
- CNNs (Convolutional Neural Networks) - for images
- RNNs (Recurrent Neural Networks) - for sequences
- LSTMs (Long Short-Term Memory) - for long sequences
- Autoencoders - dimensionality reduction

**Attention & Transformers** 🌟

- Attention Mechanism - focusing on relevant parts
- Self-Attention - all tokens attend to each other
- Multi-Head Attention - multiple attention in parallel
- Transformer Architecture - the foundation of modern NLP
- Encoder-Decoder Architecture
- Positional Encoding

---

## Phase 4: LLMs & Modern AI 🚀

**Large Language Models**

- LLMs (Large Language Models) - GPT, Claude, LLaMA
- GPT (Generative Pre-trained Transformer)
- BERT (Bidirectional Encoder Representations)
- Foundation Models - pre-trained models
- Context Window - token limits
- Perplexity - model evaluation

**Working with LLMs**

- Prompt Engineering - crafting effective prompts
- Temperature - controlling randomness
- Few-Shot / One-Shot / Zero-Shot Learning
- In-Context Learning
- Chain-of-Thought (CoT) prompting
- Instruction Tuning

**Fine-tuning & Optimization**

- Transfer Learning
- Fine-tuning pre-trained models
- LoRA (Low-Rank Adaptation) - efficient fine-tuning
- Quantization - 4-bit, 8-bit model compression
- Distillation - creating smaller models
- RLHF (Reinforcement Learning from Human Feedback)

**RAG & Knowledge Systems**

- RAG (Retrieval Augmented Generation) 🔥
- Information Retrieval (IR)
- Semantic search with embeddings
- Combining retrieval + generation
- Knowledge Graphs

---

## Phase 5: Specialized Domains

**Natural Language Processing (NLP)**

- NLP fundamentals
- Named Entity Recognition (NER)
- Sentiment Classification
- Machine Translation (MT)
- Sequence‑to‑Sequence (Seq2Seq)
- Abstractive vs Extractive Summarisation
- Natural Language Generation (NLG)
- Chatbots & conversational AI

**Computer Vision (CV)**

- Computer Vision concepts
- CNN applications (classification, detection)
- Image embeddings (CLIP)
- Stable Diffusion - text-to-image
- Diffusion Models
- GANs (Generative Adversarial Networks)
- Multimodal AI - text + vision

**Advanced Topics**

- AI Agents - autonomous decision-making
- Mixture of Experts (MoE)
- Active Learning
- Recommender Systems
- Anomaly Detection
- Human in the Loop (HITL) systems

---

## Phase 6: ML Engineering & Production

**Model Evaluation**

- Accuracy, Precision, Recall, F1 Score
- Cross‑Validation
- Confusion Matrix
- BLEU, ROUGE (for generation tasks)

**Data Engineering**

- Data pipelines
- ETL (Extract, Transform, Load)
- Data versioning
- Batch vs streaming processing

**ML Tools & Libraries**

- NumPy - numerical computing
- Pandas - data manipulation
- Scikit‑Learn - classical ML
- PyTorch / TensorFlow / Keras - deep learning
- Hugging Face Transformers
- LangChain - LLM applications

**MLOps & Deployment**

- ML Pipelines (Kedro, Airflow)
- Model versioning & monitoring
- Cloud platforms (AWS SageMaker, Azure ML, GCP)
- API deployment (FastAPI, Flask)
- Model serving & inference optimization
- A/B testing

---

## Phase 7: Ethics, Safety & Advanced Concepts

**AI Safety & Alignment**

- Hallucination - factual accuracy issues
- Alignment - matching human values
- Constitutional AI
- Prompt Injection - security concerns
- Bias & fairness in AI
- Explainability & interpretability

**Model Types Comparison**

- Generative vs Discriminative models
- Supervised vs Unsupervised vs RL
- Rules‑Based vs ML-based systems
- Classical ML vs Deep Learning tradeoffs

---

## 📚 Learning Resources by Phase

**Phase 1-2 (Foundation + Embeddings):**

- Start with your current examples: `tiktoken_example.py`, `embeddings_intro.py`
- Practice: Create embeddings for different texts, compare similarities
- Build: Simple semantic search with your own documents

**Phase 3 (Neural Networks):**

- Implement: Simple neural network from scratch
- Study: 3Blue1Brown neural network series
- Practice: MNIST digit classification with PyTorch

**Phase 4 (LLMs):**

- Use: OpenAI API, Anthropic Claude, or local LLMs
- Build: RAG system with your own knowledge base
- Practice: Prompt engineering for different tasks

**Phase 5+ (Specialization):**

- Choose your focus: NLP, CV, or multimodal
- Build end-to-end projects
- Contribute to open source (Hugging Face, LangChain)


---

**Legend:**  
✅ Completed | 🎯 Current Focus | 🔥 Priority Next | ⏭️ Coming Soon | 🚀 Advanced | 🌟 Essential

---

# **Table of Contents** {#table-of-contents} 

[M. Models](#m.-models)

[M0. Statistical thinking and intuition](#m0.-statistical-thinking-and-intuition)

[M1. Statistical inference](#m1.-statistical-inference)

[M2. Econometrics](#m2.-econometrics)

[M3. Bayesian modeling and causal inference.](#m3.-bayesian-modeling-and-causal-inference.)

[M4. Classic machine learning.](#m4.-classic-machine-learning.)

[M5. Neural nets (NN) and deep learning.](#m5.-neural-nets-\(nn\)-and-deep-learning.)

[M6. NLP, CV and RL subfields.](#m6.-nlp,-cv-and-rl-subfields.)

[M7. Other modelling techniques.](#m7.-other-modelling-techniques.)

[M8. Additional topics (harder or less exciting)](#m8.-additional-topics-\(harder-or-less-exciting\))

[D. Data](#d.-data)

[D1. Data sources.](#d1.-data-sources.)

[D2. Data analysis.](#d2.-data-analysis.)

[D3. Data engineering.](#d3.-data-engineering.)

[D4. Pipelines and orchestration.](#d4.-pipelines-and-orchestration.)

[D5. Data management](#d5.-data-management)

[T. Tools – Code and Infrastructure](#t.-tools-–-code-and-infrastructure)

[T0. Writing code](#t0.-writing-code)

[T1. Software tools.](#t1.-software-tools.)

[T2. Cloud and computing infrastructure.](#t2.-cloud-and-computing-infrastructure.)

[P. Productisation](#p.-productisation)

[P1. Productisation and business value.](#p1.-productisation-and-business-value.)

[P2. Applications, domains and cases.](#p2.-applications,-domains-and-cases.)

[P3. Society impacts and regulation.](#p3.-society-impacts-and-regulation.)

[E. Extra topics](#e.-extra-topics)

[E1. Companies](#e1.-companies)  
