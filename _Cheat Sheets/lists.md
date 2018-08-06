# Lists

## Multiple assignment

Multiple assignment lets you assign multiple variables to multiple values within a list. However, the number of
variables must match the number of list values being referenced.

This works:

```python
>>> letters = ["A", "B", "C"]
>>> x, y, z = letters
>>> print(x, y, z)
A B C
```

But neither of these do:

```python
letters = ["A", "B", "C"]
x, y = letters

letters = ["A", "B"]
x, y, z = letters
```

## Modifying lists 

### Adding to lists

#### List Concatenation

Python supports list concatenation with `+`. When you have something like `[1, 2] + [3, 4]`, you're basically plucking
out the elements from the latter and adding them to the end of the former. So, the example would result in
`[1, 2, 3, 4]`.

You can also use the form `x += [3, 4]`.

#### `.append()`

The `.append()` method is almost exactly like `+` operator. It lets you add a value to the end of a list, but there is
one key difference: if you append another list, its values won't get plucked out. Instead, the entire list will be added
to the end, creating a list of lists.

```python
>>> [1, 2].append([3, 4])
[1, 2, [3, 4]]
```

#### `.insert()`

The `.insert()` method is like the `.append()` method, except that it lets you insert values at specific indexes. If a
value already exists at that index, the value will get placed there, while the old value and everything that follows
will get nudged to the right.

#### List replication

When you use `*` on a list, that's called list replication. Basically, this performs list concatenation on the original
list with itself multiple times. As this is basically repeated list concatenation, the values from the original list
will get plucked out and added to the end; you can't create a list of lists from a simple list.

```python
>>> [0, 1] * 3
[0, 1, 0, 1, 0, 1]
```

### Deleting from lists

#### `del` for lists

As mentioned above, using `del` on a specific list index will delete the value at that index and move all following
values up by 1 index.

```python
>>> x = [0, 1, 2]
>>> del x[1]
>>> x
[0, 2]
```

#### The `.remove()` method

Using `.remove()` on a list allows you to remove the first instance of a value within that list. As with `del`, any
values that follow will get bumped up by one index, but there is a problem. If the value you're trying to remove doesn't
exist within the list, Python will throw a `ValueError`.

Basically, this is good for when you know what value you want to delete, but not where it's located. It's especially
good when that value is unique within that list.

```python
>>> [0, 2, 2].remove(2)
[0, 2]
>>> [0, 2, 2].remove(1)
ValueError
```

## Checking for existence within lists

### `in`

The `in` keyword allows you to check for whether a specific value exists within a list. It doesn't return the index
where that value is located, but it is fast.

```python
>>> 0 in [0, 2, 8]
True
```

### `not in`

`not in` is basically the same as `not (x in y)`. Python just supports this way of writing the value to make the code a
little cleaner.

```python
>>> "a" not in ["b", "c", "d"]
True
```

## Referencing and copying parts of lists

### Negative list indices

Negative list indexes let you access values starting from the end of the list. Basically, for a list `x`, `x[-1]` is
equivalent to `x[len(x) - 1]`

### Slices

Slices allow you to create separate lists that are subsets of another list. To use them, you just need to use a `:`
inside a pair of brackets.

Say that you have a list `x`.

1. `x[a:b]` will create a list that includes all elements in `x` starting from `a` and going up to `b - 1`.
2. `x[a:]` will create a list that includes all elements in `x` starting from `a` and going to the end of the list
3. `x[:b]` will create a list that starts from the beginning of the list and goes up to `b - 1`.
4. `x[:]` will create an exact copy of the original list.

Remember that lists/arrays are reference-based, so `x[:]` actually has uses for creating an entirely separate copy of
a list. Using `y = x` will have `x` and `y` both point to the exact same list (meaning that changes to one will be
reflected in the other), while `y = x[:]` will have `x` and `y` each point to separate lists.

## Looping over lists

### `for i in range(len(x))`

This is the most fundamental way of looping over a list. The loop head will start counting from a value of `i = 0` and
increment by `i` by `1` with each iteration. The loop will break when `i` equals `len(x)`, meaning that for a header
`for i in range(len([1, 2, 3]))`, `i` will have the values `0`, `1`, and `2`, but will break before `i` can becomes `3`.

### `for i in x`

The syntax for this loop is even simpler, but there is one drawback: there's no way to store the indexes of the list as
you increment. Basically, this is good for when you just want the values, but don't want to do anything with the
indexes.

## Sorting lists

### The `.sort()` method

`.sort()` allows you to sort a list **in place**, so long as the list is comprised of solely of elements of the same
type. This means that numerial lists will be sorted from least to greatest, while string lists will be sorted
lexicographically. You can also sort the list in reverse order by passing it the argument `reverse=True`.

This method also works on lists of lists. When you use this method on one, it will try sorting the sub-lists based on
each one's first element. If two sub-lists have the same element, `.sort()` will start looking at the second element,
and so on. An empty list will always be placed first, however.

#### Overriding the `.sort()` method's default lexicographical order

By default, `.sort()` will sort strings similarly to how they're organized in ASCII. That is, uppercase letters will
come before lowercase ones. You can "override" this by passing in the argument `key=str.lower`, which will sort all
values as if they were lowercase. This will group uppercase and lowercase versions of the same letter.

Default:

```python
>>> ["A", "a", "B", "b", "C", "c"].sort()
["A", "B", "C", "a", "b", "c"]
```

With `key=str.lower`:

```python
>>> test1 = ["A", "a", "B", "c", "C", "b"]
>>> test1.sort(key=str.lower) # test1 basically becomes ["a", "a", "b", "c", "c", "b"]
['A', 'a', 'B', 'b', 'c', 'C']

>>> test2 = ["Ab", "aB", "AB", "ab"]
>>> test2.sort(key=str.lower)
['Ab', 'aB', 'AB', 'ab']
```

## Copying lists

### The `copy.copy()` function

The `copy.copy()` function allows you to create a separate, shallow copy of a list. As the list will be a shallow copy,
only the main containing list will be turned into a copy. If the list contains reference-based values (such as more
lists), then those won't be turned into separate copies.

Basically, if you try copying a list of lists, the entire containing list and its contents will be copied; the contents
just happen to be references. Those references will still point to the sub-lists within the original list.

Also, this function is exactly the same as using `[:]` to create a full slice.

### The `copy.deepcopy()` function

The `copy.deepcopy()` allows you to create a deep copy of a list. This means that any reference values within the list
will be evaluated. The data that the references point at will then be copied, and references pointing to those new
copied values will be placed in the overall deep copy list.

## -