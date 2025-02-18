class Student():
    def __init__(self,name,branch,year):
        self.name=name
        self.branch=branch
        self.year=year
    def details(self):
        print("name",self.name)
        print("Branch",self.branch)
        print("year",self.year)

object=Student("ram","cse",2023)
object.details()           
        