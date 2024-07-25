import datetime
import time
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import logging
import os
import threading

import requests

logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
tail, head = os.path.split(__file__)


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        logger.info("In GET handler")
        self.send_response(200)
        logger.debug("Send 200")
        self.send_header("Content-type", "text/html")
        self.end_headers()

        now = datetime.datetime.now()
        request_info = f"{now}\n{self.requestline}\n{self.path}\n{self.headers}\n"
        print(request_info)

        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Simple HTTP-server</title></head>'.encode())
        self.wfile.write(f'<body><i>GET</i> request was received on <b>{now}</b></body></html>'.encode())

    def do_POST(self):
        logger.info("In POST handler")
        self.send_response(201)
        logger.debug("Send 201")
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if self.headers.get('Content-Length'):
            content_len = int(self.headers.get('Content-Length'))
            body = self.rfile.read(content_len)
        else:
            body = ''

        now = datetime.datetime.now()
        request_info = f"{now} {self.requestline}\n{self.headers}\n{body}\n"
        print(request_info)


class Server:

    def __init__(self):
        self.thread = threading.Thread(target=self.run, args=(HTTPServer, HttpHandler))
        self.thread.start()

    def run(self, server_class=HTTPServer, handler_class=HttpHandler):
        logger.error("Server is in process of starting...")
        server_address = ('', 8000)
        self.httpd = server_class(server_address, handler_class)
        self.httpd.serve_forever()

    def stop_server(self):
        self.httpd.shutdown()


if __name__ == '__main__':
    server = Server()

    requests.get('http://localhost:8000')
    time.sleep(5)
    server.stop_server()
    print("After stop")
