

from abc import ABC, abstractmethod

class User:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone


class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotifier(Notifier):
    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f"Email sent to {self.email}: {message}")

    
class SMSNotifier(Notifier):
    def __init__(self, phone):
        self.phone = phone

    def send(self, message):
        print(f"SMS sent to {self.phone}: {message}")


class NotifierFactory:
    _notifiers = {
        "email": EmailNotifier,
        "sms": SMSNotifier,
    }

    @classmethod
    def get_notifier(cls, channel, user):
        target_class = cls._notifiers.get(channel)

        if not target_class:
            raise ValueError(f"Invalid channel: {channel}")

        if channel == "email":
            return target_class(user.email)
        elif channel == "sms":
            return target_class(user.phone)


user = User(email="santosh@gmail.com", phone="+91-9999999999")
# Usage:
service = NotifierFactory.get_notifier(channel="sms", user=user)
service.send("Welcome aboard!")