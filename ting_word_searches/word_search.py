def exists_word(word, instance):
    if not word:
        return None

    result = []
    for item in instance._items:
        ocorrencias = [
            {"linha": linha + 1}
            for linha, conteudo in enumerate(item["linhas_do_arquivo"])
            if word.lower() in conteudo.lower()
        ]

        if ocorrencias:
            result.append(
                {
                    "palavra": word,
                    "arquivo": item["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
