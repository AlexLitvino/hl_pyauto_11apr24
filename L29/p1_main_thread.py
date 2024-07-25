from time import sleep


def do_job():

    for i in range(5):
        print(f"In do_job {i}")
        sleep(0.5)

do_job()

for i in range(5):
    print(f"In main {i}")
    sleep(0.1)

print("FINISH")
