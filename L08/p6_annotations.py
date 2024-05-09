from typing import Union, Optional, List, Dict
# mypy

def multiply_string(input_string: str, number: int = 2) -> str:
    return input_string * number

#print(multiply_string('abc ', 3))
# print(multiply_string('abc ', 'a'))


# # # Built-in function isinstance
# a = 3
# print(type(a) == int) # Don't do it
# print(isinstance(1, int))
# print(isinstance('1', int))
# print(isinstance(1, (int, float)))
# print(isinstance(1.34, (int, float)))
# print(isinstance('1', (int, float)))


# # # Returning several types
# def add(a, b) -> Union[int, float, list, None]:
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         return a + b
#     elif isinstance(a, list) and isinstance(b, int):
#         return a * b
#
#
# If None could be returned
# def add(a, b) -> Optional[Union[int, float, list]]:
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         return a + b
#     elif isinstance(a, list) and isinstance(b, int):
#         return a * b
#
#
# # Specifying all types could be too long
# def add(a: Union[int, float, list], b: Union[int, float]) -> Optional[Union[int, float, list]]:
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         return a + b
#     elif isinstance(a, list) and isinstance(b, int):
#         return a * b
#
# T_SALARY
# T_ADD_RES = Optional[Union[int, float, list]]
# def add(a: Union[int, float, list], b: Union[int, float]) -> T_ADD_RES:
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         return a + b
#     elif isinstance(a, list) and isinstance(b, int):
#         return a * b
#
#
# add([1, 2], [3, 5])
