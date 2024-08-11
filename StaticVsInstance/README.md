# Python: Static Variables and Methods

## Description

This script explores the concept of static variables and methods in Python. Static variables and methods are shared among all instances of a class and are not specific to any instance. This example demonstrates how to define and use static variables and methods in a class.

## Code Explanation

### Static Variable

The alien_count variable is defined as a class variable (static variable) in the Alien class. This variable is shared among all instances of the class and is not specific to any one instance.

```python
class Alien:

    # Static variable
    alien_count = 5

    def __init__(self):
        pass
```

### Static Method:

The get_alien_count() method is defined with the @staticmethod decorator. It operates directly on the class-level data and does not require access to instance-specific information. This method prints the current value of the alien_count variable.

```python
    @staticmethod
    def get_alien_count():
        print("Alien Count", Alien.alien_count)
```

### Class Method:

The aliens_activity_check() method is defined with the @classmethod decorator. It takes the class itself (cls) as the first parameter, allowing it to access class-level data. This method prints the total number of aliens and calls the static method get_alien_count().

Instance Creation and Method Calls: An instance of the Alien class is created, and the following methods are called:

alien.get_alien_count() prints the alien count using the static method.
alien.aliens_activity_check() prints the total number of aliens and calls get_alien_count() to display the count.

```python
    @classmethod
    def aliens_activity_check(cls):
        print(f"Total Aliens: {cls.alien_count}")
        print(Alien.get_alien_count())

alien = Alien()
alien.get_alien_count()
alien.aliens_activity_check()
```

## Output:

```
Alien Count 5
Total Aliens: 5
Alien Count 5
```

### Explanation:

    Alien Count 5 is printed by the get_alien_count() static method, showing the current count of aliens.
    Total Aliens: 5 is printed by the aliens_activity_check() class method, which also calls get_alien_count() to display the count.
    Alien Count 5 is again printed by the get_alien_count() method, which is called within aliens_activity_check().
