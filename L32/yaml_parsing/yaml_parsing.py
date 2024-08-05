import yaml

users = [{"name": "John",
          "age": 34,
          "salary": 3000},
         {"name": "Anna",
          "age": 54,
          "salary": 5000}]

# with open('users.yaml', 'w') as f:
#     yaml.dump(users, f)

with open('users.yaml', 'r') as f:
    data = yaml.load(f, yaml.Loader)
    #data = yaml.safe_load(f)

print(data)
print(data[0])
