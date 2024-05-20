class User:

    immutable_class_field = 0.1
    mutable_class_field = [1, 2]

    def __init__(self, name, age=18):
        self.name = name
        self.age = age


john = User('John')
anna = User('Anna')

# print(john.name)
# print(anna.name)
# john.name = 'James'
# print(john.name)
# print(anna.name)

print(User.immutable_class_field)
#print(User.__dict__)
print(john.immutable_class_field)
print(john.__dict__)
print(anna.immutable_class_field)
print(anna.__dict__)
#User.immutable_class_field = 0.15
john.immutable_class_field += 0.05
# john.immutable_class_field = john.immutable_class_field + 0.05
print(User.immutable_class_field)
print(john.immutable_class_field)
print(anna.immutable_class_field)
#
# john.immutable_class_field = 0.15
# print(User.immutable_class_field)  # 0.1
# print(john.immutable_class_field)  # 0.15
# print(john.__dict__)
# print(anna.immutable_class_field)  # 0.1
# print(anna.__dict__)
# print(john.__class__.immutable_class_field)

# print(User.mutable_class_field)
# print(john.mutable_class_field)
# print(anna.mutable_class_field)
# #john.mutable_class_field.append(111)
# john.mutable_class_field = [333, 4444]
# print(User.mutable_class_field)  # [1, 2, 111]
# print(john.mutable_class_field)  # [1, 2, 111]
# print(anna.mutable_class_field)  # [1, 2, 111]

