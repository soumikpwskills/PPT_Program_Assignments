from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args):
        start_time = time.time();
        retval = func(*args)
        print("Execution time: ", time.time()-start_time, "seconds")
        return retval
    return wrapper

@timer
def my_function():
    time.sleep(2)

my_function()