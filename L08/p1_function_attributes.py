"""
Docstrings
Built-in function attributes
Custom attributes
Built-in function hasattr
"""

import json


#

# # Docstrings and documentation generation
# def mlp(a, b):
#     """Returns product of two numbers"""
#     return a * b
#
#
# def add(a, b):
#     """
#     Returns product of two numbers
#     :param a:
#     :param b:
#     :return:
#     """
#     return a + b
#
#
def sub(a: float, b: float):
    """Returns difference of two numbers"""
    if not hasattr(sub, 'my_attr'):
        sub.my_attr = "MY ATTR"
    return a - b


# # Built-in function attributes
# print(sub)
# print(sub.__name__)
# print(sub.__doc__)
# print(sub.__annotations__)
# print(sub.__code__.co_filename)

print(sub.__dict__)
sub.author = "Oleksii"
print(sub.author)
print(sub.__dict__)

sub.calls = 0
print(hasattr(sub, 'my_attr'))
sub(1, 2)
sub.calls += 1
print(sub.calls)
print(sub.__dict__)
print(sub.my_attr)
sub.my_attr = "ANOTHER_ATYT"
print(sub.my_attr)
sub(1, 2)
print(sub.my_attr)
print(hasattr(sub, 'my_attr'))