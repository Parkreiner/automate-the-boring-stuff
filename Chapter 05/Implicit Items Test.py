'''
Test to see if using the form "for k, v in x" will coerce x into x.items()

Doesn't work; whenever you use a for-loop on a dictionary like this, it will always default to x.keys()
'''
x = {"a": 1, "b": 2}

for k, v in x.items():
    print(f"{k} {v}")