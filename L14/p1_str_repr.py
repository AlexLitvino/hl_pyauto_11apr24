# Difference between str and repr
# s = "qwerty"
# print(str(s))
# print(repr(s))

# import datetime
# now = datetime.datetime.now()
# print(str(now))
# print(repr(now))
# print(type(repr(now)))
# restored_now = eval(repr(now))
# print(now == restored_now)

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User with name {self.name}, {self.age} years old"

    def __repr__(self):
        #return f"User('{self.name}', {self.age})"
        return f"User(name='{self.name}', age={self.age})"



john = User('John', 23)
anna = User('Anna', 34)
print(john)
print(anna)

user_list = [john, anna]
print(user_list)