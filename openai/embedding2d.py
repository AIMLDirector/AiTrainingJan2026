import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sentence_transformers import SentenceTransformer

# 1. Generate embeddings for several related/unrelated terms
model = SentenceTransformer('all-MiniLM-L6-v2')
words = ["cat", "kitten", "puppy", "dog", "laptop", "computer", "keyboard", "pizza", "burger"]
vectors = model.encode(words)
print("Original vector shape:", vectors.shape)  

# 2. Reduce dimensions from 384 down to 2 using t-SNE
tsne = TSNE(n_components=2, perplexity=5, random_state=42)
reduced_vectors = tsne.fit_transform(vectors)

# 3. Plot the results
plt.figure(figsize=(8, 6))
for i, word in enumerate(words):
    x, y = reduced_vectors[i, :]
    plt.scatter(x, y)
    plt.annotate(word, (x, y), xytext=(5, 2), textcoords='offset points')

plt.title("2D Projection of Word Embeddings")
plt.show()
