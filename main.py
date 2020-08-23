from jaguar import Tesla
from maserati import Zero
from mercedes import Cessna
from rezvani import MB

# Define 5 of your favorite vehicles
# car1 = {"make": Porsche, "color": "Black", top_speed=140 }
# car2 = {"make": Jaguar, "color": "Gray", top_speed=100 }
# car3 = {"make": Audi, "color": "Red", top_speed=110}
# car4 = {"make": BMW, "color": "White", top_speed=120}
# car5 = {"make": Subaru, "color": "Blue", top_speed=200}

# Move all common properties in your vehicles to a new Vehicle class.
# class Vehicle:
#   def __init__(self, make, color, top_speed, wheels=4):
#     self.wheels = wheels
#     self.make = make
#     self.color = color
#     self.top_speed = top_speed
#   def drive(self):
#     print(f"I'm driving in my {self.make} La la la la la")

# Create an instance of each vehicle.
# Define a different value for each vehicle's properties.

# car1 = Vehicle("Porsche", "Black", 140)
# car2 = Vehicle("Jaguar", "Gray", 100)
# car3 = Vehicle("Audi", "Red", 110)
# car4 = Vehicle("BMW", "White", 120)
# car5 = Vehicle("Subaru", "Blue", 200)

# Create a drive() method in the Vehicle class.
# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").

f_type = Jaguar()
amg = MB()
ghibli = Maserati()
tank = Rezvani()

f_type.drive()
amg.drive()
ghibli.drive()
tank.drive()

f_type.turn("left")
f_type.stop()

amg.turn("left")
amg.stop()