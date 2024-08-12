'''
Python: Single Inheritance with Super Class

Explanation:
In this example, we have a super class called 'Fruits' and a sub class called 'Orange'
  - The 'Orange' class inherits all the properties and methods of the 'Fruits' class.
  - The 'Orange' class also has its own properties and methods that are specific to Oranges.
'''

class Fruits:
  
    def __init__(self, color , price):
      self.color = color
      self.price = price
      

class Orange(Fruits):
  
    def __init__(self, color, price, discount):
      super().__init__(color, price)
      self.discount = discount
    
    def print(self):
      print(f"Color : {self.color} , Price : {self.price}, discount : {(self.price * self.discount)/100}")
      
orange = Orange("Orange", 50, 5)
orange.print()