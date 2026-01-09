
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



def notify(user, msg, channel):
    if channel == "email":
        notifier = EmailNotifier(user.email)
        notifier.send(msg)
    elif channel == "sms":
        notifier = SMSNotifier(user.phone)
        notifier.send(msg)
