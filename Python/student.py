class Student:
    def __init__(self, fname, lname, id, energy_level =10): # you dont call init method, it calls itself
        self.fname = fname   
        self.lname = lname
        self.id = id
        self.energy_level = energy_level      

    def __str__(self):
        return f"{self.lname}  : {self.id}"
    
    def greeting(self):             #you don't need to add any otehr variables besides self unless it's an input
        print("Hi! My name is " + self.fname + " " + self.lname)

    def take_exam(self):
        self.energy_level -= 1      #don't forget to add "self."

    def get_energy_level(self):
        return self.energy_level