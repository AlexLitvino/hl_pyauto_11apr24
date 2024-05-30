# __setitem__, __getitem__, __len__, __bool__

class Building:

    def __init__(self, address, floor_numbers=6):
        self.address = address
        self.floors = [None] * floor_numbers

    def __getitem__(self, item):
        return self.floors[item]

    def __setitem__(self, key, value):
        self.floors[key] = value

b = Building('Address')
b[4] = "Office1"
print(b[4:])


# ######################################################################################################################

# # __getitem__ without keeper
# class Square:
#
#     def __getitem__(self, item):
#         return item * item
#
# square = Square()
# for i in range(10):
#     print(square[i])
