# This problem was asked by Apple.

# Implement a job scheduler which 
# takes in a function f and an integer n, and calls f after n milliseconds.

import time

def job_scheduler(f, n):
    time.sleep(n * .001)
    f()

def dummy_function():
    print('hello world')

job_scheduler(dummy_function, 3000)