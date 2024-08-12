# Python: Inheritance

**Definition:**

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class to inherit properties and behaviors (methods) from an existing class. The existing class is called the **superclass** (or base class), and the new class is called the **subclass** (or derived class). Inheritance promotes code reusability and establishes a relationship between classes.

**Definition (Simple Way):**

Inheritance is like when you get something from your parents.
In programming, it means a new class (child) can get features (like variables and functions) from an existing class (parent).
This helps us reuse the code and organize it better.

##### Inheritance Types:

1. [Single-level Inheritance or Single Inheritance](#single-inheritance)
   1. [Single Inheritance with Super Class](#11-python-single-inheritance-with-super-class)
2. Multiple Inheritance.
   1. Multiple Inheritance with Super Class
   2. Multiple Inheritance using Super and MRO
3. Multi-level Inheritance.
   1. Multi-level Inheritance with Super Class
4. Hierarchical Inheritance.
   1. Hierarchical Inheritance with Super Class
5. Hybrid Inheritance.
   1. Hybrid Inheritance with Super Class

## Single Inheritance:

```python
# Single-level Inheritance or Single Inheritance
class Parent:
    def call_parent(self):
        print("Parent Inherited Successfully")

class Child(Parent):
    def __init__(self):
        pass

    def display(self):
        print("Child Method is called")

child = Child()
child.display()
child.call_parent()

```

#### [1.1 Python: Single Inheritance with Super Class](#Single Inheritance with Super Class):

##### Explanation

In this example, we demonstrate the concept of single inheritance in Python, where a subclass inherits properties and methods from a superclass.

- **Super Class**: The `Fruits` class serves as the superclass, with properties like `color` and `price`.
- **Sub Class**: The `Orange` class is a subclass that inherits from the `Fruits` class. It adds its own property, `discount`, and a method, `print()`, which prints the details of the orange, including the calculated discount.

###### Code

```python
class Fruits:

    def __init__(self, color , price):
      self.color = color
      self.price = price


class Orange(Fruits):

    def __init__(self, color, price, discount):
      super().__init__(color, price)
      self.discount = discount

    def print(self):
      print(f"Color : {self.color} , Price : {self.price}, discount : {(self.price * self.discount)/100}")

orange = Orange("Orange", 50, 5)
orange.print()
```

###### Code Explanation

##### Fruits Class (Super Class):

- The Fruits class is the superclass with an **init** method that initializes two properties: color and price.
  Orange Class (Sub Class):
- The Orange class inherits from the Fruits class.
  In its **init** method, super().**init**(color, price) is used to call the constructor of the Fruits class, ensuring that the color and price properties are initialized in the Orange class.
  The Orange class introduces an additional property, discount, and a method, print(), which prints the color, price, and the calculated discount.
- **Object Creation and Method Call:**

  - An instance of the Orange class is created with the color "Orange", price 50, and a discount of 5%.

    The print() method is called to display the details of the orange, including the calculated discount.

Output:

```
Color : Orange , Price : 50, discount : 2.5
```

#### Explanation:

The Color of the orange as "Orange".
The Price of the orange as 50.
The discount amount is calculated as 5% of 50, which equals 2.5.

<hr/>

## 2. Multiple Inheritance:

#### This is like a child inheriting features from two parents. The child class gets features from more than one parent class.

```python
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
print(duck.fly())   # Inherited from Flyable
print(duck.swim())  # Inherited from Swimmable
```

#### Explanation:

The Duck class inherits features from both Flyable and Swimmable classes, so a duck can both fly and swim.

# 2.1 Multiple Inheritance with Super Class

## Description

This repository demonstrates how to implement multiple inheritance in Python using a simple example. The code defines a base class, `Vehicle`, and two subclasses, `Car` and `Motorcycle`. The `Car` and `Motorcycle` classes inherit from the `Vehicle` class, showcasing how each subclass can override methods while still accessing the base class's functionality.

## Code Explanation

### Classes

- **Vehicle**: The base class with attributes `brand`, `model`, and `year`, and a method `start_engine()` that prints a basic message about starting the engine.
- **Car**: Inherits from `Vehicle` and adds an attribute `doors`. It overrides the `start_engine()` method to include additional functionality specific to a car, while still calling the base class's method using `super()`.
- **Motorcycle**: Inherits from `Vehicle` and adds an attribute `engine_size`. It also overrides the `start_engine()` method, incorporating its own behavior along with the base class's method.

### Usage

The code creates instances of `Car` and `Motorcycle` and calls their `start_engine()` methods to demonstrate how the method overriding works.

### Example Code

```python
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("The engine is starting...")
        print("The vehicle is ready to move.")

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def start_engine(self):
        print("The car's engine is starting...")
        print("The car is ready to move.")
        super().start_engine()
        print("The car's engine is running...")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size

    def start_engine(self):
        print("The motorcycle's engine is starting...")
        print("The motorcycle is ready to move.")
        super().start_engine()
        print("The motorcycle's engine is running...")

# Multiple inheritance: A hybrid vehicle that can be both a car and a motorcycle
class HybridVehicle(Car, Motorcycle):
    def __init__(self, brand, model, year, doors, engine_size):
        Car.__init__(self, brand, model, year, doors)
        Motorcycle.__init__(self, brand, model, year, engine_size)

    def start_engine(self):
        print("The hybrid vehicle's engine is starting...")
        super().start_engine()
        print("The hybrid vehicle is running...")

# Example usage
hybrid = HybridVehicle("Tesla", "Model X", 2023, 4, "Electric")
hybrid.start_engine()
```

### Explanation:

The HybridVehicle class inherits from both Car and Motorcycle, making it an example of multiple inheritance. This class has access to properties and methods from both parent classes.

#### Constructor Calls:

In the HybridVehicle constructor, we call the constructors of both Car and Motorcycle to initialize the attributes defined in each.

#### Method Overriding:

The start_engine method in HybridVehicle overrides the method from both parent classes, and uses super().start_engine() to call the start_engine method from the first class in the inheritance order (which is Car).

## 2.2 Multiple Inheritance using `super` and `mro`

### Description

This repository demonstrates how to use the `super()` function and the `mro()` method in Python to handle multiple inheritance. The code example provides insights into how Python resolves method calls and initializes classes in a multiple inheritance scenario.

### Code Explanation

#### Classes

- **Apple**: A class representing an apple with attributes `color` and `taste`, and a method `message()` that prints a health-related message.
- **Banana**: A class representing a banana with attributes `color` and `taste`, and a method `message()` that prints an energy-related message.
- **Fruit**: A subclass that inherits from both `Apple` and `Banana`. This class is used to demonstrate the method resolution order (MRO) and how `super()` works in multiple inheritance.

#### Key Features

1. **Method Resolution Order (MRO)**: The `Fruit` class demonstrates how Python determines the order in which base classes are initialized and methods are resolved. The MRO can be viewed using `Fruit.__mro__` or `Fruit.mro()`.

2. **Using `super()`**: The `Fruit` class uses `super()` in two different contexts:

   - By default, `super()` refers to the first parent class in the MRO, which is `Apple` in this case.
   - `super(Apple, self)` bypasses the `Apple` class and refers to the next class in the MRO, which is `Banana`.

3. **Outside Class Access**: The code also shows how to access a method from a specific parent class outside of the `Fruit` class using `Banana.message(fruit)`.

#### Usage

The code creates an instance of `Fruit` and demonstrates the use of `super()` and `mro()` in multiple inheritance. It also prints the MRO of the `Fruit` class and accesses the `message()` method from both `Apple` and `Banana`.

#### Example Code

```python
class Apple:
    def __init__(self):
        self.color = "Red"
        self.taste = "Sweet"

    def message(self):
        print("An apple a day keeps the doctor away")

class Banana:
    def __init__(self):
        self.color = "Yellow"
        self.taste = "Sweet"

    def message(self):
        print("Bananas give us strength and power.")

class Fruit(Apple, Banana):
    def __init__(self):

        # It will take the first inherited class by default - MRO
        super().__init__()
        print(self.color)
        super().message()

        # It will Ignore the Apple class, and takes the Banana Class - MRO
        super(Apple, self).__init__()
        print(self.color)
        super(Apple, self).message()


fruit = Fruit()
fruit.message()  # An apple a day keeps the doctor away

# MRO : Method Resolution Order
print(Fruit.__mro__)  # (<class '__main__.Fruit'>, <class '__main__.Apple'>, <class '__main__.Banana'>, <class 'object'>)
print(Fruit.mro())  # (<class '__main__.Fruit'>, <class '__main__.Apple'>, <class '__main__.Banana'>, <class 'object'>)

# Outside the class access
Banana.message(fruit)  # Bananas give us strength and power.

```

### Explanation:

    The Fruit class inherits from both Apple and Banana, demonstrating how Python manages multiple inheritance.

    **Method Resolution Order (MRO):**
        Python determines the order in which base classes are called when methods are invoked using the MRO.
    **super() Function:**
        The super() function is used to call the next method in the MRO, allowing the Fruit class to interact with its parent classes in a flexible manner.
