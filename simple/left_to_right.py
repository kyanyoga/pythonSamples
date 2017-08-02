#!/usr/bin/env python

def left_join(phrases):
    newP = []
    for w in phrases:
        newP.append(w.replace("right","left"))
    # print ','.join(newP)
        
    return ','.join(newP)
    # return ",".join([p.replace("right", "left") for p in phrases])
print left_join(("left", "right", "left", "stop"))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print "done Testing..."