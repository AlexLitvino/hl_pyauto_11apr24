from dataclasses import dataclass, asdict, astuple

# , frozen=True
@dataclass(order=True)
class User:
    name: str
    age: int = 54

user1 = User('John', 23)
print(user1)

user2 = User('Anna')
print(user2)
print(user2.name)

# print(user1 == user2)
#
# user3 = User('John', 23)
# print(user1 == user3)

print(user1 < user2)
user1.name = 'James'
print(user1.name)
print(asdict(user1))
print(astuple(user1))
