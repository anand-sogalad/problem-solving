import time
from functools import wraps


def timer(func):
    wraps(func)

    def wrapper(*args, **kwargs):
        st = time.perf_counter()
        result = func(*args, **kwargs)
        et = time.perf_counter()
        print(f"The function {func.__name__} took {round(et - st, 2)} second(s)")

        return result

    return wrapper
