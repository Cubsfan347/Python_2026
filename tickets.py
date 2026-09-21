"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

tickets = list(range(1, 21))  # creating list of available tickets
while True:  # keep going til user says stop
    if len(tickets) == 0:
        print("there are no tickets available")
        break
    print(tickets)
    print("seats available")
    try:
        seat = int(input("please pick a seat, enter 0 to quit"))

        if seat == 0:
            print("goodbye")
            break

        else:
            tickets.remove(seat)
            continue
    except ValueError:
        print("that seat is not available. Make sure you've entered a number")
        continue
