# This script creates a receipt for a coffee shop purchase
# Author: Sebastian Williams
# CIS129 - CRN 30746

# Sets the sales tax and the price of the coffee and muffins

CoffeePrice = 5
MuffinPrice = 4
SalesTax = 0.06

class NegativeError(Exception):
    #Creates a custom error for negative values
    pass

# Requests the number of coffees and muffins the customer would like
# then tries to convert that input to an interger. Throws errors if
# the customer inputs a non-interger value such as text or a float
# or if the customer attempts to order a negative value.

while True:
    CoffeeOrder = input('How many coffees would you like? ')
    
    try:
        CoffeeOrder = int(CoffeeOrder)
        if CoffeeOrder < 0:
            raise NegativeError
        break
    
    except ValueError:
        print('Please enter only numerical digits.')
        print('Orders must be whole numbers.')
        print()
        
    except NegativeError:
        print('Orders cannot be negative.')
        print()
        
while True:
    MuffinOrder = input('How many muffins would you like? ')
    
    try:
        MuffinOrder = int(MuffinOrder)
        if MuffinOrder < 0:
            raise NegativeError
        break
    
    except ValueError:
        print('Please enter only numerical digits.')
        print('Orders must be whole numbers.')
        print()
        
    except NegativeError:
        print('Orders cannot be negative.')
        print()

# Calculates the price of all the muffins and all of the coffees then sums
# the two into a subtotal. Then calculates the tax and the final total. Formats
# the tax as a currency with two decimal places.

from decimal import Decimal

CoffeeTotal = CoffeeOrder * CoffeePrice
MuffinTotal = MuffinOrder * MuffinPrice
Subtotal = CoffeeTotal + MuffinTotal
Tax = Decimal(Subtotal * SalesTax)
QuantizedTax = Tax.quantize(Decimal('0.01'))
Total = Subtotal + QuantizedTax

# Prints a receipt if an order was placed. Prints a message if no order was placed.
if Subtotal > 0:
    print()
    print('***************************************')
    print("Seb's Fantastic Coffee & Muffins")
    print('Number of Coffees Bought?')
    print(CoffeeOrder)
    print('Number of Muffins Bought?')
    print(MuffinOrder)
    print('***************************************')
    print()
    print('***************************************')
    print("Seb's Fantastic Coffee & Muffins Receipt")
    # Changes grammar based on number of coffees and muffins ordered.
    if CoffeeOrder == 1:
        print('1 Coffee at $5 each: $5.00')
    if CoffeeOrder > 1:
        print(CoffeeOrder, 'Coffees at $5 each: ${price}.00'.format(price = CoffeeTotal))
    if MuffinOrder == 1:
        print('1 Muffin at $4 each: $4.00')
    if MuffinOrder > 1:
        print(MuffinOrder, 'Muffins at $4 each: ${price}.00'.format(price = MuffinTotal))
    print('6% Tax: ${tax}'.format(tax = QuantizedTax))
    print('---------')
    print('Total: ${total}'.format(total = Total))
    print('***************************************')
if Subtotal == 0:
    print()
    print('No order was placed at this time.')
