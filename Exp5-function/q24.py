# 24. Create functions for deposit, withdrawal, balance enquiry, and transaction history.
# Prevent withdrawal when the balance is insufficient and maintain a transaction record.

balance = 0
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited: " + str(amount))
    print("Amount deposited successfully.")

def withdrawal(amount):
    global balance
    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn: " + str(amount))
        print("Amount withdrawn successfully.")
    else:
        print("Insufficient balance.")

def balance_enquiry():
    print("Current Balance =", balance)

def transaction_history():
    print("Transaction History:")
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(transaction)

deposit(5000)
withdrawal(1500)
balance_enquiry()
transaction_history()