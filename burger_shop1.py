# define stubs

# GLOBAL CONSTANTS (sizes, cheese type, condiments,toppings, drinks)
SIZES = ("Single", "Double", "Triple")
CHEESES = ("American", "Swiss", "Provolone", "Cheddar", "Pepper Jack")
CONDIMENTS = ("Ketchup", "Mustard", "Mayo")
TOPPINGS = ("Bacon", "Lettuce", "Onion", "Mushrooms", "Olives", "Tomato", "Pickles")
DRINKS = ("Coke", "Diet Coke", "Sprite", "Lemonade", "Water")
DRINK_SIZE = ("Small", "Medium", "Large")


def menu():
    # display menu options
    # get user selection
    # customize
    pass


def order(phone):
    while True:
        count = 1
        for size in SIZES:
            print(f"{count}.  {size}")
            count += 1
        try:
            size = int(input("please enter the number of what size you would like:  "))
            if size < 1 or size > 3:
                print("enter number between 1 and 3")
                continue
            else:
                break
        except ValueError:
            print("enter number between 1 and 3")
            continue

    while True:
        count = 1
        for cheese in CHEESES:
            print(f"{count}.  {cheese}")
            count += 1
        try:
            size = int(
                input(
                    "please enter the number of what kind of cheese you would like:  "
                )
            )
            if size < 1 or size > len(CHEESES):
                print(f"enter number between 1 and {len(CHEESES)}")
                continue
            else:
                break
        except ValueError:
            print(f"enter number between 1 and {len(CHEESES)}")
            continue
    while True:
        count = 1
        for condiment in CONDIMENTS:
            print(f"{count}.  {condiment}")
            count += 1
        try:
            condiment = int(
                input("please enter the number of what condiments you would like:  ")
            )
            if condiment < 1 or condiment > len(CONDIMENTS):
                print(f"enter number between 1 and {len(CONDIMENTS)}")
                continue
            else:
                break
        except ValueError:
            print(f"enter number between 1 and {len(CONDIMENTS)}")
            continue

    while True:
        count = 1
        for topping in TOPPINGS:
            print(f"{count}.  {topping}")
            count += 1
        try:
            topping = int(
                input("please enter the number of what topping you would like:  ")
            )
            if topping < 1 or topping > len(TOPPINGS):
                print(f"enter number between 1 and {len(TOPPINGS)}")
                continue
            else:
                break
        except ValueError:
            print(f"enter number between 1 and {len(TOPPINGS)}")
            continue

    while True:
        count = 1
        for drink in DRINKS:
            print(f"{count}.  {drink}")
            count += 1
        try:
            drink = int(
                input("please enter the number of what drink you would like:  ")
            )
            if drink < 1 or drink > len(DRINKS):
                print(f"enter number between 1 and {len(DRINKS)}")
                continue
            else:
                break
        except ValueError:
            print(f"enter number between 1 and {len(DRINKS)}")
            continue

    while True:
        count = 1
        for drink_size in DRINK_SIZE:
            print(f"{count}.  {drink_size}")
            count += 1
        try:
            size = int(
                input("please enter the number of what drink size you would like:  ")
            )
            if drink_size < 1 or drink_size > len(DRINK_SIZE):
                print(f"enter number between 1 and {len(DRINK_SIZE)}")
                continue
            else:
                break
        except ValueError:
            print(f"enter number between 1 and {len(DRINK_SIZE)}")
            continue


def login():
    # get user information
    # check if customer already exists
    phone = input("please enter your phone number:   ")
    name = input("please enter your name:  ")
    with open("customer_list.txt", "a") as f:
        f.write(f"{phone}\n")
        f.write(f"{name}\n")
    return phone, name


def confirm_order(order):
    # confirm or change the order
    # save order to file
    # total and payment at pickup
    pass


def display_order(order):
    # display order and pickup time
    # display total and payment at pickup
    pass


def main():
    phone, name = login()
    my_order = order(phone)
    confirm_order(my_order)
    display_order(my_order)


main()
