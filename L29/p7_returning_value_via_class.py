from time import sleep
from threading import Thread


def do_job(n, message):
    s = 0
    for i in range(n):
        print(f"In do_job {message} {i}")
        s += i
        sleep(0.2)
    return s


class CustomThread(Thread):

    def __init__(self, target, *args, **kwargs):
        self.result = None
        self.args = args
        self.kwargs = kwargs
        super().__init__(target=target)

    def run(self) -> None:
        print("Running thread")
        self.result = self._target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result


thread = CustomThread(do_job, 4, "First")
thread.start()
print(thread.result)
result = thread.join()
print(result)
print(thread.result)
