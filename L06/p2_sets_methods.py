# Set methods
"""
add
clear
copy
pop - removes and returns "random" element
remove - removes element, raises exception if element is missing
discard - removes element, do nothing if element is missing

# methods with update, applies operation to left operand
# methods with update, return new set
union (s3 = s1 | s2)
update

difference (s3 = s1 - s2)
difference_update

intersection (s3 = s1 & s2)
intersection_update

symmetric_difference (s3 = s1 ^ s2)
symmetric_difference_update

isdisjoint (no common elements, "sets are independent")
issubset  (<=)
issuperset (>=)

"""
# # add
# s1 = {2, 3, 5}
# s1.add(56)
# print(s1)  # {56, 2, 3, 5}


# # clear
# s1 = {2, 3, 5}
# s1.clear()
# print(s1)  # set()
# print(type({}))

# # copy
# s1 = {2, 3, 5}
# s2 = s1.copy()
# s1.add(34)
# print(s1)  # {2, 3, 34, 5}
# print(s2)  # {2, 3, 5}


# # pop
# s1 = {4, 2, 3, 5}
# item = s1.pop()
# print(item)
# s2 = set()
# s2.pop()  # KeyError: 'pop from an empty set'


# # remove
# s1 = {2, 3, 5}
# s1.remove(5)
# print(s1)
# # s1.remove(5)  # KeyError: 5


# # discard
# s1 = {2, 3, 5}
# s1.discard(5)
# print(s1)  # {2, 3}
# s1.discard(5)
# print(s1)  # {2, 3}, no error


# # # union (|)
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# #s3 = s1.union(s2)
# s3 = s1 | s2
# print(s1)  # {1, 2, 3, 4, 5}
# print(s2)  # {4, 5, 6, 7, 8}
# print(s3)  # {1, 2, 3, 4, 5, 6, 7, 8}


# # update
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# result = s1.update(s2)
# print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8}
# print(s2)  # {4, 5, 6, 7, 8}
# print(result)  # None


# # difference (-)
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# s3 = s1.difference(s2)
# #s3 = s1 - s2
# print(s1)  # {1, 2, 3, 4, 5}
# print(s2)  # {4, 5, 6, 7, 8}
# print(s3)  # {1, 2, 3}


# # intersection
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# s3 = s1.intersection(s2)
# print(s1)  # {1, 2, 3, 4, 5}
# print(s2)  # {4, 5, 6, 7, 8}
# print(s3)  # {4, 5}


# # symmetric_difference (^)
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# s3 = s1.symmetric_difference(s2)
# # s3 = s1 ^ s2
# print(s1)  # {1, 2, 3, 4, 5}
# print(s2)  # {4, 5, 6, 7, 8}
# print(s3)  # {1, 2, 3, 6, 7, 8}
# # TODO: Task: how to get symmetric_difference with methods above (| union, - difference, & intersection)?
# s4 = (s1 | s2) - (s1 & s2)
# print(s4)


# # isdisjoint
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# result = s1.isdisjoint(s2)
# print(result)  # False
# s1 = {1, 2, 3}
# s2 = {4, 5, 6}
# result = s1.isdisjoint(s2)
# print(result)  # True


# # issubset (<=)/superset (>=)
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4}
s3 = {1, 2, 3}
# print(s1 < s2)  # True
# print(s1 <= s2)  # True
# print(s1 < s3)  # False
# print(s1 <= s3)  # True
print(s1.issubset(s2))  # True
print(s1.issubset(s3))  # True
print(s1.issuperset(s2))  # False
print(s1.issuperset(s3))  # True
