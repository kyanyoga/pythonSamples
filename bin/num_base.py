#!/usr/bin/env python

def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1
    
print checkio("AF", 16)
print checkio("AB", 10)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("AF", 16) == 175, "Hex"
    # assert checkio("101", 2) == 5, "Bin"
    # assert checkio("101", 5) == 26, "5 base"
    # assert checkio("Z", 36) == 35, "Z base"
    # assert checkio("AB", 10) == -1, "B > A > 10"
    print "done Testing..."
    
# 'To good (easy) to be true' solution.
    # if second argument 'base' is given to int(),
    # then first argument is a string representing a
    # number in a given base.
    # So int() just converts 'str_number',
    # and you have nothing left to do.
    try: return int(str_number,radix)
    except ValueError: return -1 
    '''
?
    # Create a list of numbers from 0 to 9
    # as strings, add letters from A to Z.
    rep = [str(i) for i in range(0,10)]
    rep.extend(string.ascii_uppercase)
    # cut list to leave there only the base digits
    rep = rep[:radix]
?
    res = 0
    # Go through given str_number and calculate the result.
    # We need enumerate to get the current power
    # when going through digits.
    # List index of a char from a given string
    # represents its decimal value
    for i, char in enumerate(str_number[::-1]):
        try:
            res += rep.index(char) * (radix ** i)
        except ValueError:
            return -1
    return res