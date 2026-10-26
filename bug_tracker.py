"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime


def main():
    while True:
        current_time = datetime.datetime.now()
        print("creating bug entry")
        file_name = input("please enter file name")
        description = input("please describe the error")
        priority = input("priority level:high, medium, low")
        with open("bug_list.txt", "a") as f:
            f.write(f"{current_time}\n")
            f.write(f"file_name: {file_name}\n")
            f.write(f"description:{description}\n")
            f.write(f"priority:{priority}\n")
        another = input("do you want to enter another bug?y-n").upper()
        if another == "Y":
            continue
        else:
            break


main()
