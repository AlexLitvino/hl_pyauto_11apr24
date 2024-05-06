a = 1
b = 9
c = 4

def max_3(a, b, c):
    #print("Running max_3")
    print(f"a={a}, b={b}, c={c}")
    result = None
    if a >= b and a >= c:
        #result = a
        return a
    elif b >= a and b >= c:
        #result = b
        return b
    else:
        result = c
        return c
    return result
    print("AFTER")

# print(max_3(1, 23, 3))
# print(max_3(c=2, a=7, b=5))
# print(max_3(5, c=9, b=2))
# print(max_3(c=9, b=2, 6))  # error
# print(max_3(1, 23))  # error
# print(max_3(1, 23, 3, 777))  # error

# lst = [1, 4, 3]
# print(max_3(*lst))


# def min_max(lst):
#     min_ = min(lst)
#     max_ = max(lst)
#     result = {'min': min_, 'max_': max_}
#     return result
#
# print(min_max([1, 3, 6, 2]))


# def min_max(lst):
#     return min(lst), max(lst)
#
# res = min_max([1, 3, 6, 2])
# print(res)
# print(type(res))
# a, b = min_max([1, 3, 6, 2])
# print(a, b)

# def get_file_length(file_path="comments.py"):
#     with open(file_path) as f:
#         length = len(f.readlines())
#     return length
#
# print(get_file_length("comments.py"))
# print(get_file_length())

# print(1, 2, "AAA")

# def get_files_length(*file_path):
#     file_lengths = []
#     for file in file_path:
#         with open(file) as f:
#                 file_lengths.append(len(f.readlines()))
#     return file_lengths
#
# print(get_files_length("comments.py", "p4_functions.py"))

# def sum_(*args):
#     print(args)
#     print(type(args))
#     s = 0
#     for i in args:
#         s += i
#     return s
#
# print(sum_(1, 3, 5))



# def sum_(greetings, *args, start=0, **kwargs):
#     print(greetings)
#     print(start)
#     print(args)
#     print(type(args))
#     print(kwargs)
#     s = start
#     for i in args:
#         s += i
#     return s
#
# print(sum_("Hello", 1, 3, 5, start=100, url="google.com", port=80))

# import requests
# def send_get(url="test.com", **kwargs):
#     requests.get(url=url, **kwargs)
#
# send_get()
# send_get(headers={})

# def increment(a=0):
#     return a+1
#
# print(increment())
# print(increment(3))
# print(increment())

# def increment(a=[]):
#     a.append(111)
#     return a
#
# # a = [1]
# #print(increment(a))
# print(increment())
# print(increment())
# print(increment())


# def increment(a=None):
#     if a is None:
#         a = []
#     a.append(111)
#     return a
#
# # a = [1]
# #print(increment(a))
# print(increment())
# print(increment())
# print(increment())



# def increment(a):
#     a.append(111)
#     return a
#
# a = [1, 2, 3]
# b = increment(a)
# print(b)
# print(a)


def increment(a):
    b = a[:]
    b.append(111)
    return b

a = [1, 2, 3]
b = increment(a)
print(b)
print(a)
