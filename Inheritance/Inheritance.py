'''
Python: Inheritance

Explanation:
    Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit
the properties and behavior of another class. The inheriting class is called the subclass or derived class,
and the class being inherited from is called the superclass or base class.

Types:
1. Single Inheritance: A subclass inherits from a single superclass. (parent -> child)
2. Multiple Inheritance: A subclass inherits from multiple superclasses. (grandparent, parent -> child)
3. Multilevel Inheritance: A subclass inherits from a superclass that itself inherits from another superclass (grandparent -> parent -> child)
4. Hierarchical Inheritance: A superclass has multiple subclasses. (grandparent -> parent, child (i.e) child and parent will inherit grandparent. (i.e) parent class has multiple child class)
5. Hybrid Inheritance: A combination of multiple inheritance and multilevel inheritance. (Combination of above 4)
'''

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

# Multi-level Inheritance
class Grandparent1:
    
    def call_grand(self):
        print("Grand Parent Inherited Successfully")

class Parent1(Grandparent1):
    def call_parent(self):
        print("Parent Inherited Successfully")

class Child1(Parent1):
    def __init__(self):
        pass

    def display(self):
        print("Child Method is called")

# Multi-level Inheritance
class Grandparent2:
    
    def call_grand(self):
        print("Grand Parent Inherited Successfully")

class Parent2:
    def call_parent(self):
        print("Parent Inherited Successfully")

class Child2(Grandparent2, Parent2):
    def __init__(self):
        pass

    def display(self):
        print("Child Method is called")

# Hierarchial Inheritance
class Grandparent3:
    
    def call_grand(self):
        print("Grand Parent Inherited Successfully")

class Parent3(Grandparent3):
    def call_parent(self):
        print("Parent Inherited Successfully")

class Child3(Grandparent3):
    def __init__(self):
        pass

    def display(self):
        print("Child Method is called")


# Hybrid Inheritance
class Grandparent4:
    
    def call_grand(self):
        print("Grand Parent Inherited Successfully")

class Relative(Grandparent4):
    def call_relative(self):
        print("Relative Inherited Successfully")

class Parent4(Grandparent4):
    def call_parent(self):
        print("Parent Inherited Successfully")

class Child4(Parent4, Relative):
    def __init__(self):
        pass

    def display(self):
        print("Child Method is called")





print("| Single Inheritance", ":"*10, end="\n")
child = Child()
child.display()
child.call_parent()
print(end="\n\n")
print("| Multi level Inheritance", ":"*10, end="\n")
child1 = Child1()
child1.display()
child1.call_parent()
child1.call_grand()
print(end="\n\n")
print("| Multiple Inheritance", ":"*10, end="\n")
child1 = Child2()
child1.display()
child1.call_parent()
child1.call_grand()
print(end="\n\n")
print("| Hierarchial Inheritance", ":"*10, end="\n")
child3 = Child3()
parent3 = Parent3()
child3.display()
child3.call_grand()
parent3.call_parent()
parent3.call_grand()
print(end="\n\n")
print("| Hybrid Inheritance", ":"*10, end="\n")
child4 = Child4()
child4.display()
child4.call_grand()
child4.call_parent()
child4.call_relative()