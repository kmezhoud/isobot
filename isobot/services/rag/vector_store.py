# isobot/services/rag/vector_store.py

vector_db = []


def get_all():
    return vector_db

# isobot/services/rag/vector_store.py

import json
import os

DB_PATH = "data/vector_store.json"

def load_db():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_db(db):
    with open(DB_PATH, "w") as f:
        json.dump(db, f)


def store(text: str, embedding: list, metadata: dict = None):
    """
    Stocke chunk + embedding + metadata ISO
    """

    db = load_db()

    db.append({
        "text": text,
        "embedding": embedding,
        "metadata": metadata or {}
    })

    save_db(db)
