"""
Python: Class and Objects

Description:
This script demonstrates the use of classes and objects in Python.
It defines a class called 'Television' with attributes and methods.
It then creates an object of the 'Television' class and uses its methods.
"""


class Television:

    def __init__(self):
        self.brand = None # Class instance
        self.dimensions = None
        self.warranty = None
        self.price = None

    def print_data(self): # Class Method
        # self.__dict__.keys --> builtin method __dict__ to access class variables. 
        # If already know this leave it, or Learn it
        for i in self.__dict__.keys(): 
            print(i , ':' ,self.__dict__[i])
        print('-'*15, end='\n')

tv = Television()
tv.brand = "onida"
tv.dimensions = "2040x1028"
tv.warranty = "1 Year"
tv.price = 30000

tv1 = Television()
tv1.brand = "MI"
tv1.dimensions = "2040x1028"
tv1.warranty = "1 Year"
tv1.price = 30000

tv.print_data()
tv1.print_data()