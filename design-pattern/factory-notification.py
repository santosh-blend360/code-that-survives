from abc import ABC, abstractmethod


# Domain
class User:
    def __init__(self, email: str, phone: str, device_id: str = None):
        self.email = email
        self.phone = phone
        self.device_id = device_id


# Abstraction
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


# Implementations
class EmailNotifier(Notifier):
    def __init__(self, email: str):
        self.email = email

    def send(self, message: str) -> None:
        print(f"Email sent to {self.email}: {message}")


class PushNotifier(Notifier):
    def __init__(self, device_id: str):
        self.device_id = device_id

    def send(self, message: str) -> None:
        print(f"Push notification sent to {self.device_id}: {message}")


class SMSNotifier(Notifier):
    def __init__(self, phone: str):
        self.phone = phone

    def send(self, message: str) -> None:
        print(f"SMS sent to {self.phone}: {message}")


# Factory
class NotifierFactory:
    _notifiers = {
        "email": lambda user: EmailNotifier(user.email),
        "sms": lambda user: SMSNotifier(user.phone),
        "push": lambda user: PushNotifier(user.device_id),
    }

    @classmethod
    def get_notifier(cls, channel: str, user: User) -> Notifier:
        creator = cls._notifiers.get(channel)

        if not creator:
            raise ValueError(f"Invalid channel: {channel}")

        return creator(user)


# Usage
if __name__ == "__main__":
    user = User(email="santosh@gmail.com", phone="+91-9999999999", device_id="device_123")

    notifier = NotifierFactory.get_notifier("sms", user)
    notifier.send("Welcome aboard!")

    push_notifier = NotifierFactory.get_notifier("push", user)
    push_notifier.send("Check out our new feature!")
