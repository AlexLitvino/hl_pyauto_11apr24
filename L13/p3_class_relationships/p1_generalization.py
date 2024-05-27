from abc import ABC, abstractmethod

# Generalization with specific classes
class User:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def print_info(self):
        print(f"User:\n\tname: {self.name}\n\tbirth year: {self.birthyear}")

    @staticmethod
    def is_leap(year):
        return year % 4 == 0  # it is not correct implementation, just for reference


class Employee(User):

    def __init__(self, name, birthyear, occupation, salary):
        super().__init__(name, birthyear)
        self._occupation = occupation
        self.__salary = salary

    def do_work(self):
        print("Working...")

    def increase_salary(self, amount):
        self.__salary += amount


employee = Employee('John', 33, 'Tester', 2000)
employee.print_info()
employee.do_work()


# Generalization with abstract classes
class AbstractShape(ABC):

    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)

    @abstractmethod
    def calculate_area(self):
        raise NotImplementedError


class Square(AbstractShape):

    def calculate_area(self):
        return self.sides[0] * self.sides[0]


square = Square(sides=[2, 2, 2, 2])
perimeter = square.calculate_perimeter()
square = square.calculate_area()
print(perimeter)
print(square)
