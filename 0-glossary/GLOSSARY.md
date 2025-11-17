A
Abstractive Summarisation
Abstractive summarisation is a summarisation technique that generates language using word tokens and phrases not necessarily found in the source document. In contrast, extractive summarisation draws phrases and sentences directly from the source text based on a measure of salience. The degree to which a summary is abstractive versus extractive can often be controlled by a continuous model hyperparameter that explicitly handles this trade‑off.

ACID (Atomicity, Consistency, Isolation, Durability)
ACID is a set of properties that guarantee reliable database transactions: Atomicity (all-or-nothing execution), Consistency (valid state transitions), Isolation (concurrent transactions don't interfere), and Durability (committed changes persist even after system failures).

Accuracy
Accuracy is a measurement in classification problems used to quantify a model's performance. It is the number of correct predictions as a percentage of the total number of predictions made. Correct predictions include both True Positives (TP) and True Negatives (TN).

Activation Function
Activation functions are functions used in neural networks to transform the weighted sum of inputs and biases, which is then used to decide whether a neuron is activated or not.

Active Learning
Active learning is a special case of machine learning in which a learning algorithm can interactively query a user (or oracle) to label new data points. The algorithm selects which data points to label based on how informative they are for improving the model.

AI Skill
An AI skill is a specific capability that an AI system possesses, such as image recognition, natural language processing, decision‑making, or summarization. AI skills are typically developed using machine learning and are designed to automate, augment, or mimic human tasks.

Algorithm
An algorithm is an exact list of instructions that conducts specified actions step by step in hardware or software to solve a particular problem.

Annotation
Annotation is the (often manual) process of generating metadata or labels for a source document. Examples include topic tags, photo captions, or named entities. Annotation is essential for supervised learning, where labeled data is required for training models.

Anomaly Detection
Anomaly detection is the process of identifying data points, entities, or events that deviate significantly from the norm. It is widely used in fraud detection, monitoring, and fault detection.

Artificial Intelligence (AI)
Artificial Intelligence is a field of computer science focused on creating systems that can perform tasks that typically require human intelligence, such as understanding language, recognizing patterns, and making decisions.

Autoencoder
An autoencoder is a type of neural network used to learn efficient codings (representations) of data in an unsupervised manner, often for dimensionality reduction or denoising.

AutoML (Automated Machine Learning)
AutoML refers to tools and processes that automate the end‑to‑end process of applying machine learning to real‑world problems, including model selection, hyperparameter tuning, and feature preprocessing.

B
Backpropagation
Backpropagation is an algorithm used to compute gradients of a loss function with respect to model parameters in neural networks, enabling efficient training via gradient‑based optimization.

Bag of Words (BoW)
Bag of Words is a simplified representation for text, where a document is represented as an unordered collection of its words (often with term frequencies), disregarding grammar and word order.

BASE (Basically Available, Soft state, Eventually consistent)
BASE is a database consistency model alternative to ACID, commonly used in NoSQL databases, prioritizing availability and partition tolerance over immediate consistency, accepting that data will become consistent eventually.

Batch Size
Batch size is the number of training examples used in one iteration of model parameter updates during training.

BigQuery
BigQuery is Google Cloud's fully managed, serverless data warehouse that enables fast SQL queries on large datasets using Google's infrastructure, designed for analytics and business intelligence workloads.

BERT (Bidirectional Encoder Representations from Transformers)
BERT is a deep learning model based on the Transformer architecture that learns contextual representations of words by looking both left and right in a sentence. It achieves state‑of‑the‑art performance on many NLP tasks.

Bias (Model Bias)
Bias is error introduced by approximating a real‑world problem with a simplified model. High bias can cause underfitting, where the model fails to capture relevant patterns in the data.

Big Data
Big data informally refers to datasets whose size or complexity exceed the capacity of typical personal‑computer storage and processing, often requiring distributed storage and computing resources.

Bigrams
Bigrams are sequences of two adjacent tokens (usually words) in text. They are a specific case of n‑grams with n = 2 and are used in language modeling and feature extraction.

BLEU (Bilingual Evaluation Understudy)
BLEU is an automatic metric for evaluating the quality of machine‑translated text by comparing it to one or more human reference translations.

C
CAP Theorem (Consistency, Availability, Partition Tolerance)
The CAP theorem states that a distributed database system can only guarantee two of three properties simultaneously: Consistency (all nodes see the same data), Availability (every request receives a response), and Partition Tolerance (system continues despite network failures).

Cassandra
Cassandra is an open-source, distributed NoSQL database designed for handling large amounts of data across many servers with high availability and no single point of failure, using a column-family data model.

Chatbot
A chatbot is an AI application that interacts with users via natural language, typically in text or speech, to simulate conversation and answer questions or guide users through workflows.

Classification
Classification is a supervised learning task where the goal is to predict a discrete label (e.g., spam/not spam, class A/B/C) for each input.

Cloud (Cloud Computing)
Cloud refers to remote servers accessed over the internet that provide on‑demand computing resources such as storage, processing, and machine learning services.

CDN (Content Delivery Network)
A CDN is a distributed network of servers that deliver web content and media to users based on their geographic location, reducing latency and improving performance.

Clustering
Clustering is an unsupervised learning technique that groups data points so that those in the same group (cluster) are more similar to each other than to those in other groups.

Containerization
Containerization packages applications and their dependencies into isolated containers that can run consistently across different computing environments, enabling portability and scalability.

Computer Vision
Computer vision is a field of AI focused on enabling machines to interpret and process visual information from images and videos.

Convolutional Neural Network (CNN)
A CNN is a neural network architecture well‑suited for grid‑like data (e.g., images). It uses convolutional layers to automatically learn spatial hierarchies of features.

Cross‑Entropy Loss
Cross‑entropy loss is a loss function commonly used for classification tasks where the model predicts probability distributions over classes.

Cross‑Validation
Cross‑validation is a resampling technique used to evaluate model performance by splitting data into multiple train/validation subsets and averaging the results.

D
Data Warehouse
A data warehouse is a centralized repository that stores integrated data from multiple sources, optimized for analytical queries and business intelligence, typically using a star or snowflake schema design.

DBMS (Database Management System)
A DBMS is software that manages databases, providing an interface for creating, reading, updating, and deleting data while ensuring data integrity, security, and concurrent access control.

Decision Tree
A decision tree is a model that makes predictions by recursively splitting data according to feature‑based rules, forming a tree of decisions.

Deep Learning (DL)
Deep learning is a subset of machine learning that uses neural networks with many layers (deep architectures) to learn complex patterns from large datasets.

Docker
Docker is a platform for developing, shipping, and running applications in containers, providing a standardized way to package software with all dependencies included.

Doc2Vec
Doc2Vec is an unsupervised algorithm for learning fixed‑length vector representations of variable‑length documents.

Dropout
Dropout is a regularization technique where a random subset of neurons or connections is temporarily removed during training to reduce overfitting.

E
EC2 (Elastic Compute Cloud)
EC2 is Amazon Web Services' cloud computing service that provides resizable virtual servers (instances) for running applications in the cloud.

Embeddings
Embeddings are dense, low‑dimensional vector representations of high‑dimensional or categorical objects (such as words or items), capturing semantic relationships.

Entity
An entity is a real‑world item or concept of interest, such as a person, organization, location, or product.

Epoch
An epoch is one full pass of the entire training dataset through the learning algorithm.

Extractive Summarisation
Extractive summarisation produces a summary by selecting and concatenating key sentences or phrases directly from the original text.

F
F1 Score
F1 score is the harmonic mean of precision and recall, providing a balanced measure of a classifier's accuracy, especially on imbalanced datasets.

fastText
fastText is a lightweight library for learning word and text representations and performing fast text classification.

Feature Engineering
Feature engineering is the process of creating or transforming variables (features) from raw data to improve model performance.

Feature Extraction
Feature extraction converts raw data into numerical features while retaining the most important information.

Features
Features are the measurable properties or characteristics used as inputs to a machine learning model.

Few‑Shot Learning
Few‑shot learning refers to training models that can generalize well from a very small number of labeled examples per class.

G
Generative (Model)
A generative model learns the joint distribution of inputs and outputs and can generate new data instances. This contrasts with discriminative models, which model decision boundaries between classes.

Graph
A graph is a data structure consisting of nodes (vertices) and edges that represent relationships between entities.

H
Hadoop
Hadoop is an open-source framework for distributed storage and processing of large datasets across clusters of computers, consisting of HDFS (storage) and MapReduce/YARN (processing).

HDFS (Hadoop Distributed File System)
HDFS is a distributed file system designed to store very large files across multiple machines with high fault tolerance through data replication, serving as the storage layer of the Hadoop ecosystem.

Hidden Layer
A hidden layer is an intermediate layer in a neural network between the input and output layers, where learned feature transformations occur.

Human in the Loop (HITL)
Human in the loop describes systems in which humans interact with and guide AI models, for example by providing feedback, labels, or overrides.

Hypervisor
A hypervisor is software that creates and manages virtual machines by abstracting physical hardware resources, enabling multiple operating systems to run on a single physical machine.

I
IaaS (Infrastructure as a Service)
IaaS is a cloud computing model that provides virtualized computing resources (servers, storage, networking) over the internet on a pay-as-you-go basis.

Inference (Model Inference)
Inference is the process of using a trained machine learning model to make predictions on new, unseen data.

Information Extraction (IE)
Information extraction is the process of automatically identifying and structuring specific pieces of information (e.g., entities, relations) from unstructured text.

Information Retrieval (IR)
Information retrieval is the process of finding relevant documents or document segments that satisfy an information need, typically in search systems.

Inverse Document Frequency (IDF)
Inverse document frequency is a statistic that downweights terms that occur in many documents and upweights rare terms, often used in TF‑IDF weighting.

K
Kedro
Kedro is an open‑source Python framework for building robust, maintainable data and machine learning pipelines.

Keras
Keras is a high‑level deep learning API written in Python, running on top of backends like TensorFlow, designed for fast experimentation.

Knowledge Graph
A knowledge graph is a knowledge base structured as a graph of entities (nodes) and relationships (edges), often used for reasoning, search, and recommendation.

Kubernetes
Kubernetes is an open-source container orchestration platform that automates deployment, scaling, and management of containerized applications across clusters of machines.

L
Label
A label is the target output associated with an input in supervised learning, such as class IDs or numeric values.

Lambda (AWS Lambda)
Lambda is a serverless computing service that runs code in response to events without requiring server management, executing functions on-demand and scaling automatically.

L1 Norm
The L1 norm (Manhattan distance) is the sum of absolute differences between vector components, often used in L1 regularization (Lasso) to promote sparsity.

L2 Norm
The L2 norm (Euclidean distance) is the square root of the sum of squared differences between vector components, commonly used in L2 regularization (Ridge).

Logistic Regression
Logistic regression is a supervised algorithm for binary (or multi‑class) classification that models the probability of class membership using a logistic function.

Loss Function
A loss function quantifies the difference between a model's predictions and the true targets, guiding the optimization process.

Low‑Shot Learning
Low‑shot learning is another term for few‑shot learning, where models must generalize from limited labeled data.

LSTM (Long Short‑Term Memory)
LSTM networks are a type of recurrent neural network designed to capture long‑term dependencies in sequential data using gating mechanisms.

M
Machine Learning (ML)
Machine learning is a subfield of AI that focuses on algorithms that learn patterns from data and improve their performance with experience.

Machine Reading
Machine reading refers to systems that can read, understand, and reason over unstructured text to answer questions and perform complex language tasks.

Machine Translation (MT)
Machine translation is the automatic translation of text from one natural language to another using computational models.

MapReduce
MapReduce is a programming model for processing large datasets in parallel across distributed clusters by breaking computation into Map (filtering/sorting) and Reduce (aggregating) phases.

Mean Squared Error (MSE)
Mean squared error is a common loss function for regression, defined as the average of squared differences between predicted and true values.

MongoDB
MongoDB is a popular open-source NoSQL database that stores data in flexible, JSON-like documents (BSON format), enabling schema flexibility and horizontal scaling.

MySQL
MySQL is an open-source relational database management system using SQL, widely used for web applications and known for speed, reliability, and ease of use.

N
Naïve Bayes
Naïve Bayes is a family of probabilistic classifiers that assume independence between features given the class label, often used for text classification.

Named Entity Recognition (NER)
Named entity recognition is the NLP task of identifying and classifying spans of text into predefined categories such as person, organization, or location.

Natural Language Generation (NLG)
Natural language generation is the process of producing human‑readable text from structured data or internal model representations.

Natural Language Processing (NLP)
Natural language processing is a field at the intersection of AI, linguistics, and computer science that focuses on enabling computers to understand, interpret, and generate human language.

Neo4j
Neo4j is a graph database management system that uses nodes, relationships, and properties to represent and store data, optimized for querying complex connected data and relationships.

Network (Neural / Computing Network)
In AI, a network often refers to a neural network—a computing system of interconnected nodes analogous to neurons, or to the broader computing network of interconnected machines.

NoSQL
NoSQL databases are non-relational database systems designed for flexible schemas, horizontal scalability, and handling large volumes of unstructured or semi-structured data, including document, key-value, column-family, and graph databases.

N‑grams
N‑grams are contiguous sequences of n items (often words or characters) from a document or corpus, used in language modeling and feature extraction.

Normalisation (Normalization)
Normalization is the process of scaling or transforming data to a common scale or distribution, often to stabilize and improve learning.

NumPy
NumPy is a core Python library for numerical computing, providing n‑dimensional arrays and efficient mathematical operations.

O
OLAP (Online Analytical Processing)
OLAP systems are optimized for complex analytical queries on large historical datasets, supporting multidimensional analysis, aggregations, and business intelligence reporting with slower write speeds but fast read performance.

OLTP (Online Transaction Processing)
OLTP systems are optimized for handling high volumes of short, fast transactions (inserts, updates, deletes) with ACID guarantees, prioritizing data integrity and consistency for operational applications.

Offline Machine Learning
Offline machine learning trains models on a fixed dataset, without updating the model parameters continuously as new data arrives.

Online Machine Learning
Online machine learning updates models incrementally as new data arrives, making it suitable for streaming or non‑stationary environments.

Optimisation (Optimization)
Optimization is the process of adjusting model parameters to minimize a loss function or maximize performance.

Overfitting
Overfitting occurs when a model memorizes noise or specific patterns in the training data and fails to generalize to new, unseen data.

P
Pandas
Pandas is a Python library offering data structures and tools for data manipulation and analysis, especially for tabular data.

PaaS (Platform as a Service)
PaaS is a cloud computing model that provides a platform with development tools, databases, and runtime environments, allowing developers to build and deploy applications without managing underlying infrastructure.

Pipeline (ML Pipeline)
A machine learning pipeline is a structured workflow that chains data processing, feature extraction, model training, and evaluation steps into a reproducible process.

Polly
Polly is a text‑to‑speech service (e.g., in cloud platforms) that converts text into natural‑sounding speech.

PostgreSQL
PostgreSQL is an advanced open-source relational database system known for robustness, extensibility, and standards compliance, supporting complex queries, JSON data, full-text search, and custom data types.

Precision
Precision is the ratio of true positive predictions to all positive predictions, measuring how many predicted positives are correct.

PyTorch
PyTorch is an open‑source deep learning framework that provides tensor operations and automatic differentiation, widely used for research and production.

R
Redis
Redis is an open-source, in-memory key-value data store known for extremely fast performance, used for caching, session management, real-time analytics, and message queuing.

Random Forest
Random forest is an ensemble learning method that combines predictions from many decision trees to improve robustness and accuracy.

Recall
Recall is the ratio of true positive predictions to all actual positive instances, measuring how many of the real positives are recovered by the model.

Recommender System
A recommender system suggests relevant items (such as products, movies, or documents) to users based on preferences, behavior, and item similarity.

Recurrent Neural Network (RNN)
RNNs are neural networks with cyclic connections that allow information to persist over time, making them useful for sequential data.

Regression
Regression is a supervised learning task that predicts continuous numeric values (e.g., price, temperature) from input features.

Regular Expression (Regex)
A regular expression is a sequence of characters that defines a search pattern, often used for text matching and extraction.

Regularisation (Regularization)
Regularization refers to techniques that constrain model complexity to reduce overfitting, such as L1/L2 penalties or dropout.

Reinforcement Learning (RL)
Reinforcement learning is a learning paradigm where an agent interacts with an environment, taking actions to maximize cumulative reward.

Rekognition
Rekognition is a cloud‑based service for image and video analysis, providing capabilities like object detection and face recognition.

Representation Learning
Representation learning is a set of techniques allowing models to automatically learn useful feature representations from raw data.

ROUGE
ROUGE is a set of metrics for evaluating automatic summarization and machine translation by comparing system output to reference summaries.

Rules‑Based (Rule‑Based Systems)
Rule‑based systems rely on hand‑crafted rules and logic to make decisions, instead of learned parameters from data.

S
S3 (Simple Storage Service)
S3 is Amazon Web Services' object storage service that provides scalable, durable, and secure storage for files and data, commonly used for data lakes, backups, and static content hosting.

SaaS (Software as a Service)
SaaS is a cloud computing model where software applications are hosted by a provider and accessed by users over the internet, typically through a web browser on a subscription basis.

SageMaker
SageMaker is a fully managed cloud service for building, training, and deploying machine learning models at scale.

Scikit‑Learn
Scikit‑learn is a popular Python library providing tools for supervised and unsupervised learning, model selection, and preprocessing.

SciPy
SciPy is a Python ecosystem and library for scientific and technical computing, built on top of NumPy.

Snowflake
Snowflake is a cloud-based data warehousing platform that separates storage and compute, enabling elastic scaling, multi-cloud support, and SQL-based analytics on structured and semi-structured data.

Spark (Apache Spark)
Spark is an open-source distributed computing framework for big data processing that performs in-memory computation, making it much faster than MapReduce for iterative algorithms and interactive analytics.

SQL (Structured Query Language)
SQL is a standardized programming language for managing and querying relational databases, using commands like SELECT, INSERT, UPDATE, and DELETE to manipulate structured data in tables.

Semi‑Supervised Machine Learning
Semi‑supervised learning uses both labeled and unlabeled data during training, typically a small labeled set with a much larger unlabeled set.

Sentiment Classification
Sentiment classification is the task of determining the sentiment (e.g., positive, negative, neutral) expressed in text.

Sequence‑to‑Sequence (Seq2Seq)
Seq2Seq models map input sequences (e.g., sentences) to output sequences (e.g., translations), often using encoder‑decoder architectures.

Serverless
Serverless computing is a cloud execution model where the cloud provider dynamically manages server allocation, allowing developers to run code without provisioning or managing servers, paying only for actual compute time used.

Supervised Machine Learning
Supervised learning involves training models on labeled data, where each input has a corresponding known output.

Support Vector Machine (SVM)
SVM is a supervised learning algorithm that finds the hyperplane that best separates classes in a high‑dimensional feature space.

T
Tensor
A tensor is a multi‑dimensional generalization of scalars, vectors, and matrices, used as the fundamental data structure in many deep learning frameworks.

TensorFlow
TensorFlow is an open‑source platform for building and deploying machine learning models, offering a comprehensive ecosystem of tools and libraries.

Term Frequency (TF)
Term frequency is the number of times a term appears in a document, often normalized by document length.

Term Frequency–Inverse Document Frequency (TF‑IDF)
TF‑IDF is a weighting scheme that combines term frequency and inverse document frequency to measure the importance of a term in a document relative to a corpus.

Testing Set (Test Set)
A test set is a dataset held out from training, used to provide an unbiased evaluation of a final model's performance.

Tokens
Tokens are the basic units into which text is split for processing, such as words, subwords, or characters.

Training (Model Training)
Training a model means adjusting its parameters (e.g., weights and biases) using labeled data to minimize a loss function.

Training Set
A training set is the dataset used to fit the parameters of a model.

Transfer Learning
Transfer learning reuses a model trained on one task as a starting point for another related task, saving computation and improving performance with limited data.

Transformer
The Transformer is a deep learning architecture that relies on self‑attention mechanisms to process sequences, widely used in NLP for tasks like translation and summarization.

Trigrams
Trigrams are n‑grams with n = 3, representing contiguous sequences of three tokens, commonly used for language modeling and text analysis.

U
Underfitting
Underfitting occurs when a model is too simple to capture underlying patterns in the data, performing poorly on both training and test sets.

Unsupervised Machine Learning
Unsupervised learning uses unlabeled data to discover hidden patterns or structures, such as clusters or latent factors.

V
Validation Set
A validation set is a subset of data used during training to tune hyperparameters and select models, separate from both training and test sets.

Variance (Model Variance)
Variance is the sensitivity of a model's predictions to small changes in the training data. High variance models tend to overfit.

Virtualization
Virtualization is the technology that creates virtual versions of computing resources (servers, storage, networks) by abstracting physical hardware, enabling multiple virtual machines to run on a single physical machine and improving resource utilization.

VM (Virtual Machine)
A VM is an emulated computer system that runs on physical hardware, providing an isolated environment with its own operating system and applications, managed by a hypervisor.

W
Word2Vec
Word2Vec is a family of models that learns dense vector representations of words, capturing semantic similarities based on context.

Z
Zero‑Shot Learning
Zero‑shot learning is a setup where a model must correctly classify samples from classes it has never seen during training, often by leveraging auxiliary information like semantic descriptions.

---

## Modern AI/ML Terms (2023-2025) ⭐

**Large Language Models (LLMs)**
LLMs are foundation models trained on massive text datasets with billions of parameters (e.g., GPT-4, Claude, LLaMA) capable of understanding and generating human-like text.

**GPT (Generative Pre-trained Transformer)**
GPT is a family of large language models by OpenAI that use the transformer decoder architecture for text generation tasks.

**Claude**
Claude is an LLM developed by Anthropic with emphasis on safety, helpfulness, and harmlessness through constitutional AI and RLHF.

**Prompt Engineering**
Prompt engineering is the practice of crafting effective input prompts to guide LLM outputs, including techniques like few-shot prompting, chain-of-thought, and system instructions.

**Context Window**
The context window is the maximum number of tokens (input + output) that an LLM can process in a single request, ranging from 4K to 200K+ tokens in modern models.

**Temperature**
Temperature is a hyperparameter (0.0-2.0) controlling randomness in text generation: lower values produce focused/deterministic outputs, higher values increase creativity and diversity.

**RAG (Retrieval Augmented Generation)**
RAG combines information retrieval with text generation, allowing LLMs to access external knowledge bases or documents to provide grounded, factual responses.

**Vector Database**
Vector databases (Pinecone, Weaviate, ChromaDB) store and efficiently search high-dimensional embeddings, enabling semantic search and RAG applications.

**Cosine Similarity**
Cosine similarity measures the angle between two vectors (range: -1 to 1), commonly used to quantify semantic similarity between embeddings.

**Fine-tuning**
Fine-tuning adapts a pre-trained model to a specific task or domain by continuing training on a smaller, task-specific dataset.

**LoRA (Low-Rank Adaptation)**
LoRA is an efficient fine-tuning technique that updates only a small number of parameters via low-rank matrix decomposition, reducing memory and compute requirements.

**RLHF (Reinforcement Learning from Human Feedback)**
RLHF trains models using human preferences as rewards, aligning model behavior with human values and improving response quality.

**Instruction Tuning**
Instruction tuning trains models to follow natural language instructions by fine-tuning on datasets of (instruction, response) pairs.

**Attention Mechanism**
Attention allows models to dynamically focus on relevant parts of the input when processing sequences, forming the core of transformer architectures.

**Self-Attention**
Self-attention computes relationships between all positions in a sequence simultaneously, enabling each token to attend to all other tokens.

**Multi-Head Attention**
Multi-head attention runs multiple attention operations in parallel with different learned projections, capturing diverse aspects of token relationships.

**Encoder-Decoder Architecture**
The encoder-decoder pattern uses one transformer to encode input sequences and another to generate output sequences, common in translation and summarization.

**Foundation Model**
Foundation models are large-scale pre-trained models (BERT, GPT, CLIP) that serve as starting points for many downstream tasks via transfer learning or fine-tuning.

**Tokenization**
Tokenization breaks text into subword units (tokens) using algorithms like Byte-Pair Encoding (BPE) or WordPiece, enabling efficient text processing.

**BPE (Byte-Pair Encoding)**
BPE is a tokenization algorithm that iteratively merges the most frequent character or subword pairs, creating a vocabulary of subword units.

**Quantization**
Quantization reduces model precision (e.g., from 32-bit to 8-bit or 4-bit) to decrease memory usage and increase inference speed with minimal accuracy loss.

**Hallucination**
Hallucination occurs when AI models generate plausible but factually incorrect or nonsensical information, a key challenge in LLM deployment.

**Perplexity**
Perplexity measures how well a language model predicts text, with lower values indicating better performance (exponential of average cross-entropy loss).

**Stable Diffusion**
Stable Diffusion is a latent diffusion model for generating high-quality images from text descriptions by iteratively denoising random noise.

**Diffusion Models**
Diffusion models generate data by learning to reverse a gradual noising process, widely used in image generation (DALL-E, Midjourney, Stable Diffusion).

**GAN (Generative Adversarial Network)**
GANs consist of two networks (generator and discriminator) trained adversarially, where the generator creates realistic samples and the discriminator distinguishes real from fake.

**Multimodal AI**
Multimodal AI processes multiple data types (text, images, audio, video) simultaneously, exemplified by models like GPT-4V, CLIP, and Gemini.

**CLIP (Contrastive Language-Image Pre-training)**
CLIP learns joint embeddings of images and text, enabling zero-shot image classification and cross-modal retrieval.

**Hugging Face**
Hugging Face is a platform and community for sharing pre-trained models, datasets, and tools, with the Transformers library as its flagship product.

**LangChain**
LangChain is a framework for building applications powered by LLMs, providing abstractions for chains, agents, memory, and tool integration.

**Agent (AI Agent)**
AI agents are systems that autonomously perceive environments, make decisions, and take actions to achieve goals, often using LLMs for reasoning.

**Chain-of-Thought (CoT)**
Chain-of-thought prompting encourages LLMs to show step-by-step reasoning, improving performance on complex reasoning tasks.

**In-Context Learning**
In-context learning enables models to adapt to new tasks using only examples or instructions in the prompt, without parameter updates.

**Shot (Few-Shot, One-Shot, Zero-Shot)**
"Shot" refers to the number of examples provided: zero-shot (no examples), one-shot (1 example), few-shot (2-10 examples) for task demonstration.

**Mixture of Experts (MoE)**
MoE architectures use multiple specialized sub-networks (experts) and route inputs dynamically, enabling larger models with conditional computation.

**Distillation (Knowledge Distillation)**
Distillation trains a smaller "student" model to mimic a larger "teacher" model, creating compact models that retain most of the teacher's performance.

**Prompt Injection**
Prompt injection is a security vulnerability where adversarial inputs manipulate LLM behavior to bypass safety guidelines or leak information.

**Alignment**
Alignment ensures AI systems behave according to human values and intentions, addressing safety concerns and unintended behaviors.

**Constitutional AI**
Constitutional AI
Constitutional AI trains models using a set of principles (a "constitution") to self-critique and revise responses, improving safety without extensive human labeling.

**dbt (data build tool)**
dbt is a transformation tool that enables data analysts and engineers to transform data in warehouses by writing SELECT statements, providing version control, testing, and documentation for data transformations.

**DVC (Data Version Control)**
DVC is an open-source version control system for machine learning projects, tracking datasets, models, and experiments with Git-like commands, enabling reproducibility and collaboration.

**ETL (Extract, Transform, Load)**
ETL is a data integration process that extracts data from sources, transforms it into the desired format/structure, and loads it into a destination system like a data warehouse—traditional approach where transformation happens before loading.

**ELT (Extract, Load, Transform)**
ELT is a modern data integration approach that extracts data, loads it into a destination first (typically cloud data warehouse), then transforms it—leveraging the processing power of modern data warehouses.

**Airflow (Apache Airflow)**
Airflow is an open-source workflow orchestration platform for authoring, scheduling, and monitoring data pipelines as Directed Acyclic Graphs (DAGs), widely used for ETL/ELT and ML workflows.

**Kafka (Apache Kafka)**
Kafka is a distributed streaming platform for building real-time data pipelines and streaming applications, providing high-throughput, fault-tolerant publish-subscribe messaging.

**Flink (Apache Flink)**
Flink is a stream processing framework for stateful computations over data streams, enabling real-time analytics, event-driven applications, and batch processing with low latency.

**Prefect**
Prefect is a modern workflow orchestration platform that provides dataflow automation with dynamic task generation, improved error handling, and cloud-native design.

**Fivetran**
Fivetran is a cloud-based data integration platform that automates data pipelines from various sources to data warehouses with pre-built connectors and automated schema management.

**MLflow**
MLflow is an open-source platform for managing the ML lifecycle, including experiment tracking, model packaging, versioning, and deployment, with support for various frameworks.

**Feature Store**
A feature store is a centralized repository for storing, managing, and serving ML features, ensuring consistency between training and serving, reducing feature engineering duplication, and enabling feature discovery and reuse.

**Vision Transformer (ViT)**
Vision Transformer applies the transformer architecture to image classification by treating image patches as tokens, demonstrating that attention-based models can match or exceed CNNs on computer vision tasks.

**State Space Models (SSM)**
State space models are efficient sequence modeling architectures that use linear state-space representations, offering alternatives to transformers with better computational efficiency for long sequences.

**Mamba**
Mamba is a state-space model architecture designed for efficient sequence modeling, achieving transformer-like performance with linear time complexity, particularly effective for long-context tasks.

**Sparse Transformers**
Sparse transformers reduce computational complexity by using sparse attention patterns instead of full attention, enabling efficient processing of longer sequences with reduced memory requirements.

**Longformer**
Longformer is a transformer variant that uses a combination of local windowed attention and task-motivated global attention, efficiently handling documents with thousands of tokens.

**T5 (Text-to-Text Transfer Transformer)**
T5 is an encoder-decoder transformer model that frames all NLP tasks as text-to-text problems, where both input and output are text strings, enabling unified training across diverse tasks.

**Encoder-only Architecture**
Encoder-only models (like BERT) use only the transformer encoder stack, learning bidirectional representations ideal for understanding tasks like classification, NER, and question answering.

**Decoder-only Architecture**
Decoder-only models (like GPT) use only the transformer decoder stack with causal attention, designed for autoregressive generation tasks and serving as the foundation for most large language models.

**Weights & Biases (W&B)**
Weights & Biases is an MLOps platform for experiment tracking, model versioning, dataset management, and model monitoring, providing visualization tools and collaboration features for ML teams.

**Neptune**
Neptune is an ML metadata store and experiment tracking platform that logs, organizes, and visualizes ML experiments, models, and datasets with version control and collaboration capabilities.

**Kubeflow**
Kubeflow is an open-source machine learning platform built on Kubernetes for deploying, scaling, and managing ML workflows, providing components for training, serving, and pipeline orchestration.

**Feast**
Feast is an open-source feature store that manages the lifecycle of ML features, ensuring consistency between training and serving environments with real-time and batch feature serving.

**Tecton**
Tecton is an enterprise feature platform (feature store) built for production ML, providing feature engineering, storage, and serving with real-time updates and monitoring capabilities.

**A/B Testing**
A/B testing is an experimental methodology that compares two or more versions (A, B, etc.) to determine which performs better, commonly used to evaluate ML model performance, UI changes, or product features in production.

**Model Registry**
A model registry is a centralized repository for storing, versioning, and managing ML models throughout their lifecycle, tracking metadata like training parameters, metrics, lineage, and deployment status.

**Model Monitoring**
Model monitoring involves tracking ML model performance in production, detecting issues like data drift, concept drift, performance degradation, and ensuring models continue to meet business requirements.

**Drift Detection**
Drift detection identifies changes in data distributions (data drift) or relationships between features and targets (concept drift) that can degrade model performance over time, triggering retraining or alerts.

**ONNX (Open Neural Network Exchange)**
ONNX is an open format for representing ML models, enabling interoperability between different frameworks (PyTorch, TensorFlow) and optimized deployment across various hardware platforms.

**TensorFlow Lite**
TensorFlow Lite is a lightweight framework for deploying TensorFlow models on mobile, embedded, and IoT devices with optimizations for low latency and small binary size.

**FastAPI**
FastAPI is a modern, high-performance Python web framework for building APIs with automatic interactive documentation, type hints, and async support, popular for ML model serving.

**Red Teaming**
Red teaming is a security testing practice where experts attempt to break AI systems by finding vulnerabilities, adversarial inputs, or ways to elicit unsafe outputs, helping improve model robustness and safety.

**Adversarial Testing**
Adversarial testing involves systematically probing AI systems with challenging or malicious inputs designed to expose weaknesses, biases, or failure modes before deployment.

**AI Watermarking**
AI watermarking embeds imperceptible signals in AI-generated content (text, images, audio) to enable detection and attribution of synthetic media, helping combat misinformation and deepfakes.

**Bias (AI Bias)**
AI bias refers to systematic errors or unfair outcomes in ML models, often reflecting biases in training data, that can lead to discriminatory treatment of certain groups based on protected characteristics like race, gender, or age.

**Fairness (AI Fairness)**
Fairness in AI ensures that models make equitable decisions without discriminating against individuals or groups, measured through various metrics like demographic parity, equal opportunity, or equalized odds.

**Explainability (Model Explainability)**
Explainability refers to the ability to understand and interpret how an AI model makes decisions, often using techniques like SHAP, LIME, or attention visualization to provide human-understandable explanations.

**Interpretability**
Interpretability is the degree to which humans can understand the reasoning behind a model's predictions, with simpler models (linear regression, decision trees) being more interpretable than complex deep neural networks.

**DPO (Direct Preference Optimization)**
DPO is an alignment technique that directly optimizes language models based on human preferences without requiring a separate reward model, simplifying the RLHF pipeline while achieving comparable results.

**QLoRA (Quantized Low-Rank Adaptation)**
QLoRA combines quantization and LoRA to enable efficient fine-tuning of large language models on consumer GPUs by using 4-bit quantization while maintaining performance close to full precision.

**Model Compression**
Model compression reduces model size and computational requirements through techniques like quantization, pruning, knowledge distillation, and low-rank factorization, enabling deployment on resource-constrained devices.

**vLLM**
vLLM is a high-throughput, memory-efficient inference engine for large language models, using PagedAttention to manage attention key-value memory and achieve significantly faster serving speeds.

**TGI (Text Generation Inference)**
TGI (by Hugging Face) is a production-ready inference server for large language models, providing optimizations like continuous batching, tensor parallelism, and quantization support for efficient deployment.

**Ollama**
Ollama is a tool for running large language models locally on personal computers, providing a simple interface to download, run, and interact with models like LLaMA, Mistral, and others without cloud dependencies.

**Edge Deployment**
Edge deployment runs ML models on end-user devices (phones, IoT devices, embedded systems) rather than cloud servers, enabling lower latency, improved privacy, and offline functionality.

**FAISS (Facebook AI Similarity Search)**
FAISS is a library for efficient similarity search and clustering of dense vectors, optimized for billion-scale vector databases with GPU acceleration, commonly used for embedding retrieval in RAG systems.

**HNSW (Hierarchical Navigable Small World)**
HNSW is an approximate nearest neighbor search algorithm that builds a multi-layer graph structure, providing fast and accurate similarity search for high-dimensional vectors with excellent recall-speed tradeoffs.

**Annoy (Approximate Nearest Neighbors Oh Yeah)**
Annoy is a C++ library with Python bindings for approximate nearest neighbor search, using random projection forests to create memory-mapped indexes suitable for large-scale similarity search.

**BPE (Byte Pair Encoding)**
BPE is a tokenization algorithm that iteratively merges the most frequent pairs of characters or character sequences, creating a vocabulary of subword units. Widely used in modern LLMs like GPT, it balances vocabulary size with the ability to represent rare words through subword combinations.

**WordPiece**
WordPiece is a tokenization algorithm similar to BPE, used by BERT and other Google models, that builds a vocabulary by iteratively choosing subword units that maximize the likelihood of the training data when segmented.

**SentencePiece**
SentencePiece is a language-independent tokenization library that treats text as a sequence of Unicode characters, supporting BPE and unigram language model tokenization without requiring pre-tokenization or language-specific rules.

**Mixture of Experts (MoE)**
Mixture of Experts is a neural network architecture that uses multiple specialized "expert" networks with a gating mechanism that routes inputs to the most relevant experts, enabling efficient scaling while keeping inference costs manageable.

**Mamba**
Mamba is a state space model architecture that provides an efficient alternative to transformers for sequence modeling, using selective state spaces to achieve linear-time complexity while maintaining strong performance on long sequences.

**State Space Models**
State space models are a class of sequence models based on continuous-time state representations, offering efficient alternatives to transformers with linear-time complexity for long sequences while capturing temporal dependencies.

**Vision Transformer (ViT)**
Vision Transformer applies the transformer architecture directly to image patches, treating them as tokens, demonstrating that transformers can match or exceed CNN performance on computer vision tasks when trained on sufficient data.

**CLIP (Contrastive Language-Image Pre-training)**
CLIP is a multimodal model trained on image-text pairs that learns joint representations of vision and language, enabling zero-shot image classification, image generation guidance, and cross-modal retrieval.

**Stable Diffusion**
Stable Diffusion is a text-to-image diffusion model that generates high-quality images from text prompts by learning to reverse a gradual noising process, operating in latent space for computational efficiency.

**DALL-E**
DALL-E is OpenAI's text-to-image generation model that creates images from natural language descriptions, demonstrating remarkable creativity and understanding of abstract concepts and compositions.

**Midjourney**
Midjourney is a text-to-image AI service that generates artistic, high-quality images from text prompts, known for its distinctive aesthetic style and strong performance on creative and artistic content.

**Sora**
Sora is OpenAI's text-to-video generation model capable of creating realistic and imaginative video scenes from text instructions, demonstrating understanding of physics, motion, and temporal consistency.

**Gemini**
Gemini is Google DeepMind's multimodal AI model family designed to be natively multimodal, processing and generating text, images, audio, and video with strong reasoning and code generation capabilities.

**LLaMA (Large Language Model Meta AI)**
LLaMA is Meta's family of open-source large language models ranging from 7B to 70B parameters, designed to be more accessible for research and providing strong performance at smaller scales than proprietary models.

**Mistral**
Mistral is a family of open-source large language models developed by Mistral AI, known for efficient architecture using grouped-query attention and sliding window attention, delivering strong performance at competitive sizes.

**Hallucination (AI Hallucination)**
Hallucination occurs when AI models, particularly language models, generate plausible-sounding but factually incorrect or nonsensical information, presenting it confidently as if it were true, a key challenge in deploying generative AI.

**Constitutional AI**
Constitutional AI is an alignment technique developed by Anthropic that trains models to follow a set of principles (a "constitution") through self-critique and revision, reducing harmful outputs without extensive human feedback.

**Instruction Tuning**
Instruction tuning is a fine-tuning technique that trains language models on diverse instruction-following tasks, teaching models to understand and respond to natural language instructions across various domains.

**Chain-of-Thought (CoT) Prompting**
Chain-of-thought prompting is a technique that encourages language models to generate intermediate reasoning steps before producing final answers, significantly improving performance on complex reasoning tasks.

**In-Context Learning**
In-context learning is the ability of language models to learn new tasks from examples provided in the prompt without parameter updates, leveraging patterns in the training data to adapt to new contexts dynamically.

**Zero-Shot Learning**
Zero-shot learning refers to a model's ability to perform tasks it wasn't explicitly trained on, using only the task description or prompt without any examples, relying on knowledge transfer from pre-training.

**Few-Shot Learning**
Few-shot learning enables models to learn new tasks from a small number of examples (typically 1-10) provided in the prompt, demonstrating rapid adaptation without fine-tuning or extensive training data.

**One-Shot Learning**
One-shot learning is the ability to learn a new task or concept from just a single example, either through in-context learning in prompts or through specialized meta-learning architectures.

**AlphaFold**
AlphaFold is DeepMind's breakthrough AI system that predicts 3D protein structures from amino acid sequences with remarkable accuracy, revolutionizing structural biology and drug discovery.

**AlphaGo**
AlphaGo is DeepMind's AI program that defeated world champions in the game of Go, combining deep neural networks with tree search and reinforcement learning, marking a milestone in AI's ability to master complex strategic games.

**NanoGPT**
NanoGPT is Andrej Karpathy's minimal implementation of GPT for educational purposes, demonstrating the core transformer architecture in clean, understandable code, widely used for learning how LLMs work.

**JAX**
JAX is a Python library from Google for high-performance numerical computing and machine learning, combining NumPy-like syntax with automatic differentiation, JIT compilation, and seamless GPU/TPU support.

**XGBoost**
XGBoost (Extreme Gradient Boosting) is an optimized gradient boosting library known for speed and performance, implementing regularization, parallel processing, and tree pruning, dominant in structured data competitions.

**LightGBM**
LightGBM is a gradient boosting framework by Microsoft that uses histogram-based algorithms and leaf-wise tree growth, offering faster training and lower memory usage than traditional GBDT methods.

**CatBoost**
CatBoost is a gradient boosting library by Yandex with native support for categorical features, symmetric tree structures, and ordered boosting, providing strong performance with minimal hyperparameter tuning.

**Haystack**
Haystack is an open-source NLP framework for building production-ready search systems, question answering, and RAG applications, providing components for document stores, retrievers, and readers.

**LlamaIndex (GPT Index)**
LlamaIndex is a data framework for connecting LLMs with external data sources, providing tools for data ingestion, indexing, querying, and building RAG applications with various storage backends.

**Kaggle**
Kaggle is a platform for data science competitions, datasets, and collaborative machine learning, owned by Google, providing free compute resources, learning materials, and a community for ML practitioners.

**Coursera**
Coursera is an online learning platform offering courses, specializations, and degrees from universities and companies, including popular machine learning courses from Andrew Ng and deeplearning.ai.

**deeplearning.ai**
deeplearning.ai is an education platform founded by Andrew Ng offering courses and specializations in machine learning, deep learning, and AI, known for accessible teaching and practical focus.

**3Blue1Brown**
3Blue1Brown is an educational YouTube channel by Grant Sanderson providing visual, intuitive explanations of mathematics, including essential series on linear algebra, calculus, and neural networks for ML.

**Grant Sanderson**
Grant Sanderson is a mathematics educator and creator of 3Blue1Brown, renowned for creating visually stunning explanations of complex mathematical concepts essential for understanding machine learning.

**Gilbert Strang**
Gilbert Strang is an MIT mathematics professor famous for his linear algebra course (18.06), one of the most popular mathematics courses worldwide, providing essential foundations for machine learning and data science.

**Andrej Karpathy**
Andrej Karpathy is a leading AI educator and researcher, former Director of AI at Tesla and founding member of OpenAI, known for educational content on neural networks, transformers, and creating NanoGPT.

**Andrew Ng**
Andrew Ng is a pioneering AI researcher and educator, co-founder of Coursera and deeplearning.ai, known for making machine learning accessible through online courses, leading the democratization of AI education.

**Jon Krohn**
Jon Krohn is a data science educator and author of "Deep Learning Illustrated," creating comprehensive mathematics courses (linear algebra, calculus, probability) specifically designed for machine learning practitioners.

**freeCodeCamp**
freeCodeCamp is a nonprofit organization providing free coding education through interactive courses, certifications, and extensive YouTube content, including comprehensive machine learning and data science curricula.

**MIT OpenCourseWare**
MIT OpenCourseWare is MIT's initiative providing free access to course materials from thousands of MIT courses, including legendary offerings like Gilbert Strang's Linear Algebra and modern deep learning courses.

**Econometrics**
Econometrics is the application of statistical methods to economic data, emphasizing causal inference, treatment effects, and understanding relationships between variables, providing foundations for many machine learning concepts.

**Digital Twin**
A digital twin is a virtual representation of a physical object, process, or system that uses real-time data and models to simulate, predict, and optimize the real-world counterpart's behavior.

**MDTP Framework**
MDTP (Models, Data, Tools, Productisation) is a comprehensive framework for structuring machine learning projects, covering the full lifecycle from modeling techniques through data engineering, software tools, and production deployment.

**Productisation**
Productisation (or Productization) in ML refers to the process of transforming models and algorithms into production-ready products, including deployment, monitoring, scaling, business value realization, and user-facing integration.

**Weights & Biases (W&B)**
Weights & Biases is an MLOps platform for experiment tracking, model versioning, dataset management, and model monitoring, providing visualization tools and collaboration features for ML teams.

**Model Deployment**
Model deployment is the process of making a trained machine learning model available in a production environment where it can receive inputs and generate predictions for real-world use cases.

**Feature Store**
A feature store is a centralized repository for storing, managing, and serving features for machine learning, ensuring consistency between training and inference while enabling feature reuse across models and teams.

**Experiment Tracking**
Experiment tracking involves systematically logging and organizing ML experiments, including hyperparameters, metrics, artifacts, and code versions, enabling reproducibility and comparison of model iterations.

