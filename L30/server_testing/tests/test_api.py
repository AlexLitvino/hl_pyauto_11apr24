"""
Login to Docker registry (docker login)
Download docker image
Start docker container
Perform test
Stop docker container


docker run --rm --name calc -p 5000:5000 alexlitvino/calculapiz:0.0.2
"""
import os.path
from enum import StrEnum
from urllib.parse import urljoin
import requests

BASE_URL = "http://localhost:5000/"
class Endpoints(StrEnum):
    ADD = urljoin(BASE_URL, "api/v1/add")


def test_add_nominal(app):
    response = requests.get(Endpoints.ADD, params={"op1": 34, "op2": 6})
    assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'
    assert response.json()['result'] == 40, "Error"

# def test_add_zero(tmp_path, stop_app):
#     start_app(os.path.join(tmp_path, 'server.log'))
#     response = requests.get(Endpoints.ADD, params={"op1": 0, "op2": 0})
#     assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'
#     assert response.json()['result'] == 0, "Error"