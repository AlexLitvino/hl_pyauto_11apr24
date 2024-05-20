from __future__ import annotations
"""
Methods.
Static and class methods
"""
import random

def generate_connection_error():
    if random.random() < 0.8:
        raise ConnectionError("No Connection")



class User:

    #tax_rate = 0.1
    TAX_RATE = 0.1

    def __init__(self, name, age=18, account=None):
        self.name = name
        self.age = age
        self.account = account

    def print_info(self):
        print(f"User with name {self.name} with age {self.age} years old")


    def send_money_to(self, other: User, num: float):
        #print(self.name)
        print(f"Send from {self.name} account to {other.name}")
        account_before_send = self.account
        try:
            self.account -= num
            generate_connection_error()
            other.account += num
        except ConnectionError:
            print("ERROR!!!")
            #self.account += num
            self.account = account_before_send

    def send_money_to_group(self, num: float, *others: User):
        print(others)
        for other in others:
            self.account -= num
            other.account += num

    @staticmethod
    def calcualate_future_rate(year):
        return (year - 2024) / 100 + User.TAX_RATE

    @classmethod
    def set_tax_rate(cls, new_tax_rate):
        print(f"Setting new tax rate: {new_tax_rate}")
        assert new_tax_rate < 0.25, 'Tax rate should be less than 0.25'
        cls.TAX_RATE = new_tax_rate

    @classmethod
    def create_user_with_height(cls, name, height, age, account):
        print(cls)
        user = cls(name, age, account)
        user.height = height
        return user


john = User('John', account=5000)
#john.print_info()
anna = User("Anna", 21, 2000)
oksana = User("Oksana", 34, 2000)

# print(john.account)  # 5000
# print(anna.account)  # 2000
# try:
#     john.send_money_to(anna, 1000)
# except ConnectionError:
#     print("ERROR!!!")
# print(john.account)  # 4000
# print(anna.account)  # 3000

# john.send_money_to_group(100, anna, oksana)
# print(john.account)
# print(anna.account)
# print(oksana.account)
#
# print(User.calcualate_future_rate(2035))
# print(john.calcualate_future_rate(2035))

# print(john.TAX_RATE)
# User.set_tax_rate(0.2)
# print(john.TAX_RATE)

user = User.create_user_with_height('Andrew', 170, 23, 1000)
print(user.height)