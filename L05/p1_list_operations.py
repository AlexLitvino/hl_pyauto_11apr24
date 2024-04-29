"""
Packing/Unpacking
Built-in functions: min, max, sum, sorted, reversed
"""

# coordinates = [1, 3, 4]
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# print(f"x={x}, y={y}, z={z}")


# lst = ['a', 'b', 'c', 'd']
# for index, value in enumerate(lst, start=1):
#     print(f"Line {index} is '{value}'")

# coordinates = [1, 3, 4]
# x, y, z = coordinates
# print(f"x={x}, y={y}, z={z}")


# coordinates = [1, 3, 2, 5, 4]
# x, *middle, z = coordinates
# print(x)
# print(middle)
# print(z)

# coordinates = [1, 3, 2, 5, 4]
# x, *end = coordinates
# print(x)
# print(end)

# coordinates = [1, 3, 2, 5, 4]
# *begin, z = coordinates
# print(begin)
# print(z)

# coordinates = [1, 3, 2, 5, 4]
# x, *_, z = coordinates
# print(x)
# print(_)
# print(z)

# for _ in range(10):
#     print("QQQ")

# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# # lst3 = lst1 + lst2
#
# # lst1.extend(lst2)
# # print(lst1)
#
# lst3 = [*lst1, *lst2, 'END']
# print(lst3)

# lst = [1, 2, 4.6]
# s = sum(lst, start=10)
# print(s)

# lst = ['a', 'b']
# print(sum(lst))

# lst = [1, 2, 4.6, -1, 10]
# print(min(lst))
# print(max(lst))
# lst = ['f', 'a', 'b', 'e']
# print(min(lst))

# lst = [1, 2, 4.6, -1, 10]
# reversed_list = reversed(lst)
#
# for item in reversed_list:
#     print(item)
#
#
# #print(reversed_list[1])
# print(reversed_list)
# print(list(reversed_list))
# print(lst is reversed_list)


lst = [1, 2, 4.6, -1, 10]
sorted_list = sorted(lst, reverse=True)

# for item in sorted_list:
#     print(item)

print(sorted_list)
print(sorted_list is lst)
