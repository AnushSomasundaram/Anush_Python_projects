#Write a program to evaluate a given polynomial.
# y=5X6+3X5+9 ifx>=0.

x=input(("Enter the value of x:-"))

x=int(x)

if x <= 0:
    print("The value of x is less than zero, please enter only positive numbers. Restart me.")
    exit()
else:
    y = 5*(x**6)+3*(x**3)+9
    print("The value of y after evaluation of the polynomial y=5X^6 + 3X^5 + 9 is ",y,".")
    exit()

