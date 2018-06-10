import random

start = 1
end = 20
number = random.randint(start, end)

guessCount = 0

print(f"I'm thinking of an integer between {start} and {end}. Guess the number: ", end="")
while True:
    try:
        guess = int(input())
        guessCount = guessCount + 1
        
        if guess == number:
            break
        elif guess > number:
            print("Your number is a little too high. ", end="")
        else:
            print("Your number is too low. ", end="")

        print("Guess again: ", end="")
    except:
        print("That wasn't a number!")

print("You got it! It took you " + str(guessCount) + (" guesses" if guessCount != 1 else " guess") + " to figure out the number.")