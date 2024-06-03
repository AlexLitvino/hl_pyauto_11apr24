# Descriptor in general

# class Descriptor:
#
#     def __get__(self, instance, owner):
#         pass
#
#     def __set__(self, instance, value):
#         pass
#
#     def __delete__(self, instance):
#         pass

# ######################################################################################################################
# Descriptor arguments

# obj.attr
# obj.attr = value

class Descriptor:

    def __get__(self, instance, owner):
        print("In get")
        print(f"{self}\n{instance}\n{owner}")
        print()
        return "VALUE_FROM_DESCRIPTOR"

    def __set__(self, instance, value):
        print("In set")
        print(f"{self}\n{instance}\n{value}")
        print()

    def __delete__(self, instance):
        print("In delete")
        print(f"{self}\n{instance}")
        print()


# class A:
#
#     attr = Descriptor()
#
# a = A()
# #print(a.attr)
# # print(A.attr)
# a.attr = 222
# del a.attr

# ######################################################################################################################
# Read only descriptor
# class A:
#
#     @property
#     def age(self):
#         return 23
# class Readonly:
#
#     def __init__(self, default_value):
#         self._value = default_value
#
#     def __get__(self, instance, owner):
#         return self._value
#
#     def __set__(self, instance, value):
#         raise AttributeError("Attr can't be set")
#
#
# class User:
#
#     company = Readonly('Edgio')
#
# user = User()
# print(user.company)
# print(user.__dict__)
# user.company = 'GlobalLogic'
# print(user.company)
# print(user.__dict__)

# ######################################################################################################################
# Age and UnifiedString descriptors

import datetime
class Age:

    def __get__(self, instance, owner):
        return datetime.datetime.now().year - instance.birth_year

    def __set__(self, instance, value):
        raise AttributeError("Age couldn't be changed")


class User:

    age = Age()

    def __init__(self, name, birth_year, occupation):
        self.name = name
        self.__birth_year = birth_year
        self.occupation = occupation

    @property
    def birth_year(self):
        return self.__birth_year


class Employee(User):
    pass


john = User("John", 1976, "TESter")
print(john.occupation)
print(john.age)
anna = Employee("Anna", 1990, "DEVeloper")
print(anna.age)
print(anna.occupation)
print(john.occupation)
