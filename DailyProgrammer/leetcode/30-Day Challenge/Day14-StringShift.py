# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:22:11 2020

@author: Zach
"""

def stringShift(s, shift):  
    
    new_s = s
    length = len(new_s)    
        
    for i in range(len(shift)):
        if shift[i][0] == 0:
            new_s = new_s[(shift[i][1] % length):] + new_s[:shift[i][1] % length]
        else:
            new_s = new_s[-(shift[i][1] % length):] + new_s[:-(shift[i][1] % length)]
        
    return new_s

print(stringShift("abc", [[0,5]]))


