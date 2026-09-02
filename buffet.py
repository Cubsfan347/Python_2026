"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask the user for their age (convert to int) and the day of the week (convert to string).
2. Calculate the base price using if/elif/else:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Use a match/case statement to handle special daily rules based on the day entered:
   - Tuesday: Children through age 12 are half price!
   - Sunday: Drinks are free!
   - Other days: Standard buffet pricing in effect.
4. Print the final price formatted as currency and display any applicable daily special notices.
-----------------------------------------------------------------------
"""

# buffet calculator
age = int(input("What is the users age?"))
day = input("enter the day of the week").lower()
# matching day
match day:
    case "tuesday":
        if age <= 12:
            child_price = 0.5
    case "Sunday":
        print("drinks are free")
        child_price = 1
    case _:
        child_price = 1
# calculate by age

if age < 1:
    print("under 1: free")
    price = 0
elif age <= 11:
    print("1 to 11 is $1.00")
    price = age * child_price
elif age <= 64:
    print("12 to 64 is $16.95")
    price = 16.95
else:
    print("65 & older is $12.95")
    price = 12.95

print(f"price is  ${price:.2f}")
