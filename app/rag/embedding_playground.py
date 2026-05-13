from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

sentences = [
    "Dogs are wonderful pets",
    "Cats are independent animals",
    "I love programming in Python",
    "Puppies are cute companions"
]

embeddings = model.encode(sentences)

similarity = cosine_similarity(
    [embeddings[0]],
    [embeddings[3]]
)
print(embeddings.shape)

query = "cute dogs"

query_embedding = model.encode([query])

scores = cosine_similarity(
    query_embedding,
    embeddings
)

for sentence, score in zip(sentences, scores[0]):
    print(f"{sentence} -> {score:.4f}")