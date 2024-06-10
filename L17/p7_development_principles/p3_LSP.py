# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def increase_salary(self, percent):
#         self.salary += self.salary * percent
#
#     def work_hard(self):
#         print("Tyap-lyap and to production")
#
#
# class Manager(Employee):
#
#     MANAGER_PERCENT_BONUS = 0.05
#
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#
#     def increase_salary(self, percent, bonus):
#         super().increase_salary(percent + Manager.MANAGER_PERCENT_BONUS)
#         self.salary += bonus
#
#     def work_hard(self):
#         raise TypeError('Maybe later')
#
#     def manage(self):
#         print("Managing staff...")
#
#
# john = Employee('John', 2000)
# anna = Employee('Anna', 2500)
# james = Manager('James', 4000)
# employees = [john, anna, james]
#
# # for employee in employees:
# #     employee.increase_salary(0.2)
#
# for employee in employees:
#     employee.work_hard()

# ######################################################################################################################

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * percent


class NonManagerEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work_hard(self):
        print("Tyap-lyap and to production")


class Manager(Employee):

    MANAGER_PERCENT_BONUS = 0.05

    def __init__(self, name, salary):
        super().__init__(name, salary)

    def increase_salary(self, percent):
        super().increase_salary(percent + Manager.MANAGER_PERCENT_BONUS)

    def add_annual_bonus(self, bonus):
        self.salary += bonus

    def manage(self):
        print("Managing staff...")


john = NonManagerEmployee('John', 2000)
anna = NonManagerEmployee('Anna', 2500)
james = Manager('James', 4000)
non_manager_employees = [john, anna]
managers = [james]
employees = non_manager_employees + managers

for employee in employees:
    employee.increase_salary(0.2)
for manager in managers:
    manager.add_annual_bonus(500)

for employee in non_manager_employees:
    employee.work_hard()