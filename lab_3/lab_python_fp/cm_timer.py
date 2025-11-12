import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exception_type, exception_value, traceback):
        elapsed_time = time.time() - self.start_time
        print(f"time: {elapsed_time}")

@contextmanager
def cm_timer_2(*args, **kwds):
    start_time = time.time()

    try:
        yield start_time
    finally:
        elapsed_time = time.time() - start_time
        print(f"time: {elapsed_time}")

if __name__ == "__main__":  
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)