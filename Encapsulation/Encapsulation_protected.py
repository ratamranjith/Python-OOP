'''
Python: Encapsulation (using Protected variable)

Explanation:
The following code demonstrates encapsulation in Python. It defines a class called 'BankAccount' with a
protected variable 'balance'. The 'balance' variable is prefixed with a single underscore, which
indicates that it is intended to be accessed only within the class itself.
'''

class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder  # Protected attribute
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is {self._balance}.")
        else:
            print("Invalid withdrawal amount.")

    def display_account_info(self):
        print(f"Account Holder: {self._account_holder}")
        print(f"Balance: {self._balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self._interest_rate = interest_rate  # Protected attribute for subclass

    def apply_interest(self):
        interest = self._balance * self._interest_rate / 100
        self._balance += interest
        print(f"Applied interest. New balance is {self._balance}.")

# Example usage:
account = SavingsAccount("Jane Doe", 1000, 5)
account.deposit(500)  # Deposited 500. New balance is 1500.
account.withdraw(200)  # Withdrew 200. New balance is 1300.
account.apply_interest()  # Applied interest. New balance is 1365.
account.display_account_info()
