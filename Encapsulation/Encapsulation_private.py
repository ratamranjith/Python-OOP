'''
Python: Encapsulation (using private variables)

Explanation:
Encapsulation is a fundamental concept in object-oriented programming (OOP) that binds together the data and
the methods that manipulate that data, and keeps both safe from outside interference and misuse.
It is a mechanism of hiding the internal state of an object from the outside world and only exposing the
necessary information through public methods.
'''

class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid withdrawal amount.")

    def display_account_info(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: {self.__balance}")

# Example usage:
account = BankAccount("John Doe", 1000)
account.deposit(500)  # Deposited 500. New balance is 1500.
account.withdraw(200)  # Withdrew 200. New balance is 1300.
account.display_account_info()
