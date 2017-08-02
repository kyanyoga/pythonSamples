#!/usr/bin/env python

def find_message(text):
    """Find a secret message"""
    message = ""
    for ch in text:
        if ch.isupper():
            message += ch
    return message

# if any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in s):
#      # <do something>
# else:
#      # <do something>

# debug

print find_message("How are you? Eh, ok. Low or Lower? Ohhh.")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    # assert find_message("hello world!") == "", "Nothing"
    # assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print "done Testing..."
