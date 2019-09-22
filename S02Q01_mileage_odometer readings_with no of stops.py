NOD_OOD = float(input("The distance tavelled:"))

mileage = float(input("The mileage of the car is:"))

GallonsofFuelUsed = NOD_OOD/mileage

print( "The amount of GallonofFuelUsed is" + str(GallonsofFuelUsed))

Tankcapacity = float(input("The amount of fuel a tank can hold:"))

Stops = GallonsofFuelUsed // Tankcapacity

print("The number of times car stopped to fill the fuel tank is" + str(Stops))
