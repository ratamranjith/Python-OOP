'''
Python: MultilLevel Inheritance with super class

Explanation:
In this example, we have a super class called 'Vehicle' and two sub classes 'Car'
and 'Motorcycle'. The 'Car' and 'Motorcycle' classes inherit the properties and
methods of the 'Vehicle' class.
'''
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # Initialize mileage

    def drive(self, miles):
        self.mileage += miles

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size

# Creating instances
car = Car('Toyota', 'Camry', 2015, 4)
motorcycle = Motorcycle('Honda', 'CBR500R', 2018, 500)

# Accessing properties
print(car.brand)  # Output: Toyota
print(car.model)  # Output: Camry
print(car.year)   # Output: 2015