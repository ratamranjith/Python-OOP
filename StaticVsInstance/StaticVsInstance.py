'''
Static Variables and Methods
Class Variables and Methods

Description:
    In this problem, we will explore the concept of static variables and methods in Python. Static variables and
methods are shared by all instances of a class and are not specific to any instance.
'''

class Alien:
    
    # Static variable
    alien_count = 5
    
    def __init__(self): # if we don't required any parameters, we can simply give pass
        pass
    
    @staticmethod
    def get_alien_count():
        print("Alien Count", Alien.alien_count)
    
    @classmethod
    def aliens_activity_check(cls):
        print(f"Total Aliens: {cls.alien_count}")
        print(Alien.get_alien_count())
    
alien = Alien()
alien.get_alien_count()
alien.aliens_activity_check()