"""
Semantic Similarity Explorer
=============================
Compare text similarity using embeddings.

This demonstrates how embeddings capture meaning, not just keywords.

Installation:
pip install sentence-transformers numpy scikit-learn
"""

from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load model once (reuse across functions)
model = SentenceTransformer('all-MiniLM-L6-v2')


def compare_sentences(sentence1, sentence2):
    """Compare two sentences and show their similarity score."""
    
    print("\n" + "=" * 70)
    print("COMPARING SENTENCES")
    print("=" * 70)
    
    # Generate embeddings
    embeddings = model.encode([sentence1, sentence2])
    
    # Calculate cosine similarity
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    
    print(f"\nSentence 1: '{sentence1}'")
    print(f"Sentence 2: '{sentence2}'")
    print(f"\nSimilarity Score: {similarity:.4f}")
    
    # Interpretation
    if similarity > 0.8:
        print("📊 Interpretation: Very similar (almost identical meaning)")
    elif similarity > 0.6:
        print("📊 Interpretation: Similar (related topics)")
    elif similarity > 0.4:
        print("📊 Interpretation: Somewhat related")
    else:
        print("📊 Interpretation: Not very similar (different topics)")
    
    return similarity


def keyword_vs_semantic():
    """Show why semantic search beats keyword search."""
    
    print("\n" + "=" * 70)
    print("KEYWORD SEARCH vs SEMANTIC SEARCH")
    print("=" * 70)
    
    query = "How do I fix my computer that won't start?"
    
    documents = [
        "Troubleshooting a PC that fails to boot",  # No shared keywords!
        "My computer won't turn on",                # Some keywords
        "Buy cheap computers online",               # Shared keyword, wrong meaning
        "Computer repair services near me",         # Related
    ]
    
    print(f"\nQuery: '{query}'")
    print("\nDocuments:")
    for i, doc in enumerate(documents, 1):
        print(f"  {i}. {doc}")
    
    # Semantic search
    query_emb = model.encode([query])[0]
    doc_embs = model.encode(documents)
    
    print("\n" + "-" * 70)
    print("SEMANTIC SIMILARITY SCORES:")
    print("-" * 70)
    
    results = []
    for i, doc_emb in enumerate(doc_embs):
        similarity = cosine_similarity([query_emb], [doc_emb])[0][0]
        results.append((similarity, i, documents[i]))
        print(f"\nDoc {i+1}: {similarity:.4f}")
        print(f"  '{documents[i]}'")
    
    # Sort by similarity
    results.sort(reverse=True)
    
    print("\n" + "=" * 70)
    print("BEST MATCH (by semantic meaning):")
    print("=" * 70)
    score, idx, doc = results[0]
    print(f"'{doc}' (Score: {score:.4f})")
    
    print("\n💡 INSIGHT:")
    print("Document 1 ranks highest even though it shares NO keywords!")
    print("Semantic search understands 'troubleshooting PC boot failure'")
    print("means the same as 'fix computer that won't start'")


def find_paraphrases():
    """Detect paraphrases (same meaning, different words)."""
    
    print("\n" + "=" * 70)
    print("PARAPHRASE DETECTION")
    print("=" * 70)
    
    # Original sentence
    original = "Artificial intelligence is transforming the technology industry"
    
    # Test sentences (some are paraphrases, some aren't)
    test_sentences = [
        "AI is revolutionizing tech sector",           # Paraphrase
        "Machine intelligence is changing technology", # Paraphrase
        "The weather is nice today",                   # Unrelated
        "Artificial intelligence in healthcare",       # Related but different
        "Technology companies use AI",                 # Related but different focus
    ]
    
    print(f"\nOriginal: '{original}'")
    print("\nTesting for paraphrases:\n")
    
    original_emb = model.encode([original])[0]
    test_embs = model.encode(test_sentences)
    
    threshold = 0.65  # Similarity threshold for paraphrase
    
    for i, (test_sent, test_emb) in enumerate(zip(test_sentences, test_embs), 1):
        similarity = cosine_similarity([original_emb], [test_emb])[0][0]
        is_paraphrase = "✅ PARAPHRASE" if similarity >= threshold else "❌ NOT PARAPHRASE"
        
        print(f"{i}. {is_paraphrase} (Score: {similarity:.4f})")
        print(f"   '{test_sent}'")
        print()


def semantic_clustering():
    """Group similar sentences together (clustering by meaning)."""
    
    print("\n" + "=" * 70)
    print("SEMANTIC CLUSTERING")
    print("=" * 70)
    
    sentences = [
        # Cluster 1: ML/AI
        "Machine learning algorithms learn from data",
        "Neural networks are used in deep learning",
        "AI models require training data",
        
        # Cluster 2: Programming
        "Python is a popular programming language",
        "JavaScript runs in web browsers",
        "Java is used for enterprise applications",
        
        # Cluster 3: Food
        "Pizza is a delicious Italian dish",
        "Sushi is traditional Japanese cuisine",
        "Tacos are a Mexican food favorite",
    ]
    
    print("\nSentences to cluster:")
    for i, sent in enumerate(sentences, 1):
        print(f"{i:2d}. {sent}")
    
    # Generate embeddings
    embeddings = model.encode(sentences)
    
    # Calculate similarity matrix
    similarity_matrix = cosine_similarity(embeddings)
    
    print("\n" + "-" * 70)
    print("SIMILARITY MATRIX (showing high similarities only):")
    print("-" * 70)
    
    for i in range(len(sentences)):
        for j in range(i + 1, len(sentences)):
            similarity = similarity_matrix[i][j]
            if similarity > 0.5:  # Only show significant similarities
                print(f"\n{similarity:.4f}: Sentences {i+1} and {j+1}")
                print(f"  '{sentences[i]}'")
                print(f"  '{sentences[j]}'")
    
    print("\n💡 OBSERVATION:")
    print("Sentences about similar topics cluster together!")
    print("- AI/ML sentences have high similarity with each other")
    print("- Programming sentences cluster together")
    print("- Food sentences form their own cluster")


def multilingual_similarity():
    """Check if embeddings work across languages."""
    
    print("\n" + "=" * 70)
    print("MULTILINGUAL EMBEDDINGS")
    print("=" * 70)
    
    print("\n⚠️  NOTE: 'all-MiniLM-L6-v2' is English-only.")
    print("For multilingual, use: 'paraphrase-multilingual-MiniLM-L12-v2'")
    
    # For this demo, we'll use paraphrases in English
    sentences_en = [
        "Hello, how are you?",
        "Hi, how are you doing?",
        "Good morning, how's it going?",
    ]
    
    print("\nComparing English paraphrases:")
    embeddings = model.encode(sentences_en)
    
    for i in range(len(sentences_en)):
        for j in range(i + 1, len(sentences_en)):
            similarity = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]
            print(f"\n{similarity:.4f}: '{sentences_en[i]}' vs '{sentences_en[j]}'")
    
    print("\n💡 TIP:")
    print("To compare across languages, use a multilingual model:")
    print("  model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')")


def practical_use_cases():
    """Show real-world applications."""
    
    print("\n" + "=" * 70)
    print("PRACTICAL USE CASES")
    print("=" * 70)
    
    use_cases = """
    1. SEMANTIC SEARCH 🔍
       - Search documentation by meaning, not keywords
       - Find similar customer questions in support tickets
       - Product recommendations based on description similarity
    
    2. DUPLICATE DETECTION 🔄
       - Find duplicate support tickets
       - Identify plagiarism or copied content
       - Merge similar database entries
    
    3. CONTENT RECOMMENDATION 📚
       - Recommend similar articles/blogs
       - Suggest related videos
       - Find products based on description similarity
    
    4. QUESTION ANSWERING 💬
       - Match user questions to FAQ answers
       - Find relevant documentation sections
       - Chatbot intent classification
    
    5. TEXT CLASSIFICATION 🏷️
       - Categorize emails, tickets, reviews
       - Sentiment analysis
       - Topic modeling
    
    6. CLUSTERING & ORGANIZATION 📊
       - Group similar documents automatically
       - Organize research papers by topic
       - Customer segmentation by feedback
    
    7. TRANSLATION QUALITY 🌍
       - Compare translation to original meaning
       - Assess paraphrase quality
       - Cross-lingual information retrieval
    """
    
    print(use_cases)


def main():
    """Run all demonstrations."""
    
    print("\n")
    print("🔍 " + "=" * 66 + " 🔍")
    print("   SEMANTIC SIMILARITY: UNDERSTANDING TEXT RELATIONSHIPS")
    print("🔍 " + "=" * 66 + " 🔍")
    
    # Demo 1: Basic comparison
    compare_sentences(
        "The cat is sleeping on the couch",
        "A feline is resting on the sofa"
    )
    
    compare_sentences(
        "Python is a programming language",
        "Pizza is my favorite food"
    )
    
    # Demo 2: Keyword vs semantic
    keyword_vs_semantic()
    
    # Demo 3: Paraphrase detection
    find_paraphrases()
    
    # Demo 4: Clustering
    semantic_clustering()
    
    # Demo 5: Multilingual
    multilingual_similarity()
    
    # Demo 6: Use cases
    practical_use_cases()
    
    print("\n" + "=" * 70)
    print("🎯 KEY TAKEAWAYS:")
    print("=" * 70)
    print("""
    ✓ Embeddings capture MEANING, not just keywords
    ✓ Cosine similarity measures semantic relatedness
    ✓ Similar meanings = similar vectors (high similarity score)
    ✓ Works for: search, recommendations, clustering, classification
    
    NEXT: vector_database_demo.py - Learn to store & search embeddings at scale!
    """)


if __name__ == "__main__":
    main()
