import os
from isobot.services.rag.local_ai_service import ask_local
from isobot.services.ai_service import ask_openai

# import conditionnel
try:
    from isobot.services.ai_service import ask_openai
    OPENAI_AVAILABLE = True
except Exception:
    OPENAI_AVAILABLE = False


def ask_ai(prompt: str):
    use_local = os.getenv("USE_LOCAL_AI", "false").lower() == "true"

    #  1. Mode forcé local
    if use_local:
        return ask_local(prompt)

    #  2. Essayer OpenAI si dispo
    if OPENAI_AVAILABLE:
        try:
            return ask_openai(prompt)
        except Exception as e:
            print(f"[ISOBOT] OpenAI failed → fallback local: {e}")

    #  3. Fallback automatique
    return ask_local(prompt)
