'''
Python: Setters and Getters (Using Traditional Methods)

Explanation:
    We are going to implement setters and getters without built-in property.
    Main Purpose of the setter is to modify/set the private variable value
'''
import random, time

class Space:
    
    def __init__(self):
        self.__galaxies = None
    
    def set_value(self, multiplier):
        self.__galaxies = round(time.time()*1000) * multiplier
    
    def get_value(self):
        return self.__galaxies
    
space = Space()
space.set_value(2)
print(space.get_value())