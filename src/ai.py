import ollama

def ask_ai(prompt: str) -> str:
    """
    Sends a prompt to Ollama and returns the AI response.
    """

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]