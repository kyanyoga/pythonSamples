#!/usr/bin/env python

"""
Write a function that takes a number and returns a list of its digits
"""
def solution(input):
    output = []
    i = 0
    sinput = str(input)
    while i < len(str(input)):
        output.append(int(sinput[i:i+1]))
        # print sinput[i:i+1]
        i += 1
    
    return output

#debug
print solution(123)
print solution(400)

assert solution(123) == [1,2,3]
assert solution(400) == [4,0,0]