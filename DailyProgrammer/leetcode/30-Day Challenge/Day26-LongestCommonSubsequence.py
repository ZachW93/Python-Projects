# -*- coding: utf-8 -*-
"""
Given two strings text1 and text2, return the length of their longest common 
subsequence.

A subsequence of a string is a new string generated from the original string 
with some characters(can be none) deleted without changing the relative order 
of the remaining characters. (eg, "ace" is a subsequence of "abcde" while 
"aec" is not). A common subsequence of two strings is a subsequence that is 
common to both strings.


If there is no common subsequence, return 0.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def checkCommon(list1, list2, num):
    
            commonText1 = []
            commonText2 = []
            
            for letter in list1:
                phlist2 = list(list2)
                if letter in phlist2:
                    commonText1.append(letter)
                    phlist2.pop(phlist2.index(letter))
                    
            for letter in list2:
                phlist1 = list(list1)
                if letter in phlist1:
                    commonText2.append(letter)
                    phlist1.pop(phlist1.index(letter))
                    
            if commonText1 == []:
                return num
            elif commonText1 == commonText2:
                num += len(commonText1)
                return num
            
            for i in range(len(commonText1)):     
                shiftList = commonText1[i:] + commonText1[:i]      
                if shiftList == commonText2:
                    
                    num += i
                    return num

            if commonText1[0] == commonText2[0]:
                num += 1
                commonText2.pop(0)
                commonText1.pop(0)
            else:
                commonText2.remove(commonText1[0]) 
                commonText1.pop(0)                               
            print(commonText1, commonText2, num)   
            return checkCommon(commonText1, commonText2, num)
                    
        text1List = [i for i in text1]
        text2List = [j for j in text2]
        
        common = 0

        return checkCommon(text1List, text2List, common)
