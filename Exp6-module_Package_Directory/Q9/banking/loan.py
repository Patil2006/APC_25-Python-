# Loan calculation function.

def calculate_loan(principal, rate, time):
    interest = (principal * rate * time) / 100
    total_amount = principal + interest

    return interest, total_amount