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


while True:

    print(f"1. show balance")
    print(f"2. deposit")
    print(f"3. withdraw")
    print(f"4. exit")
    try:
        choice = int(input("please enter number of your selection"))
    except ValueError:
        print("That is not a valid number. Please enter digits only")
        continue
    except Exception as e:
        print(e)
        continue
    # Decision: match compares "choice" to each case and runs the matching block
    match choice:

        case 1:
            print(f"your balance is: ${balance:.2f}")
        case 2:
            try:
                print("Deposit")
                deposit = float(input("How much is your deposit?"))
                balance += deposit
                print(f"your new balance is: ${balance:.2f}")
            except ValueError:
                print("That is not a valid number. Please enter digits only")
                continue
            except Exception as e:
                print(e)
                continue
        case 3:
            try:

                print("withdraw")
                withdraw = float(input("how much is your withdraw?"))
                if withdraw > balance:
                    print("not enough funds")
                    continue
                balance = balance - withdraw
                print(f"your new balance is: ${balance:.2f}")
            except ValueError:
                print("That is not a valid number. Please enter digits only")
                continue
            except Exception as e:
                print(e)
                continue
        case 4:
            print("goodbye")
            break
        case _:
            print("There was a data entry error")
            continue
