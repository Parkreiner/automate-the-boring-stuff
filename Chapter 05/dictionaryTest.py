import copy

# Create 3×3 board
row = {
    "left": "•",
    "middle": "•",
    "right": "•"
}
board = {
    "top": row,
    "middle": copy.copy(row),
    "bottom": copy.copy(row)
}

# Change of the spaces to be non-blank
board["bottom"]["right"] = ":P"

'''
Iterates over each row. Iterates over each space in each row for each row iteration.
'''
def checkForString(checkValue):
    for row in board.values():
        for space in row.values():
            if space == checkValue:
                return "It works!"
    return "It doesn't work!"

# Check if ":P" exists within the board
print(checkForString(":P"))
