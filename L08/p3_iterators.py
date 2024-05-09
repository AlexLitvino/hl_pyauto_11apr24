# lst = [1, 2, 3]
# for i in lst:
#     print(i)
#
# print()
#
# for i in lst:
#     print(i)

# with open('file_for_iterators.txt') as f:
#     for line in f:
#         print(line)
#         #f.__iter__()
#
#     print("Separator")
#
#     for line in f:
#         print(line)
#

# lst = [1, 2, 3]
# lst_iterator = iter(lst)
# print(lst is lst_iterator)
#
# print(next(lst_iterator))
# print(next(lst_iterator))
# print(next(lst_iterator))
# # print(next(lst_iterator))


with open('file_for_iterators.txt') as f:
    file_iterator = iter(f)
    print(f is file_iterator)
    print(next(file_iterator))
    print(next(file_iterator))
    print(next(file_iterator))
    #print(next(file_iterator))