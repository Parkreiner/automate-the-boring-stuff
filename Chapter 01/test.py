# Slightly more sophisticated version of a "Hello, World!" program

def main():
    print("Hello, world!")

    yourName = str(input("What is your name? "))

    if isProperName(yourName):
        print(f"Hello, {yourName}!")
    else:
        print("You didn't input a proper name!")

# Checks if user input a name. Isn't perfect, but does support spaces and apostrophes
def isProperName(text):
    exceptions = ["'", " "]
    if not text.isalpha():
        for i in text:
            for j in exceptions:
                if i == j:
                    return True
        return False
    return True

if __name__ == "__main__":
    main()