import sys

while True:
    userInput = input('Input "exit" to exit: ')
    if userInput.upper() == "EXIT":
        print("Exiting.")
        sys.exit()
    print('Incorrect input. You typed "' + userInput + '".')