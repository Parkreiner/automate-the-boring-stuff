# The point of this program is to implement the collatz sequence

# Prints collatz sequence of an integer
def printCollatz (number):
    while number != 1:
        if number % 2 == 0:
            print(number)
            number //= 2
        else:
            print(number)
            number = number * 3 + 1
    print(number)

# Gets user integer
while True:
    try:
        startingNumber = int(input("Please input an integer (it can be of any size): "))
        break
    except:
        print("Not a number. Gonna need an integer.")

printCollatz(startingNumber)