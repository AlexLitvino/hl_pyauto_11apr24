# import random
#
# names = ['Anna', 'Ben', 'John', 'Julia', 'William']
#
#
# def get_random_person():
#     return {'name': random.choice(names),
#             'age': random.randint(18, 80)}
#
#
# print(get_random_person())


from faker import Faker
faker = Faker('uk_UA')
#faker = Faker()
Faker.seed(100)  # set initial value to reproduce random data
print(faker.locales)
print(faker.name())
print(faker.user_agent())
print(faker.csv(data_columns=("{{name}}", "{{job}}")))
