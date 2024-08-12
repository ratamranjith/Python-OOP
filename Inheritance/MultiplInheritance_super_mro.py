'''
Python: Multiple Inheritance using super and mro

Explanation:
The following code demonstrates the use of the super() function and the mro() method in Python to
handle multiple inheritance.
'''
class Apple:
    def __init__(self):
        self.color = "Red"
        self.taste = "Sweet"
    
    def message(self):
        print("An apple a day keeps the doctor away")
        
class Banana:
    def __init__(self):
        self.color = "Yellow"
        self.taste = "Sweet"
    
    def message(self):
        print("Bananas give us strength and power.")
        
class Fruit(Apple, Banana):
    def __init__(self):
        
        #---------------------------------------------------------
        # It will take the first inherited class by default - MRO
        super().__init__()
        print(self.color)
        super().message()
        
        #-----------------------------------------------------------------
        # It will Ignore the Apple class, and takes the Banana Class - MRO
        super(Apple, self).__init__()
        print(self.color)
        super(Apple, self).message()
        

fruit = Fruit()
fruit.message() # An apple a day keeps the doctor away
# MRO : Method Resolution Order
print(Fruit.__mro__) # (<class '__main__.Fruit'>, <class '__main__.Apple'>, <class '__main__.Banana'>, <class 'object'>)
print(Fruit.mro()) # (<class '__main__.Fruit'>, <class '__main__.Apple'>, <class '__main__.Banana'>, <class 'object'>)

#-------------------------
# Outside the class access
Banana.message(fruit) # Bananas give us strength and power.