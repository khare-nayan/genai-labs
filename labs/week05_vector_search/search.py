from utils.embeddings import get_embedding
from utils.vector_store import VectorStore

docs = [
    "AI is transforming healthcare",
    "Machine learning improves predictions",
    "Cloud computing enables scalability"
]

store = VectorStore(dim=1536)

embeddings = [get_embedding(d) for d in docs]
store.add(embeddings, docs)

query = "How is AI used in medicine?"
results = store.search(get_embedding(query))

print("Results:", results)