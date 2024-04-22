# Get methods of object
str = "Qwerty"
#print(dir(str))
# for method in dir(str):
#     if not method.startswith('__'):
#         print(method)


"""
Position in string
    endswith
    find
    index
    rfind
    rindex
    startswith
    count
"""
# print("abcdef".endswith('def'))
# print("abcdef".endswith(('def', 'qwe')))
# print("abcdef".endswith('cd', 1, 4))
# print("abcdefa".find('a'))
# print("abcdefa".find('q'))
# print("abcadefa".find('a', 2, 4))
# print("abcdefa".index('a'))
# print("abcdefa".index('q'))
# print("abcadefa".index('a', 2, 4))
# print("abcdefa".rfind('a'))
# print("abcdefa".rindex('a'))
# print("abcdef".startswith('abc'))
# print("abcdabefab".count('ab'))
# print("abcdabefab".count('abq'))
# print("abcdabefab".count('ab', 2, 6))

"""
Letter case
    capitalize
    casefold
    lower
    upper
    swapcase
    title
"""
# print("Letter case")
# print("lowercased".capitalize())
# print("Street".casefold())
# print("Straße".casefold())
# print("AbCdE".lower())
# print("AbCdE".upper())
# print("AbCdE".swapcase())
# print("this is title for newspaper".title())

"""
Justification
    center
    ljust
    rjust
    zfill
"""
# print("Justification")
# print("abc".center(13, '*'))
# print("abc".rjust(13, '*'))
# print("abc".ljust(13, '*'))
# print("-34".zfill(12))

"""
Combination/separation
    join
    split
    rsplit
    splitlines
    partition
    rpartition
"""
# print("Combination/separation")
# print("-".join(['a', 'b', 'c']))
# print("a b  c".split())
# print("a-b-c".split('-'))
# print("docs.python.org/3/library/stdtypes.html".split('/', maxsplit=1))
# print("a b c".rsplit())
# print("a b c".rsplit(maxsplit=1))
# multi = """Line1
# Line2
# Line3
# """
# print(multi.splitlines())
# print(multi.splitlines(keepends=True))
# print("https://www.google.com/search?q=git".partition('?'))
# print("docs.python.org/3/library/stdtypes.html".partition('?'))
# print("a b c".rpartition(' '))

"""
Removing whitespaces
    strip
    lstrip
    rstrip
"""
# print("Removing whitespaces")
# print(" ab cd  \t\n".strip())
# print("____abcd_____".strip('_'))
# print("____abcd_____".lstrip('_'))
# print("____abcd_____".rstrip('_'))

"""
Modification
    removeprefix
    removesuffix
    replace
    expandtabs
"""
# print("Modification")
# print("DEBUG saved to db".removeprefix("DEBUG"))
# print("DEBUG saved to db".removeprefix("INFO"))
# print("abcdqq".removesuffix('qq'))
# print("abcdqq".removesuffix('QQ'))
# str1 = "ababbbabaaab"
# str2 = str1.replace('ab', 'xx')
# print(str1)
# print(str2)
# print("ababbbabaaab".replace('ab', 'xx'))
# print("ababbbabaaab".replace('ab', 'xx', 2))
# print('01\t012\t0123\t01234'.expandtabs())
# print('01\t012\t0123\t01234'.expandtabs(4))

"""
Checking
    isalnum
    isalpha
    isascii
    isdecimal
    isdigit
    isidentifier
    islower
    isnumeric
    isprintable
    isspace
    istitle
    isupper
"""
# print("Checking")
# print("ab12".isalnum())
# print("ab_12".isalnum())
# print("ab".isalpha())
# print("ab12".isalpha())
# print("ab12\n\tQ".isascii())
# print("Привет".isascii())

"""
isdecimal() method returns True only for Decimal Numbers
isdigit() method returns True only for Decimals, Subscripts, Superscripts
isnumeric() method returns True only for Digits, Vulgar Fractions, Subscripts, Superscripts, Roman Numerals, Currency Numerators
"""
# print("123".isdecimal())
# print("123a".isdecimal())
# print("2²".isdigit())
# print("2¼".isdigit())
# print("2¼Ⅸ".isnumeric())
# print("".isnumeric())

# print("my_variable".isidentifier())
# print("not-valid-python-identifier".isidentifier())
# print("abc".islower())
# print("aBc".islower())
#
# # Non-printable characters are Unicode symbols from category Other and Separator except ASCII whitespace (0x20)
# print("abc".isprintable())
# print(" \t\n".isspace())
# print("A \t\n".isspace())
#
# print("Title Cased String".istitle())
# print("Not title cased string".istitle())
#
# print("ABC".isupper())
# print("AbC".isupper())

"""
Output
    encode
    format
"""
# print("Output")
# print('Hello'.encode('ascii'))
# print('Hello'.encode('UTF-8'))
# print('Привет'.encode('UTF-8'))
# salary = 1003.45662
# print("My salary is {:.2f}".format(salary))
# packet = 156
# print("Received packet: {:#x}".format(packet))
# print("{: <10} {: <10} {: <10}".format("Anna", "Andrew", "Jack"))
# print("{: <10.2f} {: <10.2f} {: <10.2f}".format(2345.34345, 34233.4, 23.444662))


# # Chain method call
# string = "   AbCdE    "
# print(string.strip().lower().replace('ab', 'xy'))
#
# n = 3
# number_of_a = ('AB' * n).lower().count('a')
# print(number_of_a)
