'''
Python: Setters and Getters (using Chained Property)

Explanation:
    Calling calling object methods in a chained manner by using "." operator
'''
class Car:
    def __init__(self):
        self._make = ""
        self._model = ""
    
    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, value):
        self._make = value
        return self  # Return self for chaining
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        self._model = value
        return self  # Return self for chaining

# Example usage
car = Car()
car.make = "Toyota"  # Normal usage
car.make = "Toyota"  # Normal usage
car.model = "Camry"  # Normal usage
car = Car().make = "Toyota"  # Normal usage
car = Car().model = "Camry"  # Normal usage
car = Car().make("Toyota").model("Camry")  # Chained usage
car = Car().model("Camry").make("Toyota")  # Chained usage
car = Car().make("Toyota").model("Camry")  # Chained usage
car = Car().model("Camry").make("Toyota")  # Chained usage
car = Car().make("Toyota").model("Camry")  # Chained usage