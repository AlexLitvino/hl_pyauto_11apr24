from functools import total_ordering

@total_ordering
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User(name='{self.name}', age={self.age})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return (self.name == other.name) and (self.age == other.age)

    #def __ne__(self, other):

    # def __hash__(self):
    #     return hash((self.name, self.age))

    def __lt__(self, other):
        return self.age < other.age

# user1 = User("Tabitha", 18)
# user2 = User("Tabitha", 18)
# user3 = User("Jonsy", 19)
# print(f"{user1} == {user2}: {user1 == user2}")  # True
# print(f"{user1} != {user2}: {user1 != user2}")  # False
# print(f"{user1} == {user3}: {user1 == user3}")  # False
# print(f"{user1} != {user3}: {user1 != user3}")  # True

# john = User("John", 34)
# # d = {john: "12345"}
# # print(d)
#
# s = set()
# s.add(john)
# print(john in s)  # True
# john.age = 60
# print(john in s)  # False



john = User("John", 34)
james = User("James", 34)
anna = User("Anna", 23)
oksana = User("Oksana", 45)

users = [john, anna, james, oksana]
# # TODO: sort by age; sort by age and then by name
# print(sorted(users, key=lambda user: user.age))
# print(sorted(users, key=lambda user: (user.age, user.name)))
print(sorted(users))
print(john < james)
print(john >= anna)
