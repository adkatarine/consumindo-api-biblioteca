""" Arquivo contendo as solicitações HTTP para a API de obras da biblioteca.

"""
from src.helper.verify_status_code import (
    verify_status_code_between_400,
    verify_status_code_between_200,
)
from src.config.library_api import library_url
import requests
import json


def get_works() -> list:
    """Solicitação GET de todas as obras cadastradas.

    :return: list
    """
    request = requests.get(f"{library_url['works_url']}")
    print(request.status_code)
    if verify_status_code_between_200(request):
        return json.loads(request.content)
    return []


def post_work(work: dict) -> bool:
    """Solicitação POST para cadastrar uma obra.

    :param work: dados da obra que será cadastrada.
    :return: bool
    """
    request = requests.post(f"{library_url['works_url']}", data=json.dumps(work))
    return verify_status_code_between_400(request)


def put_work(id: str, work: dict) -> bool:
    """Solicitação PUT para atualizar uma obra.

    :param id: id da obra que será atualizada.
    :param work: dados da obra que será atualizada.
    :return: bool
    """
    request = requests.put(f"{library_url['works_url']}/{id}", data=json.dumps(work))
    return verify_status_code_between_400(request)


def delete_work(id: str) -> bool:
    """Solicitação DELETE para excluir uma obra.

    :param id: id da obra que será excluída.
    :return: bool
    """
    request = requests.delete(f"{library_url['works_url']}/{id}")
    return verify_status_code_between_400(request)
