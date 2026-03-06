from fastapi import FastAPI
from pydantic import BaseModel
import ollama
import json

app = FastAPI()


class Chat(BaseModel):
    message: str


SYSTEM_PROMPT = """
Convert natural language requests into Unix shell commands.

Return ONLY JSON.

Format:
{
 "command": "<shell command>"
}

No explanations.
"""


@app.post("/chat")
def chat(data: Chat):
    res = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": data.message},
        ],
    )

    output = res["message"]["content"]

    try:
        command = json.loads(output)["command"]
    except:
        command = output.split("\n")[0]

    return {"command": command.strip()}
