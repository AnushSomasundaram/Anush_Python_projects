from person import *

class Hombre(Person):

    ''' A Derived class to define Hombre properties '''

    def speak(self,msg):

        print(self.name,":\n\tHola!",msg)
