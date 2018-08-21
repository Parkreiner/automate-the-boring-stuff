'''
This program works by taking in a picnic basket dictionary and printing all the contents. Also, Brighurst was absolutely
right about dot leaders being terrible. The output doesn't look that bad with the current items, but as the keys and
values keep getting longer and longer, the output looks worse and worse.

Take a look at this nonsense:
-------------------------------------------PICNIC BASKET--------------------------------------------
Apples.............................................................................................7
Sandwiches.........................................................................................5
Bags of chips.....................................................................................10
Cans of dog water.................................................................................76
Rocks...........................................................................................3571
Very, very angry bees........................................................................6000571
All your hopes and dreams, all of which are far more delicate than the most fragile egg............3

That just looks obnoxious.
'''

import math, time

def main():
    picnic_basket = {
        "Apples": 7,
        "Sandwiches": 5,
        "Bags of chips": 10,
        "Cans of disgusting dog water": 76,
        "Rocks": 3571,
    }

    start_time = time.time()
    display_basket_contents(picnic_basket, 5)
    print(f"\nProgram took {'%.5f' % (time.time() - start_time)} seconds to run.")


def display_basket_contents(basket, min_spacing=5):    
    largest_key_length = 0
    largest_value_length = 1
    value_lengths = {}

    # Find largest key and value lengths
    for key, value in basket.items():
        # Find largest key length
        current_length = len(key)
        if current_length > largest_key_length:
            largest_key_length = current_length

        # Find most number of digits among each dict value
        current_value_length = int(math.log10(value)) + 1

        if current_value_length > largest_value_length:
            largest_value_length = current_value_length
        
        # Store value length for later use
        value_lengths[key] = current_value_length

    # Print header
    print("\n", "PICNIC BASKET".center(largest_key_length + min_spacing + largest_value_length, "-"), sep="")

    # Print each key and its value, with all pairs separated by dot leaders
    for key, value in basket.items():
        print(key.ljust(largest_key_length + min_spacing + largest_value_length - value_lengths[key], "."),
              value, sep="")



if __name__ == "__main__":
    main()