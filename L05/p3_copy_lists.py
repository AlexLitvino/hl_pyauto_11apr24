# # sharing link
# lst_init = [1, 2, 3, 4, 5]
# lst_copy = lst_init
#
# print(lst_init)
# print(lst_copy)
# lst_init[0] = 111
# print(lst_init)
# print(lst_copy)


# # using copy method
# lst_init = [1, 2, 3, 4, 5]
# lst_copy = lst_init.copy()
#
# print(lst_init)
# print(lst_copy)
# lst_init[0] = 111
# print(lst_init)
# print(lst_copy)


# # using slice
# lst_init = [1, 2, 3, 4, 5]
# lst_copy = lst_init[:]
#
# print(lst_init)
# print(lst_copy)
# lst_init[0] = 111
# print(lst_init)
# print(lst_copy)


# # copying lists with nested elements
# nested_lst = ['1 level', 1,
#               ['2 level', 2],
#               [2, ['3 level', 3]]]
#
# nested_copy = nested_lst.copy()
# # nested_copy = nested_lst[:]
# nested_lst[0] = '111 level'
# nested_lst[2][0] = '222 level'
# nested_lst[3][1][0] = '333 level'
# print(nested_lst)
# print(nested_copy)

import copy
nested_lst = ['1 level', 1,
              ['2 level', 2],
              [2, ['3 level', 3]]]

# nested_copy = copy.copy(nested_lst)
nested_copy = copy.deepcopy(nested_lst)

nested_lst[0] = '111 level'
nested_lst[2][0] = '222 level'
nested_lst[3][1][0] = '333 level'
print(nested_lst)
print(nested_copy)
