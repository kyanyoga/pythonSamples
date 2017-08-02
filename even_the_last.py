#!/usr/bin/env python

def checkio(array):
    sum = 0
    for index, item in enumerate(array, start=0):
        if index%2 == 0 or index == 0:
            sum += item
            # print index, item #item(index)
        if index == len(array) - 1:
            sum *= item                        
    """
        sums even-indexes elements and multiply at the last
    """
    return sum

print checkio([0, 1, 2, 3, 4, 5])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print "done testing!"