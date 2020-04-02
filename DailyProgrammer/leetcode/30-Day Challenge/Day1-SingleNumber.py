'''
Problem: Given a non-empty array of integers, every element appears twice 
except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement 
it without using extra memory?
'''
class Solution:
    def singleNumber(self, numList):
        numList = sorted(numList)
        if len(numList) == 1: return numList[0]
        for i in range(0, len(numList)):
            try:
                if numList[i-1] == numList[i] or numList[i] == numList[i+1]:
                    continue
                else:
                    return numList[i]
            except:
                return numList[i]