"""
Basic syntax of class
What is class and class instance. Difference.
Members (attributes) of class.
How to create instance
"""

# class User:
#
#     name = 'John'
#
# #print(User)
#
# john = User()
# print(john)
# #print(john.name)
# anna = User()
# # print(anna)
# # print(john is john)
# # print(john is anna)
# # print(isinstance(john, User))
# # print(isinstance(john, dict))
# # print(type(anna))
# print(anna.name)



class User:

    def __init__(self, my_name):
        print(f"In constructor: {self}")
        self.name = my_name


john = User('John')
print(john)
print()
anna = User('Anna')
print(anna)
# john.name = 'John'
print(john.name)
print(anna.name)

print(User.__name__)
print(anna.__class__.__name__)


# class User:
#
#     def __init__(self, my_name, age=None, account=None):
#         print(f"In constructor: {self}")
#         self.name = my_name
#
# User('John')
# User('John', 34)
# User('John', 34, 3333)