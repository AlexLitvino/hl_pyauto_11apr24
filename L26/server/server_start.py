import datetime
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import logging
import os

logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
tail, head = os.path.split(__file__)
FILE_PATH = os.path.join(tail, 'data', 'request_info.txt')  # TODO: add dir creation
logger.debug(f"FILE_PATH: {FILE_PATH}")
directory = os.path.join(tail, 'data')
if not os.path.exists(directory):
    os.makedirs(directory)

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
        self.wfile.write(f'<body><i>GET</i> request was received on {now}</body></html>'.encode())

        write_request_info(FILE_PATH, request_info)
        logger.debug("GET processed")

    def do_POST(self):
        logger.info("In POST handler")
        self.send_response(201)
        logger.debug("Send 201")
        self.end_headers()

        if self.headers.get('Content-Length'):
            content_len = int(self.headers.get('Content-Length'))
            body = self.rfile.read(content_len)
        else:
            body = ''

        now = datetime.datetime.now()
        request_info = f"{now} {self.requestline}\n{self.headers}\n{body}\n"
        print(request_info)

        write_request_info(FILE_PATH, request_info)
        logger.debug("POST processed")


def run(server_class=HTTPServer, handler_class=HttpHandler):
    logger.error("Server is in process of starting...")
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


def write_request_info(file_path, data):
    logger.warning("Writing data")
    with open(file_path, 'a') as f:
        f.write('=' * 120)
        f.write(data + '\n')
        f.write('=' * 120)


if __name__ == '__main__':
    run()
