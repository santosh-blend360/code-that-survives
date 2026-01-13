from abc import ABC, abstractmethod

#when we have if and else in business logic..

# The "Algorithm" Blueprint (Interface)
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight, distance):
        """All strategies must implement this method"""
        pass

# The Concrete Strategies
class FedExStrategy(ShippingStrategy):
    def calculate_cost(self, weight, distance):
        # FedEx: Flat $10 + $2 per kg + $0.5 per mile
        return 10 + (weight * 2) + (distance * 0.5)

class PostalStrategy(ShippingStrategy):
    def calculate_cost(self, weight, distance):
        # Postal: No flat fee, $1.5 per kg + $0.1 per mile
        return (weight * 1.5) + (distance * 0.1)

class UPSStrategy(ShippingStrategy):
    def calculate_cost(self, weight, distance):
        # UPS: Flat $20 + $1.0 per kg + $0.2 per mile
        return 20 + (weight * 1.0) + (distance * 0.2)

# The Context (The Order)
class Order:
    def __init__(self, weight, distance, strategy: ShippingStrategy):
        self.weight = weight
        self.distance = distance
        self.strategy = strategy  # This is the "brain" that can be swapped!

    def shipping_fee(self):
        # The Order doesn't know the math; it asks the Strategy
        return self.strategy.calculate_cost(self.weight, self.distance)


# HOW TO USE IT
# Initial choice: FedEx
my_order = Order(weight=5, distance=100, strategy=FedExStrategy())
print(f"FedEx Shipping: ${my_order.shipping_fee()}")


# Change strategy at runtime (User finds a cheaper option)
my_order.strategy = PostalStrategy()
print(f"Postal Shipping: ${my_order.shipping_fee()}")

# Change strategy to UPS
my_order.strategy = UPSStrategy()
print(f"UPS Shipping: ${my_order.shipping_fee()}")