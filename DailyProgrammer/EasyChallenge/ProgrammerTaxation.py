'''
The nation of Examplania has the following income tax brackets:

income cap      marginal tax rate
  ¤10,000           0.00 (0%)
  ¤30,000           0.10 (10%)
 ¤100,000           0.25 (25%)
    --              0.40 (40%)
If you're not familiar with how tax brackets work, see the section below for 
an explanation.

Given a whole-number income amount up to ¤100,000,000, find the amount of tax 
owed in Examplania. Round down to a whole number of ¤.
'''

import math

def tax(income):
    
    total_tax = 0;
    tax1 = .1;
    tax2 = .25;
    tax3 = .4;
    
    if income > 100000:
        
        income -= 100000
        total_tax += tax3*income
        
    if income > 30000:
        
        income -= 30000
        total_tax += tax2*income
    
    if income > 10000:
        
        income -= 10000
        total_tax += tax1*income
    
    total_tax = math.floor(total_tax)
    return total_tax


tax(0)
tax(10000)
tax(10009)
tax(10010)
tax(12000)
tax(56789)
tax(1234567)