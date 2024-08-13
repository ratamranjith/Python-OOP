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

- **Duck Typing**: A concept where the type of an object is determined by its behavior (methods and properties) rather than its class or inheritance.
- **Method Overriding**: Redefining a method in a derived class that already exists in its base class.
- **Polymorphic Functions**: Functions that can accept arguments of different types and respond accordingly.
- **Abstract Base Classes (ABCs)**: Using abstract classes and methods to define common interfaces for a group of classes.

### 1.1 Compile-Time Polymorphism (Method Overloading)

### Overview

**Method Overloading** is a form of compile-time polymorphism where multiple methods share the same name but differ in the number or type of parameters. Languages like Java and C++ support method overloading inherently, allowing developers to define multiple methods with the same name but different signatures within the same class.

However, **Python does not support traditional method overloading**. Instead, similar behavior can be achieved using:

- **Default Argument Values**: Providing default values for parameters allows a single method to handle multiple scenarios.
- **Variable-Length Arguments (`*args`, `**kwargs`)\*\*: Accepting arbitrary numbers of positional and keyword arguments.
- **Type Checking Within Methods**: Implementing logic inside a method to handle different types or numbers of arguments.

## Example: Using Default Arguments

In this example, we demonstrate how to mimic method overloading behavior using default arguments in Python.

### Code Implementation

```python
class SpaceShip:

    def __init__(self):
        print("Spaceship Class Initiated")

    def launch(self, crew_size=1, fuel_type="liquid"):
        """
        Launches the spaceship.

        Parameters:
        - crew_size (int): Number of crew members. Defaults to 1.
        - fuel_type (str): Type of fuel used. Defaults to "liquid".

        Returns:
        - str: Description of the launch.
        """
        if crew_size == 1:
            return f"Launching a single-seater spaceship with {fuel_type} fuel."
        else:
            return f"Launching a spaceship with {crew_size} crew members and {fuel_type} fuel."

# Example Usage
ship = SpaceShip()
print(ship.launch())  # Uses default arguments
print(ship.launch(5, "solid"))  # Overrides default arguments
```

### 2.1 - Duck Typing

Duck typing is a concept in Python where an object's suitability is determined by the presence of certain methods and properties, rather than the object's type. If an object has the required method or attribute, it can be used in place of another object, regardless of its class.

#### Code Implementation

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

### 2.2 Run-Time Polymorphism (Method Overriding)

#### Overview

Method overriding is a key feature of run-time polymorphism in object-oriented programming (OOP). It occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. This allows the subclass to define its own behavior while still adhering to the interface provided by the parent class.

### Example: Method Overriding

In this example, we demonstrate method overriding using a simple scenario involving two classes: `Alien` and `Human`. The `Human` class inherits from the `Alien` class and overrides one of its methods.

#### Code Implementation

```python
class Alien:
    def __init__(self):
        pass

    def fly(self):
        print("Alien can fly in outer space")

    def walk(self):
        print("Aliens may walk quicker than Humans in outer space")

class Human(Alien): # Inherited Alien Class
    def __init__(self):
        pass

    def walk(self):
        print("Humans will walk slower than Aliens in outer space. Since there is no gravity")

# Example Usage
human = Human()
human.fly()
human.walk()  # Method overridden
```
