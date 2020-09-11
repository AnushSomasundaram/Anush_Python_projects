#the type fuction type() shows the user what type of data a given variable or value is
#"""The ord() function in Python accepts a string of length 1 as an argument and returns the 
# unicode code point representation of the passed argument.
# For example ord('B') returns 66 which is a unicode code point value of character 'B'."


(a)=(input("Enter a number:-\t"))
(b)=(input("Now enter another number:-\t"))

sum=a+b
print("Data Type of the variable sum :-",sum,type(sum))

sum=int(a)+int(b)
print("Data Type of the variable sum :-",sum,type(sum))

sum=float(sum)
print("Data Type of the variable sum :-",sum,type(sum))


sum=chr(int (sum))
print("Data Type of the variable sum :-",sum,type(sum))
