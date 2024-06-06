# lst = []
# file

# for item in [1, 2, 3]:
#     print(item)

# lst = [1, 2, 3]
# list_iterator = iter(lst)
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))

# class SquareIterator:
#
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.stop:
#             square = self.current * self.current
#             self.current += 1
#             return square
#         else:
#             raise StopIteration
#
#
# sq_iter = SquareIterator(2, 7)
# for item in sq_iter:
#     print(item)
# # for item in sq_iter:
# #     print(item)

# ##################################################################################################################

# class SquareIterator:
#
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.current = start
#
#     def __iter__(self):
#         return SquareIterator(self.start, self.stop)
#
#     def __next__(self):
#         if self.current < self.stop:
#             square = self.current * self.current
#             self.current += 1
#             return square
#         else:
#             raise StopIteration
#
#
# sq_iter = SquareIterator(2, 7)
# for item in sq_iter:
#     print(item)
# print()
# for item in sq_iter:
#     print(item)


# ##################################################################################################################
# class SquareIterator:
#
#     class SquareIteratorLogic:
#
#         def __init__(self, start, stop):
#             self.stop = stop
#             self.current = start
#
#         def __next__(self):
#             if self.current < self.stop:
#                 square = self.current * self.current
#                 self.current += 1
#                 return square
#             else:
#                 raise StopIteration
#
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         return SquareIterator.SquareIteratorLogic(self.start, self.stop)
#
#
# sq_iter = SquareIterator(2, 7)
# for item in sq_iter:
#     print(item)
# print()
# for item in sq_iter:
#     print(item)

# ##################################################################################################################

# bad idea
class SquareIterator:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < self.stop:
            square = self.current * self.current
            self.current += 1
            return square
        else:
            raise StopIteration


# sq_iter = SquareIterator(2, 7)
# for item in sq_iter:
#     print(item)
# print()
# for item in sq_iter:
#     print(item)
