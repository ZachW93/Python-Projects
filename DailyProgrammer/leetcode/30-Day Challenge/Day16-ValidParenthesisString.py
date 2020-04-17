# -*- coding: utf-8 -*-
"""
Given a string containing only three types of characters: '(', ')' and '*', 
write a function to check whether this string is valid. We define the validity 
of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left 
parenthesis '(' or an empty string.

An empty string is also valid.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:

        left = 0
        right = 0
        
        for c in s:
            
            if c == ")":
        
                right -= 1
                left = max(left - 1, 0)
            
            elif c == "(":
            
                right += 1
                left += 1
                
            elif c == "*":
                
                left = max(left - 1, 0)
                right +=1
                
            
            if right < 0:
            
                return False
            
        check = max(left, 0)
        
        if check == 0:
            return True
        else:
            return False