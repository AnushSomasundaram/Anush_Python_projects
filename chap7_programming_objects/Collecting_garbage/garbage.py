from songbird import *

bird1 = Songbird("Koko","Tweet Tweet!")
print(bird1.name,"ID:",id(bird1))
bird1.sing()

del bird1

bird2 = Songbird("toto","sweet sweet!")
print(bird2.name,"ID:",id(bird2))
bird2.sing()


bird3 = Songbird("Polo","yeet yeet!")
print(bird3.name,"ID:",id(bird3))
bird3.sing()

del bird2
del bird3

