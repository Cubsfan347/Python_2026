"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

try:

    fname = ""
    while not fname:
        fname = input("please enter your first name:  ")
        fname = fname.strip()

    lname = ""
    while not lname:
        lname = input("please enter your last name:  ")
        lname = lname.strip()

    age = -1
    while age < 0:
        age = int(input("please enter person's age  "))

    phone = ""
    while not phone:
        phone = input("please enter phone_number:  ")
        phone = phone.strip()

    ticket_count = -1
    while ticket_count < 0:
        ticket_count = int(input("how many tickets are you buying?:  "))

    additional_tickets = ""
    while additional_tickets != "Y" and additional_tickets != "N":
        additional_tickets = input("are additional tickets being sold?:(y/n)  ").upper()
except ValueError:
    print("i'm sorry, that is not a valid value")
except Exception as e:
    print(f"Error:{e}")
