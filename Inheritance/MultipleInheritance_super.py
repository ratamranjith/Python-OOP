'''
Python: Multiple Inheritance with Superclass

Explanation:
- This code demonstrates how to use multiple inheritance in Python.
- It defines a base class called 'Vehicle' and two subclasses 'Car' and 'Motorcycle'.
- A new class 'HybridVehicle' inherits from both 'Car' and 'Motorcycle', demonstrating multiple inheritance.
- The 'start_engine' method in 'HybridVehicle' calls the 'start_engine' method from both parent classes, illustrating how multiple inheritance works in Python.
'''

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("The engine is starting...")
        print("The vehicle is ready to move.")

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def start_engine(self):
        print("The car's engine is starting...")
        print("The car is ready to move.")
        super().start_engine()
        print("The car's engine is running...")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size

    def start_engine(self):
        print("The motorcycle's engine is starting...")
        print("The motorcycle is ready to move.")
        super().start_engine()
        print("The motorcycle's engine is running...")

# Multiple inheritance: A hybrid vehicle that can be both a car and a motorcycle
class HybridVehicle(Car, Motorcycle):
    def __init__(self, brand, model, year, doors, engine_size):
        Car.__init__(self, brand, model, year, doors)
        Motorcycle.__init__(self, brand, model, year, engine_size)

    def start_engine(self):
        print("The hybrid vehicle's engine is starting...")
        Car.start_engine(self)
        Motorcycle.start_engine(self)
        print("The hybrid vehicle is running...")

hybrid = HybridVehicle("Tesla", "Model X", 2023, 4, "Electric")
hybrid.start_engine()