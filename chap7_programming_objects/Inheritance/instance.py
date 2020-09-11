from Bird import *

print("\nClass Instances of\n",Bird.__doc__)

polly=Bird('Squack,Squack!')

print("\n Number of birds:",polly.count)
print("Polly says",polly.talk())

harry=Bird("Tweet, Tweet!")

print("\n Number of birds:",harry.count)
print("Polly says",harry.talk())

