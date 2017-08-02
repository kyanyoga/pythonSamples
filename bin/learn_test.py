##: testing

##: WHY?
##: To Understand our Code better.
##: To learn when we made a mistake
##: To know when we are finished
##: To ensure any future programme changes/additions don't break our programme

def adding(a,b):
    return a + b

def test_adding():
    assert adding(3,4) == 7
    assert adding(3,2) != 10
    assert adding(99,49) == 148
    
    return "All Tests Pass for function adding()"

print test_adding()
