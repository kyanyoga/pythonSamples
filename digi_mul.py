#!/usr/bin/env python
def checkio(number):
    tot = 1
    for x in str(number):
        if int(x) !=0:
            tot *= int(x)

    return tot

print checkio(123405)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
