from fastapi import FastAPI
from app.categorizer import categorize_files
from app.folder_reader import read_files
from app.schemas import CommandRequest, FolderRequest
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


@app.post("/suggest-folders")
def suggest_folders(req: FolderRequest):

    files = read_files(req.path)

    categories = categorize_files(files)
    return categories
    # return {
    #     # "files": files,
    #     "categories": categories
    # }
