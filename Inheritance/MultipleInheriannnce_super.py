'''
Python: Multiple Inheritance with super class

Explanation:
- The following code demonstrates how to use multiple inheritance in Python. 
- It defines a base class called 'Vehicle' and two subclasses 'Car' and 'Motorcycle'. 
- The 'Car' class inherits from 'Vehicle' and the 'Motorcycle' class also inherits from 'Vehicle'.
- The 'Car' class has a method called 'start_engine' and the 'Motorcycle' class has a method called 'start_engine' as well. 
- However, the 'start_engine' method in the 'Car' class is overridden by the 'start_engine' method in the class. 
- This is because the 'start_engine' method in the 'Motorcycle' class is called when we call the 'start_engine' method on an instance of the 'Motorcycle' class.
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

car = Car("Tata", "Sierra", 1999, 4)
car.start_engine()

motorCycle = Motorcycle("hero", "splendor", 1995, 2)
motorCycle.start_engine()