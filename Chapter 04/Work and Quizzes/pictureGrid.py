'''
    Use the following list of lists:

    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    Which represent this 6x9 pattern:

    ......
    .OO...
    OOOO..
    OOOOO.
    .OOOOO
    OOOOO.
    OOOO..
    .OO...
    ......

    To print this 9x6 pattern:
    
    ..OO.OO..
    .OOOOOOO.
    .OOOOOOO.
    ..OOOOO..
    ...OOO...
    ....O....

    '''

'''
    Thinking:

    1. The resulting pattern is just the starting pattern rotated +90 degrees
    2. I need to start from the bottom left. Then I need to keep going up by 1 until I reach the top. Once I print the
       character there, I need to move to the bottom character of the column to the right
    3. Actually, since the pattern is symmetrical, I can start at the upper-left and then go down for each column.
    4. Because of how the grid variable is set up, its values are of the form grid[y][x].

    Starting point: grid[0][0]
    End of first column: grid[len(grid) - 1][0]
    Start of last column: grid[0][len(grid[0]) - 1]
    End of grid: grid[len(grid) - 1][len(grid[0]) - 1]
    '''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

newPattern = "\n"

for x in range(len(grid[0])):
    for y in range(len(grid)):
        newPattern += str(grid[y][x])
    newPattern += "\n"

print(newPattern)