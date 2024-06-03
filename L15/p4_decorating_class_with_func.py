# decorating and returning the same object
# def decorator(class_):
#     class_.default = "DEFAULT"
#
#     def add(self, a, b):
#         return a + b
#
#     class_.add = add
#
#     return class_
#
# #User = decorator(User)
#
# @decorator
# class User:
#
#     def __init__(self, name):
#         self.name = name
#
#     def print_name(self):
#         print(f"I'm {self.name}")
#
# john = User('John')
# print(User)
# print(User.default)
# print(john.add(5, 3))

# ######################################################################################################################
# decorating but returning wrapper
def decorator(class_):

    class Wrapper:

        def __init__(self, *args, **kwargs):
            self.instance = class_(*args, **kwargs)

        def add(self, a, b):
            return a + b

        def __getattr__(self, item):
            return self.instance.__getattribute__(item)

    return Wrapper


#User = decorator(User)

@decorator
class User:

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"I'm {self.name}")


john = User('John')
print(john.__class__.__name__)
print(john.add(5, 3))
john.print_name()
