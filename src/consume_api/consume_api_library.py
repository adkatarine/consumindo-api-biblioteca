import requests
import json


def get_works():
    request = requests.get("http://127.0.0.1:8000/obras")
    return json.loads(request.content)


def post_work(work):
    requests.post("http://127.0.0.1:8000/obras", data=json.dumps(work))
