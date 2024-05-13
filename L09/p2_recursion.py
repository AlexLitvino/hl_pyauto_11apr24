"""
factorial(0) = 1
factorial(1) = 1
factorial(n) = factorial(n-1) * n
"""
import os
#os.walk()


def factorial_iterative(n):
    if n == 0:
        return 1
    else:
        prod = 1
        for i in range(1, n+1):
            prod *= i
        return prod
#print(factorial_iterative(3))


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return factorial(n-1) * n

# print(factorial(0))
# print(factorial(1))
# print(factorial(3))
# print(factorial(5))
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1003)
#
# print(factorial(1000))


"""
is_palindrome

aqqqqqqqqqqqqqqb
q[::-1]
''

abcffba


"""
def is_palindrome(s, is_first_call=True):
    if is_first_call:
        s = s.strip().lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1], False)



# print(is_palindrome(" aB bA   "))  # True
# print(is_palindrome(" aB bA   Q"))  # False
print(is_palindrome('   A B  A   '))


# Direct and indirect recursion
