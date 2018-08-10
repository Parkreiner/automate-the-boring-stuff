# Extra

## Make string unicode

You can make a string unicode by putting a `u` in front of the quotation marks.

```python
x = u"これはペンです。日本語で・NOT・OK"
```

## Calculating the length of a number

There are a few ways:

### Just use a loop - This is O(Log n)

```python
x = 531

if x == 0:
    return 1
else:
    digit_length = 0
    while x != 0:
        x //= 10
        digit_length += 1
    return digit_length
```

### Convert to string and then find the length - Also O(Log n), apparently

```python
x = 243
x_length = len(str(x))
```

### Use log base 10 - Very fast, but breaks outside the range [-999 999 999 999 997, 999 999 999 999 997]

```python
import math

x = 374321
x = int(math.log10(x)) + 1
```

Examples that don't use code:

```txt
x = 1000
Log(10)(x) = 3, which is 1 short of the 4 digits in x

x = 357
Log(10)(x) = 2.5526
int(Log(10)(x)) = 2, which, again, is 1 short of the 3 digits in x
```

## Using `max()`

The `max()` function is very versatile. I really should learn how to use it. Just note that for all applications, you
need to compare values of the same type.

### Using it on a set of primitive arguments

You can pass a set of primitive arguments into `max()`, and it'll return the largest value. If you pass a set of numbers
in, it'll return the largest, while passing in a set of strings will return the string with the highest lexicographic
value.

### Using `max()` on a list

You can also pass a single list into `max()`. Doing so will return the largest value within the list. Just make sure
that you only pass either a list of nothing but strings or a list of nothing but numbers. God help you if you pass a
list containing booleans.

### Using `max()` on a dictionary

You can also pass a dictionary into `max()`, but like what happens when you try iterating over a dict, Python will
implicitly turn the list into a view object of the dictionary's keys. If you want to get the values, you'll have to
use `max(dictionary.values())`. Using the `.items()` method on a dictionary and then passing that in also works. It's
just that I don't think it's very useful; the tuples will be compared element-by-element. If there's a max value within
the first value of each tuple, then the corresponding tuple will be returned.

```python
test_dict = {
    "a": 3,
    "b": 2,
    "c": 1
}

# Returns ("c", 1) because of the first values in the tuples ("a", 3), ("b", 2), and ("c", 1), "c" is the greatest
# Were the tuples ("a", 3), ("a", 2), and ("a", 1), ("a", 3) would be returned
print(max(test_dict.items()))
```

### Providing a key

`max()` also supports an optional `key` argument. This specifies a function that you want to run each value through
before comparing everything. If you use `max(some_list, key=str)`, then the whole list will be turned into a list of
strings, which will then be used for the comparison instead. You could also use things like
`max(some_list, key=str.lower)` `max(some_list, key=str.upper)`.

## Pip

Pip, which stands for "Pip Installs Packages", is Python's main package manager. To install new modules, just use
`pip install <module name>`. You can then import them into your functions like you would with any of the built-in
modules.