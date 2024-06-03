"""
Write decorator that outputs duration of function runtime +
"""
import time


# def profiler(func):
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Runtime: {end - start}")
#         return result
#
#     return wrapper
#
#
# @profiler
# def add(a, b):
#     return a + b
#
# #add = profiler(add)
#
# print(add(3, 54))


def profiler(lst):

    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start
            lst.append(duration)
            print(f"Runtime: {duration}")
            return result

        return wrapper
    return decorator


stats = []

@profiler(stats)
def add(a, b):
    return a + b

#add = profiler(add)

print(add(3, 54))
print(add(3, 54))
print(stats)
