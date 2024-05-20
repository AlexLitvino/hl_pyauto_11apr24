# # separate variables
# name = "John"
# age = 32
# salary = 1500
# print(f"{name}'s salary before raise: {salary}")
# salary += 100
# print(f"{name}'s salary after raise: {salary}")


# as dictionary and lists of dictionaries
employees = [
    {'name': 'John', 'age': 32, 'salary': 1500},
    {'name': 'Mary', 'age': 35, 'salary': 2500},
    {'name': 'Oksana', 'age': 31, 'salary': 2200},
]


def get_salary(employees, name: str) -> int:
    return [employee['salary'] for employee in employees if employee['name'] == name][0]


def get_total_salary(employees):
    return sum([employee['salary'] for employee in employees])


print(get_salary(employees, "John"))  # 1500
print(get_salary(employees, "Mary"))  # 2500
print(get_salary(employees, "Oksana"))  # 2200
# print(get_salary(employees, "James"))  # IndexError

print(get_total_salary(employees))
