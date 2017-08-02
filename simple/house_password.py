#!/usr/bin/env python

def checkio(data):
    # re.match("[a-zA-Z0-9]+", password)
    hasDigit = False
    hasUpper = False
    hasLower = False
    # 
    if len(data) < 10:
        return False
    
    for ch in data:
        # print ch
        if ch.isupper():
            hasUpper = True
        if ch.islower():
            hasLower = True
        if ch.isdigit():
            hasDigit = True
    print hasDigit, hasLower, hasUpper
    if (hasDigit and hasLower and hasUpper):
        return True
    return False

    # for c in data:
    #         if c.isdigit(): 
    #             hasDigit = True
    #         elif c.isupper():
    #             hasUpper = True
    #         elif c.islower():
    #             hasLower = True
    #     return hasDigit and hasUpper and hasLower
    # else:
    #     return False

#Some hints
#Just check all conditions

# print checkio('A1213pokl')
# print checkio('bAse730onE4')
# print checkio('asasasasasasasaas')
print checkio('ULFFunH8ni')


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio('A1213pokl') == False, "1st example"
    # assert checkio('bAse730onE4') == True, "2nd example"
    # assert checkio('asasasasasasasaas') == False, "3rd example"
    # assert checkio('QWERTYqwerty') == False, "4th example"
    # assert checkio('123456123456') == False, "5th example"
    # assert checkio('QwErTy911poqqqq') == True, "6th example"
    print "done Testing..."