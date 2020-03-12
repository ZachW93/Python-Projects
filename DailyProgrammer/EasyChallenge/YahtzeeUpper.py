# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:20:27 2020

@author: Zach

Challenge: [Easy] Yahtzee Upper Section Scoring

The game of Yahtzee is played by rolling five 6-sided dice, and scoring the 
results in a number of ways. You are given a Yahtzee dice roll, represented 
as a sorted list of 5 integers, each of which is between 1 and 6 inclusive. 
Your task is to find the maximum possible score for this roll in the upper 
section of the Yahtzee score card. Here's what that means.

For the purpose of this challenge, the upper section of Yahtzee gives you six 
possible ways to score a roll. 1 times the number of 1's in the roll, 2 times 
the number of 2's, 3 times the number of 3's, and so on up to 6 times the 
number of 6's. For instance, consider the roll [2, 3, 5, 5, 6]. If you scored 
this as 1's, the score would be 0, since there are no 1's in the roll. If you 
scored it as 2's, the score would be

Expected Output: 
    
yahtzee_upper([2, 3, 5, 5, 6]) => 10
yahtzee_upper([1, 1, 1, 1, 3]) => 4
yahtzee_upper([1, 1, 1, 3, 3]) => 6
yahtzee_upper([1, 2, 3, 4, 5]) => 5
yahtzee_upper([6, 6, 6, 6, 6]) => 30


"""

def yahtzee_upper(yahtzeeRoll):
    
    yahtzeeDict = {}
    score = 0;
    
    for roll in range(1,7):
        
        yahtzeeDict[roll] = roll*yahtzeeRoll.count(roll)
        
        if yahtzeeDict[roll] > score:
            
            score = yahtzeeDict[roll]
            
        else: 
        
            continue
        
    print(score)
            
    

yahtzee_upper([2, 3, 5, 5, 6])
yahtzee_upper([1, 1, 1, 1, 3])
yahtzee_upper([1, 1, 1, 3, 3])
yahtzee_upper([1, 2, 3, 4, 5])
yahtzee_upper([6, 6, 6, 6, 6])
            
        