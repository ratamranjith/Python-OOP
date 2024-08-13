# Python: Setters and Getters

## Overview

This repository demonstrates various ways to implement setters and getters in Python. Setters and getters are methods used to control access to the attributes of a class, providing a way to manage the state of an object. This includes:

- **Traditional Methods**: Using explicit getter and setter methods.
- **Using Decorators**: Utilizing Python's `@property` decorator to define getters and setters.
- **Using `property()`**: Implementing getters and setters without decorators using the `property()` function.

## Implementations

### 1. Traditional Methods

In this implementation, setters and getters are defined explicitly using traditional methods. The primary purpose of the setter is to modify or set the value of a private variable.

```python
import random, time

class Space:

    def __init__(self):
        self.__galaxies = None

    def set_value(self, multiplier):
        self.__galaxies = round(time.time()*1000) * multiplier

    def get_value(self):
        return self.__galaxies

space = Space()
space.set_value(2)
print(space.get_value())
```

### 2. Using Decorators

This approach demonstrates the use of Python's @property decorator to create properties with associated getter and setter methods. The example shows the implementation using both private and protected variables.

#### Using Private Variables

```python
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
```

#### Using Protected Variables

```python
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
```

**Note:**
If the {Decorators}.setter is not present, then the variable is in read-only mode and cannot be modified.

### 3. Using property() Method Without Decorators

    In this implementation, we create getter and setter methods without using decorators by utilizing the property() function. This method provides a more explicit approach to defining property methods.

```python
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
```
