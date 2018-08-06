# Dictionaries

## Structure

In Python, dictionaries are not ordered. This means that while you might have defined a set of key-value pairs in a
specific order, there's no guarantee that that order will be preserved when you work with it.

## Dictionary methods

### Methods handy for looping

#### The `.keys()` method

`.keys()` allows you to retrieve all the keys within the dictionary you call this method for. This set of keys will be
returned as something called a view object.

Python automatically calls this method if you try using a `for` loop on a dictionary. These two are equivalent:

```python
for i in x:
    # Code
```

```python
for i in x.keys():
    # Code
```

#### The `.values()` method

`.values()` is exactly like `.keys()`, except that it returns a view object of a dictionary's values. There is no way
to call this implicitly.

#### The `.items()` method

`.items()` is basically a combination of `.keys()` and `.values()`, returning a view object full of key-value tuples.
Like with `.values()`, there is no way of calling this implicitly.

When you use `.items()` in a loop, you can either use one storage value or two. If you use one, it will be set to the
tuple. But if you use two, the first will set set to the tuple's key, while the second will be set to the tuple's value.

```python
for key, value in x:
    # Code
```

#### Turning `.keys()`, `.values()`, or `.items()` into true lists

As mentioned earlier, all the above methods return a view object. If you want to turn these into true lists, you'll
have to use the `list()` function.

```python
>>> x = {
    "a": 1,
    "b": 2
}
>>> print(list(x.items()))
[("a", 1), ("b", 2)]
```

### Methods handy for accessing and manipulating values

#### The `.get()` method

It can get tedious to check for whether a value exists over and over again, especially since referencing a key that
doesn't exist results in a `KeyError`. This is why Python provides the `.get()` method. It allows you to check for
whether a key exists. If it does, the method will return the key's value. If it doesn't, it'll either return `None` or
an optional value.

```python
>>> picnicItems = {"apples": 5, "cups": 2}
>>> print(f"There are {str(picnicItems.get("apples", 0)} apples.")
There are 5 apples.
>>> print(f"There are {str(picnicItems.get("blueberries", 0)} blueberries.")
There are 0 blueberries.
>>> picnicItem.get("oranges")
None
```

#### The `.setdefault()` method

`.setdefault()` allows you to check for whether a key exists. If it does, the method will return that key's value. If
it doesn't, it will add that key to the dictionary, along with a value that you define. If this happens, the method will
then return that value you defined.

Sample code that counts the number instances of each character within a string:

```python
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
```

### Outputting dictionaries

#### `pprint.pprint()`

The `.pprint()` method allows you to print dictionary values in an aesthetically-pleasing way, sorting them when
necessary. The sort order seems to be as follows:

1. Punctuation and spaces
2. Numbers
3. Uppercase letters
4. Lowercase letters
5. Other stuff(???)

However, it's important to note that `.pprint()` only breaks output across multiple lines when it can't everything
within a defined width. By default, this is the width of the terminal, but you can also set custom widths with an
argument like `width=80`. If you want to force everything to be printed across multiple lines, use `width=1`. This will
cause every single key-value pair to trip the width limit, but the function won't break the pairs themselves*.

Example:

```python
import pprint
x = {"a": 1, "b": 2, "c": 3, "d": 4}
pprint.pprint(x) # Prints {"a": 1, "b": 2, "c": 3, "d": 4} on a single line
pprint.pprint(x, width=1)
'''
Prints x like so:
{"a": 1,
"b": 2,
"c": 3,
"d": 4}
'''
```

\* There is an exception, though. If you use `width=1` on a dictionary that contains a string value comprised of
multiple characters separated by spaces, that string will be broken up at each space.

#### `pprint.pformat()`

This is basically `pprint()`, except that it returns the output as a string, instead of printing it to the terminal.
Using `print()` on the return value of this method is the same as just called `.pprint()`.