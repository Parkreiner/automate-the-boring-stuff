# Practice Questions

## 1. What does the code for an empty dictionary look like?

`{ }`

## 2. What does a dictionary value with a key 'foo' and a value 42 look like?

`{"foo": 42}`

## 3. What is the main difference between a dictionary and a list?

Lists are ordered, while dictionaries aren't. Also, lists key track of values via numerical indexes, while dictionaries
keep track of them via keys (which don't have to be integers).

## 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

You get a `KeyError`.

## 5. If a dictionary is stored in a variable `spam`, what is the difference between the expressions `'cat' in spam` and `'cat' in spam.keys()`?

There is no difference.

## 6. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat' in spam` and `'cat' in spam.values()`?

`"cat" in spam` will check to see if `spam` contains the key `"cat"`. `"cat" in spam.values()` will check to see if
`spam` contains a value of `"cat"`.

## 7. What is a shortcut for the following code?

Original:

```python
if 'color' not in spam:
    spam['color'] = 'black'
```

Shortcut:

```python
spam.setdefault("color", "black")
```

## 8. What module and function can be used to “pretty print” dictionary values?

`pprint()` from the `pprint` library.