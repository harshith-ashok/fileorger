from fastapi import FastAPI
from contextlib import asynccontextmanager

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

import agent


transport = StdioTransport(
    command="python",
    args=["mcp_server.py"]
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with Client(transport) as client:

        # give the agent access to the client
        agent.client = client

        yield


app = FastAPI(lifespan=lifespan)


@app.post("/prompt")
async def prompt(data: dict):

    result = await agent.run_agent(data["prompt"])

    return {"response": result}
