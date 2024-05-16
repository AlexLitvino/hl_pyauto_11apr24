print()

import re
import itertools
import math

import xml

py_dict = {'a': 1, 'b': 2}
# import json
# py_dict = {'a': 1, 'b': 2}
# print(json.dumps(py_dict))


# from json import dumps as json_dumps
# print(json_dumps(py_dict))
#
# def dumps():
#     return 'dumped'
#
# print(dumps())

# import json as my_json
# print(my_json.dumps(py_dict))

# import requests
# response = requests.get('https://google.com')
# print(response)

# from helpers.math_util import add
#
# print(add(2, 4))

import helpers
print(helpers.math_util.add(4, 5))


print(__name__)

if __name__ == '__main__':
    print("MAIN")
