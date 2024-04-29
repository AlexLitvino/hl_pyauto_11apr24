"""
    append
    clear
    copy
    count
    extend
    index
    insert
    pop
    remove
    reverse
    sort
"""
# # append
# lst = [1, 2, 3, 4, 5]
# lst.append(6)
# print(lst)


# # clear
# lst = [1, 2, 3, 4, 5]
# lst.clear()
# print(lst)


# # copy
# lst1 = [1, 2, 3, 4, 5]
# lst2 = lst1.copy()
# lst1[0] = 111
# print(lst1)
# print(lst2)

# lst1 = [[1], 2, 3, 4, 5]
# lst2 = lst1.copy()
# lst1[0].append(222)
# lst1.append(666)
# print(lst1)
# print(lst2)
# print(lst1[0] is lst2[0])

# # count
# lst = [1, 2, 3, 3, 4, 3]
# print(lst.count(3))
# print(lst.count(5))


# # extend
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# lst1.extend(lst2)
# print(lst1)
# lst1.extend("abcde")
# print(lst1)


# # index
# lst = [1, 2, 3, 3, 4, 3, 5, 6]
# print(lst.index(3))
# print(lst.index(3, 4, 6))
# print(lst.index(999))


# # insert
# lst = [1, 2, 3]
# lst.insert(0, 'INSERTED')
# print(lst)  # ['INSERTED', 1, 2, 3]
# lst.insert(-1, 'INSERTED2')
# print(lst)


# # pop
# lst = [1, 2, 3, 4, 5]
# item = lst.pop()
# print(item)
# print(lst)
# item = lst.pop(0)
# print(item)
# print(lst)


# # remove
# lst = [1, 2, 3, 4, 5, 3]
# lst.remove(3)
# print(lst)
# # lst.remove(17)


# # reverse
# lst = [1, 2, 3, 4, 5]
# lst.reverse()
# print(lst)

# lst = [3, 2, 4, 5, 1]
# lst.sort()
# print(lst)

# lst = [3, 2, 4, 5, 1]
# lst.sort(reverse=True)
# print(lst)

lst = ['f', 'a', 'b', 'e', 'aa', 'ab']
lst.sort()
print(lst)
"""
a
ab
"""
print('ab' < 'b')
