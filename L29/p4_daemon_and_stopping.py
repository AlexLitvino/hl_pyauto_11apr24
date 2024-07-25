from time import sleep
from threading import Thread


# def do_job(iter_number, wait, message):
#
#     for i in range(iter_number):
#         print(f"In do_job {message} {i}")
#         sleep(wait)
#
#
# thread1 = Thread(target=do_job, args=(4, 0.3, '111'), daemon=True)
# thread1.start()
# #print(thread1.isDaemon())
# print(thread1.daemon)
# for i in range(5):
#     print(f"In main {i}")
#     sleep(0.1)
#
# print("FINISH")

# # #############################################################################################################
#
# def infinite_job(message, wait):
#     i = 0
#     while True:
#         print(f"In do_job {message} {i}")
#         sleep(wait)
#         i += 1
#
#
# thread = Thread(target=infinite_job, args=('Hello', 0.1), daemon=True)
# thread.start()
#
# for i in range(5):
#     print(f"In main {i}")
#     sleep(0.1)
#
#
# print("FINISH")

# #############################################################################################################

is_running = True
def infinite_job(message, wait):
    i = 0
    while is_running:
        print(f"In do_job {message} {i}")
        sleep(wait)
        i += 1


thread = Thread(target=infinite_job, args=('Hello', 0.1))
thread.start()

for i in range(5):
    print(f"In main {i}")
    sleep(0.1)
is_running = False

print("FINISH")

# #############################################################################################################
from queue import Queue


class Collector:

    def __init__(self):
        self._thread = Thread(target=self.collect)
        self._queue = Queue()
        self._running = True
        self._thread.start()

    def collect(self):
        print('Collecting...')
        while self._running:
            item = client.collect()
            self._queue.put(item)

    def stop(self):
        self._running = False

    def get_items(self):
        items = []
        while not self._queue.empty():
            items.append(self._queue.get())
        return items
