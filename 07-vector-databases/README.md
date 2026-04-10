# Phase 7: Vector Databases

This module turns embeddings into something operational. Once you can generate vectors, the next practical problem is storing them, filtering them, and retrieving them fast enough to support real systems.

## Actual Module Contents

1. [00_START_HERE.ipynb](00_START_HERE.ipynb)
2. [01_vector_db_basics.ipynb](01_vector_db_basics.ipynb)
3. [02_chroma_guide.ipynb](02_chroma_guide.ipynb)
4. [03_qdrant_guide.ipynb](03_qdrant_guide.ipynb)
5. [04_weaviate_guide.ipynb](04_weaviate_guide.ipynb)
6. [05_milvus_guide.ipynb](05_milvus_guide.ipynb)
7. [06_aurora_pgvector_guide.ipynb](06_aurora_pgvector_guide.ipynb)

## What To Learn Here

- Why ANN search exists
- The difference between local prototype tooling and production vector infrastructure
- When metadata filtering matters as much as vector similarity
- How vector databases connect directly to RAG quality

## Recommended Order

- Start with the basics notebook
- Use Chroma first for local intuition
- Compare Qdrant, Weaviate, Milvus, and pgvector-style workflows after that
- Move to Phase 8 RAG once you understand indexing, retrieval, and filtering trade-offs

## Study Advice

- Learn one local-first stack deeply before comparing every database.
- Focus on retrieval behavior, persistence, and filtering, not vendor feature lists.
- Benchmark with your own document shapes if possible.

## Good Follow-On Projects

Note: removed paid databases. getting too many sales calls.

### Self-Hosted (Open Source)

| Database | Best For | Language | License | Performance |
|----------|----------|----------|---------|-------------|
| **Chroma** | Local dev, prototyping | Python | Apache 2.0 | Fast |
| **Qdrant** ⭐ | Production, filtering | Rust | Apache 2.0 | Very Fast |
| **Weaviate** ⭐ | Enterprise, GraphQL | Go | BSD-3 | Fast |
| **Milvus** ⭐ | Large scale, hybrid search | C++/Python | Apache 2.0 | Very Fast |
| **FAISS** ⭐ | Research, benchmarking | C++/Python | MIT (Meta) | Fastest |
| **pgvector** | Existing PostgreSQL | C/SQL | PostgreSQL | Fast |
| **Redis** | Caching + vectors | C | BSD | Very Fast |
| **Elasticsearch** | Search + vectors | Java | Apache 2.0/SSPL | Fast |
| **MongoDB** | Document DB + vectors | C++ | SSPL | Fast |

---

## 🚀 Quick Start Examples

### 1. Chroma (Local)

```python
# Install: pip install chromadb

import chromadb
from chromadb.config import Settings

# Initialize (persistent storage)
client = chromadb.Client(Settings(
    persist_directory="./chroma_db",
    chroma_db_impl="duckdb+parquet"
))

# Create collection
collection = client.create_collection(
    name="documents",
    metadata={"hnsw:space": "cosine"}
)

# Add documents (Chroma generates embeddings automatically)
collection.add(
    documents=[
        "Machine learning is a subset of AI",
        "Deep learning uses neural networks",
        "Natural language processing handles text"
    ],
    ids=["doc1", "doc2", "doc3"],
    metadatas=[
        {"category": "ML"},
        {"category": "DL"},
        {"category": "NLP"}
    ]
)

# Query
results = collection.query(
    query_texts=["What is deep learning?"],
    n_results=3
)

print(results)
```


### 2. Qdrant (Self-Hosted or Cloud)

```python
# Install: pip install qdrant-client

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue

# Initialize
client = QdrantClient(path="./qdrant_db")  # Local file-based
# client = QdrantClient(url="http://localhost:6333")  # Docker
# client = QdrantClient(url="https://xyz.cloud.qdrant.io", api_key="your-key")  # Cloud

# Create collection with advanced config
client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(
        size=1536, 
        distance=Distance.COSINE,
        on_disk=False  # Keep in memory for speed
    )
)

# Add vectors with rich metadata
points = [
    PointStruct(
        id=1,
        vector=[0.1] * 1536,
        payload={
            "text": "Machine learning is a subset of AI",
            "category": "ML",
            "date": "2024-01-15",
            "author": "John Doe"
        }
    ),
    PointStruct(
        id=2,
        vector=[0.2] * 1536,
        payload={
            "text": "Deep learning uses neural networks",
            "category": "DL",
            "date": "2024-01-16",
            "author": "Jane Smith"
        }
    ),
    PointStruct(
        id=3,
        vector=[0.15] * 1536,
        payload={
            "text": "Natural language processing handles text",
            "category": "NLP",
            "date": "2024-01-17",
            "author": "John Doe"
        }
    )
]

client.upsert(collection_name="documents", points=points)

# Basic search
search_result = client.search(
    collection_name="documents",
    query_vector=[0.1] * 1536,
    limit=3
)

for hit in search_result:
    print(f"Score: {hit.score:.4f} - {hit.payload['text']}")

# Advanced search with filtering
filtered_result = client.search(
    collection_name="documents",
    query_vector=[0.1] * 1536,
    query_filter=Filter(
        must=[
            FieldCondition(
                key="category",
                match=MatchValue(value="ML")
            )
        ]
    ),
    limit=3
)

# Batch search (multiple queries at once)
batch_results = client.search_batch(
    collection_name="documents",
    requests=[
        {
            "vector": [0.1] * 1536,
            "limit": 2
        },
        {
            "vector": [0.2] * 1536,
            "limit": 2
        }
    ]
)

# Scroll through all points (for export/backup)
records, next_offset = client.scroll(
    collection_name="documents",
    limit=10
)

# Get collection info
collection_info = client.get_collection("documents")
print(f"Vectors count: {collection_info.vectors_count}")
print(f"Points count: {collection_info.points_count}")

# Delete by filter
client.delete(
    collection_name="documents",
    points_selector=Filter(
        must=[
            FieldCondition(key="author", match=MatchValue(value="John Doe"))
        ]
    )
)
```

### 3. Weaviate (Self-Hosted )

```python
# Install: pip install weaviate-client

import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery

# Initialize
client = weaviate.connect_to_local()  # Docker local
# client = weaviate.connect_to_wcs(
#     cluster_url="https://your-cluster.weaviate.network",
#     auth_credentials=Auth.api_key("your-api-key")
# )  # Weaviate Cloud

# Create collection (schema)
from weaviate.classes.config import Configure, Property, DataType

collection = client.collections.create(
    name="Document",
    description="A collection of documents with embeddings",
    vectorizer_config=Configure.Vectorizer.none(),  # We provide our own vectors
    properties=[
        Property(name="text", data_type=DataType.TEXT),
        Property(name="category", data_type=DataType.TEXT),
        Property(name="date", data_type=DataType.DATE),
        Property(name="author", data_type=DataType.TEXT)
    ]
)

# Add objects with vectors
documents = client.collections.get("Document")

documents.data.insert_many([
    {
        "text": "Machine learning is a subset of AI",
        "category": "ML",
        "date": "2024-01-15T00:00:00Z",
        "author": "John Doe",
        "_vector": [0.1] * 1536
    },
    {
        "text": "Deep learning uses neural networks",
        "category": "DL",
        "date": "2024-01-16T00:00:00Z",
        "author": "Jane Smith",
        "_vector": [0.2] * 1536
    },
    {
        "text": "Natural language processing handles text",
        "category": "NLP",
        "date": "2024-01-17T00:00:00Z",
        "author": "John Doe",
        "_vector": [0.15] * 1536
    }
])

# Vector search
response = documents.query.near_vector(
    near_vector=[0.1] * 1536,
    limit=3,
    return_metadata=MetadataQuery(distance=True)
)

for obj in response.objects:
    print(f"Distance: {obj.metadata.distance:.4f}")
    print(f"Text: {obj.properties['text']}")
    print(f"Category: {obj.properties['category']}\n")

# Filtered vector search
from weaviate.classes.query import Filter

response = documents.query.near_vector(
    near_vector=[0.1] * 1536,
    limit=3,
    filters=Filter.by_property("category").equal("ML")
)

# Hybrid search (vector + keyword)
response = documents.query.hybrid(
    query="machine learning artificial intelligence",
    vector=[0.1] * 1536,
    alpha=0.5,  # 0.5 = balanced, 0 = pure keyword, 1 = pure vector
    limit=3
)

# GraphQL query (Weaviate's native interface)
# This gives you more flexibility
result = client.query.get(
    "Document",
    ["text", "category", "author"]
).with_near_vector({
    "vector": [0.1] * 1536
}).with_limit(3).with_additional(["distance", "certainty"]).do()

print(result)

# Aggregate queries
response = documents.aggregate.over_all(
    group_by="category"
)

# Get object by ID
uuid = response.objects[0].uuid
obj = documents.query.fetch_object_by_id(uuid)

# Update object
documents.data.update(
    uuid=uuid,
    properties={"text": "Updated text about machine learning"}
)

# Delete objects
documents.data.delete_by_id(uuid)

# Batch operations for performance
with client.batch.dynamic() as batch:
    for i in range(1000):
        batch.add_object(
            collection="Document",
            properties={
                "text": f"Document {i}",
                "category": "Batch",
                "date": "2024-01-01T00:00:00Z",
                "author": "Batch User"
            },
            vector=[0.1] * 1536
        )

client.close()
```

### 4. Milvus (Self-Hosted or Zilliz Cloud)

```python
# Install: pip install pymilvus

from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection
)

# Connect to Milvus
connections.connect(
    alias="default",
    host='localhost',
    port='19530'
)
# Zilliz Cloud:
# connections.connect(
#     alias="default",
#     uri="https://your-cluster.zillizcloud.com",
#     token="your-token"
# )

# Check if collection exists
collection_name = "documents"
if utility.has_collection(collection_name):
    utility.drop_collection(collection_name)

# Define schema
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=1000),
    FieldSchema(name="category", dtype=DataType.VARCHAR, max_length=100),
    FieldSchema(name="author", dtype=DataType.VARCHAR, max_length=200),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1536)
]

schema = CollectionSchema(
    fields=fields,
    description="Document collection with embeddings",
    enable_dynamic_field=True  # Allow dynamic fields
)

# Create collection
collection = Collection(
    name=collection_name,
    schema=schema,
    using='default',
    shards_num=2  # Number of shards for distribution
)

# Insert data
entities = [
    ["Machine learning is a subset of AI", "Deep learning uses neural networks", "NLP handles text"],
    ["ML", "DL", "NLP"],
    ["John Doe", "Jane Smith", "John Doe"],
    [[0.1] * 1536, [0.2] * 1536, [0.15] * 1536]
]

insert_result = collection.insert(entities)
print(f"Inserted {len(insert_result.primary_keys)} entities")

# Create index for fast search (required before searching)
index_params = {
    "metric_type": "COSINE",  # or "L2", "IP" (inner product)
    "index_type": "IVF_FLAT",  # or "HNSW", "IVF_SQ8", etc.
    "params": {"nlist": 128}
}

collection.create_index(
    field_name="embedding",
    index_params=index_params
)

# Load collection into memory (required before search)
collection.load()

# Vector search
search_params = {
    "metric_type": "COSINE",
    "params": {"nprobe": 10}
}

query_vector = [[0.1] * 1536]

results = collection.search(
    data=query_vector,
    anns_field="embedding",
    param=search_params,
    limit=3,
    output_fields=["text", "category", "author"]
)

for hits in results:
    for hit in hits:
        print(f"Distance: {hit.distance:.4f}")
        print(f"Text: {hit.entity.get('text')}")
        print(f"Category: {hit.entity.get('category')}\n")

# Filtered search (boolean expression)
results = collection.search(
    data=query_vector,
    anns_field="embedding",
    param=search_params,
    limit=3,
    expr='category == "ML"',  # Filter expression
    output_fields=["text", "category", "author"]
)

# Hybrid search (with scalar filtering)
results = collection.search(
    data=query_vector,
    anns_field="embedding",
    param=search_params,
    limit=3,
    expr='author == "John Doe" and category in ["ML", "NLP"]',
    output_fields=["text", "category", "author"]
)

# Query by ID
query_result = collection.query(
    expr="id in [1, 2, 3]",
    output_fields=["id", "text", "category"]
)

# Delete entities
collection.delete(expr='category == "DL"')

# Get collection statistics
stats = collection.get_stats()
print(f"Collection stats: {stats}")

# Partition support (for multi-tenancy)
partition = collection.create_partition("partition_2024")
partition.insert(entities)

# Search in specific partition
results = collection.search(
    data=query_vector,
    anns_field="embedding",
    param=search_params,
    limit=3,
    partition_names=["partition_2024"]
)

# Release collection from memory
collection.release()

# Drop collection
utility.drop_collection(collection_name)

# Disconnect
connections.disconnect("default")
```

### 5. FAISS (Research/Benchmarking)

```python
# Install: pip install faiss-cpu (or faiss-gpu)

import faiss
import numpy as np

# Create index
dimension = 1536
index = faiss.IndexFlatL2(dimension)  # L2 distance
# index = faiss.IndexFlatIP(dimension)  # Inner product (cosine)

# Add vectors
vectors = np.random.random((100, dimension)).astype('float32')
index.add(vectors)

# Search
query_vector = np.random.random((1, dimension)).astype('float32')
k = 5  # Top 5 results
distances, indices = index.search(query_vector, k)

print(f"Top {k} results:")
for i, (idx, dist) in enumerate(zip(indices[0], distances[0])):
    print(f"  {i+1}. Index: {idx}, Distance: {dist:.4f}")
```

---

## 🔍 Comparison Guide

### 🌟 World-Famous Products

#### Open Source (Free)

**FAISS (Facebook/Meta)** ⭐⭐⭐⭐⭐
- **Status**: Open source (MIT), by Meta AI Research
- **Fame**: 25K+ GitHub stars, research standard
- **Used by**: Research labs, benchmarking, prototypes
- **Pricing**: Free
- **Best for**: Research, fastest performance, benchmarking

**Qdrant** ⭐⭐⭐⭐
- **Status**: Open source (Apache 2.0) + Cloud option
- **Fame**: Growing fast, 15K+ GitHub stars
- **Used by**: Startups, ML teams
- **Pricing**: Self-hosted free, Cloud from $20/month
- **Best for**: Production + filtering, Rust performance

**Weaviate** ⭐⭐⭐⭐
- **Status**: Open source (BSD-3) + Cloud option
- **Fame**: 8K+ GitHub stars, AI-native
- **Used by**: Enterprise, AI companies
- **Pricing**: Self-hosted free, Cloud from $25/month
- **Best for**: GraphQL, modular AI stack

**Milvus** ⭐⭐⭐⭐
- **Status**: Open source (Apache 2.0) + Zilliz Cloud
- **Fame**: 25K+ GitHub stars, LF AI Foundation
- **Used by**: Large-scale deployments
- **Pricing**: Self-hosted free, Cloud pay-as-you-go
- **Best for**: Massive scale, billions of vectors

**Chroma** ⭐⭐⭐
- **Status**: Open source (Apache 2.0)
- **Fame**: 10K+ GitHub stars, developer-friendly
- **Used by**: Prototypes, local dev
- **Pricing**: Free
- **Best for**: Getting started, local development

**pgvector** ⭐⭐⭐⭐
- **Status**: Open source (PostgreSQL license)
- **Fame**: 8K+ GitHub stars, PostgreSQL extension
- **Used by**: Anyone with PostgreSQL
- **Pricing**: Free (with PostgreSQL)
- **Best for**: Existing PostgreSQL databases

**Redis** ⭐⭐⭐⭐⭐
- **Status**: Open source (BSD) + Redis Enterprise
- **Fame**: 62K+ GitHub stars, most popular cache
- **Used by**: Twitter, GitHub, Snapchat, Stack Overflow
- **Pricing**: Self-hosted free, Cloud from $5/month
- **Best for**: Caching + vector search, real-time apps

---

### Choose Based on Use Case

#### For Prototyping / Local Development
**Best: Chroma or FAISS**
- Quick setup
- No infrastructure needed
- Good for learning and testing

#### For Production with Existing PostgreSQL
**Best: pgvector**
- Leverage existing database
- ACID transactions
- SQL queries
- No new infrastructure

#### For Production RAG Systems
**Best: Pinecone, Qdrant Cloud, or Weaviate Cloud**
- Managed service (no ops)
- Automatic scaling
- High availability
- Fast queries
- Advanced filtering

#### For Large-Scale Enterprise
**Best: Milvus, Weaviate, or Qdrant**
- Hybrid search (vector + keyword)
- Advanced filtering
- Self-hosted control
- Massive scale (billions of vectors)
- Multi-tenancy support

#### For Research / Benchmarking
**Best: FAISS**
- Fastest raw performance
- Many index types
- No database overhead

---

## 📊 Feature Comparison

| Feature | Pinecone | MongoDB | Google | Azure | AWS | Chroma | Qdrant | Weaviate | Milvus | FAISS | pgvector | Redis | Elastic |
|---------|----------|---------|--------|-------|-----|--------|--------|----------|--------|-------|----------|-------|----------|
| **Managed Cloud** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ |
| **Self-Hosted** | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Open Source** | ❌ | ✅ | ❌ | ❌ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Filtering** | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Hybrid Search** | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Multi-tenancy** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| **ACID** | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| **Auto-scaling** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ | ⚠️ | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ |
| **Learning Curve** | Easy | Easy | Medium | Medium | Medium | Easy | Medium | Medium | Hard | Easy | Easy | Easy | Medium |

---

## 🎓 Learning Modules

### Module 1: Basics (2 hours)
**[01_vector_db_basics.ipynb](01_vector_db_basics.ipynb)**
- What are vector databases
- Similarity metrics (cosine, L2, dot product)
- CRUD operations
- Basic search

### Module 2: Chroma (1 hour)
**[02_chroma_guide.ipynb](02_chroma_guide.ipynb)**
- Local development
- Auto-embedding
- Collections
- Persistence

### Module 3: Qdrant (1.5 hours)
**[03_qdrant_guide.ipynb](03_qdrant_guide.ipynb)**
- Qdrant setup (Docker/Cloud)
- Advanced filtering
- Batch operations
- Performance tuning

### Module 4: Weaviate (1.5 hours)
**[04_weaviate_guide.ipynb](04_weaviate_guide.ipynb)**
- Weaviate setup (Docker/Cloud)
- GraphQL queries
- Hybrid search (vector + keyword)
- Schema design and modules

### Module 5: Milvus (2 hours)
**[05_milvus_guide.ipynb](05_milvus_guide.ipynb)**
- Milvus/Zilliz Cloud setup
- Collection schema design
- Index types (IVF, HNSW)
- Partitioning and sharding
- Large-scale deployments

### Module 6: Aurora pgvector (1 hour)
**[06_aurora_pgvector_guide.ipynb](06_aurora_pgvector_guide.ipynb)**
- PostgreSQL integration
- SQL + vectors
- Indexes (IVFFlat, HNSW)
- Hybrid queries

---

## 🔗 Integration with Your Learning Path

### Phase 1: Tokenization (Completed ✅)
- Convert text → tokens
- Handle special characters
- Different algorithms (BPE, WordPiece, SentencePiece)

### Phase 2: Embeddings (Next)
- Convert tokens → dense vectors
- Word2Vec, GloVe, Transformer embeddings
- OpenAI, HuggingFace embedding models

### Phase 3: Vector Databases (This Module 📍)
- Store embeddings efficiently
- Semantic similarity search
- RAG systems
- Production deployment

### Phase 4: LLM Applications
- ChatGPT integration
- Retrieval-Augmented Generation
- Context management
- Prompt engineering

---

## 💡 Common Use Cases

### 1. Semantic Search
```python
# Store product descriptions as embeddings
# Search: "comfortable shoes for running"
# Returns: semantically similar products
```

### 2. Question Answering (RAG)
```python
# Store documentation as embeddings
# Question: "How do I reset my password?"
# Retrieve: relevant docs → send to LLM → answer
```

### 3. Recommendation Systems
```python
# Store user preferences as embeddings
# Find similar users or items
# Recommend based on similarity
```

### 4. Duplicate Detection
```python
# Store documents as embeddings
# Find near-duplicates using similarity threshold
```

### 5. Content Moderation
```python
# Store policy violations as embeddings
# Check new content for similarity to violations
```

---

## 📈 Performance Considerations

### Indexing Speed
- **Fastest**: FAISS, Qdrant
- **Fast**: Pinecone, Weaviate, Milvus
- **Moderate**: Chroma, pgvector

### Query Speed (1M vectors)
- **Fastest**: FAISS (in-memory)
- **Very Fast**: Qdrant, Milvus
- **Fast**: Pinecone, Weaviate
- **Moderate**: pgvector

### Scalability
- **Best**: Pinecone, Milvus, Weaviate
- **Good**: Qdrant
- **Limited**: FAISS, Chroma, pgvector

---

## 💰 Cost Comparison (Monthly)

### Free Tier Options
- **Pinecone**: 1 pod (1GB, ~1M vectors)
- **MongoDB Atlas**: 512MB shared cluster
- **Azure AI Search**: Free tier (50MB, 10K documents)
- **Google Cloud**: $300 free credits (new users)
- **AWS**: Free tier (12 months)
- **Qdrant Cloud**: 1GB cluster
- **Weaviate Cloud**: Sandbox instance
- **Redis Cloud**: 30MB free
- **Chroma**: Unlimited (self-hosted)
- **FAISS**: Free (self-hosted)
- **pgvector**: Free (with PostgreSQL)
- **Elasticsearch**: Free (self-hosted)

### Production Costs (10M vectors, approximate)
- **Google Vertex AI**: ~$200-500/month (depends on QPS)
- **Azure AI Search**: ~$250-500/month (S1-S2 tier)
- **AWS OpenSearch**: ~$200-400/month
- **Pinecone**: ~$200-400/month
- **MongoDB Atlas**: ~$150-300/month (M30+)
- **Elasticsearch Cloud**: ~$150-300/month
- **Qdrant Cloud**: ~$100-200/month
- **Weaviate Cloud**: ~$150-300/month
- **Redis Enterprise Cloud**: ~$100-200/month
- **Self-hosted**: Server costs only (~$50-200/month)

---

## 🚀 Quick Start Guide

### Step 1: Choose Your Database
```bash
# For learning: Chroma
pip install chromadb

# For production (managed):
pip install pinecone-client  # Pinecone
pip install pymongo  # MongoDB Atlas
pip install google-cloud-aiplatform  # Google Vertex AI
pip install azure-search-documents  # Azure AI Search
pip install opensearch-py  # AWS OpenSearch
pip install qdrant-client  # Qdrant Cloud
pip install weaviate-client  # Weaviate Cloud

# For self-hosted (open source):
pip install qdrant-client  # Qdrant
pip install weaviate-client  # Weaviate
pip install pymilvus  # Milvus
pip install faiss-cpu  # FAISS (or faiss-gpu)

# For existing databases:
pip install pgvector  # PostgreSQL
pip install redis  # Redis
pip install elasticsearch  # Elasticsearch
```

### Step 2: Generate Embeddings
```bash
# OpenAI (easiest, paid)
pip install openai

# HuggingFace (free, local)
pip install sentence-transformers

# Custom models
pip install transformers torch
```

### Step 3: Build Your First App
```python
# See examples in:
# - 01_vector_db_basics.py
# - 02_pinecone_guide.py
# - 03_chroma_guide.py
```

---

## 📚 Additional Resources

### Documentation
- [Pinecone Docs](https://docs.pinecone.io/)
- [Chroma Docs](https://docs.trychroma.com/)
- [Qdrant Docs](https://qdrant.tech/documentation/)
- [Weaviate Docs](https://weaviate.io/developers/weaviate)
- [Milvus Docs](https://milvus.io/docs)
- [pgvector Docs](https://github.com/pgvector/pgvector)
- [FAISS Wiki](https://github.com/facebookresearch/faiss/wiki)

### Tutorials
- [LangChain Vector Stores](https://python.langchain.com/docs/modules/data_connection/vectorstores/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)

---

## ⏱️ Time Estimates

| Module | Time | Difficulty |
|--------|------|------------|
| Vector DB Basics | 2 hours | Beginner |
| Chroma Guide | 1 hour | Beginner |
| Qdrant Guide | 1.5 hours | Intermediate |
| Weaviate Guide | 1.5 hours | Intermediate |
| Milvus Guide | 2 hours | Intermediate |
| pgvector Guide | 1 hour | Intermediate |
| Production RAG | 2 hours | Intermediate |
| Advanced Patterns | 2 hours | Advanced |
| **Total** | **~14.5 hours** | **Beginner-Advanced** |

---

## ✅ Prerequisites Checklist

Before starting this module, ensure you understand:

- [ ] Tokenization (Phase 1)
- [ ] What embeddings are (Phase 2)
- [ ] Vector similarity (cosine, dot product)
- [ ] Basic Python and APIs
- [ ] SQL basics (for pgvector)
- [ ] Docker basics (optional, for self-hosted)

---

## 🎯 Learning Outcomes

After completing this module, you will:

- ✅ Understand vector database architecture
- ✅ Store and retrieve embeddings efficiently
- ✅ Perform semantic similarity search
- ✅ Build RAG applications
- ✅ Choose the right database for your use case
- ✅ Deploy production vector search
- ✅ Optimize for cost and performance

---

## 🤝 Getting Help

- **Discord Communities**: Pinecone, Weaviate, Qdrant have active Discords
- **GitHub Issues**: For technical problems
- **Stack Overflow**: Tag with database name
- **Documentation**: All have excellent docs

---

- A semantic document search service
- A metadata-filtered retrieval API
- A retrieval benchmark comparing two vector backends on the same corpus
