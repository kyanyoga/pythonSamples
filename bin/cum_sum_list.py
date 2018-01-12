#!/usr/bin/env python

"""
Write a function that returns the cumulative sum of elements in a list
"""

def solution(input):
    output = []
    tot = 0
    for item in input:
        tot += item
        output.append(tot)
        
    return output

# def wally():
#    Counter

#debug
print solution([1,1,1])
print solution([1,-1,3])

assert solution([1,1,1]) == [1,2,3]
assert solution([1,-1,3]) == [1,0,3]