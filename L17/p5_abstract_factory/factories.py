from abc import ABC, abstractmethod

from L17.p5_abstract_factory.parsers import HTTPParser, FTPParser
from L17.p5_abstract_factory.ports import HTTPPort, HTTPSecurePort, FTPPort


class AbstractFactory(ABC):

    def __init__(self, is_secure):
        self.is_secure = is_secure

    @abstractmethod
    def create_protocol(self):
        pass

    @abstractmethod
    def create_port(self):
        pass

    @abstractmethod
    def create_parser(self):
        pass


class HTTPFactory(AbstractFactory):

    def create_protocol(self):
        if self.is_secure:
            return 'https'
        else:
            return 'http'

    def create_port(self):
        if self.is_secure:
            return HTTPSecurePort()
        else:
            return HTTPPort()

    def create_parser(self):
        return HTTPParser()


class FTPFactory(AbstractFactory):

    def create_protocol(self):
        return 'ftp'

    def create_port(self):
        return FTPPort()

    def create_parser(self):
        return FTPParser()
