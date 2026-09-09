"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

there = False
while not there:
    here = input("Are we there yet?  ").lower()

    if here == "yes":
        there = True


# 99 Bottles of Beer on the wall
bottles = 99
for y in range(bottles, 2, -1):
    print(f"\n{y} bottles of beer on the wall")
    print(f"{y} bottles of beer")
    print("take one down,pass it around")
    print(f"{y-1} bottles of beer on the wall")


print(f"\n2 bottles of beer on the wall")
print(f"2 bottles of beer")
print("take one down,pass it around")
print(f"1 bottle of beer on the wall")


print(f"\n{y} bottle of beer on the wall")
print(f"{y} bottle of beer")
print("take one down,pass it around")
print(f"0 bottles of beer on the wall")
