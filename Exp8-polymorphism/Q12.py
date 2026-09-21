"""
Problem Statement:
Develop an online shopping payment module using polymorphism.
Create a base class Payment and derived classes UPIPayment,
CardPayment, and WalletPayment. Each class should implement
its own make_payment() method. Demonstrate polymorphism
using a common function.
"""

class Payment:
    def make_payment(self):
        pass


class UPIPayment(Payment):
    def make_payment(self):
        print("Payment made using UPI")


class CardPayment(Payment):
    def make_payment(self):
        print("Payment made using Card")


class WalletPayment(Payment):
    def make_payment(self):
        print("Payment made using Wallet")


def process_payment(payment):
    payment.make_payment()


upi = UPIPayment()
card = CardPayment()
wallet = WalletPayment()

process_payment(upi)
process_payment(card)
process_payment(wallet)