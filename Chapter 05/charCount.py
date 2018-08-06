'''
Simple program that counts the number times each character appears in the string. I modified it slightly to group
uppercase and lowercase letters and to ignore spaces and punctuation.

I then modified it again to display the count values using the 
'''

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
counts = {}

for character in message.upper():
    if character.isalpha():
        counts.setdefault(character, 0)
        counts[character] = counts[character] + 1

pprint.pprint(counts)