from isobot.services.rag.search import search
from isobot.services.ai_router import ask_ai
from isobot.services.rag.ingest import ingest_pdf



def ask(question: str, iso_name="iso_9001"):

    context_chunks = search(question, iso_name)

    if not context_chunks:
        return "Aucun contexte trouvé."

    context = "\n\n".join(
        c["text"] if isinstance(c, dict) else str(c)
        for c in context_chunks
    )

    prompt = f"""
Tu es un expert ISO 9001.

Contexte:
{context}

Question:
{question}
"""

    return ask_ai(prompt)
