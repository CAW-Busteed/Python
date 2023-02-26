import time


def f(a, b):
    """Print the latest tutorial from Real Python"""
    t0 = time.perf_counter()
    for i in range(10**7):
        # c = a + b
        c = sum([a, b])
    t1 = time.perf_counter()
    print(f'it took: {t1 - t0} secs')


if "__main__" == __name__:
    f(2, 3)
