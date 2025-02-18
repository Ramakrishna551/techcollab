class Cat:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        print("object with name is {} created ".format(name))
    def talk(self):
        print("miyaaav") 
        # print("im sound like "+(str)self.name)
cat =Cat("puppy","white")
cat.talk()