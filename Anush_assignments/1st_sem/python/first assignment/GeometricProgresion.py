
# Write a program to find the biggest number in the  geometric progression with start value a and 
# common ratio r less than a given number n.


def Geometric_Progression_check(base_number, ratio ,highest_number):

    print(" Given:- Base =",base_number,"\n Ratio =",ratio,"\n Highest Number=",highest_number)
    
    target = int(highest_number/base_number)
    #print (target)
    
    exponent=0
    
    while (ratio**exponent) <= target:
        exponent = exponent+1
        #print(exponent)    
    
    exponent=exponent-1
    
    raised_ratio=(ratio ** exponent)
    required_value = base_number * raised_ratio

    
    print ("The highest number in the geometric progression before",highest_number,"is",required_value)

Geometric_Progression_check(2,3,56)

Geometric_Progression_check(1,2,17)