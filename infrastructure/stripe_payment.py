from domain.payment_method import PaymentMethod

class StripePayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Processing Stripe payment of ${amount}")
