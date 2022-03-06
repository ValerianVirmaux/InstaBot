import time

from logs.logging_toolbox import log_process

def retry(howmany):
    def tryIt(func):
        def f(*args, **kwargs):
            attempts = 0
            while attempts < howmany:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    attempts += 1
                    warning = f"{attempts}- {func.__name__} : {err.msg}"
                    log_process.warning(warning)
                    time.sleep(2)
            log_process.error(func.__name__)
            raise Exception
        return f
    return tryIt


def sleep(n):
    def decorator_func(func):
        def wrapper_func(*args, **kwargs):
            time.sleep(n)
            retval = func(*args, **kwargs)
            return retval
        return wrapper_func
    return decorator_func