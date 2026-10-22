# Import functions from banking package.

from banking.account import create_account, check_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_loan

name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

account = create_account(name, account_number, balance)

print("\nAccount Details")
print("Name:", account["name"])
print("Account Number:", account["account_number"])
print("Balance:", check_balance(account))

deposit_amount = float(input("\nEnter deposit amount: "))
deposit(account, deposit_amount)
print("Balance after deposit:", check_balance(account))

withdraw_amount = float(input("Enter withdrawal amount: "))
withdraw(account, withdraw_amount)
print("Balance after withdrawal:", check_balance(account))

principal = float(input("\nEnter loan amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter loan period: "))

interest, total = calculate_loan(principal, rate, time)

print("\nLoan Details")
print("Interest:", interest)
print("Total Loan Amount:", total)