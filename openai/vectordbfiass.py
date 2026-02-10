import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

# 1. Data & Embedding Generation
docs = ["The sun is a star.", "Fish live in water."]
embeddings = model.encode(docs).astype('float32') # FAISS requires float32

# 2. Store: Initialize Index and Add Vectors
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)  # Uses Euclidean distance
index.add(embeddings)

# 3. Query
query_text = "What is the sun?"
query_embedding = model.encode([query_text]).astype('float32')
distances, indices = index.search(query_embedding, k=1)

# 4. Retrieve Original Text
match_index = indices[0][0]
print(f"FAISS Match: {docs[match_index]} | Distance: {distances[0][0]}")
