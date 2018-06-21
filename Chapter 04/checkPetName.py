myPets = ["Zophie", "Pooka", "Fat-Tail"]
name = input("Enter a cat name: ")
if name not in myPets:
    print(f"Sorry. Don't got a cat by the name of {name}.")
else:
    print(f"Yup! I've got {name}.")