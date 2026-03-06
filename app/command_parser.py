from app.ollama_client import generate_command


def parse_user_input(user_input: str):

    command = generate_command(user_input)

    return command
