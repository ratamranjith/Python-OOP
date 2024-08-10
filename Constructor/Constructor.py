'''
Python : Constructor

Description:
A constructor is a special method in Python classes. It is used to initialize the attributes of a class
when an object of that class is created.
'''

# Simple
class Satellite:
    
    def __init__(self): # Constructor
        print("Satellite Testing Started")
        

satellite = Satellite() # Constructor will always get executed. Careful while using the constructor

# With Variables
class Rocket:
       
    def __init__(self):
        self.name = "Douglas"
        self.speed = None

rocket = Rocket()
rocket.speed = "7.9 km/sec"
print(rocket.name) # Output: Douglas
print(rocket.speed) # Output: 7.9 km/sec


# Constructor with arguments
class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

car = Car("Black", "BMW", "1985")
print(car.color)
print(car.model)
print(car.year)


# Constructor will not support constructor overloading
class Bike:
    def __init__(self, color, model, year): # 1st Constructor
        self.color = color
        self.model = model
        self.year = year
    
    def __init__(self, color): # 2nd constructor
        self.color = color
        
        
bike = Bike("green") # 1st constructor will be getting neglected, it will take the latest constructor
print(bike.color)