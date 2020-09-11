#getattr() , hasattr(), setattr(), delattr()

from Bird import *

chick=Bird("cheep ,cheep!")

chick.age="1 week"

print("\nChick says ",chick.talk())

chick.age="2 weeks"
print("Chick Now",chick.age)

setattr(chick,"age","3 weeks")

print("\bChick attributes:")
for attr in dir(chick):
    
    if attr[0]!="_":
        print(attr,":",getattr(chick,attr))

delattr(chick,"age")
print("\n Chick Age attribute?",hasattr(chick,"age"))


