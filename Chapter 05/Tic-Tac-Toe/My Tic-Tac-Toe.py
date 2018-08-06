'''
Trying to create tic-tac-toe before going through the book's example (UPDATE: lol it turns out the book doesn't even
try to get the game working.)

MARKERS
• - Empty space
X - Player 1's mark
O - Player 2's mark

Don't know how to use objects yet, so I'm sure they would be able to help things even more

---

The code is definitely getting there. There are just two main problems:
1. I haven't implemented a good way of checking for unwinnable states yet. I just check for whether there are still
   empty spaces. If there aren't any more, and a win state hasn't happened yet, then the game obviously has to be
   unwinnable. I feel I can do more, though.
2. The code doesn't recognize input like "upper right" (instead of "upper-right"). It seems that the best way of doing
   this is by using regular expressions and the re.split() method. I know nothing about REs, though.
'''
import copy

# Board assets
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
player_marks = {
    1: "X",
    2: "O"
}

def main():
    game_over = False
    current_player = 1
    turn_number = 1

    # Display starting board state
    display_board(turn_number)
    
    while not game_over:
        # Prompt current player for move and update board based on it
        change_board(current_player)

        turn_number = turn_number + 1

        # Display updated board state
        display_board(turn_number)
        
        # Check for three-in-a-row or unwinnable board; display message if game over
        game_state = check_for_game_over()

        if game_state == "WIN":
            game_over = True
            print(f"\nCongratulations, player {current_player}. You win!\n")
        elif game_state == "DRAW":
            game_over = True
            print("\nThe game has ended in a draw. Neither player wins.\n")
        elif game_state == "EARLY DRAW":
            game_over = True
            print("\nIt is impossible for either player to win now. The game has ended in a draw.")
         
        if not game_over:
            # Swap current player
            current_player = current_player % 2 + 1

'''
Prompts the current player for the space where they would like to place their marker. It keeps pestering
them until they submit a move that both is in the proper form and hasn't been done yet.
'''
def change_board(current_player):
    '''
    Gets user's choice of space, returning it as a two-element list. The first element corresponds to the row, while the
    second element corresponds to the column. (e.g., top-middle or bottom-left).
    '''
    def get_move():
        while True:
            print(f"\nPlayer {current_player}, please input the row, followed by the column, of the space you want " +
                  f"to put an {player_marks[current_player]} in, joined by a hyphen (for example, top-right): ", end="")
            move_list = input().lower().split("-")

            # I expect people to type "upper" and "lower" pretty often
            if move_list[0] == "upper":
                move_list[0] = "top"
            elif move_list[0] == "lower":
                move_list[0] = "bottom"

            # Turns certain single-word answers into two-element lists
            if len(move_list) == 1:
                if move_list[0] == "center" or move_list[0] == "middle":
                    move_list[0] = "middle" 
                    move_list.append("middle")
                elif move_list[0] == "left" or move_list[0] == "right":
                    move_list.append(move_list[0])
                    move_list[0] = "middle"
                elif move_list[0] == "top" or move_list[0] == "bottom":
                    move_list.append("middle")

            # Determines whether the defined move is in the right format
            if len(move_list) == 2 and move_list[0] in board and move_list[1] in row:
                return move_list
            
            print("\nInvalid space.")
        
    ''' Start of change_board()'s main logic '''
    while True:
        # Prompt player n for move
        move_list = get_move()
        
        # Space on the board corresponding to the move
        desired_space = board[move_list[0]][move_list[1]]

        # Again, empty spaces are represented by bullets
        if desired_space == "•":
            board[move_list[0]][move_list[1]] = player_marks[current_player]
            return
        else:
            print("\nThat space has already been filled.", end= " ")

'''
Turns the current state of the board into a string and then prints it along with the current turn number (max 9).
'''
def display_board(turn_number):
    # Seems to be necessary only because I'm using the .values() method
    global board
    
    board_string = f"\nTURN {turn_number}:\n"
    
    for columns in board.values():
        for rows in columns.values():
            board_string = board_string + rows
        board_string = board_string + "\n"
    
    print(board_string, end="")

'''
Checks if the game has reached a point where one player has won or neither player can win (even if not all spaces are
filled).
'''
def check_for_game_over():
    '''
    Converts the board into a list and returns it.
    '''
    def make_board_list():
        board_list = []
        for row in board.values():
            for column in row.values():
                board_list.append(column)
        
        return board_list

    board_list = make_board_list()

    '''
    Determines if there is a three-in-a-row. Check ticTacToeNotes.md for more information on how this is done, but
    basically, this just checks if the symbol in one space equals the symbols in both the spaces it forms a three-in-a-
    row with. The loop helps generalize how each type of three-in-a-row gets checked.
    '''
    def is_win():
        '''
        What method is used for in each iteration:
        1 - Check for horizontal three-in-a-rows
        2 - Check for diagonal three-in-a-row from upper-right to lower-left
        3 - Check for vertical three-in-a-rows
        4 - Check for diagonal three-in-a-row from upper-left to lower-right
        '''
        for method in range(1, 5):
            if method == 1:
                start = 0
                end = 8
                increment = 3
            elif method == 2:
                start = 2
                end = 3
                increment = 1
            elif method == 3:
                start = 0
                end = 3
                increment = 1
            else:
                start == 0
                end = 1
                increment = 1
            
            for i in range(start, end, increment):
                if board_list[i] != "•":
                    if board_list[i] == board_list[i + method] and board_list[i] == board_list[i + 2 * method]:
                        return "WIN"
            
        return
    
    '''
    Determines if the current board state makes the game impossible to win for either player. A dead end is a line that
    can no longer be used to win; that is, it has both an O and and an X inside it.
    '''
    def is_draw():
        dead_end_count = 0
        empty_space_count = 0

        # Count number of empty spaces; doing this outside other loop to avoid counting spaces multiple times
        for i in board_list:
            if i == "•":
                empty_space_count = empty_space_count + 1
        
        # Count number of dead ends; structure is similar to is_win()'s
        for method in range(1, 5):
            if method == 1:
                start = 0
                end = 8
                increment = 3
            elif method == 2:
                start = 2
                end = 3
                increment = 1
            elif method == 3:
                start = 0
                end = 3
                increment = 1
            else:
                start == 0
                end = 1
                increment = 1

            for i in range(start, end, increment):
                x_count = 0
                o_count = 0

                # Iterate over each space of the three spaces within each line
                for j in range(3):
                    space = board_list[i + j * method]

                    if space == "X":
                        x_count = x_count + 1
                    elif space == "O":
                        o_count = o_count + 1
                
                if x_count > 0 and o_count > 0:
                    dead_end_count = dead_end_count + 1
        
        if empty_space_count == 0:
            return "DRAW"
        elif dead_end_count == 8 or (dead_end_count == 7 and empty_space_count == 2):
            return "EARLY DRAW"
        return

        
    return is_win() or is_draw()


main()