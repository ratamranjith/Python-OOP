'''
Python: Getter and Setter (using property method without using decorators)

Explanation:
The following code demonstrates how to use getter and setter methods without using decorators.
'''
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    name = property(get_name, set_name)

# Example usage
person = Person("Martian", 30)
print(person.name)

'''
Note: Protected also follows the same rule
'''