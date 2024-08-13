'''
Python: Getter and Setter (using Decorators)

Explanation:
The following code demonstrates how to use getter and setter methods in Python. It uses the built-in property
function to create a property with a getter and a setter.
'''

#-------------------------------------
# implementing using Private Variables
class Person:
    def __init__(self, name):
        self.__name = name
    
    # Getter for name
    @property
    def name(self):
        return self.__name
    
    # Setter for name
    @name.setter
    def name(self, name):
        self.__name = name

#---------------------------------------
# implementing using Protected Variables
class Person1:
    def __init__(self, age):
        self._age = age
    
    # Getter for age
    @property
    def age(self):
        return self._age
    
    # Setter for age
    @age.setter
    def age(self, age):
        self._age = age


person = Person("Martian")
print(person.name)  # Output: John

person1 = Person1(20)
print(person1.age)

'''
Note: If {Decorators}.setter is not present, then the variable is in readonly mode and it cannot be accessed
'''