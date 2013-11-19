

__author__ = 'parthan'

def checkio(inputs):
    sofia, sincr, oldman, oincr = inputs[:]
    result = list(zip(range(sofia, oldman, sincr), range(oldman, sofia, -oincr)))
    for item in result:
        print item
        if item[0] >= item[1]:
            return item[0]

if __name__ == "__main__":
    #print checkio([100, 50, 1500, 100])
    assert checkio([150, 50, 1000, 100]) == 450, 'First'
    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    print 'All is ok'