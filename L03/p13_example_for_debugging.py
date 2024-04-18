def is_even(number):
    result = None
    if number % 2 == 0:
        result = True
    else:
        result = False
    return result


print("Before debug")
lst = [4, 5, 2, 5, 2, 8, 4, 8, 1, 5]

squares = []
for number in lst:
    if is_even(number):
        print(number)
        print("In if")
        square = number * number
        squares.append(square)
    else:
        print("In else")
        print("Odd number detected")

print(squares)
