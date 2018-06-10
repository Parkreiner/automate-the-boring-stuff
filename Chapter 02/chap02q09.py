try:
    spam = int(input("Please type an integer: "))
    if spam == 1:
        print("Hello!")
    elif spam == 2:
        print("Howdy!")
    else:
        print("Greetings!")
except:
    print("That wasn't an integer.")


