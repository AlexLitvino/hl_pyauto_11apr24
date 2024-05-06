# General, map
# print(len([1, 2]))
# res = map(len, [[1, 2], [2], []])
# print(list(res))
# # res= input("Enter a, b")
# # "4 5" -> ['4', '5']
# # print(res)
# a, b = map(int, input("Enter a, b").split())
# print(a, b)


# lambda with one parameter
# def sqr(x):
#     return x*x

# sqr = lambda x: x*x
# print(sqr(54))

lst = [1, 2, 34]
#print(list(map(sqr, lst)))
print(list(map(lambda x: x*x, lst)))



# lambda with two parameters
sum_ = lambda x, y: x + y

# lambda with no parameters
# lambda : is_status_valid()

# lambda with any number of parameters

# min
# max
# sorted

# Examples with sorted
users = [(1, 'John', 34), (2, 'Anna', 42), (3, 'Andrew', 17), (4, 'Jane', 36), (5, 'Anna', 36)]
print(sorted(users))

# sort by age
print(sorted(users, key=lambda user: user[2]))

# sort by age ascending, then by name
print(sorted(users, key=lambda user: (user[2], user[1])))

# Example with comparing versions
versions = ['1.1.0', '1.1.2', '1.1.9', '1.1.10']
print(max(versions))
print(max(versions, key=lambda version: [int(component) for component in version.split('.')]))

