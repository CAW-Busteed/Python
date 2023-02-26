import time
import mysum0


def f(a, b):
    """Print the latest tutorial from Real Python"""
    t0 = time.perf_counter_ns()
    mysum0.add(a, b)
    # mysum0.subtract(a, b)
    t1 = time.perf_counter_ns()
    print(f'it took: {t1 - t0} nano-secs')


if "__main__" == __name__:
    f(2, 3)
