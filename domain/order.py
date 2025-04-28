from .payment_method import PaymentMethod

class Order:
    def __init__(self, amount: float, payment_method: PaymentMethod):
        self.amount = amount
        self.payment_method = payment_method

    def process_payment(self) -> None:
        self.payment_method.pay(self.amount)
