# Decorating function with class
# class CallCounter:
#
#     def __init__(self, func):
#         self.func = func
#         self.calls = 0
#
#     def __call__(self, *args, **kwargs):
#         self.calls += 1
#         print(f"{self.func.__name__} called {self.calls} times")
#         return self.func(*args, **kwargs)
#
#
# def add(a, b):
#     return a + b
#
# add = CallCounter(add)
#
#
# @CallCounter
# def mlp(a, b):
#     return a * b
#
# print(type(add))
# print(type(mlp))
# #print(add.__name__)
# #print(mlp.__name__)
#
# print(add(4, 6))
# print(mlp(4, 1))
# print(add(4, 36))
# print(add(6, 3))
# print(mlp(2, 7))

# ######################################################################################################################
# # Impossible to decorate methods using classes
# class User:
#
#     def __init__(self, name):
#         self.name = name
#
#     @CallCounter
#     def print_name(self):
#         print(self.name)
#
# olga = User("Olga")
# olga.print_name()

# ######################################################################################################################
# Decorating methods with functions

# # Not instance independent
# def call_counter(func):
#
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         print(f"{func.__name__} called {wrapper.calls} times")
#         return func(*args, **kwargs)
#     wrapper.calls = 0
#     return wrapper
#
# # # Instance independent
#
#
# class User:
#
#     def __init__(self, name):
#         self.name = name
#
#     @call_counter
#     def print_name(self):
#         print(self.name)
#
# olga = User("Olga")
# john = User("John")
# olga.print_name()
# john.print_name()
# olga.print_name()

# ######################################################################################################################
# Passing parameters to class based constructor and using for methods
import functools

class CallCounter:

    def __init__(self, decorator_arg):
        self.decorator_arg = decorator_arg
        self.calls = 0

    def __call__(self, func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(self.decorator_arg)
            self.calls += 1
            print(f"{func.__name__} called {self.calls} times")
            return func(*args, **kwargs)

        return wrapper


# @CallCounter("ADD FUNC")
# def add(a, b):
#     return a + b
#
#
# @CallCounter("MLP FUNC")
# def mlp(a, b):
#     return a * b
#
# print(type(add))
# print(type(mlp))
# print(add.__name__)
# print(mlp.__name__)
#
# print(add(4, 6))
# print(mlp(4, 1))
# print(add(4, 36))
# print(add(6, 3))
# print(mlp(2, 7))
#
#
class User:

    def __init__(self, name):
        self.name = name

    @CallCounter('Method')
    def print_name(self):
        print(self.name)

john = User('John')
olga = User("Olga")
john.print_name()
olga.print_name()
john.print_name()
