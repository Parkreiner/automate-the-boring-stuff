# Checking to see what exactly passing `key=str.lower` into the list sort method actually does

test1 = ["A", "a", "B", "c", "C", "b"]
test1.sort(key=str.lower)
print(test1)

test2 = ["Ab", "aB", "AB", "ab"]
test2.sort(key=str.lower)
print(test2)

test3 = ["A", "aB"]
test3.sort(key=str.lower)
print(test3)