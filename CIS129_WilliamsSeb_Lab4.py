# CIS129_WilliamsSeb_Lab4.py
# Module 4 Lab 4
# Author: Sebastian Williams
# CIS129 - CRN 30746
# 18 JUN 2024

""""This program obtains the monthly sales and sales increase percent and then 
determines and prints the store bonus and employee bonus."""

# declare local variables
monthlySales = None  # monthly sales amount
storeAmount = None  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase

# Defines a function to get a value to assign to a variable after a prompt
def getValue(value, prompt):
    while True:
        try:
            value = float(input(prompt).rstrip('%').replace(',', '')) #Removes percent symbols and commas
            return value
            break
        except ValueError: #Reprompts user if a letter or random symbol is entered
            print('Please only enter numerical digits and decimals.')
            print()


# Gets the monthly sales and sales increase
monthlySales = getValue(monthlySales, 'Monthly Sales: $')
salesIncrease = getValue(salesIncrease, 'Percentage of Sales Increase: ')
salesIncrease = salesIncrease / 100

# This code determines the storeAmount bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# This code determines the empAmount bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

# This code prints the bonus information
print()
print("The store bonus amount is $" + str(storeAmount))
print("The employee bonus amount is $" + str(empAmount))
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ')



