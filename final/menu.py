"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""


def read_menu():
    menu_items = {}
    try:
        with open("final\\menu.txt", "r") as file:
            for line in file:
                print(line)
                parts_of_line = line.strip().split(":")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menu_items[category] = detail
                print(menu_items)
        return menu_items
    except FileNotFoundError:
        print("Please make sure menu.txt exists.")
    except IndexError:
        return menu_items  # this handles blank lines in the text file
    except Exception as e:
        print(e)


def split_into_variables(menu_items):
    print(menu_items)
    sizes = menu_items.get("SIZES")
    cheeses = menu_items.get("CHEESES")
    condiments = menu_items.get("CONDIMENTS")
    toppings = menu_items.get("TOPPINGS")
    drinks = menu_items.get("DRINKS")
    drink_size = menu_items.get("DRINK_SIZE")
    return sizes, cheeses, condiments, toppings, drinks, drink_size


# def print_menu(sizes, cheeses, condiments, toppings, drinks, drink_size):


def print_sizes(sizes):
    print("Sizes\n")
    sizes_item = sizes.split(",")
    count = 1
    for item in sizes_item:
        print(f"{count}.  {item.strip()}")
        count += 1
    return len(sizes_item)


def print_cheeses(cheeses):
    print("Cheeses\n")
    cheeses_item = cheeses.split(",")
    count = 1
    for item in cheeses_item:
        print(f"{count}.\t{item.strip()}")
        count += 1
    return len(cheeses_item)


def print_condiments(condiments):
    print("Condiments\n")
    condiments_item = condiments.split(",")
    count = 1
    for item in condiments_item:
        print(f"{count}.\t{item.strip()}")
        count += 1
    return len(condiments_item)


def print_toppings(toppings):
    print("Toppings\n")
    toppings_item = toppings.split(",")
    count = 1
    for item in toppings_item:
        print(f"{count}\t{item.strip()}")
        count += 1
    return len(toppings_item)


def print_drinks(drinks):
    print("Drinks\n")
    drinks_item = drinks.split(",")
    count = 1
    for item in drinks_item:
        print(f"{count}.\t{item.strip()}")
        count += 1
    return len(drinks_item)


def print_drink_size(drink_size):
    print("Drink_size\n")
    drink_size_item = drink_size.split(",")
    count = 1
    for item in drink_size_item:
        print(f"{count}.\t{item.strip()}")
        count += 1
    return len(drink_size_item)
