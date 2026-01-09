class User:
    def __init__(self, is_authenticated):
        self.is_authenticated = is_authenticated

# its like a gift we are wrapping something do for more than 2 times

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

@login_required
@logger_decorator
def transfer_money(user, amount, recipient):
    # business logic for transferring money
    return f"Successfully transferred ${amount} to {recipient}"

user = User(is_authenticated=True)

print(view_balance(user))
print(transfer_money(user, 500, "Santosh"))

@logger_decorator
def add(a,b):
    # print("inside add function") // not a good practice 
    return a + b

print(f"Sum: {add(10, 20)}")    
