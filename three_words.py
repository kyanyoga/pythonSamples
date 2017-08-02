#!/usr/bin/env python

# links: https://docs.python.org/3/library/stdtypes.html

def checkio(words):
    wcount = 0
    isWord = True
    for w in words.split():
        # print w
        if w.isdigit():
            wcount = 0
        if w.isalpha():
            wcount += 1
            if wcount >= 3 and isWord:
                return True
            
    return False


# print checkio("Hello World hello")
# print checkio("He is 123 man")

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print "done Testing..."
