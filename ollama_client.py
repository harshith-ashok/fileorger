import ollama

MODEL = "qwen2.5-coder:14b"


def ask_llm(messages):

    response = ollama.chat(
        model=MODEL,
        messages=messages
    )

    return response["message"]["content"]
