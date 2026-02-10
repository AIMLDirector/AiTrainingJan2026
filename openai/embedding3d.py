import plotly.express as px
from sklearn.manifold import TSNE
from sentence_transformers import SentenceTransformer

# 1. Prepare broader data to see distinct clusters
model = SentenceTransformer('all-MiniLM-L6-v2')
data = {
    "Pets": ["cat", "kitten", "dog", "puppy", "hamster"],
    "Tech": ["laptop", "smartphone", "computer", "software", "keyboard"],
    "Food": ["pizza", "burger", "sushi", "pasta", "taco"]
}

words = [item for sublist in data.values() for item in sublist]
labels = [category for category, items in data.items() for _ in items]

# 2. Generate Embeddings
vectors = model.encode(words)

# 3. Reduce to 3D using t-SNE
tsne = TSNE(n_components=3, perplexity=5, random_state=42)
vectors_3d = tsne.fit_transform(vectors)

# 4. Create Interactive 3D Plot
fig = px.scatter_3d(
    x=vectors_3d[:, 0], 
    y=vectors_3d[:, 1], 
    z=vectors_3d[:, 2],
    text=words,
    color=labels,
    title="3D Semantic Concept Map"
)

fig.update_traces(marker=dict(size=5))
fig.show()
