#!/usr/bin/env python

def index_power(array, n):
    if len(array) < n+1:
        return -1
    return array[n]**n
    
    
    """
        Find Nth power of the element with index N.
    """
    return None

print index_power([1, 2], 3)
print index_power([1, 2, 3, 4], 2)
print index_power([96,92,94],3)
print index_power([1, 3, 10, 100], 3)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    assert index_power([96,92,94],3) == -1, "IndexError"
    print "done Testing..."