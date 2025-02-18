class Dog:
    def __init__(self,name):
        self.name=name
        print("object with name :{} created ".format(name))

    def talk(slef):
        print("woof!")
        
    def printname(self):
        print("my name is :{}".format(self.name))
    
    def __str__(self):
        return self.name
charlie =Dog("charile")
bruno=Dog("Bruno")
charlie.talk()
bruno.talk()
bruno.printname()
charlie.printname()