# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:19:29 2020

@author: Zach
"""
def lastStoneWeight(stones):

    
    def removeStone(stonesList):
       if len(stonesList) == 1: 
           return stonesList
       stonesList.sort(reverse = True)
       if stonesList[0] != stonesList[1]: 
           newStone = stonesList[0] - stonesList[1]
           stonesList.append(newStone)
       stonesList.pop(1)
       stonesList.pop(0)
       return removeStone(stonesList)
        
    return removeStone(stones)
    
