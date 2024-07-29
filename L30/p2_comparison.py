from time import sleep
import time

from threading import Thread
from multiprocessing import Process
NS = 1000_000_000


def do_io_job(n):
    for _ in range(n):
        print("Start waiting")
        sleep(1)
        print("End waiting")


def do_cpu_job(n):
    import random
    import math
    for _ in range(n):
        lst = [random.random() for i in range(1000_000)]
        [math.sin(i) for i in lst]
        [pow(i, 4.454355) for i in lst]


if __name__ == '__main__':
    pass
#
#     # ##################################################################################################################
#
#     start_time = time.perf_counter_ns()
#     for i in range(4):
#         do_io_job(4)
#     end_time = time.perf_counter_ns()
#     print(f"Sync io task performed in {(end_time - start_time)/NS}, s")
#
#
#     start_time = time.perf_counter_ns()
#     threads = []
#     for i in range(4):
#         thread = Thread(target=do_io_job, args=(4,))
#         threads.append(thread)
#         thread.start()
#     for t in threads:
#         t.join()
#     end_time = time.perf_counter_ns()
#     print(f"Async io task performed in {(end_time - start_time)/NS}, s")
#
#     start_time = time.perf_counter_ns()
#     processes = []
#     for i in range(4):
#         process = Process(target=do_io_job, args=(4,))
#         processes.append(process)
#         process.start()
#     for p in processes:
#         p.join()
#     end_time = time.perf_counter_ns()
#     print(f"Parallel io task performed in {(end_time - start_time)/NS}, s")

# T P N
# T 4.001180633
# P 4.011223331
    # ######################################################################################################################

    start_time = time.perf_counter_ns()
    for i in range(4):
        do_cpu_job(4)
    end_time = time.perf_counter_ns()
    print(f"Sync cpu task performed in {(end_time - start_time)/NS}, s")


    start_time = time.perf_counter_ns()
    threads = []
    for i in range(4):
        thread = Thread(target=do_cpu_job, args=(4,))
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()
    end_time = time.perf_counter_ns()
    print(f"Async cpu task performed in {(end_time - start_time)/NS}, s")

    start_time = time.perf_counter_ns()
    processes = []
    for i in range(4):
        process = Process(target=do_cpu_job, args=(4,))
        processes.append(process)
        process.start()
    for p in processes:
        p.join()
    end_time = time.perf_counter_ns()
    print(f"Parallel cpu task performed in {(end_time - start_time)/NS}, s")

# P T  N
