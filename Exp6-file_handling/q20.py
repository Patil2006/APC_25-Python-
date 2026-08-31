# Q20. Calculate total deposits, withdrawals, final balance and largest transaction

file = open("transactions.txt", "w")

file.write("Deposit,5000\n")
file.write("Withdrawal,1000\n")
file.write("Deposit,3000\n")
file.write("Withdrawal,500\n")

file.close()

file = open("transactions.txt", "r")

total_deposits = 0
total_withdrawals = 0
transactions = []

for line in file:
    transaction, amount = line.strip().split(",")

    amount = float(amount)
    transactions.append(amount)

    if transaction.lower() == "deposit":
        total_deposits += amount
    elif transaction.lower() == "withdrawal":
        total_withdrawals += amount

file.close()

final_balance = total_deposits - total_withdrawals
largest_transaction = max(transactions)

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)