#!/usr/bin/env python

def checkio(text):
    letters = {}
    text = text.replace(' ', '')
    for l in str(text.lower()):
        if not l.isalpha(): continue
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    x = sorted(letters)
    mx = max(x, key=letters.get)
    # print (mx)
    return (mx)
'''
    text = text.lower()
    filtered_text = filter(str.isalpha, text)
    counter = Counter(sorted(filtered_text))
    return counter.most_common(1)[0][0]
'''

'''
# Variables
    i = 0                                   # Controls the alphabet lenght;
    counter = 0                             # Number of times that the actual item appears in text;
    countMemory = 0                         # Number of times that the most present letter appears;
    alphabet = "abcdefghijklmnopqrstuvwxyz" # Wordlist to check;
    
    text = text.lower()                     # Conver text to lower case;    

    for item in alphabet:                   # Check each alphabet letter (in order);    
        if i < len(alphabet):               # Limit the counter to the alphabet lenght;        
            counter = text.count(item)      # Count the alphabet item on the text;
            
            if counter > countMemory:       # If the actual letter is more present than the provious letter...            
                countMemory = counter       # It's quantity will me stored in the countMemory...
                letter = item               # With his letter;
                
        i += 1                              # For each time the FOR routine runs, it increase this variable;

    return letter                           # Return the more present and first in alphabet letter.

'''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")