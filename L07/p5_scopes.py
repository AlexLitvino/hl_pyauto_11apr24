# LEGB (LNGB)

# Local scope

# # Case 1
# def func():
#     x = 5
#     print(x)
#
# func()  # x = 5
# print(x)  # error


# # Case 2
# x = 1
# def func():
#     x = 5
#     print(x)
#
# func()  # x = 5
# print(x)  # x = 1


# # Global scope
# # Case 3
# x = 23
# def func():
#     print(x)
#
# func()  # 23
# print(x)  # 23


# # # Case 4
# x = 23
# def func():
#     print(x)
#     x = 64
#
# #func()  # error
# print(x)  # 23


# # Case 5
# x = 23
# def func():
#     global x
#     print(x)
#     x = 64  # assigning to global
#
# func()  # 23
# print(x)  # 64
# ######################################################################################################################

# # # Non-local scope
# # Case 6
# def outer_func():
#     x = 2
#     print(f"In outer: {x}")  # 2
#
#     def inner_func():
#         x = 5
#         print(f"In inner: {x}")  # 5
#
#     inner_func()
#     print(f"At the end of outer: {x}")  # 2
#
# outer_func()
# # # In outer: 2
# # # In inner: 5
# # # At the end of outer: 2


# # Case 7
# def outer_func():
#     x = 2
#     print(f"In outer: {x}")  # 2
#
#     def inner_func():
#         nonlocal x
#         x = 5
#         print(f"In inner: {x}")  # 5
#
#     inner_func()
#     print(f"At the end of outer: {x}")  # 5
#
# outer_func()
# # In outer: 2
# # In inner: 5
# # At the end of outer: 5


# # # Case 8
# x = 10
# def outer_func():
#     x = 2
#     print(f"In outer: {x}")  # 2
#
#     def inner_func():
#         global x
#         x = 5
#         print(f"In inner: {x}")  # 5
#
#     inner_func()
#     print(f"At the end of outer: {x}")  # 2
#
# outer_func()
# print(f"Global {x}")  # 5
# # In outer: 2
# # In inner: 5
# # At the end of outer: 2
# # Global 5
# ######################################################################################################################

# Built-in scope
def func_with_builtin(lst):
    #len = lambda x: x * 2
    def len(lst):
        return lst * 2
    print(len(lst))  # re-defined function len is used


lst = [1, 3]
func_with_builtin(lst)  # [1, 3, 1, 3]
print(len(lst))  # 2; built-in function len is used
