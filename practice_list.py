#!/usr/bin/env python

'''
(if you can solve the python category, the first two problems
(non-unique elements and roman numerals),you should be good to go): 
https://www.checkio.org/ 
'''

list = ['apple', 'mango', 'pear', 'orange', 'banana']
lenf = len(list)

print ("length of fruitlist %s " % (lenf))

for item in list:
    print item
    
user = "Gus"
number = 38746
print("%s asked %d questions on stackoverflow.com" % (user, number))
print("{0} asked {1} questions on stackoverflow.com".format(user, number))

new_list = [] 
for i in range(0,10):
    new_list.append(i)
    print i, # print on same line
    
print new_list[1], new_list[3], new_list[9]

list.sort()
for item in list:
    print item
    
def fruitIn(fruit, fruitlist):    
    return fruit in fruitlist

def testFruit():
    assert fruitIn('apple', list)
    # assert fruitIn('passion', list)
    assert fruitIn('orange', list)
    return "All test Passed!"
    
print testFruit()


    
