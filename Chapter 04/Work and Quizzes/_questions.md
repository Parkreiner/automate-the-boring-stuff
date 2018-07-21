
# Chapter 4 Practice Questions

## Set one:

### 1. What is `[]`?

`[]` is simply an empty list.

### 2. Look at the below code. How would you change the third value to `"hello"`?

```python
spam = [2, 4, 6, 8, 10]
```

`spam[2] = "hello"

## Set 2: Assume that `spam` is a list with the values `["a", "b", "c", "d"]`

### 3. What does spam[int(int('3' * 2) // 11)] evaluate to?

```python
spam[int(int('3' * 2) // 11)]
spam[int(int('33') // 11)]
spam[int(33 // 11)]
spam[int(3)]
spam[3]
"d"
```

### 4. What does spam[-1] evaluate to?

It's equivalent to `spam[len(spam) - 1]`, so `"d"`.

### 5. What does spam[:2] evaluate to?

It's a slice of `spam` that runs from the beginning of the list to just before the element at index `2`. So, it becomes
`["a", "b"]`.

## Set 3: Assume that `bacon` is the list `[3.14, 'cat', 11, 'cat', True]`

### 6. What does bacon.index('cat') evaluate to?

It evaluates to `1`, as that is where the first instance of `cat` is located within the list.

### 7. What does bacon.append(99) make the list value in bacon look like?

The list becomes `[3.14, 'cat', 11, 'cat', True, 99]`.

### 8. What does bacon.remove('cat') make the list value in bacon look like?

It removes the first instance of `"cat"`, turning the list into `[3.14, 11, 'cat', True]`

## Set 4

### 9. What are the operators for list concatenation and list replication?

They're just `+` and `*` respectively.

### 10. What is the difference between the append() and insert() list methods?

`append()` always inserts the method's argument at the end of the list. `insert()`, on the other hand, lets you place
the method's argument at any index within the list, moving any element at that index and all following elements up by
one index.

### 11. What are two ways to remove values from a list?

Those would be the `.remove()` method and the `del` keyword. However, `del` requires that you know the index of the
value you want to get rid of.

### 12. Name a few ways that list values are similar to string values.

The biggest one is that strings are basically lists of characters. This means that specific characters can be referenced
via bracket notation, just as with lists and its values. It also means that the two can use a lot of the same methods
and that you can create slices of each.

### 13. What is the difference between lists and tuples?

The biggest one is that tuples are immutable. As far as writing them, though, lists are created via brackets (`[ ])`,
while tuples are created via parentheses (`( )`).

### 14. How do you type the tuple value that has just the integer value 42 in it?

To create any single-value tuple, you need to terminate the value with a comma. So, a tuple of just `42` would be
`(42,)`.

### 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

If you're allergic to built-in functions, you can create a list from a tuple by iterating over the tuple and appending
each value to the end of the list. I have no idea how to do turn lists into tuples iteratively, though. But to make
things much easier, you just need to use the `list()` and `tuple()` methods.

### 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

They contain references to those lists. That means that if you have two separate variables pointing at the same list
and modify the value one points at, the change will be reflected in both.

### 17. What is the difference between copy.copy() and copy.deepcopy()?

Both create a separate copy of a list, as opposed to just copying the list's reference. If you're creating a copy of a
simple list, then the two methods will work exactly the same. But if you're dealing with lists of lists, then
`copy.copy()` won't create separate copies of the inner lists, while `copy.deepcopy()` will.