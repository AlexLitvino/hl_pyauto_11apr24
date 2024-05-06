import pickle

user = {
    'name': 'John',
    'age': 23
}

byte_string = pickle.dumps(user)
print(byte_string)

with open('pickle.db', 'wb') as f:
    pickle.dump(user, f)

with open('pickle.db', 'rb') as f:
    data = pickle.load(f)

with open('pickle.db', 'rb') as f:
    byte_string_from_file = f.read()
print(byte_string_from_file)

print(data)
print(type(data))
