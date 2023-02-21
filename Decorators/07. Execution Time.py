import time


def exec_time(function):

    def wrapper(*args):
        start = time.time()
        func_result = function(*args)
        end = time.time()
        return abs(start-end)
    return wrapper
