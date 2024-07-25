from time import sleep
from threading import Thread, Lock, RLock, Event, Timer


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.lock = Lock()
        self.running = Event()
        #self.running.

    def increase_salary(self):
        #with self.lock:
        #self.lock.acquire(timeout=1)
        self.lock.acquire()
        #self.lock.acquire()
        local_var = self.salary
        local_var += 100
        sleep(1)
        self.salary = local_var
        self.lock.release()
        #self.lock.release()

john = Employee('John', 1000)
# john.increase_salary()
# john.increase_salary()
# print(john.salary)

# thread1 = Thread(target=john.increase_salary)
# thread2 = Thread(target=john.increase_salary)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print(john.salary)

def func():
    print("ALARM")

timer = Timer(3, func)
timer.start()

for i in range(10):
    print(i)
    sleep(1)
