import pyperclip

def main():
    # Get text stored in clipboard and turn it into list
    lines = pyperclip.paste().split("\n")

    # Create new list with an asterisk in front of each non-empty line
    lines = ["* " + line if line != "\r" else line for line in lines]

    # Join list back into string
    combined = "\n".join(lines)

    # Copy modified text back to clipboard
    pyperclip.copy(combined)

    print("Your text has been formatted.")

main()