'''
This is basically how the .center() method works.

There are three cases:
1. The amount of needed padding is even
2. The amount of needed padding is odd and the length of the original string is even
3. The amount of needed padding is odd and the length of the original string is odd

Had trouble deciding whether to consolidate that "else if" into an "elif", but I think that the current way makes it
more obvious that the if within the else is checking for an entirely different value.
'''

def my_center(s, new_length, c=" "):
    s_length = len(s)
    difference = new_length - s_length

    if difference > 0:
        if difference % 2 == 0:
            left = difference // 2
            right = left
        else:
            if s_length % 2 == 0:
                right = difference // 2
                left = right + 1
            else:
                left = difference // 2
                right = left + 1
        return c * left + s + c * right
    return s

test = "Boy howdy!" # Length of 10
odd_test = test[:-1]

print("Mine:")
print(my_center(test, 20, "-")) # Case 1
print(my_center(test, 21, "-")) # Case 2
print(my_center(odd_test, 20, "-")) # Case 3

print("\nDefault:")
print(test.center(20, "-"))
print(test.center(21, "-"))
print(odd_test.center(20, "-"))