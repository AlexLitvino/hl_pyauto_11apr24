# def func(a, b, c):
#     print(f"a={a}")
#     print(f"b={b}")
#     print(f"c={c}")
#     print()
#
# func(1, 2, 3)
# func(1, c=3, b=2)
# func(c=3, b=2, a=1)


def func(a, /, b, c):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
# func(1, 2, 3)
# func(1, c=3, b=2)
#func(c=3, b=2, a=1)

def func(a, *, b, c):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
#func(1, 2, 3)
#func(1, c=3, b=2)
#func(c=3, b=2, a=1)

def func(a, /, *, b, c):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
#func(1, 2, 3)
#func(1, c=3, b=2)
# func(c=3, b=2, a=1)
