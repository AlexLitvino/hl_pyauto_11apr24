from time import sleep
from threading import Thread


# def do_job(iter_number, wait, message):
#
#     for i in range(iter_number):
#         print(f"In do_job {message} {i}")
#         sleep(wait)
#
#
# thread1 = Thread(target=do_job, args=(4, 0.3, '111'))
# thread2 = Thread(target=do_job, kwargs={'iter_number': 6, 'wait': 0.1, 'message': '222'})
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# for i in range(5):
#     print(f"In main {i}")
#     sleep(0.2)
#
# print("FINISH")

# #########################################################################################################


def do_job(iter_number, wait, message):

    for i in range(iter_number):
        print(f"In do_job {message} {i}")
        sleep(wait)


thread1 = Thread(target=do_job, args=(4, 0.3, '111'))
thread1.start()
thread1.join(timeout=0.5)


for i in range(5):
    print(f"In main {i}")
    sleep(0.2)

print("FINISH")
