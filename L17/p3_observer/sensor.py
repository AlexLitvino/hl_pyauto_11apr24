import random


class Sensor:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, subscriber):
        subscriber.update(self.current_temperature)

    def notify_all(self):
        current_temperature = self.current_temperature
        for subscriber in self.subscribers:
            subscriber.update(current_temperature)

    @property
    def current_temperature(self):
        return 10 + 20 * random.random()

