"""
    clear
    copy
    fromkeys
    get
    items
    keys
    pop - removes couple, and returns value by key. Exception if no key. Default value could be set
    popitem - removes and returns key-value pair. Before 3.7 - random, 3.7+ - last
    setdefault
    update
    values
"""

# # clear
# d = {1: 1, 2: 2, 3: 3}
# d.clear()
# print(d)


# # copy
# d = {1: 1,
#      2: [2]}
# d2 = d.copy()
# d[1] = 22222
# d[2].append(111)
# print(d)
# print(d2)


# # from_keys
# d = {6: 4}.fromkeys([1, 2, 3, 4], 5)
# print(d)
#
# d = {}.fromkeys([1, 2, 3, 4])
# print(d)  # {1: None, 2: None, 3: None, 4: None}
# memory = [None] * 1024
# print(memory)

# # get
# d = {1: 1, 2: 2}
# value_key_1 = d.get(1, 'Default')
# print(value_key_1)
# value_key_10 = d.get(10, 'Default')
# print(value_key_10)
# value_key_10 = d.get(10)
# print(value_key_10)


# # keys, values, items
# d = {1: 10, 2: 20, 3: 30}
# print(d.keys())
# print(d.values())
# print(d.items())
# # print(d.keys()[0])
# for k, v in d.items():
#     print(f"d[{k}] = {v}")


# # pop
# d = {1: 10, 2: 20, 3: 30}
# value = d.pop(1, 'Default')
# print(value)  # 10
# print(d)  # {2: 20, 3: 30}

# d = {1: 10, 2: 20, 3: 30}
# value = d.pop(10, 'Default')
# print(value)
# print(d)  # {1: 10, 2: 20, 3: 30}
#
# d = {1: 10, 2: 20, 3: 30}
# value = d.pop(10)  # error


# popitem
# d = {1: 10, 2: 20, 3: 30}
# pair = d.popitem()
# print(pair)
# print(d)

# d = {}
# pair = d.popitem()


# # setdefault
# d = {1: 10, 2: 20, 3: 30}
# value = d.setdefault(1, 1111)
# print(value)
# print(d)
# value = d.setdefault(9, 999)
# print(value)
# print(d)


# # update
# d1 = {1: 10, 2: 20, 3: 30}
# d2 = {3: 'c', 4: 'b'}
# result = d1.update(d2)
# print(d1)
# print(result)


# d1 = {1: 10, 2: 20, 3: 30}
# d2 = {3: 'c', 4: 'b'}
# d3 = {**d1, **d2}
# print(d1)
# print(d2)
# print(d3)


d1 = {1: 10, 2: 20, 3: 30}
d2 = {3: 'c', 4: 'b'}
d1 |= d2
print(d1)
print(d2)
