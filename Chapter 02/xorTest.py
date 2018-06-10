boolSet = [False, True]

# Straightforward version because I'm bad with boolean algebra
for i in range(len(boolSet)):
    for j in range(len(boolSet)):
        a = boolSet[i]
        b = boolSet[j]
        print(f"{i}{j} - {(a and not b) or (not a and b)}")