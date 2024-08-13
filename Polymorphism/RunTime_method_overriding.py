'''
Python: Run-time (Method Overriding)

Explanation:
    - Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. 
    This allows the subclass to define its own behavior while still adhering to the interface provided by the parent class.
'''
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

human = Human()
human.fly()
human.walk()  # Method overriden
