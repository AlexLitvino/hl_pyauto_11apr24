from abc import ABC, abstractmethod


# Interfaces implementation
class Movable(ABC):

    @abstractmethod
    def move(self, x, y):
        raise NotImplementedError


class Car(Movable):

    def __init__(self, model, tank_volume):
        self.model = model
        self.tank_volume = tank_volume

    def move(self, x, y):
        print(f"Moving by road to ({x}, {y})")


class Plane(Movable):

    def __init__(self, number_of_passengers):
        self.number_of_passengers = number_of_passengers

    def move(self, x, y):
        print(f"Moving by air to ({x}, {y})")


car = Car('Jeep', 120)
car.move(10, 45)
plane = Plane(60)
plane.move(40, 10)