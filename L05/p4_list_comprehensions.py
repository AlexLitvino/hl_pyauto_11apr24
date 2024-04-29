# lst = []
#
# for item in range(10):
#     if item % 2 == 0:
#         lst.append(item * item)
# print(lst)
#
# # [expression(item) for item in sequence if condition(item)]
# lst = [item * item for item in range(10) if item % 2 == 0]
# print(lst)
#
# lst = [x for x in range(10)]
# print(lst)

# s = 'fbvsw4w5y342t53gfebgfbhrt45rq423q'
# #print(list(s))
# lst = [int(x) for x in s if x.isdigit()]
# print(lst)
# print(sum(lst))

# import random
# lst = [random.random() for _ in range(10)]
# print(lst)

lst = []
for i in range(10):
    for j in range(10):
        if i % 2 == 0 and j % 2 == 1:
            lst.append(i * j)
print(lst)

#lst = [i * j for i in range(10) if i % 2 == 0 for j in range(10) if j % 2 == 1]
lst = [i * j for i in range(10) for j in range(10) if j % 2 == 1 and i % 2 == 0]
print(lst)
