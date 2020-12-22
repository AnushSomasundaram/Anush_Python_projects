#For every number from 1 to n, find how many digits of that number is odd and display along with the number

def no_of_odd_digits(number):

    print("The given number is ",number)
    
    number=str(number)
    
    count=0
    
    for ele in number:
        #print(ele)
        if (int(ele)%2)!=0  :
            count = count+1
            #print (count)
        
    print("There are",count,"odd digits")

    if count>0:
        print("The odd digits in the number are:-")
        
        for ele in number:
                if (int(ele)%2)!=0:
                    print(ele)
    else:
        print("There are no odd numbers to display")


no_of_odd_digits(123456)