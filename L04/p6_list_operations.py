"""
List type characteristics
List creation
Operation with lists
    Length, getting element, slices, in-operation
    Iterating over list (for-each, for-index, for-enumerate)
    Lists concatenation
    Lists duplication
    Lists comparison
Packing/Unpacking
Built in functions: min, max, sum, sorted, reversed
Deleting objects and lists elements
"""

# lst1 = [1, 2]
# lst2 = list('abc')
# print(lst2)
# lst3 = list({'a': 1, 'b': 2})
# print(lst3)
# print(len(lst1))
# lst = ['a', 'b', 'c', 'd']
# print(lst[-1])
# print(lst[1:3])  # [b c]

# lst = ['a', 'b', 'c', 'd']
# print('a' in lst)
# lst1 = [1, 2]
# lst2 = [3, 4]
# lst3 = lst1 + lst2
# print(lst3)

lst = ['a', 'b', 'c', 'd']

# for element in lst:
#     print(element)

# for index in range(len(lst)):
#     print(lst[index])

# print(list(enumerate(lst, start=1)))
#
# for index, value in enumerate(lst, start=1):
#     print(f"Line {index} is '{value}'")

# lst1 = ['a', 'b', 3]
# lst2 = ['a', 'b', 4]
# print(lst2 > lst1)

# lst1 = ['a', 'b', '3']
# lst2 = ['a', 'b', 4]
# print(lst2 > lst1)

# lst = [1, 2]
# lst_d = lst * 2
# print(lst_d)
# lst[0] = 111
# print(lst)
# print(lst_d)

# lst = [1, [2, 3]]
# lst_d = lst * 2
# print(lst_d)
# print(lst_d[1] is lst_d[3])
# # lst[1] = 111
# # print(lst)
# lst_d[1][0] = 222
# print(lst_d)

# a = 3
# print(a)
# del a
# print(a)

lst = ['a', 'b', 'c', 'd']
print(lst)
del lst[0]
print(lst)
lst.append('QQQ')
print(lst)
