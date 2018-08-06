import pprint

test = {
    1: ["A", "B", "C"],
    2: {
        "D": "Dog",
        "E": "Elephant",
        "F": "Fox"
    }
}
test2 = {
    "A": "Aardvark",
    "B": "Beeeeees (as in, a lot of them)",
    "C": "Capybara"
}
test3 = {
    "G": 1,
    "H": 2,
    "I": 3
}

print(test)
pprint.pprint(test, width=1)

print(test2)
pprint.pprint(test2)

print(test3)
pprint.pprint(test3)