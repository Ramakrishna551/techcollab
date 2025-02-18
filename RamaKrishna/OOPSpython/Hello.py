class Hello:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name    

hel=Hello("Hello world")
# hel.name()
print(hel)