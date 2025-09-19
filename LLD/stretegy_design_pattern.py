import abc

# 1. The Strategy Interface
# This defines the common method for all payment strategies.
class PaymentStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pay(self, amount):
        pass

# 2. Concrete Strategy Classes
# Each class implements a specific payment method.

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using PayPal.")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using Bitcoin.")

# 3. The Context Class
# This class uses the strategy. It doesn't know the specific
# implementation, only that it can call the 'pay' method on the
# strategy object it holds.
class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def checkout(self, amount):
        print("Starting checkout process...")
        self._payment_strategy.pay(amount)
        print("Checkout complete.")

# The Client Code
# This is where the magic happens! We can switch strategies at runtime.
if __name__ == "__main__":
    # Use Credit Card for the first purchase
    cart1 = ShoppingCart(CreditCardPayment())
    cart1.checkout(100)

    print("-" * 20)

    # Now, use PayPal for the next purchase
    cart2 = ShoppingCart(PayPalPayment())
    cart2.checkout(50)
    
    print("-" * 20)

    # Use a different strategy (Bitcoin)
    cart3 = ShoppingCart(BitcoinPayment())
    cart3.checkout(75)
