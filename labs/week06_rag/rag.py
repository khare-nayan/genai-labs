from utils.embeddings import get_embedding
from utils.vector_store import VectorStore
from utils.llm_client import chat

documents = open("sample_text.txt").read().split("\n")

store = VectorStore(dim=1536)

embeddings = [get_embedding(d) for d in documents]
store.add(embeddings, documents)

query = "What is AI?"

context = "\n".join(store.search(get_embedding(query)))

prompt = f"""
Answer using context only:

{context}

Question: {query}
"""

print(chat(prompt))