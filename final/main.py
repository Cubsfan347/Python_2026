import Python_2026.final.menu as menu


def order(phone):
    order = []
    menu_items = menu.read_menu()
    sizes, cheeses, condiments, toppings, drinks, drink_size = (
        menu.split_into_variables(menu_items)
    )
    while True:
        print(f"while true {sizes}")
        my_length = menu.print_sizes(sizes)
        try:
            size = int(input("please enter the number of what size you would like:  "))
            if size < 1 or size > 3:
                print("enter number between 1 and 3")
                continue
            else:
                print(sizes)
                sizes = sizes.split(",")
                # left off here
                order.append(sizes[size - 1])
                print(f"order  {order}")
                break
        except ValueError:
            print("enter number between 1 and 3")
            continue

    while True:
        my_length = menu.print_cheeses(cheeses)
        try:
            cheese = int(
                input(
                    "please enter the number of what kind of cheese you would like:  "
                )
            )
            if size < 1 or size > my_length:
                print(f"enter number between 1 and {my_length}")
                continue
            else:
                order += cheeses[cheese - 1]
                break
        except ValueError:
            print(f"enter number between 1 and {my_length}")
            continue
    while True:
        my_length = menu.print_condiments(condiments)
        try:
            condiment = int(
                input("please enter the number of what condiment you would like:  ")
            )
            # todo allow more than one
            if condiment < 1 or condiment > my_length:
                print(f"enter number between 1 and {my_length}")
                continue
            else:
                order += condiments[condiment - 1]
                break
        except ValueError:
            print(f"enter number between 1 and {my_length}")
            continue

    while True:
        my_length = menu.print_toppings(toppings)
        try:
            topping = int(
                input("please enter the number of what topping you would like:  ")
            )
            # todo allow more than one
            if topping < 1 or topping > my_length:
                print(f"enter number between 1 and {my_length}")
                continue
            else:
                order += toppings[topping - 1]
                break
        except ValueError:
            print(f"enter number between 1 and {my_length}")
            continue

    while True:
        my_length = menu.print_drinks(drinks)
        try:
            drink = int(
                input("please enter the number of what drink you would like:  ")
            )
            if drink < 1 or drink > my_length:
                print(f"enter number between 1 and {my_length}")
                continue
            else:
                order += drinks[drink - 1]
                break
        except ValueError:
            print(f"enter number between 1 and {my_length}")
            continue

    while True:
        my_length = menu.print_drink_size(drink_size)
        try:
            drink = int(
                input("please enter the number of what drink size you would like:  ")
            )
            if drink < 1 or drink > my_length:
                print(f"enter number between 1 and {my_length}")
                continue
            else:
                order += drink_size[drink - 1]
                break
        except ValueError:
            print(f"enter number between 1 and {my_length}")
            continue

    # printing to file
    with open("final\\orders.txt", "a") as file:
        file.write(order)


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


def old_orders(phone):
    # display last 5 orders
    pass


def main():
    phone, name = login()
    my_order = old_orders(phone)
    my_order = order(phone)
    confirm_order(my_order)
    display_order(my_order)


main()
