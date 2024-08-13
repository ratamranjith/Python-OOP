'''
Python: Setters and Getters (using Validation in setter)

Explanation:
The following code snippet demonstrates how to use setters and getters in Python. The setter is used to validate
the input data before assigning it to the instance variable. The getter is used to retrieve the value of
the instance variable.

(i.e) Applying the condition to validate the value
'''
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0: # Validation check
            raise ValueError("Price cannot be negative")
        self._price = value

# Example usage
product = Product("Laptop", 1000)
product.price = 900  # Valid
# product.price = -200  # Raises ValueError: Price cannot be negative
# Same can be applied for person's age, since age is a positive value