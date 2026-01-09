from abc import ABC, abstractmethod

#The "Algorithm" Blueprint (Interface)
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight):
        """All strategies must implement this method"""
        pass


# The Concrete Strategies
class FedExStrategy(ShippingStrategy):
    def calculate_cost(self, weight):
        # FedEx: Flat $10 + $2 per kg
        return 10 + (weight * 2)

class PostalStrategy(ShippingStrategy):
    def calculate_cost(self, weight):
        # Postal: No flat fee, just $1.5 per kg
        return weight * 1.5

# The Context (The Order)
class Order:
    def __init__(self, weight, strategy: ShippingStrategy):
        self.weight = weight
        self.strategy = strategy  # This is the "brain" that can be swapped!

    def shipping_fee(self):
        # The Order doesn't know the math; it asks the Strategy
        return self.strategy.calculate_cost(self.weight)


# HOW TO USE IT
# Initial choice: FedEx
my_order = Order(weight=5, strategy=FedExStrategy())
print(f"FedEx Shipping: ${my_order.shipping_fee()}")


# Change strategy at runtime (User finds a cheaper option)
my_order.strategy = PostalStrategy()
print(f"Postal Shipping: ${my_order.shipping_fee()}")