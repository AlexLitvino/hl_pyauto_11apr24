from urllib import request

from L17.p5_abstract_factory.factories import AbstractFactory


class Connector:

    def __init__(self, factory: AbstractFactory):
        self.protocol = factory.create_protocol()
        self.port = factory.create_port()
        self.parse = factory.create_parser()

    def read(self, host, path):
        url = f"{self.protocol}://{host}:{str(self.port)}{path}"
        print(f"Connecting to {url}")
        return request.urlopen(url).read()
