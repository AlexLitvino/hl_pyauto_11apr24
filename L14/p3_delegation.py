# class Data:
#
#     def __init__(self, lst):
#         self.lst = lst
#
#     @property
#     def average(self):
#         return sum(self.lst) / len(self.lst)
#
#     def append(self, item):
#         self.lst.append(item)
#
# data = Data([1, 2, 3])
# print(data.average)
# #data.lst.append(4)
# data.append(4)
# print(data.average)

# #####################################################################################################
# from collections import UserList
#
# class Data(UserList):
#
#     def __init__(self, lst):
#         super().__init__(lst)
#
#     @property
#     def average(self):
#         return sum(self.data) / len(self.data)
#
#
# data = Data([1, 2, 3])
# print(data.average)
# data.append(4)
# print(data.average)
# print(data[1:])
# data.extend([1, 2])
# print(data.average)
# #####################################################################################################


class Data:

    def __init__(self, lst):
        self.lst = lst

    @property
    def average(self):
        return sum(self.lst) / len(self.lst)

    def __getattr__(self, item):
        return self.lst.__getattribute__(item)

    def __getitem__(self, item):
        return self.lst.__getitem__(item)


data = Data([1, 2, 3])
print(data.average)
data.append(4)
print(data.average)
print(data[1:])
