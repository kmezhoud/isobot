REQUIRED_SECTIONS = [
    "objet",
    "champ d'application",
    "responsabilités",
    "description"
]

def check_structure(text):
    result = {}
    text_lower = text.lower()

    for section in REQUIRED_SECTIONS:
        result[section] = section in text_lower

    score = sum(result.values()) / len(REQUIRED_SECTIONS) * 100

    return {
        "sections": result,
        "score_iso": score
    }
