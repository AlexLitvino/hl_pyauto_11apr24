from abc import ABC, abstractmethod
import json
import pickle


class AbstractReaderWriter(ABC):

    @staticmethod
    @abstractmethod
    def read(path):
        pass

    @staticmethod
    @abstractmethod
    def write(data, path):
        pass


class JSONReaderWriter(AbstractReaderWriter):

    @staticmethod
    def read(path):
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    def write(data, path):
        with open(path, 'w') as file:
            json.dump(data, file)


class PickleReaderWriter(AbstractReaderWriter):

    @staticmethod
    def read(path):
        with open(path, 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def write(data, path):
        with open(path, 'wb') as file:
            pickle.dump(data, file)
