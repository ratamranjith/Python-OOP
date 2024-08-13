'''
Python: Polymorphism

Explanation:
    Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. 
    The word "polymorphism" comes from the Greek words "poly," meaning many, and "morph," meaning form. Essentially, it means "many forms." 
    In Python, this concept allows methods to be used in different ways depending on the object that is invoking the method.

Example:
    Imagine you have a remote control that can work with different devices—TVs, air conditioners, and sound systems. 
    The remote control is a single interface that interacts with multiple devices, but the way it controls each device differs. 
    Similarly, in Python, polymorphism allows a single interface (like a method) to interact with different objects in unique ways.

Types of Polymorphism in Python:
    1. Compile-Time Polymorphism or Static
        Compile-time polymorphism is determined at the time of code compilation. 
        It is also known as static polymorphism.
        This is typically achieved through,
            - Method Overloading
            - Operator Overloading.

    2. Run-Time Polymorphism or Dynamic
        Run-time polymorphism is determined at runtime. 
        It is also known as dynamic polymorphism.
        This is typically achieved through,
            - Method Overriding
            - Polymorphic Functions
            - Duck Typing
            - Abstract Base Classes (ABCs)


# 1. Duck Typing:
    Duck typing is a concept in Python where an object is determined by its behavior (methods and properties) rather than its class or inheritance. If an object has the required method or attribute, it can be used in place of another object.

'''
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
