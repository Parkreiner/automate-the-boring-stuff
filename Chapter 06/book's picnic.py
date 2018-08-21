'''
This is the book's implementation of the formatted picnic table printing that I made in "dot leader print.py". The only
problem is that this is tailored specifically to the dictionary; throwing in super-long values doesn't make the table
expand. Still, once you move past the loop I made to calculate the proper widths for each key and value, our
implementations are almost the same.
'''

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {
    'sandwiches': 4, 
    'apples': 12, 
    'cups': 4, 
    'cookies': 8000,
    'The Michael Jordan of Drunk Driving': 5
}

printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)