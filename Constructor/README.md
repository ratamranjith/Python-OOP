# Python: Constructor

## Description

This script demonstrates the use of constructors in Python classes. A constructor is a special method that is automatically called when an object of a class is created. The script includes examples of different types of constructors, including simple constructors, constructors with variables, constructors with arguments, and an illustration of how Python handles constructor overloading.

## Code Explanation

The script demonstrates the following concepts:

1. **Simple Constructor**:

   - A basic constructor is defined using the `__init__()` method in the `Satellite` class. When an instance of the class is created, the constructor automatically prints a message indicating that the satellite testing has started.

   ```python
   class Satellite:
       def __init__(self):  # Constructor
           print("Satellite Testing Started")

   satellite = Satellite()  # Constructor will always get executed.
   ```

2. **Constructor with Variables**:

   - The `Rocket` class includes a constructor that initializes the `name` attribute with a default value and the `speed` attribute with `None`. After creating an instance of the class, the `speed` attribute is set, and both `name` and `speed` are printed.

   ```python
   class Rocket:
       def __init__(self):
           self.name = "Douglas"
           self.speed = None

   rocket = Rocket()
   rocket.speed = "7.9 km/sec"
   print(rocket.name)  # Output: Douglas
   print(rocket.speed)  # Output: 7.9 km/sec
   ```

3. **Constructor with Arguments or Parameterized Constructor**:  

   - The `Car` class demonstrates a constructor that takes arguments to initialize its attributes. The `__init__()` method accepts `color`, `model`, and `year` as parameters, which are used to set the corresponding attributes during object creation.

   ```python
   class Car:
       def __init__(self, color, model, year):
           self.color = color
           self.model = model
           self.year = year

   car = Car("Black", "BMW", "1985")
   print(car.color)  # Output: Black
   print(car.model)  # Output: BMW
   print(car.year)  # Output: 1985
   ```

4. **Constructor Overloading**:

   - Python does not support constructor overloading, meaning you cannot have multiple constructors with different parameters in the same class. The `Bike` class example shows that when multiple constructors are defined, only the last one is used, and the previous one is ignored.

   ```python
   class Bike:
       def __init__(self, color, model, year):  # 1st Constructor
           self.color = color
           self.model = model
           self.year = year

       def __init__(self, color):  # 2nd Constructor
           self.color = color

   bike = Bike("green")  # The 1st constructor is neglected, and the latest constructor is used.
   print(bike.color)  # Output: green
   ```

   - In this example, the first constructor in the `Bike` class is ignored, and only the second one is executed, illustrating that Python does not allow multiple constructors within the same class.

## Conclusion

This script highlights how constructors are used in Python, providing examples of simple constructors, constructors with variables and arguments, and demonstrating that Python does not support constructor overloading.
