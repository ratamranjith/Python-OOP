'''

Python: Compile-Time (Method Overloading)

Explanation:
    In Python, method overloading is not supported at compile-time. However, we can achieve similar functionality
using default argument values or variable number of arguments.

In other words, Method overloading is a form of compile-time polymorphism where multiple methods share the same name but differ in the number or type of parameters.
Python doesn’t support traditional method overloading like Java or C++. 
However, similar behavior can be achieved using default arguments, variable-length arguments (*args, **kwargs), or type checking within a single method.

'''

#------------------------
# Using Default Arguments
class SpaceShip:
    
    def __init__(self):
        print("Spaceship Class Initiated")
    
    def launch(self, crew_size=1, fuel_type="liquid"): # Default Arguments is given
        if crew_size == 1:
            return f"Launching a single-seater spaceship with {fuel_type} fuel."
        else:
            return f"Launching a spaceship with {crew_size} crew members and {fuel_type} fuel."

ship = SpaceShip()
print(ship.launch())  # Output: Launching a single-seater spaceship with liquid fuel.
print(ship.launch(5, "solid"))  # Output: Launching a spaceship with 5 crew members and solid fuel.