# This script creates a receipt for a coffee shop purchase
# Author: Sebastian Williams
# CIS129 - CRN 30746

# Sets the sales tax and the price of the goods sold
LattePrice = 8
CoffeePrice = 5
MuffinPrice = 4
DonutPrice = 3
SalesTax = 0.06

class NegativeError(Exception):
    #Creates a custom error for negative values
    pass

# Requests the number of each good the customer would like then
# tries to convert that input to an interger. Throws errors if
# the customer inputs a non-interger value such as text or a float
# or if the customer attempts to order a negative value.

while True:
    LatteOrder = input('How many lattes would you like? ')
    
    try:
        LatteOrder = int(LatteOrder)
        if LatteOrder < 0:
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

while True:
    DonutOrder = input('How many donuts would you like? ')
    
    try:
        DonutOrder = int(DonutOrder)
        if DonutOrder < 0:
            raise NegativeError
        break
    
    except ValueError:
        print('Please enter only numerical digits.')
        print('Orders must be whole numbers.')
        print()
        
    except NegativeError:
        print('Orders cannot be negative.')
        print()

# Calculates the price of all the goods ordered then sums the two into 
# a subtotal. Then calculates the tax and the final total. Formats the
# tax as a currency with two decimal places.

from decimal import Decimal

LatteTotal = LatteOrder * LattePrice
CoffeeTotal = CoffeeOrder * CoffeePrice
MuffinTotal = MuffinOrder * MuffinPrice
DonutTotal = DonutOrder * DonutPrice
Subtotal = LatteTotal + CoffeeTotal + MuffinTotal + DonutTotal
Tax = Decimal(Subtotal * SalesTax)
QuantizedTax = Tax.quantize(Decimal('0.01'))
Total = Subtotal + QuantizedTax

# Prints a receipt if an order was placed. Prints a message if no order was placed.
if Subtotal > 0:
    print()
    print('***************************************')
    print("Seb's Fantastic Cafe")
    print('Number of Lattes Bought?')
    print(LatteOrder)
    print('Number of Coffees Bought?')
    print(CoffeeOrder)
    print('Number of Muffins Bought?')
    print(MuffinOrder)
    print('Number of Donuts Bought?')
    print(DonutOrder)
    print('***************************************')
    print()
    print('***************************************')
    print("Seb's Fantastic Cafe")
    # Changes grammar based on number of each good ordered.
    if LatteOrder == 1:
        print('1 Latte at $8 each: $8.00')
    if LatteOrder > 1:
        print(LatteOrder, 'Lattes at $8 each: ${price}.00'.format(price = LatteTotal))
    if CoffeeOrder == 1:
        print('1 Coffee at $5 each: $5.00')
    if CoffeeOrder > 1:
        print(CoffeeOrder, 'Coffees at $5 each: ${price}.00'.format(price = CoffeeTotal))
    if MuffinOrder == 1:
        print('1 Muffin at $4 each: $4.00')
    if MuffinOrder > 1:
        print(MuffinOrder, 'Muffins at $4 each: ${price}.00'.format(price = MuffinTotal))
    if DonutOrder == 1:
        print('1 Donut at $3 each: $3.00')
    if DonutOrder > 1:
        print(DonutOrder, 'Donuts at $3 each: ${price}.00'.format(price = DonutTotal))
    print('6% Tax: ${tax}'.format(tax = QuantizedTax))
    print('---------')
    print('Total: ${total}'.format(total = Total))
    print('***************************************')
    print()
    print("Thank You for Visiting Seb's Cafe!")
    print('Please visit again soon!')
if Subtotal == 0:
    print()
    print('No order was placed at this time.')
    print("Thank You for Visiting Seb's Cafe!")
