container = {}
base_list = [1, 2, 3, 4, 5]
letter = "a"

# Add to the container dictionary. Add 1 * i to each number in base_list for each iteration i, starting from 0
# The letter keeps increasing by 1 with each iteration, too
for i in range(5):
    container[chr(ord(letter) + i)] = [j + i for j in base_list]

for k, v in container.items():
    print(f"{k}: {v}")