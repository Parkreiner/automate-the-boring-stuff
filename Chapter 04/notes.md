# Chapter 4 Notes

## The List Data Type
Lists are interesting, as unlike a language like C, Python allows you to put multiple data types in the same list.

However, using a list index that lies outside the list will result in an error.

## Negative Indexes
Python allows you to use negative indexes, which refer to elements in the list, starting from the right. So, -1 will
refer to the very last element, -2 will refer to the element to the left of that, and so on.

Basically, think of negative index values as being the length of the array plus that negative value. So, in an array of
length 5, an index of -1 will subtract 1 from the length, resulting in 4. The highest index in the array is 4, so the
value at that index gets printed.

## Getting Sublists with Slices
A slice allows you to get multiple values from a list by turning them into a new list. The notation is pretty similar to
basic array or list notation – you’re using integers as indexes – but you need two integers, separated by a colon.

And just like with the range function, the first value will be included, but not the second one. It’ll count up to that
value.

You can also omit values in the slice. You can omit both values, but that’s the equivalent of the original array. If you
omit the first value, that’s equivalent to setting it to 0. If you omit the second value, that’s equivalent to setting
it to the length of the array.

### Using slices to create separate copies of lists
You would think that omitting both values would be pointless, as that would just be equivalent to the original list, but
that's exactly the point. By default, `newList = originalList` will just have `newList` point at `originalList`. So, any
operations performed on the former will actually be done on the latter. Since slices return new lists instead of
modifying the original, `newList = originalList[:]` will give `newList` a separate copy of the original list, instead of
just a reference.

## List Concatenation and List Replication
When you use the `+` and `*` operators on lists, it’s not that different from using them on strings.

Using `+` will create a new combined array:
```python
>>> print([0, 1, 2] + [3, 4, 5])
[0, 1, 2, 3, 4, 5]
```

Using `*` will add multiple copies of that array to itself.
```python
>>> [0, 1] * 3
[0, 1, 0, 1, 0, 1]
```

## Using the `del` keyword for List Items and regular variables
You can use the `del` keyword to delete an element at a specific index of a list. When you do, any elements that came
after will be moved up one index.

You can also use it to delete an actual variable. All further references to that variable will result in a `NameError`
– it will be as if that variable never existed.

## Working with Lists
Whenever you catch yourself making very similar variables, either in function or theme, then you might want to consider
turning them into a list.
```python
catName1 = 'Zophie'
catName2 = 'Pooka'
catName3 = 'Simon'
catName4 = 'Lady Macbeth'
catName5 = 'Fat-tail'
catName6 = 'Miss Cleo'
```

The above can easily be turned into a list of cat names. And if the order of the names ever matters, you can do a lot
more with lists than with unconnected variables. Plus, there is a number of problems with that implementation:
* No easy way to add extra cat names
* Writing repetitive code like this almost always results in repetitive code elsewhere, particular code that handles it

Getting user input for all those cats would be a huge hassle, but when you use a list, you can approach things more
programmatically, even including support for an arbitrary number of cats:
```python
catNames = []
while True:
    print(f"Enter the name of cat {len(catNames) + 1} (or just press Enter to stop): ", end="")
    name = input()

    if name == "":
        break
    
    catNames = catNames.append(name)

print("The names of all the cats are:")
for name in catNames:
    print(name)
```

## Using `for` loops with lists
So, it seems that technically, the `for` keyword *only* works on lists and list-like values. When you do something like
`for i in range(3)`, that `range(3)` is creating a new list-like value. `for i in [0, 1, 2]` has the exact same
functionality.

**The technical term for the "list-like value" the author keeps referring to is a sequence**, but it doesn't seem like
the book goes into them in too much depth.

Perhaps the most common use for looping over a list is doing something with the value at each index:
```python
x = [0, 1, 2]
for i in range(len(x)):
    # Do something with x[i]
```

The above form is useful when you need to refer to the indexes of each item, but when you don't, you can also use this
more straight-forward form:
```python
x = ["A", "B", "C"]
for i in x:
    print(i) # Can access the values in order, but it's basically impossible to use math with them
```

## The `in` and `not in` operators
The `in` and `not in`* operators are quick and convenient ways of checking if a value exists within a list. Both return
boolean values.

```python
>>> junk = ["Boy", "Howdy", "Eat my bacon", "Mars is not a planet"]
>>> "Boy" in junk
True
```
\* It seems that `not in` just exists for convenience. `a not in b` should be equal to `not (a in b)`.

## The multiple assignment trick
Python provides a very convenient shorthand if you're pulling values from a list to assign to variables. However, the
length of the list must be equal to the number of variables being assigned.

Instead of this:
```python
letters = ["A", "B", "C"]
x = letters[0]
y = letters[1]
z = letters[2]
```

You can do this:
```python
letters = ["A", "B", "C"]
x, y, z = letters
```

But these won't work:
```python
letters = ["A", "B", "C"]
x, y = letters

letters = ["A", "B"]
x, y, z = letters
```

And just in general, you can use multiple assignment to swap values of variables
```python
>>> a, b = "Alice", "Bob"
>>> a, b = b, a
>>> print(a)
"Bob"
>>> print(b)
"Alice"
```

## Augmented Assignment Operators
Augmented assignment operators provide shorthand for updating an existing value. However, Python does not support `++`
or `--` notation, though it does support literally everything else. It even has an augmented operator for integer
division, which is more than JS can say.

#### The operators
* `x += y`
* `x -= y`
* `x *= y`
* `x /= y`
* `x //= y`
* `x %= y`

You can even use `+=` and `*=` on strings and lists. They'll do concatenation and replication, respectively.

## Methods
A method is just a function that belongs to a value and that can be called in terms of that value. For example, the
`index()` method in `exampleList.index("value that you want to find the index of")`. All primitives have their own
methods, all of which are designed to make manipulating those primitives easier.

## Finding a value with the `index()` method
The `.index()` method allows you to find the index where a value is placed in a list. If the value exists in the list,
then the method will return an integer equal to the index. If it doesn't exist, then the method won't return something
like `-1`; it'll just give you a `ValueError`.

If the value you're looking for appears multiple times, then the method will just return the first index where it can be
found.

## Adding values to lists with the `.append()` and `.insert()` methods
The `.append()` method is basically the same as running the `+=` operator on a list. However, there is a slight
difference. `[1] + [2]` results in `[1, 2]` – the values from the second list are plucked out and placed at the end of
the first one. However, `[1].append([2])` results in `[1, [2]]` – the second list is kept intact, and the entire thing
gets appended to the end.

The `.insert()` method, in turn, is very close to the `.append()` method; the only difference is that it lets you place
new values at a specific index. If you choose an index that already has a value, then the value you're adding will get
put there, while the element that used to be at that location and everything else will get bumped to the right one
index. This does mean that it needs two values.

```python
>>> [1, 2].insert(0, 12) # Inserts 12 at index 0, pushing all following elements to the right by 1 index
[12, 1, 2]
```

**Just make sure to never do this**
```python
>>> example = example.append("Some text")
>>> example = example.insert(0, "Some other text")
```
The methods themselves don't have return values. That's because they modify the original list instead of creating a new
one. If you try to set a variable to one of these methods, you'll get a value of `None`.

Also, these methods are exclusive to lists. If you try using them on other value types, you'll get an `AttributeError`.

## Removing values from lists with `.remove()`
The list `.remove()` method is basically a more sophisticated version of using `del`. It doesn't require you to know the
specific index of a value – only that it exists somewhere in the list variable.

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove("bat")
>>> spam
["cat", "rat", "elephant"]
```

If you try removing a value that does not exist, you'll get a `ValueError`. On the flipside, removing a value that
appears multiple times will only remove the first instance.

### `.remove()` vs `del`
Both operations are great for deleting values, but they do have different uses. `del` is great when you know the index
of the value you want to delete, but not necessarily what that value is. `.remove()` is great when you know what value
you want to delete, but not necessarily where it's located (though things do get muddier when you have multiple
instances of the same value in an array).

## Sorting list elements with `.sort()`
The `.sort()` method allows you to arrange list elements of a similar type "in order" and in place. For numerical
values, this will arrange them from least to greatest. For alphabetical elements, they'll be sorted lexicographically*.
However, you can't use the method when your list contains a variety of values, such as numbers and strings.

You can even use the `.sort()` method on a list of lists, so long as all the sub-lists contain elements of the same
type. The method will just sort the sub-lists based on their first element. If two or more sub-lists have the same first
element, then the method will look at the next element in each until it finds a mismatch. If you throw an empty list
inside the list of lists you're trying to sort, then it will always be considered first.

You can also make the method return your elements in reverse order through the `reverse=True` argument.
```python
>>> [1, 2, 3].sort(reverse=True)
[3, 2, 1]
```

### Overriding default lexicographic order
Just as a reminder, in lexicographic order, uppercase letters come before lowercase ones. This means that you'll get
this when you have a mix of string cases:
```python
>>> ["A", "a", "B", "b", "C", "c"].sort()
["A", "B", "C", "a", "b", "c"]
```

However, Python does provide a work-around. It doesn't overwrite lexicographic order to place lowercase elements before
uppercase ones, but it does keep strings that start with the same letter together, no matter the case. All you need to
do is pass the method an argument of `key=str.lower`. This will cause Python to treat all of the elements as being in
all-lowercase while it's sorting.

```python
>>> test1 = ["A", "a", "B", "c", "C", "b"]
>>> test1.sort(key=str.lower)
['A', 'a', 'B', 'b', 'c', 'C']

>>> test2 = ["Ab", "aB", "AB", "ab"]
>>> test2.sort(key=str.lower)
['Ab', 'aB', 'AB', 'ab']
```

## Example Program