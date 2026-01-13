from abc import ABC, abstractmethod
import functools

# --- 1. Singleton: AppConfig ---
class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)
            # Configuration values
            cls._instance.app_name = "MegaCab"
            cls._instance.currency = "₹"
        return cls._instance


# --- 2. Strategy: Pricing ---
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, distance: float) -> float:
        pass

class NormalPricing(PricingStrategy):
    def calculate_fare(self, distance: float) -> float:
        return distance * 10

class SurgePricing(PricingStrategy):
    def calculate_fare(self, distance: float) -> float:
        return distance * 25


# --- 3. Strategy: Payment ---
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class UPIPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using UPI.")

class CardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Card.")

class WalletPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Wallet.")


# --- 4. Decorator: Logging and Authentication ---
def logger_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} completed.")
        return result
    return wrapper

def auth_decorator(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        # Simulated authentication check
        if not getattr(user, 'is_authenticated', False):
            print("[AUTH] User is not authenticated. Access Denied.")
            return None
        return func(user, *args, **kwargs)
    return wrapper


# --- 5. Domain / Context ---
class User:
    def __init__(self, name: str, is_authenticated: bool = True):
        self.name = name
        self.is_authenticated = is_authenticated

class BookingSystem:
    def __init__(self, pricing_strategy: PricingStrategy, payment_strategy: PaymentStrategy):
        self.config = AppConfig()
        self.pricing_strategy = pricing_strategy
        self.payment_strategy = payment_strategy

    @auth_decorator
    @logger_decorator
    def book_ride(self, user: User, distance: float):
        fare = self.pricing_strategy.calculate_fare(distance)
        print(f"Booking ride for {user.name} for {distance}km in {self.config.app_name}.")
        print(f"Total Fare: {self.config.currency}{fare}")
        
        # Payment stage
        self.payment_strategy.pay(fare)
        return fare


# --- 6. Usage ---
if __name__ == "__main__":
    # Initialize Configuration (Singleton)
    config = AppConfig()
    print(f"Welcome to {config.app_name} Booking System!")

    # Initial setup: Normal Pricing and UPI Payment
    user_harsh = User("Harsh", is_authenticated=True)
    system = BookingSystem(pricing_strategy=NormalPricing(), payment_strategy=UPIPayment())

    # Case 1: Normal Booking
    print("\n--- Testing Normal ride ---")
    system.book_ride(user_harsh, 10)

    # Case 2: Runtime Strategy Swap (Surge Pricing)
    print("\n--- Testing Surge ride ---")
    system.pricing_strategy = SurgePricing()
    system.book_ride(user_harsh, 10)

    # Case 3: Different Payment Method
    print("\n--- Testing Card Payment ---")
    system.payment_strategy = CardPayment()
    system.book_ride(user_harsh, 5)

    # Case 4: Unauthenticated User
    print("\n--- Testing Unauthenticated User ---")
    guest_user = User("Guest", is_authenticated=False)
    system.book_ride(guest_user, 15)
