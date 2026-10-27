import hashlib
from pathlib import Path


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def find_duplicates(folder_path):
    folder = Path(folder_path).expanduser().resolve()

    if not folder.exists() or not folder.is_dir():
        raise ValueError("Please enter a valid folder path.")

    hashes = {}

    for file_path in folder.rglob("*"):
        if not file_path.is_file():
            continue

        try:
            file_hash = calculate_hash(file_path)
            hashes.setdefault(file_hash, []).append(file_path)
        except OSError as error:
            print(f"Skipped {file_path}: {error}")

    return [paths for paths in hashes.values() if len(paths) > 1]