from ting_file_management.file_management import txt_importer


def process(path_file, instance):
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
    print(f"{data_process}")


def remove(instance):
    result = instance.dequeue()

    if result is None:
        return print("Não há elementos")

    return print(f"Arquivo {result['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
