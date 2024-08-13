'''
Python: Setters and Getters (using lazy access)

Explanation:
    The following code snippet demonstrates how to implement setters and getters in Python using lazy access. Lazy access means
    that the value is only computed when it is actually needed.
    (i.e) value will be a static, it will be computed with user input. without setter

'''

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

# Example usage
circle = Circle(5)
print(circle.area)  # Output: 78.53975
