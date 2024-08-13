'''
Python: Abstraction

Explanation:
The following code demonstrates the concept of abstraction in Python. 
Abstraction is a fundamental concept in object-oriented programming that allows us to show only the necessary information to the outside world while hiding the internal details.

Example:
    If we are preparing for the exam, one of our friend gone through the entire concepts. 
    when we ask him to teach us, he is not going to teach us all the concepts, he will teach us only the necessary
    concepts that we need to know for the exam. 
    Based on his key concepts, we will write our own story in the exam to score marks
    This is an example of abstraction.
'''

from abc import ABC, abstractmethod

class Vehicle(ABC): # Invoking ABC class, means we cannot create an object of Abstract Class
    
    @abstractmethod
    def start_engine(self): # Like template, mandatory if the class is inherited / invoked
        pass


class Car(Vehicle):
    
    def start_engine(self):
        print("Car engine started")


car = Car()
car.start_engine()