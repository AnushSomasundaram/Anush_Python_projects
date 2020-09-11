from man import *
from hombre import *
from person import *


guy1=Man('Richard')
guy2=Hombre("Ricardo")

guy1.speak("It's a beautiful evening")
guy2.speak("Es una tarde hermosa.\n")


Person.speak(guy1)
Person.speak(guy2)


