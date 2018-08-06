# Extra Things I learned

## Python is not like C when it comes to loops

In C, a loop like this is really bad practice:

```c
for (int i = 0; i < strlen(exampleArray); i++)
{
    printf("Stuff");
}
```

The reason is that the value of `strlen(exampleArray)` gets re-evaluated with each loop iteration. To prevent this, you
would need to make a slight modification:

```c
for (int i = 0, x = strlen(exampleArray); i < x; i++)
{
    printf("Stuff");
}
```

With this, `strlen(exampleArray)` only gets calculated once, as part of the initial conditions, and then the result gets
stored in `x`. So, you don't need to recalculate `strlen(exampleArray)` with each iteration, as the result (which never
changes), is stored in a separate variable.

Python is nothing like this. This is perfectly fine:

```python
for i in range(len(exampleArray)):
    print("Stuff")
```

This is because Python converts the loop into a list-like object. I don't fully understand what that means, but at the
very least, len(exampleArray) doesn't get recalculated with each iteration. However, this doesn't apply to all modern
programming languages. JavaScript still benefits from the C-style improvement, though the gains aren't as stark. While
JS does store the length of an array in a property value, this loop still suffers from a slight performance dip:

```javascript
for (let i = 0; i < exampleArray.length; i++)
{
    console.log("Stuff");
}
```

This is because `exampleArray` still needs to get dereferenced with each iteration, as that's the only way to get at its
`length` property. You can fix this "problem" like so:

```javascript
for (let i = 0, x = exampleArray.length; i < x; i++)
{
    console.log("Stuff");
}
```

With the above, `exampleArray` only needs to get dereferenced as part of the initial conditions.

## The `sorted()` function (not method)

`sorted()` lets you turn a list or dictionary into a sorted list. I still need to read up on the rules for how this is
done, but it seems to be pretty intuitive, defaulting to things like numerical and alphabetical order.

## List comprehensions