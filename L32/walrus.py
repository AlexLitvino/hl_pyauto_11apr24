"""
q
"""

# x = input("Enter string: ")
# while x != 'q':
#     print(x.upper())
#     x = input("Enter string: ")

# x = 10

# while (x := input("Enter string: ")) != 'q':
#     print(x.upper())


def cube(y):
    return pow(y, 3)

# x = 5
# y = 3 if x > 10 else 4

lst = [cube(x) for x in range(11) if cube(x) > 17]
print(lst)


lst = [res for x in range(11) if (res := cube(x)) > 17]
print(lst)
