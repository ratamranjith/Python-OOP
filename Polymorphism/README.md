# Python: Polymorphism

## Overview

Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. The term "polymorphism" comes from the Greek words "poly," meaning many, and "morph," meaning form. Essentially, it means "many forms."

In Python, polymorphism enables methods to be used in different ways depending on the object that is invoking the method. This allows for a single interface to interact with different types of objects in varied ways.

## Types of Polymorphism in Python

### 1. Compile-Time Polymorphism or Static

Compile-time polymorphism is determined at the time of code compilation and is also known as static polymorphism. This type can be achieved through:

- **Method Overloading**: Defining multiple methods with the same name but different parameters within a class.
- **Operator Overloading**: Customizing the behavior of operators for user-defined classes.

### 2. Run-Time Polymorphism or Dynamic

Run-time polymorphism is determined at runtime and is also known as dynamic polymorphism. This type can be achieved through:

- **Method Overriding**: Redefining a method in a derived class that already exists in its base class.
- **Polymorphic Functions**: Functions that can accept arguments of different types and respond accordingly.
- **Duck Typing**: A concept where the type of an object is determined by its behavior (methods and properties) rather than its class or inheritance.
- **Abstract Base Classes (ABCs)**: Using abstract classes and methods to define common interfaces for a group of classes.

## Example: Duck Typing

Duck typing is a concept in Python where an object's suitability is determined by the presence of certain methods and properties, rather than the object's type. If an object has the required method or attribute, it can be used in place of another object, regardless of its class.

### Code Implementation

Here's an example demonstrating duck typing:

```python
class Alien:
    def communicate(self):
        return "Beep Beep"

class Human:
    def communicate(self):
        return "Hello!"

def initiate_communication(creature):
    return creature.communicate()

alien = Alien()
human = Human()

print(initiate_communication(alien))  # Output: Beep Beep
print(initiate_communication(human))  # Output: Hello!
```

#### Explanation:

- Classes Alien and Human: Both classes have a method named communicate(), which returns a different string.
- Function initiate_communication(): This function accepts any object and calls its communicate() method, demonstrating polymorphism.
- **Duck Typing:**
  Despite the objects alien and human being instances of different classes, the initiate_communication() function works with both because they share the same method name.
