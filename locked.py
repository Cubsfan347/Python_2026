"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

# declare variables/data structures
DEPARTMENT_NAME = "Accounting"
USER_NAMES = ("b_pommigero", "bjork52", "pinatapena", "aferrari", "amg4ever")
passwords = ["whistler4999", "bayern2026", "Jaguars5050", "Florida2200!", "Acmilan1899"]
# while loop
while True:
    print(f"1. lookup username")
    print(f"2. add username")
    print(f"3. change password")
    print(f"4. exit")
    # try
    try:
        choice = int(input("please enter number of your selection"))
    except ValueError:
        print("That is not a valid number. Please enter digits only")
        continue
    except Exception as e:
        print(e)
        continue

    match choice:

        case 1:
            name = input("please enter username to lookup")
            if name in USER_NAMES:
                print(f"{name} is an employee")
            else:
                print(f"{name} is not an employee")
            continue
        case 2:
            try:
                print("add username")
                name = input("please enter username to add")
                USER_NAMES.append(name)

            except Exception as e:
                print(e)
                continue
        case 3:
            try:

                print("change password")
                name = input("please enter the user name")
                if name in USER_NAMES:
                    # error checking
                    # print(passwords) - error check
                    location = USER_NAMES.index(name)
                    password = input("Enter new password")
                    passwords[location] = password
                    print("password has been changed")
                    # print(passwords) - error check
                else:
                    print("I'm sorry, that user does not exist")

            except Exception as e:
                print(e)
                continue
        case 4:
            print("goodbye")
            break
        case _:
            print("There was a data entry error")
            continue
