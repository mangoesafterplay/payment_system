from infrastructure.paypal_payment import PaypalPayment
from infrastructure.stripe_payment import StripePayment
from domain.order import Order

# Using Paypal
paypal_order = Order(100.0, PaypalPayment())
paypal_order.process_payment()

# Using Stripe
stripe_order = Order(250.0, StripePayment())
stripe_order.process_payment()

