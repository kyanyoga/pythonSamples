#!/usr/bin/env python

def long_repeat(line):
    cnt = 0
    
    for s in line:
        sub = ""
        p = ""
        if s == p:
            sub += s
    """
        length the longest substring that consists of the same char
    """
    # your code here
    return 0

text = list(text)


import collections
from collections import Counter

k = Counter(text).most_common(2)
print(k)
k = sorted(k)
for j in k:

    if j[0].isalpha() == True:
        if j[0].isdigit() == False:
            Counter(k).most_common(7)
            re.search('[A-Z]', j[0])

            return j[0]


def func(text):
    counter = 0
    text_l = text.lower()
    
    for i in range(len(text_l) - 1):
        print(text_l[i], text_l[i+1])
        if text_l[i] == text_l[i+1]:
            counter += 1
            
    return counter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')