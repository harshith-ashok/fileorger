from pathlib import Path

IGNORE = [".DS_Store", ".localized"]


def read_files(directory):

    path = Path(directory)

    files = []

    for item in path.iterdir():
        if item.is_file() and item.name not in IGNORE:
            files.append(item.name)

    return files
