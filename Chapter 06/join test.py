x = ["What", "a", "nice", "day"]
print(" ".join(x))

# Have to use a list comprehension for this, since the method expects nothing but strings.
y = ["The", "answer to life", "is", 42]
print(" ".join([str(x) for x in y]))

# Checking what happens if you pass nothing in; results in an error
print(" ".join())