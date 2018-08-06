examples = {}

examples["a"] = "12345"
examples["b"] = [1, 2, 3, 4, 5]
examples["c"] = {"a": 1, "b": 2, "c": 3}
examples["d"] = (5, 6, 7, 8, 9)

for i in examples.values():
    # .join() returns TypeError if you trying joining non-strings.
    # Using list comprehension to turn each iterable into a list of strings
    string_list = [str(x) for x in i]
    print(", ".join(string_list))