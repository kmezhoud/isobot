from isobot.services.rag.search import search
from isobot.services.ai_router import ask_ai
from isobot.services.rag.ingest import ingest_pdf

def ask(question: str):
    try:
        context_chunks = search(question)

        # protection
        if not context_chunks:
            context_chunks = []

        context = "\n".join(context_chunks)

        prompt = f"""
        Tu es un expert ISO 9001.

        Contexte:
        {context}

        Question:
        {question}
        """

        return ask_ai(prompt)

    except Exception as e:
        print(f"[ISOBOT ERROR] {e}")
        return f"Erreur interne: {str(e)}"
