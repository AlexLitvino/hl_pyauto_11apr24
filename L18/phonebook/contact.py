import datetime
import re


class StringValidator:
    """Descriptor for setting string values.
    Set value should correspond to pattern specified in constructor.
    If value doesn't satisfy pattern AssertionError should be raised"""

    def __init__(self, pattern):
        self.pattern = pattern
        self.match = re.compile(pattern)

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        assert self.match.fullmatch(value), f"Set value doesn't correspond to '{self.pattern}' regular expression"
        instance.__dict__[self.name] = value


class Contact:
    """
    name field should contain alphanumeric symbols 3-20 length
    description field should contain any symbol. It can't be longer than 120 symbols
    """
    name = StringValidator(pattern=r"[a-zA-Z0-9]{3,20}")
    description = StringValidator(pattern=r".{,120}")

    def __init__(self, name, birth_year=None, phones=None, description="", weight=None, height=None):  # TODO: birth date with variants MM-DD, MM-DD-YYYY
        self.name = name
        self.birth_year = birth_year
        self.weight = weight
        self.height = height
        if phones:
            self.phones = phones
        else:
            self.phones = []
        self.description = description

    @property
    def age(self):
        if self.birth_year:
            return datetime.datetime.now().year - self.birth_year
        else:
            return None

    @property
    def body_mass_index(self):
        if self.weight and self.height:
            return self.weight / ((self.height/100) ** 2)
        else:
            return None

    def __str__(self):
        # TODO: update depending of what fields are present
        return f"{self.name} {self.birth_year} {' '.join(self.phones)}"

    def serialize(self):
        return {
            'name': self.name,
            'birth_year': self.birth_year,
            'weight': self.weight,
            'height': self.height,
            'phones': self.phones,
            'description': self.description
        }


if __name__ == '__main__':
    contact1 = Contact('Joe')
    print(contact1)
    print(contact1.age)
    print(contact1.name)

    contact2 = Contact('Leo')
    print(contact2)
    print(contact2.age)
    print(contact2.name)

    print(contact1.name)
