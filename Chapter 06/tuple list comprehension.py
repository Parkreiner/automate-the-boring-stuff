'''
This was a test to see whether list comprehensions are able to access the individual values within a list of tuples.

They totally can!
'''

x = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# In this case, a refers to each tuple within x
alt_x = [a for a in x]

# This totally works! a, b, c refers to each value within each tuple within x
summed_x = [a + b + c for a, b, c in x]

# alt_x is a shallow copy of x, while summed_x is [6, 15, 24]
print(f"{alt_x} --- {summed_x}")