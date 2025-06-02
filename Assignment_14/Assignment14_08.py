# Create a class Vehicle with a method start(). Derive a class Car and override the method start() with additional behavior. Show method overriding.

class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car is starting with ignition and engine roar...")

# Creating objects and calling methods
vehicle1 = Vehicle()
vehicle1.start()

car1 = Car()
car1.start()
