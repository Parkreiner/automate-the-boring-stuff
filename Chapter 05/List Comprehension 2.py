x = [1, 2, 3, 4, 5]

y = [(item * 5 + 1) // 2 for item in x]

print(f"Base: {x}", f"(x * 5 + 1) // 2: {y}", sep="\n")