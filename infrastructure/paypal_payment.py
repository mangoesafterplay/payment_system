from domain.payment_method import PaymentMethod

class PaypalPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount}")
