"""
For (3 types), nested lists, break, continue, else
"""

# for i in range(10):
#     print(i)

# lst = [1, 3, 4]
# for i in lst:
#     print(i)

# struct = [1, 2, 'aaa', [1, 3], {'a': 3, 'b': [1, 2, 'qwerty']}]
# print(struct[4]['b'][2])

lst = [
    [1, 2, 'SKIP', 3, 4],
    [111, 222, 'SKIP', 333, 444]
]

# for outter in lst:
#
#     for inner in outter:
#         if inner == 'SKIP':
#             continue
#
#         if inner == 3:
#             break
#         print(inner)

# for outter in lst:
#
#     for inner in outter:
#         if inner != 'SKIP':
#             if inner == 3:
#                 break
#             print(inner)


# for outter in lst:
#
#     for inner in outter:
#         if inner == 'SKIP':
#             pass
#         else:
#             if inner == 3:
#                 break
#             print(inner)



# status_code = 404
# if not status_code == 404:
#     print("Process page")
#
# if status_code == 404:
#     pass
# else:
#     print("Process page")

# lst = [1, 2, 3]
# for i in lst:
#     print(i + len(lst))

# lst = [1, 2, 3]
# lst_length = len(lst)
# for i in lst:
#     print(i + lst_length)