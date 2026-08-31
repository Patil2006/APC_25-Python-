# Deposit and withdrawal functions.

def deposit(account, amount):
    account["balance"] += amount
    return account["balance"]


def withdraw(account, amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        return account["balance"]
    else:
        print("Insufficient balance")
        return account["balance"]