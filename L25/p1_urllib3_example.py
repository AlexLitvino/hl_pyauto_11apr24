import urllib3

# resp = urllib3.request("GET", "https://gorest.co.in/public/v2/users")
# print(resp.status)
# print(resp.data)

from cerberus import Validator

schema = {'name': {'type': 'string'}, 'age': {'type': 'integer'}}
v = Validator(schema)

document = {'name': 111}
print(v.validate(document))