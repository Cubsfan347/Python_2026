"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# ask user for two integers
num1 = int(input("please type an integer"))
num2 = int(input("please type another integer"))


# logic checks
if num1 > 0 & num2 > 0:
    print("both numbers are greater than 0")
else:
    print("both numbers are not greater than 0")

if num1 > 100 & num2 > 100:
    print("both numbers are greater than 100")
else:
    print("both numbers are not greater than 100")

if num1 % 2 == 0 or num1 % 2 == 0:
    print("at least one of them is even")
else:
    print("at least one of them is odd")

if num1 < 100 or num2 < 100:
    print("at least one of them is under 100")
else:
    print("at least one of them is not under 100")

if num1 != num2:
    print("they are not equal")

if num1 != 0 & num2 != 0:
    print("they are not equal to 0")


if num1 > 0:
    print("num1 is positive")
elif num1 < 0:
    print("num1 is negative")
else:
    print("number must be 0")
