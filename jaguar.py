from car import Car

class Jaguar(Car):
  def __init__ (self):
    self.fuel_capacity = 0
  def drive(self):
        print("I'm in my Jaguar!!!")

  def turn(self, direction):
    self.direction = direction
    print (f"This Jaguar is turning {self.direction}!")
