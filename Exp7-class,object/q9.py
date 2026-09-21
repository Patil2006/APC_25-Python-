# Q9. Design an ATM class that allows a user to check balance, deposit money, withdraw money, and display account details. Create an object of the class and implement the operations through a menu-driven program.

class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("Updated Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def display_account(self):
        print("Account Number:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)

atm = ATM(1001, "Rahul", 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        atm.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        atm.withdraw(amount)
    elif choice == 4:
        atm.display_account()
    elif choice == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")