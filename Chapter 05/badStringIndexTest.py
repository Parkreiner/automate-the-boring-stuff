x = "Junk"

try:
    print(x[50])
except ValueError:
    print("Hmm")