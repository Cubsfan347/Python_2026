"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


# TODO: Define get_price(size)
def get_price(size):
    match size:
        case "small":
            return 3.0
        case "medium":
            return 4.0
        case "large":
            return 5.0
        case _:
            print("invalid entry")
            return 0


# TODO: Define blend(size, base, fruit, scoops)
def blend(size, base, fruit, price):
    print("you have selected")
    print(size)
    print(f"$ {price:.2f}")
    print(fruit)
    print(base)


# TODO: Define main() to collect input and call your logic


def main():
    try:
        size = input("What size smoothie do you want?(small, medium, large):").lower()
        price = get_price(size)
        print(price)
        for fruit in FRUITS:
            print(fruit)
        selected_fruit = input("which fruit do you want?  ")
        for base in BASES:
            print(base)
        selected_base = input("which base do you want?  ")
    except Exception as e:
        print(e)
    blend(size, base, fruit, price)


main()
