class Student: 
    def __init__(self, fname, lname, id, energy_level=0.0):
        self.fname = fname   
        self.lname = lname
        self.id = id
        self.energy_level = energy_level      

    def __str__(self): #this is the dunder method
        return f"{self.lname}  :  {self.id}"
    
    def greeting(self):
        print("Hi! my name is " + self.fname, self.lname + ".")
    
    def take_exam(self):
        self.energy_level -= 1

    def get_energy_level(self):
        return self.energy_level