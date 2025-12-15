# Vector Databases for Embeddings

## Phase 3: Storing and Querying Embeddings

After learning **tokenization** (Phase 1) and **embeddings** (Phase 2), you're ready to store and efficiently query those embeddings using vector databases.

---

## 📚 What You'll Learn

This module covers:
- Why vector databases are needed
- Popular vector database options
- How to store embeddings
- Semantic search and similarity queries
- Production deployment patterns
- Hybrid search (vectors + keywords)

---

## 🎯 Learning Path

### Prerequisites

Before this module, you should understand:
- ✅ **Tokenization** - How to convert text to tokens
- ✅ **Embeddings** - How to convert tokens to dense vectors
- 📍 **You are here** - Storing and querying embeddings

### What You'll Build

By the end of this module:
- Store embeddings in vector databases
- Perform semantic similarity search
- Build RAG (Retrieval-Augmented Generation) systems
- Deploy production vector search
- Combine vector + keyword search

---

## 🗄️ Vector Database Options

### Cloud-Based (Managed)

| Database | Best For | Pricing | Open Source? | Scalability |
|----------|----------|---------|--------------|-------------|
| **Pinecone** ⭐ | Production RAG, easy setup | Free tier: 1 index, paid from $70/mo | ❌ Proprietary | Excellent |
| **MongoDB Atlas** ⭐ | Existing MongoDB users | Free tier: 512MB, paid from $57/mo | ✅ Core is OSS | Excellent |
| **Google Vertex AI** ⭐ | Google Cloud ecosystem | Pay-as-you-go, ~$100+/mo | ❌ Proprietary | Excellent |
| **Azure AI Search** ⭐ | Azure ecosystem | Free tier, paid from $75/mo | ❌ Proprietary | Excellent |
| **AWS OpenSearch** ⭐ | AWS ecosystem | Pay-as-you-go, ~$100+/mo | ✅ Fork of ES | Excellent |
| **Elasticsearch** ⭐ | Search + vectors | Elastic Cloud from $95/mo | ✅ Apache 2.0 | Excellent |
| **Redis Cloud** | Caching + vectors | Free tier, paid from $5/mo | ✅ Open Source | Good |

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

### 1. Pinecone (Cloud)

```python
# Install: pip install pinecone-client openai

import pinecone
from openai import OpenAI

# Initialize
pinecone.init(api_key='your-api-key', environment='us-west1-gcp')
client = OpenAI(api_key='your-openai-key')

# Create index
index_name = 'semantic-search'
if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        name=index_name,
        dimension=1536,  # OpenAI embedding size
        metric='cosine'
    )

index = pinecone.Index(index_name)

# Generate and store embeddings
texts = [
    "Machine learning is a subset of AI",
    "Deep learning uses neural networks",
    "Natural language processing handles text"
]

for i, text in enumerate(texts):
    # Get embedding from OpenAI
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    embedding = response.data[0].embedding
    
    # Store in Pinecone
    index.upsert(vectors=[(f"doc_{i}", embedding, {"text": text})])

# Search
query = "What is deep learning?"
query_embedding = client.embeddings.create(
    input=query,
    model="text-embedding-ada-002"
).data[0].embedding

results = index.query(vector=query_embedding, top_k=3, include_metadata=True)
for match in results.matches:
    print(f"Score: {match.score:.4f} - {match.metadata['text']}")
```

### 2. Chroma (Local)

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

### 3. MongoDB Atlas Vector Search

```python
# Install: pip install pymongo

from pymongo import MongoClient
from pymongo.operations import SearchIndexModel
import os

# Connect to MongoDB Atlas using environment variable
# Set your connection string: export MONGODB_URI="mongodb+srv://username:password@cluster.mongodb.net/"
client = MongoClient(os.getenv("MONGODB_URI"))
db = client['vector_db']
collection = db['documents']

# Create vector search index (do this once via Atlas UI or API)
# Index definition:
# {
#   "fields": [{
#     "type": "vector",
#     "path": "embedding",
#     "numDimensions": 1536,
#     "similarity": "cosine"
#   }]
# }

# Insert documents with embeddings
documents = [
    {
        "text": "Machine learning is a subset of AI",
        "embedding": [0.1] * 1536,  # Your actual embedding
        "category": "ML"
    },
    {
        "text": "Deep learning uses neural networks",
        "embedding": [0.2] * 1536,
        "category": "DL"
    }
]
collection.insert_many(documents)

# Vector search using aggregation pipeline
query_embedding = [0.15] * 1536

results = collection.aggregate([
    {
        "$vectorSearch": {
            "index": "vector_index",
            "path": "embedding",
            "queryVector": query_embedding,
            "numCandidates": 100,
            "limit": 3
        }
    },
    {
        "$project": {
            "_id": 0,
            "text": 1,
            "category": 1,
            "score": {"$meta": "vectorSearchScore"}
        }
    }
])

for doc in results:
    print(f"Score: {doc['score']:.4f} - {doc['text']}")
```

### 4. Qdrant (Self-Hosted or Cloud)

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

### 5. Weaviate (Self-Hosted or Cloud)

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

### 6. Milvus (Self-Hosted or Zilliz Cloud)

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

### 7. FAISS (Research/Benchmarking)

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

### 8. Redis with Vector Similarity

```python
# Install: pip install redis

import redis
import numpy as np

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Create index with vector field
from redis.commands.search.field import VectorField, TextField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType

schema = (
    TextField("text"),
    VectorField("embedding",
        "FLAT", {
            "TYPE": "FLOAT32",
            "DIM": 1536,
            "DISTANCE_METRIC": "COSINE"
        }
    )
)

r.ft("idx:documents").create_index(
    schema,
    definition=IndexDefinition(prefix=["doc:"], index_type=IndexType.HASH)
)

# Add documents
embedding = np.array([0.1] * 1536, dtype=np.float32).tobytes()
r.hset("doc:1", mapping={
    "text": "Machine learning is a subset of AI",
    "embedding": embedding
})

# Vector search (KNN)
query_embedding = np.array([0.1] * 1536, dtype=np.float32).tobytes()
results = r.ft("idx:documents").search(
    f"*=>[KNN 3 @embedding $vec AS score]",
    query_params={"vec": query_embedding}
)

for doc in results.docs:
    print(f"Score: {doc.score} - {doc.text}")
```

### 9. Elasticsearch with Vector Search

```python
# Install: pip install elasticsearch

from elasticsearch import Elasticsearch

# Connect
es = Elasticsearch(["http://localhost:9200"])

# Create index with vector mapping
index_name = "documents"
es.indices.create(
    index=index_name,
    body={
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "embedding": {
                    "type": "dense_vector",
                    "dims": 1536,
                    "index": True,
                    "similarity": "cosine"
                }
            }
        }
    }
)

# Index document
es.index(
    index=index_name,
    document={
        "text": "Machine learning is a subset of AI",
        "embedding": [0.1] * 1536
    }
)

# Vector search
query_embedding = [0.1] * 1536
results = es.search(
    index=index_name,
    body={
        "knn": {
            "field": "embedding",
            "query_vector": query_embedding,
            "k": 3,
            "num_candidates": 100
        },
        "_source": ["text"]
    }
)

for hit in results["hits"]["hits"]:
    print(f"Score: {hit['_score']:.4f} - {hit['_source']['text']}")
```

### 10. Google Vertex AI Vector Search

```python
# Install: pip install google-cloud-aiplatform

from google.cloud import aiplatform
from google.cloud.aiplatform import MatchingEngineIndex, MatchingEngineIndexEndpoint

# Initialize
aiplatform.init(project='your-project-id', location='us-central1')

# Create index (one-time setup)
index = MatchingEngineIndex.create_tree_ah_index(
    display_name="semantic-search-index",
    dimensions=1536,
    approximate_neighbors_count=10,
    distance_measure_type="COSINE_DISTANCE",
)

# Deploy index to endpoint
endpoint = MatchingEngineIndexEndpoint.create(
    display_name="semantic-search-endpoint",
    public_endpoint_enabled=True
)

endpoint.deploy_index(
    index=index,
    deployed_index_id="deployed_index_id",
    machine_type="n1-standard-2"
)

# Add vectors
embeddings = [[0.1] * 1536, [0.2] * 1536]  # Your embeddings
embedding_ids = ["doc_1", "doc_2"]

index.upsert_datapoints(
    datapoints=[
        {"datapoint_id": id, "feature_vector": emb}
        for id, emb in zip(embedding_ids, embeddings)
    ]
)

# Query
query_embedding = [0.15] * 1536
response = endpoint.find_neighbors(
    deployed_index_id="deployed_index_id",
    queries=[query_embedding],
    num_neighbors=3
)

for neighbor in response[0]:
    print(f"ID: {neighbor.id}, Distance: {neighbor.distance}")
```

### 11. Azure AI Search (formerly Azure Cognitive Search)

```python
# Install: pip install azure-search-documents azure-identity

from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    VectorSearchAlgorithmConfiguration,
)
from azure.core.credentials import AzureKeyCredential

# Initialize
endpoint = "https://your-service.search.windows.net"
key = "your-admin-key"
index_name = "semantic-search"

credential = AzureKeyCredential(key)
index_client = SearchIndexClient(endpoint, credential)

# Create index with vector field
index = SearchIndex(
    name=index_name,
    fields=[
        SearchField(name="id", type=SearchFieldDataType.String, key=True),
        SearchField(name="text", type=SearchFieldDataType.String, searchable=True),
        SearchField(
            name="embedding",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=1536,
            vector_search_configuration="vector-config"
        )
    ],
    vector_search=VectorSearch(
        algorithm_configurations=[
            VectorSearchAlgorithmConfiguration(
                name="vector-config",
                kind="hnsw",
                hnsw_parameters={"metric": "cosine"}
            )
        ]
    )
)

index_client.create_or_update_index(index)

# Add documents
search_client = SearchClient(endpoint, index_name, credential)

documents = [
    {
        "id": "1",
        "text": "Machine learning is a subset of AI",
        "embedding": [0.1] * 1536
    }
]

search_client.upload_documents(documents)

# Vector search
query_embedding = [0.1] * 1536

results = search_client.search(
    search_text=None,
    vector=query_embedding,
    top_k=3,
    vector_fields="embedding"
)

for result in results:
    print(f"Score: {result['@search.score']:.4f} - {result['text']}")
```

---

## 🔍 Comparison Guide

### 🌟 World-Famous Products

#### Proprietary (Paid/Freemium)

**Pinecone** ⭐⭐⭐⭐⭐
- **Status**: Proprietary, VC-backed
- **Fame**: Most popular managed vector DB
- **Used by**: Major AI companies, startups
- **Pricing**: Free tier, then $70-400+/month
- **Best for**: Production RAG, easy setup

**MongoDB Atlas Vector Search** ⭐⭐⭐⭐⭐
- **Status**: Core is open-source (SSPL), Atlas is managed
- **Fame**: 35M+ downloads/month, Fortune 500 companies
- **Used by**: Google, Adobe, Cisco, Toyota
- **Pricing**: Free tier (512MB), then $57+/month
- **Best for**: Existing MongoDB users, hybrid queries

**AWS OpenSearch Serverless** ⭐⭐⭐⭐⭐
- **Status**: Open-source fork of Elasticsearch
- **Fame**: Part of AWS, massive enterprise adoption
- **Used by**: Thousands of AWS customers
- **Pricing**: Pay-as-you-go, ~$100+/month
- **Best for**: AWS-native apps, full-text + vector search

**Elasticsearch** ⭐⭐⭐⭐⭐
- **Status**: Open source (Apache 2.0) + Elastic Cloud (paid)
- **Fame**: 400M+ downloads, industry standard for search
- **Used by**: Netflix, Uber, Microsoft, GitHub
- **Pricing**: Self-hosted free, Elastic Cloud from $95/month
- **Best for**: Full-text search + vector capabilities

**Google Vertex AI Vector Search** ⭐⭐⭐⭐⭐
- **Status**: Proprietary, Google Cloud Platform
- **Fame**: Part of Google Cloud AI, enterprise-grade
- **Used by**: Google Cloud customers, Fortune 500
- **Pricing**: Pay-as-you-go, ~$100+/month
- **Best for**: Google Cloud ecosystem, scalable vector search
- **Features**: Matching Engine, billions of vectors, <100ms latency

**Azure AI Search** ⭐⭐⭐⭐⭐
- **Status**: Proprietary, Microsoft Azure
- **Fame**: Part of Azure AI, used by Microsoft customers
- **Used by**: Azure customers, Fortune 500
- **Pricing**: Free tier, paid from $75/month
- **Best for**: Azure ecosystem, hybrid search (vector + keyword + semantic)
- **Features**: Built-in AI enrichment, 50+ languages

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
**[01_vector_db_basics.py](./01_vector_db_basics.py)**
- What are vector databases
- Similarity metrics (cosine, L2, dot product)
- CRUD operations
- Basic search

### Module 2: Pinecone (1.5 hours)
**[02_pinecone_guide.py](./02_pinecone_guide.py)**
- Pinecone setup
- Indexing strategies
- Metadata filtering
- Production patterns

### Module 3: Chroma (1 hour)
**[03_chroma_guide.py](./03_chroma_guide.py)**
- Local development
- Auto-embedding
- Collections
- Persistence

### Module 4: Qdrant (1.5 hours)
**[04_qdrant_guide.py](./04_qdrant_guide.py)**
- Qdrant setup (Docker/Cloud)
- Advanced filtering
- Batch operations
- Performance tuning

### Module 5: Weaviate (1.5 hours)
**[05_weaviate_guide.py](./05_weaviate_guide.py)**
- Weaviate setup (Docker/Cloud)
- GraphQL queries
- Hybrid search (vector + keyword)
- Schema design and modules

### Module 6: Milvus (2 hours)
**[06_milvus_guide.py](./06_milvus_guide.py)**
- Milvus/Zilliz Cloud setup
- Collection schema design
- Index types (IVF, HNSW)
- Partitioning and sharding
- Large-scale deployments

### Module 7: pgvector (1 hour)
**[07_pgvector_guide.py](./07_pgvector_guide.py)**
- PostgreSQL integration
- SQL + vectors
- Indexes (IVFFlat, HNSW)
- Hybrid queries

### Module 8: Production RAG (2 hours)
**[08_production_rag.py](./08_production_rag.py)**
- Building RAG systems
- Document chunking
- Retrieval strategies
- LLM integration

### Module 9: Advanced Topics (2 hours)
**[09_advanced_patterns.py](./09_advanced_patterns.py)**
- Hybrid search
- Reranking
- Multi-vector search
- Sharding strategies

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
- [Redis Vector Search](https://redis.io/docs/stack/search/reference/vectors/)
- [Elasticsearch Vector Search](https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search.html)

### Tutorials
- [LangChain Vector Stores](https://python.langchain.com/docs/modules/data_connection/vectorstores/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [Pinecone Learning Center](https://www.pinecone.io/learn/)

---

## ⏱️ Time Estimates

| Module | Time | Difficulty |
|--------|------|------------|
| Vector DB Basics | 2 hours | Beginner |
| Pinecone Guide | 1.5 hours | Beginner |
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

**Ready to store and search embeddings at scale!** 🚀

Built with ❤️ for the AI/ML learning journey
