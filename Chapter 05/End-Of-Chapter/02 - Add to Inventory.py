inventory = {
    "Rope": 1,
    "Torch": 6,
    "Gold Coin": 42,
    "Dagger": 1,
    "Arrow": 12
}

dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

def display_inventory():
    total_items = 0
    for key, value in sorted(inventory.items()):
        print(f"{key} × {value}")
        total_items = total_items + value
    print(f"Total number of items: {total_items}")

def add_to_inventory(inv, loot):
    for i in loot:
        # Makes each piece of loot properly uppercased
        formatted_i = " ".join([word[0].upper() + word[1:].lower() for word in i.split(" ")])
        
        inv.setdefault(formatted_i, 0)
        inv[formatted_i] = inv[formatted_i] + 1
    return inv 

add_to_inventory(inventory, dragon_loot)
display_inventory()