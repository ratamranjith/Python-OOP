# Python: Inheritance

**Definition:**

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class to inherit properties and behaviors (methods) from an existing class. The existing class is called the **superclass** (or base class), and the new class is called the **subclass** (or derived class). Inheritance promotes code reusability and establishes a relationship between classes.

**Definition (Simple Way):**

Inheritance is like when you get something from your parents. 

In programming, it means a new class (child) can get features (like variables and functions) from an existing class (parent). 

This helps us reuse the code and organize it better.


##### Inheritance Types:

1. Single-level Inheritance or Single Inheritance.
   1. Single Inheritance with Super Class
2. Multi-level Inheritance.
   1. Multi-level Inheritance with Super Class
3. Multiple Inheritance.
   1. Multiple Inheritance with Super Class
4. Hierarchial Inheritance.
   1. Hierarchial Inheritance with Super Class
5. Hybrid Inheritance.
   1. Hybrid Nheritance with Super Class

## Single Inheritance:

```
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


#### 1.1 Python: Single Inheritance with Super Class

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

### Fruits Class (Super Class):

* The Fruits class is the superclass with an **init** method that initializes two properties: color and price.
  Orange Class (Sub Class):
* The Orange class inherits from the Fruits class.
  In its **init** method, super().**init**(color, price) is used to call the constructor of the Fruits class, ensuring that the color and price properties are initialized in the Orange class.
  The Orange class introduces an additional property, discount, and a method, print(), which prints the color, price, and the calculated discount.
* **Object Creation and Method Call:**
  * An instance of the Orange class is created with the color "Orange", price 50, and a discount of 5%.

    The print() method is called to display the details of the orange, including the calculated discount.

Output:

```
Color : Orange , Price : 50, discount : 2.5
```

### Explanation:

The Color of the orange as "Orange".
The Price of the orange as 50.
The discount amount is calculated as 5% of 50, which equals 2.5.
