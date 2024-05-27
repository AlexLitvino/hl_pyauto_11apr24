# from typing import Union
#
# # {1: "a"} + {2:  "b"} -> {1: "a", 2: "b"}
#
# def add(a: Union[int, float, str, dict], b: Union[int, float, str, dict]):
#     if isinstance(a, dict) and isinstance(b, dict):
#         # a.update(b)
#         # return a
#
#         # result = {}
#         # result.update(a)
#         # result.update(b)
#         # return result
#
#         return {**a, **b}
#     return a + b
#
# print(add(4, 6))
# print(add("ab", "cd"))
# a = {1: "a"}
# b = {2:  "b"}
# print(add(a, b))
# print(a)
# print(b)

class Employee:

    def __init__(self, name, salary, department=None, **kwargs):
        self.name = name
        self.salary = salary
        self.department = None
        print(type(kwargs))
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * percent

    @classmethod
    def create_employee(cls, name, salary, department):
        employee = cls(name, salary)
        employee.department = department
        return employee


class Manager(Employee):

    def increase_salary(self, percent, bonus=0):
        #self.salary += self.salary * percent + bonus
        super().increase_salary(percent)
        self.salary += bonus


# employee = Employee('John', 1000)
# # employee.increase_salary(0.2)
# # print(employee.salary)
#
# manager = Manager("Anna", 4000)
# # manager.increase_salary(0.2, 500)
# # print(manager.salary)
#
# employees = [employee, manager]
# for employee in employees:
#     employee.increase_salary(0.2)
#
# for employee in employees:
#     print(employee.salary)

employee = Employee('Andrew', 2300, 'Test', passport="qwerty123344")
print(employee.passport)






