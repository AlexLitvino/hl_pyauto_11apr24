import sqlite3
DB_PATH = 'object_conversion.db'


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User(name={self.name}, age={self.age})"


class UserWithConformMethod(User):

    def __init__(self, name, age):
        super().__init__(name, age)

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return f"{self.name}|{self.age}"


# ######################################################################################################################
# # Using __conform__ for converting Python object to db
# connection = sqlite3.connect(DB_PATH, isolation_level=None)
# TABLE_NAME_CONFORM = 'UserConform'
# cursor = connection.cursor()
# cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME_CONFORM} (employee TEXT);')
# user_conform = UserWithConformMethod('John Smith', 56)
# cursor.execute(f'INSERT INTO {TABLE_NAME_CONFORM} VALUES (?);', (user_conform,))
# cursor.execute(f'SELECT * FROM {TABLE_NAME_CONFORM};')
# data = cursor.fetchall()
# print(data)


# ######################################################################################################################
# # Using sqlite3.PARSE_COLNAMES
# def user_adapter(user):
#     return f"{user.name}|{user.age}"
#
#
# def user_converter(value):
#     value = str(value, 'utf-8')
#     name, age = value.split('|')
#     return User(name, int(age))
#
#
# sqlite3.register_adapter(User, user_adapter)
# sqlite3.register_converter('my_user', user_converter)
#
# TABLE_NAME_COLNAMES = 'UserColNames'
# connection = sqlite3.connect(DB_PATH, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
#
# cursor = connection.cursor()
# cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME_COLNAMES} (user my_user);')
# user_colnames = User('John Smith', 34)
# cursor.execute(f'INSERT INTO {TABLE_NAME_COLNAMES} (user) VALUES (?);', (user_colnames,))
# connection.commit()
#
# cursor.execute(f'select user as "user [my_user]" from {TABLE_NAME_COLNAMES};')
#
# data = cursor.fetchall()
# print(data)
# restored_user = data[0][0]
# print(restored_user.name)

# ######################################################################################################################
# # Using sqlite3.PARSE_DECLTYPES
#
def user_adapter(user):
    return f"{user.name}|{user.age}"


def user_converter(value):
    value = str(value, 'utf-8')
    name, age = value.split('|')
    return User(name, int(age))


sqlite3.register_adapter(User, user_adapter)
sqlite3.register_converter('my_user', user_converter)

TABLE_NAME_DECLTYPES = 'UserDeclTypes'
connection = sqlite3.connect(DB_PATH, isolation_level=None, detect_types=sqlite3.PARSE_DECLTYPES)

cursor = connection.cursor()
cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME_DECLTYPES} (user my_user);')
user_decltypes = User('John Smith', 34)
cursor.execute(f'INSERT INTO {TABLE_NAME_DECLTYPES}(user) VALUES (?);', (user_decltypes,))

cursor.execute(f'select user from {TABLE_NAME_DECLTYPES};')

data = cursor.fetchall()
print(data)
restored_user = data[0][0]
print(restored_user.name)
