import requests
import json


def get_works():
    request = requests.get("http://127.0.0.1:8000/obras")
    return json.loads(request.content)


def post_work(work: dict):
    requests.post("http://127.0.0.1:8000/obras", data=json.dumps(work))


def put_work(id: str, work: dict):
    requests.put(f"http://127.0.0.1:8000/obras/{id}", data=json.dumps(work))


def delete_work(id: str):
    requests.delete(f"http://127.0.0.1:8000/obras/{id}")
