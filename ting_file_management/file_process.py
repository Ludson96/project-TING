from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file: str, instance: Queue) -> None:
    if any(
        path_file == instance.search(index)["nome_do_arquivo"]
        for index in range(len(instance))
    ):
        return print(f"O arquivo '{path_file}' já foi processado.")

    lines_file = txt_importer(path_file)
    data_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines_file),
        "linhas_do_arquivo": lines_file,
    }
    instance.enqueue(data_process)
    return print(f"{data_process}")


def remove(instance: Queue) -> None:
    file = instance.dequeue()

    if file is None:
        return print("Não há elementos")

    return print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance: Queue, position: int):
    try:
        file = instance.search(position)

    except IndexError:
        return print("Posição inválida", file=sys.stderr)

    return print(file)
