"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

# Define Pizza Order


# GLOBAL CONSTANTS (Sizes, Toppings)
SIZES = ("small", "medium", "large", "extra large")
TOPPINGS = ("cheese", "sausage", "pepperoni", "mushrooms", "green olive", "black olive")


def menu():
    # display menu options
    # get user selection
    # customize
    pass


def login():
    # get user information
    # check if user exists
    id = input("please enter your name")
    return id


def display_order(order):
    # display order and pickup time
    # display total and payment at pickup
    print(f"hello {order}")
    for size in SIZES:
        print(size)
    my_size = input("choose your size")

    for topping in TOPPINGS:
        print(topping)
    my_toppings = input("choose your toppings")

    is_delivery = input("do you want delivery y/n?")
    return order, my_size, my_toppings, is_delivery


def make_pizza(order, size="medium", toppings="none", delivery="pickup"):
    # display order
    print("here is your pizza order")
    print(order)
    print(f"size = {size}")
    print(f"toppings = {toppings}")
    print(f"delivery = {delivery}")


def main():
    id = login()
    order, size, toppings, delivery = display_order(id)

    make_pizza(order, size, toppings, delivery)


main()
