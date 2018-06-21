# Array with a bunch of 1s, as well as other numbers
x = [1, 2, 3, 1, 1, 7, 8, 9, 1, 1, 1]
try:
    # Keeps running until there are no more values of 1, which will cause a ValueError
    while True:
        x.remove(1)
except:
    print(f"All values of 1 have been removed from x. It is now {x}.")