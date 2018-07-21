
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

## Getting Sub-lists with Slices

A slice allows you to get multiple values from a list by turning them into a new list. The notation is pretty similar to
basic array or list notation – you’re using integers as indexes – but you need two integers, separated by a colon.

And just like with the range function, the first value will be included, but not the second one. It’ll count up to that
value.

You can also omit values in the slice. You can omit both values, but that’s the equivalent of the original array. If
you omit the first value, that’s equivalent to setting it to 0. If you omit the second value, that’s equivalent to
setting it to the length of the array.

### Using slices to create separate copies of lists

You would think that omitting both values would be pointless, as that would just be equivalent to the original list, but
that's exactly the point. By default, `newList = originalList` will have `newList` and `originalList` point at the same
value – the `=` operator will be reference-based, not value-based. So, any operations performed on one will affect both.
Since slices return new lists instead of modifying the original, `newList = originalList[:]` will have `newList` point
at a separate copy.

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

You can also use it to delete a primitive variable (that isn't inside a list). All further references to that variable
will result in a `NameError` – it will be as if that variable never existed.

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
more with lists than with unconnected variables. Plus, the above approach just has some real problems:

* No easy way to add extra cat names
* Writing repetitive code like this almost always results in repetitive code elsewhere, particularly the code that handles it

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
`for i in range(3)`, that `range(3)` is creating a new list-like value. `for i in [0, 1, 2]` works similarly.

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
    print(i) # Can access the values in order, but it's basically impossible to use math with the indexes
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

### The operators

* `x += y`
* `x -= y`
* `x *= y`
* `x /= y`
* `x //= y`
* `x %= y`

You can even use `+=` and `*=` on strings and lists. They'll do concatenation and replication, respectively.

## Methods

A method is just a function that belongs to a value and that can be called in terms of that value. For example, the
`index()` method in `exampleList.index( <value that you want to find the index of> )`. All primitives have their own
methods, all of which are designed to make manipulating those primitives easier.

## Finding a value with the `index()` method

The `.index()` method returns the value of the first index where the method's argument can be found. However, if the
argument can't be found, the method won't return `-1`.  Instead, it will give you a `ValueError`, so be careful when
using it.

## Adding values to lists with the `.append()` and `.insert()` methods

The `.append()` method is basically the same as running the `+` or `+=` operators on a list. However, there is a slight
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

**Just make sure to never do this:**

```python
>>> example = example.append("Some text")
>>> example = example.insert(0, "Some other text")
```

The methods themselves don't have return values. That's because they modify the original list instead of creating a new
one. If you try to reference a variable that was set to one of these methods, you'll get a value of `None`.

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

If you try removing a value that does not exist, you'll get a `ValueError`. On the flip side, removing a value that
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
>>> test1.sort(key=str.lower) # test1 basically becomes ["a", "a", "b", "c", "c", "b"]
['A', 'a', 'B', 'b', 'c', 'C']

>>> test2 = ["Ab", "aB", "AB", "ab"]
>>> test2.sort(key=str.lower)
['Ab', 'aB', 'AB', 'ab']
```

## Example Program: Magic 8 Ball with a Twist

This is a pretty succinct way of implementing a magic 8 ball:

```python
messages = ["It is certain.",
    "It it decidedly so.",
    "Yes, definitely",
    "Reply hazy. Try asking later.",
    "Concentrate and ask again",
    'My reply is "No".',
    "Outlook ain't too great",
    "Most doubtful"
]

print(messages[random.randint(0, len(messages) - 1)])

```

## Exceptions to Python's indenting rules

Most of the time, Python is very indentation-based. This means that code that's indented at the same level will tend to
be part of the same block. There are some exceptions, though.

For example, lists can span multiple lines and can have any amount of spacing between them. Python will know not to act
as if the list is finished until it sees the closing bracket `]`.

But there is something else. When splitting any kind of statement across multiple lines, you can use `\` to indicate
that the statement extends to the next line. Some parts of the language do this automatically, but not everything does.
`\`, when used manually, can be used with **everything**.

These two are identical:

```python
print("This code is being split across " + \
      "multiple lines.")

print("This code is being split across " + # No \ placed - Also, placing comments like this is valid Python
      "multiple lines.")
```

But these two aren't:

```python
# Works perfectly fine
if 0 == \
    0:
    print("Equal")

# Results in SyntaxError; the conditional is treated as incomplete
if 0 == 
    0:
    print("Equal")
```

## List-Like Types: Strings and Tuples

It's important to note that lists aren't the only way of ordering information. Strings, after all, are just arrays/lists
of characters. Because of this, you can apply most of the methods to strings that you can to generic lists: indexing,
slicing, iterating over them, getting their `len()`, and being used with the `in` and `not` operators.

```python
>>> name = "Bugger"
>>> "bug" in name
False
>>> "Bug" in name
True
"A" not in name
True
>>> name = "Zophie"
>>> for i in name:
>>>     print("* * * " + i.upper() + " * * *")
* * * Z * * *
* * * O * * *
* * * P * * *
* * * H * * *
* * * I * * *
* * * E * * *
```

## Mutable and Immutable Data Types

However, even though strings are basically lists, they don't behave exactly the same. In C, all arrays are immutable,
both regular arrays and strings. But even though the creators of Python modified arrays to be mutable when they turned
them into lists, they didn't do the same for strings. So there's a bit of an inconsistency: strings are not mutable
under any circumstances. Try to change a character, and you'll get a `TypeError` back.

If you want to modify a string, you'll have to slice the parts you want to keep and combine them with the parts you want
to add.

```python
>>> ungrammaticalName = "Zophie a Cat"
>>> fixedName = ungrammaticalName[:7] + "the" + ungrammaticalName[8:]
>>> fixedName
"Zophie the Cat"
```

In the above example, `ungrammaticalName` remains unchanged. You could do something like the below, though. It'll have
the `name` variable container point at new string, leaving the old one to be garbage collected.

```python
>>> name = "Zophie a Cat"
>>> name = name[:7] + "the" + name[8:]
>>> name
"Zophie the Cat"
```

And just because lists are mutable doesn't mean they'll be mutated every time you change their values. When you do
something like this:

```python
>>> eggs = [1, 2, 3]
>>> eggs = [4, 5, 6]
>>> eggs
[4, 5, 6]
```

You aren't modifying the old list. Instead, you're just creating a replacement and assigning the variable to it. If you
wanted to mutate the original list into the new one, you'd have to do something like this:

```python
>>> eggs = [1, 2, 3]
>>> while len(eggs) != 0:
>>>     del eggs[0]
>>> eggs += [4, 5, 6]
>>> eggs
[4, 5, 6]
```

Which is quite a bit more verbose, especially if you don't use loops or if you add the new elements individually.

## The Tuple Data Type

Tuples are yet another way of grouping data together. However, there are a number of differences, the most obvious being
that tuples group pieces of data within the parentheses `(` and `)`, as opposed to `[` and `]`. Like lists and strings,
tuple values can be referenced by a specific index, but like the latter and not the former, tuples are completely
immutable.

If you have a tuple with only one value, then the interpreter will assume that it's just a value contained within
parentheses. To prevent this, you need to place a comma after the value.

```python
# Example tuple
x = (1,)
```

As for what they're used for, it seems that they're basically a constant version of lists. They're good for when you
want to make it obvious that you're making a value constant without overloading the code with comments. And since the
Python devs know that the tuple will never change, they can make some optimizations to make the interpreter run faster.

## Converting between the list and tuple types with the `tuple()` and `list()` functions

Just like how `int("42")` will evaluate to the integer `42` and `str(42)` will evaluate to the string `"42"`, so too can
the `tuple()` and `list()` functions convert data values of one type into the other. `tuple()` will turn any array-based
element (a list or a string) into a tuple. `list()`, however, will turn any tuple **or** string into a list.

However, you cannot put simple primitives into these functions. If you do, you'll get a `TypeError`. Basically, anything
you put into one of these functions must be iterable.

```python
>>> tuple([1, 2, 3])
(1, 2, 3)
>>> list(("A", "B", "C"))
["A", "B", "C"]
>>> tuple("Example")
("E", "x", "a", "m", "p", "l", "e")
>>> list(2)
TypeError
```

## References

All lists in Python are reference-based (tuples and strings should be as well).

For a refresher, think of each variable being a box that can only hold so much. Primitive values are small enough to fit
inside, but more complex data types like lists aren't. So, when a list gets created, what gets stored inside the
variable is a reference to that list. When you set one variable equal to a second variable, the content gets copied
over, but the content itself can vary. If the second variable is a primitive, then the entire primitive value can go
inside the first. But if the second variable is a list, then the first variable will still copy the contents – they'll
just happen to to be a reference.

When you modify a list variable, the interpreter will take the reference within the variable and use it to find the
location of the actual list. But if two separate variables have the same reference, then they share a list. Any changes
done through one will be reflected when you reference the other.

## Passing References

It's absolutely vital that you understand references to understand how arguments get passed into functions. When you
pass an argument into a function, that argument's value will be passed in. If the value is for a primitive, then the
entire value can be thrown in. But if the value is a reference to something like a list or tuple, then that reference
will get passed in. That means that any code that modifies the value the reference points to will be reflected even if
you don't return anything.

Look at this code:

```python
def addHello(y):
    y.append("Hello!")

x = ["Oh", "Oh", "Oh"]
addHello(x)
print(x)
```

Both `x` and `y` each have a separate reference to a list, but the references both point at the same list.

## The `copy` module's `copy()` and `deepcopy()` functions

Most of the time, passing list and list-like values by reference is perfectly fine. You shouldn't run into many major
issues with them. But sometimes you need a separate copy of a list, because you're going to be making changes that you
don't want reflected in the original. Python makes this easy via the `copy.copy()` and `copy.deepcopy()` methods.
`copy.copy()` returns a separate copy of a reference-based value.

```python
import copy

junk = [1, 2, 3, 4]
otherJunk = copy.copy(junk)

junk.append(5)
print(otherJunk) # Still [1, 2, 3, 4]
```

Now, what's the difference between copies and deep copies? If you're only copying similar reference-based values, then
there's zero difference. The difference only becomes relevant once you start working with compound values, such as lists
of lists. When you use `copy.copy()` on a list of lists, it will make a copy of the main list, but it won't make any
copies of the inner lists. So, say that you have a list of lists called `x`, use `copy.copy()` on it, and store the
result in `y`. `x` and `y` will be separate lists, but they'll still share inner lists. That is, they'll both have
references to the same values.

By using `copy.deepcopy()`, you'll create separate copies not just of the containing list, but of every list inside it
as well.