#!/usr/bin/env python

def count_words(text, words):
    tot = 0
    # tstr = ""
    # for p in text.split(" "):
    #     tstr = str(p)
    #     tstr = p.lower()
    #     for w in words:
    #         if tstr.find(w):
    #             tot += 1
    
    tot = 0
    for w in words:
        if  text.lower().count(w) >= 1:
            tot += 1
    return tot
        
        
print count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})
print count_words("Bananas, give me bananas!!!", {"banana", "bananas"})

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    # assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    # assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
    #                    {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print "done Testing..."
