import json

# # converting Python dict to JSON string
# data = {'a': 1, 'b': 2}
# json_string = json.dumps(data)
# print(json_string)
# print(type(json_string))
# print(type(data))
#
# # Converting JSON string to Python object
# restored_data = json.loads(json_string)
# print(restored_data)
# print(type(restored_data))


# writing Python dict to JSON file
data = {'a': 1, 'b': 2}
# with open('data.json', 'w') as f:
#     json.dump(data, f)

# # reading JSON file
with open('data.json', 'r') as f:
    restored_data2 = json.load(f)
print(restored_data2)
print(restored_data2['a'])
print(restored_data2 == data)
