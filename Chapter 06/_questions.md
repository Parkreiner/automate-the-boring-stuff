# Chapter 6 – Questions

## 1. What are escape characters?

Escape characters are characters that are explicitly denoted as being part of a string, rather than part of the
language. If your strings require quotation marks or whitespace characters, escape characters will often do the trick.

## What do `\n` and `\t` represent?

`\n` is a newline character, while `\t` is a tab.

## 4. The string value `"Howl's Moving Castle"` is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?

That's because it's impossible for the single quote to be confused for part of the language, as the string didn't start
with one.

## 5. If you don’t want to put `\n` in your string, how can you write a string with newlines in it?

You can use triple quotes and type the newlines yourself, like a damn animal.

## 6. What do the following expressions evaluate to?

### `'Hello world!'[1]`

`e`

### `'Hello world!'[0:5]`

`Hello`

### `'Hello world!'[:5]`

`Hello`

### `'Hello world!'[3:]`

`lo world!`

## 7. What do the following expressions evaluate to?

### `'Hello'.upper()`

`HELLO`

### `'Hello'.upper().isupper()`

`True`

### `'Hello'.upper().lower()`

`False`

## 8. 8. What do the following expressions evaluate to?

### `'Remember, remember, the fifth of November.'.split()`

`["Remember,", "remember,", "the", "fifth", "of", "November"]`

### `'-'.join('There can be only one.'.split())`

`"There-can-only-be-one"`

## 9. What string methods can you use to right-justify, left-justify, and center a string?

`.ljust()`, `.rjust()`, and `.center()`

## 10. How can you trim whitespace characters from the beginning or end of a string?

Just use the `.split()` method without an argument.