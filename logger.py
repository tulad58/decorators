import os
from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            name_function = old_function.__name__
            time_now = datetime.now()
            with open(path, "a+", encoding="utf-8") as f:
                f.write(f"{name_function}\n")
                f.write(f"{result}\n")
                f.write(f"{args}\n")
                f.write(f"{kwargs}\n")
                f.write(f"{time_now}\n")
            return result
        return new_function
    return __logger
