import subprocess
import time


import pytest
import requests

def start_server(output=None):
    start_command = "docker run --rm --name calc -p 5000:5000 alexlitvino/calculapiz:0.0.2"
    output = subprocess.PIPE if output is None else open(output)
    subprocess.Popen(start_command.split(), stdout=output)

def stop_server():
    stop_command = "docker container stop calc"
    subprocess.Popen(stop_command.split())


def wait_for_server_started(timeout, step):
    for i in range(int(timeout/step)):
        try:
            response = requests.get('http://localhost:5000/')
            if 0 < response.status_code < 600:
                break
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(step)
    else:
        raise Exception("Server wasn't started")

@pytest.fixture()
def app():
    start_server()
    wait_for_server_started(5, 0.1)
    yield
    stop_server()

@pytest.fixture()
def stop_app():
    yield
    stop_server()


# docker ps -q -f name=calc