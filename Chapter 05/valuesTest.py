from functools import partial

def basic_stuff():
    test = {}

    start = "a"
    num_of_letters = 10

    # Populate test with values like "a": 0 and "b": 1
    for i in range(num_of_letters):
        test[chr(ord(start) + i)] = i + 1

    print(test)

    # .values(), .keys(), and .items() methods return view, not list; need to be converted into one
    print(list(test.values()))

basic_stuff()

all_people = {
    "Alice": {"apples": 5, "pretzels": 12 },
    "Bob": { "ham Sandwiches": 3, "apples": 2 },
    "Carol": { "cups": 3, "apple pies": 1 }
}

'''
    This function prints what each person brought to the picnic and then prints the total items between them (so if
    person A brought 5 apples and person B brought 3, the function would print that the group has 8 apples between them)
    
    ---

    Expected output:
    Alice brought 5 apples and 12 pretzels.
    Bob brought 3 ham sandwiches and 2 apples.
    Carol brought 3 cups and 1 apple pies.

    All together, they brought 7 apples, 12 pretzels, 3 ham sandwiches, 3 cups, and 1 apple pies.

    ---

    If there were a "Dan" who brought 5 apples, 6 oranges, and 4 bags of chips, his line would look like:

    Dan brought 5 apples, 6 oranges, and 4 bags of chips.
'''
def print_picnic_info():
    easyPrint = partial(print, end="")

    item_totals = {}
    easyPrint("\n")
    
    # Print what each person brought and also add up the item totals
    for key1, value1 in all_people.items():
        easyPrint(f"{key1} brought ")

        for key2, value2 in value1.items():
            # Add to item totals
            item_totals.setdefault(key2, 0)
            item_totals[key2] = item_totals[key2] + value2    
            
            # Print key-value pair
            easyPrint(f"{value2} {key2}")

        easyPrint(".\n")

    # Start printing item totals   
    easyPrint("\nAll together, they brought ")

    # Iterate over the total items; need to do list conversion for proper sentence-like formatting
    item_totals_list = list(item_totals.items())
    number_of_items = len(item_totals_list)
    for i in range(number_of_items):
        easyPrint(f"{item_totals_list[i][1]} {item_totals_list[i][0]}")

        if i == number_of_items - 1:
            easyPrint(".\n")
        else:
            easyPrint(", ")

        if i == number_of_items - 2:
            easyPrint("and ")

print_picnic_info()

