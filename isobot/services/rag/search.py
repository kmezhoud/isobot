# isobot/services/rag/search.py

from isobot.services.rag.vector_store import get_all
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# def search(query, top_k=3):
#     vector_db = get_all()
# 
#     if not vector_db:
#         return []
# 
#     # ici tu dois aussi embed le query
#     from isobot.services.rag.embedding import embed_text
#     query_emb = embed_text(query)
# 
#     scored = []
#     for item in vector_db:
#         score = cosine_similarity(query_emb, item["embedding"])
#         scored.append((score, item["text"]))
# 
#     scored.sort(reverse=True)
# 
#     return [text for _, text in scored[:top_k]]
from isobot.services.rag.vector_store import get_vector_path, load_db

def search(question: str, iso_name="iso_9001"):

    # 🔥 ICI (pas dans ask)
    path = get_vector_path(iso_name)
    db = load_db(path)

    # TODO: remplacer par vraie recherche vectorielle
    return db[:5]
