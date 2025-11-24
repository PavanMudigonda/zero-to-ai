"""
Vector Database Demo
====================
Learn to store and search embeddings efficiently using ChromaDB.

Why Vector Databases?
- Store millions of embeddings efficiently
- Fast similarity search (milliseconds, not seconds)
- Persist data across sessions
- Foundation for RAG (Retrieval Augmented Generation)

Installation:
pip install chromadb sentence-transformers
"""

import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.config import Settings

# Initialize model
model = SentenceTransformer('all-MiniLM-L6-v2')


def create_simple_collection():
    """Create your first vector database collection."""
    
    print("\n" + "=" * 70)
    print("PART 1: CREATING A VECTOR DATABASE")
    print("=" * 70)
    
    # Create a Chroma client (in-memory)
    client = chromadb.Client()
    
    # Create a collection (like a table in traditional DB)
    collection = client.create_collection(
        name="my_first_collection",
        metadata={"description": "Learning vector databases"}
    )
    
    print("\n✓ Created collection: 'my_first_collection'")
    
    # Sample documents
    documents = [
        "Machine learning is a subset of AI",
        "Python is great for data science",
        "Neural networks mimic the human brain",
        "Deep learning requires large datasets",
    ]
    
    # Generate IDs
    ids = [f"doc_{i}" for i in range(len(documents))]
    
    # Generate embeddings
    embeddings = model.encode(documents).tolist()
    
    # Add to collection
    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids
    )
    
    print(f"✓ Added {len(documents)} documents with embeddings")
    print(f"\nCollection contains {collection.count()} items")
    
    return client, collection


def query_collection(collection):
    """Search the collection using semantic similarity."""
    
    print("\n" + "=" * 70)
    print("PART 2: SEMANTIC SEARCH")
    print("=" * 70)
    
    # User query
    query = "What is artificial intelligence?"
    
    print(f"\nQuery: '{query}'")
    
    # Generate query embedding
    query_embedding = model.encode([query]).tolist()
    
    # Search (returns top 2 most similar)
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=2
    )
    
    print("\nTop 2 Results:")
    print("-" * 70)
    
    for i, (doc, distance) in enumerate(zip(results['documents'][0], 
                                            results['distances'][0]), 1):
        # ChromaDB returns distance (lower is better)
        # Convert to similarity: similarity = 1 - (distance/2)
        similarity = 1 - (distance / 2)
        print(f"\n{i}. Similarity: {similarity:.4f} | Distance: {distance:.4f}")
        print(f"   {doc}")
    
    print("\n💡 OBSERVATION:")
    print("Results are ranked by semantic similarity, not keyword matching!")


def persistent_database():
    """Create a database that persists to disk."""
    
    print("\n" + "=" * 70)
    print("PART 3: PERSISTENT STORAGE")
    print("=" * 70)
    
    # Create persistent client
    client = chromadb.PersistentClient(path="./chroma_db")
    
    print("\n✓ Created persistent database at './chroma_db'")
    
    # Create or get collection
    collection_name = "ml_knowledge_base"
    
    # Delete if exists (for demo purposes)
    try:
        client.delete_collection(name=collection_name)
    except:
        pass
    
    collection = client.create_collection(name=collection_name)
    
    # Knowledge base documents
    documents = [
        # ML Basics
        "Supervised learning uses labeled training data",
        "Unsupervised learning finds patterns in unlabeled data",
        "Reinforcement learning learns through trial and error",
        
        # Algorithms
        "Decision trees split data based on features",
        "Random forests combine multiple decision trees",
        "Neural networks have layers of connected nodes",
        
        # Data
        "Feature engineering creates useful input variables",
        "Data preprocessing cleans and prepares data",
        "Training and test sets evaluate model performance",
        
        # Concepts
        "Overfitting occurs when model memorizes training data",
        "Cross-validation helps assess model generalization",
        "Regularization prevents overfitting",
    ]
    
    # Add metadata for filtering
    metadatas = [
        {"category": "basics"}, {"category": "basics"}, {"category": "basics"},
        {"category": "algorithms"}, {"category": "algorithms"}, {"category": "algorithms"},
        {"category": "data"}, {"category": "data"}, {"category": "data"},
        {"category": "concepts"}, {"category": "concepts"}, {"category": "concepts"},
    ]
    
    ids = [f"kb_{i}" for i in range(len(documents))]
    embeddings = model.encode(documents).tolist()
    
    # Add to collection
    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas
    )
    
    print(f"✓ Added {len(documents)} documents to persistent database")
    print("\n💾 Database saved to disk - survives program restarts!")
    
    return client, collection


def filtered_search(collection):
    """Search with metadata filters."""
    
    print("\n" + "=" * 70)
    print("PART 4: FILTERED SEARCH")
    print("=" * 70)
    
    query = "How do I prevent models from overfitting?"
    
    print(f"\nQuery: '{query}'")
    print("Filter: category = 'concepts'")
    
    query_embedding = model.encode([query]).tolist()
    
    # Search with filter
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3,
        where={"category": "concepts"}  # Filter by metadata
    )
    
    print("\nFiltered Results:")
    print("-" * 70)
    
    for i, (doc, meta) in enumerate(zip(results['documents'][0], 
                                        results['metadatas'][0]), 1):
        print(f"\n{i}. Category: {meta['category']}")
        print(f"   {doc}")
    
    print("\n💡 TIP:")
    print("Metadata filtering is powerful for:")
    print("  - Searching within specific sections")
    print("  - Time-based filtering (date ranges)")
    print("  - User permissions (only search your documents)")


def build_qa_system(collection):
    """Simple Q&A system using vector search."""
    
    print("\n" + "=" * 70)
    print("PART 5: SIMPLE Q&A SYSTEM")
    print("=" * 70)
    
    # Sample questions
    questions = [
        "What's the difference between supervised and unsupervised learning?",
        "How do random forests work?",
        "What causes overfitting?",
        "Why split data into training and test sets?",
    ]
    
    print("\nAsking questions to the knowledge base:\n")
    
    for question in questions:
        print("-" * 70)
        print(f"Q: {question}")
        
        # Search
        query_embedding = model.encode([question]).tolist()
        results = collection.query(
            query_embeddings=query_embedding,
            n_results=1
        )
        
        # Best answer
        answer = results['documents'][0][0]
        distance = results['distances'][0][0]
        similarity = 1 - (distance / 2)
        
        print(f"A: {answer}")
        print(f"   (confidence: {similarity:.2%})")
        print()


def compare_to_traditional_db():
    """Explain vector DB vs traditional database."""
    
    print("\n" + "=" * 70)
    print("PART 6: VECTOR DB vs TRADITIONAL DATABASE")
    print("=" * 70)
    
    comparison = """
    TRADITIONAL DATABASE (SQL, NoSQL):
    ===================================
    Query:  SELECT * FROM docs WHERE text LIKE '%machine learning%'
    How:    Exact keyword matching
    Result: Only docs containing "machine learning"
    Speed:  Fast (indexed), but limited
    
    VECTOR DATABASE:
    ================
    Query:  Find docs similar to: "What is AI?"
    How:    Semantic similarity (embeddings + cosine distance)
    Result: Docs about ML, AI, neural networks (related concepts!)
    Speed:  Fast (HNSW, IVF indexes), millions of vectors
    
    KEY DIFFERENCES:
    ================
    
    1. SEARCH TYPE:
       Traditional: Exact/fuzzy keyword matching
       Vector:      Semantic similarity (meaning-based)
    
    2. QUERY:
       Traditional: SQL/NoSQL query language
       Vector:      Natural language or example text
    
    3. INDEX:
       Traditional: B-trees, hash indexes
       Vector:      Approximate Nearest Neighbor (ANN) - HNSW, IVF
    
    4. USE CASES:
       Traditional: Structured data (users, orders, inventory)
       Vector:      Semantic search, recommendations, RAG
    
    5. PERFORMANCE:
       Traditional: O(log n) for indexed queries
       Vector:      O(log n) approximate (99%+ accuracy)
    
    WHEN TO USE VECTOR DB:
    ======================
    ✓ Semantic search (find by meaning)
    ✓ Recommendations (similar products/content)
    ✓ Duplicate detection
    ✓ RAG systems (LLM + knowledge retrieval)
    ✓ Image/audio similarity search
    ✓ Anomaly detection
    
    POPULAR VECTOR DATABASES:
    =========================
    • ChromaDB (what we're using) - Simple, embedded
    • Pinecone - Managed, scalable
    • Weaviate - GraphQL, open-source
    • Milvus - Distributed, high-performance
    • Qdrant - Rust-based, fast
    • pgvector - PostgreSQL extension
    • FAISS - Facebook AI, library (not full DB)
    """
    
    print(comparison)


def advanced_concepts():
    """Explain advanced vector DB concepts."""
    
    print("\n" + "=" * 70)
    print("PART 7: ADVANCED CONCEPTS")
    print("=" * 70)
    
    concepts = """
    1. APPROXIMATE NEAREST NEIGHBOR (ANN):
       ====================================
       Problem: Exact search in high dimensions is slow
       Solution: Trade 1-2% accuracy for 100x speed
       
       Algorithms:
       • HNSW (Hierarchical Navigable Small World)
         - Graph-based, very fast, memory-intensive
       • IVF (Inverted File Index)
         - Cluster-based, good for large datasets
       • LSH (Locality Sensitive Hashing)
         - Hash similar items to same buckets
    
    2. DISTANCE METRICS:
       ==================
       • Cosine Distance (most common for text)
         - Range: 0 (identical) to 2 (opposite)
         - Ignores magnitude, focuses on direction
       
       • Euclidean Distance (L2)
         - Straight-line distance in n-dimensional space
         - Good for images, spatial data
       
       • Dot Product
         - Combines magnitude and direction
         - Fast, used in some recommender systems
    
    3. INDEXING STRATEGIES:
       =====================
       • Flat Index: Brute force, 100% accurate, slow
       • HNSW: Fast queries, high memory
       • IVF: Balanced speed/memory, good for large scale
    
    4. OPTIMIZATION TIPS:
       ===================
       • Batch inserts (1000s at a time)
       • Choose right distance metric
       • Use metadata filters to reduce search space
       • Normalize embeddings (for cosine similarity)
       • Cache frequently accessed results
    
    5. SCALING:
       =========
       • Single machine: up to ~10M vectors
       • Distributed: billions of vectors
       • Consider: Pinecone, Weaviate, Milvus for scale
    """
    
    print(concepts)


def next_steps():
    """What to build next."""
    
    print("\n" + "=" * 70)
    print("🚀 WHAT TO BUILD NEXT")
    print("=" * 70)
    
    projects = """
    BEGINNER PROJECTS:
    ==================
    1. Personal Document Search
       - Index your notes, PDFs, articles
       - Search by questions, not keywords
    
    2. FAQ Chatbot
       - Store Q&A pairs as embeddings
       - Match user questions to best answers
    
    3. Content Recommender
       - "Users who liked X also liked Y"
       - Based on embedding similarity
    
    INTERMEDIATE PROJECTS:
    ======================
    4. Code Search Engine
       - Index code snippets with descriptions
       - Natural language → find relevant code
    
    5. Research Paper Organizer
       - Auto-cluster papers by topic
       - Find related papers
    
    6. Customer Support Ticket Routing
       - Classify tickets by similarity
       - Find duplicate issues automatically
    
    ADVANCED PROJECTS:
    ==================
    7. RAG System (Retrieval Augmented Generation)
       - Vector DB + LLM = accurate, grounded responses
       - Next major topic in your learning path!
    
    8. Multi-modal Search
       - Search images with text (CLIP embeddings)
       - Find products by description + image
    
    9. Real-time Recommendation Engine
       - Update embeddings as users interact
       - Hybrid search (vector + filters)
    """
    
    print(projects)


def main():
    """Run all demonstrations."""
    
    print("\n")
    print("🗄️  " + "=" * 65 + " 🗄️")
    print("   VECTOR DATABASES: STORING & SEARCHING EMBEDDINGS")
    print("🗄️  " + "=" * 65 + " 🗄️")
    
    # Part 1: Create simple collection
    client, collection = create_simple_collection()
    
    # Part 2: Query it
    query_collection(collection)
    
    # Part 3: Persistent database
    persistent_client, persistent_collection = persistent_database()
    
    # Part 4: Filtered search
    filtered_search(persistent_collection)
    
    # Part 5: Q&A system
    build_qa_system(persistent_collection)
    
    # Part 6: Comparison
    compare_to_traditional_db()
    
    # Part 7: Advanced concepts
    advanced_concepts()
    
    # Part 8: Next steps
    next_steps()
    
    print("\n" + "=" * 70)
    print("🎓 CONGRATULATIONS!")
    print("=" * 70)
    print("""
    You now understand:
    ✓ What embeddings are (dense vector representations)
    ✓ How to measure similarity (cosine, euclidean)
    ✓ How to store embeddings (vector databases)
    ✓ How to search by meaning (semantic search)
    
    YOU'RE READY FOR:
    📚 Phase 3: Neural Networks & Transformers
    🤖 Phase 4: LLMs & RAG Systems
    
    Keep building! The best way to learn is by doing.
    """)


if __name__ == "__main__":
    main()
