'''
Python: Setters and Getters - (using Traditional Private Method)

Explanation:
The following code snippet demonstrates how to use private methods as setters and getters in Python. The `__
` prefix is used to denote private methods.
'''
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    # Private getter
    def __get_name(self):
        return self._name
    
    # Private setter
    def __set_name(self, name):
        self._name = name
    
    # Public method to access the private getter
    def display_name(self):
        return self.__get_name()
    
    # Public method to set the private setter
    def change_name(self, name):
        self.__set_name(name)

# Example usage
person = Person("Martian", 30)
print(person.display_name())
