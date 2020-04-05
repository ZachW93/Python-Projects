# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:47:53 2020

@author: Zach
"""

def moveZeroes(numberList):
    i = 0
    zeros = 0
    while i != len(numberList) - zeros:
        if numberList[i] == 0:
            numberList.append(0)
            numberList.pop(i)
            zeros += 1
        else:
            i+=1
