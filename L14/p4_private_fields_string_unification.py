class PrivacyMixin:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __setattr__(self, key, value):
        if key in self.private_fields:
            raise Exception("Private field can't be set")
        else:
            super().__setattr__(key, value)


class StringUnificationMixin:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __setattr__(self, key, value):
        if key in self.string_fields:
            self.__dict__[key] = value.capitalize()
        else:
            super().__setattr__(key, value)



class User(PrivacyMixin, StringUnificationMixin):

    private_fields = ['salary']
    string_fields = ['name', 'occupation']

    def __init__(self, name, occupation, salary, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.occupation = occupation
        self.__dict__['salary'] = salary

    def __repr__(self):
        return f'User("{self.name}", "{self.occupation}", {self.salary})'


john = User("John", "SW Tester", 3000)
print(john)
# john.salary = 5000

john.name = "JAmes"
john.occupation = "DEVeloper"
print(john)
