# Libraries

## Ways of calling libraries

You can either import a library by using `import <library name>` or `from <library name> import <parts of library>`.
Using the former will force you to use the library's name when referring to the specific function you want to use (so
`sys.exit()`, for example). Using the latter, however, will allow you to use the function name by itself (just
`exit()`). `import <library name>` and `from <library name> import *` are equivalent; they just differ slightly in how
you interact with the code that gets imported.

## List of libraries

### `copy`

#### `copy.copy(x)`

Creates a shallow copy of a data structure `x`.

#### `copy.deepcopy(x)`

Creates a deep copy of a data structure `x`.

### `pprint`

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

### `random`

#### `random.randint(x, y)`

This generates a random integer `n` between `a` and `b`, such that `a` <= `n` <= `b`.

### `sys`

#### `sys.exit()`

Calling `sys.exit()` allows you to terminate an entire program early.


