import random

#print(random.random())  # random float in range [0, 1) 0.0 <= X < 1.0

# # TODO: Task: How to get random [0, N)
# N = 5;  0 <= X < 5   [0, 1) * 5 =
# for i in range(10):
#     print(5 * random.random())


# # # TODO: Task: How to get random [a, b)
# # a = 2
# # b = 5
# for i in range(10):
#     print(random.random() * (5-2) + 2)

#print(random.randint(1, 100))  # a <= N <= b


#print(random.randrange(1, 10, 3))  # random from range(a, b, c)


# print(random.randbytes(4))
# print(type(random.randbytes(4)))  # n -random bytes (immutable)


# lst = ['chrome', 'edge', 'ff']
# print(random.choice(lst))  # random element of list


# lst = [3, 7, 9, 4]
# res = random.shuffle(lst)  # shuffles original list
# print(res)
# print(lst)

#print(random.choices([1, 2, 3], k=2))  # random k elements WITH replacement



# # print(random.sample("ABCDEF", 2))  # returns 2 unique elements from list
# # print(random.sample("AAAAAAAAAAAAAAAABCDEF", 2))  # returns 2 unique elements from list
# lst = [1, 2, 3]
# print(random.sample(lst, 2, counts=[1, 2, 333]))  # returns 2 elements from list where 1 element lst[0], 2 elements lst[1], 333 element lst[2]


# # Saving random generator state
# random.seed(1)
# print([random.random() for _ in range(10)])


# Restoring during re-run
random.seed(1)
print("Test1")
print(random.randint(0, 100))

state = random.getstate()

with open('random_state', 'w') as f:
    f.write(str(state))

print("Test2")
print(random.randint(0, 100))

random.setstate(state)

print("Test2 again")
print(random.randint(0, 100))
