# __add__, __radd__, __iadd__, __del__, __sub__, __mlp__, __truediv__, __and__, __or__

class Donkey:
    def __init__(self, name):
        self.name = name
        self.speed = 1
        self.strength = 4


class Horse:
    def __init__(self, name):
        self.name = name
        self.speed = 5
        self.strength = 2

    def __str__(self):
        return f"{self.__class__.__name__:} speed: {self.speed} strength: {self.strength}"

    def __add__(self, other):
        return Mule(self.speed, other.strength)

    def __radd__(self, other):
        return Mule(self.speed, other.strength)

    def __iadd__(self, other):
        self.strength += other.strength
        return self

    def __del__(self):
        print("Horse killed")
        del self

class Mule:
    def __init__(self, speed, strength):
        self.speed = speed
        self.strength = strength

    def __str__(self):
        return f"{self.__class__.__name__:} speed: {self.speed} strength: {self.strength}"


horse = Horse("First")
donkey = Donkey("Second")
print(horse + donkey)
print(donkey + horse)
horse += donkey
print(horse)
del horse