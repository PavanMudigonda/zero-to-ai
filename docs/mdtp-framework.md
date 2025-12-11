# mdtp framework
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

