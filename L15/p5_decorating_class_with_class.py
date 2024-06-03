# DON'T DO THIS

class Tracer:

    def __init__(self, aClass):
        self.aClass = aClass

    def __call__(self, *args, **kwargs):
        self.wrapped = self.aClass(*args, **kwargs)
        return self

    def __getattr__(self, item):
        print(f"Trace: {item}")
        return getattr(self.wrapped, item)


@Tracer
class User:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

# Person = Tracer(Person)

john = User("John")
john.print_name()
anna = User("Anna")
anna.print_name()

john.print_name()
