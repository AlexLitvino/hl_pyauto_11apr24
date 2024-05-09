# Principles decorators are build on

# Passing function as argument

# def print_list(lst, print_function):
#     print(f"Printing lists using {print_function.__name__}")
#     print_function(lst)
#     print("Printing is performed successfully")
#
#
# def print_to_console(lst):
#     for item in lst:
#         print(item)
#
# def print_with_index(lst):
#     for index, item in enumerate(lst, start=1):
#         print(f"{index}\t{item}")
#
# lst = [1, 2, 3, 4, 5]
# print_list(lst, print_to_console)
# print_list(lst, print_with_index)


# # Returning function as result from another function
# def add(x, y):
#     return x + y
#
#
# def mlp(x, y):
#     return x * y
#
#
# def dispatcher(function_name):
#     print("Selecting operation to perform...")
#     if function_name == 'add':
#         return add
#     elif function_name == 'mlp':
#         return mlp
#     else:
#         raise RuntimeError('Not supported operation')
#
#
# print(dispatcher('add')(3, 5))
# print(dispatcher('mlp')(2, 6))
# print(dispatcher('sub')(7, 2))


# # Re-assigning variables
# def add(x, y):
#     return x + y
#
# sum_ = add
# add = None
# print(sum_(3, 7))

import functools

def greetings(name):
    """Generates greetings"""
    return f"Hello, {name}"


def italic_decorator(func):

    @functools.wraps(func)
    def wrapper(name):
        return f"<i>{func(name)}</i>"

    return wrapper


greetings = italic_decorator(greetings)
print(greetings("Anna"))
print(greetings.__name__)
print(greetings.__doc__)

# ######################################################################################################################

# def italic_decorator(func):
#
#     def wrapper(name):
#         return f"<i>{func(name)}</i>"
#
#     return wrapper
#
#
# def bold_decorator(func):
#
#     def wrapper(name):
#         return f"<b>{func(name)}</b>"
#
#     return wrapper
#
#
# @bold_decorator
# @italic_decorator
# def greetings(name):
#     return f"Hello, {name}"
#
# #greetings = bold_decorator(italic_decorator(greetings))
#
# print(greetings("Anna"))

# ######################################################################################################################

# def style(tag):
#
#     def decorator(func):
#
#         def wrapper(*args, **kwargs):
#             return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
#
#         return wrapper
#
#     return decorator
#
#
# @style('i')
# @style('b')
# def greetings(name, cat):
#     return f"Hello, {name} and {cat}"
#
# print(greetings("Anna", "Murzik"))