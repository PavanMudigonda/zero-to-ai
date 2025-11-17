# Machine Learning Guide

**Machine Learning Checklist**  

---

## 📑 Table of Contents

### Introduction & Getting Started

- [Prerequisites](#-prerequisites)
- [Beginner Track: Core Resources](#-beginner-track-core-resources)
- [Learning Roadmap](#️-learning-roadmap)
- [Reference Textbooks](#-reference-textbooks)
- [Video Series (Essential)](#-video-series-essential)
- [Supplementary Resources](#️-what-else-supplementary-resources)
- [Not in Scope](#️-not-in-scope-but-important)
- [Extended Modelling Process](#extended-modelling-process)

### MDTP Framework: Models, Data, Tools, Productisation

**M. Models**

- [M0. Statistical thinking and intuition](#m0-statistical-thinking-and-intuition)
- [M1. Statistical inference](#m1-statistical-inference)
- [M2. Econometrics](#m2-econometrics)
- [M3. Bayesian modeling and causal inference](#m3-bayesian-modeling-and-causal-inference)
- [M4. Classic machine learning](#m4-classic-machine-learning)
- [M5. Neural nets (NN) and deep learning](#m5-neural-nets-nn-and-deep-learning)
- [M6. NLP, CV and RL subfields](#m6-nlp-cv-and-rl-subfields)
- [M7. Other modelling techniques](#m7-other-modelling-techniques)
- [M8. Additional topics (harder or less exciting)](#m8-additional-topics-harder-or-less-exciting)
- [M9. Modern AI Architectures (2020-2025)](#m9-modern-ai-architectures-2020-2025)

**D. Data**

- [D1. Data sources](#d1-data-sources)
- [D2. Data analysis](#d2-data-analysis)
- [D3. Data engineering](#d3-data-engineering)
- [D4. Pipelines and orchestration](#d4-pipelines-and-orchestration)
- [D5. Data management](#d5-data-management)

**T. Tools – Code and Infrastructure**

- [T0. Writing code](#t0-writing-code)
- [T1. Software tools](#t1-software-tools)
- [T2. Cloud and computing infrastructure](#t2-cloud-and-computing-infrastructure)
- [T3. Development Tools and Environment](#t3-development-tools-and-environment)

**P. Productisation**

- [P1. Productisation and business value](#p1-productisation-and-business-value)
- [P2. Applications, domains and cases](#p2-applications-domains-and-cases)
- [P3. Society impacts and regulation](#p3-society-impacts-and-regulation)

**E. Extra**

- [E1. Companies](#e1-companies)

### Personalized Learning Path

- [Your Current Position](#-your-current-position)
- [Phase 1: Foundation](#phase-1-foundation)
- [Phase 2: Embeddings & Vectors](#phase-2-embeddings--vectors-current-focus)
- [Phase 3: Neural Networks & Architecture](#phase-3-neural-networks--architecture)
- [Phase 4: LLMs & Modern AI](#phase-4-llms--modern-ai-)
- [Phase 5: Specialized Domains](#phase-5-specialized-domains)
- [Phase 6: ML Engineering & Production](#phase-6-ml-engineering--production)
- [Phase 7: Ethics, Safety & Advanced Concepts](#phase-7-ethics-safety--advanced-concepts)

### Microsoft AI/Agent Framework Ecosystem

- [Microsoft Agent Frameworks & Courses](#-microsoft-agent-frameworks--courses)

### Career & Community

- [Interviews & Career Insights](#-interviews--career-insights)
- [Influential Educators & Thinkers](#-influential-educators--thinkers)
- [Professional Glossary & Common Terms](#-professional-glossary--common-terms)

---

This guide provides a comprehensive roadmap for learning machine learning, from foundational mathematics to production-ready AI systems. It combines:

- **M (models)**: probability, statistics, econometrics, machine learning, deep learning and other modelling areas.  
- **D (data)**: data engineering, data management and data governance.  
- **T (tools)**: software tools, databases and computing infrastructure.  
- **P (productisation)**: ok, now you have the data, a model and a server running, but what's the benefit?

---

## 📋 Prerequisites

Before diving into machine learning, ensure you have:

- **Working knowledge of Python** - Basic programming concepts, data structures, control flow
- **Mathematical foundations** - Comfort with mathematical notation and concepts from:
  - Linear algebra (vectors, matrices, operations)
  - Calculus (derivatives, gradients, chain rule)
  - Basic probability and statistics

If you need to strengthen these areas, refer to the resources in the sections below.

---

## 🚀 Beginner Track: Core Resources

Three foundational resources form the entry track for beginners:

### 1. Mathematics for Machine Learning (MML)

- [ ] **Authors:** Marc Peter Deisenroth, A. Aldo Faisal, Cheng Soon Ong (2020)  
- [ ] **Link:** Free textbook  
- [ ] **Coverage:** Linear algebra, calculus, probability for ML context  
- [ ] **Use for:** Part 1 for math review, Chapter 8 for ML introduction

### 2. Introduction to Statistical Learning with Python (ISLP)

- [ ] **Authors:** Gareth James, Daniela Witten, Trevor Hastie, Rob Tibshirani (2023)  
- [ ] **Link:** Free textbook  
- [ ] **Coverage:** Classic ML algorithms, statistical learning theory  
- [ ] **Use for:** Main textbook for supervised/unsupervised learning methods

### 3. Deep Learning Specialization

- [ ] **Instructor:** Andrew Ng  
- [ ] **Platform:** deeplearning.ai / Coursera  
- [ ] **Coverage:** Neural networks, CNNs, RNNs, sequence models  
- [ ] **Use for:** Practical deep learning implementation

---

## 🗺️ Learning Roadmap

[ ] Original guide: [Beginner Learning Path](https://trics.me/beginner.html)

```
Math    ML       DL                   Subfields and data types
=====   =======  =================    ============================

          +-------------------------> Tabular data and time series
          |
MML   -> ISLP -> deeplearning.ai  -> Text and speech (NLP)
(free)   (free)  Deep Learning        Transformers (the T in ChatGPT)
          |      Specialization  +    Computer vision (CV)
          |      any of 3 free   |    Reinforcement learning (RL)
          |      textbooks       |
          |                      |
         Practical manuals:      |
         - scipy lectures        |
         - Müller, Géron, Burkov |
                                 v
                        Choose your specialization
```

### Python Packages by Domain

**Math & Computation:**

- `numpy` - Numerical computing, arrays, linear algebra
- `scipy` - Scientific computing, optimization, statistics

**Machine Learning:**

- `scikit-learn` - Classic ML algorithms (see [Gaël Varoquaux 2023 interview](https://www.youtube.com/watch?v=ONb2OcLRQTo))

**Deep Learning:**

- `torch` (PyTorch) - Most advanced, research-focused
- `tensorflow` - Most cited, production-ready
- `keras` - Easier interface, high-level API

**Data Handling:**

- `pandas` or `polars` - Tabular data manipulation

**Visualization:**

- `matplotlib` - Standard plotting
- `plotly`, `bokeh` - Interactive visualizations

---

## 📚 Reference Textbooks

These denser textbooks serve as references alongside the core beginner track:

### Classic Machine Learning

- [ ] **Bishop (2006)** - Pattern Recognition and Machine Learning
- [ ] **Murphy (2022)** - Probabilistic Machine Learning

### Deep Learning

- [ ] **Goodfellow, Bengio, Courville (2016)** - Deep Learning Book (DLB)
  - The reference text with continuous citations
- [ ] **Zhang, Lipton, Li, Smola (2021)** - [Dive into Deep Learning (d2l)](https://d2l.ai/)
  - Jupyter notebooks integrating exposition, math, and runnable code
  - Freely available with interactive examples
- [ ] **Prince (2023)** - [Understanding Deep Learning (UDL)](https://udlbook.github.io/udlbook/)
  - Recent textbook with updated content

### Specialized Domains

- [ ] **Jurafsky and Martin** - Speech and Language Processing (NLP)
- [ ] **Sutton and Barto** - Reinforcement Learning: An Introduction (RL)

---

## 🎥 Video Series (Essential)

### StatQuest by Josh Starmer

- [ ] **Focus:** Statistics and ML concepts explained intuitively
- [ ] **Style:** Visual, step-by-step breakdowns
- [ ] **Best for:** Understanding core concepts (PCA, regression, neural nets, etc.)
- [ ] **Link:** YouTube channel

### 3Blue1Brown by Grant Sanderson

- [ ] **Focus:** Mathematical visualization
- [ ] **Notable:** Neural Networks series, Calculus series, Linear Algebra series
- [ ] **Style:** Beautiful animations explaining mathematical intuition
- [ ] **Best for:** Deep understanding of math behind ML
- [ ] **Link:** YouTube channel

### Andrej Karpathy

- [ ] **Focus:** Neural networks, transformers, GPT architecture
- [ ] **Notable:** [NanoGPT](https://github.com/karpathy/nanoGPT) - minimal GPT implementation
- [ ] **Style:** Code walkthroughs, architectural deep dives
- [ ] **Best for:** Understanding modern transformer architectures
- [ ] **Link:** YouTube and GitHub

---

## 🛠️ What Else? Supplementary Resources

### Probability and Statistics

- [ ] **Probability for Data Science (P4D)** - Introductory course
- [ ] **Seeing Theory** - Visual introduction to probability and statistics

### Practical Python for ML

- [ ] **scipy lectures** - Underappreciated resource by scikit-learn package authors
- [ ] **Python Data Science Handbook** - Jake VanderPlas (includes ML chapter)
- [ ] **Practical books** (combine concepts + code):
  - [ ] Müller & Guido - Introduction to Machine Learning with Python (paid)
  - [ ] Géron - Hands-On Machine Learning (paid)
  - [ ] Burkov - The Hundred-Page Machine Learning Book (free preview)

### Code Collections and Practice

- [ ] **ML-From-Scratch** - Implementing algorithms from scratch
- [ ] **Kaggle competitions** - Real datasets and competitions
  - Note: Kaggle is Google-owned, emphasizes TensorFlow over PyTorch

### Domain-Specific Modeling

- [ ] **Econometrics** - [Econ 1630](https://www.brown.edu/Departments/Economics/Faculty/Glenn_Loury/louryhomepage/teaching/Ec_1630/) chapters 1, 2, 4, 5
- [ ] **Data analysis vocabulary** - Industry perspectives from:
  - Google, Mathworks, H2O.ai, NVIDIA documentation

### Research Papers and Advanced Topics

- [ ] Statistical Learning Theory (loss, risk, PAC-Bayes)
- [ ] Breiman's "Two Cultures" (2001) - Inference vs. prediction debate
- [ ] Current ML/AI research on arXiv

---

## ⚠️ Not in Scope (But Important)

This guide focuses on ML concepts and modeling. These related skills are NOT deeply covered but are essential for professional work:

- **Python programming depth** - Advanced OOP, design patterns, performance optimization
- **Linux and cloud computing** - DevOps, containerization, orchestration
- **Data processing pipelines** - Airflow, Spark, real-time streaming
- **Model productization** - API design, scalability, monitoring
- **Experiment design** - A/B testing, causal inference, statistical power
- **Advanced statistics** - Bayesian methods, time series, survival analysis
- **Non-ML modeling** - Optimization, simulation, control theory
- **Domain knowledge** - Business understanding, subject matter expertise
- **ML adoption outcomes** - Organizational change, ethics, governance

For coverage of these topics, refer to the complete MDTP sections below.

---

## Extended Modelling Process

The table below summarizes steps in the extended modeling process, from initial idea to business/societal benefits:  

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

# **M. Models**

~~Non-essential topics are strike-through~~

## **M0. Statistical thinking and intuition**

- [ ] Probability, random variables, distributions.  
- [ ] Model vs. reality. Digital twins.
- [ ] Structure and causality.
- [ ] Inference (econometrics) vs generalisation (machine learning). Breiman's *[Two Cultures](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full)* (2001) and rebuttals.  
- [ ] Observation, experiment and experiment design.  
- [ ] Treatment and treatment effects.
- [ ] Measurement errors and missing data.

## **M1. Statistical inference**

- [ ] Data generating process, sample vs population.  
- [ ] Sampling techniques and inference. Statistical model.
- [ ] Frequentist and Bayesian views of a statistical model.  
- [ ] ~~Modelling tradeoffs and “no free lunch”.~~  
- [ ] Measuring model quality and performance.  
- [ ] Model lifecyle, data and model drift.

## **M2. Econometrics**

- [ ] Cross-section, time series, panel and spatial data.
- [ ] Linear regression and ordinary least squares (OLS).  
- [ ] Violation of OLS assumptions. [*Peter Kennedy*](https://en.wikipedia.org/wiki/Peter_Kennedy_\(economist\)) textbook and the [*10 Commandments*](https://www.principlesofeconometrics.com/poe5/writing/kennedy.pdf).  
- [ ] ~~Difference-in-differences, instrumental variables, regression discontinuity.~~  
- [ ] ~~Time series. Seasonal adjustment, smoothing, filtering.~~  
- [ ] ~~Systems of equations.~~  
- [ ] Estimation techniques: OLS and varieties, GMM, maximum likelihood, Bayesian estimates.

## **M3. Bayesian modeling and causal inference.**

- [ ] ~~Bayesian modeling and probabilistic programming.~~  
- [ ] ~~Causal inference and do-notation.~~

## **M4. Classic machine learning.**

- [ ] Tasks: classification, regression, clustering, dimensionality reduction, decision trees, support vector machines and discriminant analysis.  
- [ ] Criteria for model selection and performance evaluation.
- [ ] ~~Statistical learning theory (loss, theoretical and empirical risk, PAC-Bayes)~~  
- [ ] ~~Forecast combination, choosing forecasts and AutoML.~~

## **M5. Neural nets (NN) and deep learning.**

- [ ] Simple perceptron and NN construction (gradient descent, backpropagation, regularization).  
- [ ] Traditional NN architectures (feed-forward, convolutional, recurrent, generative аdversarial, transformers).  
- [ ] **Embeddings and vector representations** (word2vec, sentence-transformers, dense vectors for semantic meaning).  
- [ ] **Tokenization** (BPE, WordPiece, SentencePiece for modern LLMs).  
- [ ] **Attention mechanism** (self-attention, multi-head attention - foundational for transformers).  
- [ ] **Mixture of Experts (MoE)** architecture for efficient scaling.  
- [ ] Artificial general intelligence (AGI) and tests for intelligence.

## **M6. NLP, CV and RL subfields.**

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
- [ ] ~~Reinforcement learning (RL). [*Sutton and Barto*](http://www.incompleteideas.net/book/the-book-2nd.html)*.*~~  
- [ ] ~~Robotics. [*Underactuated Robotics*](https://underactuated.csail.mit.edu/) *course notes by [Russ Tedrake](http://people.csail.mit.edu/russt/).*~~

## **M7. Other modelling techniques.**

- [ ] ~~Graphs and networks. [*NetworkX bibliography.*](https://networkx.org/documentation/stable/#bibliography)~~  
- [ ] ~~Agent-based modeling (ABM).~~
- [ ] ~~Game theory and auction design.~~  
- [ ] ~~Optimisation and linear programming (LP). [*MOSEK and*](https://docs.mosek.com/modeling-cookbook/zbiblio.html#id181)~~
      [*JuMP*](https://jump.dev/JuMP.jl/stable/background/bibliography/) *[bibliographies.](https://docs.mosek.com/modeling-cookbook/zbiblio.html#id181) [Stephen Boyd](https://web.stanford.edu/~boyd) books and classes.*  
- [ ] ~~System dynamics (SD). [*Jay Forrester.*](https://systemdynamics.org/news/memorial/jay-w-forrester/)~~  
- [ ] ~~Control theory. [*r/ControlTheory wiki*](https://www.reddit.com/r/ControlTheory/wiki/index/) *and [Feedback Systems by Aström and Murray](https://www.cds.caltech.edu/~murray/books/AM08/pdf/am08-complete_28Sep12.pdf)*.~~

## **M9. Modern AI Architectures (2020-2025).**

- [ ] **Transformer variants** (encoder-only: BERT; decoder-only: GPT; encoder-decoder: T5).  
- [ ] **Vision Transformers (ViT)** for image understanding.  
- [ ] **State Space Models** (Mamba, structured state spaces for efficient sequence modeling).  
- [ ] **Retrieval-augmented architectures** (RAG systems combining retrieval and generation).  
- [ ] **Sparse models and efficient transformers** (Sparse Transformers, Longformer, sliding window attention).

## **M8. Additional topics (harder or less exciting)**

- [ ] ~~Combinatorics… *[is hard.](https://www.reddit.com/r/mathematics/comments/17e0h2h/combinatorics_destroying_my_ego_the_strangest_of/)*~~  
- [ ] ~~Mathematical statistics (point estimation, confidence bands, hypothesis testing).~~  
- [ ] ~~Central limit theorems, asymptotics and convergence.~~  
- [ ] ~~Non-parametric statistics. [*All of Nonparametric Statistics*](https://link.springer.com/book/10.1007/0-387-30623-4)*.*~~  
- [ ] ~~Entropy, cross-entropy and information theory.~~  
- [ ] ~~Differential equations and random processes.~~  
- [ ] ~~Probability as part of measure theory.~~

# **D. Data**

## **D1. Data sources.**

- [ ] Data collection, observation vs experiment, registration protocols.
- [ ] Physical sensors.  
- [ ] Proprietary vs open data, disclosure requirements, official statistics.  
- [ ] Data distribution and providers. Data markets.  
- [ ] Data protection and privacy.

## **D2. Data analysis.**

- [ ] EDA and descriptive statistics.  
- [ ] Graphs, visualizations, dashboards.  
- [ ] Analysis as a DAG.
- [ ] Reproducible research.

## **D3. Data engineering.**

- [ ] Structured data. Serialization formats (CSV, JSON, XML). Binary data formats.  
- [ ] SQL for tabular data. Dataframes (pandas, polars) and dataframe backends.  
- [ ] Processing large datasets (MapReduce, Hadoop, Spark).  
- [ ] Everything as a vector: text, images, sound and video.
- [ ] Data ingestion, transform, storage, retrieval.  
- [ ] **Vector databases** (Pinecone, Weaviate, ChromaDB, pgvector for embedding storage).  
- [ ] **Embedding storage and retrieval** (semantic search, nearest neighbor, HNSW, FAISS).  
- [ ] **Real-time data streaming** (Kafka, Flink, event-driven architectures).  
- [ ] **Data versioning** (DVC, LakeFS for reproducibility).

## **D4. Pipelines and orchestration.**

- [ ] Modelling pipelines (Airflow and similar).  
- [ ] Model delivery (eg FastAPI).  
- [ ] **MLOps platforms** (MLflow, Weights & Biases, Kubeflow, Neptune).  
- [ ] **Feature stores** (Feast, Tecton for feature management).  
- [ ] **A/B testing and experimentation frameworks** for production ML.  
- [ ] **Model versioning and registry** (tracking model lineage and artifacts).  

## **D5. Data management**

- [ ] Data quality  
- [ ] Corporate data governance (DMBOK).

# **T. Tools – Code and Infrastructure**

## **T0. Writing code**

- [ ] Linux and command line on a local and remote machine.  
- [ ] Software development practices for data modelling (version control, unit testing, APIs, DevOps, product thinking and metrics, architecture).  
- [ ] Python, R, Julia ecosystems for machine learning.

## **T1. Software tools.**

- [ ] Proprietary statistical packages and their documentation.  
- [ ] Open software for statistics (R), machine learning (scikit-learn) and neural networks (pytorch, tensorflow and keras).  
- [ ] Managed services for machine learning (H20, DataRobot, etc).  
- [ ] **LLM frameworks** (LangChain, LlamaIndex, Haystack for LLM applications).  
- [ ] **Hugging Face ecosystem** (Transformers, Datasets, Accelerate, PEFT for model training).  
- [ ] **Vector database libraries** (FAISS, Annoy, hnswlib for similarity search).  
- [ ] **Modern ML frameworks** (JAX, XGBoost, LightGBM, CatBoost for gradient boosting).

## **T2. Cloud and computing infrastructure.**

- [ ] Cloud services and infrastructure provisioning.  
- [ ] **GPU computing** (CUDA, distributed training, multi-GPU setups).  
- [ ] **Container orchestration** (Docker, Kubernetes for ML workloads).  
- [ ] **Serverless ML** (AWS Lambda for inference, Modal, Banana, Replicate).  
- [ ] **Edge deployment** (TensorFlow Lite, ONNX Runtime, model optimization for edge devices).  
- [ ] **LLM hosting** (vLLM, TGI Text Generation Inference, Ollama for local models).

### ☁️ Understanding the Cloud (Business Perspective)

**Client-Server Foundation:**

- Your machine isn't the most powerful (would be too costly)
- Connect to remote machines as admin (e.g., via SSH)
- Users connect to servers for workloads (e.g., API calls)
- Compute and storage happen at the server
- Software evolved from monolith to modular

**Cloud Mindmap:**

- **Virtualization**: Server is no longer a single physical machine (resource efficiency)
- **Storage Solutions**: Various data storage options (S3, block, object storage)
- **Containerization**: Applications spin off containers
- **Orchestration**: Smart container management (Kubernetes)
- **PaaS**: Hosted application environments
- **Serverless**: Small, event-driven functions (Lambda)
- **Networking**: Zones, CDNs, load balancing

**On-Premise vs. Cloud Criteria:**

- Hardware costs vs. operational expenses
- Maintenance costs and staff requirements
- Security and compliance
- Speed and latency
- Flexibility and scalability
- Data ownership and control

**Economics of Cloud Computing:**

- **Virtualization** (hypervisor, VM) achieves higher hardware utilization
- **Decoupling**: Storage (S3) separate from compute (EC2)
- **Load switching** and containerization (Kubernetes, OpenShift)
- Network costs and data transfer pricing
- Data center economies of scale

**Cloud Providers:**

- **Major**: AWS (50% market share), GCP, Azure
- **Service Models**: SaaS / PaaS / IaaS
- **Vendor Lock-in**: Switching costs can be high
- **Competition**: EU antitrust investigations ongoing

**Important Trends:**

- "Managed" and "hybrid" clouds emerged
- Providers offer myriad of services (often with terrible APIs)
- Cannot easily switch providers
- Some companies "grow out of cloud" and return to on-premise

**Data Centers & Energy:**

- Hyperscalers vs. smaller providers
- Energy efficiency critical for sustainability

**Major Deals:**

- Broadcom buying VMware for $68B (2023)
- Microsoft settles EU cloud complaint for €22M (2024)

**Resources:**

- Microsoft: [Economics of the Cloud](https://news.microsoft.com/download/archived/presskits/cloud/docs/The-Economics-of-the-Cloud.pdf)
- Computer Weekly: Broadcom's VMware acquisition impact

### 🗄️ Databases and Storage

**Storage Fundamentals:**

- **HDD vs. SSD vs. Cloud (S3)**: Cost, speed, accessibility tradeoffs
- **File Systems**: HDFS (Hadoop Distributed File System)
- Disk costs and access time considerations

**Database Management Systems (DBMS):**

- **Relational Databases**: SQL-based (PostgreSQL, MySQL, Oracle, SQL Server)
- **NoSQL Types**:
  - Key-Value (Redis, DynamoDB)
  - Document (MongoDB, CouchDB)
  - Column (Cassandra, HBase)
  - Graph (Neo4j, Neptune)
  - **Vector** (Pinecone, Weaviate, ChromaDB, pgvector)
  - Time Series (InfluxDB, TimescaleDB)

**Database Popularity Rankings:**

- <https://db-engines.com/en/ranking>
- JetBrains Developer Ecosystem Survey
- Stack Overflow Developer Survey

**Large Data Processing:**

- **MapReduce**: Programming model for large datasets
- **Hadoop**: HDFS + YARN + MapReduce
- **Spark**: Fast, in-memory distributed computing

**Search Databases:**

- ElasticSearch, Splunk, Solr for full-text search

**Data Warehouses (DW):**

- Architecture: Decoupling storage and compute
- **Cloud Providers**: AWS (Redshift), GCP (BigQuery), Azure (Synapse)
- **New Players**: Snowflake, Databricks (venture-funded, high valuations)

**Database Theory:**

- Relational algebra and ER-diagrams
- **ACID** (Atomicity, Consistency, Isolation, Durability)
- **CAP Theorem** (Consistency, Availability, Partition Tolerance)
- **BASE** (Basically Available, Soft state, Eventually consistent)
- DDL (Data Definition Language) and DML (Data Manipulation Language)
- Normalization and normal forms
- Hashing and B-trees
- **OLAP** (Online Analytical Processing) vs. **OLTP** (Online Transaction Processing)

**Industry Consolidation:**

- Sun buys MySQL (2008), Oracle buys Sun (2010)
- SAP acquires Sybase (2010)
- Cloudera-Hortonworks merger (2019)
- Valkey: Redis fork after license change (2024)

**Learning Resources:**

- DuckDB co-founder: "The Ancient Art of Data Management" (2023 video)
- Lecture notes on database engineering (VSUUT, India)

### 🔧 Data Engineering Tools

**Data Engineering Lifecycle** (from Fundamentals of Data Engineering, O'Reilly):

```
Generation → Storage → Ingestion → Transformation → Serving
```

See also: [Exploring the Modern Data Warehouse](https://learn.microsoft.com/training/) by Microsoft Learn

**Workflow & Orchestration:**

- **Apache Airflow**: Most popular workflow orchestration
- **Prefect**, **Luigi**, **Dagster**: Modern alternatives
- **MLFlow**: ML lifecycle management

**Modern Data Stack:**

```
Data Sources → Ingestion → Storage → Transform → BI/Analytics
               (Fivetran)   (Snowflake) (dbt)     (Looker)
```

**Key Components:**

- Ingestion: Fivetran, Airbyte, Stitch
- Storage: Snowflake, Databricks, BigQuery
- Transform: dbt (data build tool), Spark
- BI: Looker, Tableau, PowerBI
- Reverse ETL: Census, Hightouch

**Additional Resources:**

- Andriy Burukov: MLOps book
- Data Engineering Zoomcamp
- MAD (ML/AI/Data) landscape: firstmark.com
- Reddit: Comments on weekly plan for DE job interview (pipeline2insights)

---

## **T3. Development Tools and Environment.**

- [ ] **Jupyter ecosystem** (JupyterLab, Jupyter notebooks, extensions, interactive computing).  
- [ ] **IDEs and AI coding assistants** (VS Code, Cursor, GitHub Copilot, Windsurf).  
- [ ] **Experiment tracking** (Weights & Biases, Neptune, Comet for reproducibility).  
- [ ] **Data labeling tools** (Label Studio, Prodigy, Scale AI for annotation).

#

# **P. Productisation**

Delivering value for users, business stakeholders and society from data and models.

Note: “model producisation” usually means two things – taking a model out of a single author usage to a workable system – thus making a pipeline, or designing a task ina  way that is likely to serve a business purpose

## **P1. Productisation and business value.**

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

### 🔄 ML Project Lifecycle Framework

**The Business-Driven ML Process:**

**A. Identify the Business Case**

- Hypothesis where you can earn more or save money
- Clear articulation of expected improvements
- Motivation: Why is this worth pursuing?

**B. Create the Adequate Model**

- Simplified representation of value chain or business process
- **Control points**: Where you make decisions and take actions
- **Data points**: Where you collect data to inform decisions and measure success

**C. State the Proposed Change**

- **Why**: Motivation and business justification
- **What/How/Where**: Detailed proposal
- **Success Criteria**: How to measure if it worked
- **Estimate ROI**: Is it worth the investment?
- **Test Plan**: Simplest way to validate the hypothesis

**D. Prove with Experiments**

- Run controlled tests
- Measure actual impact vs. expected
- Iterate based on results

**E. Scale or Pivot**

- If profitable: Scale the solution
- If not: Update model, change approach, or move to next opportunity
- Document lessons learned

**F. Continuous Improvement**

- Iterate faster, cheaper, with better outcomes
- Build feedback loops into production systems

### 👥 Data Team Roles & Responsibilities

**Perfect World (the "Bam" scenario):**

```
Idea → Good data → Known model → Quick inference → 
Bam to production → Bam cool effect → Bam business liked it
```

**Practically Perfect World (Reality):**

```
Many ideas → Business hypothesis → Expected result → 
Where to deploy? → Which model? → Is there data? → 
Can we train? → Does it work? → Can we deploy? → 
Production monitoring → Can we improve? → Is business happy? → 
How long will results persist?
```

**Role Breakdown - Who Does What?**

1. **Full-Stack Data Scientist** - End-to-end ownership: data → model → deployment
2. **Data Scientist / Modeler** - Focus on model development and experimentation
3. **Data Engineer / Data Architect** - Data pipelines, storage, and infrastructure
4. **Machine Learning Engineer** - Model deployment, serving, production optimization
5. **Software Engineers** - Application development and integration
6. **Research Scientist** - Novel algorithms and state-of-the-art research
7. **Business Analyst** - Requirements, metrics, stakeholder communication
8. **Business Lead / Product Manager** - Strategy, ROI, and product vision
9. **Vendor/Consultant** - External expertise and specialized tools

### 🚀 When Does a Pipeline Become a "Product"?

- Any pipeline that delivered business results (however simple)
- Complex systems beyond model+prediction (frontend, hardware, business rules)
- Anything with data/intelligence that users want
- Industry-specific sellable solutions

### ⚠️ Production Challenges

**Technical:** Data quality, model drift, infrastructure failures, integration issues

**Organizational:** Silos, vested interests, unclear responsibilities, misaligned incentives

**Business:** Unclear success criteria, changing requirements, insufficient ROI

### 📚 ML Production Resources

- **ITMO University Role Model**: <https://github.com/aimclub/ai-competency-model/>
- **Awesome Production ML**: <https://github.com/EthicalML/awesome-production-machine-learning>

**Key Insight from "Demystifying AI for the Enterprise":**
> Feedback loops and ongoing monitoring are most critical for production success.

---

## **P2. Applications, domains and cases**

- [ ] Recommender systems (RecSys).  
- [ ] Clinical trials.  
- [ ] Quality control and industrial automation.  
- [ ] Finance.  
- [ ] **Conversational AI and chatbots** (customer service, virtual assistants).  
- [ ] **Code generation** (GitHub Copilot, code assistants, automated programming).  
- [ ] **Document intelligence** (Q&A over documents, summarization, extraction).  
- [ ] **Search and information retrieval** (semantic search, hybrid search systems).

## **P3. Society impacts and regulation.**

- [ ] Fairness, biases, equity, human loop and ethics.  
- [ ] Grounds for AI regulation and policy.
- [ ] Generation-scale and wicked problems.  
- [ ] **AI safety and alignment** (value alignment, red teaming, adversarial testing).  
- [ ] **Prompt injection and security** vulnerabilities in LLM systems.  
- [ ] **Environmental impact** (carbon footprint of training large models).  
- [ ] **AI watermarking and detection** (synthetic content identification).  
- [ ] **Copyright and intellectual property** issues with generative AI.

# **E. Extra topics**

## **E1. Companies**

- [ ] ~~Academic vs corporate research.~~  
- [ ] ~~Company valuations.~~  
- [ ] ~~Data ownership.~~

---

# **Personalized Learning Roadmap**

This section provides a structured, phase-based approach to learning AI/ML, tailored for progressive skill building from foundations to advanced applications.

## 🎯 Your Current Position

**Phase 1 - Foundation** ✅ (You've completed tokenization basics)  
**Phase 2 - Embeddings & Vectors** 🎯 (You are here - working on embeddings)  
**Phase 3 - Neural Networks & Transformers** ⏭️ (Coming next)  
**Phase 4 - LLMs & Applications** 🔜 (Advanced topics)

---

## Phase 1: Foundation

**Core Concepts**

- [ ] Artificial Intelligence (AI)
- [ ] Machine Learning (ML)
- [ ] Supervised / Unsupervised / Semi‑Supervised Learning
- [ ] Reinforcement Learning (RL)
- [ ] Offline vs Online Machine Learning
- [ ] Overfitting, Underfitting, Bias, Variance

**Math & Statistics Basics**

- [ ] Loss Functions (Cross‑Entropy, Mean Squared Error)
- [ ] Optimization (gradients, backpropagation basics)
- [ ] L1 Norm, L2 Norm, Regularisation
- [ ] Probability (Naïve Bayes, distributions)

**Data Fundamentals**

- [ ] Features, Labels, Annotation
- [ ] Training/Validation/Testing Sets
- [ ] Feature Engineering & Feature Extraction
- [ ] Normalisation

---

## Phase 2: Embeddings & Vectors (Current Focus)

**Tokenization**

- [ ] Tokens - Text broken into processable units
- [ ] Tokenization algorithms (BPE, WordPiece)
- [ ] Subword tokenization concepts

**Embeddings** 🔥 (Learn next)

- [ ] Embeddings - Dense vector representations
- [ ] Word2Vec, fastText, Doc2Vec
- [ ] Semantic meaning in vector space
- [ ] Cosine Similarity - Measuring semantic similarity
- [ ] Vector operations (addition, subtraction, distance)

**Vector Storage & Retrieval**

- [ ] Vector Database (Pinecone, Weaviate, ChromaDB)
- [ ] Semantic search vs keyword search
- [ ] Nearest neighbor search
- [ ] Dimensionality (384, 768, 1536 dimensions)

**Text Representations (Classical)**

- [ ] Bag of Words, N‑grams (Bigrams, Trigrams)
- [ ] TF (Term Frequency), IDF (Inverse Document Frequency)
- [ ] TF‑IDF weighting

---

## Phase 3: Neural Networks & Architecture

**Neural Network Basics**

- [ ] Neural Networks, Hidden Layers
- [ ] Activation Functions (ReLU, sigmoid, tanh)
- [ ] Backpropagation (in depth)
- [ ] Gradient descent & optimization
- [ ] Epoch, Batch Size, Learning rate
- [ ] Dropout, Regularization techniques

**Deep Learning Architectures**

- [ ] Deep Learning fundamentals
- [ ] CNNs (Convolutional Neural Networks) - for images
- [ ] RNNs (Recurrent Neural Networks) - for sequences
- [ ] LSTMs (Long Short-Term Memory) - for long sequences
- [ ] Autoencoders - dimensionality reduction

**Attention & Transformers** 🌟

- [ ] Attention Mechanism - focusing on relevant parts
- [ ] Self-Attention - all tokens attend to each other
- [ ] Multi-Head Attention - multiple attention in parallel
- [ ] Transformer Architecture - the foundation of modern NLP
- [ ] Encoder-Decoder Architecture
- [ ] Positional Encoding

---

## Phase 4: LLMs & Modern AI 🚀

**Large Language Models**

- [ ] LLMs (Large Language Models) - GPT, Claude, LLaMA
- [ ] GPT (Generative Pre-trained Transformer)
- [ ] BERT (Bidirectional Encoder Representations)
- [ ] Foundation Models - pre-trained models
- [ ] Context Window - token limits
- [ ] Perplexity - model evaluation

**Working with LLMs**

- [ ] Prompt Engineering - crafting effective prompts
- [ ] Temperature - controlling randomness
- [ ] Few-Shot / One-Shot / Zero-Shot Learning
- [ ] In-Context Learning
- [ ] Chain-of-Thought (CoT) prompting
- [ ] Instruction Tuning

**Fine-tuning & Optimization**

- [ ] Transfer Learning
- [ ] Fine-tuning pre-trained models
- [ ] LoRA (Low-Rank Adaptation) - efficient fine-tuning
- [ ] Quantization - 4-bit, 8-bit model compression
- [ ] Distillation - creating smaller models
- [ ] RLHF (Reinforcement Learning from Human Feedback)

**RAG & Knowledge Systems**

- [ ] RAG (Retrieval Augmented Generation) 🔥
- [ ] Information Retrieval (IR)
- [ ] Semantic search with embeddings
- [ ] Combining retrieval + generation
- [ ] Knowledge Graphs

---

## Phase 5: Specialized Domains

**Natural Language Processing (NLP)**

- [ ] NLP fundamentals
- [ ] Named Entity Recognition (NER)
- [ ] Sentiment Classification
- [ ] Machine Translation (MT)
- [ ] Sequence‑to‑Sequence (Seq2Seq)
- [ ] Abstractive vs Extractive Summarisation
- [ ] Natural Language Generation (NLG)
- [ ] Chatbots & conversational AI

**Computer Vision (CV)**

- [ ] Computer Vision concepts
- [ ] CNN applications (classification, detection)
- [ ] Image embeddings (CLIP)
- [ ] Stable Diffusion - text-to-image
- [ ] Diffusion Models
- [ ] GANs (Generative Adversarial Networks)
- [ ] Multimodal AI - text + vision

**Advanced Topics**

- [ ] AI Agents - autonomous decision-making
- [ ] Mixture of Experts (MoE)
- [ ] Active Learning
- [ ] Recommender Systems
- [ ] Anomaly Detection
- [ ] Human in the Loop (HITL) systems

---

## Phase 6: ML Engineering & Production

**Model Evaluation**

- [ ] Accuracy, Precision, Recall, F1 Score
- [ ] Cross‑Validation
- [ ] Confusion Matrix
- [ ] BLEU, ROUGE (for generation tasks)

**Data Engineering**

- [ ] Data pipelines
- [ ] ETL (Extract, Transform, Load)
- [ ] Data versioning
- [ ] Batch vs streaming processing

**ML Tools & Libraries**

- [ ] NumPy - numerical computing
- [ ] Pandas - data manipulation
- [ ] Scikit‑Learn - classical ML
- [ ] PyTorch / TensorFlow / Keras - deep learning
- [ ] Hugging Face Transformers
- [ ] LangChain - LLM applications

**MLOps & Deployment**

- [ ] ML Pipelines (Kedro, Airflow)
- [ ] Model versioning & monitoring
- [ ] Cloud platforms (AWS SageMaker, Azure ML, GCP)
- [ ] API deployment (FastAPI, Flask)
- [ ] Model serving & inference optimization
- [ ] A/B testing

---

## Phase 7: Ethics, Safety & Advanced Concepts

**AI Safety & Alignment**

- [ ] Hallucination - factual accuracy issues
- [ ] Alignment - matching human values
- [ ] Constitutional AI
- [ ] Prompt Injection - security concerns
- [ ] Bias & fairness in AI
- [ ] Explainability & interpretability

**Model Types Comparison**

- [ ] Generative vs Discriminative models
- [ ] Supervised vs Unsupervised vs RL
- [ ] Rules‑Based vs ML-based systems
- [ ] Classical ML vs Deep Learning tradeoffs

---

## 📚 Learning Resources by Phase

**Phase 1-2 (Foundation + Embeddings):**

- [ ] Start with your current examples: `tiktoken_example.py`, `embeddings_intro.py`
- [ ] Practice: Create embeddings for different texts, compare similarities
- [ ] Build: Simple semantic search with your own documents

**Phase 3 (Neural Networks):**

- [ ] Implement: Simple neural network from scratch
- [ ] Study: 3Blue1Brown neural network series
- [ ] Practice: MNIST digit classification with PyTorch

**Phase 4 (LLMs):**

- [ ] Use: OpenAI API, Anthropic Claude, or local LLMs
- [ ] Build: RAG system with your own knowledge base
- [ ] Practice: Prompt engineering for different tasks

**Phase 5+ (Specialization):**

- [ ] Choose your focus: NLP, CV, or multimodal
- [ ] Build end-to-end projects
- [ ] Contribute to open source (Hugging Face, LangChain)

## 🤖 Microsoft Agent Frameworks & Courses

Microsoft offers a comprehensive ecosystem of AI/agent frameworks, educational courses, and development tools. This section provides a structured learning path through Microsoft's offerings.

### 🎓 Educational Courses & Tutorials

#### AI Agent Development

- [ ] **[AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)** ⭐ 45k stars
  - 15-lesson curriculum covering agent fundamentals to production
  - Topics: Introduction to agents → Agent patterns → Production deployment
  - Hands-on examples with Python and practical implementations
  - 15.2k forks, 422 watchers - highly active community

#### Model Context Protocol (MCP)

- [ ] **[MCP for Beginners](https://github.com/microsoft/mcp-for-beginners)** ⭐ 13.3k stars
  - 11 modules on Model Context Protocol
  - Emerging standard for AI-tool communication
  - Multi-language support: C#, Java, JavaScript, Python, Rust, TypeScript
  - 4.3k forks - growing adoption

#### IoT Development

- [ ] **[IoT for Beginners](https://github.com/microsoft/IoT-For-Beginners)** ⭐ 16.6k stars
  - 24 lessons covering complete IoT development lifecycle
  - Topics: Sensors → Cloud integration → Production systems
  - Practical projects: Farm → Transport → Manufacturing → Retail → Consumer
  - 2.7k forks

#### Python Fundamentals

- [ ] **[Python for Beginners](https://github.com/microsoft/c9-python-getting-started)** ⭐ 7.9k stars
  - Channel 9 series with 3-course progression
  - Beginner-friendly introduction to Python programming
  - Foundation for ML/AI development

#### GitHub Copilot & AI-Assisted Development

- [ ] **[GitHub Copilot Tutorial](https://github.com/features/copilot)** - Comprehensive guide
  - **Mission Control**: Multi-step workflows in VS Code
  - **Agent Mode**: Autonomous coding with feedback loops
  - **Copilot CLI**: Terminal integration (`copilot explain`, `copilot fix tests`)
  - **Code Review**: Automated PR review with risk detection
  - **Coding Agent**: Async task handling with issue assignments
  - **Best Practices**: Review everything, prompt with context, small increments
  - **Prompt Patterns**: Specific examples for caching, CSV import, test generation

### 🔧 Agent Frameworks & Tools

#### Core Agent Frameworks

- [ ] **[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)** ⭐ 5.1k stars
  - Core offering for building AI agents
  - Python and .NET support
  - Layered API design: Core API → AgentChat API → Extensions
  - Production-ready architecture

- [ ] **[Agent Lightning](https://github.com/microsoft/agent-lightning)** ⭐ 8.5k stars
  - RL training framework for any agent
  - Works with minimal code changes
  - Enables reinforcement learning without framework lock-in

- [ ] **[AutoGen](https://github.com/microsoft/autogen)** ⭐ 51.7k stars (Legacy/Maintained)
  - Multi-agent framework (original Microsoft offering)
  - Now directing users to Microsoft Agent Framework
  - Still maintained but considered legacy
  - Large community and extensive examples

#### Prompt Engineering & Orchestration

- [ ] **[POML (Prompt Orchestration Markup Language)](https://github.com/microsoft/poml)** ⭐ 4.7k stars
  - Markup language for prompt engineering
  - HTML-like syntax for structured prompts
  - VS Code extension available
  - Declarative approach to prompt design

- [ ] **[GenAIScript](https://github.com/microsoft/genaiscript)** ⭐ 2.8k stars
  - JavaScript/TypeScript framework for programmatic prompt assembly
  - Compose prompts with code logic
  - Integrate with existing workflows
  - Type-safe prompt construction

#### AI Development & Testing Tools

- [ ] **[PromptBench](https://github.com/microsoft/promptbench)** ⭐ 2.7k stars
  - Python library for LLM evaluation and benchmarking
  - Adversarial testing capabilities
  - Dynamic evaluation frameworks
  - Performance metrics and analysis

- [ ] **[Intelligence Toolkit](https://github.com/microsoft/intelligence-toolkit)** ⭐ 94 stars
  - Interactive workflows for AI intelligence reports
  - Case/entity/text intelligence analysis
  - Data-driven insights generation
  - Production intelligence workflows

#### Development Environment & Tools

- [ ] **[VS Code Tools for AI](https://github.com/microsoft/vscode-tools-for-ai)** ⭐ 340 stars
  - Azure ML VS Code extension
  - Build, train, and deploy ML models
  - Integrated development experience
  - Azure Machine Learning integration

### 📚 Learning Path Recommendations

#### Beginner Path (Start Here)

1. ✅ **Python for Beginners** - Get comfortable with Python
2. ✅ **AI Agents for Beginners** - Learn agent fundamentals (Lessons 1-5)
3. ✅ **GitHub Copilot Tutorial** - Familiarize with AI-assisted coding
4. ✅ **MCP for Beginners** - Understand the protocol standard (Modules 1-3)

#### Intermediate Path

1. ✅ **AI Agents for Beginners** - Complete remaining lessons (6-15)
2. ✅ **Microsoft Agent Framework** - Build your first agent
3. ✅ **GenAIScript** or **POML** - Choose your prompt engineering approach
4. ✅ **PromptBench** - Test and evaluate your models

#### Advanced Path

1. ✅ **Agent Lightning** - Add RL capabilities to agents
2. ✅ **AutoGen** (optional) - Explore multi-agent patterns
3. ✅ **Intelligence Toolkit** - Production intelligence workflows
4. ✅ **MCP for Beginners** - Complete advanced modules (8-11)

---

## 🎤 Interviews & Career Insights

### Featured Interview: randomlyCoding

**Topic:** Production pipelines, engineering skills and job roles

**Key Takeaways:**

- Importance of understanding production systems beyond modeling
- Skills balance: modeling + engineering + business understanding
- Real-world constraints differ significantly from academic projects
- Team collaboration and communication are critical skills

**Full Interview:** Available on MLMW website

### Essential for Job Success

**Must-Have Cloud Knowledge:**
> "One thing I would say is usually a *must* is familiarity with Linux and a cloud provider (AWS, GCP, Azure). You don't need to know all 3 cloud providers (pick AWS if you don't know any yet - it has 50% market share) but if you don't know any of them it'll be harder to onboard you and your first few weeks would be a lot more overwhelming – even knowing a different one to the one you use at a specific job will help as they all have similar functionality."

**Interview Preparation Resources:**

- **CIS 4190/5190: Applied Machine Learning** (Spring 2023) - Great list of resources on one page
- **deepmleet** (deepmleet.streamlit.app) - The leetcode of machine learning
- **Society of Actuaries (SOA)**: Statistics for Risk Modeling (SRM) Exam
  - Note: Topics are solid but literature slightly dated (ISLR instead of ISLP)

---

## 👥 Influential Educators & Thinkers

People who make complex things accessible through courses, books, and personal interaction:

### Highly Recommended Educators

- **Will Curt** - Clear explanations of statistical concepts
- **Scott Cunningham** - Causal Inference: The Mixtape author
- **Laura Mayoral** - Econometrics educator
- **Allen Downey** (r/AllenDowney/) - Think Stats, Think Bayes author

### Active Researchers on Social Media

Many professors and textbook authors are surprisingly reachable:

- **Jeffrey Wooldridge** (@jmwooldridge) - Econometrics
- **Paul Goldsmith-Pinkham** (@paulgp)
  - Repo: Yale Applied Empirical Methods PhD Course
  - Video lectures available (PGP playlist)

### Video Content Creators

Already covered in Video Series section:

- Josh Starmer (StatQuest) - "This man is a genius"
- Grant Sanderson (3Blue1Brown) - "Very high quality content"
- Andrej Karpathy - Transformer architecture deep dives

### Additional Recommendation

- **Machine Learning Street Talk**
  - Reader note: "Sometimes a bit too dense for absolute beginners but really good. They list resources, papers, books."

### Hall of Shame

- **Siraj Raval** - Story of plagiarism in education (cautionary tale)

---

## 📖 Professional Glossary & Common Terms

### Common ML Terms

**Supervised vs. Unsupervised vs. Semi-Supervised Learning:**

- **Supervised**: Learning with labeled data (input-output pairs)
- **Unsupervised**: Learning patterns from unlabeled data (clustering, dimensionality reduction)
- **Semi-Supervised**: Combination of labeled and unlabeled data

**Structured vs. Unstructured Data:**

- **Structured**: Organized in tables/databases (SQL, CSV, Excel)
- **Unstructured**: No predefined format (text, images, audio, video)

### Professional Slang

**Feature Engineering:**

- Variable selection and transformation
- Creating new features from existing data
- Domain knowledge applied to improve model inputs

**ETL vs. ELT:**

- **ETL** (Extract, Transform, Load): Traditional data integration - transform before loading
- **ELT** (Extract, Load, Transform): Modern approach - transform after loading into warehouse

### Fading Buzzwords

**Data Mining:** (1990s-2000s)

- Early term for discovering patterns in data
- Largely replaced by "machine learning" and "analytics"

**Big Data:** (2010s)

- Emphasis on volume, velocity, variety (3 Vs)
- Now implicit in "data engineering" and "cloud computing"
