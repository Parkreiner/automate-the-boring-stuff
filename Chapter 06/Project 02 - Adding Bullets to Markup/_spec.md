# Project 2 - Adding Bullets to Markup

Okay, so the goal of this program seems pretty simple. You just want to make a script that reads the text stored in
your clipboard, modifies it to place an asterisk before each line (which is how Wikipedia denotes bullets), and then
copy the result back to the clipboard.

## Thinking

1. Read the input from the clipboard
2. Split the text into an list by newline characters
3. Append an asterisk to the end of each element in the list
4. Rejoin the list and copy it to the clipboard