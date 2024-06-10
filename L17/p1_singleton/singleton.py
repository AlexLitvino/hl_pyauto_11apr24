# def singleton(class_):
#
#     def wrapper(*args, **kwargs):
#         if not hasattr(class_, 'instance'):
#             instance = class_(*args, **kwargs)
#             setattr(class_, 'instance', instance)  # class_.instance = instance
#         return getattr(class_, 'instance')
#     return wrapper
#
#
# @singleton
# class King:
#
#     def __init__(self, name):
#         self.name = name
#
#
# print(type(King))  # <class 'function'>
# john = King("John")
# james = King("James")
# print(john is james)
# print(james.name)

# #############################################################################################################

class King:

    instance = None

    def __new__(cls, *args, **kwargs):
        if King.instance is None:
            instance = super().__new__(King)
            King.instance = instance
            #King.instance = super().__new__(King)
        return King.instance

    def __init__(self, name):
        self.name = name


john = King("John")
james = King("James")
print(john is james)
print(james.name)
