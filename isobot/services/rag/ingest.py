from isobot.utils.pdf_reader import extract_pdf_text
from isobot.services.rag.embedding import embed_text
from isobot.services.rag.vector_store import store
#from isobot.utils.text_splitter import split_text
from isobot.services.rag.iso_parser import extract_iso_structure, iso_chunker


def ingest_pdf(file_path: str):

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
            metadata=chunk["metadata"]
        )
