'''
Python: Encapsulation (Using Private method)

Explanation:
The following code demonstrates encapsulation in Python using a private method. Encapsulation is a fundamental concept in
object-oriented programming (OOP) that binds data and methods that manipulate that data within a single unit

'''

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
#   If we try to access the private method directly will result in an AttributeError:
#   eg: account.__log_transaction("deposit", 500)  # This will raise an AttributeError.

'''
Explanation:
Private Methods: 
    The __log_transaction method is a private method, which means it cannot be accessed or called directly from outside the class. It is only meant to be used internally by other methods within the class.
Encapsulation: By using private methods, the class hides certain internal functionalities that should not be exposed or modified by the outside world. This helps in maintaining the integrity of the class’s internal processes.
Key Points:
No Direct Access: 
    Direct access to the private method, such as account.__log_transaction(), will result in an AttributeError. This ensures that the method is only used where and when the class designer intended.
Internal Use: The private method __log_transaction is used internally within the deposit and withdraw methods to log transactions, ensuring that this logging process is encapsulated and protected from external interference.
'''