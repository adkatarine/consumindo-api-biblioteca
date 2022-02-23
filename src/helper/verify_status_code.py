""" Classe contendo verificações de status code.

"""
import requests


def verify_status_code_between_400(request) -> bool:
    """Verifica se o status code retornado configura um erro.

    :param request: resposta de uma solicitação HTTP.
    :return: bool
    """
    if 400 <= request.status_code < 500:
        return False
    return True


def verify_status_code_between_200(request) -> bool:
    """Verifica se o status code retornado configura uma solicitação bem sucedida.

    :param request: resposta de uma solicitação HTTP.
    :return: bool
    """
    if request.status_code == requests.codes.ok:
        return True
    return False
