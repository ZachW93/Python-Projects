# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:03:10 2020
@author: Zach W


Challenge: [Easy] Necklace Matching

Imagine a necklace with lettered beads that can slide along the string. Here's an example image. 
In this example, you could take the N off NICOLE and slide it around to the other end to make ICOLEN. 
Do it again to get COLENI, and so on. For the purpose of today's challenge, 
we'll say that the strings "nicole", "icolen", and "coleni" describe the same necklace.

Generally, two strings describe the same necklace if you can remove some number 
of letters from the beginning of one, attach them to the end in their original ordering, 
and get the other string. Reordering the letters in some other way does not, in general, 
produce a string that describes the same necklace.

Write a function that returns whether two strings describe the same necklace.

Expected Output:
    
same_necklace("nicole", "icolen") => true
same_necklace("nicole", "lenico") => true
same_necklace("nicole", "coneli") => false
same_necklace("aabaaaaabaab", "aabaabaabaaa") => true
same_necklace("abc", "cba") => false
same_necklace("xxyyy", "xxxyy") => false
same_necklace("xyxxz", "xxyxz") => false
same_necklace("x", "x") => true
same_necklace("x", "xx") => false
same_necklace("x", "") => false
same_necklace("", "") => true

@author: Zach
"""

#Defined function named "same_necklace" that will loop through a word to check
#if any variation of word (in particular order) will result in another word
#that was inputted.

def same_necklace(name1, name2):
    
    counter = 0;
    
    if len(name1) == len(name2):
        
        if name1 == name2:
            
            print("True")
            
        else:
        
            for i in range(len(name1)):
            
                counter = counter + 1;
                
                newName = name1[i:] + name1[:i]
                
                if newName == name2:
                    
                    print("True")
                    break
                
                elif counter == len(name1):
                        
                    print("False")
                    break
                    
                else:

                    continue                      
        
    else:
        print("False")

#necklaceName1 = input("Please enter the first name of your necklace: ")
#necklaceName2 = input("Please enter the second name of your necklace: ")

same_necklace("nicole", "icolen")
same_necklace("nicole", "lenico")
same_necklace("nicole", "coneli")
same_necklace("aabaaaaabaab", "aabaabaabaaa")
same_necklace("abc", "cba")
same_necklace("xxyyy", "xxxyy")
same_necklace("xyxxz", "xxyxz")
same_necklace("x", "x")
same_necklace("x", "xx")
same_necklace("x", "")
same_necklace("", "")
