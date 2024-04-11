"""
Number
    int
    float

string

bool
list
tuple
dict
set
frozenset

File
Custom classes

"""
# a = 111
# float_numer = 0.1
# float_numer2 = .1
# science_number = 2.3E4  # 2.3 * 10^4
# print(science_number)
# print(0.1 + 0.1 + 0.1)
#
# import decimal
# print(decimal.Decimal("0.1") + decimal.Decimal("0.1") + decimal.Decimal("0.1"))
#
# complex = 1 + 2j
#
# str1 = "qwerty"
# print(str1[0])
# #str1[0] = 'Q'

# str2 = 'qwerty'
# multiline = """111
# 222
# 333
# """
# print(multiline)

# is_visible = False
# is_clickable = True
# print(is_clickable)
# print(type(is_clickable))
# print(True + False + True)

# lst = [1, 'Letter', False]
# print(lst[0])
# print(lst[2])
# print(lst)
# print(len(lst))
# lst.append('LAST_ITEM')
# print(lst)
# print(len(lst))
# lst[0] = 111
# print(lst)

tupl = (1, 2, 3)
print(tupl[1])
#tupl[1] = 222

configuration = ('WebApp', '1.1.0')

print(1 + 2.3)

# dictionary = {
#     'a': 1,
#     'b': 2,
#     #[1, 2]: 5
#     'b': 333
# }
# print(dictionary)
# dictionary['c'] = 3
# print(dictionary)
# print(dictionary['b'])

'''
s = {1, 2, 3, 'string'}
print(s)
s.add('NEW_ELEMENT')
print(s)
s2 = {2, 3, 5, 6}
print(s.intersection(s2))
'''

all_test_cases = {1, 2, 3, 4, 5}
# print(all_test_cases)
test_cases_ip = {2, 3}
not_started = all_test_cases - test_cases_ip
print(not_started)
