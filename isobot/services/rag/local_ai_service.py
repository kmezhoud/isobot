from ollama import chat

def ask_local(prompt: str, model: str = "mistral"):
    response = chat(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        options={
            "temperature": 0.2   # 🔥 ici
        }
    )

    return response["message"]["content"]
