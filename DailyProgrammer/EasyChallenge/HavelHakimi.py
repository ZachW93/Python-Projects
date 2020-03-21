'''
Problem:
It was a dark and stormy night. Detective Havel and Detective Hakimi arrived 
at the scene of the crime.

Other than the detectives, there were 10 people present. They asked the first 
person, "out of the 9 other people here, how many had you already met before 
tonight?" The person answered "5". They asked the same question of the second 
person, who answered "3". And so on. The 10 answers they got from the 10 people 
were:

5 3 0 2 6 2 0 7 2 5
The detectives looked at the answers carefully and deduced that there was an 
inconsistency, and that somebody must be lying. (For the purpose of this 
challenge, assume that nobody makes mistakes or forgets, and if X has met 
Y, that means Y has also met X.)

Your challenge for today is, given a sequence of answers to the question 
"how many of the others had you met before tonight?", apply the Havel-Hakimi 
algorithm to determine whether or not it's possible that everyone was telling 
the truth.

If you're feeling up to it, skip ahead to the Challenge section below. 
Otherwise, try as many of the optional warmup questions as you want first, 
before attempting the full challenge.    
'''



'''
PART 1: Given a sequence of answers, return the same set of answers with all the 
0's removed.
'''

def elim0s(values):
    
    return list(filter(lambda num: num != 0, values))
    
'''
PART 2: Given a sequence of answers, return the sequence sorted in descending 
order, so that the first number is the largest and the last number is the 
smallest.
'''

def greatestToLeast(values):
    
    return values.sort(reverse = True)

'''
PART 3: Given a number N and a sequence of answers, return true if N is greater 
than the number of answers (i.e. the length of the sequence), and false if N is 
less than or equal to the number of answers. For instance, given 7 and 
[6, 5, 5, 3, 2, 2, 2], you would return false, because 7 is less than or equal 
to 7.
'''

def isGreaterThanLength(num, values):
    if num > len(values):
        return True
    else:
        return False

'''
PART 4: Given a number N and a sequence in descending order, subtract 1 from 
each of the first N answers in the sequence, and return the result. For 
instance, given N = 4 and the sequence [5, 4, 3, 2, 1], you would subtract 1 
from each of the first 4 answers (5, 4, 3, and 2) to get 4, 3, 2, and 1. The 
rest of the sequence (1) would not be affected:
'''

def subtractOne(size, values):
    
    list(filter(lambda num: num - 1, values))  
    return values[0:size]
