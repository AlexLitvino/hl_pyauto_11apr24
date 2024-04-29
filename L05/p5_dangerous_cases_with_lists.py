# # # Case 1
# lst = ['qwerttyy\n', '123454\n', 'zxcv']
#
# for line in lst:
#     if line.endswith('\n'):
#         line = line[: -1]
#
# print(lst)
#
#
#
#
# # ['qwerttyy\n', '123454\n']
#
# # # Solution
#
# updated_lst = [line[:-1] if line.endswith('\n') else line for line in lst]
# updated_lst = [line.strip() for line in lst]
# print(updated_lst)









# # Case2
# lst = list(range(10))
# print(lst)
# # for i in lst:
# #     print(i)
# #     if i % 2 == 0:
# #         lst.append(i)
# # print(lst)
#
# # [0, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 4, 6, 8]
#
# # Solution
# lst = lst + [i for i in lst if i % 2 == 0]
# result = lst.extend([i for i in lst if i % 2 == 0])
# print(result)
# #"aaa".replace('a', 'b')
# print(lst)



# Case 3
lst = [6, 4, 5, 3, 6, 6, 6, 7]
# for index, item in enumerate(lst):
#     print(index, item)
#     if item == 6:
#         del lst[index]
# print(lst)
# [4, 5, 3, 7]
# [4, 5, 3, 6, 7]

# lst = [6, 4, 5, 3, 6, 6, 6, 7]
# del lst[0]
# print(lst)


# # Solution1
# lst = [i for i in lst if i != 6]
# print(lst)

# # Solution 2
lst = [6, 4, 5, 3, 6, 6, 6, 7]
for index in range(len(lst)-1, -1, -1):
    if lst[index] == 6:
        del lst[index]
print(lst)
