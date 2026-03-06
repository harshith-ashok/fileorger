import ollama


def generate_command(prompt: str):

    system_prompt = """
You are a Linux command generator.

Convert the user request into a safe Linux command.

Rules:
- Output ONLY the command
- No explanation
- Use common linux utilities
"""

    response = ollama.chat(
        model="codellama:latest",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()
