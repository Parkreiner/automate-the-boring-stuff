'''
Test to see just what happens when the .center() method needs to add an odd number of spaces. How does the spacing get
split up?

How many cases are there?
1. There are an even number of characters and an even padded length,
   meaning that the difference between them is even
2. There are an odd number of characters and an odd padded length,
   meaning that the difference between them is even
3. There are an odd number of characters and an even padded length,
   meaning that the difference between them is odd
4. There are an even number of characters and an odd padded length,
   meaning that the difference between them is odd

Output:
1. Even padded length and an --Even # of characters--
2. Odd padded length and an ---Odd # of characters---
3. Even padded length and an --Odd # of characters---
4. Odd padded length and an ---Even # of characters--
'''

x = "Even # of characters" # Length of 20
y = "Odd # of characters" # Length of 19

# Tests cases 1 and 4
for i in range(2):
    print(f"Padded length of {24 + i} ({'Even' if (24 + i) % 2 == 0 else 'Odd'}) and an {x.center(24 + i, '-')} ({len(x)})")

# Tests cases 2 and 3
for i in range(2):
    print(f"Padded length of {24 + i} ({'Even' if (24 + i) % 2 == 0 else 'Odd'}) and an {y.center(24 + i, '-')} ({len(y)})")