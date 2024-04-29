"""
Tuple type characteristics
Tuple creation
Comparison size of list and tuple
Operation with tuples
    Length, getting element, slices, in-operation
    Iterating over tuple
    Tuples concatenation (different, with the same)
    Tuples duplication
    Tuples comparison
Tuples methods
    count(item)
    index(item, start, end)
Tuples could contain mutable types
Interesting case with adding elements to nested list
"""

# t1 = (1,
#       2,
#       3,
#       4,
#       )
#
# print(t1)
# print(len(t1))
# print(3 in t1)
# print(3333 in t1)
# print(t1[:2])  # (1, 2)
# t2 = (1,)
# print(t2)
# print(type(t2))
# t3 = 1, 2, 3
# print(t3)
#
# t1 = (1, 2)
# t2 = (3, 4)
# t3 = t1 + t2
# print(t3)
#
# t1 += t2  # t1 = t1 + t2
# print(t1)
#
# print(t1 *2)

# t1 = (1, 2, 3, 5, 1)
# print(t1.count(1))
# print(t1.index(1, 2))




t1 = (1, [2, 3])
print(t1)
t1[1].append(444)
print(t1)
# t2 = (1, 2)
# d = {t2: 1, t1: 3}
# print(d)


lst = [1, 2, 3, 4, 5, 6]
tup = (1, 2, 3, 4, 5, 6)
import sys
print(sys.getsizeof(lst))
print(sys.getsizeof(tup))

