import multiprocessing
from time import sleep


# def do_job(n, output):
#     s = 0
#     for i in range(n):
#         print(f"In subprocess: {i}")
#         s += i
#         sleep(2)
#     print(s)
#     output['result'] = s
#     return s
#
#
# if __name__ == '__main__':
#     n = 5
#     output = {}
#     sleep(3)
#     process = multiprocessing.Process(target=do_job, args=(n, output))
#     process.start()
#
#     for i in range(10):
#         print(f"In main process {i}")
#         sleep(0.3)
#
#     process.join()
#     print(output)  # {}


# ######################################################################################################################

# # # Return value from process using manager shared Value
# def do_job(n, output):
#     s = 0
#     for i in range(n):
#         print(f"In subprocess: {i}")
#         s += i
#         sleep(0.2)
#     output.value = s
#     return s
#
# import ctypes
# if __name__ == '__main__':
#     n = 5
#     #output = multiprocessing.Value('i')  # 'i' is for integers
#     # see in c_type code - c_int is the same as c_long
#     output = multiprocessing.Value(ctypes.c_int)  # 'i' is for integers
#     #output = multiprocessing.Value('i')  # 'i' is for integers
#     process = multiprocessing.Process(target=do_job, args=(n, output))
#     process.start()
#
#     for i in range(3):
#         print(f"In main process {i}")
#         sleep(0.3)
#
#     process.join()
#     print(output)  # <Synchronized wrapper for c_long(10)>
#     print(output.value)


# ######################################################################################################################

# Return value from process using value shared type
def do_job(n, output):
    s = 0
    for i in range(n):
        print(f"In subprocess: {i}")
        s += i
        sleep(0.2)
    print(s)
    output['result'] = s
    return s


if __name__ == '__main__':
    n = 5
    output = multiprocessing.Manager().dict()
    process = multiprocessing.Process(target=do_job, args=(n, output))
    process.start()

    for i in range(3):
        print(f"In main process {i}")
        sleep(0.3)

    process.join()
    print(output)
    print(output['result'])
