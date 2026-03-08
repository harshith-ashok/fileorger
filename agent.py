import json
import ollama

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

import re


transport = StdioTransport(
    command="python",
    args=["mcp_server.py"]
)

client = None


SYSTEM_PROMPT = """
You are a tool-using agent.

Available tools:
- list_files(path)
- read_file(path)

Rules:
1. NEVER guess filenames.
2. Use list_files first to see available files.
3. Only read files that exist.

Respond ONLY with JSON.

Example:
{"tool":"list_files","args":{"path":"."}}
"""


async def run_agent(prompt: str):

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )

    content = response["message"]["content"]

    match = re.search(r"\{.*\}", content, re.S)

    if not match:
        raise Exception(f"Model did not return JSON:\n{content}")

    tool_call = json.loads(match.group())

    tool = tool_call["tool"]
    args = tool_call["args"]
    try:
        result = await client.call_tool(tool, args)
    except Exception as e:
        result = {"error": str(e)}

    print("LLM RESPONSE:", content)
    return result
