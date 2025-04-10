from car import Car
cars = []
with open("cars.txt") as file:
    for line in file:
            car_info = line.strip().split()  #removes the new line and then split it
            car_info[2] = int(car_info[2]) #makes the 3rd index of the string into int
            car_info[3] = int(car_info[3])
            one_car = Car(car_info[0], car_info[1], car_info[2], car_info[3])
            cars.append(one_car)
            print(Car)

car1 = cars[0]
car2 = cars[1]

print("car1 gas tank is: " + str(car1.get_gas_tank()))          #dont forget to add second set of parenthesees
print("car1 odometer is: " + str(car1.get_odomoter()))
car1.drive()
print("car1 gas tank is: " + str(car1.get_gas_tank()))          
print("car1 odometer is: " + str(car1.get_odomoter()))
#prints confirm that the gas and odometer do decrease and increase by the correct amounts based on the engine_type

print("car2 gas tank is: " + str(car2.get_gas_tank()))          
print("car2 odometer is: " + str(car2.get_odomoter()))
car2.drive()
print("car2 gas tank is: " + str(car2.get_gas_tank()))          
print("car2 odometer is: " + str(car2.get_odomoter()))