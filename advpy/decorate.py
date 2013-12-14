__author__ = 'Parthan'

"""Wrtie a decorator function `logtime` to print the amount of time a function is taken to execute.
"""

import time

def logtime(f):
    def decorated(*x):
        start = time.time()
        v = f(*x)
        timetaken = time.time() - start
        print "%s took %.5f seconds" % (f.__name__+'('+str(x)+')', timetaken)
        return v
    return decorated

class LogTime:
    def __init__(self, f):
        self.f = f

    def __call__(self, *x, **y):
        start = time.time()
        v = self.f(*x, **y)
        timetaken = time.time() - start
        print "%s took %.5f seconds" % (self.f.__name__+'('+str(x)+')', timetaken)
        return v

@LogTime
def timepass(n):
    result = 0
    for i in range(n):
        for j in range(i):
            result += i*j
    return result

def main():
    print timepass(100)

