# Python: Encapsulation (using Private Variables)

## Description

This repository demonstrates the concept of encapsulation in Python, a fundamental principle of object-oriented programming (OOP). Encapsulation binds together the data and the methods that manipulate that data, keeping both safe from outside interference and misuse. It hides the internal state of an object from the outside world and only exposes the necessary information through public methods.

## Code Explanation

### Class

- **BankAccount**: This class represents a simple bank account with private attributes for the account holder's name and balance. The class provides public methods to deposit and withdraw money, as well as to display account information.

### Key Features

1. **Private Attributes**:
   - `__account_holder` and `__balance` are private attributes. They cannot be accessed directly from outside the class, ensuring that the internal state of the object is protected.
2. **Public Methods**:
   - `deposit(amount)`: Allows for adding funds to the account while validating the deposit amount.
   - `withdraw(amount)`: Allows for withdrawing funds from the account with checks to ensure the withdrawal amount is valid.
   - `display_account_info()`: Displays the account holder's name and the current balance.

### Example Usage

The code creates an instance of `BankAccount` and demonstrates how to use the public methods to interact with the encapsulated data.

### Example Code

```python
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
```

### Output

Deposited 500. New balance is 1500.
Withdrew 200. New balance is 1300.
Account Holder: John Doe
Balance: 1300
