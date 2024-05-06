import shelve

user = {
    'name': 'John',
    'age': 23
}

with shelve.open('shelve.db') as f:
    f['user'] = user

with shelve.open('shelve.db') as f:
    restored_user = f['user']

print(restored_user)
