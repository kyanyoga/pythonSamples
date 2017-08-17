#!/usr/bin/env python

# def long_repeat(line):
#     if line is '':
#         return 0
#     current = max = 1
#     for index in range(1, len(line)):
#         if line[index] == line[index-1]:
#             current += 1
#             if current > max:
#                 max = current
#         else:
#             current = 1
#     return max

def long_repeat(text):
    if len(text) == 0:
        return 0
    
    counter = 0
    text_l = text.lower()
    max_counter = 0                                   # add
    
    for i in range(len(text_l) - 1):
        print(text_l[i], text_l[i+1])
        if text_l[i] == text_l[i+1]:
            counter += 1
        else:                                          # add
            max_counter = max(max_counter, counter+1) # add
            print max_counter
            counter = 0                               # add

    return max(max_counter, counter+1)                # update

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert long_repeat('sdsffffse') == 4, "First"
    # assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('xaabbbccccddddd') == 5, " Third"
    # assert long_repeat('') == 0, "Fourth"
    print('"Run" is good. How is "Check"?')