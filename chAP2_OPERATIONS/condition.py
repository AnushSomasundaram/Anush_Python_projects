# a tenery operator is an operator that evaluates an experssion for a true or false condition.
#"""If and else keywords are used for a conditional expression which is if and else in the same line"

a=1
b=2

print("\nVariable a is","one" if (a==1) else "not one")
print("\nVariable a is","even" if (a%2==0) else "not even")

print("\nVariable b is","one" if (b==1) else "not one")
print("\nVariable b is","even" if (b%2==0) else "not even")

max=a if(a>b) else b
print("max is the greater value between a and b and max is",max)
