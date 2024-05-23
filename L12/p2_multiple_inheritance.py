# class Horse:
#
#     def __init__(self, speed):
#         print("In Horse Constructor")
#         self.speed = speed
#
#     def ride(self):
#         print(f"Riding with speed {self.speed}")
#
#
# class Donkey:
#
#     def __init__(self, weight):
#         print("In Donkey Constructor")
#         self.weight = weight
#
#     def transport(self):
#         print(f"Transport cargo of weight {self.weight}")
#
#
# class Mule(Horse, Donkey):
#
#     def __init__(self, speed, weight):
#         #super().__init__(speed)
#         Horse.__init__(self, speed)
#         Donkey.__init__(self, weight)
#
#     def work(self):
#         self.ride()
#         self.transport()
#
#
# mule = Mule(100, 50)
# # mule.ride()
# # mule.transport()
# # print(mule.weight)
# # print(Mule.__bases__)
# # print([cls.__name__ for cls in Mule.__bases__])
# mule.work()


# ######################################################################################################################
#object
class Horse:

    def __init__(self, speed, **kwargs):
        print("In Horse Constructor")
        super().__init__(**kwargs)
        self.speed = speed

    def ride(self):
        print(f"Riding with speed {self.speed}")

    def info(self):
        print(self.speed)


class Donkey:

    def __init__(self, weight, **kwargs):
        print("In Donkey Constructor")
        super().__init__(**kwargs)
        self.weight = weight

    def transport(self):
        print(f"Transport cargo of weight {self.weight}")

    def info(self):
        print(self.weight)


class Mule(Donkey, Horse):

    def __init__(self, speed, weight):
        super().__init__(speed=speed, weight=weight)

    def work(self):
        self.ride()
        self.transport()
"""
     O
Horse Donkey
   Mule
"""



mule = Mule(100, 50)
# mule.ride()
# mule.transport()
mule.work()
mule.info()

print(Mule.__mro__)