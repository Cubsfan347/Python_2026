"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""


class Order:
    def __init__(
        self, order_type, size, cheese, condiments, toppings, drink, drink_size
    ):
        # private attributes protect the order details
        self.__order_type = order_type
        self.__size = size
        self.__cheese = cheese
        self.__condiments = condiments
        self.__toppings = toppings
        self.__drink = drink
        self.__drink_size = drink_size

    # Getters

    def get_order_type(self):
        return self.__order_type

    def get_size(self):
        return self.__size

    def get_cheese(self):
        return self.__cheese

    def get_condiments(self):
        return self.__condiments

    def get_toppings(self):
        return self.__toppings

    def get_drink(self):
        return self.__drink

    def get_drink_size(self):
        return self.__drink_size

    # Setters

    def set_order_type(self, order_type):
        self.__order_type = order_type

    def set_size(self, size):
        self.__size = size

    def set_cheese(self, cheese):
        self.__cheese = cheese

    def set_condiments(self, condiments):
        self.__condiments = condiments

    def set_toppings(self, toppings):
        self.__toppings = toppings

    def set_drink(self, drink):
        self.__drink = drink

    def set_drink_type(self, drink_type):
        self.__drink_type = drink_type

    # Methods (functions inside a class) describe behaviors/actions an object can do

    def return_summary(self):
        # Return: a one-line summary (str) describing this object's current state
        summary = f"order summary: {self.__order_type}, {self.__size}, {self.__cheese}, {self.__condiments}, {self.__toppings}, {self.__drink}, {self.__drink_size}"

        return summary


def main():
    my_order1 = Order(
        "burger", "double", "provolone", "mustard", "olives", "coke", "large"
    )
    print(my_order1.return_summary())

    my_order2 = Order(
        "burger", "double", "cheddar", "ketchup", "pickles", "coke", "medium"
    )
    print(my_order2.return_summary())


main()
