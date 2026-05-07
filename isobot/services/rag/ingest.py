from isobot.utils.pdf_reader import extract_pdf_text
from isobot.services.rag.embedding import embed_text
from isobot.services.rag.vector_store import store, get_vector_path
#from isobot.utils.text_splitter import split_text
from isobot.services.rag.iso_parser import extract_iso_structure, iso_chunker
import os
import re

def extract_iso_name(file_path: str) -> str:
    filename = os.path.basename(file_path).lower()

    # enlever extension
    name = os.path.splitext(filename)[0]

    # normaliser
    name = name.replace(" ", "_")

    # extraire pattern iso_xxx
    match = re.search(r"iso[_\s-]*\d+", name)

    if match:
        return match.group(0).replace(" ", "_").replace("-", "_")

    # fallback si pas standardisé
    return name
  
  
def ingest_pdf(file_path: str, iso_name: str):
    
    
    path = get_vector_path(iso_name)

    # 🔥 IMPORTANT : éviter reprocessing
    if os.path.exists(path) and os.path.getsize(path) > 0:
        print(f"[ISOBOT] Vector store exists for {iso_name} → skipping ingestion")
        return

    print(f"[ISOBOT] Building vector store for {iso_name}...")
    
    # 1. extraction PDF
    text = extract_pdf_text(file_path)

    # 2. parsing ISO structure
    structured = extract_iso_structure(text)

    # 3. chunking intelligent
    chunks = iso_chunker(structured)

    # 4. embeddings + stockage
    for chunk in chunks:
        emb = embed_text(chunk["text"])

        store(
            text=chunk["text"],
            embedding=emb,
            metadata=chunk["metadata"],
            iso_name=iso_name
        )
