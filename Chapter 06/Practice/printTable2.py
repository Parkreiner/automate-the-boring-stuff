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

Okay, now I'm trying to put the things I saw in "Loop Like a Native" into practice. There are two obvious places where
I could improve the code:

1. The dictionary storing each longest length
2. The loop for finding the longest length in each sub-list
3. The loop for generating the formatted table


Ways (1) could be improved:
[√] 1. Replace the dictionary with a list

Ways (2) could be improved:
[√] 1. Turn the list comprehension into a generator

Ways (3) could be improved:
[√] 1. Get rid of the range(len()) constructions

---

Why I made the above changes.

(1)-1: Dictionaries feel more sophisticated, but if you're using nothing but sequential integers as your keys, then
       it's no different than a list.
(2)-1: Using a list comprehension requires that a full list be generated; this is fine for this project specifically,
       but it becomes an albatross for huge problems, as everything will need to be remembered at the same time. By
       using a generator, the computer only needs to remember one value at a time; the memory footprint is cut way down.
(3)-1: Using range(len()) is really bad in general, because it generates either a bunch of integers that aren't actually
       used, or a bunch of integers that aren't bound to the data they correspond to. Using enumerate forces the numbers
       to be bound to each piece of data.

'''

table_data1 = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

def print_table2(table):
    def list_len_generator(l):
        for i in l:
            yield len(i)

    # Determines the number of spaces between each row cell in the output
    min_margin = 4

    # Finds the longest lengths in each column
    longest_lengths = []
    for column in table:
        longest_lengths.append(max(list_len_generator(column)))

    # Generates the formatted table
    output = []
    for row in zip(*table):
        row_contents = []
        for i, cell in enumerate(row):
            row_contents.append(cell.rjust(longest_lengths[i]))

        output.append((" " * min_margin).join(row_contents))

    # Prints the table
    for row in output:
        print(row)



print_table2(table_data1)