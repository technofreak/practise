__author__ = 'Parthan'

"""Write a function 'maximum' that works like built-in 'max' function. It should take an optional keyword arguments
'key' when supplied should use 'key(x)' and key(y) for computong values x and y.

>>> maximum(['Python','Haskell'])
'Python'
>>> maximum(['Python','Haskell',], key=len)
Haskell
"""


def maximum(items, key=None):
    if not key:
        key = lambda x: x
    max = ''
    for item in items:
        # if not key:
        #     max = (item > max and item) or max
        # else:
        #     max = (key(item) > key(max) and item) or max
        #max = getitem(item, key) > getitem(max, key) and item or max
        max = (key(item) > key(max) and item) or max

    return max
