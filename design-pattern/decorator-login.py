class User:
    def __init__(self, is_authenticated):
        self.is_authenticated = is_authenticated


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} completed.")
        return result
    return wrapper


def login_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            raise Exception("Access denied")
        return func(user, *args, **kwargs)
    return wrapper


@login_required
@logger_decorator
def view_balance(user):
    #business logic
    return "$1,000,000"

user = User(is_authenticated=True)

print(view_balance(user))