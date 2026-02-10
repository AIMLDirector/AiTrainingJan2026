import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 1. Initialize persistent storage
client = chromadb.PersistentClient(path="./my_chroma_db")
collection = client.get_or_create_collection(name="knowledge_base")

# 2. Data & Embedding Generation
docs = ["The sun is a star.", "Fish live in water."]  # 10TB
embeddings = model.encode(docs).tolist() 
#print(embeddings)
# 3. Store: IDs are required
collection.add(
    ids=["doc1", "doc2"],
    documents=docs,
    embeddings=embeddings,
    metadatas=[{"topic": "space"}, {"topic": "biology"}]
)

# 4. Query
query_text = "What is the sun?"
query_embedding = model.encode(query_text).tolist()
results = collection.query(query_embeddings=[query_embedding], n_results=1)
# print(results)

print(f"Chroma Match: {results['documents'][0][0]} | Score: {results['distances'][0][0]}")
