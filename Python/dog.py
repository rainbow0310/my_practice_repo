class Dog:
    def __init__(self, name, breed, age, energy_level = 10, is_hungry = True):
        self.name = name   
        self.breed = breed
        self.age = age
        self.energy_level = energy_level  
        self.is_hungry = is_hungry    

    def __str__(self):
        return f"{self.name}  : {self.breed}"
    
    def feed(self):
        self.is_hungry = False
    
    def play(self):
        if self.is_hungry == False:
            self.is_hungry = True
            self.energy_level -= 1
        else:
            print("dog is hungry and will not play")
    
    def rest(self):
        energy_level += 1

    
    def get_is_hungry(self):
        return self.is_hungry
    
    def get_energy_level(self):
        return self.energy_level