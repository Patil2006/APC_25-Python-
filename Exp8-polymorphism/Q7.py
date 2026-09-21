"""
Problem Statement:
Create a base class BankAccount with a method calculate_interest().
Derive SavingsAccount, CurrentAccount, and FixedDepositAccount.
Override the method to calculate interest differently for each
account type.
"""

class BankAccount:
    def calculate_interest(self, balance):
        return 0


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 4 / 100


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 2 / 100


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 7 / 100


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

balance = 50000

for account in accounts:
    print("Interest:", account.calculate_interest(balance))