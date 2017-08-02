#!/usr/bin/env python

"""
Write a function that returns the elements on odd positions (0 based) in a list
for index, value in enumerate(numbers, start=1):
-- while --
colors = ["red", "green", "blue", "purple"]
i = 0
while i < len(colors):
    print(colors[i])
    i += 1
"""

def solution(input):
    output = []
    for index, item in enumerate(input, start = 0):
        if index%2 != 0:
            output.append(item)
    return output

# debug
print solution([0,1,2,3,4,5])
print solution([1,-1,2,-2])

assert solution([0,1,2,3,4,5]) == [1,3,5]
assert solution([1,-1,2,-2]) == [-1,-2]