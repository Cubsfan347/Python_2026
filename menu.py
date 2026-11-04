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
    menus = {}
    try:
        with open("menu.txt", "r") as file:
            for line in file:
                print(line)
                parts_of_line = line.strip().split(":")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail
                print(menus)
        return menus
    except FileNotFoundError:
        print("Please make sure menu.txt exists.")
    except IndexError:
        return menus  # this handles blank lines in the text file
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


def print_menu(sizes, cheeses, condiments, toppings, drinks, drink_size):

    print("Sizes\n")
    print(sizes)
    sizes_item = sizes.split(",")
    for item in sizes_item:
        print(f"\t{item.strip()}")

    print("Cheeses\n")
    cheeses_item = cheeses.split(",")
    for item in cheeses_item:
        print(f"\t{item.strip()}")

    print("Condiments\n")
    condiments_item = condiments.split(",")
    for item in condiments_item:
        print(f"\t{item.strip()}")

    print("Toppings\n")
    toppings_item = toppings.split(",")
    for item in toppings_item:
        print(f"\t{item.strip()}")

    print("Drinks\n")
    drinks_item = drinks.split(",")
    for item in drinks_item:
        print(f"\t{item.strip()}")

    print("Drink_size\n")
    drink_size = drink_size.split(",")
    for item in drink_size:
        print(f"\t{item.strip()}")


def main():
    menu_items = read_menu()
    sizes, cheeses, condiments, toppings, drinks, drink_size = split_into_variables(
        menu_items
    )
    print_menu(sizes, cheeses, condiments, toppings, drinks, drink_size)


main()
