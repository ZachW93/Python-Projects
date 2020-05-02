'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
'''

def rangeBitwiseAnd(m, n):
    
    counter = 0
    
    while m != n:
        
        m >>= 1
        n >>= 1
        counter += 1
    
    output = m << counter
    
    return output
    
