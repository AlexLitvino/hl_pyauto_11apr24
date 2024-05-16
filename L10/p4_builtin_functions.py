# https://docs.python.org/3/library/functions.html

# # ######################################################################################################################

# # enumerate(iterable, start=0)


# # ######################################################################################################################

# # # map()
# res = map(int, [2.5, 4.6, 5.6])
# print(list(res))
# lst = [2.5, 4.6, 5.6]
# res = [int(i) for i in lst if i > 4]
# print(res)
#
# res = map(lambda x, y: x + y, "abc", "123456")
# #res = map(lambda x, y: x + y, ["a", "b", "c"], ["1", "2", "3", "4", "5", "6"])
# print(list(res))


# # ######################################################################################################################

#print(len("qqq") > 3)

# # # filter()
# res = filter(lambda x: len(x) > 3, ["aaa", 'b', "qqq"])
# if list(res):
#     print("Some files")

#print(list(res))


# # ######################################################################################################################
#
# # zip()
# names = ['Anna', 'John']
# salaries = [1000, 1500]
# age = [36, 45]
# res = zip(names, salaries)
# print(list(res))
# print(dict(res))

# # ######################################################################################################################
#
# # functools.reduce(function, sequence, initial=_initial_missing)
# for sum, max, combining list of lists
from functools import reduce
res = reduce(lambda x, y: x + y, [1, 3, 5, 7])
print(res)
# [1, 3, 5, 7])
# [4, 5, 7])
# [9, 7])
# 16

# def min_(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# res = reduce(lambda x, y: x + y, [[1, 3], [5, 7], [1, 3, 4, 56]])
# print(res)
# res = reduce(min_, [6, 1, 3, 4, 3, 5])  # min
# res = reduce(lambda x, y: x if x < y else y, [6, 1, 3, 4, 3, 5])  # min
# print(res)

# # ######################################################################################################################
#
# abs(x)
# print(abs(30))
# print(abs(0))
# print(abs(-60))
#
# r = 3 + 4j
# print(abs(r))
#
# # ######################################################################################################################
#
# # aiter
# # aiter would not be discussed, added in Py3.10
#
# # ######################################################################################################################
#
# # all(iterable, /)
#
# empty_lst = []
# lst1 = [100, 200, 300]
# lst2 = [100, 200, 0]
# lst3 = [0, 0, 0]
# print(all(lst1))
# print(all(lst3))
#
# # # If you need non-empty list with all elements are True
# print(all([]))
# print(all(lst1) and lst1)

# # ######################################################################################################################

# # any(iterable, /)

# empty_lst = []
# lst1 = [100, 200, 300]
# lst2 = [100, 200, 0]
# lst3 = [0, 0, 0]
# print(any(lst2))
# print(any(lst3))
# print(any([]))


# # ######################################################################################################################
#
# # anext
# # anext would not be discussed, added in Py3.10
#
# # ######################################################################################################################
#
# print()
# # ascii(object, /)
# # ascii() the same as repr() but escapes non-ascii characters
# print(ascii(1234))
# multiline = """Not
#
# qwerty
# ЇЇЇЇ
# """
# print(ascii(multiline))  # 'Not\n\nqwerty\n\u0407\u0407\u0407\u0407\n'
# print(repr(multiline))  # 'Not\n\nqwerty\nЇЇЇЇ\n'
#
# # ######################################################################################################################
#
# # bin(x, /)
# # x is int or implements __index__

# print(bin(15))
# print(type(bin(15)))
# print(f'{14:#b}')
# print(f'{14:b}')

# # oct(x, /)
# # x is int or implements __index__
# print(oct(15))
# print(type(oct(15)))
# print(f'{10:#o}')
# print(f'{10:o}')

# # hex(x, /)
# # x is int or implements __index__
# print(hex(15))
# print(type(hex(15)))
# print(f'{255:#x}')
# print(f'{255:x}')
# print(f'{255:X}')

# ######################################################################################################################

# # bool(x=False, /)
# print(bool(True))
# print(bool(False))
# print(bool(100))
# print(bool(0))
# print(bool([1, 2, 4]))
# print(bool([]))

# # ######################################################################################################################

# #breakpoint()
# # We will check it when see debugger

# # ######################################################################################################################

# # bytearray()
# # class bytearray(source=b'')
# # class bytearray(source, encoding)
# # class bytearray(source, encoding, errors)
#
# print(bytearray())
# print(bytearray(3))
# print(bytearray([0, 1, 2, 3, 255]))
# # print(bytearray([1, 2, 3, 256]))
# print(bytearray("abcde\t", encoding='ascii'))
# # print(bytearray("abcdeЮ\t", encoding='ascii'))
# print(bytearray("привет", encoding='utf-8'))
# print(type(b"erererer"))

# # bytes() is the same as bytearray but immutable
# # class bytes(source=b'')
# # class bytes(source, encoding)
# # class bytes(source, encoding, errors)

# # ######################################################################################################################

# # callable(object, /)
# print(callable(bin))
# print(callable(5))

# # ######################################################################################################################

# # chr(i, /)
# # ord(c, /)

# # show ascii table
# # could be used when need to validate range of symbols
# print(chr(107))
# print(ord('k'))

#"abcdefe"
# []
import string



# # check if all symbols from 'p' to 'z'
# # p - 112, z - 122
# str1 = "pqwww"
# str2 = "auy"
# def is_from_p_to_z(s:str) -> bool:
#    pass
# print(is_from_p_to_z(str1))  # True
# print(is_from_p_to_z(str2))  # False

# # ######################################################################################################################
#
# # @classmethod
# # Transform a method into a class method.
#
# # ######################################################################################################################
#
# # compile() for code parsing (syntax analyse)
#
# # ######################################################################################################################
#
# # complex
# print(complex(1, 3))  # (1+3j)
#
# # ######################################################################################################################
#
# # delattr(object, name, /)
#
# # ######################################################################################################################

# # # dict()
# d = dict(name="John", age=45)
# print(d)

# # ######################################################################################################################
#
# # dir()
# # Tells about Structure tab of PyCharm
# NNN = 2
# print(dir())
# QQQ = 3
# print(dir("abc"))

#print(dir(""))

# # ######################################################################################################################
#
# # divmod(a, b, /)
# print(divmod(15, 7))
# print((15 // 7, 15 % 7))
#
# # ######################################################################################################################
#
# # eval(expression, /, globals=None, locals=None)
# # DON'T USE IT!!!
# x = 2
# print(eval("x+3"))
#
# # ######################################################################################################################
#
# # exec()  for running code
#
# # ######################################################################################################################
#
# # float()
# print(float("3.14"))
# print(float(3))
#
# # ######################################################################################################################
#
# # format()
# # it is call of obj.__format__(spec)
#
# print(format(10, 'b'))
# print(format('Q', '_>5'))
# a = 'Q'
# print(f"{a:_>5}")

#print("a={a}".format(a=4))


# import datetime
# now = datetime.datetime.now()
#
# print(f"{now!s}")
# print(f"{now!r}")
# print(f"{now!a}")

# country = "Україна"
# print(f"{country!a}")

# number = 1.57765434
# print(f"{number:.3f}")



# # ######################################################################################################################

# # frozenset(iterable=set(), /)
# print(frozenset([1, 2, 3, 2, 2]))  # frozenset({1, 2, 3})

# # ######################################################################################################################

# # getattr(object, name, /)
# # getattr(object, name, default, /)

# # ######################################################################################################################

# # globals()
# before = 4
# print(globals())
# after = 3
# def func(q):
#     a = 3
#     print(globals())
# func(4)

# # ######################################################################################################################

# # hasattr(object, name, /)
# # The result is True if the string is the name of one of the object’s attributes, False if not.

# # ######################################################################################################################

# # hash()
# print(hash(1))
# print(hash(1.0))
# #print(hash([1, 2, 3]))
# print(hash((1, 2, 3)))

# # ######################################################################################################################

# # help()
# # Show usage of help in Python interpretator - help() to start, q - to quit
# def func(a):
#     """Returns square of number"""
#     return a*a
# print(help(func))  # Returns the following lines:

# # ######################################################################################################################

# # id()
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# lst3 = lst1
# print(id(lst1))
# print(id(lst2))
# print(id(lst3))
# print(id(lst1) == id(lst3))
# print(lst1 is lst3)

# # ######################################################################################################################

# # input()

# # ######################################################################################################################

# # int()
# # class int(x=0, /)
# # class int(x, /, base=10)

# print(int("345"))
# print(int(45.5))
# # print(int("45.5"))
# # print(int("123a"))
# print(int("12", 10))
# print(int("1010", 2))
# print(int("0b1010", 2))
# print(int("12", 16))
# print(int("0x12", 16))

# # ######################################################################################################################

# # isinstance()
print(type([1, 2]) is list)
print(type([1, 2]) == list)
print(isinstance([1, 2], (list, dict)))

# # ######################################################################################################################

# # issubclass()

# # ######################################################################################################################

# # iter()

# # ######################################################################################################################

# # len(s, /)
# # might be error if len > 2**100
# print(len("abcde"))
# print(len((1, )))
# print(len({1: 'a', 2: 'b'}))

# # ######################################################################################################################

# # list()
# print(list("abcd"))
# print(list({1: 'a', 2: 'b'}))

# # ######################################################################################################################

# # locals()
# print(globals())
# print(locals())
# print(id(locals()) == id(globals()))
# def func(a, b, c=3):
#     res = a + b
#     print(locals())
#     return res
# func(1, 2)

# # ######################################################################################################################

# # max()
# # min()
# # max(iterable, /, *, key=None)
# # max(iterable, /, *, default, key=None)
# # max(arg1, arg2, /, *args, key=None)
# print(max(1, 2, 3, 4))
# print(max([1, 2, 3, 4]))
# print(min((4, 2, 7, 6)))
# print(max([], default=100))
# print(max([]))  # ValueError: max() arg is an empty sequence
# print(max(["qw", "fffe", "eeedf", "s", "abcde"], key=len))
# #print(max([1,3,5,"ddd"]))

# # ######################################################################################################################

# # memoryview()  # Not used

# # ######################################################################################################################

# # next()

# # ######################################################################################################################

# # object()  # returns super class

# # ######################################################################################################################

# # open()

# # ######################################################################################################################

# # pow(base, exp, mod=None)
# print(pow(2, 3))
# print(pow(2, 3, 5))
# print(pow(-2, 2))
# print(-2 ** 2)
# print(pow(base=3, exp=-1))

# # ######################################################################################################################

# # print()
# #print(self, *args, sep=' ', end='\n', file=None
# # print(1, "ddsdasdasd", [2,3,4])
# # print(1, "ddsdasdasd", [2,3,4], sep='#')

# # print(1, "ddsdasdasd", [2,3,4], sep='#', end='!')
# # print("NEW LINE")
#
# with open("print.txt", 'w') as f:
#     print("TO_PRINT.TXT", 1, "ddsdasdasd", [2,3,4], sep='#', end='!', file=f)

# # ######################################################################################################################

# # property()

# # ######################################################################################################################

# # range()
# #range(start, stop[, step])
# # returns range object
# # r5 = range(5)
# # i5 = iter(r5)
# # print(next(iter(i5)))
# # print(next(iter(i5)))
# # print(range(5))
# # print(list(range(1, 10)))
# # print(list(range(1, 10, 3)))

# # ######################################################################################################################

# # # repr()
# import datetime
# now = datetime.datetime.now()
# print(str(now))
# print(repr(now))
# date = eval("datetime.datetime(2024, 5, 16, 21, 48, 1, 495246)")
# print(type(date))


# # ######################################################################################################################

# # # reversed() -reversed iterator
# # a = range(5)
# # iter_a = iter(a)
# # print(next(iter_a))
# # print(next(iter_a))
# # print(next(iter_a))
# # iter_a_reversed = reversed(a)
# # print(next(iter_a_reversed))
# # print(next(iter_a_reversed))
# # print(next(iter_a_reversed))

# # ######################################################################################################################
#
# # round()  # check what you really need round, truncate, ceil, floor
# print(round(1.75))
# print(round(1.75, 0))
# print(round(1.75, 1))
# print(round(1.75, 2))

# # ######################################################################################################################

# # set()

# # ######################################################################################################################

# # setattr()

# # ######################################################################################################################

# # slice()  # It is not used directly

# # ######################################################################################################################

# # sorted()
# names = ["John", "Anna", "Andrew", "Walter"]
# print(names)
# print(sorted(names))
# print(sorted(names, reverse=True))
# print(sorted(names, key=lambda name: len(name)))
# print(sorted(names, key=lambda name: (len(name), name)))

# # sorting dictionaries
# john = {'name': 'John', 'age': 23}
# marta = {'name': 'Marta', 'age': 43}
# james = {'name': 'James', 'age': 16}

# people = [john, marta, james]
# print(people)
# #print(sorted(people))
# print(sorted(people, key=lambda man: man['age'], reverse=True))

# # ######################################################################################################################

# # staticmethod()

# # ######################################################################################################################

# # # str() compare with repr
# # print(str(True))
# # print(type(str(True)))
# #print(str(b'\x6b', encoding='ascii')) # k

# # ######################################################################################################################

# # # sum()
# salaries = [1, 3, 4, 5]
# print(sum(salaries))
# print(sum(salaries, start=100))

# # ######################################################################################################################

# # super()

# # ######################################################################################################################

# # tuple()

# # ######################################################################################################################

# # type()  # Separately for classes
# #use isinstance() in if-s
# print(type(3))
# print(type(3.5))
# print(type([2, ]))
# print(isinstance(3, int))
# print(isinstance([1,2,3], dict))

# # ######################################################################################################################

# # vars()

# # ######################################################################################################################

# # __import__()

# # ######################################################################################################################
