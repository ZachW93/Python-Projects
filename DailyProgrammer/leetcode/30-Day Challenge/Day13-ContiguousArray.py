# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:19:12 2020

@author: Zach
"""

def findMaxLength(nums):
    
    def currMaxLength(numArray):
        
        zeroes = 0
        ones = 0
        
        for i in range(len(numArray)):
            if (max(zeroes, ones) - min(zeroes, ones)) > (len(numArray) - i):
                break
            
            if numArray[i] == 1:
                ones += 1
            else:
                zeroes += 1

        return min(zeroes, ones)*2
    
    return max(currMaxLength(nums), currMaxLength(nums[::-1]))
    
print(findMaxLength([1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1]))



        