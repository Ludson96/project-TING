import sys
import os


def txt_importer(path_file: str) -> list[str]:
    if not os.path.exists(path_file):
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    if os.path.splitext(path_file)[1].lower() != ".txt":
        return print("Formato inválido", file=sys.stderr)

    with open(path_file, 'r') as file:
        content = file.read().split("\n")
        return content
