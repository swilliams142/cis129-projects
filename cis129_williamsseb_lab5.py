# cis129_williamsseb_lab5.py
# Module 5 Lab 5
# Author: Sebastian Williams
# CIS129 - CRN 30746
# 19 JUN 2024

"""Tracks the number of bottles returned over a week and prints the total bottles
and the total paid."""

# Declare local variables
todays_bottles = 0
total_bottles = 0
counter = 0
total_payout = 0
keep_going = 'y'

# Collects bottle data over 7 days, sums the bottles collected and calculates the total payout based of total number of bottles.
while (keep_going == 'y'):
    while counter < 7: #Stops loop at the 7th day
        counter += 1 
        todays_bottles = int(input(f'Enter number of bottles returned for day #{counter}: '))
        total_bottles = total_bottles + todays_bottles 
    total_payout = total_bottles * 0.10
    print(f'The total number of bottles collected this week was {total_bottles} and the payout was ${total_payout:.2f}.')
    print()
    counter = 0 # Resets loop to 1st day
    total_bottles = 0 # Resets total of bottles for new week
    keep_going = input('Do you want to enter another week’s worth of data? (y or n)? ') # Allows user to restart the program
    

    