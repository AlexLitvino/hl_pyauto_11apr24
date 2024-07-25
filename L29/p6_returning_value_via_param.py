from time import sleep
from threading import Thread


def add(n, result=None):
    if result is None:
        result = {}
    s = 0
    for i in range(n):
        print('CALCULATION')
        s += i
        sleep(0.1)
    result['data'] = s
    return s

#print(add(6))

result = {}
thread = Thread(target=add, args=(6, result))
thread.start()
thread.join()
print(result)
print('FINISH')
