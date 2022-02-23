def helper_adjust_authors(obras: list) -> list:
    """Converte a lista de autores das obras em uma string.

    :param obras: lista com todas as obras cadastradas.
    :return: list
    """
    if obras:
        for obra in obras:
            obra["authors"] = ", ".join(obra["authors"])
        return obras
    return obras
