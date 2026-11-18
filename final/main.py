import menu
import datetime


def order(phone):
    order = []
    timestamp = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    menu_items = menu.read_menu()
    order.append(phone)

    if not menu_items:
        print("Unable to place an order because the menu could not be loaded.")
        return order

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
            if cheese < 1 or cheese > my_length:
                print(f"enter number between 1 and {my_length}")
                continue
            else:
                order.append(cheeses.split(",")[cheese - 1].strip())
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
                order.append(condiments.split(",")[condiment - 1].strip())
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
                order.append(toppings.split(",")[topping - 1].strip())
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
                order.append(drinks.split(",")[drink - 1].strip())
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
                order.append(drink_size.split(",")[drink - 1].strip())
                break
        except ValueError:
            print(f"enter number between 1 and {my_length}")
            continue

    with open("Python_2026\\final\\orders.txt", "a") as file:
        file.write(f"{timestamp}*{order}\n")
    order = f"{timestamp}*{order}"
    return order


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
    # read items into all items
    # grab date time stamp from order
    # for loop to check which line matches date time stamp
    # when that is found we assign the index to my_index
    # break apart order and display numbered items
    # ask user if it is good or if they need to make changes
    # make changes as needed
    # if changes happen we need to update the dictionary line and rewrite the dictionary to the file

    # cancel order - delete in crud
    pass


def display_order(order):
    # split order on :
    # copy the split items from menu same thing
    # cycle through printing the formatted reciept
    # add 20 minutes to the current time and tell them it will be ready for pickup at that time
    order_items = {}
    try:
        with open("Python_2026\\final\\orders.txt", "r") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                print(line)
                category, separator, detail = line.partition("*")

                category = category.strip()
                detail = detail.strip()
                order_items[category] = detail
        print(order_items)

    except FileNotFoundError:
        print(f"Menu file not found: {"Python_2026\\final\\orders.txt"}")
        return order_items


def main():
    phone, name = login()

    my_order = order(phone)
    confirm_order(my_order)
    # display_order(my_order)


main()
