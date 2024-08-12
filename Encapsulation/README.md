# Python: Encapsulation

1. Using Private Variables (\_\_variableName)
2. Using Protected Variables (\_variableName)
3. Using Private Method (\_\_methodName)

## 1. Private Variables

### Description

This repository demonstrates the concept of encapsulation in Python, a fundamental principle of object-oriented programming (OOP). Encapsulation binds together the data and the methods that manipulate that data, keeping both safe from outside interference and misuse. It hides the internal state of an object from the outside world and only exposes the necessary information through public methods.

#### Code Explanation

#### Class

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

```
Deposited 500. New balance is 1500.
Withdrew 200. New balance is 1300.
Account Holder: John Doe
Balance: 1300
```

## 2. Protected Variables

### Description:

This repository demonstrates the concept of encapsulation in Python using protected variables. Encapsulation is a fundamental principle of object-oriented programming (OOP) that binds data and the methods that manipulate that data together, keeping both safe from outside interference and misuse. This example also shows how inheritance can be used to extend functionality.

#### Code Explanation

#### Classes

- **BankAccount**: Represents a simple bank account with protected attributes `_account_holder` and `_balance`. It provides public methods to deposit and withdraw money, and to display account information.
- **SavingsAccount**: Inherits from `BankAccount` and adds functionality specific to savings accounts, such as applying interest. It uses a protected attribute `_interest_rate` for managing the interest rate.

### Key Features

1. **Protected Attributes**:

   - `_account_holder` and `_balance` in `BankAccount` are protected attributes. They are intended to be accessible within the class and its subclasses but are not meant to be accessed directly from outside.
   - `_interest_rate` in `SavingsAccount` is also a protected attribute, used for interest calculations.

2. **Public Methods**:
   - `deposit(amount)`: Adds funds to the account and updates the balance.
   - `withdraw(amount)`: Withdraws funds from the account while checking for validity.
   - `display_account_info()`: Displays the account holder's name and balance.
   - `apply_interest()`: In `SavingsAccount`, this method calculates and applies interest to the account balance.

### Example Usage

The code creates an instance of `SavingsAccount` and demonstrates how to use the public methods to interact with the protected attributes, including depositing, withdrawing, applying interest, and displaying account information.

### Example Code

```python
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
```

# Output

```
Deposited 500. New balance is 1500.
Withdrew 200. New balance is 1300.
Applied interest. New balance is 1365.
Account Holder: Jane Doe
Balance: 1365
```

# 3. Using Private Method

## Description

This repository demonstrates encapsulation in Python using a private method. Encapsulation is a fundamental concept in object-oriented programming (OOP) that binds together the data and methods that manipulate that data within a single unit, protecting the internal state of the object from external interference.

## Code Explanation

### Class

- **BankAccount**: This class represents a bank account with private attributes for the account holder's name and balance. It also includes public methods to deposit and withdraw money, display account information, and a private method to log transactions.

### Key Features

1. **Private Attributes**:

   - `__account_holder` and `__balance` are private attributes, accessible only within the class, ensuring that the internal state of the object is secure from unauthorized access.

2. **Public Methods**:

   - `deposit(amount)`: Allows for adding funds to the account while logging the transaction.
   - `withdraw(amount)`: Allows for withdrawing funds from the account with checks to ensure the withdrawal amount is valid, and logs the transaction.
   - `display_account_info()`: Displays the account holder's name and the current balance.

3. **Private Method**:
   - `__log_transaction(transaction_type, amount)`: A private method used to log deposit and withdrawal transactions. This method is not accessible from outside the class, highlighting the encapsulation principle.

### Example Usage

The code creates an instance of `BankAccount` and demonstrates how to use the public methods to interact with the encapsulated data and how the private method is used internally for logging transactions.

### Example Code

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__log_transaction("withdraw", amount)
        else:
            print("Invalid withdrawal amount.")

    def display_account_info(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: {self.__balance}")

    def __log_transaction(self, transaction_type, amount):
        # Private method for logging transactions
        print(f"Logged {transaction_type} of {amount} for {self.__account_holder}.")

# Example usage:
account = BankAccount("John Doe", 1000)
account.deposit(500)  # Deposited 500. New balance is 1500. Logs the transaction.
account.withdraw(200)  # Withdrew 200. New balance is 1300. Logs the transaction.
account.display_account_info()

# Note:
#   If we try to access the private method directly, it will result in an AttributeError:
#   eg: account.__log_transaction("deposit", 500)  # This will raise an AttributeError.
```
