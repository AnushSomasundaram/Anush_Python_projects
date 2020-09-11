#When using a function from a module, use the syntax: module_name.function_name.

import math, random

print("Rounded up 9.5",math.ceil(9.5))
print("Rounded down 9.5",math.floor(9.5))

num=int(4)

print(num,"Squared:",math.pow(num,2))
print(num,"Square root",math.sqrt(num))

nums=random.sample(range(1,49),6)

print("Your lucky lotto numbers are:-",nums)

#guess=random.random()
#print("A random number between 0 and 1  is",guess)


