"""
Inheritance
Polymorphism
Encapsulation
Abstraction
Hiding


Inheritance (IS-A)
 A
B C

b = B()
print(b.attr)
"""
class Person:

    POPULATION = 0

    def __init__(self):
        print("In Person Constructor")
        Person.POPULATION += 1


class User(Person):

    COMPANY = 'Company ltd.'

    def __init__(self, name, age):
        print("In User Constructor")
        super().__init__()
        self.name = name
        self.age = age

    def print_info(self):
        print(f"User: name {self.name}, age {self.age}")


class Employee(User):

    def __init__(self, name, age, occupation):
        print("In Employee Constructor")
        super().__init__(name, age)
        self.occupation = occupation

    def employee_info(self):
        print(f"Employee: name {self.name}, age {self.age}")


john = Employee('John', 34, 'Tester')
# print(isinstance(john, Employee))
# print(isinstance(john, User))
# print(issubclass(Employee, User))
john.print_info()
Employee.employee_info(john)
# john.employee_info()
# print(john.POPULATION)