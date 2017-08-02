#!/usr/bin/env python

# imports if needed

# print fizz is divisible by 3
# print buzz if divisible by 5
# print the number in other cases

def checkio(number):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    res = ""
    
    if number%3 == 0:
        res = "Fizz"
    if number%5 == 0:
        res = "Buzz"
    if (number%3 == 0) and (number%5 == 0):
        res = "Fizz Buzz"
    if (number%3 != 0) and (number%5 != 0):
        res = str(number)
    return res

''' -or-
    if number%15== 0:
        return "Fizz Buzz"
    if number%3 == 0:
        return "Fizz"
    if number%5 == 0:
        return "Buzz"
    return str(number)
'''

#Some hints:
#Convert a number in the string with str(n)
print checkio(30)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print "done Testing..."
