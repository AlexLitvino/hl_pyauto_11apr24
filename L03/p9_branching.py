"""
Branching with ifs
Ternary operator
"""

# status_code = 404
#
# if status_code == 404:
#     print("Page not found")
#     print("Next")
# print("After if")


# status_code = 500
#
# if status_code == 404:
#     print("Page not found")
#     print("Next")
# elif status_code == 500:
#     print("Server error")
# print("After if")


# status_code = 404
#
# if status_code == 404:
#     print("Page not found")
#     print("Next")
# else:
#     print("Something else")
# print("After if")

# status_code = 404
#
# if status_code == 404:
#     print("Page not found")
#     print("Next")
# elif status_code == 500:
#     print("Server error")
# elif status_code == 201:
#     print("Created")
# else:
#     print("Something else")
# print("After if")

lst = [1, 2, 3]
lst = []
#lst = None
# if lst != []:
#     print("Processing")

if not lst and lst is not None:
    print("Processing")

a = 3
if a > 10:
    b = 34
else:
    b = 100

b = 34 if a > 10 else 100
