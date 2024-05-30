# hasattr()
# getattr()
# setattr()


class Data:

    def __init__(self, data):
        self.data = data

    def __getattr__(self, item):
        print("In __getattr__")
        if item == "corrupted_data":
            return self.data + '3r413294$$R!$!R@$%'
        else:
            raise AttributeError

    # @property
    # def corrupted_data(self):
    #     return self.data + '3r413294$$R!$!R@$%'

    def __setattr__(self, key, value):
        if key == "zero_data":
            print("Setting zero_data...")
            # self.zero_data = value # RecursionError: maximum recursion depth exceeded while calling a Python object
            self.__dict__['zero_data'] = value
        else:
            self.__dict__[key] = value

    def __getattribute__(self, item):
        print("In __getattribute__")
        print(item)
        #return getattr(self, item)  # RecursionError: maximum recursion depth exceeded while calling a Python object
        return super().__getattribute__(item)



data = Data("1234567890")
corrupted_data = data.corrupted_data
print(corrupted_data)
# data.correct_data  #
# data.zero_data = '000000'
# print(data.zero_data)
# print(data.data)
