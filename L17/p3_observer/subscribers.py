from abc import ABC, abstractmethod

class AbstractSubscriber(ABC):

    @abstractmethod
    def update(self, temperature):
        pass


class MobileClient(AbstractSubscriber):

    def update(self, temperature):
        print(f"SHOW TEMP ON MOBILE: {temperature}")


class WebClient(AbstractSubscriber):

    def update(self, temperature):
        print(f"SHOW TEMP ON WEB: {temperature}")
