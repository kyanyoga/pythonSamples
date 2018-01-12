#!/usr/bin/env python

# imports if needed


def say_hi(name, age):
    return "Hi. My name is " + name + " and I'm " + str(age) + " years old"
    

print say_hi("Gus", 53)

if __name__ == '__main__':
    # These are the asserts
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')
