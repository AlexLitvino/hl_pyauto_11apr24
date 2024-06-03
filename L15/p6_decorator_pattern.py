from abc import ABC, abstractmethod
import random


# class DataProvider:
#
#     def __init__(self, max_number):
#         self.max_number = max_number
#
#     def get_data(self):
#         return str(random.randint(1, self.max_number))
#
#
# class AbstractDecorator(ABC):
#     def __init__(self, wrappee):
#         self.wrappee = wrappee
#
#     @abstractmethod
#     def get_data(self):
#         pass
#
#
# class CorruptionDecorator(AbstractDecorator):
#
#     def get_data(self):
#         return f"\0\0{self.wrappee.get_data()}"
#
#
# class DoubleDecorator(AbstractDecorator):
#
#     def get_data(self):
#         data = self.wrappee.get_data()
#         return f"{data}{data}"
#
#
# data_provider = DataProvider(10)
# print(data_provider.get_data())
# corrupted_data_provider = CorruptionDecorator(data_provider)
# print(repr(corrupted_data_provider.get_data()))
#
# doubled_data_provider = DoubleDecorator(data_provider)
# print(doubled_data_provider.get_data())

# ######################################################################################################################

class ProviderInterface(ABC):

    @abstractmethod
    def get_data(self):
        raise NotImplementedError


class DataProvider(ProviderInterface):

    def __init__(self, max_number):
        self.max_number = max_number

    def get_data(self):
        return str(random.randint(1, self.max_number))


class AbstractDecorator(ProviderInterface):
    def __init__(self, wrappee):
        self.wrappee = wrappee

    @abstractmethod
    def get_data(self):
        pass


class CorruptionDecorator(AbstractDecorator):

    def get_data(self):
        return f"\0\0{self.wrappee.get_data()}"


class DoubleDecorator(AbstractDecorator):

    def get_data(self):
        data = self.wrappee.get_data()
        return f"{data}{data}"


data_provider = DataProvider(10)
print(data_provider.get_data())
corrupted_data_provider = CorruptionDecorator(data_provider)
print(repr(corrupted_data_provider.get_data()))

doubled_data_provider = DoubleDecorator(data_provider)
print(doubled_data_provider.get_data())
