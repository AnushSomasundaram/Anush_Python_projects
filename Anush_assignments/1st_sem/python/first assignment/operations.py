"""Write a Python program that allows the user to enter two integer values,
and displays the results when each of the following arithmetic operators are applied. For example, 
if the user enters the values 7 and 5, the output would be,
7+5=12
7-5=2 and so on."""

number1=int(input("Please enter the first integer:-"))

number2=int(input("\nPlease enter the second integer:-"))

sum=number1+number2

difference=number1-number2


print("\The sum of the two integers is",number1,"+",number2,"=",sum," .")

print("\nThe difference between the two integers is",number1,"-",number2,"=",difference," .")
