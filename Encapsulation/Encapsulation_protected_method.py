'''
Python: Encapsulation (Using Protected method)

Explanation:
The following code demonstrates encapsulation using a protected method in Python. Encapsulation is a fundamental concept in
object-oriented programming (OOP) that binds together the data and the methods that manipulate that data.
'''

class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._log_transaction("withdraw", amount)
        else:
            print("Invalid withdrawal amount.")

    def display_account_info(self):
        print(f"Account Holder: {self._account_holder}")
        print(f"Balance: {self._balance}")

    def _log_transaction(self, transaction_type, amount):
        # Protected method for logging transactions
        print(f"Logged {transaction_type} of {amount} for {self._account_holder}.")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self._interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self._interest_rate / 100
        self._balance += interest
        self._log_transaction("interest", interest)
        print(f"Applied interest. New balance is {self._balance}.")

# Example usage:
account = SavingsAccount("Jane Doe", 1000, 5)
account.deposit(500)  # Deposited 500. New balance is 1500.
account.withdraw(200)  # Withdrew 200. New balance is 1300.
account.apply_interest()  # Applied interest. New balance is 1365.
account.display_account_info()

# The protected method _log_transaction is accessible but should be used with caution:
account._log_transaction("manual log", 100)  # This will log the transaction but is not recommended for external use.

'''
Explanation:

Protected Methods: 
    The _log_transaction method is a protected method. While it can be accessed from outside the class, it is intended for internal use by the class and its subclasses.
Encapsulation: 
    By using protected methods, you signal that certain methods are meant to be used within the class or by derived classes, rather than being part of the public interface of the class.

Key Points:
Protected Access: 
    The protected method _log_transaction can be accessed directly from outside the class, but this goes against the intended design, as it is meant for internal use.
Subclass Interaction: 
The SavingsAccount subclass uses the protected method _log_transaction inherited from BankAccount to log interest transactions. This shows how protected methods can be extended and used within subclasses.
'''