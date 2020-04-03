# -*- coding: utf-8 -*-
"""
Problem: Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any 
positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), or it 
loops endlessly in a cycle which does not include 1. Those numbers for which 
this process ends in 1 are happy numbers.
"""

#Logic: When given a number, the more times you loop through the cycle, the 
#number gets smaller. Given this conjecture, there must be a time where the cycle
#either A) repeats or B) becomes 1. Using a while loop for the cycle, we can 
#append all new numbers to a list and check if the number has already been entered.
#If so, break the loop and return false.
    

def isHappy(number):
    
    numberList = []
    while number not in numberList:
        if number == 1: return True
        numberList.append(number)
        number = sum([int(i)**2 for i in str(number)])
    return False

    
