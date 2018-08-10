# Chapter 6 – Manipulating Strings

It seems that most if not all of the concepts that applied to lists also apply to strings. That makes sense, as strings
are just arrays of characters. However, it seems that Python also supports some more high-level tricks, such as
accessing the operating system's clipboard.

## Working with strings

### String literals

A string literal is any value contained within quotation marks. However, using them does require some care, as placing
quotation marks inside a string risks terminating the literal early. One way of getting around this is using double
quotes when you know your string contains only single quotes, and vice-versa, but that's far from perfect. Luckily,
Python provides a number of ways to type strings.

#### Escape Characters

Escaping characters allows you to force the interpreter to process a character as part of a string, rather than as part
of the language. To escape a character (as long as it's not a letter), just use `\`, followed by the character. For
example, the below string escapes the `'` in `I'm` to prevent it from terminating the string early:

```python
>>> x = 'Here is an example string that I\'m making.'
```

Here are some of the more common escape characters:

* `\'` - Single quote
* `\"` - Double quote
* `\t` - Tab
* `\n` - New line
* `\\` - Backslash

#### Raw Strings

Python allows you to turn a string into a raw string by placing the character `r` just before it. Basically, it behaves
as a regular string in most contexts, except for when it needs to be printed. When it's time for a raw string to be
printed, the `print` function will interpret it exactly as it is written, meaning, for example, that if it encounters a
`\n`, it won't turn that into a line break, but keep it as "backslash-n".

Just be careful; it seems that raw strings are good for supporting regular expressions, but it seems that regular
expressions use a `.` to denote certain things. That means that if you use a raw string, you'll have to use `\.`.

```python
>>> r"\"What a cool string this is\", I thought as I typed garbage into the computer\."
```

#### Multi-line strings with triple quotes

Triple quotes are yet another way of formatting strings. Like regular quotes, you can enclose them with single-quotes or
double quotes, but whichever one you choose, you need three on both ends. Any characters contained within triple quotes
will be treated as part of the string, including actual line breaks. Inserting real line breaks into normal strings
doesn't work, as it results in an `EOL` error, but it's perfectly fine for triple-quote strings.

Also, because triple-quote strings are enclosed within three quotation marks on both sides, it can't get confused by
singleton single or double quotes. That means that you don't have to escape them.

## Indexing and slicing strings

Slices for strings work exactly how they do for lists. This means that you can access sets of characters that start and
end at any arbitrary points.

```python
>>> x = "Example string"
>>> x[1:5]
xamp
>>> x[2:]
ample string
>>> x[:2]
Ex
```

Just remember that for all slices, the second value in the range (if it's defined) is excluded. Also, slices don't
modify the original string (unless you set the variable that holds it to the slice).

## The `in` and `not in` operators for strings

You can also use `in` and `not in` for strings, though unlike their usage for lists, you can search for a sequence of
values. For example, `"string" in "test string"` will check for whether the sequence `"string"` exists within
`"test string"`. It doesn't check for the presence of all individual letters; the only way the expression will evaluate
to `True` is if the characters exist in that specific sequence.

This difference in how `in` and `not in` function for lists vs strings makes each suited to different uses. For example,
if you want to check to see if a list contains a specific sequence of values, you can convert it into a string and then
search for that sequence.

## Useful string methods

### `.upper()`, `.lower()`, and `.title()`

Python provides a set of methods for quickly transforming parts of a string to match a certain case. When you call the
following three on a string, they will return **a copy** of the string that has been formatted in some way.

* `.upper()` - Returns the string, but it's all-uppercase
* `.lower()` - Returns the string, but it's all-lowercase
* `title()` - Returns the string, except that the first letter of each "word" will be uppercase, while all other letters
    will be lowercase.

### The "`isX()`" methods

Python also provides boolean methods for determining whether the string matches a given format:

* `isupper()` - Returns `True` if every character is uppercase and `False` otherwise
* `islower()` - Returns `True` if every character is lowercase and `False` otherwise
* `istitle()` - Returns `True` if the first letter of each "word" is uppercase with all others being lowercase and
    `False` otherwise
* `isalpha()` - Returns `True` if the string contains nothing but alphabetic characters
* `isalnum()` - Returns `True` if the string contains nothing but alphanumeric characters
* `isdecimal()` - Returns `True` if the string contains nothing but numerical characters
* `isspace()` - Returns `True` if the string contains nothing but whitespace characters (spaces, tabs, etc.)

However, if you try applying any of the above boolean methods to an empty string, it will return `False`.

### `startswith()` and `endswith()`

The `startswith()` and `endswith()` functions allow you to check for whether a sub-string exists at the start or end
of another string, respectively.

```python
>>> "Test string".startswith("Test")
True
>>> "Cool beans".endswith("s")
True
"Jeff Bezos is a piece of shit.".endswith("and I wish him a truly good day")
False
```

## `join()` and `split()`

The `.join()` method allows you to combine an array of strings into a single string, each each string being joined by
another string that you define. However, the method doesn't get called on the list; instead, it gets called on the
string you want to use as a connector. The array that you want stitched together then gets passed as an argument.

```python
>>> x = ["a", "b", "c"]
>>> print(" ".join(x))
a b c
```

The `.split()` method is the opposite, in almost every way. It splits a string into into an array, based on a delimiter,
but you call it on the string you want to split and pass the delimiter in as an argument.

```python
>>> x = "Cool, cool, and more cool"
>>> print(x.split(", "))
["Cool", "cool", "and more cool"]
>>> x = "The dopest shit around"
>>> print(x.split())
["The", "dopest", "shit", "around"]
```

As the above example showcases, calling `.split()` without an argument will make the method default to using whitespace
characters as the delimiters, not just spaces.

If you decide to use the `.split()` method on a string that uses triple quotes, every whitespace character aside from
spaces that's within it will map to the default escape character. So, if you have a string that has a lot of new lines,
you just have to use `\n` as the delimiter.

The book's example:

```python
>>> spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
>>> spam.split('\n')
['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the fridge',
'that is labeled "Milk Experiment".', '', 'Please do not drink it.', 'Sincerely,', 'Bob']
```

## Justifying text with `.rjust()` `.ljust()`, and `.center()`

The `.rjust()`, `ljust()`, and `.center()` methods provide a basic way of justifying text. That is, they just insert a
bunch of padding spaces.

Look at this example:

```python
>>> x = "'Sup, my man"
>>> print(x.rjust(20))
"        'Sup, my man"
```

`.rjust()` looks at its numerical argument and then at the length of the string it was called on. It adds padding zeros
until the length of the new string equals the argument. In the above example, `"'Sup, my man"` is `12` characters long,
so `.rjust()` will add `8` characters to make the resulting string `20` characters long. `.ljust()` and `.center()`
behave similarly, with `.ljust()` adding spaces to the right of the string, and `.center()` adding spaces to both sides.

For all of these, there is also an optional second argument that you can add. This defines the single character that you
want to add as padding instead of a space. However, the character **must** be a single character, or else you'll get a
`TypeError`.

This works:

```python
>>> x = "Cool"
>>> print(x.rjust(20, "-"))
```

This doesn't:

```python
>>> x = "Cool"
>>> print(x.rjust(20, "+-"))
```

Also, if the requested padded string length is longer than the original string, the methods will just return the

### How padding gets added

`.center()` behaves differently based on the requested length of the padded string and the length of the original string
that the padding is getting added to.

Basically, the number of padding characters gets split across both sides, but when you have an odd number to add, there
will be one character left over. That character will go on the right if the original string's length is odd but will go
on the left if the original string's length is even. Why it's not consistent, I have no idea.

## Removing whitespace with `.strip()`, `.rstrip()`, and `.lstrip()`

The `.strip`, `.rstrip()`, and `.lstrip()` methods all allow you to **remove** certain characters from strings.
`.lstrip()` will remove from the left of the string, `.rstrip()` will remove from the right, and `.strip()` will remove
from both sides.

By default, these functions will remove whitespace characters, but you can also define sequences of characters (via
strings) that you want to remove. However, the curious thing is that the methods will remove all instances of the
sequence, as well as its reverse:

```python
>>> x = "SpamSpamSpamBaconSpamEggsSpamSpammapS"
>>> print(x.strip("mapS"))
BaconSpamEggs
```

Even though the string `"mapS"` only appears once (at the very end of `x`), the `.strip()` method will also remove all
instances of its reverse – that is, `"Spam"`. So, for this specific example, `print(x.strip("Spam"))` would still print
the same string.

## Accessing the clipboard via the `pyperclip` module

The `pyperclip` module contains methods `copy()` and `paste()` that allow you to copy text to and from your computer's
clipboard. However, it does come come installed by default. Once a module is installed, you can import it into a script
just how you would for any built-in module: `import <module name>`.

`pyperclip.copy(<Some string>)` will copy that string to your clipboard. `pyperclip.paste()` will paste the clipboard's
contents. However, just be aware that your Python interpreter won't have exclusive access to the clipboard; any other
program could modify it, which is something to keep in mind if you copy to and from the clipboard within the same
script.

There are also two more things to be aware of, specifically for `.paste()`:

1. It doesn't print anything; it just returns a string if it can.
2. If the clipboard contains something other than just text, the method will return an empty string.

## Running Python scripts outside of IDLE

So apparently the book has expected you to run all Python scripts through IDLE up until this point. There's an appendix
entry on how to get something better, but there's a good chance that it'll just give me information I already knew. I
don't get why any experienced developer would use IDLE, though; it doesn't even support command-line arguments.