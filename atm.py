"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a "while True" loop to remain awake.
[ ] 3. Main menu uses match-case logic for selections.
[ ] 4. Inputs are validated (e.g., .isdigit()) to prevent crashes.
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

balance = 1000.00
choice = 1
while choice > 0 and choice < 5:
    print(f"1. show balance")
    print(f"2. deposit")
    print(f"3. withdraw")
    print(f"4. transfer")
    print(f"5. exit")
    choice = int(input("please enter number of your selection"))

    # Decision: match compares "choice" to each case and runs the matching block
    match choice:

        case 1:
            print(f"your balance is: ${balance:.2f}")
        case 2:
            print("Deposit")
            deposit = float(input("How much is your deposit?"))
            balance = balance + deposit
            print(f"your new balance is: ${balance:.2f}")
        case 3:
            print("withdraw")
        case 4:
            print("transfer")
        case 5:
            print("goodbye")
