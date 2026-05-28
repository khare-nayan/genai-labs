from utils.embeddings import get_embedding
import numpy as np

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

text1 = "AI is amazing"
text2 = "Artificial intelligence is powerful"

emb1 = get_embedding(text1)
emb2 = get_embedding(text2)

print("Similarity:", cosine(emb1, emb2))