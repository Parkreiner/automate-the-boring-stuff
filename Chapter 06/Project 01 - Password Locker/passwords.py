#!/usr/bin/env python3

'''
This is a simplified implementation of a password manager

Also, it isn't necessary to store sys.argv[1] inside the account variable; it just makes things more readable.
'''

# Dictionary of passwords
PASSWORDS = {
    "email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
    "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
    "bank": "password1234"
}

import sys, pyperclip

# Check that the right number of arguments was passed in
if len(sys.argv) != 2:
    print("USAGE: python passwords.py <account type you want the password for>")
    sys.exit(1)

# Check for whether account exists in password dictionary
account = sys.argv[1]
if account not in PASSWORDS:
    print(f'ERROR: "{account}" not found in list of accounts. Please try again.')
    sys.exit(1)

# Copy the password to the user's clipboard and print a message acknowledging that
pyperclip.copy(PASSWORDS[account])
print(f'The password for "{account}" has been copied to your clipboard.')
sys.exit(0)