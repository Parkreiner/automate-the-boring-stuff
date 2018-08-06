inventory = {
    "Rope": 1,
    "Torch": 6,
    "Gold Coin": 42,
    "Dagger": 1,
    "Arrow": 12
}

'''
Required Output

Inventory:
12 × Arrow
1 × Dagger
42 × Gold Coin
Torch × 6
Rope × 1
Total number of items: 62
'''

def displayInventory():
    total_items = 0
    for key, value in sorted(inventory.items()):
        print(f"{key} × {value}")
        total_items = total_items + value
    print(f"Total number of items: {total_items}")

displayInventory()