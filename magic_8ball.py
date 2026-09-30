"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

import random

# TODO: Create a tuple of at least 8 responses
RESPONSES = (
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Doubtful",
    "of course",
    "Don't count on it",
    "Outlook not so good",
)

print("Welcome to the Digital Oracle!")

# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop


# the magic 8 ball

while True:
    user_input = input("what question do you have for the magic 8 ball?")
    clean_input = user_input.strip().lower()
    if clean_input == "quit":
        print("thank you for your question")
        break

    answer = random.choice(RESPONSES)
    print(answer)
