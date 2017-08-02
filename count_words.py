#!/usr/bin/env python

def checkio(instr):
    
    if instr == ' ':
        return 0
    
    A = []
    instr = instr.strip()
    
    if instr == ' ':
        return 0
    
    for w in instr.split(' '):
        # print w
        if w not in A:
            A.append(w)
        print A
           
    return len(A)

print checkio(' ')
# print checkio(' Hello World ')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(' ') == 0
    assert checkio(' Hello Word ') == 2
    print "done Testing..."
