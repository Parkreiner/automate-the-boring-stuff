'''
    Comma Code
    Say you have a list value like this:

    spam = ['apples', 'bananas', 'tofu', 'cats']

    Write a function that takes a list value as an argument and returns a string with all the items separated by a comma
    and a space, with and inserted before the last item. For example, passing the previous spam list to the function
    would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed
    to it.
    '''

'''
    Thinking:

    1. I need to display an element for each and every iteration of the loop.
    2. If the number of elements is two or less, there aren't any commas at all.
    3. If the number of elements is one, then "and" isn't there, either.
    4. Everything needs to be on the same line, but I need to be sure to terminate the line once I'm done.

    Solution process:
    1. Started by calling multiple print statements. Got really convoluted, as I set one of the end values to a ternary
       operator. Explicitly checked for whether the list was only one item
    2. Realized that was dumb and simplified things more
    3. Got rid of check for whether the list was one item long. Now a single-element list will add an extra space to the
       end.
    4. Used functools to create my own print statement so that I wouldn't have to keep typing end=""
    4. Realized that it's much cleaner just to keep building up a string and then have only one print statement.
    5. Removed that extra space at the end for one-element lists
    6. Cleaned up booleans, making them more inter-connected instead of independent statements; cut number of booleans
       down from 4 to 3
    '''

# Makes it easier to change arrays for testing
one = ['apples']
two = ['apples', 'bananas']
four = ['apples', 'bananas', 'tofu', 'cats']
spam = two

# Avoids recalculating the length of spam so often
listLength = len(spam)

# String containing joined array elements
combined = ""

for i in range(listLength):
    combined += str(spam[i])

    if i < listLength - 1:
        if listLength != 2:
            combined += ","
        if i == listLength - 2:
            combined += " and"

        combined += " "

print(combined)