# Process of instance creation using __new__ method

class Cat:

    def __init__(self, name):
        print(f"In constructor: {self}")
        self.name = name
        self.language = None

    def set_language(self, language):
        self.language = language

    def meow(self):
        """Say meow"""
        if not self.language:
            print("self.language not set")
        else:
            print(self.language)

# murzik = Cat('Murzik')
# print(murzik)
# print(murzik.name)

murzik = object.__new__(Cat)
print(murzik)
murzik.__init__('Murzik')
print(murzik.name)
#murzik.set_language('Meow')
murzik.meow()