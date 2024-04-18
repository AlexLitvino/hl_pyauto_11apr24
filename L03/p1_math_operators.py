# Mathematical operators

# Math operators work with int, float, decimal, complex, but also overridden for some other types
# print(3 + 3)
# print(4 - 2)
# print(4 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(4 % 2)
# print(2 ** 3)
# print(4 ** 0.5)
# print(-2 ** 2)
# print(2 ** 2)
# print(2.0 ** 2)
# print(pow(2, 2))
# print(pow(2.0, 2))
# print(pow(2, 3, 3))

# # Decimal
# import decimal
# print(decimal.getcontext())
# decimal.getcontext().prec = 2
# print(decimal.Decimal(0.125) + decimal.Decimal(0.1) + decimal.Decimal(0.100000001))
# print(0.125 + 0.1 + 0.100000001)


# # Complex
# a = 3 + 4j
# b = 2j
# print(a + b)
# print(a * b)

# __add__

# ######################################################################################################################
# # Addition and multiplication with strings
str1 = "Hello "
str2 = ", worlds"
# print(str1 + str2)
print(str1 * 3)
print(3 * str1)
print('Q' + (-3) * str1 + 'Q')  # ''
