print(max(3, 5))
print(max("A", "ABC"))
print(max("AA", "Z"))
print(max([1, 2, 3]))

test_dict = {
    "a": 3,
    "b": 2,
    "c": 1
}

print(max(test_dict))
print(max(test_dict.values()))

test_list = ["ABC", 123, True]
print(max(test_list, key=str))
print(max(test_dict.items()))