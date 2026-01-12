from abc import ABC, abstractmethod
import functools

# --- 1. Singleton: AppConfig ---
class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppConfig, cls)
            
            cls._instance.app_name = "MegaCab"
            cls._instance.currency = "₹"
        return cls._instance

# -- 2. Stretgy: Pricing --
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, distance: float)-> float:
        pass
class NormalPricing(PricingStrategy):
    def calculate_fare(self, distance: float) -> float:
        return distance * 10
class SurgePricing(PricingStrategy):
    def calculate_fare(self, distance: float) -> float:
        return distance * 25

# -- 3 strategy: Payment --
class PaymetStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class UPIPayment(PaymetStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using UPI.")

class CardPayment(PaymetStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Card.")

class chequePayment(PaymetStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Cheque.")

class WalletPayment(PaymetStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Wallet.")

# === 4. Decorators--->
def logger_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
