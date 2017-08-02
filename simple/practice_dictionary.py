#!/usr/bin/env python

# Dictionary (HashMap) - Or just a map
'''
dict = {}       #"Define an empty Dictionary"
dict[x]         #"Return value for key x"
dict[x] = 1     # "Set value for key x to 1"
dict.keys()     #"Return list of keys"
'''

#manual dictionary
my_dict = {'Kelly' : '333-111-4444', 'Mark': '999-444-2222', 'John': '555-222-3333'}

print my_dict
 
print my_dict.keys()
print my_dict.values()
print my_dict.has_key('Kelly')


print my_dict['Mark']
my_dict['Mark'] = '888-444-2222'
print my_dict['Mark']


