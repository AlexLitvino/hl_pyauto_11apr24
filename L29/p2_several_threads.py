from time import sleep
from threading import Thread

def do_job():

    for i in range(5):
        print(f"In do_job {i}")
        sleep(0.3)

thread = Thread(target=do_job)
thread.start()

for i in range(5):
    print(f"In main {i}")
    sleep(0.2)

print("FINISH")
