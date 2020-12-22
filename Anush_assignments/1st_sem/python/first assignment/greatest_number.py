#Write a program to find the greatest of 3 numbers.

numbers=[]

i=0

while i<3:
    x=input("Enter the element:-")
    x = int(x)
    numbers.append(x)
    i=i+1

max=max(numbers)

print("The maximum value in the list of numbers is",max,".")


