from sentence_transformers import SentenceTransformer, util

# 1. Load a pre-trained model (small & fast)
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Define your source data
documents = [
    "The cat is sleeping on the rug.",
    "A robotic arm assembling a car.",
    "Global stock markets are rising today."
]

# 3. Generate embeddings (the "DNA" vectors)
doc_embeddings = model.encode(documents)

# 4. Search for something similar
query = "A feline is resting."
query_embedding = model.encode(query)

# 5. Calculate similarity scores
# util.cos_sim returns a matrix of similarity scores between 0 and 1
similarities = util.cos_sim(query_embedding, doc_embeddings)

# Output the results
for i, score in enumerate(similarities[0]):
    print(f"Score: {score:.4f} | Text: {documents[i]}")
