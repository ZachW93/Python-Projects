'''
Problem:

The Revised Julian Calendar is a calendar system very similar to the familiar Gregorian Calendar,
but slightly more accurate in terms of average year length. The Revised Julian Calendar has a leap 
day on Feb 29th of leap years as follows:

Years that are evenly divisible by 4 are leap years.
Exception: Years that are evenly divisible by 100 are not leap years.
Exception to the exception: Years for which the remainder when divided by 900 is either 200 or 600 are leap years.
For instance, 2000 is an exception to the exception: the remainder when dividing 2000 by 900 is 200. 
So 2000 is a leap year in the Revised Julian Calendar.

Challenge and output:

Given two positive year numbers (with the second one greater than or equal to the first), 
find out how many leap days (Feb 29ths) appear between Jan 1 of the first year, and Jan 1 of 
the second year in the Revised Julian Calendar. This is equivalent to asking how many leap years 
there are in the interval between the two years, including the first but excluding the second.

leaps(2016, 2017) => 1
leaps(2019, 2020) => 0
leaps(1900, 1901) => 0
leaps(2000, 2001) => 1
leaps(2800, 2801) => 0
leaps(123456, 123456) => 0
leaps(1234, 5678) => 1077
leaps(123456, 7891011) => 1881475

For this challenge, you must handle very large years efficiently, much faster than checking 
each year in the range.

leaps(123456789101112, 1314151617181920) => 288412747246240
'''


#There are 24 leap years between 0-100 (excluding 100) in the gregorian caledar.
#Using this knowledge we can determine how many leap years there are and subtract
#the outliers. Not all inputs will start and end at a number divisible by 100. 
#Thus we will create a function for "firstleapyear" to find out where the leap
#years start, and go from there.

def leaps(year1, year2):
    
    leapYearCounter = 0;
    currentYear = year1;
    
    while leapYearCounter < 1:
        
        if currentYear % 4 == 0:
        
            if (currentYear % 100 == 0) & (currentYear % 900 != (200 or 600)):
                
                currentYear += 1;
                
            else:
                
                leapYearCounter += 1;
                
        else:
            
            currentYear += 1;
            
    if (currentYear < year2) & (year2 - currentYear < 5):
        
        return 1
    
    elif currentYear >= year2:
    
        return 0
    
    else:
        
        return 2
        
print(leaps(2001,2004))
print(leaps(2000,2004)) 
print(leaps(2000,2009))            
           
    

    
    
    
