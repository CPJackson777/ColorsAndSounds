from car import Car

class MB(Car):
    def __init__(self):
        self.fuel_capacity = 0

    def drive(self):
        print("test drive")

    def turn(self, direction):
      self.direction = direction
      print (f"I'm turning {self.direction}!")

    def stop(self):
      self.direction = direction