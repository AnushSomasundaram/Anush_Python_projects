#this program is about attributes which each class in python already comes with
# dir(),__dict__,the dictionary of a base class includes its default __init__method

from Bird import *

zola = Bird("Beep, Beep!")

print("\nBuilt-in instance attributes")
for attrib in dir(zola):
    if attrib[0]=="_":
        print(attrib)

for item in Bird.__dict__:
    print(item,":",Bird.__dict__[item])

print("\n Instance Dictionary")


for item in zola.__dict__:
    print(item,":",zola.__dict__[item])

print("\n Instance Dictionary")


