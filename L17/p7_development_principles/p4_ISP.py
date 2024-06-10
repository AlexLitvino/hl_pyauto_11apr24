from abc import ABC, abstractmethod


class BackAndForthCloseable(ABC):

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def back(self):
        pass


class Closeable(ABC):

    @abstractmethod
    def close(self):
        pass


class BackAndForth(ABC):

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def back(self):
        pass
