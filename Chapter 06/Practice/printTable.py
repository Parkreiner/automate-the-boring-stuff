'''
This program takes a set number of lists and prints all values at each index side-by-side, with all values right-
aligned.

Expected output for tableData1:

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose

Each sub-list within the list corresponds to a column in the output.

---

I'm going to solve this problem twice. First, I'll do it with my current skillset and toolset (including the bits and
pieces I remember from "Loop Like a Native"). Then, I'll redo the code after re-watching "Loop Like a Native" to see
exactly how much that improves it.
'''

table_data1 = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

def print_table(table):
    # Multiplies the number of spaces between each row element
    min_margin = 4

    # Finds the longest lengths in each column
    longest_lengths = []
    for i, column in enumerate(table):
        longest_lengths.append(max( [len(row) for row in column] ))

    
    '''
    I need to go back over the loop, because I was honestly swapping values around until something worked. I need to be
    able to understand why things work.

    Okay, so the table is a bit weird. The length of each sub-list corresponds to the height of the table, while the
    length of the parent list is the table's width. With the loops set up as they are now, I'm basically creating one
    row at a time. Then, when it comes time to access a specific value within a sublist, that's denoted by [j][i],
    rather than [i][j]. If the values were switched, you'd run out of bounds like 90% of the time.

    Basically, the main problem is that there's a mismatch between how the table needs to be printed (row-by-row) and
    how the data is set up (column-by-column).
    '''
    # Generate the formatted table
    output = []
    for i in range(len(table[0])):
        row = []
        for j in range(len(table)):
            row.append(table[j][i].rjust(longest_lengths[j]))

        output.append((" " * min_margin).join(row))
    
    # Print the table
    print("\n".join(output))



print_table(table_data1)