# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:24:56 2020

@author: Zach
"""

def maxProfit(prices):
    total = 0
    for i in range(len(prices) - 1):
        if prices[i+1] > prices[i]: total += prices[i+1] - prices[i]     
            
    return total

