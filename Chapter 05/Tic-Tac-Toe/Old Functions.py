# This function checked for whether there were still any empty spaces
def is_still_winnable():
        for row in board.values():
            for column in row.values():
                if column == "•":
                    return
        return "DRAW"

# Much more elegant version that
def is_draw():
    for i in board_list:
        if i == "•":
            return
    return "DRAW"