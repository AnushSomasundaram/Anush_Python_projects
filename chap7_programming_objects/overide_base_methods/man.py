from person import *

class Man(Person):

    ''' A Derived class to define Man properties '''

    def speak(self,msg):

        print(self.name,":\n\tHello!",msg)
