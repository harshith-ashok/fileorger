from fastapi import FastAPI
from app.schemas import CommandRequest
from app.command_parser import parse_user_input
from app.executor import run_command
from app.security import validate_command

app = FastAPI()


@app.post("/terminal")
def ai_terminal(req: CommandRequest):

    command = parse_user_input(req.query)

    if not validate_command(command):
        return {
            "error": "Command not allowed",
            "command": command
        }

    output = run_command(command)

    return {
        "query": req.query,
        "command": command,
        "output": output
    }
