# 1. Sa se scrie un context manager care masoara durata de executie a unei bucati de cod
from contextlib import contextmanager
from time import perf_counter, sleep


class TimerManager:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        print(self.end - self.start)


with TimerManager():
    sleep(5)
    print('M-am trezit')
print()


@contextmanager
def timer_manager():
    start = perf_counter()
    print(f'Start: {start}')
    yield
    stop = perf_counter()
    print(f'Stop: {stop}')
    print(stop - start)


with timer_manager() as t:
    sleep(2)
