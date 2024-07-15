import json
import logging
import time

import requests


logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

RATE = 1
delay = 1/RATE


def generator(file_path):
    logger.debug(f"Opening file {file_path}")
    with open(file_path, 'r') as f:
        requests_list = json.load(f)
    while True:
        yield from requests_list


def runner(file_path):
    g = generator(file_path)
    logger.info("Start sending requests...")
    for request in g:
        try:
            logger.debug(f"Sending request {request}")
            method = request["method"]
            url = request["url"]
            params = request.get("params", "")
            # TODO: add data, json
            headers = request.get("headers", {})
            response = requests.request(method=method, url=url, params=params, headers=headers)
            logger.debug(response)
            time.sleep(delay)
        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
     import sys
     requests_file_path = sys.argv[1]
     logger.debug(requests_file_path)
     runner(requests_file_path)
