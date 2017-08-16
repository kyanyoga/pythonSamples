#!/usr/bin/env python

A = [   "X.O",
        "XX.",
        "XOO" ]

B = [   "OO.",
        "XOX",
        "XOX"]

C = [   "OOO",
        ".XO",
        "XXX"]

D = [   "O.X",
        "XX.",
        "XOO"]

# Another Solutions: Looks like a potential to chagne the data.
# diagonalItems = []
#     diagonalItems.insert(0, ''.join(row[number] for number, row in enumerate(game_result)))
#     diagonalItems.insert(0, ''.join(row[::-1][number] for number, row in enumerate(game_result)))
#     
#     rowItems = game_result
#     colItems = zip(*game_result)
#     
#     for gameLine in chain(rowItems, colItems, diagonalItems):
#         for item, count in Counter(gameLine).items():
#             if count >= 3 and item != '.':
#                 return item
# ?
#     return 'D'

# rows + columns + diagonals
    # r = gb[:] + list(map(''.join,list(zip(*gb)) + list(zip(*[(gb[i][i],gb[i][2-i]) for i in range(3)]))))
    # return ('XXX' in r) and 'X' or ('OOO' in r) and 'O' or 'D'
    
# Mine will reduce to this:
# def checkio(data):
#     for i in range (0, 3):
#             if data[i][0] == data[i][1] == data[i][2] and data [i][0] != ".":
#                 #checking for horizontal matches
#                 return data[i][0]
#             if (data[0][i] == data[1][i] == data[2][i] and data [0][i] != "."):
#                 #checking for vertical matches
#                 return data[0][i]
#     if data[0][0] == data[1][1] == data[2][2] and data [0][0] != ".":
#             #checking for SE diagonal
#             return data[0][0]
#     if data[2][0] == data[1][1] == data [0][2] and data [2][0] != ".":
#             #checking for NE diagonal
#             return data[2][0]
#     return "D"
    
def checkio(array):
    xwin = False
    owin = False
    
    for row in array:
        if row[0] == row[1] == row[2] and row[0] != ".":
            if row[0] == 'X':
                xwin = True
            if row[0] == 'O':
                owin = True
          
    rotated_field = zip(*array)
        
    for row in rotated_field:
        if row[0] == row[1] == row[2] and row[0] != ".":
            if row[0] == 'X':
                xwin = True
            if row[0] == 'O':
                owin = True
                
    # check diagonial
    # print array[0][0] + ' ' + array[1][1] + ' ' + array[2][2]
    # print array[0][-1] + ' ' + array[1][-2] + ' ' + array[2][-3]
    if array[0][0] == array[1][1] == array[2][2] != ".":
        if array[0][0] == 'X':
                xwin = True
        if array[0][0] == 'O':
                owin = True
                
    if array[0][-1] == array[1][-2] == array[2][-3] != ".":
        if array[0][-1] == 'X':
                xwin = True
        if array[0][-1] == 'O':
                owin = True
                
    if xwin and owin:
        return 'D'
    if xwin==False and owin==False:
        return 'D'
    if xwin:
        return 'X'
    if owin:
        return 'O'
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print "Testing..."
    # print checkio(A)
    # print checkio(B)
    # print checkio(C)
    print checkio(D)
    print "done Testing..."
    