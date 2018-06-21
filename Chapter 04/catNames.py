catNames = []
while True:
    print(f"Enter the name of cat {len(catNames) + 1} (or just press Enter to stop): ", end="")
    name = input()

    if name == "":
        break
    
    catNames.append(name)

if len(catNames) == 0:
    print("\nYou didn't input any cat names!")
else:
    print("\nThe names of all the cats are:")
    for name in catNames:
        print(name)
    print(f"That's {len(catNames)} cats.")