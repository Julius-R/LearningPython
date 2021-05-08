
class Doggo:
    def __init__(self, name, age, isGoodBoy):
        self.name = name
        self.age = age
        self.isGoodBoy = isGoodBoy  
      
    def bark(self):
        print("Woof!")
    

doge = Doggo("Bryce", 5, True)
doge.bark()


# Inheritance

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printName(self):
        print(f"{self.fname} {self.lname}")
        
        
class Employee(Person):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
    
j = Employee('Jason', 'Stanley', 57000)    
print(j.salary)
j.printName()