__author__ = 'Parthan'

"""Wrtie a decorator function `with_retries` that retries the function 5 times before giving up
"""

import urllib2
import functools

def with_retries(f):
    @functools.wraps(f)
    def wrapper(*args):
        ctr = 5
        while ctr:
            try:
                return f(*args)
            except Exception, e:
                ctr -= 1
                print "Error: Not Found, retrying (%d)" % ((5-ctr) + 1)
    return wrapper

def with_retries_new(ctr=5, sleeptime=0):
    @functools.wraps(f)
    def decorator(f):
        def g(*args):
            for i in range(ctr):
                try:
                    return f(*args)
                except Exception, e:
                    print "Error %s, retrying (%d)"%(e, i+1)
        return g
    return decorator

def with_retries_simple(f=None, ctr=5, sleeptime=0):
    if not f:
        return lambda f: with_retries_simple(f, ctr, sleeptime)

    def g(*args):
        for i in range(ctr):
            try:
                return f(*args)
            except Exception, e:
                print "Error %s, retrying (%d)"%(e, i+1)
                if sleeptime: time.sleep(sleeptime)
        print "Giving up.."
    return g

@with_retries_simple(ctr=10)
def wget(url):
    return urllib2.urlopen(url).read()

def main_retry():
    url = 'http://google.com/no-such-page'
    wget(url)

"""Wrtie a decorator `ignore_exception` that takes exception type as argument and ignores if that exception is raised by
the function being decorated. The new function should return None in case of exception.
"""


def ignore_exception(f=None, exc_type=None):
    if not f:
        return lambda f: ignore_exception(f, exc_type)

    def decorator(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except exc_type, e:
            print "Ignoring exception: %s"%e
            return None
    return decorator

def main():
    file = "/public/foo.txt"

    @ignore_exception(exc_type=IOError)
    def read(file):
        print open(file).readline()
    read(file)