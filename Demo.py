import time
import os


def timeit(func):
    def test():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print("time used:", end - start)

    return test


@timeit
def sum1():
    sum = 1 + 2
    print(sum)

# sum1()
path=os.path.realpath(__file__)
print(path)