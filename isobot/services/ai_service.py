from openai import OpenAI
import os
from dotenv import load_dotenv

#load openai_api_key from .env file
load_dotenv()
# 
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# 
def improve_text(text):
    prompt = f"""
    Tu es un expert ISO 9001.

    Corrige et améliore ce document :
    - structure
    - clarté
    - responsabilités
    - conformité ISO

    Document:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content



def ask_openai(prompt: str):
    use_local = os.getenv("USE_LOCAL_AI", "false").lower() == "true"

    # Mode forcé local
    if use_local:
        return ask_local(prompt)

    # Essayer OpenAI
    try:
        from isobot.services.ai_service import ask_openai
        return ask_openai(prompt)

    except Exception as e:
        print(f"[ISOBOT] OpenAI indisponible → fallback local: {e}")
        return ask_local(prompt)
