# Account creation and balance functions.

def create_account(name, account_number, balance):
    account = {
        "name": name,
        "account_number": account_number,
        "balance": balance
    }
    return account


def check_balance(account):
    return account["balance"]