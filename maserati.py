from car import Car

# Maserati
class Maserati(Car):
    def __init__(self):
        self.battery_kwh = 0

    def drive(self):
        print("Listen to me roar!")

    def turn(self, direction):
      self.direction = direction
      print (f"I'm turning {self.direction}!")

    def stop(self):
      self.direction = direction