class PaymentBase:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        pass

class CreditCardPayment(PaymentBase):
    def process_payment(self):
        print(f"Processing credit card payment of {self.amount}")

class PayPalPayment(PaymentBase):
    def process_payment(self):
        print(f"Processing PayPal payment of {self.amount}")


if __name__ == "__main__":
    payments = [
        CreditCardPayment(100),
        PayPalPayment(200),
        CreditCardPayment(150)
    ]
    for payment in payments:
        payment.process_payment()

