"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

# Get gross income and expenses from the user
# input() reads values as text (strings),so float()converts them to numberswith decimals for calculation

gross_income = float(input("what is your gross monthly income? "))
car = float(input("what do you spend on your car? "))
housing = float(input("what do you spend on rent?"))
internet = float(input("what do you spend on internet?"))
groceries = float(input("what do you spend on groceries?"))
phone = float(input("what do you spend on your phone?"))


# calculate net income assuming a 20% tax deduction (retaining 80%)
net_income = gross_income * 0.8

# Sum up monthly costs
total_expenses = car + housing + internet + groceries + phone

# Find the remaing disposable income
remaining_income = net_income - total_expenses
# calculate percent spent total expenses divided by net income

# Format and display total expenses
# format and display remaining
# format and display percent spent
# $ prints as a literal dollar sign in front
# , adds thousand separator commas
# .2f specifies 2 decimal places of floating-point precision
print(f"\n\nyou spent a total of ${total_expenses: ,.2f}")

# calculate and display the expenses a percentage of net income

# .2f multiplies the result by 100, rounds to 2 decimal places, and andappends the % sign
print(f"that was {total_expenses/net_income:,.2%} of your net income")
print(f"this is how much money you have left{remaining_income:,.2f}")
