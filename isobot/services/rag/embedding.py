import os

from ollama import embeddings

def embed_text(text: str):

    # 🔥 sécurité taille (OBLIGATOIRE)
    if len(text) > 1500:
        text = text[:1500]

    try:
        #  LOCAL FIRST (OBLIGATOIRE)
        return embeddings(
            model="nomic-embed-text",
            prompt=text
        )["embedding"]

    except Exception as local_error:
        print(f"[ISOBOT] Local embedding failed: {local_error}")

        #  fallback OpenAI (optionnel)
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise Exception("No embedding engine available (local + openai failed)")

        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        res = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )

        return res.data[0].embedding
