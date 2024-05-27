import datetime

# class User:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def is_retired(self):
#         # True > 70, False otherwise
#         # if self.age > 70:
#         #     return True
#         # else:
#         #     return False
#         #return True if self.age > 70 else False
#         return self.age > 70
#
# john = User("John", 34)
# print(john.is_retired())


class User:

    def __init__(self, name, birth_year, salary):
        self.name = name
        self.birth_year = birth_year
        self._salary = salary

    def get_name(self):
        return self.name

    def set_name(self, value: str):
        self.name = value.capitalize()

    def get_age(self):
        return datetime.datetime.now().year - self.birth_year

    @property
    def age(self):
        return datetime.datetime.now().year - self.birth_year

    # @property
    # def salary(self):
    #     """Property for salary"""
    #     return self._salary
    #
    # @salary.setter
    # def salary(self, value):
    #     if value <= 0:
    #         raise ValueError("Salary should be greater than 0")
    #     self._salary = value
    #
    # @salary.deleter
    # def salary(self):
    #     print("In deleter")
    #     del self._salary


    def get_salary(self):
        """Property for salary"""
        return self._salary

    def set_salary(self, value):
        if value <= 0:
            raise ValueError("Salary should be greater than 0")
        self._salary = value

    def del_salary(self):
        print("In deleter")
        del self._salary

    salary = property(fget=get_salary, fset=set_salary, fdel=del_salary, doc="""Property for salary""")



john = User("John", 1987, 1000)
# #john.name = "JAmes"
# john.set_name("JAmes")
# print(john.name)
# print(john.get_age())
# print(john.age)

print(john.salary)
#john.salary = -1000
john.salary = 5000
print(john.salary)
#del john.salary
print(john.salary)
print(User.salary.__doc__)