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


def login():
    # get user information
    # check if customer already exists
    pass


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
    id = login()
    order = menu(id)
    confirm_order(order)
    display(order)


main()
