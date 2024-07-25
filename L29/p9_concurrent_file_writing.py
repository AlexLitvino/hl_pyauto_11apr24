from time import sleep
from threading import Thread


def writer(file, data):
    for i in range(100):
        with open(file, 'a') as f:
            f.write(data + '\n')

file_path = 'output.txt'

# threads = []
# for line in ['1111************************************************************', '2222=====']:
#     thread = Thread(target=writer, args=(file_path, line))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()


data = ['1111************************************************************', '2222=====']
import concurrent.futures
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for line in data:
        futures.append(executor.submit(writer, "output2.txt", line))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

