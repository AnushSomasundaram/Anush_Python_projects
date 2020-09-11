class Songbird:

    def __init__(self,name,song):
        self.name=name
        self.song=song
        print(self.name,"Is born...")

    def sing(self):
        print(self.name,"sings:",self.song)

# the __del__ is a destructor method...it will delete the instance objects of the class 
    def __del__(self):
        print(self.name,"Flew Away!\n")
