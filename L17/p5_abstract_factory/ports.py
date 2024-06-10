from abc import ABC, abstractmethod


class Port(ABC):

    @abstractmethod
    def __str__(self):
        pass


class HTTPPort(Port):

    def __str__(self):
        return '80'


class HTTPSecurePort(Port):

    def __str__(self):
        return '443'


class FTPPort(Port):

    def __str__(self):
        return '21'
