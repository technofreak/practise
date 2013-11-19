__author__ = 'Parthan'

"""
You are given a list of integers. For this task, you should return a list consisting of only the non-unique elements in
this list. To do so you will need to remove all unique elements (elements which are contained in a given list only once
). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements
and result will be [1, 3, 1, 3].
"""

def checkio(data):
    #for i in set(data):
    #    if data.count(i) > 1:
    #        continue
    #    else:
    #        data.remove(i)
    return [x for x in data if data.count(x) > 1]

if __name__ == "__main__":
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "sample 1"
    assert checkio([1, 2, 3, 4, 5]) == [], "sample 2"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "sample 3"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "sample 4"
