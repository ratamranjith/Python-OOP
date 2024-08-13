'''
Python: Setters and Getters (using Cache Property)

Explanation:
    Storing the value in a variable and retrieving the value again without computations/calculations

'''

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__area = None  # Cache for area
    
    @property #Getter
    def area(self):
        if self.__area is None:  # Compute only once
            self.__area = 3.14159 * (self.__radius ** 2)
        return self.__area

# Example usage
circle = Circle(5)
print(circle.area)  # Computed and cached
print(circle.area)  # Retrieved from cache