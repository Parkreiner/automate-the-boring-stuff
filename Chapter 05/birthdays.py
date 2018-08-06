# List of birthdays, as defined by the first name of the people who have them
birthdays = {
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar 4"
}

while True:
    name = input("Enter the name of the person whose birthday you would like to display (or just press Enter to exit): ")
    if name == "":
        break

    # Ensures that only the first letter is uppercase
    name = name[0].upper() + name[1:].lower()

    # Adds ' to end of name if it ends in s; otherwise makes it end in 's
    possessive = "'" if (name[len(name) - 1] == "s") else "'s"

    if name in birthdays:
        print(f'{name}{possessive} birthday falls on {birthdays[name]}.')
    else:
        bday = input(f"{name}{possessive} birthday is not on file. Please enter their birthday (e.g., Nov 21) or " +
                      "press Enter to quit: ")

        if bday == "":
            break

        birthdays[name] = bday
        print(f"Database updated. {name}{possessive} birthday is listed as {birthdays[name]}.")