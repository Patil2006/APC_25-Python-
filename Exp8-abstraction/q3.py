# Q3. Create an abstract class BankAccount with abstract methods deposit() and withdraw(). Derive SavingsAccount and CurrentAccount and implement the required operations.

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Savings Account Deposit:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings Account Withdrawal:", amount)
        else:
            print("Insufficient Balance")

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Current Account Deposit:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Current Account Withdrawal:", amount)

savings = SavingsAccount(101, 10000)
current = CurrentAccount(102, 20000)

savings.deposit(5000)
savings.withdraw(3000)
print("Savings Account Balance:", savings.balance)

current.deposit(5000)
current.withdraw(3000)
print("Current Account Balance:", current.balance)