"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION B - EMOJI CIPHER
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. EMOJI_CIPHER constant maps every letter (A-Z) to an emoji.
[ ] 3. Program takes a word or phrase from the user.
[ ] 4. Program loops through characters and prints emojis.
[ ] 5. A 'try/except' block handles spaces or punctuation.
-----------------------------------------------------------------------
"""

# the dictionary maps each letter to an emoji
EMOJI_CIPHER = {
    "A": "🍎",
    "B": "🍌",
    "C": "🐱",
    "D": "🦴",
    "E": "🐘",
    "F": "🧊",
    "G": "🍇",
    "H": "🏠",
    "I": "🍦",
    "J": "🧊",
    "K": "🔑",
    "L": "🍋",
    "M": "🐵",
    "N": "🌙",
    "O": "🐙",
    "P": "🍑",
    "Q": "❓",
    "R": "🌹",
    "S": "⭐",
    "T": "🌴",
    "U": "🦄",
    "V": "🌋",
    "W": "💧",
    "X": "❌",
    "Y": "🌟",
    "Z": "🦋",
}
# menu repeats until user chooses to quit
while True:
    print()
    print("1 convert word to emojis")
    print("2 convert emojis to words")
    print("3 quit")

    choice = int(input("please pick a number: "))

    if choice == 1:
        message = input("Enter word: ").upper()
        # converts eachmessage character to an emoji
        for char in message:
            try:
                print(EMOJI_CIPHER[char], end=" ")
            except KeyError:
                print(" ", end=" ")

    elif choice == 2:
        message = input("Enter coded word: ")
        # search the dictionary for the letter matching each emoji
        for key in message:
            try:
                for item in EMOJI_CIPHER:
                    if key == EMOJI_CIPHER[item]:
                        print(item, end="")

            except KeyError:
                print(" ", end=" ")

    else:
        print("goodbye")
        break
    continue
