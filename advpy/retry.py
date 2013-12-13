__author__ = 'Parthan'

"""Wrtie a decorator function `with_retries` that retries the function 5 times before giving up
"""

import urllib2

def with_retries(ctr):
    def decorate(f):
        def wrapper(*args):
            while ctr:
                try:
                    return f(*args)
                except Exception, e:
                    ctr -= 1
                    print "Error: Not Found, retrying (%d)" % ((5-ctr) + 1)
        return wrapper
    return decorate

@with_retries(10)
def wget(url):
    return urllib2.urlopen(url).read()

def main():
    url = 'http://google.com/no-such-page'
    wget(url)