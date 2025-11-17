# Install required library:
# pip install sentence-transformers

from sentence_transformers import SentenceTransformer
import numpy as np

# Load a pre-trained embedding model
print("Loading model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded!\n")

# Example texts
texts = [
    "The cat sits on the mat",
    "A dog rests on the carpet",
    "The car is parked in the garage",
    "I love pizza and pasta"
]

# Generate embeddings for each text
print("Generating embeddings...")
embeddings = model.encode(texts)

print(f"\nEmbedding shape: {embeddings.shape}")
print(f"Number of texts: {embeddings.shape[0]}")
print(f"Dimensions per embedding: {embeddings.shape[1]}")

# Show first embedding (truncated)
print(f"\nFirst 10 values of embedding for '{texts[0]}':")
print(embeddings[0][:10])

# Calculate cosine similarity between texts
def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors"""
    dot_product = np.dot(vec1, vec2)
    magnitude = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return dot_product / magnitude

print("\n" + "="*60)
print("SIMILARITY SCORES (closer to 1 = more similar)")
print("="*60)

for i in range(len(texts)):
    for j in range(i + 1, len(texts)):
        similarity = cosine_similarity(embeddings[i], embeddings[j])
        print(f"\n'{texts[i]}'")
        print(f"  vs")
        print(f"'{texts[j]}'")
        print(f"  Similarity: {similarity:.4f}")
