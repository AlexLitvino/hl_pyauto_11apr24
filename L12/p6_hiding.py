"""
Default - no in Python
Public
Protected
Private
"""

class User:

    def __init__(self, name, age, salary=1000):
        self.name = name
        self.age = age
        self._salary = salary
        self.__heartbeat = 100

    def print_info(self):
        print(f"User: name {self.name}, age {self.age}")

    def _change_heartbeat(self, amount):
        self.__heartbeat += amount

    def show_heartbeat(self):
        print(self.__heartbeat)


class Employee(User):

    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        self.occupation = occupation

    def employee_info(self):
        print(f"Employee: name {self.name}, age {self.age}")

    def increase_salary(self, amount):
        self._salary += amount

    def drink_coffee(self):
        self._change_heartbeat(30)


john = Employee('John', 34, 'Tester')
print(john.name)
john.age += 10
print(john.age)
print(john._salary)
john._salary +=1000
print(john._salary)
print(john._User__heartbeat)
john.show_heartbeat()
john.drink_coffee()
john.show_heartbeat()