# import sys
#
# lst = [i * i for i in range(1000) if i % 2 == 0]
# #print(lst)
# print(sys.getsizeof(lst))
#
# gen = (i * i for i in range(10) if i % 2 == 0)
# print(gen)
# # print(sys.getsizeof(gen))
#
# for i in gen:
#     print(i)
# print("=====")
# for i in gen:
#     print(i)

def gen_sqr(n, message):
    for i in range(n):
        if i % 2 == 0:
            yield i * i, message
        if i == 5:
            return "STOPPED"

# g = gen_sqr()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# g = gen_sqr()
# print(g is iter(g))
# print(gen_sqr())
# for i in gen_sqr():
#     print(i)
#
# for i in gen_sqr():
#     print(i)


# g1 = gen_sqr(10, "A")
# g2 = gen_sqr(10, "B")
#
# for i, m in g1:
#     print(f"{i} - {m}")
# for i, m in g2:
#     print(f"{i} - {m}")

# from collections import ChainMap
# from itertools import chain
#
# g1 = gen_sqr(10, "A")
# g2 = gen_sqr(10, "B")
#
# for i, m in chain(g1, g2):
#     print(f"{i} - {m}")


gen = (i * i for i in range(10) if i % 2 == 0)
#print(list(gen))
print(16 in gen)  # True
print(16 in gen)  # False

# lst = [0, 4, 16, 36, 64]
# print(16 in lst)
