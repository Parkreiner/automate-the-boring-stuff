# Chapter 5: Dictionaries and Structuring Data

## The Dictionary Data Type

Like lists, dictionaries are a tool for grouping and organizing data. Unlike lists, however, dictionaries don't order
elements sequentially, as dictionary index values (these are called keys) can be more than just integers. A pair of a
dictionary key and the value it corresponds to is called a key-value pair.

In Python, all dictionaries are denoted with braces `{ }`. Here's an example:

```python
myCat = {
    "size": "fat",
    "color": "gray",
    "disposition": "loud"
}
```

You can then access the dictionary values through bracket notation, just like with lists:

```python
>>>"My cat is so " + myCat["size"] + "."
"My cat is so fat."
```

But as mentioned earlier, dictionary keys can be more than integers, meaning they you can still just use integers for
your key values. But since dictionaries aren't sequential, you don't have to start counting at `0` and can jump around
for each key.

## Dictionaries vs Lists

Dictionaries are not ordered. So, even if a dictionary has a key that's equal to `0`, that's not the first value,
because there is no "first value". Likewise, two dictionaries are equal if they have the same key-value pairs. It
doesn't matter what order they appear in.

```python
>>>eggs = {
    "name": "Zophie",
    "species": "Cat",
    "age": 8
}
>>> ham = {
    "species": "Cat",
    "age": 8,
    "name": "Zophie"
}
>>> eggs == ham
True
```

There's more. Because dictionaries can't be ordered, it's impossible to take a slice of them. And finally, trying to
access a value through a key that doesn't exist within the dictionary results in a `KeyError` message, much like the
`IndexError` message for lists.

Dictionaries are incredibly powerful, as they allow you to pair and organize information in meaningful ways. Take this
code, for example:

```python
# List of birthdays, as defined by the first name of the people who have them
birthdays = {
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar 4"
}

while True:
    name = input("Enter the name of the person whose birthday you would like to display (or just press Enter to exit): ")
    if name == "":
        break

    # Ensures that only the first letter is uppercase
    name = name[0].upper() + name[1:].lower()

    # Adds ' to end of name if it ends in s; otherwise makes it end in 's
    possessive = "'" if (name[len(name) - 1] == "s") else "'s"

    if name in birthdays:
        print(f'{name}{possessive} birthday falls on {birthdays[name]}.')
    else:
        print(f"I do not have {name}{possessive} birthday on file. Please enter their birthday (three-letter month " +
               "followed by day) or press Enter to quit: ", end="")

        bday = input()

        if bday == "":
            break

        birthdays[name] = bday
        print(f"Database updated. {name}{possessive} birthday is listed as {birthdays[name]}.")
```

## The `.keys()`, `.values()`, and `.items()` methods

Python provides three methods for turning a dictionary into a list-like value (in this case, objects called view
objects). Note that these won't be true lists, meaning that they won't have a lot of basic list functionality, such as
support for the `.append()` method or immutability. However, they can be used in `for` loops.

The methods each return a unique sequence type, all of which are listed below:

* `.keys()` - Returns `dict_keys` view object containing all keys within the dictionary
* `.values()` - Returns `dict_values` view object containing all values within the dictionary
* `.items()` - Returns `dict_items` view object containing tuples of each key-value pair within the dictionary

An example:

```python
>>> spam = {
>>>    "color": "red",
>>>    "age": 42
>>> }
>>> for values in spam:
>>>     print(values)

"red"
42
```

Note that **if you iterate over a dictionary without any of these methods, `.keys()` will be called implicitly**.

### Turning the view objects into true lists

In order to turn the return values of the above methods into a true list (meaning a value that's mutable and will
support other methods like `.append()`), you need to use the `list()` function.

```python
>>> spam = { "color": "Red", "age": 42 }
>>> spam.keys()
dict_keys(["color", "age"])

>>> list(spam.keys())
["color", "age"]
```

### Multiple variable assignment trick for `.items()` method

If you use two variables in a `for` loop that iterates over the return value of a dictionary's `.items()` method,
then each one will correspond to a different value in the tuple.

```python
>>> spam = { "color": "Red", "age": 42 }
>>> for keys, values in spam.items():
        print(f'Key: {keys} | Value: {values}')
'Key: "color" | Value: "Red"'
'Key: "age" | Value: 42`
```

## Checking whether a key or value exists within a dictionary

You can use the `in` and `not in` operators to check whether a value is contained within a dictionary. If you use these
operators on the dictionary with no other modifications, then the `.keys()` function will be called by default, allowing
to comb through the dictionary's keys. But you can also call `.keys()` explicitly. What's more, you can use `.values()`
to check whether a value is inside a dictionary.

```python
>>> example = {1: "A", 2: "B", 26: "Z"}
>>> print(1 in example)
True
>>> print(26 in example.keys())
True
>>> print("Z" not in example.values())
True
```

## The `.get()` method

As mentioned earlier, trying to use a key that doesn't exist inside a dictionary will result in a `KeyError`. But
checking whether a key exists can get tedious. This is why Python provides the `.get()` method. This method takes two
arguments: the key you want to check for and the value you want to use if the key doesn't exist.

Check this out:

```python
>>> picnicItems = {"apples": 5, "cups": 2}
>>> print(f"I am bringing {str(picnicItems.get('cups', 0))} cup(s).")
"I am bringing 2 cups".
>>> print(f"I am bringing {str(picnicItems.get("eggs", 0))} egg(s).")
"I am bringing 0 eggs."
```

Had you not used `.get()`, the second print statement would've resulted in a `KeyError`.

## The `.setdefault()` method

Sometimes you need to check for whether a key exists within a dictionary, and if it doesn't, add it and a value to that
dictionary. It's not hard to do with normal Python:

```python
>>> cat = {"name": "George", "age": 741}
>>> if "color" not in spam:
        spam["color"] = "Petrified white"
>>> cat["color"]
"Petrified white"
```

But the `.setdefault()` method not only lets you do all that in a single line of code, but it also returns the value of
the key if it does exist. If `.setdefault()` does end up setting a key value, then it'll return that value.

```python
>>> cat = {"name": "George", "age": 741}
>>> cat.setdefault("name", "Joey Joe Joe")
"George"

>>> cat.setdefault("color", "Petrified white")
"Petrified white"
```

`.setdefault()` is a pretty handy shortcut, as it allows you to check for whether a value exists right before trying to
reference it. Take this code for example:

```python
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
```

It counts the number of instances of each character in a string. If the character is not part of the dictionary yet,
then it gets added as a key with a value of `0`. Then, right after that, the key that corresponds to the character gets
its value incremented by `1` no matter what.

## Pretty Printing

Importing the `pprint` module gives you access to the `pprint()` and `pformat()` functions. Both are designed to print
dictionary values in a more aesthetically-pleasing way. With `pprint()`, not only will each key-value pair be on a
separate line, but by default, they'll even be sorted, with different marks being sorted in this order:

1. Punctuation and spaces
2. Numbers
3. Uppercase letters
4. Lowercase letters
5. Other stuff(???)

However, something very important to note is that `pprint()` tries printing everything on a single line, and will only
print values across multiple lines when it can't. One way around this is by defining the function's `width` argument,
setting it to 1. `width` basically acts as a threshold for what causes line breaks. If you call `pprint(width=80)`, the
values will only break if the resulting string would exceed `80` characters in length. If you set it to `1`, though,
every single line will trip the threshold, but the values themselves won't get broken up. This effectively prints each
value on a new line, regardless of length.

`pformat` is basically `pprint()` without the printing part. It generates the string that would be printed but returns
it as a value. This means that `print(pprint.pformat(exampleVariable, width=1))` is equal to
`pprint.pprint(exampleVariable, width=1)`.

## Using Data Structures to Model Real-World Things

Way before the internet, it was possible to play games like chess with people from across the world. It basically
involved mailing a postcard with the move that you wanted to make to your opponent, so they could make that change on
their board. Of course, doing this required a way of unambiguously describing chess spaces, and so algebraic chess
notation was born.

### How algebraic chess notation works

Relative to the white player, each space is labeled with a number and a letter, with both starting at the lower-left.
The letters span horizontally, going from a–h (lowercase), while the numbers span vertically, going from 1–8. This means
that the space in the lower-left corner for the white player is `a1`. The space in the lower-left corner for the white
player is `h8`.

Each piece is also identified by a letter, all of which are listed below:

* P - Pawn
* R - Rook
* B - Bishop
* N - Knight
* Q - Queen
* K - King

To describe each turn in the game, you need two sets of instructions: one for what the white player did (they always go
first), and one for what the black player did. So, the instruction set `2. Nf3 Nc6` describes the second turn of the
game, saying that the white player's knight moved to `f3`, while the black player's knight moved to `c6`.

Still, the point is that a lot of things can be modeled via computers, though things with discrete states and steps are
a bit easier. And it just happens that lists and dictionaries are fantastic tools for doing this.

## Starting simpler: Modeling Tic-Tac-Toe

This is how the author displays their tic-tac-toe board. It does look more like a traditional tic-tac-toe board and does
let you use spaces for empty board spaces instead of bullets, but it does look kind of ugly. I think the only truly good
way of making a tic-tac-toe board would be by making a GUI.

```txt
O|O|O
-+-+-
X|X|
-+-+-
 | |X
```

Anyway, the point is, I implemented a fully functional tic-tac-toe board when that wasn't required in the book. My
approach might not be perfect, but at least I'm learning something.

## Nested dictionaries and lists

Modeling a tic-tac-toe board is easy. It only ever requires nine spaces, so things never risk getting convoluted (unless
you go out of your way to make them that way). However, as you start modeling more and more complex things, you might
find yourself making a data structure full of nested lists and dictionaries. When you do, just remember that lists and
dictionaries are better-suited to different things. Lists are good for storing data sequentially, while dictionaries are
good for associating values with each other.

Here's an example of a dictionary of dictionaries:

```python
allGuests = {
    "Alice": {"apples": 5, "pretzels": 12 },
    "Bob": { "ham Sandwiches": 3, "apples": 2 },
    "Carol": { "cups": 3, "apple pies": 1 }
}

def totalBrought():
    for guest in allGuests:
        print(f"{guest} brought", end=" ")

        item_list = list(allGuests[guests].items())

        for item_brought in len(item_list):
            print(f"{item_brought[0]}", end="")
            if item_brought == len(item_list) - 1:
                print(".")
            else:
                print(",", end=" ")
```