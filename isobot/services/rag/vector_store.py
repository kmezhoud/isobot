# isobot/services/rag/vector_store.py

vector_db = []


def get_all():
    return vector_db

# isobot/services/rag/vector_store.py

import json
import os

#DB_PATH = "data/vector_store.json"
def get_vector_path(iso_name: str):
    return f"data/{iso_name}/vector_store.json"


def load_db(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_db(path, db):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(db, f)


def store(text, embedding, metadata=None, iso_name=None):
    

    path = get_vector_path(iso_name)

    db = load_db(path)

    db.append({
        "text": text,
        "embedding": embedding,
        "metadata": metadata or {}
    })

    save_db(path, db)
