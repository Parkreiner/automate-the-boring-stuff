# Questions

## Python's answers to pointers

Does Python have an equivalent to pointers? Or is there a better way of structuring this code? (Note that I haven't
gotten to learning about objects or classes yet, so I'm sure there's a better way of writing the code using them.)

Here's a simplified version of some code I'm using for a tic-tac-toe game:

```python
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

while True:
    move_list = ["middle", "right"]

    # Space on the board corresponding to the move
    desired_space = board[move_list[0]][move_list[1]]

    # Empty spaces are represented by •
    if desired_space == "•":
        board[move_list[0]][move_list[1]] = "X"
        return
    else:
        print("That space has already been filled.", end= " ")

'''
Resulting board state:
•••
••X
•••
'''
```

So, I set the value of `desired_space` to `board[move_list[0]][move_list[1]]`, but then inside the conditional, I have
to spell out that mess again. That's because using `desired_space = "X"` would modify the variable, rather than the
`board` value it copied from. Pointers would be able to solve this, as I could just point `desired_space` at the value
stored within `board` rather than copying it, but apparently Python doesn't have them.

## Is it bad to reference an array index multiple times in a conditional?

Say that I have a bunch of `if` statements, all of which use an array index in the conditional. Is it bad to use the
index over and over again, since it'll have to be dereferenced each time, or is the impact so negligible that I
shouldn't worry about it? As in, if I get to the point where this kind of performance matters, should I just consider
using a different language?

```python
# Turns certain single-word answers into two-element lists
if len(move_list) == 1:
    if move_list[0] == "center" or move_list[0] == "middle":
        # Stuff
    elif move_list[0] == "left" or move_list[0] == "right":
        # More stuff
    elif move_list[0] == "top" or move_list[0] == "bottom":
        # Even more stuff
```