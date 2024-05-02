"""
Creation({}, dict, comprehension)
Requirement to keys
Operations:
    len
    in
    Getting existing/non-existing key
    adding new element
    updating existing element
    Iterating over keys, values
"""

d1 = {1: 'a', 2: 'b', 3: 'c', (1, 2): 'd'}
print(d1)
d2 = dict([(1, 'a'), (2, 'b')])
print(d2)
d3 = {i: chr(i) for i in range(67, 80)}
print(d3)

# print(len(d3))
# print(d3[67])
# if 100 in d3:
#     print(d3[100])
# else:
#     print("No such key")
#
# d3[100] = "QQQ"
# print(d3)
# d3[100] = "WWW"
# print(d3)

# for key in d3:
#     print(key)

# for key in d3:
#     print(d3[key])

# print(d3.keys()[0]) # error

# for key in d3.keys():
#     print(key)

# for value in d3.values():
#     print(value)

for key, value in d3.items():
    print(f"{key} -> {value}")

del d3[67]

print(d3)
