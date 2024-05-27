from __future__ import annotations
import random


class IDCardManager:

    __employee_card_mapping = {}

    @staticmethod
    def add_new_entry(name):
        new_id = random.randint(1000, 9999)
        IDCardManager.__employee_card_mapping[name] = new_id
        return IDCard(new_id)

    @staticmethod
    def validate_card(employee: Employee):
        if employee.name in IDCardManager.__employee_card_mapping:
            return IDCardManager.__employee_card_mapping[employee.name] == employee.apply_id_card()
        else:
            return False


class IDCard:

    def __init__(self, value):
        self.__id = value

    def get_id(self):
        return self.__id


class Employee:

    def __init__(self, name):
        self.name = name
        self.__id_card = IDCardManager.add_new_entry(self.name)

    def apply_id_card(self):
        return self.__id_card.get_id()


def enter_to_office(employee):
    if IDCardManager.validate_card(employee):
        print(f"Employee {employee.name} passes control")
    else:
        print("Trespasser!!!")


john = Employee('John')
enter_to_office(john)

john.name = "Anna"  # Anna takes John's IDCard
enter_to_office(john)


class Intruder:

    def __init__(self, name):
        self.name = name

    def apply_id_card(self):
        return 1111


enter_to_office(Intruder('John'))
