import time


# Wait (time.sleep)
# print('before sleep')
# time.sleep(3)
# print('after sleep')
#

# def wait_until(condition, timeout, step):
#     pass

# def wait(seconds):
#     print(f"Waiting for {seconds} seconds...")
#     for _ in range(seconds):
#         time.sleep(1)
#         print('.', sep='', end='')
#     print()
#
# wait(5)


# Measurement duration
# # time.clock (obsolete, use before 3.8)
# a = time.clock()
# print(a)

# # time.time
# start_time = time.time()
# print(start_time)
# time.sleep(3)
# end_time = time.time()
# print(f"duration = {end_time - start_time}, s")


# # time.perf_counter - the most accurate clock for hort periods
# start_time = time.perf_counter()
# time.sleep(3)
# end_time = time.perf_counter()
# print(f"duration = {end_time - start_time}, s")

# # time.process_time() - doesn't take time spent in sleeps
# start_time = time.process_time_ns()
# for i in range(10000000):
#     pow(3.3443432, 2.781213)
# time.sleep(3)
# end_time = time.process_time_ns()
# print(f"duration = {(end_time - start_time)/1000_000_000}, s")


# # Getting UTC time, local time or using timestamps
# print(time.time())  # current timestamp
# print(time.gmtime())  # current GMT time
# print(time.localtime())  # current local time
# print(time.gmtime(3600))  # GMT time for timestamp
# print(time.localtime(3600))  # local time for timestamp


# struct_time = time.localtime()
# print(struct_time.tm_wday)  # get component of time
# print(time.mktime(struct_time))  # convert time structure to timestamp
# #
# # Formatting time
# print(time.strftime("%H:%M"))  # for current time
# print(time.strftime("%H:%M", struct_time))  # for specific time


# ######################################################################################################################
# datetime lib

# # timedelta object
# from datetime import timedelta
# delta = timedelta(days=1) + timedelta(hours=5)
# print(delta)
#
# year = timedelta(days=365)
# ten_years = 10 * year
# print(ten_years)
#
# # # date object
# from datetime import date
# # today = date.today()
# # print(today)
# # print(today + ten_years)
# # #
# print(date.fromtimestamp(3600 * 24))


# # # datetime object
from datetime import datetime
# print(datetime.today())
# t1 = datetime(year=2022, month=11, day=3)
# t2 = datetime(year=2024, month=1, day=1)
# print(t2 - t1)
# print(type(t2 - t1))
#
today = datetime.today()
print(today.strftime("%Y %m %d - %H:%M:%S"))
