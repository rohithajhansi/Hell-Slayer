import time
from random import choice
from Setup import unnecessary_items, necessary_items

inventory = []
          
def items(item):
    """Creates a function that will be called when the player encounters a necessary item"""
    print(f"\nAs you continue on your journey, you encounter a disgusting {item} on the ground.")
    time.sleep(1)
    print("You have 2 options:")
    options = [f"1. Pick up the {item}", f"2. Leave the {item}"]
    print()
    print("\n".join(map(lambda x: x, options)))
    time.sleep(1)
    total_items = 0
    while total_items <= 7:
        try:
            user_option = int(input(f"\nWhat do you want to do with the {item} (number)? \n"))
            if user_option == 1:
                print(f"\nYou made a great decision to pick up the {item}.")
                time.sleep(1)
                print(f"\nYou slowly reach out to pick up the {item} with 2 fingers and carefully placed it in your backpack.\n")
                inventory.append(item.title())
                total_items += 1
                break

            elif user_option == 2:
                print(f"\nYou left the {item} on the ground and walked away as fast as humanely possible, hoping there wouldn't come a time where you would regret it.")
                break
        except (TypeError, ValueError, Exception):
            print("\nEnter a number (|_|).")

def needed():
    """Creates a function that will be called when the player encounters a random item"""
    
    random = choice(necessary_items)
    necessary_items.remove(random)
    time.sleep(1)
    items(random)

def not_needed():
    """Creates a function that will be called when the player encounters a random item"""

    random = choice(unnecessary_items)
    unnecessary_items.remove(random)
    time.sleep(1)
    items(random)