ALLOWED_COMMANDS = [
    "ls",
    "cat",
    "grep",
    "find",
    "pwd",
    "echo",
    "du",
    "df"
]


def validate_command(command: str):

    cmd = command.split()[0]

    if cmd not in ALLOWED_COMMANDS:
        return False

    return True
